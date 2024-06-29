# Loki6
Loki6 is a Python-based tool designed to gather system information and save it to a USB drive. It's useful for forensic purposes or capturing system snapshots.

Features
Collects system information such as hostname, platform details, IP address, and more.
Saves collected information into a structured folder (loki6) on the connected USB drive.
Includes an executable (lokiusb.exe) for easy deployment on Windows systems without Python installed.
Usage
Method 1: Using Python Script (lokiusb.py)
Ensure Python is installed on your system.
Clone or download the loki6 project repository.
Navigate to the directory containing lokiusb.py.
Modify usb_drive variable in lokiusb.py to match your USB drive letter (D:\ in this example).
Run the script:
Copy code
python lokiusb.py
System information will be collected and saved into D:\loki6.
Method 2: Using Executable (lokiusb.exe)
Download lokiusb.exe from the project repository's dist directory.
Connect your USB drive and ensure it's mapped to the expected drive letter (D:\ in this example).
Double-click lokiusb.exe to run it.
System information will be collected and saved into D:\loki6.
Notes
Ensure the USB drive (D:\) is writable and has sufficient space.
Python installation is required only for running lokiusb.py. lokiusb.exe is self-contained and does not require Python.
