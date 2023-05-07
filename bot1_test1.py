import discord
import settings
from bot_mantik import *
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('*hello'):
        await message.channel.send('Selam! Ben bir botum!')
    elif message.content.startswith("seni kim yapti"):
        await message.channel.send("alperen adli müthiş bir coder, ne yazkki onu hiç göremiyorum,çünkü benim gözlerim yok ")    
    elif message.content.startswith('*bye'):
        await message.channel.send(":cry:")
    elif message.content.startswith('*smile'):
        await message.channel.send(emoji_olusturucu())
    elif message.content.startswith('*coin'):
        await message.channel.send(yazi_tura())
    elif message.content.startswith('*pass'):
        await message.channel.send(sifre_olusturucu(10))
    else:
        
        await message.channel.send("üzgünüm bunu anlayamadim")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.content.startswith('!deleteme'):
            msg = await message.channel.send('I will delete myself now...')
            await msg.delete()
            await message.channel.send('Goodbye in 3 seconds...', delete_after=3.0)

    async def on_message_delete(self, message):
        msg = f'{message.author} has deleted the message: {message.content}'
        await message.channel.send(msg)
    
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)

    async def on_message(self, message):
        if message.content.startswith('!editme'):
            msg = await message.channel.send('10')
            await msg.edit(content='40')

    async def on_message_edit(self, before, after):
        msg = f'**{before.author}** edited their message:\n{before.content} -> {after.content}'
        await before.channel.send(msg)

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(settings.settings["TOKEN"])
