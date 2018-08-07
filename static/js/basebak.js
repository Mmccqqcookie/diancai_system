/**
 * Created by ServerSupporter-03 on 2018/7/25.
 */

$(function(){
    sousuo_tijiao();
    onload_img();
});

function sousuo_tijiao(){
    $('.sousuo_tijiao').click(function (){
        var search_val = $('#id_search').val();
        if(search_val){
            $.ajax({
                url: '/search_keyword',
                type:'GET',
                data : {'keyword':search_val},
                success:function(data){
                    if(data.data){
                        var targ = $('.detail');
                        targ.empty();
                        data.data.forEach(function(item){
                            var creat_li = $('<li>');
                            var creat_div = $('<div>');
                            var creat_img = $('<img>');
                            var creat_h5 = $('<h4>');
                            var creat_p1 = document.createElement('p');
                            creat_a.attr({'href':item.url,'target':'_blank'});
                            creat_img.attr({src:item.img,alt:item.title});
                            creat_a.append(creat_img);
                            creat_h5.text(item.title);
                            creat_p1.innerText = item.side_dish;
                            creat_li.append(creat_a);
                            creat_li.append(creat_h5);
                            creat_li.append(creat_p1);
                            creat_li.append(item.stats);

                            targ.append(creat_li);
                        })
                    }
                }
            })
        }

    })
}


function onload_img() {
    $('img').bind('onerror',function load_img_num(){
        var src = $(this).src;
        console.log(src,1111);
        $(this).attr('src',src)
    })

}