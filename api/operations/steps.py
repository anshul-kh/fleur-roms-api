steps = {
      "method": "TWRP",
      "steps": [
        "Unlock the bootloader of your Xiaomi device if not already unlocked.",
        "Download the custom ROM in ZIP format compatible with your device.",
        "Transfer the ROM ZIP file to your device's internal storage or SD card.",
        "Download and install TWRP (Team Win Recovery Project) on your device.",
        "Power off your Xiaomi device.",
        "Boot the device into TWRP recovery mode by holding the Volume Up and Power buttons simultaneously until the TWRP logo appears.",
        "In TWRP, select 'Wipe' and perform a factory reset by swiping to confirm. (Optional: For a clean flash, also wipe Dalvik/ART Cache, System, Data, and Cache.)",
        "Go back to the TWRP main menu and select 'Install'.",
        "Navigate to the location where you stored the ROM ZIP file and select it.",
        "Swipe to confirm the flash. Wait for the ROM installation to complete.",
        "Once the installation is complete, you can optionally flash other ZIPs such as Google Apps (GApps) or Magisk (for root).",
        "After flashing, select 'Reboot System' to boot into the newly installed ROM.",
        "Set up your device after it boots up with the new ROM."
      ]
    }

def get_steps():
    return steps    