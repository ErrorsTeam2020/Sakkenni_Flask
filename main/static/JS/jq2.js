/* start home page */ 
$('#Home').addClass('active')
$('#Home').css({'color':'#13386f'})
$('#Home').click(function(){
    $(this).addClass('active')
    $('#Noti').removeClass('active')
    $('#profile-icon').removeClass('active')
    $('#settings').removeClass('active')
    $('#profile-icon').css({'color':'#6a6e72'})
    $('#settings').css({'color':'#6a6e72'})
    
})
/* notification slid down */
$('#ntf-bt').click(function(){
    $('#ntf-sldown').slideToggle()
})
$('#ntf-icon').click(function(){
    $('#ntf-sldown').slideToggle()
})
$('#sett-bt').click(function(){
    $('#sett-sldown').slideToggle(200)
})
$('#sett-div i').click(function(){
    $('#sett-sldown').slideToggle(200)

    $('#cn-owner').click(function(){
        $('#popup').fadeIn(300)
    })
    $('#popup').click(function(){
    $(this).fadeOut()
})
    $('#popup #popup-info').click(function(e){
        e.stopPropagation()
    })
    $('#popup-info button').click(function(e){
        e.preventDefault();
        $('#popup button').parent().parent('#popup').fadeOut(300);
    })
})

