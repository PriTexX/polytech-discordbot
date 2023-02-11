import disnake
from disnake.ext import commands
from disnake import TextInputStyle


bot = commands.Bot(command_prefix="!")


class MyModal(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Login",
                placeholder="Foo Tag",
                custom_id="name",
                style=TextInputStyle.short,
                max_length=50,
            )
        ]
        super().__init__(title="Create Tag", components=components)

    # The callback received when the user input is completed.
    async def callback(self, inter: disnake.ModalInteraction):
        embed = disnake.Embed(title="Tag Creation")
        for key, value in inter.text_values.items():
            embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            )
        await inter.response.send_message(embed=embed)


@bot.slash_command()
async def tags(inter: disnake.AppCmdInter):
    """Sends a Modal to create a tag."""
    await inter.response.send_modal(modal=MyModal())


bot.run("MTA3Mzg2Nzc5OTQ1MTE2MDU4OA.Gg0bfW.2Y2Jh482e-GBjxj7JPQypBmZGdEVt6V6BbNYjM")