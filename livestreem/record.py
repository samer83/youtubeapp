import urllib
import m3u8
import streamlink


def record_stream(url,filename,iterations):
    last_part = 0
    for i in range(iterations+1):

        streams = streamlink.streams(url)
        stream_url = streams["best"]
        print(stream_url.args['url'])

        m3u8_obj = m3u8.load(stream_url.args['url'])

        previous_part_time = last_part
        last_part = m3u8_obj.segments[-1].program_date_time

        if i >= 1:
         for j in range(1, len(m3u8_obj.segments)):
            if m3u8_obj.segments[-j].program_date_time == previous_part_time:
               break
         print('i is: ')
         print(i)

         print('jjjj is: ')
         print(j)

         print('i am jjjj now')
        
         file = open(filename + ".ts", "ab+")
         print('jj file opened ')
         print(m3u8_obj.segments[-i].uri)

         # with urllib.request.urlopen(m3u8_obj.segments[-i].uri) as response:
         #       html = response.read()
         #       print('file being red')
         #    #    print(html)
         #       file.write(html)

         for i in range(j-1,0,-1):
            with urllib.request.urlopen(m3u8_obj.segments[-i].uri) as response:
               html = response.read()
               print('file being red')
               file.write(html)
         print('file closed')
        #  file.close()



