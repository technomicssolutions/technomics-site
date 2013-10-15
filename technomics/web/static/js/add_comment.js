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
});

// {% url 'add_blog_comment' blog_id=blog.id %}?page={{ blogs.number }}