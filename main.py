import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".", help_command=None)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await client.change_presence(activity=discord.Game("UwU Type .help"))


#--------------------------------------------------------
def translate(txt):
    output = ''
    for i in range(len(txt)):
        char = txt[i]
        if (i > 0):
            prev = txt[i - 1]
        else:
            prev = ''

        if (char == 'r' or char == 'l'):
            output += "w"
        elif (char == 'R' or char == 'L'):
            output += "W"
        elif (char == "o"):
            if (prev == 'm' or prev == 'n' or prev == 'N' or prev == 'M'):
                output += "yo"
            else:
                output += "o"
        elif (char == "o"):
            if (prev == 'm' or prev == 'n' or prev == 'N' or prev == 'M'):
                output += "YO"
            else:
                output += "O"
        else:
            output += char

    return output


#--------------------------------------------------------
@client.command(name="uwufy")
async def uwufy(ctx, *, text=''):
    if (not text == ''):
        await ctx.send(translate(text))
    else:
        channel = ctx.channel
        lastmsg = (await channel.history(limit=2).flatten())[1]
        await channel.send(translate(lastmsg.content))


#--------------------------------------------------------
@client.command(name="help")
async def help(ctx):
    await ctx.send(
        "```\nCommands:\n.help\n.uwufy -    .uwufy Sample Text\n       -    If no text is given, it will uwufy the latest message in the channel\n```"
    )


#--------------------------------------------------------
try:
    client.run(os.getenv("TOKEN"))
except discord.HTTPException:    os.system("kill 1")
