from pyrogram import Client, filters
from crawle.crawler import get_results
from crawle.videoDownloader import download_video_from_link
import os
proxi = {
    "scheme": "socks5",
    "hostname": "127.0.0.1",
    "port": 2080
}
api_id = 14381680
api_hash = "e062fd165636c6a327fa0be3b8ec3276"
bot_token="8239834763:AAFqysk4PKtjvS9ugXwpu45u5RF0aBBA29I"
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_inline_query()
async def answer(client, inline_query):
    if len(inline_query.query) > 3:
        await inline_query.answer(
            results= await get_results(inline_query.query),
            cache_time=1
        )

@app.on_message()
async def videoDownload(c, m):
    if m.entities:
        if m.entities[len(m.entities)-1].url:
            name = download_video_from_link(m.entities[len(m.entities)-1].url)
            await c.send_video(m.chat.id, name)
            os.remove(name)
    else:
        await m.reply("not found command")
app.run()

