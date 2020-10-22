import json
from vulcan import Vulcan


def reg(token, symbol, pin):
    certificate = Vulcan.register(token, symbol, pin, "Home Assistant")
    with open("vulcan.json", "w") as f:
        json.dump(certificate.json, f)

    return None
