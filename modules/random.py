print("import random")

class Random:
    def randbytes(n):
        print(f"random.randbytes({n})")
        return 0

    def randrange(start, stop=None, step=1):
        randrange_content = f"{f'start={start}' if start else ''}{f', stop={stop}' if stop else ''}{f', step={step}' if step and not step == 1 else ''}"
        print(f"random.randrange({randrange_content})")
        return 0

    def randint(a, b):
        print(f"random.randint(a={a}, b={b})")
        return 0

    def choice(seq):
        print(f"random.choice(seq={seq})")
        return 0

    def gauss(mu, sigma):
        print(f"random.gauss(mu={mu}, sigma={sigma})")
        return 0

    def random():
        print("random.random()")
        return 0

    def getrandbits(k):
        print(f"random.getrandbits(k={k})")
        return 0