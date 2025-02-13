import os
import subprocess
import ctypes
import platform

def is_admin():
    """Check if the script is running with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def apply_windows_updates():
    """Function to automatically install critical Windows updates."""
    print("Checking for Windows updates...")
    os.system("powershell -Command \"& {Start-Process powershell -ArgumentList 'Install-WindowsUpdate -AcceptAll -AutoReboot' -Verb RunAs}\"")

def set_power_management():
    """Function to apply power management tweaks."""
    print("Applying power management tweaks...")
    # Set the power scheme to 'High performance'
    subprocess.call('powercfg /setactivescheme SCHEME_MIN', shell=True)

    # Disable hibernation
    os.system("powercfg -hibernate off")

    # Turn off hard disk after 20 minutes
    os.system("powercfg -change -disk-timeout-ac 20")
    os.system("powercfg -change -disk-timeout-dc 20")

def main():
    if platform.system() != "Windows":
        print("SuperMate is designed to run on Windows systems only.")
        return

    if not is_admin():
        print("This script requires administrative privileges. Please run it as an administrator.")
        return

    print("Starting SuperMate...")
    apply_windows_updates()
    set_power_management()
    print("Updates and power management tweaks have been applied successfully.")

if __name__ == "__main__":
    main()