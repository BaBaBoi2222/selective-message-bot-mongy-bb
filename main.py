import discord
from discord.ext import commands
from discord.ext.commands import Bot

TOKEN = 'ABCD' #ENTER YOUR DISCORD BOT TOKEN HERE


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    #---- SET ACTIVITY OF THE BOT ----#
    game = discord.Game("ENTER THE ACTIVITY HERE") 
    await client.change_presence(status=discord.Status.idle, activity=game)
    #---- SET ACTIVITY OF THE BOT----#
    print("logged in as {0.user}".format(client))

#---- COMMANDS TRIGGERED BY MESSAGES SENT BY USER ----#
@client.event
async def on_message(message: discord.Message):
    
    #---- LOGS DMS THAT THE BOT RECEIVES ----#
    msg_dump_channel = 1234 # ENTER THE CHANNEL ID OF THE CHANNEL THAT YOU WANT FOR DM LOGS OF THE BOT
    mychannel = client.get_channel(msg_dump_channel)
    if message.guild is None and not message.author.bot:
        await mychannel.send("***" + str(message.author) + " :*** " + message.content)
    #---- LOGS DMS THAT THE BOT RECEIVES ----#

    if message.author == client.user: 
        return #this lets the bot ignore it's own messages so that it doesn't crash 
    
    #---- TRIGGER WORD(s) FEATURES ----#
    msg_content = message.content.lower()

    mongiess = ['the', 'list', 'of', 'trigger', 'words'] #ENTER THE TRIGGER WORDS IN THIS
    
    #---- SEND MESSAGES FOR TRIGGER WORD(s) ----#
    if msg_content in mongiess:
        await message.channel.send('The message that you want to send if a trigger word is sent.')
    #---- SEND MESSAGES FOR TRIGGER WORD(s) ----#
    
        #---- AUTO DELETE ANYTHING OTHER THAN THE TRIGGER WORDS ----#
    else:
        if message.channel.id == 1234:  #ENTER THE CHANNEL ID FOR THE AUTODELETION CHANNEL
            if message.author.id != 123: #ENTER THE USER ID OF THE USER WHOSE MESSAGES SHOULD NOT GET DELETED
                await message.delete() #DELETES EVERY MESSAGE OTHER THAN THE TRIGGER WORD
        #---- AUTO DELETE ANYTHING OTHER THAN THE TRIGGER WORDS ----#
    
    #---- TRIGGER WORD(s) FEATURES ----#

#---- SEND MESSAGES TO A SPECIFIC CHANNEL ----#
    mong = client.get_channel(123) #ENTER THE CHANNEL ID OF THE CHANNEL TO SEND MESSAGES TO
    first_word_of_message = message.content.split()[0]
    if message.author == client.user:
        return
    if message.channel.id == 123: #ENTER THE CHANNEL ID OF THE CHANNEL WHICH CAN USE THE COMMAND
        if message.author.id == 123: #ENTER THE USER ID OF THE USER WHICH CAN USE THE COMMAND
            if first_word_of_message == "scream":
                full_message = message.content.split("scream")[1]
                await message.channel.send("`I screamed:` " + full_message)
                await mong.send(full_message)
#---- SEND MESSAGES TO A SPECIFIC CHANNEL ----#   
        
        #---- DM USER BY USER ID ----#        
            deemm = message.content.split("^")
            if deemm[0] == "dm":
                the_req_user = await client.fetch_user(int(deemm[1]))
                the_req_msg = deemm[2]
                await the_req_user.send(the_req_msg)
        #---- DM USER BY USER ID ----#  
        
#---- COMMANDS TRIGGERED BY MESSAGES SENT BY USER ----#


#---- DELETES EDITED MESSAGES IN A SPECIFIC CHANNEL ----#
@client.event
async def on_message_edit(old, new):
    if new.channel.name == 'ENTER THE CHANNEL NAME HERE':
        await new.delete()
#---- DELETES EDITED MESSAGES IN A SPECIFIC CHANNEL ----#

client.run(TOKEN)
