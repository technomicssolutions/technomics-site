
window.addEvent('domready', function(){
    
    $('send').addEvent('click', function(e){
        e.stop();
        var contact_data = $('contact_form').toQueryString();
        console.log('data'+contact_data);
        var ajaxRequest = new Request({ 
            url: '/contactus',
            method: 'POST',
            data: contact_data,
            onSuccess: function(){
                console.log('You have successfully sent the Message');
            }
            // onFailure: function(){
            //     console.log('error :'+ data);
            // }

        }); 
        ajaxRequest.send(); 
	});  
});



