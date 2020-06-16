from userbot.system import command, bot

@command(pattern="^.lore ?(.*)")
async def lore(event):
    await bot.send_message(event.chat_id, "Lore è un figo")