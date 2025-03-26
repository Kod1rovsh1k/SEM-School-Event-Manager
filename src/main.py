import asyncio

from stub import *

async def main():
    await setup_run()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"{Fore.RED}[-] {Fore.WHITE}You stopped program {Fore.RED}:(")