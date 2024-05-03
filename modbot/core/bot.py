# External
import logging
from interactions import (AutoShardedClient, listen)
from interactions.api.events import (Startup, Ready, Login, Disconnect)
# Internal
from modbot.bot.commands import Commands


class Bot(AutoShardedClient, Commands):
    """Wrapped class for interactions.py client.
    """
    def __init__(self, token: str):
        """Wrapped class for interactions.py client.

        Args:
            token (str): Token for bot authentication.
        """
        # Call parent class initialization
        AutoShardedClient.__init__(self, token=token)
        Commands.__init__(self)

    # Event Listeners
    @listen(Startup)
    async def event_startup(self):
        pass

    @listen(Login)
    async def event_login(self):
        logging.info(f"LOGIN: Logged on as: {self.app.name}")

    @listen(Ready)
    async def event_ready(self):
        logging.info("READY: Bot is ready.")

    @listen(Disconnect)
    async def event_disconnect(self):
        logging.info("DISCONNECT: Stopping bot.")