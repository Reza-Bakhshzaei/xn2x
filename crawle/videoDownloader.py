import m3u8_To_MP4, requests, re, os

def download_video_from_link(url):
    print(f"url= {url}")
    if url.split("/")[-1]+".mp4" not in os.listdir():
        response = requests.get(url).text
        m3u8_file = response.find("html5player.setVideoHLS('")
        m = response.find("\n", m3u8_file)
        f = response[m3u8_file+len("html5player.setVideoHLS('"): m-len("');")]
        print(f"f= {f}")
        response = requests.get(f).content
        resolutions = sorted(sorted([tex for tex in response.decode("utf-8").split("\n") if re.findall("hls-(480|720|1080|360)p.*.m3u8", tex)]), key=len)
        print(f"resolutions= {resolutions}")
        m3u8_To_MP4.multithread_download(m3u8_uri=f.replace(f.split("/")[-1], resolutions[-1]), mp4_file_name="{}.mp4".format(url.split("/")[-1]))
        return url.split("/")[-1]+".mp4"
    else:return url.split("/")[-1]+".mp4"