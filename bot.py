import discord, random
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('M2L1\Imagenes'))
    with open(f'M2L1\Imagenes/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

@bot.command()
async def mem_ani(ctx):
    img_name = random.choice(os.listdir('M2L1\eni'))
    with open(f'M2L1\eni/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'Yes, {ctx.subcommand_passed} is cool')

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def man_plast(ctx):
    mn_plas = ["https://www.youtube.com/watch?v=T1zH0RfeZlU",
               "https://www.youtube.com/watch?v=D_u6mNlHprE",
               "https://www.youtube.com/watch?v=XLth_2Ag5_4",]
    plas = random.choice(mn_plas)

    await ctx.send(plas)

@bot.command()
async def carton(ctx):
    mn_car = ["https://www.youtube.com/watch?v=6zNiZofMemk",
              "https://www.youtube.com/watch?v=bOd0QwW0FHk",
              "https://www.youtube.com/watch?v=_tDtqKZIIEk"]
    car = random.choice(mn_car)
    await ctx.send(car)
@bot.command()
async def vidrio(ctx):
    mn_vid = ["https://www.youtube.com/watch?v=W13cDrJ299Q&pp=ygUXbWFudWFsaWRhZGVzIGNvbiB2aWRyaW8%3D",
              "https://www.youtube.com/watch?v=VrNNSYgTK5k",
              "https://www.youtube.com/watch?v=FlHPIma2zv0"]
    vid = random.choice(mn_vid)
    await ctx.send(vid)
@bot.command()
async def papel(ctx):
    mn_pap = ["https://www.youtube.com/watch?v=tWzDc0dx9oQ&pp=ygUWbWFudWFsaWRhZGVzIGNvbiBwYXBlbA%3D%3D",
              "https://www.youtube.com/watch?v=47ejbROR8ho&pp=ygUWbWFudWFsaWRhZGVzIGNvbiBwYXBlbA%3D%3D",
              "https://www.youtube.com/watch?v=5EzlPtFuYW4"]
    pap = random.choice(mn_pap)
    await ctx.send(pap)

bot.run("TOKEN")
