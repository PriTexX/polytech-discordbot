import discord

from ui import BagReportModalComponent
from core.entity import BagReport
from services import sendBagReport


class BagReportButtonComponent(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Сообщить об ошибке", style=discord.ButtonStyle.danger, custom_id="bag-report-btn")
    async def button_click(self, interaction: discord.Interaction, button):
        bag_report_modal = BagReportModalComponent()
        await interaction.response.send_modal(bag_report_modal)

        if await bag_report_modal.wait():  # Вернет False при timeout или если пользователь закроет окно
            return

        bag_report = BagReport(bag_report_modal.fullNameInput, bag_report_modal.groupInput, interaction.user,
                               interaction.guild.name, bag_report_modal.problemReportInput)

        await sendBagReport(bag_report_modal.interaction, bag_report)
