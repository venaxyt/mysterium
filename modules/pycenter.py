print("import pycenter")

def center(var: str, space: int = None, icon: str = "", sep: bool = False):
    center_content = f"{f'var={var}' if var else ''}{f', space={space}' if space else ''}{f', icon={icon}' if icon else ''}{f', sep={sep}' if sep else ''}"
    print(f'pycenter.center("{center_content}")')
    return var

def makebox(content: str):
    print(f'pycenter.makebox("{content}")')
    return content