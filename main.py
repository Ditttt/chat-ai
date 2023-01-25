import aiohttp
import asyncio
import sys
from utils import ChatGpt
import subprocess
import time

subprocess.call("clear", shell=True)
index = 0
while True:
    index += 1
    if index > 1:
        time.sleep(3)
        exit = input(
            "Ketik Quit/Q Jika Ingin Keluar/Berhenti, Ketik Yes/Y Jika Ingin Lanjut : "
        ).title()
        match exit:
            case "Quit":
                subprocess.call("clear", shell=True)
                sys.exit()
            case "Q":
                subprocess.call("clear", shell=True)
                sys.exit()
            case "Y":
                subprocess.call("clear", shell=True)
            case "Yes":
                subprocess.call("clear", shell=True)
            case _:
                teks = "Input tidak valid, silahkan coba lagi".title()
                print(f'\033[1m\033[31m{teks}\033[0m\033[0m')
                continue
    inp = input(
        f"""

\033[34m░█████╗░██╗░░██╗░█████╗░████████╗  ██████╗░░█████╗░████████╗  ██████╗░██╗░░░██╗
██╔══██╗██║░░██║██╔══██╗╚══██╔══╝  ██╔══██╗██╔══██╗╚══██╔══╝  ██╔══██╗╚██╗░██╔╝
██║░░╚═╝███████║███████║░░░██║░░░  ██████╦╝██║░░██║░░░██║░░░  ██████╦╝░╚████╔╝░
██║░░██╗██╔══██║██╔══██║░░░██║░░░  ██╔══██╗██║░░██║░░░██║░░░  ██╔══██╗░░╚██╔╝░░
╚█████╔╝██║░░██║██║░░██║░░░██║░░░  ██████╦╝╚█████╔╝░░░██║░░░  ██████╦╝░░░██║░░░
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░  ╚═════╝░░╚════╝░░░░╚═╝░░░  ╚═════╝░░░░╚═╝░░░

██████╗░██╗████████╗████████╗████████╗████████╗
██╔══██╗██║╚══██╔══╝╚══██╔══╝╚══██╔══╝╚══██╔══╝
██║░░██║██║░░░██║░░░░░░██║░░░░░░██║░░░░░░██║░░░
██║░░██║██║░░░██║░░░░░░██║░░░░░░██║░░░░░░██║░░░
██████╔╝██║░░░██║░░░░░░██║░░░░░░██║░░░░░░██║░░░
╚═════╝░╚═╝░░░╚═╝░░░░░░╚═╝░░░░░░╚═╝░░░░░░╚═╝░░░\033[34m

\033[1m\033[31mMungkin Jawaban/Informasi Yang Diberikan Bisa Saja Salah\033[0m\033[0m

Silahkan Masukkan Pertanyaan Yang Kamu ingin Tanyakan : """
    )
    try:
        res = asyncio.run(ChatGpt.chat_gpt(inp))
    except:
        pass
    print(
        f"""
🇶 : \033[94m{inp}\033[0m
🇦 : {res}
"""
    )
