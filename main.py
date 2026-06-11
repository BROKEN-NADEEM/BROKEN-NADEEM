import os
import sys
import time
import random
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import init, Fore, Style

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
{Fore.RED}       [!!!] DEMO MODE: FAKE PERSONAL DATA FOR UI TESTING
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

def generate_fake_indian_data():
    """Generate realistic fake data for demo (never claims to be real)"""
    first_names = ["RAHUL", "PRIYA", "AMIT", "NEHA", "VIKAS", "POOJA", "RAJ", "ANJALI"]
    last_names = ["VERMA", "SHARMA", "KUMAR", "SINGH", "GUPTA", "PATEL"]
    user_name = f"{random.choice(first_names)} {random.choice(last_names)}"
    father_names = [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(10)]
    father_name = random.choice(father_names)
    districts = ["NORTH DELHI", "SOUTH MUMBAI", "EAST BANGALORE", "WEST CHENNAI", "CENTRAL KOLKATA", "JAIPUR CITY", "LUCKNOW CENTRAL"]
    home_district = random.choice(districts)
    locations = ["NEAR METRO STATION", "OPPOSITE CITY HOSPITAL", "BEHIND MAIN MARKET", "RESIDENTIAL COLONY A", "COMMERCIAL COMPLEX", "NEAR RAILWAY STATION"]
    current_location = random.choice(locations)
    return user_name, father_name, home_district, current_location

def stylish_upper_box(title, data_dict):
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
    print(Fore.GREEN + "┌──(ENTER TARGET NUMBER | E.G. +91XXXXXXXXXX)")
    target_num = input(Fore.GREEN + "└─> " + Fore.WHITE).strip()
    if not target_num:
        print(Fore.RED + "\n[-] ERROR: NUMBER CANNOT BE EMPTY!")
        return
    if not target_num.startswith('+'):
        target_num = '+' + target_num

    try:
        matrix_loading_animation()
        parsed = phonenumbers.parse(target_num, None)
        if not phonenumbers.is_valid_number(parsed):
            dynamic_logo()
            print(Fore.RED + f"\n[-] ERROR: {target_num} IS INVALID.")
            return

        # Real public data
        country = geocoder.description_for_number(parsed, "en") or "UNKNOWN"
        operator = carrier.name_for_number(parsed, "en") or "UNKNOWN"
        tz_list = timezone.time_zones_for_number(parsed)
        tz = tz_list[0] if tz_list else "N/A"

        # Generate fake personal data for demo
        fake_name, fake_father, fake_district, fake_location = generate_fake_indian_data()

        # Prepare report
        report_data = {
            "USER NAME": f"{fake_name} [DEMO]",
            "FATHER NAME": f"{fake_father} [DEMO]",
            "HOME DISTRICT": f"{fake_district} [DEMO]",
            "CURRENT LOCATION": f"{fake_location} [DEMO]",
            "COUNTRY/REGION": country.upper(),
            "SIM OPERATOR": operator.upper(),
            "TIME ZONE": tz.upper(),
            "NETWORK STATUS": "ONLINE"
        }

        dynamic_logo()
        stylish_upper_box("CRITICAL TARGET REPORT (DEMO DATA)", report_data)

        print(Fore.RED + "\n ⚠️⚠️⚠️  DISCLAIMER  ⚠️⚠️⚠️")
        print(Fore.YELLOW + " THE FIELDS 'USER NAME', 'FATHER NAME', 'HOME DISTRICT', 'CURRENT LOCATION'")
        print(Fore.YELLOW + " ARE RANDOMLY GENERATED FAKE DATA FOR DEMONSTRATION PURPOSES ONLY.")
        print(Fore.YELLOW + " NO REAL PERSONAL INFORMATION IS FETCHED FROM THE PHONE NUMBER.")
        print(Fore.YELLOW + " REAL TRACKING OF NAME/FATHER/LOCATION FROM A PHONE NUMBER IS ILLEGAL AND IMPOSSIBLE.")

    except Exception as e:
        dynamic_logo()
        print(Fore.RED + f"\n[-] SYSTEM EXCEPTION: {str(e).upper()}")

if __name__ == "__main__":
    main_tracker()
