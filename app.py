from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('z8nsPxTqnRNG1iaNMOFJj2scFhNwolkIV804UfyfZ4ZSA25TrU/W1gHfMHqvlm7gk/uPnOqAVB2kRhU5kleTMOy4p5U/gw7Ns4NnZm97RHJC90InE6/i5cwiOciU51y5u19qwu597sz3d5LL1TsVWAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9948ae5d22a2c5b1b008b5f6bb02eb72')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='你吃飽了嗎?'))


if __name__ == "__main__":
    app.run()