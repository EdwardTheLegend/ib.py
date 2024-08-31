from discord.ext import commands

from utils.checks import admin_command, staff_command
from utils.commands import available_subcommands


class ChannelOrder(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.hybrid_group(aliases=["co"])
    @staff_command()
    async def channelorder(self, ctx: commands.Context):
        """
        Commands for discord channel arrangement within categories.
        """
        await available_subcommands(ctx)

    @channelorder.command()
    @admin_command()
    async def snapshot(self, ctx: commands.Context, category=None):
        """
        Save the arrangement of channels in a category.
        """

        if not category:
            # Current channel category if no category is provided
            category = ctx.channel.category
        else:
            categories = ctx.guild.categories
            for cat in categories:
                if cat.name.lower() == category.lower():
                    break
                if str(cat.id) == category:
                    break
            else:
                await ctx.send("Category not found.")
                return
            
            category = cat

        channels = category.channels

        await ctx.send(f"Channels are {channels} in category {category}.")
        return

    @channelorder.command(aliases=["r"])
    @staff_command()
    async def rollback(self, ctx: commands.Context):
        """
        Revert the arrangement of channels in a category.
        """
        raise NotImplementedError("Command requires implementation and permission set-up.")

    @channelorder.command(aliases=["l"])
    async def list(self, ctx: commands.Context):
        """
        List the arrangement of channels in a category.
        """
        raise NotImplementedError("Command requires implementation and permission set-up.")


async def setup(bot: commands.Bot):
    await bot.add_cog(ChannelOrder(bot))
