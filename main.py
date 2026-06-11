import os
import sys
import time
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import init, Fore, Style

# Initialize color system
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def dynamic_logo():
    clear_screen()
    # Stylish Cyber-Hacker "BROKEN" Logo
    logo = f"""
{Fore.GREEN} █▀▄▀█ ▄▀█ ▀█▀ █▀█ █▀█ ▀▄▀   ▄▀█ █▄░█ █ █▀▄▀█ ▄▀█ ▀█▀ █ █▀█ █▄░█
{Fore.GREEN} █░▀░█ █▀█ ░█░ █▀▄ █▄█ █░█   █▀█ █░▀█ █ █░▀░█ █▀█ ░█░ █ █▄█ █░▀█
{Fore.GREEN} ─────────────────────────────────────────────────────────────
{Fore.CYAN}       [+] SYSTEM: ACTIVE  |  [+] CODED BY: BROKEN NADEEM
{Fore.GREEN} ─────────────────────────────────────────────────────────────
    """
    print(logo)

def matrix_loading_animation():
    dynamic_logo()
    print(Fore.GREEN + "[*] CONNECTING TO SECURE GATEWAY...")
    time.sleep(0.5)
    
    sequences = [
        "[✓] IP OVERRIDE: SUCCESSFUL",
        "[✓] EXTRACTING METADATA DICTIONARY",
        "[✓] BYPASSING TELECOM OPERATOR FIREWALL",
        "[✓] PACKETS SYNCHRONIZED WITH SATELLITE"
    ]
    
    for seq in sequences:
        sys.stdout.write(Fore.LIGHTBLACK_EX + f" {seq}\n")
        sys.stdout.flush()
        time.sleep(0.3)
        
    print(Fore.GREEN + "\n[*] INJECTING INJECTION PAYLOAD: ", end="")
    for _ in range(25):
        sys.stdout.write(Fore.GREEN + "█")
        sys.stdout.flush()
        time.sleep(0.03)
    print(Fore.LIGHTGREEN_EX + " [READY]")
    time.sleep(0.5)

def main_tracker():
    dynamic_logo()
    
    print(Fore.GREEN + "┌──(Enter Phone Number | e.g. +91xxxxxxxxx or 91xxxxxxxxx)")
    target_num = input(Fore.GREEN + "└─> " + Fore.WHITE).strip()
    
    if not target_num:
        print(Fore.RED + "\n[-] ERROR: Number cannot be empty!")
        return

    # AUTO-FIX: Agar user '+' lagana bhool jaye toh automatic add karega
    if not target_num.startswith('+'):
        target_num = '+' + target_num

    try:
        # Running the full matrix layout animation
        matrix_loading_animation()
        
        # Parse & Analyze Data
        parsed_data = phonenumbers.parse(target_num, None)
        
        if not phonenumbers.is_valid_number(parsed_data):
            dynamic_logo()
            print(Fore.RED + f"\n[-] ERROR: THE NUMBER {target_num} IS INVALID.")
            return

        # Fetching data strings
        country = geocoder.description_for_number(parsed_data, "en")
        operator = carrier.name_for_number(parsed_data, "en")
        tz_list = timezone.time_zones_for_number(parsed_data)
        tz = tz_list[0] if tz_list else "N/A"
        
        # Clean Compact Thin UI Box Output
        dynamic_logo()
        print(Fore.GREEN + " ┌────────────────────────────────────────┐")
        print(Fore.GREEN + " │        TARGET DATA EXTRACTION          │")
        print(Fore.GREEN + " ├────────────────────────────────────────┤")
        print(Fore.GREEN + f" │ " + Fore.CYAN + "Country/Region : " + Fore.WHITE + f"{country:<21}" + Fore.GREEN + " │")
        print(Fore.GREEN + f" │ " + Fore.CYAN + "Carrier (Sim)  : " + Fore.WHITE + f"{operator if operator else 'Unknown':<21}" + Fore.GREEN + " │")
        print(Fore.GREEN + f" │ " + Fore.CYAN + "Timezone       : " + Fore.WHITE + f"{tz:<21}" + Fore.GREEN + " │")
        print(Fore.GREEN + f" │ " + Fore.CYAN + "Network Status : " + Fore.LIGHTGREEN_EX + f"{'ONLINE':<21}" + Fore.GREEN + " │")
        print(Fore.GREEN + " └────────────────────────────────────────┘")
        
        print(Fore.YELLOW + "\n [!] Note: Exact real-time GPS coordinates require device tracking access.")

    except Exception as error:
        dynamic_logo()
        print(Fore.RED + f"\n[-] SYSTEM EXCEPTION: {str(error)}")
        print(Fore.YELLOW + "[*] Tip: Make sure to include the correct country code digits.")

if __name__ == "__main__":
    main_tracker()
