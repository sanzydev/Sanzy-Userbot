# Copyright by (C) 2020-2023 by TgCatUB@Github.

from SanzyDev import CMD_HELP
from SanzyDev.sanzy import (
    sanzy_cmd,
    eod,
    eor,
)
from ..sanzy.aihelp import (
    gen_edited_resp,
    gen_resp
)
from . import cmd


@sanzy_cmd(pattern=r"ai(?:\s|$)([\s\S]*)")
async def chatgpt(event):
    text = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    chat_id = event.chat_id
    if "-r" in text:
        text = text.replace("-r", "").strip()
        if not reply or not reply.text or not text:
            return await eod(
                event,
                "Balas ke pesan dan berikan pesan instruksi setelah tag -r.__",
            )
        await eor(event, "`Searching edited text..`")
        response = gen_edited_resp(reply.text, text)
        return await eor(event, response)
    if not text and reply:
        text = reply.text
    if not text:
        return await eod(event, "Berikan Saya sebuah text ")

    sanzyevent = await eor(event, "__Searching...__")
    gptresp = gen_resp(text, chat_id)
    await eor(sanzyevent, gptresp)

CMD_HELP.update(
    {
        "Open AI": f"**Plugin : **`Open AI`\
        \n\n  »  **Perintah :** `{cmd}ai` <berikan text>\
        \n  »  **Kegunaan : **Untuk Bertanya Kepada ChatGPT.\
        \n\n  »  **Perintah :** `{cmd}ai -r` <sambil reply chat>\
        \n  »  **Kegunaan : **Untuk Bertanya Kepada ChatGPT dari pertanyaan orang pesan orang lain.\
    "
    }
)
