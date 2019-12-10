$('#submit_button').click(function(){
    event.preventDefault();
    console.log('form submited')
    send_data();
});

function send_data(){
    console.log("send data is working")
    $.ajax({
        url : "calculator",
        type : "GET",
        data : {
            amount : $('#amount_to_conv').val(),
            from_currency: $('#from_currency').val(),
            to_currency: $('#to_currency').val()
        }, 

        // handle a successful response
        success : function(response_data) {
            $('#result').html("<b>Result:" + response_data.result_of_conv + "</b>")
            console.log(response_data);
            console.log("success");
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>");
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
};
