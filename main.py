from pygooglenews import GoogleNews
import random 
import json
import requests
import time

webhook_url = '  ' #your discord webhook URL here 
gn = GoogleNews(country='INDIA')
local = gn.geo_headlines("JHARKHAND", proxies=None, scraping_bee=None)

def get_link():
    links = {}
    newsitem = local['entries']
    for item in newsitem[:80]:
        links[item.title] = item.link   
    return links

def get_news():
    dic = get_link()
    pair = []
    final = []
    for title, url in dic.items():
        pair.append((title, url))
        final.append(pair)
        pair= []

    for items in final[random.randint(0, 50)]:
        newsTitle = items[0]
        link = items[1]
    final=[]
    return newsTitle, link


def send_msg():
    title, URL = get_news()

    message = {
        "username": "Ranchi News BOT",
        "embeds": [
            {
                "author": {
                    "name": "News",
                    "icon_url": "https://imgur.com/gallery/heDJx92"
                },
                "title": f"{title}",
                "description": f"Read more about it **[here]({URL}).**",
                "color": 15258703,

            }
        ]
    }

    # Send the message to the Discord webhook.
    response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})

    # Check if the message was sent successfully.
    if response.status_code == 204:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(response.text)


def play():
    while True:
      send_msg()
      time.sleep(7200)


play()
