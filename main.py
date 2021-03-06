import discord

class MyClient(discord.Client):
    async def on_message(self, message):
        if message.channel.id == 817424573842325504:
            emo = '\N{WHITE HEAVY CHECK MARK}'
            emoji = '\N{CROSS MARK}'
            await message.add_reaction(emo)
            await message.add_reaction(emoji)
        elif message.channel.id == 757658767692136663:
            emo = '\N{WHITE HEAVY CHECK MARK}'
            emoji = '\N{CROSS MARK}'
            await message.add_reaction(emo)
            await message.add_reaction(emoji)
Client = MyClient()
Client.run('ODE3NzMzNzk5MTE4NTA0MDA2.YENz8g.Mz9ZfPlpdyUQAWMDErzqXCB9-FM')
