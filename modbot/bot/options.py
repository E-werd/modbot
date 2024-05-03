# External
from interactions import SlashCommandChoice
# Internal
from modbot.core.astrology import ZodiacSign


class Options:
    @staticmethod
    def choice_zodiac() -> list:
        """Generate choices for zodiac signs.

        Returns:
            list: A list of slash command choices.
        """
        out: list[SlashCommandChoice]   = []
        full: str                       = ""

        for sign in ZodiacSign:
            full = sign.symbol + " " + sign.full
            out.append(SlashCommandChoice(name=full, value=sign.name))

        return out