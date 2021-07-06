import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(1701601729)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = ""
    DATABASE_URL = ""
    APP_ID = ""
    API_HASH = ""
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(1701601729)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n```𝐅𝐨𝐫𝐜𝐞 𝐠𝐫𝐨𝐮𝐩 𝐦𝐞𝐦𝐛𝐞𝐫𝐬 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐚 𝐬𝐩𝐞𝐜𝐢𝐟𝐢𝐜 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐛𝐞𝐟𝐨𝐫𝐞 𝐬𝐞𝐧𝐝𝐢𝐧𝐠 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬 𝐢𝐧 𝐭𝐡𝐞 𝐠𝐫𝐨𝐮𝐩.\n𝐈 𝐰𝐢𝐥𝐥 𝐦𝐮𝐭𝐞 𝐦𝐞𝐦𝐛𝐞𝐫𝐬 𝐢𝐟 𝐭𝐡𝐞𝐲 𝐧𝐨𝐭 𝐣𝐨𝐢𝐧𝐞𝐝 𝐲𝐨𝐮𝐫 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐚𝐧𝐝 𝐭𝐞𝐥𝐥 𝐭𝐡𝐞𝐦 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐭𝐡𝐞 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐚𝐧𝐝 𝐮𝐧𝐦𝐮𝐭𝐞 𝐭𝐡𝐞𝐦𝐬𝐞𝐥𝐟 𝐛𝐲 𝐩𝐫𝐞𝐬𝐬𝐢𝐧𝐠 𝐚 𝐛𝐮𝐭𝐭𝐨𝐧.```",
        
        "**Setup**\n```𝐅𝐢𝐫𝐬𝐭 𝐨𝐟 𝐚𝐥𝐥 𝐚𝐝𝐝 𝐦𝐞 𝐢𝐧 𝐭𝐡𝐞 𝐠𝐫𝐨𝐮𝐩 𝐚𝐬 𝐚𝐝𝐦𝐢𝐧 𝐰𝐢𝐭𝐡 𝐛𝐚𝐧 𝐮𝐬𝐞𝐫𝐬 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧 𝐚𝐧𝐝 𝐢𝐧 𝐭𝐡𝐞 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐚𝐬 𝐚𝐝𝐦𝐢𝐧.\n𝐍𝐨𝐭𝐞 ⚠️ : 𝐎𝐧𝐥𝐲 𝐜𝐫𝐞𝐚𝐭𝐨𝐫 𝐨𝐟 𝐭𝐡𝐞 𝐠𝐫𝐨𝐮𝐩 𝐜𝐚𝐧 𝐬𝐞𝐭𝐮𝐩 𝐦𝐞 𝐚𝐧𝐝 𝐢 𝐰𝐢𝐥𝐥 𝐥𝐞𝐚𝐯𝐞 𝐭𝐡𝐞 𝐜𝐡𝐚𝐭 𝐢𝐟 𝐢 𝐚𝐦 𝐧𝐨𝐭 𝐚𝐧 𝐚𝐝𝐦𝐢𝐧 𝐢𝐧 𝐭𝐡𝐞 𝐜𝐡𝐚𝐭.```",
        
        "**Commmands**\n```/ForceSubscribe``` - To get the current settings.\n```/ForceSubscribe no/off/disable``` - To turn of ForceSubscribe.\n```/ForceSubscribe {channel username}``` - To turn on and setup the channel.\n```/ForceSubscribe clear``` - To unmute all members who muted by me.\n\nNote: **/FSub is an alias of /ForceSubscribe**",
        
        "**𝐑𝐞𝐩𝐨𝐫𝐭 𝐁𝐮𝐠𝐬 🔽**"
      ]

      START_MSG = "𝐇𝐞𝐲 **[{}](tg://user?id={})**\n𝐈 𝐚𝐦 𝐅𝐨𝐫𝐜𝐞 𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐛𝐞 - 𝐈 𝐜𝐚𝐧 𝐡𝐞𝐥𝐩 𝐲𝐨𝐮 𝐭𝐨 𝐟𝐨𝐫𝐜𝐞 𝐦𝐞𝐦𝐛𝐞𝐫𝐬 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐬𝐩𝐞𝐜𝐢𝐟𝐢𝐜 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐛𝐞𝐟𝐨𝐫𝐞 𝐰𝐫𝐢𝐭𝐢𝐧𝐠 𝐚𝐧𝐲𝐭𝐡𝐢𝐧𝐠 𝐢𝐧 𝐠𝐫𝐨𝐮𝐩 . 𝐉𝐮𝐬𝐭 𝐚𝐧𝐝 𝐦𝐞 𝐢𝐧 𝐨𝐮𝐫 𝐜𝐡𝐚𝐭 𝐚𝐧𝐝 𝐬𝐞𝐭 𝐦𝐞 𝐮𝐩 .\n\n𝐇𝐢𝐭 /help 𝐭𝐨 𝐤𝐧𝐨𝐰 𝐦𝐨𝐫𝐞 .\n\n𝐁𝐨𝐭 𝐢𝐬 𝐩𝐚𝐫𝐭 𝐨𝐟 @DevelopedBots ."
