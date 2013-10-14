window.addEvent('domready', function(){
    var send_comment = $('send_comment');
    if (send_comment) {
        send_comment.addEvent('click', function(e){
             e.stop();
             var comment_data = $('comment_form').toQueryString();
             var blog_id = $('hidden_blog_id').get('name');
             var ajaxRequest = new Request({ 
                 url: '/blog/comment/add/'+blog_id+'/',
                 method: 'POST',
                 data: comment_data,
                 onSuccess: function(){
                     console.log('You have successfully sent the Message');
                 }
//                  onFailure: function(){
//                      console.log('error :'+ data);
//                  }

             }); 
             ajaxRequest.send(); 
	     }); 
        // $('submit_form').addEvent('click', function(e){
        //     e.stop();
        //     var form_data = $('form_experienced').toQueryString();
        //     console.log('data'+form_data);
        //     var ajaxRequest = new Request({ 
        //         url: '/careers_experienced',
        //         method: 'POST',
        //         data: form_data,
        //         onSuccess: function(){
        //             console.log('You have successfully sent the Message');
        //         }
        //         // onFailure: function(){
        //         //     console.log('error :'+ data);
        //         // }

        //     }); 
        //     ajaxRequest.send(); 
        // }); 
    }
});




