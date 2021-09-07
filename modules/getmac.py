print("import getmac")

def get_mac_address(interface=None, ip=None, ip6=None, hostname=None, network_request=True):
    get_mac_address_content = f"{f'interface={interface}' if interface else ''}{f', ip={ip}' if ip else ''}{f', ip6={ip6}' if ip6 else ''}{f', hostname={hostname}' if hostname else ''}{f', network_request={network_request}' if network_request and not network_request == True else ''}"
    print(f'getmac.get_mac_address({get_mac_address_content})')
    return "00:00:00:00:00:00"