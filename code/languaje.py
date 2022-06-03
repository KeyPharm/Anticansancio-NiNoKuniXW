import yaml
settings = open("settings.yaml", 'r')
s = yaml.safe_load(settings)

def myLanguaje():
    if s["languaje"]:
        return s["languaje"]
    else:
        return "ES"
