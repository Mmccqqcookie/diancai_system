/**
 * Created by ServerSupporter-03 on 2018/7/25.
 */

$(function(){
    click_login_logout();
    quxiao_click();
    get_yanzhenma();
    resgistr();
    login_on();
    display_login_menu();
    keyup_submit_login_resgistr();

});

function click_login_logout() {
    $('.click-login,.click-zhuce').click(function () {
        $('.zhezhaoceng').removeClass('hider');
        $('.login_logout').removeClass('hider');
    })
}

function quxiao_click() {
    $('.goback').click(function () {
        $('.login_logout input').val('');
        $('.zhezhaoceng').addClass('hider');
        $('.login_logout').addClass('hider');
    })
}

function check_email_vaild(reglog,email) {
    var regx = /@/;
    var pattr = /^\w+@\w+\.(com|cn|gov)$/;
    if (email.search(regx) != -1 && pattr.test(email) == true){

    }else{
        if (reglog){
            $('.zhuce_error').text('邮箱格式不正确');
            return false;
        }else{
            $('.login_error').text('邮箱格式不正确');
            return false;
        }


    }
}
function timekeeping(){
    $('.get-yanzhenma').attr("disabled", true);
    var interval=setInterval(function(){
     total=$.cookie("total");
     $('.get-yanzhenma').css({'background-color':'#F2F2F2','cursor':'not-allowed',"color":'black'});
     $('.get-yanzhenma').text('请等待'+total+'秒');
     total--;
     if(total==0){
     clearInterval(interval);
     total=$.cookie("total",total, { expires: -1 });
     $('.get-yanzhenma').text('重新获取');
     $('.get-yanzhenma').css({'background-color':'#337ab7','cursor':'pointer',"color":'white'});
     $('.get-yanzhenma').attr("disabled", false);
     }else{
     $.cookie("total",total);
     }
    },1000);
   }
function get_yanzhenma() {
    $('.get-yanzhenma').click(function () {
         var email = $('.login_logout .zhuce input[name="email"]').val();
    if(email){
        var check_emailvalid = check_email_vaild(true,email);
        if(check_emailvalid == false){
            return false;
        }else{
            $('.zhuce_error').text('');
            $.ajax({
                url:'/send_email_code',
                type: 'POST',
                data:{'email':email},
                success:function (data) {
                    if (data.status){
                        $.cookie("total",60);
                        if($.cookie("total")!=undefined&&$.cookie("total")!='NaN'&&$.cookie("total")!='null'){//cookie存在倒计时
                            timekeeping();
                            $.cookie('code',data.code)
                        }else{
                            $('#btn').attr("disabled", false);
                        }
                    }else{
                        $('.zhuce_error').text(data.message)
                    }
                }
            })
        }
    }else{
        $('.zhuce_error').text('* 邮箱不能为空')
    }
    })
}
function zhuce() {
    var email = $('.login_logout .zhuce input[name="email"]').val();
        var password = $('.login_logout .zhuce input[name="password"]').val();
        var yanzhenma = $('.login_logout .zhuce input[name="yanzhenma"]').val();
        if (email){
            var check_emailvaild = check_email_vaild(true,email);
            if(check_emailvaild == false){
                return false;
            }
            if(password){
                if (yanzhenma){
                    $('.zhuce_error').text('');
                    var code = $.cookie('code');
                    if (yanzhenma == code){
                        $.ajax({
                        url:'/resgistr',
                        type:'POST',
                        data:{'email':email,'password':password},
                        success:function (data) {
                            if(data.status){
                                $('.login_logout input').val('');
                                $('.zhezhaoceng').addClass('hider');
                                $('.login_logout').addClass('hider');
                            }
                        }
                    })
                    }else{
                         $('.zhuce_error').text('验证码输入有误')
                    }
                }else{
                    $('.zhuce_error').text('请输入验证码');
                    return false;
                }
            }else{
                $('.zhuce_error').text('请输入密码');
                return false;
            }
        }else{
            $('.zhuce_error').text('请输入邮箱');
            return false;
        }
}
function resgistr() {
    $('.registr').click(function(){
        zhuce();
    })
}
function keyup_submit_login_resgistr() {

    $('input[name="yanzhenma"]').keypress(function(event){
        if(event.keyCode == "13") {
            zhuce();
     }
    });
     $('input[name="password"]').keypress(function(event){
        if(event.keyCode == "13") {
            login();
     }
    })

}
function login() {
    var email = $('.login_logout .login input[name="email"]').val();
        var password = $('.login_logout .login input[name="password"]').val();
        if (email){
            var check_emailvaild = check_email_vaild(false,email);
            if(check_emailvaild == false){
                return false;
            }
            if(password){
                $('.login_error').text('');
                $.ajax({
                    url:'/login',
                    type:'POST',
                    data:{'email':email,'password':password},
                    success:function (data) {
                        if(!data.status){
                            $('.login_error').text(data.message);
                        }else{
                            window.location.reload('/index')
                        }
                    }

                })
            }else{
                $('.login_error').text('请输入密码')
            }
        }else{
            $('.login_error').text('邮箱不能为空')
        }
}

function login_on() {
    $('.login-on').click(function () {
        login();
})
}


function display_login_menu() {
    $('.user_menu').click(function () {
        if($('.login-menud').hasClass('hider')){
            $('.login-menud').removeClass('hider');
        }else{
            $('.login-menud').addClass('hider');
        }

    })
}

