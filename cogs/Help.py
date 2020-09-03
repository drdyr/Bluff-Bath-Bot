from discord.ext import commands
import discord


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        commands = discord.Embed(
            colour=discord.Colour.dark_green(),
            type='rich',
        )
        commands.set_author(name="ALL COMMANDS (prefix with -bb) ")
        commands.add_field(name='help', value='Displays all bot commands.', inline=False)
        commands.add_field(name='links', value='Collection of web pages to learn how to play.')
        commands.add_field(name='hand rankings', value='Displays poker hands from strongest to weakest.',
                           inline=False)
        commands.add_field(name='blinds', value='Brief explanation of blinds in poker.', inline=False)

        await ctx.send(embed=commands)

    @commands.command()
    async def rankings(self, ctx):
        hand_rankings = discord.Embed(
            colour=discord.Colour.dark_green(),
            type='rich',
            description="In the most popular variant of Poker, Texas Hold 'Em, each player takes the 2 cards initially dealt to them and matches them with 3 of the 5 community cards to construct the best 5 card hand.",
        )
        hand_rankings.set_author(name='POKER HAND RANKINGS', )
        hand_rankings.set_image(
            url='https://cdn.discordapp.com/attachments/746084637427630105/746708442030538762/unknown.png')

        await ctx.send(embed=hand_rankings)

    @commands.command()
    async def blinds(self, ctx):
        blinds = discord.Embed(
            colour=discord.Colour.dark_green(),
            type='rich',
            description="At the end of each hand, the dealer (button) moves once clockwise. Next hand, there are 2 mandatory bets which must be placed before any cards are dealt: small blind and big blind. The small blind is always left to dealer and big blind left to small blind. The big blind is almost always double the small blind. The dealer will then deal 2 cards, one at a time, to each player starting with the player to the left. "
        )
        blinds.set_author(name='BLINDS', )
        blinds.set_image(
            url='https://cdn.discordapp.com/attachments/746084637427630105/746728383727140935/1200px-Texas_Hold27em_Poker_Table_with_Blinds.png')

        await ctx.send(embed=blinds)

    @commands.command()
    async def links(self, ctx):
        links = discord.Embed(
            colour=discord.Colour.dark_green(),
            type='rich',
            description='Collection of web pages to learn how to play:'
        )
        links.set_author(name='LINKS')
        links.add_field(name='Tutorials',
                        value='https://uk.pokernews.com/poker-rules/texas-holdem.htm\nhttps://www.palapoker.com/texas-holdem/\nhttps://www.partypoker.com/en/how-to-play/texas-holdem')

        await ctx.send(embed=links)


def setup(bot):
    bot.remove_command("help")
    bot.add_cog(Help(bot))

