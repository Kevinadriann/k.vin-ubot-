from userbot import CMD_HELP, bot
from userbot.events import register


# Port By @VckyouuBitch From GeezProject
# Untuk Siapapun Yang Hapus Credits Ini, Kamu Anjing:)
@register(outgoing=True, pattern=r"^\.tmsg (.*)")
async def _(event):
    k = await event.get_reply_message()
    if k:
        a = await bot.get_messages(event.chat_id, 0, from_user=k.sender_id)
        return await event.edit(f"Total Message Dari {u}. Total Chats `{a.total}`")
    u = event.pattern_match.group(1)
    if not u:
        u = "me"
    a = await bot.get_messages(event.chat_id, 0, from_user=u)
    await event.edit(f"Total Message Dari {u}. Total Chats `{a.total}`")


CMD_HELP.update(
    {
        "totalmsg": "πΎπ€π’π’ππ£π: `.tmsg` | `.tmsg` <username>\
    \nβ³ : Mengembalikan jumlah pesan total pengguna dalam obrolan saat ini."
    }
)
