$(function() {
    
    $('#download').click(function(e) {
        e.preventDefault()
    var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');

    let formData = {
        'url'      : $('#inputurl').val(),
    };
    $.ajax({
        url:"/api/downloader/youtube/",
        async:true,
        headers:{"X-CSRFToken": $crf_token},
        dataType: "json",
        type: "POST",
        data: formData,
        success: function( data ) {
            if (data['error'] == "0"){
                var name = data['name']
                // window.open('/static/' + name)
                $.fileDownload('/static/' + name)
                .done(function () { alert('File download a success!'); })
                .fail(function () { alert('File download failed!'); });

                
            }
        },
        error: function(data){
            console.log(data)
        }
    });
});

});