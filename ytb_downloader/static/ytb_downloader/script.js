$(function() {
    
    $('#download').click(function(e) {
    e.preventDefault()
    var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    
    if ($('#inputurl').val() == '')
        return

    $("#download").html('<i class="fa fa-spinner fa-spin"></i>Loading');
    let url = $('#inputurl').val(),
        api_url = "",
        formData = {
            'url'      : url
        };
    if (url.includes('youtu'))
    {
        api_url = "/api/downloader/youtube2/";
        state = "youtube"
    }
    else 
    if (url.includes("linked"))
    {
        api_url = "/api/downloader/linkedin/"
        state = "linkedin"
    }

        $.ajax({
            url:api_url,
            async:true,
            headers:{"X-CSRFToken": $crf_token},
            dataType: "json",
            type: "POST",
            data: formData,
            success: function( data ) {
                if (data['error'] == "0"){

                    if (state == "youtube")
                    {
                        $('#video_result').text(data['name'])
                        var test_url = '',
                            player = videojs('my-player'),
                            sources = [];
                            $("#video_result").append("<br /> <img class='m-auto' width='300px' src='" + data['thumbnail'] + "' />" )
                            $.each(data['arr'], function( index, value ) {
                            $("#video_result").append('<br/><a href="'+value.url+'" target="blank" >' + value.ext + " - " +   value.format_note + "</a>");
                            

                            if (value.ext == 'mp4')
                                
                            {type_current = "video/"// else 

                            type_final = type_current + value.ext
                            sources.push ({type: type_final, src: value.url})}
                            
                        });
                        
                        player.poster (data['thumbnail'])
                        player.src(
                            [sources]
                        );

                        $("#download").html('Download');
                        $("#inputurl").val('');


                    }
                    else
                    if (state == "linkedin")
                    {
                        var name = data['name']
                        // $('#video_result').text("download Linkedin Video")
                        var test_url = '',
                            player = videojs('my-player'),
                            sources = [];
                        $("#video_result").append("<br /> <a href='"+data["url"]+"' target='blank' > Click Here to Download <br /><img class='m-auto' width='300px' src='" + data['thumbnail'] + "' /></a>" )
                            
        
        
                        // var options = {};
                        
                        //$('#my-player').removeClass( ["hide"] )
                        player.poster (data['thumbnail'])
                        player.src(
                            [sources]
                        );
        
                        $("#download").html('Download');
                        $("#inputurl").val('');
                    }
                    
                
    
                }
            },
            error: function(data){
                console.log(data)
            }
        });

});



function download(filename, text) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:video/mp4;' + encodeURIComponent(text));
    element.setAttribute('download', filename);
  
    element.style.display = 'none';
    document.body.appendChild(element);
  
    element.click();
  
    document.body.removeChild(element);
  }
  

});