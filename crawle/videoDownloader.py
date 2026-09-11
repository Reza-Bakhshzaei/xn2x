import requests, re, os
from pym3u8downloader import M3U8Downloader

def download_video_from_link(url):
    name = url.split("/")[-1]+".mp4"
    if name not in os.listdir():
        response = requests.get(url).text
        m3u8_file = response.find("html5player.setVideoHLS('")
        m = response.find("\n", m3u8_file)
        f = response[m3u8_file+len("html5player.setVideoHLS('"): m-len("');")]
        response = requests.get(f).content
        resolutions = sorted(sorted([tex for tex in response.decode("utf-8").split("\n") if re.findall("hls-(480|720|1080|360)p.*.m3u8", tex)]), key=len)
        print(f"resolutions= {resolutions}")
        # m3u8_To_MP4.multithread_download(m3u8_uri=f.replace(f.split("/")[-1], resolutions[-1]), mp4_file_name="{}.mp4".format(url.split("/")[-1]))
        link = f.replace(f.split("/")[-1], resolutions[-1])
        downloader = M3U8Downloader(
            input_file_path=link,
            output_file_path=name
        )
        print("Downloading....")
        downloader.download_playlist()
        return name
    else:return name