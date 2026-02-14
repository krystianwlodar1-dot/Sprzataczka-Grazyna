import os
import discord
from discord.ext import commands

# Pobranie tokena z environment variables
TOKEN = os.getenv("DISCORD_TOKEN")

# Intents – do czyszczenia wiadomości potrzebujemy message_content
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')

# Komenda !clean
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clean(ctx, limit: int = 100):
    """
    Czyści wiadomości w kanale. Limit domyślny: 100.
    Można zrobić np. !clean 50
    """
    deleted = await ctx.channel.purge(limit=limit)
    await ctx.send(f'Usunięto {len(deleted)} wiadomości.', delete_after=5)

# Obsługa błędów uprawnień
@clean.error
async def clean_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Nie masz uprawnień do czyszczenia wiadomości!")

bot.run(TOKEN)
