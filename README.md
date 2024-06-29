# Loki6
Loki6 is a Python-based tool designed to gather system information and save it to a USB drive. It's useful for forensic purposes or capturing system snapshots.

Features

* Collects system information such as hostname, platform details, IP address, and more.
* Saves collected information into a structured folder (loki6) on the connected USB drive.
* Includes an executable (lokiusb.exe) for easy deployment on Windows systems without Python installed.

Usage

Method 1: Using Python Script (lokiusb.py)

1. Ensure Python is installed on your system.
2. Clone or download the loki6 project repository and saved it into your USB inside create the folder named "loki6"
3. Navigate to the directory containing lokiusb.py.
4. Modify usb_drive variable in lokiusb.py to match your USB drive letter (D:\ in this example).
5. Run the script:

Run the code in CMD / Terminal:

python lokiusb.py


1. System information will be collected and saved into D:\loki6.

Method 2: Using Executable (lokiusb.exe)

1. Download lokiusb.exe from the project repository's dist directory.
2. Connect your USB drive and ensure it's mapped to the expected drive letter (D:\ in this example).
3. Double-click lokiusb.exe to run it.
4. System information will be collected and saved into D:\loki6.

Notes

* Ensure the USB drive (D:\) is writable and has sufficient space.
* Python installation is required only for running lokiusb.py. lokiusb.exe is self-contained and does not require Python.

