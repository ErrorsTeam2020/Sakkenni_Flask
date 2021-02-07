/* start home page */ 
$(document).ready(function(){
    $(window).on('scroll' , function(){
        var sc = $(window).scrollTop()
        console.log(sc)
        if(sc >= 200){
            $('#sec-00').animate({height:'487px'    
            },800)
            $('header').animate({height:'70px'},600)
            $('header').css({'backgroundColor':'#092138f2'})
            $('#logo').animate({width:'90px'},600)
            $('ul').css({'transform':'translate(40px,10px)'},600) 
            $('#search-box #tap').hide(600)
            $('#search-box').css({'position':'fixed',
                                  'zIndex':'9999',
                                  'top':'65px',
                                  'backgroundColor':'#f1f1f1',
                                  'border':'1px',
                                  'borderRadius':'0px'
            })
            $('#search-box').animate({width:'100%',
                                      height:'70px',
                                      marginRight:'0',
                                      right:'0px'
            },600)
            $('#search-box').animate({'paddingTop':'20px'},600)
            $('#search-bt').css({'display':'inline',
                                 'transform':'translate(-10px,3px)'})
            $('#search-bt').animate({width:'150px',
                                    height:'46px',
                                    margin:'0px',
            },600)
            $('.selection').css({'background-color':'#c3c3c3'})
            $('.selection').animate({width:'230px',
                                     height:'45px',
                                     margin:'5px 20px 5px 10px '
            },800) 
           $('#caption').animate({top:'230px'},200)
           $('#cap-paragraph').animate({top:'280px'},200)
           $('#disc-div > div:nth-of-type(1)').fadeIn();
           $('#disc-div > div:nth-of-type(1)').css({'display':'inline-block'});
           $('#disc-div > div:nth-of-type(2)').fadeIn();
           $('#disc-div > div:nth-of-type(2)').css({'display':'inline-block'});
           $('#disc-div > div:nth-of-type(3)').fadeIn();
           $('#disc-div > div:nth-of-type(3)').css({'display':'inline-block'});
        }
        
        if(sc >= 450){
           $('#sec-02').animate({height:'600px'},800)
           $('#slider-div,#advs-div').animate({margin:'0px'}).fadeIn(800)
           }
        $(".fa-angle-right").click(function(){
            $('.advs-div > div:nth-of-type(1)').hide()
            $('.advs-div > div:nth-of-type(2)').show()
        })
        $(".fa-angle-left").click(function(){
            $('.advs-div > div:nth-of-type(2)').hide()
            $('.advs-div > div:nth-of-type(1)').show()
        })
        if(sc > 1034 ){
            $('#sec-03').animate({height:'480px'},800)
            $('#apt-container').animate({margin:'70px 20px 0px 0px'},600)
            $('#apt-container').show(800)
        }
    })
    $('#c-owner').click(function(){
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

