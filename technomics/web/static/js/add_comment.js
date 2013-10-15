window.addEvent('domready', function(){
    
    var blog_comment_links = $$('.blog_comment');
    var comment_form = $('comment_form');
    blog_comment_links.each(function(item, index){
//        alert(index + " = " + item);
        item.addEvent('click', function(e) {
        e.stop();
        if (item.getParent().contains(comment_form)) {
            ;
        }
        else {
            alert(comment_form);
            comment_form.inject(item.getParent(), 'after');
        }
        });
});
//    if (blog_comment_link) {
//        blog_comment_link.addEvent('click', function(e) {
//            e.stop();
//            alert
////            this.element = blog_comment_link;
////            console.log("hello");
////            if (this.element.getParent().contain(comment_form)) {
////                alert("hello");
//////                comment_form.show();
////            }
////            else {
////                this.element.getParent().inject(comment_form);
////                comment_form.setStyle('display', 'block');
////            }
//        });
//    }
});

//    var comment_form = $('comment_form') 
//    var send_comment = $('send_comment');
//    if (send_comment) {
//        send_comment.addEvent('click', function(e){
//             e.stop();
//             
////             var comment_data = comment_form.toQueryString();
////             var blog_id = $('hidden_blog_id').get('name');
////             var ajaxRequest = new Request({ 
////                 url: '/blog/comment/add/'+blog_id+'/',
////                 method: 'POST',
////                 data: comment_data,
////                 onSuccess: function(response){
//////                     console.log('You have successfully sent the Message');
//////                    console.log(response);
////                    comment_form.hide();
////                    $('comments').set('html', response);

////                 }
//////                  onFailure: function(){
//////                      console.log('error :'+ data);
//////                  }

////             }); 
//             ajaxRequest.send(); 
//         }); 
//        // $('submit_form').addEvent('click', function(e){
//        //     e.stop();
//        //     var form_data = $('form_experienced').toQueryString();
//        //     console.log('data'+form_data);
//        //     var ajaxRequest = new Request({ 
//        //         url: '/careers_experienced',
//        //         method: 'POST',
//        //         data: form_data,
//        //         onSuccess: function(){
//        //             console.log('You have successfully sent the Message');
//        //         }
//        //         // onFailure: function(){
//        //         //     console.log('error :'+ data);
//        //         // }

//        //     }); 
//        //     ajaxRequest.send(); 
//        // }); 
//    }




