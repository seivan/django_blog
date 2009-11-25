import re
def embed_youtube(youtube_url):
    #import pdb; pdb.set_trace()
    regex = re.compile(r"(http://)?(www\.)?(youtube\.com/watch\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})")
    video_url = regex.match(youtube_url)
    video_id = video_url.group('id')
    return """<object width="425" height="344">
                <param name="movie" value="http://www.youtube.com/watch/v/%s"></param>
                <param name="allowFullScreen" value="true"></param>
                <embed src="http://www.youtube.com/watch/v/%s" type="application/x-shockwave-flash" allowfullscreen="true" width="425" height="344"></embed>
                </object>""" % (video_id, video_id)