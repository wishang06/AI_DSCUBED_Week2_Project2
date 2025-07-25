"""
This file contains the UI components for the discord bot, including:
- Yes/No Button View
- Interaction check
"""

from typing import Optional

import discord


class YesNoView(discord.ui.View):
    def __init__(self, timeout: Optional[float]) -> None:
        super().__init__(timeout=timeout)
        self.value: Optional[bool] = None

    @discord.ui.button(label="Yes", style=discord.ButtonStyle.green)
    async def yes_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button[discord.ui.View],
    ) -> None:
        self.value = True
        await interaction.response.defer()
        self.stop()

    @discord.ui.button(label="No", style=discord.ButtonStyle.red)
    async def no_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button[discord.ui.View],
    ) -> None:
        self.value = False
        await interaction.response.defer()
        self.stop()
