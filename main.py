try: 
    import conf
except ImportError:
    pass
import discord
from discord.ext import commands
import img_handler as imhl
import os

intents = discord.Intents.default()
intents.members = True



bot = commands.Bot(command_prefix="!", intents = intents)
vchannel = 835474867762626580
channel = 825309119589122088
@bot.command(name="hello")
async def command_hello(ctx):
    global channel
    if ctx.channel.id == channel:
        msg = f'hello'
        await ctx.channel.send(msg)

@bot.command(name="repeat")
async def repeat(ctx):
    global channel
    if ctx.channel.id == channel:
        if ctx.message.content == "!repeat":
            await ctx.send(f'what?')
        else:
            await ctx.send(f'{ctx.message.content[7:]}')

@bot.command(name="about_me")
async def about_me(ctx):
    global channel
    if ctx.channel.id == channel:
        await ctx.channel.send(f'Your name is {ctx.message.author.name} \nYour id is {ctx.message.author.id}\n{"Your nickname is " + ctx.message.author.nick if ctx.message.author.nick != None else ""}')

@bot.command(name="get_channels")
async def get_channels(ctx):
    count = 1
    msg = ""
    global channel
    if ctx.channel.id == channel:
        for channel in ctx.guild.channels:
            msg += f'{count}. {channel} - {channel.id} \n'
            count += 1
    
        await ctx.channel.send(msg)
@bot.command(name="get_members")
async def get_members(ctx):
    msg = ''
    count = 1
    global channel
    if ctx.channel.id == channel:
        for member in ctx.guild.members:
              
              
            msg += f'{count}. {member} {"- " + member.nick if member.nick != None else ""} - {member.id}\n'
            count += 1
        await ctx.channel.send(msg)
@bot.command(name="get_member")
async def get_member(ctx, member:discord.Member=None ):
    msg = None
    global channel
    if ctx.channel.id == channel:
        if member:
            msg = f'Member {member.name} {"- " + member.nick if member.nick != None else ""} - {member.id}'

        if msg == None:
            msg = "ERROR"
        await ctx.channel.send(msg)
     
@bot.command(name="mk")
async def mk(ctx, f1:discord.Member=None, f2:discord.Member=bot.user):

    global channel
    if ctx.channel.id == channel:
        if f1 and f2:

            await imhl.vs_create(f1.avatar_url, f2.avatar_url)

            await ctx.channel.send(file = discord.File(os.path.join("./img/result.png")))
@bot.command(name="mka")
async def mka(ctx, f1:discord.Member=None, f2:discord.Member=bot.user):

    global channel
    if ctx.channel.id == channel:
        if f1 and f2:

            await imhl.vs_create_animated(f1.avatar_url, f2.avatar_url)

            await ctx.channel.send(file = discord.File(os.path.join("./img/result.gif")))
@bot.command(name = "fight")
async def command_fight(ctx):
    msg = ""
    global channel

    if ctx.channel.id == channel:



        

        if len(ctx.author.voice.channel.members) == 2:

            f1 = ctx.author.voice.channel.members[0]
            f2 = ctx.author.voice.channel.members[1]
            voice_channel = ctx.author.voice.channel

            msg = f'{f1.name} {f"-{f1.nick}" if f1.nick else ""} vs {f2.name} {f"({f2.nick})" if f2.nick else ""}'

            await voice_channel.connect()
            await imhl.vs_create_animated(f1.avatar_url, f2.avatar_url)
            await ctx.channel.send(msg)
            await ctx.channel.send(file=discord.File(os.path.join("./img/result.gif")))
            voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
            await voice_client.play(discord.FFmpegPCMAudio(executable="./FFmpeg/ffmpeg.exe", source="./sound/mk.mp3"))
        if len(ctx.author.voice.channel.members) == 1:

            f1 = ctx.author.voice.channel.members[0]
            f2 = bot.user
            voice_channel = ctx.author.voice.channel

            msg = f'{f1.name} {f"- {f1.nick}" if f1.nick else ""} vs {f2.name}'
            await voice_channel.connect()
            await imhl.vs_create_animated(f1.avatar_url, f2.avatar_url)
            await ctx.channel.send(msg)
            await ctx.channel.send(file=discord.File(os.path.join("./img/result.gif")))
            voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
            await voice_client.play(discord.FFmpegPCMAudio(executable="./FFmpeg/ffmpeg.exe", source="./sound/mk.mp3"))

        
@bot.command(name="join")
async def vc_join(ctx):
    msg = ""
    global channel
    if ctx.channel.id == channel:
        voice_channel = ctx.author.voice.channel
        if voice_channel:
            msg=f'Подключаюсь к {voice_channel.name}'
            await ctx.channel.send(  msg  )
            await voice_channel.connect()

@bot.command(name="leave")
async def vc_leave(ctx):
    msg = ""
    global channel
    if ctx.channel.id == channel:
        voice_channel = ctx.author.voice.channel
        if voice_channel:
            msg=f'Отключаюсь от {voice_channel.name}'
            await ctx.channel.send(  msg  )
            await ctx.voice_client.disconnect()

@bot.command(name="ost")
async def vc_ost(ctx):
    msg = ""
    global channel
    if ctx.channel.id == channel:
        voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        msg = f'Mortal combat'
        await ctx.channel.send(msg)
        await voice_client.play(    discord.FFmpegPCMAudio( executable="./FFmpeg/ffmpeg.exe", source="./sound/mk.mp3")    )

bot.run(os.environ["BOT_TOKEN"])
