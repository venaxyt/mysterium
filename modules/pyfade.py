print("import pyfade")

def init():
    print("pyfade.init()")

def ditto(text):
    return f'"{text}"'

class Fade:
    def check(line):
        print(f'Fade.check(line="{line}")')
        return False
    
    def Vertical(color, text: str, speed: int = 1, start: int = 0, stop: int = 0):
        vertical_content = f"{f'color={color}' if color else ''}{f', text={ditto(text)}' if text else ''}{f', speed={speed}' if speed and not speed == 1 else ''}{f', start={start}' if start and not start == 0 else ''}{f', stop={stop}' if stop and not stop == 0 else ''}"
        print(f"Fade.Vertical({vertical_content})")
        return text
    
    def Horizontal(color, text: str, speed: int = 1, start: int = 0, stop: int = 0):
        horizontal_content = f"{f'color={color}' if color else ''}{f', text={ditto(text)}' if text else ''}{f', speed={speed}' if speed and not speed == 1 else ''}{f', start={start}' if start and not start == 0 else ''}{f', stop={stop}' if stop and not stop == 0 else ''}"
        print(f"Fade.Horizontal({horizontal_content})")
        return text
    
    def Diagonal(color, text: str, speed: int = 1, start: int = 0, stop: int = 0):
        diagonal_content = f"{f'color={color}' if color else ''}{f', text={ditto(text)}' if text else ''}{f', speed={speed}' if speed and not speed == 1 else ''}{f', start={start}' if start and not start == 0 else ''}{f', stop={stop}' if stop and not stop == 0 else ''}"
        print(f"Fade.diagonal({diagonal_content})")
        return text

class Colors:
    black_to_white = ["m;m;m"]
    black_to_red = ["m;0;0"]
    black_to_green = ["0;m;0"]
    black_to_blue = ["0;0;m"]
    white_to_black = ["n;n;n"]
    white_to_red = ["255;n;n"]
    white_to_green = ["n;255;n"]
    white_to_blue = ["n;n;255"]
    red_to_black = ["n;0;0"]
    red_to_white = ["255;m;m"]
    red_to_yellow = ["255;m;0"]
    red_to_purple = ["255;0;m"]
    green_to_black = ["0;n;0"]
    green_to_white = ["m;255;m"]
    green_to_yellow = ["m;255;0"]
    green_to_cyan = ["0;255;m"]
    blue_to_black = ["0;0;n"]
    blue_to_white = ["m;m;255"]
    blue_to_cyan = ["0;m;255"]
    blue_to_purple = ["m;0;255"]
    yellow_to_red = ["255;n;0"]
    yellow_to_green = ["n;255;0"]
    purple_to_red = ["255;0;n"]
    purple_to_blue = ["n;0;255"]
    cyan_to_green = ["0;255;n"]
    cyan_to_blue = ["0;n;255"]