import disnake
from disnake.ext import commands
from disnake import TextInputStyle


bot = commands.Bot(command_prefix="/")


class MyModal(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Login",
                placeholder="Enter your login",
                custom_id="login",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Password",
                placeholder="Enter your password.",
                custom_id="password",
                style=TextInputStyle.short,
            ),
        ]
        super().__init__(title="Create Tag", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        embed = disnake.Embed(title="Tag Creation")
        for key, value in inter.text_values.items():
            embed.add_field(                                                # тут и хранятся данные
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            )
        await inter.response.send_message(embed=embed)


@bot.slash_command()
async def tags(inter: disnake.AppCmdInter):
    await inter.response.send_modal(modal=MyModal())


bot.run("MTA3Mzg2Nzc5OTQ1MTE2MDU4OA.G95JNg.KBfamY0Awy6AYN7y992j_LA0Okx2ZcO_iXuxg8")