print("import json")

def dump(obj, fp=False, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw):
    dump_content = f"{f'obj={obj}' if obj else ''}{f', fp={fp}' if fp else ''}{f', skipkeys={skipkeys}' if skipkeys else ''}{f', ensure_ascii={ensure_ascii}' if ensure_ascii and not ensure_ascii == True else ''}{f', check_circular={check_circular}' if check_circular and not check_circular == True else ''}{f', allow_nan={allow_nan}' if allow_nan and not allow_nan == True else ''}{f', cls={cls}' if cls else ''}{f', indent={indent}' if indent else ''}{f', separators={separators}' if separators else ''}{f', default={default}' if default else ''}"
    print(f"json.dump({dump_content})")
    return ""

def dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw):
    dumps_content = f"{f'obj={obj}' if obj else ''}{f', skipkeys={skipkeys}' if skipkeys else ''}{f', ensure_ascii={ensure_ascii}' if ensure_ascii and not ensure_ascii == True else ''}{f', check_circular={check_circular}' if check_circular and not check_circular == True else ''}{f', allow_nan={allow_nan}' if allow_nan and not allow_nan == True else ''}{f', cls={cls}' if cls else ''}{f', indent={indent}' if indent else ''}{f', separators={separators}' if separators else ''}{f', default={default}' if default else ''}"
    print(f"json.dumps({dumps_content})")
    return ""

def detect_encoding(b):
    print(f"json.detect_encoding(b={b})")
    return ""

def load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
    load_content = f"{f'fp={fp}' if fp else ''}{f', cls={cls}' if cls else ''}{f', object_hook={object_hook}' if object_hook else ''}{f', parse_float={parse_float}' if parse_float else ''}{f', parse_int={parse_int}' if parse_int else ''}{f', parse_constant={parse_constant}' if parse_constant else ''}{f', object_pairs_hook={object_pairs_hook}' if object_pairs_hook else ''}"
    print(f"json.load({load_content})")
    return ""

def loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
    loads_content = f"{f's={s}' if s else ''}{f', cls={cls}' if cls else ''}{f', object_hook={object_hook}' if object_hook else ''}{f', parse_float={parse_float}' if parse_float else ''}{f', parse_int={parse_int}' if parse_int else ''}{f', parse_constant={parse_constant}' if parse_constant else ''}{f', object_pairs_hook={object_pairs_hook}' if object_pairs_hook else ''}"
    print(f"json.load({loads_content})")
    return ""