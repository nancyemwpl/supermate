# SuperMate

## Description
SuperMate is a Python utility designed to enhance the longevity and performance of Windows-operated devices. It achieves this by applying critical updates and power management tweaks. This ensures that your system remains up-to-date and optimized for better power efficiency and longevity.

## Features
- Automatically installs critical Windows updates.
- Applies power management settings to optimize system performance and energy use:
  - Sets the power scheme to 'High Performance'.
  - Disables system hibernation.
  - Configures hard disk to turn off after 20 minutes of inactivity.

## Requirements
- Windows Operating System
- Administrative privileges
- Python 3.x
- PowerShell with the `PSWindowsUpdate` module installed

## Installation
1. Ensure you have Python 3.x installed on your Windows machine.
2. Make sure PowerShell has the `PSWindowsUpdate` module. You can install it using the following command:
   ```powershell
   Install-Module -Name PSWindowsUpdate
   ```

## Usage
1. Open a command prompt or PowerShell with administrative privileges.
2. Navigate to the directory where `supermate.py` is located.
3. Run the script using:
   ```bash
   python supermate.py
   ```

## Note
- This script is designed to work on Windows systems only.
- Ensure you have administrative privileges to run this script effectively.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Author
[Your Name]