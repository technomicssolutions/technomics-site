window.addEvent('domready', function(){
    $$('.form_comment').hide();
    // var blog_comment_links = $$('.blog_comment');
    // var comment_form = $('comment_form');
    // blog_comment_links.each(function(item, index){
    //     item.addEvent('click', function(e) {
    //     e.stop();
    //     if (item.getParent().contains(comment_form)) {
    //         ;
    //     }
    //     else {
    //         comment_form.inject(item.getParent(), 'after');
    //     }
    // });
    $$('.blog_comment').addEvent('click', function(e){
        $$('.blog_comment').hide();
        form_id = this.getParent().getElement('form').get('id');
        $(form_id).show();
    });
    $$('.comment_submit').addEvent('click', function(e) {
        $$('.blog_comment').show();
        // form_id = this.getParent().get('id');
        // var form_data = $(form_id).toQueryString();
        // var url = 'blog/comment/add/'+form_id+'/';
        // var ajaxRequest = new Request({ 
        //     url: url,
        //     method: 'POST',
        //     data: form_data,
        //     onSuccess: function(){
        //         console.log('You have successfully sent the Message');
        //     }
        // });
        $(form_id).hide();

    });
});

// {% url 'add_blog_comment' blog_id=blog.id %}?page={{ blogs.number }}