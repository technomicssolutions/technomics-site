
window.addEvent('domready',function() {
    var showDuration = 3000;
    var container = $('banner');
    var images = container.getElements('img');
    var currentIndex = 0;
    var interval;
    var minMargin = -1550;
    var maxMargin = 1550;
    var startMargin = 0;

    images.each(function(img,i){ 
        img.set('opacity',1);
    });

    var show = function() {
        images[currentIndex].tween('margin-left', startMargin , minMargin);
        images[currentIndex = currentIndex < images.length - 1 ? currentIndex+1 : 0].tween('margin-left', maxMargin, startMargin)
        // images[currentIndex].fade('out');
        // images[currentIndex = currentIndex < images.length - 1 ? currentIndex+1 : 0].fade('in');
    };
    
    window.addEvent('load',function(){
        interval = show.periodical(showDuration);
    });
});

