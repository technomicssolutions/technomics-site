window.addEvent('domready', function(){
    $('send_comment').addEvent('click', function(e){
         e.stop();
//         alert('hai')
         var contact_data = $('comment_form').toQueryString();
          console.log('data'+contact_data);
 //        var ajaxRequest = new Request({ 
 //            url: '/contactus',
 //            method: 'POST',
 //            data: contact_data,
 //            onSuccess: function(){
 //                console.log('You have successfully sent the Message');
 //            }
 //            // onFailure: function(){
 //            //     console.log('error :'+ data);
 //            // }

 //        }); 
 //        ajaxRequest.send(); 
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
});



