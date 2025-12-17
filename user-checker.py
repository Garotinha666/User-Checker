import asyncio
import aiohttp
import random
import string
import os
from colorama import init, Fore, Style
from cfonts import render

init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')

AVAILABLE = "available.txt"

PLATFORMS = {
    "1": ("Instagram", "https://i.instagram.com/api/v1/users/web_profile_info/?username={}",
          {"User-Agent": "Instagram 292.0.0.19.93 Android", "x-ig-app-id": "936619743392459"}),
    "2": ("Twitter/X", "https://api.twitter.com/2/users/by/username/{}?user.fields=created_at",
          {"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"}),
    "3": ("TikTok", "https://www.tiktok.com/api/search/user/?keyword={}&cursor=0"),
    "4": ("YouTube", "https://www.googleapis.com/youtube/v3/channels?part=id&forUsername={}&key=AIzaSyC9XL3ZjWddXya1AemN0lrZ3db4bxF5f4"),
    "5": ("Twitch", "https://api.twitch.tv/helix/users?login={}",
          {"Client-ID": "kimne78kx3ncx6brgo4mv6wki5h1ko", "Accept": "application/json"}),
    "6": ("GitHub", "https://api.github.com/users/{}"),
    "7": ("Discord", "https://discord.com/api/v9/users/{}",
      {"Authorization": "SEU_DISCORD_TOKEN_AQUI"}),,
}

# Banner + Credit
banner = render("USER CHECKER", colors=['cyan', 'white'], align='center', font='block')
print(f"{Fore.CYAN}{banner}{Style.RESET_ALL}")
print(f"{Fore.WHITE}           Advanced Username Availability Checker")
print(f"{Fore.MAGENTA}                    made by VaiXourar\n{Style.RESET_ALL}")

for k in sorted(PLATFORMS):
    print(f"{Fore.WHITE}[{Fore.CYAN}{k}{Fore.WHITE}] {PLATFORMS[k][0]}")
print(f"{Fore.CYAN}{'~' * 45}{Style.RESET_ALL}\n")

choice = input(f"{Fore.YELLOW}Select platform (1-7): {Fore.WHITE}")
if choice not in PLATFORMS:
    exit(f"{Fore.RED}Invalid choice!")

name = PLATFORMS[choice][0]
url_template = PLATFORMS[choice][1]
headers_base = PLATFORMS[choice][2] if len(PLATFORMS[choice]) > 2 else {}

mode = input(f"{Fore.YELLOW}[1] Check from users.txt   [2] Generate random\nChoose: {Fore.WHITE}")
if mode not in ["1", "2"]:
    exit()

async def save(user):
    with open(AVAILABLE, "a", encoding="utf-8") as f:
        f.write(f"{name}: @{user}\n")

async def check(session, user):
    url = url_template.format(user)
    headers = headers_base.copy()
    headers.setdefault("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")

    try:
        timeout = aiohttp.ClientTimeout(total=9)
        async with session.get(url, headers=headers, timeout=timeout) as r:
            text = await r.text()

            # Instagram, GitHub, Discord → 404 = available
            if choice in ["1", "6", "7"]:
                if r.status == 404 or "Not Found" in text:
                    print(f"{Fore.GREEN}[AVAILABLE] @{user} → {name}")
                    await save(user)
                else:
                    print(f"{Fore.RED}[TAKEN] @{user}")
            # Twitter/X
            elif choice == "2":
                if r.status == 404 or "Could not find" in text:
                    print(f"{Fore.GREEN}[AVAILABLE] @{user} → Twitter/X")
                    await save(user)
                else:
                    print(f"{Fore.RED}[TAKEN] @{user}")
            # TikTok, YouTube, Twitch
            else:
                if r.status != 200 or "[]" in text or '"user_list": []' in text or '"items": []' in text:
                    print(f"{Fore.GREEN}[AVAILABLE] @{user} → {name}")
                    await save(user)
                else:
                    print(f"{Fore.RED}[TAKEN] @{user}")
    except asyncio.TimeoutError:
        print(f"{Fore.YELLOW}[TIMEOUT] @{user} → skipped")
    except:
        pass  # Silent fail on any error

async def main():
    connector = aiohttp.TCPConnector(limit=500, ssl=False)
    timeout = aiohttp.ClientTimeout(total=12)
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as s:
        if mode == "1":
            if not os.path.exists("users.txt"):
                open("users.txt", "w", encoding="utf-8").close()
                print(f"{Fore.CYAN}Created empty users.txt")
            users = [line.strip().lstrip("@") for line in open("users.txt", encoding="utf-8") if line.strip()]
            print(f"\n{Fore.CYAN}Checking {len(users)} usernames...\n")
            for u in users:
                await check(s, u)
                await asyncio.sleep(0.18)

        else:
            try:
                length = int(input(f"{Fore.CYAN}Username length (4-15) → 6: ") or 6)
                amount = int(input(f"{Fore.CYAN}Amount to generate → 1000: ") or 1000)
            except:
                length, amount = 6, 1000

            chars = string.ascii_lowercase + string.digits + "_"
            print(f"\n{Fore.MAGENTA}Generating & checking {amount} random usernames (length {length})...\n")
            for _ in range(amount):
                u = ''.join(random.choices(chars, k=length))
                await check(s, u)
                await asyncio.sleep(0.16)

    done = render("FINISHED", colors=['green', 'cyan'], align='center', font='block')
    print(f"\n{Fore.GREEN}{done}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Available usernames saved → {AVAILABLE}")
    print(f"{Fore.MAGENTA}                made by ice.o1 🔥")
    input(f"\n{Fore.WHITE}Press Enter to exit...")

asyncio.run(main())
