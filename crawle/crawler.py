import requests, json
from bs4 import BeautifulSoup
from pyrogram.types import InlineQueryResultPhoto, InputTextMessageContent
from pyrogram.enums import ParseMode

base_url = "https://www.xnxx.com"

async def get_results(query):
    url = "{}/search/{}?top".format(base_url, query)
    results = []
    response = requests.get(url).content
    soup = BeautifulSoup(response, features='lxml')
    r = {}
    for row, col in zip(soup.find_all('div',{'class':'thumb'}), soup.find_all('p', {'class':'metadata'})):
        if len(results) < 21:
            results.append(InlineQueryResultPhoto(
                photo_url= row.a.img['data-src'],
                thumb_url=row.a.img['data-src'],
                description="Meta Data: {}".format("-".join(col.text.split())),
                title=row.a['href'].split("/")[-1].replace("_", " ") if row.a['href'].split("/")[-1].replace("_", " ") != " " else "No Title",
                input_message_content=InputTextMessageContent("[{}]({})\n{}".format(row.a['href'].split("/")[-1].replace("_", " ") if row.a['href'].split("/")[-1].replace("_", " ") != " " else "No Title", base_url+row.a['href'], " - ".join(col.text.split())), disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN)
            ))
        else:break
    return results