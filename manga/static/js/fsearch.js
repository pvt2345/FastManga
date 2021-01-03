(function($){
    $.fn.fsearch = function(){
      var $searchInput = $(this);
      $searchInput.after('<div id="SearchResult"></div>');
      $resultDiv = $('#SearchResult');
      //$searchInput.focus();
      $searchInput.addClass('searchi');
      $resultDiv.html("<ul></ul><div id='search-footer' class='searchf'></div>");
      //value old
      $old = '';
      var timesearchstory = null;
      
      $searchInput.keyup(function(e) {
      var q=$(this).val().trim();
        if(q != '') { 
            if(q == $old || q.length < 3)
                return;
            
            if(q == $old && e.keyCode != 13){
                if(e.keyCode == 27) {
                    $searchInput.val('');
                    $resultDiv.hide();
                }
                return;
            }
            $old = q;
            
            var current_index = $('.selected').index(),
            $options = $resultDiv.find('.option'),
            items_total = $options.length;
            
            $resultDiv.fadeIn();
            $resultDiv.find('#search-footer').html("<img src='"+ baseurljs +"themes/hm/images/loading.gif' alt='Loading...'/>");
            if (timesearchstory != null) {
                clearTimeout(timesearchstory);
            }
            timesearchstory = setTimeout(function() {
                timesearchstory = null;
                $.ajax({
                    contentType : "application/x-www-form-urlencoded; charset=UTF-8",
                    url: baseurljs + 'getstorysearchjson',
                    type: 'POST',
                    data: "searchword=" + change_alias(q),
                    dataType: "json",
                    success: function(jsonResult){
                        var str='';
                        for(var i=0; i<jsonResult.length;i++) {
                            str += '<a href="' + linkstory(jsonResult[i].id_encode) + '"><li onmouseover="fmouseover(' + jsonResult[i].id + ');" id=' + jsonResult[i].id + ' class="option item">';
                            str += '<img class="item_image" src="'+jsonResult[i].image+'" />';
                            str += '<div class="item_panel_right">';
                            str += '<span class="item_name">' + jsonResult[i].name + '</span>';
                            if(jsonResult[i].author.trim() != '') {
                                str += '<span class="item_author">'+ jsonResult[i].author +'</span>';
                            }
                            if(jsonResult[i].lastchapter.trim() != '') {
                                str += '<span class="item_chapter" >'+ jsonResult[i].lastchapter +'</span>';
                            }
                            str += '</div></li></a>';
                        }
                        $resultDiv.find('ul').empty().prepend(str);
    
                        $url_search_tam = baseurljs + 'search/' + change_alias(q);
                        $search_panel = "<p><a href='"+ $url_search_tam +"' style='color: #ff530d;' >Click here to view all results.</a></p>";
                        if(jsonResult.length > 0)
                            $resultDiv.find('div#search-footer').html("<p>Display first "+ jsonResult.length +" results.</p>" + $search_panel);
                        else
                            $resultDiv.find('div#search-footer').html("<p>No matches found. Try a different search...</p>" + $search_panel);
                    }          
                });
            }, 1000);
        }
        else{
            //Hide the results if there is no search input
            $resultDiv.hide();
        }
    });
    
        // Hide the search result when clicked outside
        jQuery(document).on("click", function(e) { 
            var $clicked = $(e.target);
            if ($clicked.hasClass("searchi") || $clicked.hasClass("searchf")) { }
            else{
                $resultDiv.fadeOut(); 
            }
        });
        
        // Show previous search results when the search box is clicked
      
        $searchInput.click(function(){
            var q=$(this).val();
            if(q != '')
            { 
                $resultDiv.fadeIn();
            }
        });
    };
    })(jQuery);
    
    $(document).ready(function() {
        var chk_search_story = document.getElementById('search-story');
        if (chk_search_story) {
    
            $('#search-story').fsearch();
    
            jQuery(function($) {
                jQuery('#search-story').keypress(function( event ) {
                    if ( event.which == 13 ) {
                        window.location = $search_address + change_alias(chk_search_story.value);
                    }
                })
            });
            
            $(".pn-search-btn").click(function() {
                window.location = $search_address + change_alias(chk_search_story.value);
            });
        };
    });
    
    function fmouseover(id) {
         $(".option").removeClass("selected");
        document.getElementById(id).className += " selected";
    }
    
    function linkstory(nameunsigned) {
        if(nameunsigned != null) {
            url = baseurljs + "manga/" + nameunsigned;
            return url;
        }
    }