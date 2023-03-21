import discord

class BagReportModalComponent(discord.ui.Modal, title="Окно авторизации"):
    def __init__(self):
        super().__init__()
        self.timeout = 240
        self.interaction = None

    fullNameInput = discord.ui.TextInput(label="Введите ФИО: ", style=discord.TextStyle.short, required=True, max_length=50)
    groupInput = discord.ui.TextInput(label="Введите учебную группу: ", required=True, max_length=20)
    problemReportInput = discord.ui.TextInput(label="Опишите вашу проблему: ", required=True, style=discord.TextStyle.long, max_length=200)

    async def on_submit(self, interaction: discord.Interaction):
        self.interaction = interaction
        self.stop()
