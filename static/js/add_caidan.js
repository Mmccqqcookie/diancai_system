/**
 * Created by ServerSupporter-03 on 2018/8/1.
 */
$(function(){
    button_click();

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


    })
}