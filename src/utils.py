import subprocess

# Python cannot query the Operating System directly
# Subprocess moduel is used to run PowerShell commands from Python.
# Run command will get the computer model from Windows

def get_computer_model():
    try:
        output = subprocess.check_output(['powershell', '-Command', "(Get-CimInstance Win32_ComputerSystem).Model"], text=True)
        return output.strip()
    except Exception as e:
        return f"Error retrieving model: {e}"
