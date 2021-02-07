$('#student').click(function(){
    $(this).css({'backgroundColor':'#092138e8','boxShadow':'5px 5px 10px inset #000000','color':'white'})
    $('#owner').css({'backgroundColor':'#ababab','color':'#d2d1d1','boxShadow':'none'})
    $('#user-university').fadeIn();
})
$('#owner').click(function(){
    $(this).css({'backgroundColor':'#092138e8','boxShadow':'5px 5px 20px inset #000000','color':'white'})
    $('#student').css({'backgroundColor':'#ababab','color':'#d2d1d1','boxShadow':'none'})
    $('#user-university').fadeOut(200);
})