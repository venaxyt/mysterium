print("import playsound")

def playsound(sound, block=True):
    sound = f'"{sound}"'
    print(f"playsound.playsound({sound}{f', block={block}' if block else ''})")