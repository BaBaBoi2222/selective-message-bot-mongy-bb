# selective-message-bot-mongy-bb
 Just a simple fun project, the code is not that good sorry i just wanted a simple bot
## What can the bot do?
- Responds to specific keywords.
- Deletes a message which does not have the keywords in it.
- Deletes the messages if they are edited in a specific channel. (you can ignore a user from this)
- Send dms.(you can make it such that only a specific user can use that command)
- Log the dms it recieves in a specific channel.
- Send custom messages in a specific channel.(you can make it such that only a specific user can use that command)
- Set custom activity for the bot
## How to customize the bot to only use the features that I want to use?
The bot is seperated into code blocks with some comments, you can remove the features that you don't want and keep the ones that you want.
For example:
```py
@client.event
async on_ready():
    #---- SET ACTIVITY OF THE BOT----#
    game = discord.Game("The game activity")
    await client.change_presence(status=discord.Status.idle, activity=game)
    #---- SET ACTIVITY OF THE BOT----#
    print("logged in as {0.user}".format(client))
#---- SEND MESSAGES FOR A TRIGGER WORD ----#
@client.event
async on_message(message):
    if message == 'trigger':
        message.channel.send("The message that you want to send")
#---- SEND MESSAGES FOR A TRIGGER WORD ----#
```
If you want to use the **SET ACTIVITY FOR BOT** feature ONLY you can remove everything between the **SEND MESSAGES FOR A TRIGGER WORD**

## How to use the dm command
you just need to use this format `dm^TheUserID^the message that you want to send`
## How to send messages to a channel
use `scream` followed by the message
for example: `scream GIGGLY BALLS`
> GIGGLY BALLS

***You can read the comments in the code to customize the commands for your server*** 

I think the code could have been written in a more efficient way but i just need this bot for simple purposes and it was just a fun project, have a nice day! :D