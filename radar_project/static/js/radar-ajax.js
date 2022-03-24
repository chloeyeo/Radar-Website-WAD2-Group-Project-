$(document).ready(function() { 

    $(".like_post_btn").click(function(){
        var getPostId;
        getPostId = $(this).attr('post-id');
        $.get('/radar/like_post/', {'post_id': getPostId},
        function(data){
            var name = data.post_id
            var selector = document.getElementsByName(name);
            
            $(selector).html("Likes : " + data.total_likes);

            // why isn't the button updating
            if(data.liked){
                $(this).css("Liked");
            }else{
                $(this).html("Like");
            }
        }
        );
    });

    $("#login_form").on("submit", function(){
        // adding some ajax functionality of login form
    })

    $("#sign-up-form").on("submit", function(){
        // adding some ajax functionality of signup form
    })

});
