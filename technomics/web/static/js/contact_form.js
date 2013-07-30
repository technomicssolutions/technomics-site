
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
        console.log(contact_data);
        var ajaxRequest = new Request({ 
            url: '/contactus',
            method: 'POST',
            data: contact_data,
            onRequest: function(){
              alert('just sent a Ajax request!');
            },
            onComplete: function(){
                alert('completed');
            }
        }); 
        ajaxRequest.send(); 
	});
    
});



