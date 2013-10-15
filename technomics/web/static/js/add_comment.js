window.addEvent('domready', function(){
    
    var blog_comment_links = $$('.blog_comment');
    var comment_form = $('comment_form');
    blog_comment_links.each(function(item, index){
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

