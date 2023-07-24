import os
import discord, requests
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command()
async def mem(ctx):
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        img_name = random.choice(os.listdir("meme_bot/images"))
        with open(f"meme_bot/images/{img_name}","rb") as f:
            picture = discord.File(f)
            # A continuación, podemos enviar este archivo como parámetro.
            await ctx.send(file=picture)

bot.run("MTEyNTkyMTE3NTI1MjUxMjg2OA.GDDFff.ZG3ELZ55O6gzyHeWB6oKia1ivD5kZAtrx5nqLQ")