import discord, random, json, urllib.request
from discord.ext import commands
from database import *


def requestCat():
    ### Returns a random cat image from imgur
    firstVar = urllib.request.urlopen("https://api.thecatapi.com/v1/images/search").read()
    secondVar = json.loads(firstVar)
    return(secondVar[0]['url']) 

def requestDog():
    ### Returns a random dog image
    firstVar = urllib.request.urlopen("https://random.dog/woof.json?ref=apilist.fun").read()
    secondVar = json.loads(firstVar)
    return(secondVar['url']) 


client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('.help'))
    print('The Bot is online and running baby ;)')

### A ping command
@client.command()
async def ping(ctx):
    embeded=discord.Embed(title=f'Pong! \n{round(client.latency * 1000)}ms', value=f'Pong! \n{round(client.latency * 1000)}ms', colour=discord.Colour.green())
    await ctx.send(embed=embeded)

### A purge command
@client.command(aliases=['purge'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, ammount=5):
    await ctx.channel.purge(limit=ammount + 1)

### Here is the ban command
@client.command()
@commands.has_permissions(ban_members=True)

async def ban(ctx, member: discord.Member=None):

    if not member:

        await ctx.send('Please mention a member')

        return

    await member.ban()

    await ctx.send(f'{member.display_name} was banned from the server')

### And here the kick command
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member=None, *, reason=None):

    if not member:

        await ctx.send('Please mention a member')

        return
    await member.kick()

    if reason != None:
        await ctx.send(f'{member.display_name} was kicked from the server. Reason: {reason}')
    else:
        await ctx.send(f'{member.display_name} was kicked from the server.')

### GIFS
### Hmm
@client.command()
async def hmm(ctx):
    await ctx.send(random.choice(gifs_hmm))
### Uhh
@client.command(aliases=["kinda"])
async def uhh(ctx):
    await ctx.send(random.choice(gifs_uhh))
### What
@client.command()
async def what(ctx):
    await ctx.send(random.choice(gifs_what))
### Anyways
@client.command()
async def anyways(ctx):
    await ctx.send(random.choice(gifs_anyways))
### Ok
@client.command()
async def ok(ctx):
    await ctx.send(random.choice(gifs_ok))
### Hello
@client.command(aliases=["hello"])
async def hi(ctx):
    await ctx.send(random.choice(gifs_hello))
### Hack
@client.command(aliases=["ddos"])
async def hack(ctx):
    await ctx.send(random.choice(gifs_hack))
### No
@client.command()
async def no(ctx):
    await ctx.send(random.choice(gifs_no))
### Yes
@client.command()
async def yes(ctx):
    await ctx.send(random.choice(gifs_yes))
### END OF GIFS

### Shrek command
@client.command()
async def shrek(ctx):
    await ctx.send(random.choice(cursed_shrek))

### Dice command
@client.command(aliases=['roll'])
async def dice(ctx, number=6):
    if number < 3:
        await ctx.send('Big idiot trying to roll a dice with less than 3 sides.')
    else:
        await ctx.send(f'You roll a dice and... The result is {random.randint(1, number)}')

### Coinflip command
@client.command(aliases=['flip', 'coinflip'])
async def coin(ctx):
    sides=["heads", "tails"]
    await ctx.send("You flip a coin and... It's " + random.choice(sides) +"!" )

### Use command
@client.command()
async def userate(ctx):
    await ctx.send('This bot is as used as the word "Razbliuto"')


### Help command
@client.remove_command('help')
@client.command()
async def help(ctx):
    embeded=discord.Embed(title='Help', value='Help', colour=discord.Colour.blurple())

    embeded.add_field(name='Commands', value="- .roll: Rolls a dice, you can specify face count\n- .meme: well...\n- .flip: Flips a coin for you, what a good boy\n- .fear: Tells a short horror story\n- .quote: Tells a random quote\n- .shrek: uhh...\n- .help: It's a paradox\n- .tehc: Tech jokes\n- .joke: Really bad jokes\n- .story: Tells a short story\n- .ping: Latency of the bot")
    embeded.add_field(name='Gifs', value="- .hmm\n- .what\n- .hi\n- .ok\n- .uhh\n- .anyways\n- .no\n- .yes\n- .hack")
    embeded.add_field(name='Images', value='- .cat\n - .dog')
    embeded.add_field(name='Mod Only', value="- .kick: You guess\n- .ban: What do you think it does?\n- .clear: Deletes a specified amount of messages")
    await ctx.send(embed=embeded)

### Fuck command (really long btw)
@client.command()
async def fuck(ctx):
    await ctx.send("You are hypocritical, greedy, violent, malevolent, vengeful, cowardly, deadly, mendacious, meretricious, loathsome, despicable, belligerent, opportunistic, barratrous, contemptible, criminal, fascistic, bigoted, racist, sexist, avaricious, tasteless, idiotic, brain-damaged, imbecilic, insane, arrogant, deceitful, demented, lame, self-righteous, byzantine, conspiratorial, satanic, fraudulent, libelous, bilious, splenetic, spastic, ignorant, clueless, illegitimate, harmful, destructive, dumb, evasive, double-talking, devious, revisionist, narrow, manipulative, paternalistic, fundamentalist, dogmatic, idolatrous, unethical, cultic, diseased, suppressive, controlling, restrictive, malignant, deceptive, dim, crazy, weird, dystopic, stifling, uncaring, plantigrade, grim, unsympathetic, jargon-spouting, censorious, secretive, aggressive, mind-numbing, arassive, poisonous, flagrant, self-destructive, abusive, socially-retarded, puerile, clueless, and generally NOT GOOD.")

### Fear command
@client.command(aliases=["horror"])
async def fear(ctx,):
    await ctx.send(random.choice(horror))

### Story command
@client.command(aliases=["story", "tell"])
async def tale(ctx,):
    await ctx.send(random.choice(stories))

### Quotes command
@client.command()
async def quote(ctx):
    await ctx.send(random.choice(phrases))

### Tech command
@client.command(aliases=["tehc"])
async def tech(ctx):
    await ctx.send(random.choice(tech_jokes))

### Jokes command
@client.command(aliases=["fun"])
async def joke(ctx):
    await ctx.send(random.choice(jokes))
### Memes command
@client.command(aliases=["random"])
async def meme(ctx):
    await ctx.send(random.choice(memes_list))

### Cat command
@client.command(aliases=['cats'])
async def cat(ctx):
    await ctx.send(requestCat())

### Dog command
@client.command(aliases=['dogs'])
async def dog(ctx):
    await ctx.send(requestDog())

client.run("") ## Add token here