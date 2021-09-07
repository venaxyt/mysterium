print("import pyproxies")

def proxy(server, timeout = 5):
    print(f'pyproxies.proxy(server="{server}"{f", timeout={timeout}" if timeout and not timeout == 5 else ""})')
    return {"https": f"http://198.162.1.1:8080"}