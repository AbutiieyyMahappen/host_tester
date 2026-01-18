print("\033[32m=====================================================")
print("\033[31m|                  Developer Info                  |")
print("\033[36m=====================================================")
print("\033[37m| Developer : Abutiiey Mahappen                   |")
print("\033[32m| Github    : https://github.com/abutieymahappen    |")
print("\033[36m| Facebook  :https://mahappentech                       |")
print("\033[33m| Telegram  : https//MahappenTech                      |")
print("\033[37m=====================================================")
print()

import subprocess
import platform

def ping_host(host):
    print("\033[32m=====================================================")
    print(f"\033[32m|              Pinging {host}...              |")
    print("\033[32m=====================================================")
    current_os = platform.system().lower()
    param = "-n" if current_os == "windows" else "-c"
    command = ["ping", param, "4", host]
    response = subprocess.call(command)
    if response == 0:
        print(f"\033[36m\n{host} host is UP 😊")
    else:
        print(f"\033[31m\n{host} host is DOWN 😔")

while True:
    print("\033[36m")
    print("\033[37m                                           ")
    print("\033[37     1. Ping Host                    ")
    print("\033[37     2. About                       ")
    print("\033[31m    3. Exit                         ")
    print("\033[37m")
    choice = input("\033[36mEnter your Option(1/2/3): ")
    if choice == "1":
        target = input("\033[36mEnter HOST / IP: ")
        ping_host(target)
    elif choice == "2":
        print("\033[32m=====================================================")
        print("\033[32m|                     About                     |")
        print("\033[32m=====================================================")
        print("\033[36mThis tool uses the ICMP echo request to ping a host.")
        print("\033[36mIt checks if the host is up and responding to ping requests.")
        print("\033[36mPlease make sure you have an active internet connection.")
        print("\033[36mThe tool will not work without internet connectivity.")
        print("\033[32m=====================================================")
    elif choice == "3":
        print("\033[32m=====================================================")
        print("\033[32m|                   Goodbye!                   |")
        print("\033[32m=====================================================")
        break
    else:
        print("\033[31mInvalid Option. Please try again.")
