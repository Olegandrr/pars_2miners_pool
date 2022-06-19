import requests
import config


def send_telegram(text):
    token = config.token_bot
    url = config.url_api_telegram
    channel_id = config.channel_id
    url += token
    method = url + "/sendMessage"
    message = requests.post(method, data={"chat_id": channel_id, "text": text})
    if message.status_code != 200:
        raise Exception("post_text error")

