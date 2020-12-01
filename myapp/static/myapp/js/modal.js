$(function(){

   //いいえを選んだ処理
    $('.js-modal-open').on('click',function(){
        $('.js-modal').fadeIn();
        return false;
    });

    //閉じる
    $('.js-modal-close').on('click',function(){
        $('.js-modal').fadeOut();
        return false;
    });

    //はいを選んだ処理
    $('.fadeIn').on('click',function(){
        $('.yes-modal').fadeIn();
        return false;
    });
    //閉じる
    $('.close-btn').on('click',function(){
        $('.yes-modal').fadeOut();
        return false;
    });




});