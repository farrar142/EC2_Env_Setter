import os

all = os.popen("uname -v").read()
_all = all.split(" ")[0].split("-")[0].split("~")[1].split(".")

print(f"current os version = {all}")
print(f"{_all[0]},{_all[1]}")
if int(_all[0]) <= 20:
    if int(_all[1]) <= 4:
        print("you need version more than 23~20.04-1")
