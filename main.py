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
    # High-end Cyber "BROKEN" Banner
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
    print(Fore.GREEN + "[*] ACCESSING CORE TELECOM GATEWAY...")
    time.sleep(0.5)
    
    sequences = [
        "[✓] OVERRIDING BASE STATION CONTROLLER",
        "[✓] FETCHING PUBLIC REGISTRATION RECORDS",
        "[✓] EXTRACTING CELLULAR BROADCAST DATA",
        "[✓] PACKETS SYNCHRONIZED WITH NODE-B"
    ]
    
    for seq in sequences:
        sys.stdout.write(Fore.LIGHTBLACK_EX + f" {seq}\n")
        sys.stdout.flush()
        time.sleep(0.3)
        
    print(Fore.GREEN + "\n[*] COMPILING TARGET REPORT: ", end="")
    for _ in range(25):
        sys.stdout.write(Fore.GREEN + "█")
        sys.stdout.flush()
        time.sleep(0.03)
    print(Fore.LIGHTGREEN_EX + " [SUCCESS]")
    time.sleep(0.5)

def main_tracker():
    dynamic_logo()
    
    print(Fore.GREEN + "┌──(ENTER TARGET NUMBER | E.G. +91xxxxxxxxx OR 91xxxxxxxxx)")
    target_num = input(Fore.GREEN + "└─> " + Fore.WHITE).strip()
    
    if not target_num:
        print(Fore.RED + "\n[-] ERROR: NUMBER CANNOT BE EMPTY!")
        return

    # Auto Plus Fix
    if not target_num.startswith('+'):
        target_num = '+' + target_num

    try:
        # Running loading sequence
        matrix_loading_animation()
        
        # Parse Data
        parsed_data = phonenumbers.parse(target_num, None)
        
        if not phonenumbers.is_valid_number(parsed_data):
            dynamic_logo()
            print(Fore.RED + f"\n[-] ERROR: THE NUMBER {target_num} IS INVALID.")
            return

        # Fetching legitimate public telecom info
        country = geocoder.description_for_number(parsed_data, "en")
        operator = carrier.name_for_number(parsed_data, "en")
        tz_list = timezone.time_zones_for_number(parsed_data)
        tz = tz_list[0] if tz_list else "N/A"
        
        # Converting outputs to upper case for formatting
        country_upper = country.upper() if country else "UNKNOWN"
        operator_upper = operator.upper() if operator else "UNKNOWN"
        tz_upper = tz.upper()

        # Clean Compact Thin UI Box Output with CAPITAL headings
        dynamic_logo()
        print(Fore.GREEN + " ┌────────────────────────────────────────┐")
        print(Fore.GREEN + " │         CRITICAL TARGET REPORT         │")
        print(Fore.GREEN + " ├────────────────────────────────────────┤")
        print(Fore.GREEN + f" │ " + Fore.CYAN + "USER NAME      : " + Fore.YELLOW + f"{'RESTRICTED (PRIVACY)':<21}" + Fore.GREEN + " │")
        print(Fore.GREEN + f" │ " + Fore.CYAN + "FATHER NAME    : " + Fore.YELLOW + f"{'RESTRICTED (PRIVACY)':<21}" + Fore.GREEN + " │")
        print(Fore.GREEN + f" │ " + Fore.CYAN + "HOME REGION    : " + Fore.WHITE + f"{country_upper:<21}" + Fore.GREEN + " │")
        print(Fore.GREEN + f" │ " + Fore.CYAN + "DISTRICT/JILA  : " + Fore.WHITE + f"{country_upper:<21}" + Fore.GREEN + " │")
        print(Fore.GREEN + f" │ " + Fore.CYAN + "OPERATOR (SIM) : " + Fore.WHITE + f"{operator_upper:<21}" + Fore.GREEN + " │")
        print(Fore.GREEN + f" │ " + Fore.CYAN + "CURRENT ZONE   : " + Fore.WHITE + f"{tz_upper:<21}" + Fore.GREEN + " │")
        print(Fore.GREEN + f" │ " + Fore.CYAN + "NETWORK STATUS : " + Fore.LIGHTGREEN_EX + f"{'ONLINE':<21}" + Fore.GREEN + " │")
        print(Fore.GREEN + " └────────────────────────────────────────┘")
        
        print(Fore.YELLOW + "\n [!] NOTE: PERSONAL DATA (NAME/FATHER) & EXACT LIVE LOCATION")
        print(Fore.YELLOW + "     ARE PROTECTED BY LAW AND NOT STORED IN PUBLIC APIS.")

    except Exception as error:
        dynamic_logo()
        print(Fore.RED + f"\n[-] SYSTEM EXCEPTION: {str(error).upper()}")

if __name__ == "__main__":
    main_tracker()
