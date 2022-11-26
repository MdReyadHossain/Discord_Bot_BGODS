import os
import requests
import json
import responses
import discord


async def send_message(message, user_message, is_private):
    try:
        user_name = str(message.author)
        response = responses.get_response(user_message, user_name)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_bgods():
    LINK = 'https://discord.com/api/oauth2/authorize?client_id=1025481026853687429&permissions=1643094998080&scope=bot'

    TOKEN = os.getenv('TOKEN')  # set token in environment variable for private

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)  # connection with discord by discord py library

    @client.event  # take event from discord
    async def on_ready():
        print(f'{client.user} Successfully logged in and Turned on :)')  # showing the bot name

    @client.event
    async def on_message(message):
        userName = str(message.author)
        userMessage = str(message.content)
        channel = str(message.channel)
        # if message from discord bot or not? if not then it's from ourselves and return
        if userName == client.user:
            return

        if userMessage[0] == '?':
            userMessage = userMessage[1:]  # [1:] Remove the first letter
            await send_message(message, userMessage, is_private=True)
        elif userMessage[0] == '$':
            userMessage = userMessage[1:]
            await send_message(message, userMessage, is_private=False)

    # to run replit of the bot, but it will run as public, so that the token had to put in .env file(private file)
    client.run(TOKEN)  # the token of discord bot
