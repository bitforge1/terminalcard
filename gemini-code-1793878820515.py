import datetime
import os

def print_card():
   
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    os.system('cls' if os.name == 'nt' else 'clear')
    
    logo = f"""
{CYAN}  ██████╗ ██╗███████╗██╗  ██╗
  ██╔════╝ ██║██╔════╝╚██╗██╔╝
  ██║  ███╗██║█████╗   ╚███╔╝ 
  ██║   ██║██║██╔══╝   ██╔██╗ 
  ╚██████╔╝██║███████╗██╔╝ ██╗
   ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝{RESET}
    """
    
    print(logo)
    print(f"{BOLD}=================================================={RESET}")
    print(f" {GREEN}Status:{RESET}   Online & Ready to Code ")
    print(f" {GREEN}GitHub:{RESET}   https://github.com/YOUR_USERNAME")
    print(f" {GREEN}Local Time:{RESET} {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{BOLD}=================================================={RESET}")
    print(f" {YELLOW}Tip:{RESET} Great things start with a single commit.\n")

if __name__ == "__main__":
    print_card()
