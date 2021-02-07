from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField, BooleanField, SubmitField, ValidationError, \
    RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from main.models import User, Flat


class SignupForm(FlaskForm):
    fullName = StringField('الاسم بالكامل', validators=[DataRequired(), Length(min=5, max=50)])
    username = StringField('اسم المستخدم', validators=[DataRequired(), Length(min=2, max=20)])
    address = StringField('العنوان', validators=[DataRequired(), Length(min=2, max=20)])
    # faculty = StringField('كلية', validators=[DataRequired(), Length(min=2, max=20)])
    # university = StringField('جامعة', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('البريد الالكتروني', validators=[DataRequired(), Email()])
    password = PasswordField('كلمة المرور', validators=[DataRequired()])
    confirm_password = PasswordField('تأكيد كلمة المرور', validators=[DataRequired(), EqualTo('password')])

    nat_id = IntegerField('الرقم القومي', validators=[DataRequired()])
    phone = IntegerField('رقم الهاتف', validators=[DataRequired()])
    gov = SelectField('المحافظة',
                      choices=['Alexandria', ' Aswan', 'Asyut', ' Beheira', ' Beni Suef', 'Cairo', 'Dakahlia',
                               'Damietta', 'Faiyum', 'Gharbia', 'Giza', 'Ismailia', 'Kafr El Sheikh', 'Luxor', 'Matruh',
                               'Minya', 'Monufia', 'New Valley', 'North Sinai', 'Port Said', '	Qalyubia', 'Sharqia',
                               'Sohag', ' South Sinai', ' Suez'])

    user_class = SelectField('تسجيل كـ', choices=['صاحب عقار', 'طالب'])
    gender = SelectField('النوع', choices=['male', 'female'])
    submit = SubmitField('تأكيد')

    def validate_nat_id(self, nat_id):
        user = User.query.filter_by(nat_id=nat_id.data).first()
        if user:
            raise ValidationError("خطأ! , الرقم القومي مستخدم من قبل")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("خطأ! , اسم المستخدم مستخدم من قبل")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("خطأ! , البريد الالكتروني مستخدم من قبل")


class LoginForm(FlaskForm):
    email = StringField('البريد الالكتروني', validators=[DataRequired(), Email()])
    password = PasswordField('كلمة المرور', validators=[DataRequired()])
    remember = BooleanField('تذكرني')
    submit = SubmitField('تسجيل دخول')


class flatp(FlaskForm):
    title = StringField('اسم الاعلان', validators=[DataRequired(), Length(min=0, max=80)])
    gov = SelectField('المحافظة',
                      choices=['القاهرة', 'الإسكندرية', 'المنوفية', 'الإسماعيلية', 'أسوان', 'أسيوط', 'الأقصر',
                               'البحر الأحمر', 'البحيرة', 'بني سويف'
                          , 'بورسعيد', 'جنوب سيناء', 'البحيرة', 'الدقهلية', 'دمياط', 'سوهاج', 'السويس', 'الشرقية',
                               'الغربية', 'الفيوم'
                          , 'القليوبية', 'قنا', 'كفرالشيخ', 'شمال سيناء', 'مطروح', 'المنيا', 'الوادي الجديد'])
    address = StringField('العنوان', validators=[DataRequired()])
    price = IntegerField('سعر الايجار الشهري', validators=[DataRequired()])
    description = StringField('الوصف التفصيلي', validators=[DataRequired()])
    room_no = IntegerField('عدد الغرف', validators=[DataRequired()])
    student_no = IntegerField('عدد الطلبه', validators=[DataRequired()])
    submit = SubmitField('نشر الاعلان')
