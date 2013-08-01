
window.addEvent('domready', function(){
    new OverText("name",{

    });
    new OverText("email",{

    })
    new OverText("msg",{
        
    })
    $('send').addEvent('click', function(e){
        e.stop();
        var contact_data = $('contact_form').toQueryString();
        var ajaxRequest = new Request({ 
            url: '/contactus',
            method: 'POST',
            data: contact_data,
            onComplete: function(){
                alert('You have successfully sent the Message');
            }
        }); 
        ajaxRequest.send(); 
	});  
});



