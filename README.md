# ModBot

This is intended to be a general-purpose bot for Discord. The idea is to have a blank canvas with a simple module API to easily expand without writing a whole bot, just the fun parts.

Written with 3.12 in mind, but requires Python 3.10+ due to interactions.py requirements. See [requirements.txt](requirements.txt) for more information about dependencies.

Bot code based on [interactions.py](https://interactions-py.github.io/interactions.py/).

Requires tokens for Discord in ```.env```, see [.env.example](.env.example).

Run with ```python3 -m modbot``` or ```run.sh```.