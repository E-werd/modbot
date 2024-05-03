# External
import logging
from interactions import (OptionType, slash_command, slash_option, SlashContext, Embed)
# Internal
from modbot.bot.options import Options


class Commands:
    def __init__(self) -> None:
        """Commands for the bot.

        Args:
        data (Data): The Data object holding data.
        """
        pass

    # Commands
    @slash_command(
            name="horoscope",
            description="Show horoscope for specified sign"
        )
    @slash_option(
            name="sign",
            description="zodiac sign",
            opt_type=OptionType.STRING,
            required=True,
            choices=Options.choice_zodiac()
            )
    async def horoscope(self, ctx: SlashContext, sign: str):
        # Prepare data for horoscope fetch
        _sign: str      = sign

        # Log request
        logging.info(f"Received 'horoscope' request from '{ctx.user.username}' [{ctx.author_id}] with parameters: sign: {_sign}")

        await ctx.send(_sign)