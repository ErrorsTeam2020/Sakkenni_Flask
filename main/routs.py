from flask import Flask, render_template, url_for, redirect, flash
from main.forms import LoginForm, SignupForm, flatp
from main import app, db, bcrypt
from main.models import User, Flat
from flask_login import login_user, current_user, logout_user


@app.route('/')
@app.route('/home')
def home():
    flat = Flat.query.all()
    file = url_for('static', filename='hg/last2.css')
    return render_template('page3.2.html', file=file, flat=flat)


@app.route('/login', methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        Pass = bcrypt.check_password_hash(user.password, form.password.data)
        if user and Pass:
            login_user(user)
            flash('تم تسجيل الدخول بنجاح', 'success')
            return redirect(url_for('home'))
        else:
            flash('فشل تسجيل الدخول اعد المحاوله', 'danger')

    file = url_for('static', filename='css/main.css')
    return render_template('login.html', file=file, form=form)


@app.route('/profile')
def profile():
    file = url_for('static', filename='profile/profile3.css')
    return render_template('profile.html', file=file)


@app.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(fullname=form.fullName.data, username=form.username.data, address=form.address.data,
                    governorate=form.gov.data, email=form.email.data, password=hashed_password,
                    user_class=form.user_class.data, gender=form.gender.data, phone=form.phone.data,
                    nat_id=form.nat_id.data)
        db.session.add(user)
        db.session.commit()

        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))

    file = url_for('static', filename='css/main.css')
    return render_template('Account.html', file=file, title="إنشاء حساب", form=form)


@app.route('/newad', methods=["GET", "POST"])
def ad():
    form = flatp()
    if form.validate_on_submit():
        flat = Flat(title=form.title.data, address=form.address.data, description=form.description.data,
                    governorate=form.gov.data, price=form.price.data, student_num=form.student_no.data,
                    room_num=form.room_no.data,author=current_user)
        db.session.add(flat)
        db.session.commit()
        return redirect(url_for('home'))

    file = url_for('static', filename='css/main.css')
    return render_template('ad.html', file=file, title="إنشاء حساب",form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
