print("import re")

def findall(pattern, string, flags=0):

    print(f"re.findall({pattern}, {string})")


def split(pattern, string, maxsplit=0, flags=0):

    print(f"re.split({pattern}, {string})")


def subn(pattern, repl, string, count=0, flags=0):

    print(f"re.subn({pattern}, {repl}, {string})")


def sub(pattern, repl, string, count=0, flags=0):

    print(f"re.sub({pattern}, {repl}, {string})")


def search(pattern, string, flags=0):

    print(f"re.search({pattern}, {string})")


def fullmatch(pattern, string, flags=0):

    print(f"re.fullmatch({pattern}, {string})")


def match(pattern, string, flags=0):

    print(f"re.match({pattern}, {string})")


def finditer(pattern, string, flags=0):

    print(f"re.finditer({pattern}, {string})")


def purge():

    print("re.purge()")


def template(pattern, flags=0):

    print(f"re.template({pattern})")


def escape(pattern):

    print(f"re.escape({pattern})")


def compile(pattern, flags=0):

    pattern  = ""

ASCII        = ""
IGNORECASE   = ""
LOCALE       = ""
UNICODE      = ""
MULTILINE    = ""
DOTALL       = ""
VERBOSE      = ""
TEMPLATE     = ""
DEBUG        = ""