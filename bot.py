#!/usr/bin/python
# -- coding: utf-8 -
import discord

bot = discord.Client()
mat = ["хуй","пидор","сука","нахуй"]
@bot.event
async def on_message(message):
    mes = message.content
    user = message.author
    arg = "Асужденный"
    role_mat = discord.utils.get(message.guild.roles, name=str(arg))
    if mes.lower() in mat:
        await user.add_roles(str(role_mat))


bot.run("NzE0NzQyNDY3OTI0MTk3NDc2.XszFyw.P7paOTijc2qerB7yelDWGpHnWy8")
