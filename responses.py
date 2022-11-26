import random
import bot
from datetime import datetime


def get_response(message: str, user_name) -> str:
    user_message = message.lower()

    if user_message == 'hello':
        return 'Yo! Whats up ' + user_name

    if user_message == 'time':
        time = "It's " + datetime.now().strftime("%H:%M %p") + " now"
        return time

    if user_message == 'flip' or user_message == 'flip coin':
        coin = random.choice(["Head 😄", "Tail 🐍"])
        return coin

    else:
        return "`Hey dude, I didn't recognize your command, Please give some idea about this to my BOSS " \
               "\'BlazeSteel#5091\'`"
