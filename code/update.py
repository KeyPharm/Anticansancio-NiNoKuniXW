import requests
# save some space
# save some space
# save some space
# save some space
# save some space
# save some space
# save some space
# save some space
# save some space
# save some space
# save some space
# save some space
# save some space
# save some space
# save some space
# save some space
# save some space
# save some space
# respeta los espacios antes y después  del =. y siempre línea 20
versioncontrol = "0.1"

def update():
    raw = requests.get("https://raw.githubusercontent.com/XanOpiat/Python-CSGO-Cheat/main/Utils/Utilities.py").text
    if raw != None:
        vc = raw.splitlines()[20].split("=")[-1][2:-1]
        if vc == versioncontrol and vc != None:
            return True
    return False