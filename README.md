# LokiSys

**LokiSys** is a lightweight, Python-based system information gathering tool tailored for **Windows OS environments**, designed primarily for **digital forensics**, **incident response**, and **system diagnostics**. It collects key system metadata and stores the output on a connected USB device—enabling **offline evidence acquisition** or **live triage** scenarios.

---

## 🧰 Features

- Captures critical system details: hostname, OS version, IP address, platform information, and more.
- Automatically creates a structured folder (`loki6`) on the connected USB drive.
- Offers both Python script and standalone executable (`lokiusb.exe`) for deployment—no Python installation required on the target machine.

---

## 🚀 Usage

### 📜 Method 1: Run via Python Script (`lokiusb.py`)

1. Ensure Python is installed on the system.
2. Clone or download this repository and save it to your USB drive.
3. Create a folder named `loki6` inside your USB (e.g., `D:\loki6`).
4. Open `lokiusb.py` and update the `usb_drive` variable to match your USB letter (e.g., `D:\\`).
5. Run the script using:

   ```bash
   python lokiusb.py

### 🧱 Method 2: Run via Executable (lokiusb.exe)
1.Download lokiusb.exe from the dist folder of this repository.
2.Connect your USB drive (ensure it's mapped to the correct letter, e.g., D:\).
3.Double-click lokiusb.exe.
4.Output will be saved automatically to D:\loki6.

### ⚠️ Notes
1. Ensure the USB drive is writable and has sufficient space.
2. lokiusb.exe is compiled and does not require Python installation.
3. This tool is intended for legitimate system analysis and forensic use only.

### 📁 Output Example
The tool will generate a structured folder on your USB with logs such as:
```
D:\loki6\
├── system_info.txt
├── network_info.txt
└── metadata.log
```

### 🧪 Forensic Use Cases
1. Live system triage in digital forensic investigations
2. Rapid metadata acquisition from target endpoints
3. Portable reconnaissance tool for field agents or analysts

### 💡 Disclaimer
This tool is developed for educational and lawful forensic usage only. Always obtain proper authorization before executing on any system.

