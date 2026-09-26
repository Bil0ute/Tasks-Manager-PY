import discord
from discord.ext import commands
from discord import Intents
import random


intents = Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="?", intents=intents)


def pile_ou_face():
    pof = random.randint(1, 2 )
    if pof == 1:
        return "face"
    else:
        return "pile"

def cln():
    plo = random.randint(1, 5 )
    if plo == 1:
        return "https://usagif.com/wp-content/uploads/gif/anime-hug-94.gif"
    elif plo == 2:
        return "https://usagif.com/wp-content/uploads/gif/anime-hug-26.gif"
    elif plo == 3:
        return "https://usagif.com/wp-content/uploads/gif/anime-hug-37.gif"
    elif plo == 4:
        return "https://usagif.com/wp-content/uploads/gif/anime-hug-72.gif"
    elif plo == 5:
        return "https://usagif.com/wp-content/uploads/gif/anime-hug-57.gif"



@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong !")

@bot.command()
async def love(ctx):
    await ctx.message.add_reaction("❤️")

@bot.command()
async def fac(ctx):
    await ctx.author.send("Voici le lien vers le serveur discord de l'université ! : https://discord.gg/CpUrV8f5")

@bot.command()
async def flip(ctx):
    résultat = pile_ou_face()
    await ctx.send(f"🪙 Tu as fait {résultat}  !")

@bot.command()
async def membres(ctx):
    members = len(ctx.guild.members)
    await ctx.send(f"Il y a actuellement {members} membres dans le serveur !")

@bot.command()
async def hug(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    await ctx.send(f"{ctx.author.mention} fais un câlin à {member.mention}{cln()}")

@bot.command()
async def id(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    await ctx.send(f"Voici l'id de {member.mention}:{member.id} ")
    await ctx.message.add_reaction(f"")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    if amount > 50:
        amount = 50
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"🧹 {amount} messages supprimés !", delete_after=5)

@bot.command()
async def ball(ctx, question):
    rep = ["Oui", "Non", "Peut-être", "Certainement", "certainement pas", "jamais"]
    await ctx.send(f"🎱 {random.choice(rep)}")

bot.run("MTQ2MTEwODQ2MzYzMDQxODA2Mg.Gb6KIW.cAbA886aGNRVXEx-xmkP6nwJ4ZITM0TfSkOgb")
