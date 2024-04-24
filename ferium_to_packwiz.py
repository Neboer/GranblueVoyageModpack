import json
import subprocess
from sys import argv
from os import chdir

config_file_locations = argv[1]


# Load ferium config
with open(config_file_locations, "r") as f:
    config_data = json.load(f)

profiles = config_data["profiles"]

# Get profile selection if there are multiple profiles
if len(profiles) > 1:
    print("Available profiles:")
    for idx, profile in enumerate(profiles):
        print(f"{idx + 1}. {profile['name']}")
    profile_selected = int(input("Please select which profile you want: ")) - 1
    selected_profile = profiles[profile_selected]
else:
    selected_profile = profiles[0]

chdir("Packwiz")

# Extract mods and install them
mods = selected_profile["mods"]
for mod in mods:
    mod_type = list(mod["identifier"].keys())[0]
    if mod_type == "ModrinthProject":
        identifier = mod["identifier"]["ModrinthProject"]
        subprocess.run(["packwiz", "modrinth", "install", identifier, "-y"])
    elif mod_type == "CurseForgeProject":
        identifier = str(mod["identifier"]["CurseForgeProject"])
        subprocess.run(["packwiz", "curseforge", "install", "--addon-id", identifier, "-y"])
    else:
        print(f"unsupport mod {mod}")
