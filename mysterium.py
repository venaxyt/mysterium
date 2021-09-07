# Made by @venaxyt on Github (helped by @IDRALOU)
import threading, requests, gratient, zipfile, signal, fade, sys, os

# Mysterium top bar title
os.system("title 𝙈 𝙔 𝙎 𝙏 𝙀 𝙍 𝙄 𝙐 𝙈")

# Definitions
def clear():
    os.system("cls")

def pause():
    os.system("pause >nul")

def leave():
    try:
        sys.exit()
    except:
        exit()

def error(error):
    print(gratient.red(f"  [>] Error: {error}"), end = "")
    pause(); clear(); leave()

# Custom purple gratient color definition
def purple(text):
    os.system(""); faded = ""; down = False
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
  {purple("[>] If you want to inspect a file encrypted with pyarmor, put it in a zip file with the pytransform folder")}
"""
# Editing this banner will not transform you in a programmer /// Ce n'est pas en changeant la bannière que vous allez devenir développeur

# Mysterium user inputs his uninspected file directory
uninspected_file_directory = False
while not uninspected_file_directory:
    clear(); print(fade.water(banner))
    uninspected_file_directory = input(purple("  [>] Enter uninspected file directory : ") + "\033[38;2;157;0;230m")

uninspected_file_directory = uninspected_file_directory.replace("'", "").replace('"', "")
uninspected_file_name = "uninspected"

# Retrieve uninspected file extension from directory
directory_characters = 0
for character in uninspected_file_directory:
    directory_characters += 1

# Check if Mysterium user specified uninspected file extension
if not "." in uninspected_file_directory:
    error("You have to specify the file extension")

# Check if uninspected file extension is "py" or "pyc"
elif not uninspected_file_directory[directory_characters - 2:] == "py" and not uninspected_file_directory[directory_characters - 3:] == "pyc" and not uninspected_file_directory[directory_characters - 3:] == "exe"and not uninspected_file_directory[directory_characters - 3:] == "zip":
    error('You can only scan "py", "pyc" or "zip" files for the moment')

# Definition of uninspected file extension
if uninspected_file_directory[directory_characters - 2:] == "py":
    uninspected_file_extension = "py"
if uninspected_file_directory[directory_characters - 3:] == "pyc":
    uninspected_file_extension = "pyc"
if uninspected_file_directory[directory_characters - 3:] == "exe":
    uninspected_file_extension = "exe"
if uninspected_file_directory[directory_characters - 3:] == "zip":
    uninspected_file_extension = "zip"

# Checking "exe" files is not disponible yet
if uninspected_file_extension == "exe":
    error("For the moment you can't inspect executable files, decompile them first")

# Check if Mysterium directory exists
modules_directory = "modules"
if not os.path.isdir(modules_directory):
    error("You have to download modules before inspecting any file")
try:
    os.system(f'copy "{uninspected_file_directory}" "modules\\uninspected.{uninspected_file_extension}" >nul')   #3 char .
except:
    error("An unexpected error occurred during file scan (01)")

# Unzip the file if it is in a "zip" file
if uninspected_file_extension == "zip":
    zipfile.ZipFile("modules\\uninspected.zip", "r").extractall("modules")
    os.remove("modules\\uninspected.zip")
    uninspected_file_name = input(purple("  [>] Enter python obfuscated file without .py : ") + "\033[38;2;157;0;230m")

# Jump line even zip file detected
print("")

# Define pyarmor uninspected file as ".py"
if not uninspected_file_extension == "pyc":
    uninspected_file_extension = "py"

# Start uninspected file under Mysterium modules
os.system(f'"modules\\{uninspected_file_name}.{uninspected_file_extension}"')

print(gratient.blue("\n  [>] The code is finished, don't forget to follow @venaxyt and @IDRALOU on Github"), end = "")
pause(); clear(); leave()