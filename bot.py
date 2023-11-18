import discord
import responses
import apitokens

discordapitoken = apitokens.discord_token()

async def send_message(message, user_message, is_bot):
    try:
        jamil = str("Jamil Post!!!! :))) :DDD")

        response = responses.get_response(user_message)
        if is_bot:
            await message.channel.send(jamil)
            await message.channel.send(response)

        else:
            pass

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = f"{discordapitoken}"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():

        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '!':
            user_message = user_message[1:]

            await send_message(message, user_message, is_bot=True)
        else:
            await send_message(message, user_message, is_bot=False)

    client.run(TOKEN)
