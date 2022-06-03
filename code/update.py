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
versioncontrol = "0.41"

def update():
    raw = requests.get("https://raw.githubusercontent.com/KeyPharm/Anticansancio-NiNoKuniXW/main/code/update.py").text
    if raw != None:
        vc = raw.splitlines()[20].split("=")[-1][2:-1]
        if vc == versioncontrol and vc != None:
            return True
    return False

def getNewUpdate():
    import os, requests, zipfile, io, shutil, sys
    from pathlib import Path
    dir = os.getcwd()
    r = requests.get("https://github.com/KeyPharm/Anticansancio-NiNoKuniXW/archive/refs/heads/main.zip", stream=True)
    if r:
        z = zipfile.ZipFile(io.BytesIO(r.content))
        if "Anticansancio-NiNoKuniXW-main/" in z.namelist():
            source_dir = dir + "\\" + "Anticansancio-NiNoKuniXW-main\\"
            target_dir = dir + "\\"
            z.extractall(dir)
            try:
                os.remove(source_dir + "\\" + "settings.yaml")
                os.remove(source_dir + "\\" + "README.md")
                os.remove(source_dir + "\\" + "README.md.txt")
            except OSError:
                pass
            shutil.copytree(source_dir, target_dir, dirs_exist_ok=True)
            shutil.rmtree(source_dir)
        print("Restarting...")
        sys.stdout.flush()
        os.execl(sys.executable, 'python code\\main.py', *sys.argv[1:])

def getVersionControl():
    return versioncontrol