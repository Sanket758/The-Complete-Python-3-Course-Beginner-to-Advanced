

$(document).ready(function(){
    console.log("loaded");
    $.material.init();

    $(document).on("submit", "#register-form", function(e){
        e.preventDefault()
        var form = $('#register-form').serialize();
        $.ajax({
            url : '/postregistration',
            type: 'POST',
            data: form,
            success: function(response){
                console.log(response);
            }
        });
    });

    $(document).on("submit", "#login-form", function(e){
        e.preventDefault()

        var form = $(this).serialize();
        $.ajax({
           url: '/check-login',
           type: 'POST',
           data: form ,
           success: function(resp){
               if(resp == 'error'){
                alert('Could not login in');
               }else{
                console.log("logged in as",resp);
                window.location.href = '/';
               }
           }
        });
    });

    $(document).on('click', '#logout-link',function(e){
        e.preventDefault()
        $.ajax({
            url: '/logout',
            type: 'GET',
            success: function(res){
                if(res == 'success'){
                    window.location.href = '/login';
                }else{
                    alert('something gone wrong!');
                }
            }
        });
    });

    $(document).on("submit", "#post-activity", function(e){
        e.preventDefault()
        var form = $('#post-activity').serialize();
        $.ajax({
            url: '/post-activity',
            type: 'POST',
            data: form,
            success: function(res){
                console.log(res);
            }
        });
    });

});
