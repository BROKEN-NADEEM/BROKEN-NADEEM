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

def stylish_upper_box(title, data_dict):
    """Print a fully uppercase, stylish report box"""
    print(Fore.GREEN + " ╔══════════════════════════════════════════════════╗")
    print(Fore.GREEN + " ║" + Fore.CYAN + f" {title.upper():^46}" + Fore.GREEN + "║")
    print(Fore.GREEN + " ╠══════════════════════════════════════════════════╣")
    for key, value in data_dict.items():
        key_upper = key.upper()
        val_upper = str(value).upper()
        print(Fore.GREEN + f" ║ {Fore.CYAN}{key_upper:<14}{Fore.GREEN}: {Fore.WHITE}{val_upper:<29}{Fore.GREEN}║")
    print(Fore.GREEN + " ╚══════════════════════════════════════════════════╝")

def main_tracker():
    dynamic_logo()
    
    print(Fore.GREEN + "┌──(ENTER TARGET NUMBER | E.G. +91XXXXXXXXXX OR 91XXXXXXXXXX)")
    target_num = input(Fore.GREEN + "└─> " + Fore.WHITE).strip()
    
    if not target_num:
        print(Fore.RED + "\n[-] ERROR: NUMBER CANNOT BE EMPTY!")
        return

    # Auto-add plus sign
    if not target_num.startswith('+'):
        target_num = '+' + target_num

    try:
        # Running loading sequence
        matrix_loading_animation()
        
        # Parse phone number
        parsed_data = phonenumbers.parse(target_num, None)
        
        if not phonenumbers.is_valid_number(parsed_data):
            dynamic_logo()
            print(Fore.RED + f"\n[-] ERROR: THE NUMBER {target_num} IS INVALID.")
            return

        # Fetch real public telecom info
        country = geocoder.description_for_number(parsed_data, "en")
        operator = carrier.name_for_number(parsed_data, "en")
        tz_list = timezone.time_zones_for_number(parsed_data)
        tz = tz_list[0] if tz_list else "N/A"
        
        # Convert to uppercase for stylish display
        country_upper = country.upper() if country else "UNKNOWN"
        operator_upper = operator.upper() if operator else "UNKNOWN"
        tz_upper = tz.upper()

        # Prepare all data fields (personal ones are privacy protected)
        report_data = {
            "USER NAME": "🔒 RESTRICTED (PRIVACY)",
            "FATHER NAME": "🔒 RESTRICTED (PRIVACY)",
            "HOME DISTRICT": "🔒 RESTRICTED (PRIVACY)",
            "CURRENT LOCATION": "🔒 RESTRICTED (PRIVACY)",
            "COUNTRY/REGION": country_upper,
            "SIM OPERATOR": operator_upper,
            "TIME ZONE": tz_upper,
            "NETWORK STATUS": "ONLINE"
        }

        dynamic_logo()
        stylish_upper_box("CRITICAL TARGET REPORT", report_data)
        
        print(Fore.YELLOW + "\n ⚠️  NOTE: PERSONAL DATA (NAME/FATHER/EXACT LOCATION) IS PROTECTED BY LAW")
        print(Fore.YELLOW + "     AND NOT STORED IN PUBLIC APIS. THE ABOVE PRIVATE FIELDS ARE")
        print(Fore.YELLOW + "     SHOWN AS RESTRICTED FOR LEGAL & ETHICAL REASONS.")

    except Exception as error:
        dynamic_logo()
        print(Fore.RED + f"\n[-] SYSTEM EXCEPTION: {str(error).upper()}")

if __name__ == "__main__":
    main_tracker()
