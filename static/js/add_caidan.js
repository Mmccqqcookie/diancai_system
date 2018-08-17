/**
 * Created by ServerSupporter-03 on 2018/8/1.
 */
$(function(){
    button_click();
    Add_tijiao_dish();
    Add_cate_dish_menu();
    fixed_button_on_click();

});

function button_click() {
    $('.form-group button').click(function () {
        var category_url = $(this).attr('category_url');
        $.ajax({
            url:category_url,
            type: "GET",
            data:'',
            success:function (data) {
                 if(data.status){
                        var targ = $('.detail');
                        targ.empty();
                        $('.add_quxiao button').removeClass('hider');
                        $('.add_tijiao_caidan').val(category_url);
                        data.data.forEach(function(item){
                            var creat_li = $('<li>');
                            var creat_a = $('<a>');
                            var creat_img = $('<img>');
                            var creat_h5 = $('<h4>');
                            var creat_button1 = $('<button>');
                            var creat_button2 = $('<button>');
                            var creat_p1 = document.createElement('p');
                            creat_a.attr({'href':item.url,'target':'_blank'});
                            creat_img.attr({src:item.img,alt:item.title});
                            creat_a.append(creat_img);
                            creat_h5.text(item.title);
                            creat_button1.text('加入菜单');
                            creat_button1.click(function () {
                                $(this).addClass('add-menu');
                                $(this).text('已选择');
                                $(this).val(1);
                                $(this).css({'background-color': '#F2F2F2', 'cursor': 'not-allowed', "color": 'black'});
                            });
                            creat_button2.text('移除菜单');
                             creat_button2.click(function () {
                                 $(this).siblings().filter('.add-menu').text('加入菜单');
                                  $(this).siblings().filter('.add-menu').removeAttr('value');
                                 $(this).siblings().filter('.add-menu').css({'background-color': '#337ab7', 'cursor': 'pointer', "color": 'white'})
                            });
                            creat_p1.innerText = item.side_dish;
                            creat_li.append(creat_a);
                            creat_li.append(creat_button1);
                            creat_li.append(creat_button2);
                            creat_li.append(creat_h5);
                            creat_li.append(creat_p1);
                            creat_li.append(item.stats);
                            targ.append(creat_li);
                        });
                        $('.detail li button').addClass('blue');
                        $('nav[aria-label="Page navigation"]').removeClass('hider');
                        $('nav ul li').removeClass('active');
                        $('nav ul li').first().addClass('active');
                        var nav_ul_li_leth =  $('nav ul li').length;
                        for(var i=0;i<nav_ul_li_leth+1;i++){
                            if(i == 0){
                                $('nav ul li').eq(i).children().attr('href',category_url)
                            }else{
                                $('nav ul li').eq(i).children().attr('href',category_url +'?page=' + (i+1))
                            }
                        }
                        $('#display_caidan')[0].scrollIntoView(true);

                    }
            }
        })
    })
}

function Add_tijiao_dish() {
    $('.add_tijiao_caidan').click(function () {
        var add_tijiao_addr = $(this).val();

        var dish_val = $('button[category_url="' +add_tijiao_addr + '"]').parent().next().children().val() + ' ';

        $('.display-caidan .detail li button[value="1"]').each(function () {
            var dish = $(this).siblings().filter('h4').text();
            var reg = new RegExp(dish);
            if(reg.test(dish_val) == false){
                 dish_val +=  dish + ' ';
            }else{
                return true;
            }
        });
        $('button[category_url="' +add_tijiao_addr + '"]').parent().next().children().val(dish_val);
    })
}


function Add_cate_dish_menu() {
    $('.add_cate_tijiao').click(function () {
        var user = $('.click_login_email').text();
        var jiachangcai = $('.jiachangcai').children().val();
        var xiafancai = $('.xiafancai').children().val();
        var sucai = $('.sucai').children().val();
        var dayudarou = $('.dayudarou').children().val();
        var tanggeng = $('.tanggeng').children().val();
        var liangcai = $('.liangcai').children().val();

        $.ajax({
            url:'/add_dish_menu',
            type:'POST',
            data:{'user':user,'jiachangcai':jiachangcai,'xiafancai':xiafancai,'sucai':sucai,
            'dayudarou':dayudarou,'tanggeng':tanggeng,'liangcai':liangcai},
            success:function (data) {
                if(data.status==false){
                    $('.data-message').text(data.message);
                    $('.data-message').css({'color':'red'})
                }else{
                    $('.data-message').text(data.message);
                    $('.data-message').css({'color':'green'})
                }
                setTimeout(function () {
                    $('.data-message').text('')
                },8000)
            }
        })
    })
}


function fixed_button_on_click() {
    $('.black-index').click(function () {
        window.location.href = '/';
    });
    $('.black-dish').click(function () {
        $('#display_caidan')[0].scrollIntoView(true);
    });
    $('.black-top').click(function () {
        $('.pg_body')[0].scrollIntoView(true);
    });
    $('.qingchu').click(function () {
        window.location.href = '/'
    })

}