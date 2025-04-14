import discord

from discord.ext import commands 
from app import generador_password

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print("El bot esta en linea")


@bot.command()
async def hola(ctx):
    await ctx.send("Hola, soy un bot de prueba")



@bot.command()
async def adios(ctx):
    await ctx.send("Hasta luego")

@bot.command()
async def password(ctx):
    await ctx.send("Ingresa la longitud de la contraseña")

    def verificar(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    longitud = await bot.wait_for('message',check=verificar, timeout=20 )
                                   
    longitud = int(longitud.content)

    password = generador_password(longitud)
    await ctx.send(f"tu contraseña es: {password} ")


bot.run("")
