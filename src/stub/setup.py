import os

from colorama import init, Fore
from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv

init(autoreset=True)
load_dotenv()


async def setup_run(env: str = "./.env" or None) -> None:
    if not os.path.isfile(env):
        with open(env, "w") as env_file:
            env_file.write(f"DJANGO_SECRET_KEY='{get_random_secret_key()}'")
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{Fore.GREEN}[+] {Fore.WHITE}File ({Fore.GREEN}.env{Fore.WHITE}) was successful created {Fore.GREEN}<3"
                  f"\n{Fore.YELLOW}[~] {Fore.WHITE}Restart the program to start working {Fore.GREEN};)")
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print(f'{Fore.GREEN}[+] {Fore.WHITE}Website was started {Fore.GREEN}<3')
        os.system(f"uv run stub/manage.py runserver")


__all__ = [
    "setup_run",
    "Fore"
]