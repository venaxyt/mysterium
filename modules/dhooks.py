print("import dhooks")

class Webhook:
    def __init__(self, url, **kwargs):
        print("from dhooks import Webhook")
        print(f'webhook = dhooks.Webhook(url="{url}")')

    def send(self, content: str = "", **kwargs):
        print(f'webhook.send(content="{content}")')

    def modify(self, name, **kwargs):
        print(f'webhook.modify(name="{name}")')

    def get_info(self):
        print("webhook.get_info()")
        return ""

    def close(self):
        print("webhook.close()")

    def delete(self):
        print("webhook.delete()")