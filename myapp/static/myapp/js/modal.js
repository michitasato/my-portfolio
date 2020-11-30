$(function(){

   //いいえを選んだ処理
    $('.js-modal-open').on('click',function(){
        $('.js-modal').fadeIn();
        return false;
    });

    $('.js-modal-close').on('click',function(){
        $('.js-modal').fadeOut();
        return false;
    });

    //はいを選んだ処理
    $('.fadeIn').on('click',function(){
        $('.yes-box').fadeIn();
        return false;
    });

});