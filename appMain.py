from bs4 import BeautifulSoup
import requests
import re
from discord_webhook import DiscordWebhook, DiscordEmbed
import os

_webhook_url = os.environ['WEBHOOKURL']
_source_url = os.environ['SOURCEURL']

def __main__():
    o = get_content()

    t = sort_with_col(o, 3)
    w = sort_with_col(o, 4)
    m = sort_with_col(o, 5)

    bm = beautify(m)
    bw = beautify(w)
    bt = beautify(t)

    shoot([make_embed("Today", bt), make_embed("Week", bw), make_embed("Month", bm)])

def shoot(l):
    webhook_urls = [_webhook_url]
    webhook = DiscordWebhook(url=webhook_urls)
    for x in l:
        webhook.add_embed(x)
    response = webhook.execute()
    print(response)


def make_embed(type, str):
    t = {"Today": "ff0047", "Week": "7289da", "Month": "1400ff"}
    embed = DiscordEmbed(title=type + ' sorted', description=str, color=int(t[type], 16))
    # embed.set_author(name='Author Name', url='https://github.com/lovvskillz',
    #                  icon_url='https://avatars0.githubusercontent.com/u/14542790')
    # embed.set_footer(text='Embed Footer Text')
    embed.set_timestamp()
    # embed.add_embed_field(name='Field 1', value='Lorem ipsum')
    # embed.add_embed_field(name='Field 2', value='dolor sit')
    # embed.add_embed_field(name='Field 3', value='amet consetetur')
    # embed.add_embed_field(name='Field 4', value='sadipscing elitr')
    return embed


def beautify(z):
    return re.sub("[{}\']+", "", '\n'.join(str(e) for e in list(map(lambda x: {x[1]: x[3:6]}, z[:10]))))


def sort_with_col(z, c):
    return sorted(z, key=lambda x: float(x[c]), reverse=True)


def get_content():
    html = requests.get(_source_url).content
    soup = BeautifulSoup(html, 'html.parser')
    tr = soup.find_all('tr')
    z = []
    for x in tr[3:]:
        z.append(x.text.split('\n'))
    return z


__main__()
