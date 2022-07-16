import requests
import json

import discord
from discord.ext import commands
 


bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help
 
 
@bot.command()
async def tiktok(ctx, *, urltiktok):
    await ctx.message.delete()
    await ctx.send("Generando link tik tok...", delete_after=0)

    response = requests.get(f"https://jose89fcb.es/tiktok/tiktok.php?url=" + urltiktok)
    tiktok = response.json()['tiktok']
    Creador = response.json()['Creador']
    Titulo = response.json()['Titulo']
    Fecha = response.json()['Fecha']
    Avatar = response.json()['Avatar']         


    embed = discord.Embed(title=f"tik tok", description=f"[Descargar video]({tiktok})\n\nCreador🡺 {Creador}\n\nTitulo🡺 {Titulo}\n\nFecha🡺 {Fecha}", color=discord.Colour.random()) 
    embed.set_author(name="Tik Tok", icon_url=f"{Avatar}")
        
   

   


  
   
        
    await ctx.send(embed=embed)
   
      




 

 
 
 
@bot.event
async def on_ready():
    print("BOT listo!")
    
 
    
bot.run('')
