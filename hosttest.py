print( "\033[37mDeveloper : Abutiiey Mahappen")
#print("Language : Python")
print("\033[32mGithub : https://github/abutieymahappen.com")
print("\033[36mFacebook : mahappentech")
print("\033[33mTelegram : MahappenTech")
print()
import subprocess
import platform

def ping_host(host):
    current_os = platform.system().lower()

    # Set correct param (-n for windows, -c for rest)
    param = "-n" if current_os == "windows" else "-c"
    command = ["ping", param, "4", host]
    print(f"\033[32mPinging {host}...")
    response = subprocess.call(command)

    if response == 0:
        print(f"\033[36m\n{host} host is UP.")
    else:
        print(f"\033[31m\n{host} host is DOWN.")

target = input("\033[36mEnter HOST / IP: ")
ping_host(target)
