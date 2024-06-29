import os
import json
import platform
import subprocess
from datetime import datetime

def get_system_info():
    system_info = {
        "hostname": platform.node(),
        "platform": platform.system(),
        "platform-release": platform.release(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "ip-address": get_ip_address(),
        "username": get_username(),
        "network-configuration": get_network_configuration()
    }

    return system_info

def get_ip_address():
    if platform.system() == "Windows":
        ip_info = subprocess.getoutput("ipconfig | findstr IPv4").strip().split(":")[-1].strip()
    else:
        ip_info = "Unknown"
    return ip_info

def get_username():
    return os.getlogin()

def get_network_configuration():
    if platform.system() == "Windows":
        network_info = subprocess.getoutput("ipconfig /all")
    else:
        network_info = "Network configuration not available on non-Windows systems"
    return network_info

def save_info_to_usb(system_info, usb_drive):
    usb_path = os.path.join(usb_drive, "loki6")
    os.makedirs(usb_path, exist_ok=True)

    # Generate a unique folder name using timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = f"action_{timestamp}"

    # Create a new folder for each action
    action_folder = os.path.join(usb_path, folder_name)
    os.makedirs(action_folder)

    # Save system information to a JSON file inside the action folder
    file_name = "system_info.json"
    file_path = os.path.join(action_folder, file_name)
    with open(file_path, "w") as f:
        json.dump(system_info, f, indent=4)

    print(f"System information saved to {file_path}")

def main():
    # Adjust the USB drive letter as per your system
    usb_drive = "D:\\"  # Change this to the correct drive letter on your laptop
    if not os.path.exists(usb_drive):
        print(f"USB drive not found at {usb_drive}")
        return

    system_info = get_system_info()
    save_info_to_usb(system_info, usb_drive)

if __name__ == "__main__":
    main()
