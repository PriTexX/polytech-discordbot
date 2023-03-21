import discord
from core.entity import BagReport


async def sendBagReport(interaction: discord.Interaction, bag_report: BagReport):
    embed = discord.Embed(color=discord.Color.brand_red())
    embed.add_field(name="Author: ", value=bag_report.user.mention, inline=False)
    embed.add_field(name="Author's fullname: ", value=bag_report.fullName, inline=False)
    embed.add_field(name="Group: ", value=bag_report.group, inline=False)
    embed.add_field(name="Server: ", value=bag_report.server, inline=False)
    embed.add_field(name="Problem: ", value=bag_report.bag_report_message, inline=False)
    embed.set_thumbnail(url=bag_report.user.display_avatar.url)

    await interaction.client.me.send(embed=embed)

    await interaction.response.send_message("Сообщение об ошибке было успешно отправлено!", ephemeral=True, delete_after=120)
