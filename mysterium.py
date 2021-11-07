# Made by @venaxyt on Github (helped by @IDRALOU and @Bleu-No)
# >>> https://github.com/venaxyt/mysterium
# Checking if needed modules are installed
import argparse
import os
import platform
import sys
import zipfile
from shutil import copyfile

is_windows = True if platform.system() == "Windows" else False

try:
    import fade
    import gratient
except:
    try:
        if is_windows:
            output = ">nul"
        else:
            output = "/dev/null"

        os.system(f"python -m pip install -r requirements.txt {output}")

        import fade
        import gratient
    except:
        exit()

system = platform.system()

if is_windows:
    # Mysterium top bar title
    os.system("title 𝙈 𝙔 𝙎 𝙏 𝙀 𝙍 𝙄 𝙐 𝙈")


# Definitions
def clear():
    if is_windows:
        os.system("cls")
    else:
        os.system("clear")


def pause():
    input()


def leave():
    try:
        sys.exit()
    except:
        exit()


def error(error):
    print(gratient.red(f"  [>] Error: {error}"), end="")
    pause()
    clear()
    leave()


# Custom purple gratient color definition
def purple(text):
    os.system("")
    faded = ""
    down = False

    for line in text.splitlines():
        red = 40
        for character in line:
            if down:
                red -= 3
            else:
                red += 3
            if red > 254:
                red = 255
                down = True
            elif red < 1:
                red = 30
                down = False
            faded += (f"\033[38;2;{red};0;220m{character}\033[0m")
    return faded


# Gratient coloured banner
banner = f"""
           :::   :::   :::   :::   ::::::::  :::::::::::  ::::::::::  :::::::::   :::::::::::  :::    :::    :::   :::
         :+:+: :+:+:  :+:   :+:  :+:    :+:     :+:      :+:         :+:    :+:      :+:      :+:    :+:   :+:+: :+:+:
       +:+ +:+:+ +:+  +:+ +:+   +:+            +:+      +:+         +:+    +:+      +:+      +:+    +:+  +:+ +:+:+ +:+
      +#+  +:+  +#+   +#++:    +#++:++#++     +#+      +#++:++#    +#++:++#:       +#+      +#+    +:+  +#+  +:+  +#+
     +#+       +#+    +#+            +#+     +#+      +#+         +#+    +#+      +#+      +#+    +#+  +#+       +#+
    #+#       #+#    #+#     #+#    #+#     #+#      #+#         #+#    #+#      #+#      #+#    #+#  #+#       #+#
   ###       ###    ###      ########      ###      ##########  ###    ###  ###########   ########   ###       ###

  {purple("[>] Mysterium has been created by @venaxyt on Github / https://github.com/venaxyt/mysterium / Mysterium 2021©")}
  {purple("[>] To inspect a code encrypted with Pyarmor, put it in a zip with the pytransform folder and it's architecture")}
  {purple(f"[>] Mysterium version : 1.2.0  /  Running with Python {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}  /  Discord server : https://discord.gg/mysterium")}
"""
# Editing this banner will not transform you in a programmer /// Ce n'est pas en changeant la bannière que vous allez devenir développeur


# Allow mysterium to be used in command line interface (CLI)
parser = argparse.ArgumentParser(description="[+] Mysterium CLI")
parser.add_argument('-f', dest="filepath", required=False, default=None, help='The path to the file you want to inspect')

args = parser.parse_args()

uninspected_file_directory = args.filepath

# Mysterium user inputs his uninspected file directory if not specified
# with the -f flag
while not uninspected_file_directory:
    clear()
    print(fade.water(banner))
    uninspected_file_directory = input(purple("  [>] Enter uninspected file path : ") + "\033[38;2;157;0;230m")

uninspected_file_directory = uninspected_file_directory.replace("'", "").replace('"', "")
uninspected_file_name = "uninspected"

filename, uninspected_file_extension = os.path.splitext(uninspected_file_directory)
# Remove the dot from the extension
uninspected_file_extension = uninspected_file_extension[1:]

# Check if Mysterium user specified uninspected file extension
if not uninspected_file_extension:
    error("You have to specify the file extension")

supported_file_extensions = ["py", "pyc", "exe", "zip"]
if uninspected_file_extension not in supported_file_extensions:
    error('This extension of the file is not supported. You can only scan the following formats: {}.'.format(",".join(supported_file_extensions)))

# Extraction of Python files from the executable one
if uninspected_file_extension == "exe":
    copyfile(uninspected_file_directory, os.path.join("executable", "uninspected.exe"))
    print(gratient.blue("\n  [>] Trying to extracted Python files from the executable..."), end="")
    os.system("cd executable && python pyinstxtractor.py uninspected.exe")
    if os.path.isdir(os.path.join("executable", "uninspected.exe_extracted")):
        print(gratient.blue("\n  [>] Successfully extracted files from the executable"), end="")
    else:
        error("There was an error extracting Python files from the executable")
    # Remove exported executable file
    os.remove(os.path.join("executable", "uninspected.exe"))
    print("")  # To jump a line
    uninspected_file_name = input(purple("  [>] Enter Python file name with extension : ") + "\033[38;2;157;0;230m")
    exe_base_path = os.path.join("executable", "uninspected.exe_extracted")
    if os.path.isfile(os.path.join(exe_base_path, f"{uninspected_file_name}.pyc")):
        copyfile(os.path.join(exe_base_path, f"{uninspected_file_name}.pyc"), os.path.join("modules", f"{uninspected_file_name}.pyc"))
    elif os.path.isfile(os.path.join(exe_base_path, f"{uninspected_file_name}")):
        copyfile(os.path.join(exe_base_path, f"{uninspected_file_name}"), os.path.join("modules", f"{uninspected_file_name}.pyc"))
    else:
        error("The extracted pyc file has not been found")
    # Define uninspected file extension as .pyc
    uninspected_file_extension = "pyc"

# Check if Mysterium directory exists
if not os.path.isdir("modules"):
    error("You have to download modules before inspecting any file")

if not uninspected_file_extension == "exe":
    try:
        copyfile(uninspected_file_directory, os.path.join("modules", f"uninspected.{uninspected_file_extension}"))
    except FileNotFoundError:
        error("File to inspect not found. Check the uninspected file path.")

# Unzip the file if it is in a "zip" file (used for Pyarmor / external encryptages)
if uninspected_file_extension == "zip":
    zipfile.ZipFile(os.path.join("modules", "uninspected.zip"), "r").extractall("modules")
    os.remove(os.path.join("modules", "uninspected.zip"))
    uninspected_file_name = input(purple("  [>] Enter Python obfuscated file name with extension : ") + "\033[38;2;211;0;230m")

    uninspected_file_name, uninspected_file_extension = os.path.splitext(uninspected_file_name)
    # Remove the dot from the extension
    uninspected_file_extension = uninspected_file_extension[1:]

    if uninspected_file_extension != "py" and uninspected_file_extension != "pyc":
        error("The file extension can only be .py or .pyc")

# Jump a line even zip file detected
print("")

# Define pyarmor uninspected file as ".py" (can be edited by .pyc if pyarmor main Python file is encrypted under .pyc)
if not uninspected_file_extension == "pyc":
    uninspected_file_extension = "py"

# Start uninspected file under Mysterium modules
# import modules.blue
# modules.blue.Blue(f'modules\\{uninspected_file_name}.{uninspected_file_extension}', uninspected_file_directory)
os.system("python {}".format(os.path.join("modules", f"{uninspected_file_name}.{uninspected_file_extension}")))

print(gratient.blue("\n  [>] The code is finished, don't forget to follow @venaxyt / @IDRALOU / @Bleu-No on Github"), end="")
os.remove(os.path.join("modules", f"{uninspected_file_name}.{uninspected_file_extension}"))
pause()
clear()
leave()
