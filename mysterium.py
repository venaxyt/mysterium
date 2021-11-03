# Made by @venaxyt on Github (helped by @IDRALOU and @Bleu-No)
# >>> https://github.com/venaxyt/mysterium
# Checking if needed modules are installed
try:
    import gratient, zipfile, fade, sys, os
except:
    try:
        import os; os.system("py -m pip install -r requirements.txt >nul")
        import gratient, zipfile, fade, sys, os
    except:
        exit()


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
  {purple("[>] To inspect a code encrypted with Pyarmor, put it in a zip with the pytransform folder and it's architecture")}
  {purple(f"[>] Mysterium version : 1.2.0  /  Running with Python {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}  /  Discord server : https://discord.gg/mysterium")}
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
elif uninspected_file_directory[directory_characters - 3:] == "pyc":
    uninspected_file_extension = "pyc"
elif uninspected_file_directory[directory_characters - 3:] == "exe":
    uninspected_file_extension = "exe"
elif uninspected_file_directory[directory_characters - 3:] == "zip":
    uninspected_file_extension = "zip"
else:
    error("This extension of the file is not supported")

# Extraction of Python files from the executable one
if uninspected_file_extension == "exe":
    os.system(f'copy "{uninspected_file_directory}" "executable\\uninspected.exe" >nul')
    print(gratient.blue("\n  [>] Trying to extracted Python files from the executable..."), end = "")
    os.system("cd executable && pyinstxtractor.py uninspected.exe >nul")
    if os.path.isdir("executable\\uninspected.exe_extracted"):
        print(gratient.blue("\n  [>] Successfully extracted files from the executable"), end = "")
    else:
        error("There was an error extracting Python files from the executable")
    # Remove exported executable file
    os.remove("executable\\uninspected.exe")
    print("")  # To jump a line
    uninspected_file_name = input(purple("  [>] Enter Python file name with extension : ") + "\033[38;2;157;0;230m")
    if os.path.isfile(f"executable\\uninspected.exe_extracted\\{uninspected_file_name}.pyc"):
        os.system(f'copy "executable\\uninspected.exe_extracted\\{uninspected_file_name}.pyc" "modules\\{uninspected_file_name}.pyc" >nul')
    elif os.path.isfile(f"executable\\uninspected.exe_extracted\\{uninspected_file_name}"):
        os.system(f'copy "executable\\uninspected.exe_extracted\\{uninspected_file_name}" "modules\\{uninspected_file_name}.pyc" >nul')
    else:
        error("The extracted pyc file has not been found")
    # Define uninspected file extension as .pyc
    uninspected_file_extension = "pyc"

# Check if Mysterium directory exists
if not os.path.isdir("modules"):
    error("You have to download modules before inspecting any file")

if not uninspected_file_extension == "exe":
    try:
        os.system(f'copy "{uninspected_file_directory}" "modules\\uninspected.{uninspected_file_extension}" >nul')
    except:
        error("An unexpected error occurred during file scan")

# Unzip the file if it is in a "zip" file (used for Pyarmor / external encryptages)
if uninspected_file_extension == "zip":
    zipfile.ZipFile("modules\\uninspected.zip", "r").extractall("modules")
    os.remove("modules\\uninspected.zip")
    uninspected_file_name = input(purple("  [>] Enter Python obfuscated file name with extension : ") + "\033[38;2;211;0;230m")
    
    # Calculating number of characters in the file name
    file_name_characters = 0
    for character in uninspected_file_name:
        file_name_characters += 1

    # Checking the file extension
    if uninspected_file_name[file_name_characters - 2:] == "py":
        uninspected_file_extension = "py"
        uninspected_file_name = uninspected_file_name[:-3]
    elif uninspected_file_name[file_name_characters - 3:] == "pyc":
        uninspected_file_extension = "pyc"
        uninspected_file_name = uninspected_file_name[:-4]
    else:
        error("The file extension can only be .py or .pyc")

# Jump a line even zip file detected
print("")

# Define pyarmor uninspected file as ".py" (can be edited by .pyc if pyarmor main Python file is encrypted under .pyc)
if not uninspected_file_extension == "pyc":
    uninspected_file_extension = "py"

# Start uninspected file under Mysterium modules
# import modules.blue
# modules.blue.Blue(f'modules\\{uninspected_file_name}.{uninspected_file_extension}', uninspected_file_directory)
os.system(f'modules\\{uninspected_file_name}.{uninspected_file_extension}')

print(gratient.blue("\n  [>] The code is finished, don't forget to follow @venaxyt / @IDRALOU / @Bleu-No on Github"), end = "")
os.remove(f"modules\\{uninspected_file_name}.{uninspected_file_extension}")
pause(); clear(); leave()
