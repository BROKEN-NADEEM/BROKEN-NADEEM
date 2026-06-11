import os
import sys
import time
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import init, Fore, Style

# Initialize Colorama for neon style
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def hacker_banner():
    clear_screen()
    print(Fore.GREEN + Style.BRIGHT + """
 █▄▄ █▀█ █▀█ █▄▀ █▀▀ █▄░█   █▄░█ ▄▀█ █▀▄ █▀▀ █▀▀ █▀▄▀█
 █▄█ █▀▄ █▄█ █░█ ██▄ █░▀█   █░▀█ █▀█ █▄▀ ██▄ ██▄ █░▀░█
 ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀   ▀▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀░░░▀
 ─────────────────────────────────────────────────────
         [+] SYSTEM: ONLINE | AUTH: BROKEN NADEEM [+]
 ─────────────────────────────────────────────────────
    """)

def scan_animation():
    print(Fore.GREEN + "\n[*] INITIALIZING SATELLITE LINK...")
    time.sleep(1)
    sys.stdout.write(Fore.CYAN + "[*] FETCHING CARRIER DATA: ")
    for _ in range(20):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(0.05)
    print(Fore.GREEN + " [SUCCESS]")
    time.sleep(0.5)

def track_number():
    hacker_banner()
    
    # Input with style
    print(Fore.GREEN + "┌──(Enter Target Number with Country Code, e.g., +91xxxxxxxxx)")
    raw_number = input(Fore.GREEN + "└─> " + Fore.WHITE)
    
    if not raw_number.strip():
        print(Fore.RED + "\n[-] Error: Number cannot be empty!")
        return

    try:
        scan_animation()
        
        # Parsing number
        parsed_num = phonenumbers.parse(raw_number, None)
        
        if not phonenumbers.is_valid_number(parsed_num):
            print(Fore.RED + "\n[-] ERROR: INVALID TARGET NUMBER.")
            return

        # Fetching Information
        country_location = geocoder.description_for_number(parsed_num, "en")
        service_provider = carrier.name_for_number(parsed_num, "en")
        time_zones = timezone.time_zones_for_number(parsed_num)

        # Display Results in a compact, clean layout
        print(Fore.GREEN + "\n ┌─────────────────────────────────────────┐")
        print(Fore.GREEN + " │           TARGET INFO EXTRACTED         │")
        print(Fore.GREEN + " ├─────────────────────────────────────────┤")
        print(Fore.GREEN + f" │ " + Fore.CYAN + "Country/State : " + Fore.WHITE + f"{country_location:<23}" + Fore.GREEN + " │")
        print(Fore.GREEN + f" │ " + Fore.CYAN + "Carrier (Sim) : " + Fore.WHITE + f"{service_provider if service_provider else 'Unknown':<23}" + Fore.GREEN + " │")
        print(Fore.GREEN + f" │ " + Fore.CYAN + "Timezone      : " + Fore.WHITE + f"{time_zones[0]:<23}" + Fore.GREEN + " │")
        print(Fore.GREEN + f" │ " + Fore.CYAN + "Status        : " + Fore.LIGHTGREEN_EX + f"{'ACTIVE':<23}" + Fore.GREEN + " │")
        print(Fore.GREEN + " └─────────────────────────────────────────┘")
        
        print(Fore.YELLOW + "\n[!] Note: Real-time exact GPS location requires device permission or GPS logs.")

    except Exception as e:
        print(Fore.RED + f"\n[-] AN ERROR OCCURRED: {str(e)}")

if __name__ == "__main__":
    track_number()
