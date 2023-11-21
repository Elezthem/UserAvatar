import nextcord
from nextcord.ext import commands

# другие импорты и настройки

bot = commands.Bot(command_prefix='.')

# другие команды и события

@bot.command(usage="[user]")
async def avatar(ctx, *, user: nextcord.Member = None):
    """
    `.avatar @user` - and **/** `/avatar`
    """
    if user is None:
        user = ctx.author

    embed = nextcord.Embed(
        title=f"Avatar for {user.name}",
        color=0x2b2d31
    )
    embed.set_image(url=user.display_avatar.url)

    await ctx.send(embed=embed)

# запуск бота
bot.run("YOUR_BOT_TOKEN")
