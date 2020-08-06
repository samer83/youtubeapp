$(function() {
    
    $('#download').click(function(e) {
    e.preventDefault()
    var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    
    if ($('#inputurl').val() == '')
        return

    $("#download").html('<i class="fa fa-spinner fa-spin"></i>Loading');
    var url = $('#inputurl').val();

    let formData = {
        'url'      : url
    };
    if (url.includes('youtu'))
    {
    $.ajax({
        url:"/api/downloader/youtube2/",
        async:true,
        headers:{"X-CSRFToken": $crf_token},
        dataType: "json",
        type: "POST",
        data: formData,
        success: function( data ) {
            if (data['error'] == "0"){
                var name = data['name']
                $('#video_result').text(name)
                var test_url = '',
                    player = videojs('my-player'),
                    sources = [];
                $("#video_result").append("<br /> <img class='m-auto' width='300px' src='" + data['thumbnail'] + "' />" )
                $.each(data['arr'], function( index, value ) {
                    $("#video_result").append('<br/><a href="'+value.url+'" target="blank" >' + value.ext + " - " +   value.format_note + "</a>");
                    

                    
                    if (value.ext == 'mp4')
                        
                    {type_current = "video/"// else 
                    //     type_current = "video/"

                    type_final = type_current + value.ext
                    sources.push ({type: type_final, src: value.url})}
                    // player.src.
                    // $("#video_link").attr("href", value.url)
                    // $("#video_link").html( value.ext + " - " +   value.format_note)
                  });

                // var options = {};
                
                //$('#my-player').removeClass( ["hide"] )
                player.poster (data['thumbnail'])
                player.src(
                    [sources]
                );

                $("#download").html('Download');
                $("#inputurl").val('');


                // player.src(sources);

               

                // for (x in data['arr'])
                // {   console.log(x)
                    
                //     $("#video_link").attr("href", x['url'])
                //     $("#video_link").attr("text", x['ext'])
                // }

                // window.open('/static/' + name)
                // $.fileDownload('/static/' + name)
                // .done(function () { alert('File download a success!'); })
                // .fail(function () { alert('File download failed!'); });


            }
        },
        error: function(data){
            console.log(data)
        }
    });
    }

    else 
    if (url.includes("linked"))
    {
        $.ajax({
            url:"/api/downloader/linkedin/",
            async:true,
            headers:{"X-CSRFToken": $crf_token},
            dataType: "json",
            type: "POST",
            data: formData,
            success: function( data ) {
                if (data['error'] == "0"){
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
    
    
                    // player.src(sources);
    
                   
    
                    // for (x in data['arr'])
                    // {   console.log(x)
                        
                    //     $("#video_link").attr("href", x['url'])
                    //     $("#video_link").attr("text", x['ext'])
                    // }
    
                    // window.open('/static/' + name)
                    // $.fileDownload('/static/' + name)
                    // .done(function () { alert('File download a success!'); })
                    // .fail(function () { alert('File download failed!'); });
    
    
                }
            },
            error: function(data){
                console.log(data)
            }
        });
    }

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