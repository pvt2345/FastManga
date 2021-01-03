$(document).ready(function() {
    $('.header-mobile-menu').click(function() {
        $('.header-menu').toggle();
    });
    
    $("#owl-slider").owlCarousel({
        autoPlay : true,
        items :8,
        autoheight: true,
        lazyLoad : true,
        navigation : true,
        pagination : false,
        navigationText : ["",""],
        itemsDesktop : [1160,5],
        itemsDesktopSmall : [992,4],
        itemsTablet: [768,3],
        itemsMobile : [479,2],
        slideSpeed : 200,
    });
    
    $('body').append('<div id="top">Back to Top</div>');
    $(window).scroll(function(){if($(window).scrollTop()!=0){$('#top').fadeIn();}else{$('#top').fadeOut();}});$('#top').click(function(){$('body,html').animate({scrollTop:0},300);});
    
    $('.notification-popup').click(function(){
        $('.notification-popup').hide();
    });
    $('.notification-close').click(function(){
        $('.notification-popup').hide();
    });
});

function show_notication_popup(content) {
    $(".notification-content").html(content);
    $('.notification-popup').show();
}

function change_alias(alias) {
    var str = alias;
    str= str.toLowerCase(); 
    str= str.replace(/Ã |Ã¡|áº¡|áº£|Ã£|Ã¢|áº§|áº¥|áº­|áº©|áº«|Äƒ|áº±|áº¯|áº·|áº³|áºµ/g,"a"); 
    str= str.replace(/Ã¨|Ã©|áº¹|áº»|áº½|Ãª|á»|áº¿|á»‡|á»ƒ|á»…/g,"e"); 
    str= str.replace(/Ã¬|Ã­|á»‹|á»‰|Ä©/g,"i"); 
    str= str.replace(/Ã²|Ã³|á»|á»|Ãµ|Ã´|á»“|á»‘|á»™|á»•|á»—|Æ¡|á»|á»›|á»£|á»Ÿ|á»¡/g,"o"); 
    str= str.replace(/Ã¹|Ãº|á»¥|á»§|Å©|Æ°|á»«|á»©|á»±|á»­|á»¯/g,"u"); 
    str= str.replace(/á»³|Ã½|á»µ|á»·|á»¹/g,"y"); 
    str= str.replace(/Ä‘/g,"d");
    str= str.replace(/ /g,"_");
    /* str= str.replace(/!|@|%|\^|\*|\(|\)|\+|\=|\<|\>|\?|\/|,|\.|\:|\;|\'| |\"|\&|\#|\[|\]|~|-|$|_/g,"_"); */
    /* str= str.replace(/[^0-9a-zÃ Ã¡áº¡áº£Ã£Ã¢áº§áº¥áº­áº©áº«Äƒáº±áº¯áº·áº³áºµÃ¨Ã©áº¹áº»áº½Ãªá»áº¿á»‡á»ƒá»…Ã¬Ã­á»‹á»‰Ä©Ã²Ã³á»á»ÃµÃ´á»“á»‘á»™á»•á»—Æ¡á»á»›á»£á»Ÿá»¡Ã¹Ãºá»¥á»§Å©Æ°á»«á»©á»±á»­á»¯á»³Ã½á»µá»·á»¹Ä‘\s]/gi, '_'); */
    str= str.replace(/[^0-9a-z\s]/gi, '_');
    str= str.replace(/_+_/g,"_"); /* __ to _ */
    str= str.replace(/^\_+|\_+$/g,""); 

    return str;
}

function trim (s, c) {
  if (c === "]") c = "\\]";
  if (c === "\\") c = "\\\\";
  return s.replace(new RegExp(
    "^[" + c + "]+|[" + c + "]+$", "g"
  ), "");
}

/* handle comment facebook */
$(document).ready(function() {
    $('.fb-comment-title').click(function() {
        if(!$(".fb-comment-title").hasClass( "fb-comment-title-show")) {
            fc_fb_comment_load('show');
        }
        else {
            fc_fb_comment_load('hide');
        }
    });
});

$(document).ready(function() {
    if ($.cookie("panel-fb-comment")) {
        cookie_panel_fb_comment = $.cookie("panel-fb-comment");
        if(cookie_panel_fb_comment == 'fb-comment-title-show') {
            fc_fb_comment_load('show');
        }
        else if(cookie_panel_fb_comment == 'fb-comment-title-hidden') {
            fc_fb_comment_load('hide');
        }
    } else {
        fc_fb_comment_load('show');
    }
});

var load_comment = 0;
function fc_fb_comment_load(result) { /* load - show - hide */
    if (!$('.fb-comments-content').length) {
        return;
    }
    
    load_comment++;

    if(result == 'load') {
        cookie_panel_fb_comment = $.cookie("panel-fb-comment");
        if(cookie_panel_fb_comment == 'fb-comment-title-hidden') {
            return;
        }
    }

    if(result == 'hide') {
        $(".fb-comments-content").html('');
    
        $(".fb-comment-title").removeClass("fb-comment-title-show");
        $(".fb-comment-title").addClass("fb-comment-title-hidden");

        var date = new Date();
        date.setTime(date.getTime() + (365 * 24 * 60 * 60 * 1000));
        $.cookie("panel-fb-comment", "fb-comment-title-hidden", {expires: date, path: "/"});
        return;
    }
    
    $(".fb-comment-title").addClass("fb-comment-title-show");
    $(".fb-comment-title").removeClass("fb-comment-title-hidden");
    
    var url_comment = $(".fb-comments-content").attr('id');
    url_comment = atob(url_comment);

    var str_comment = '<div class="fb-comments" data-href="' + url_comment + '" data-width="100%" data-numposts="10" data-colorscheme="light"></div>';
    if ($.cookie('changer-mode-dark') && $.cookie('changer-mode-dark') == 'yes') {
        str_comment = '<div class="fb-comments" data-href="' + url_comment + '" data-width="100%" data-numposts="10" data-colorscheme="dark"></div>';
    }
    
    $(".fb-comments-content").html(str_comment);
    if (load_comment > 1) {
        FB.XFBML.parse($('.commentsfab').get(0),function(){ $(".FB_Loader").remove(); });
    }
    
    var date = new Date();
    date.setTime(date.getTime() + (365 * 24 * 60 * 60 * 1000));
    if(result == 'show') {
        var date = new Date();
        date.setTime(date.getTime() + (365 * 24 * 60 * 60 * 1000));
        $.cookie("panel-fb-comment", "fb-comment-title-show", {expires: date, path: "/"});
    }
}