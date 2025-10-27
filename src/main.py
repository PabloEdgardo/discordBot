import discord
from discord.ext import commands, tasks
from datetime import time 

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

#eventos
@bot.event
async def on_ready():
    enviar_mensagem.start()
    bom_dia.start()
    boa_tarde.start()
    boa_noite.start()
    print(f"bot {bot.user} inicializado")

@bot.event
async def on_member_join(membro:discord.Member):
    canal = bot.get_channel(1432157367637770311)
    await canal.send(f"{membro.mention} entrou no servidor <3")

@bot.event
async def on_member_remove(membro:discord.Member):
    canal = bot.get_channel(1432157367637770311)
    await canal.send(f"{membro.mention} saiu do servidor :(")

@bot.event
async def on_reaction_add(reacao:discord.Reaction, membro:discord.Member):
    await reacao.message.reply(f"o membro {membro.name} reagiu com a reação:{reacao.emoji}")

#comandos

@bot.command()
async def ola(ctx:commands.Context, nome):
    nome = ctx.author.name
    await ctx.reply(f"opa {nome}")

@bot.command()
async def falar(ctx:commands.Context, *,texto):
    await ctx.send(texto)

@bot.command()
async def soma(ctx:commands.Context, num1:float,num2:float):
    resultado = num1+num2
    await ctx.send(f"a soma entre {num1} e {num2} é igual a {resultado}")

#tasks

@tasks.loop(seconds=5)
async def enviar_mensagem():
    canal = bot.get_channel(1432170302623846510)
    await canal.send("salve allah")

@tasks.loop(time=time(6, 0))
async def bom_dia():
    canal = bot.get_channel(1432174543543468123)
    await canal.send("bom dia")

@tasks.loop(time=time(12, 0))
async def boa_tarde():
    canal = bot.get_channel(1432174543543468123)
    await canal.send("boa tarde")

@tasks.loop(time=time(18, 0))
async def boa_noite():
    canal = bot.get_channel(1432174543543468123)
    await canal.send("boa noite")
    
bot.run("MTQzMjA5MDcwNDgxMjk3MDAzNA.GgUNwc.r4ifyg-wQRZjrT5UH1x3XmMVn8a5bgorv-ROmw")
