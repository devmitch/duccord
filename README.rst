=====================
Duccord - Discord Bot
=====================

Overview
========

Duck-themed Discord bot with MongoDB integration.

Commands::

  $hi - Say hi to the bot.
  $echo <string> - Echoes a string back to the user.
  $subscribe - Toggles subscription to daily duck picture DMs

Dependencies:
    + discord.py
    + pymongo
    + requests

Build Instructions:

1. Install required packages

2. Rename ``settings.py.example`` to ``settings.py`` and insert your discord bot token in the variable

3. Run ``python3 duccord.py``