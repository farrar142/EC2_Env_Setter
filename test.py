import os

all = os.popen("uname -v").read()
_all = all.split(" ")[0].split("-")[0].split("~")[1].split(".")

print(f"current os version = {all}")
print(f"{_all[1]},{all[2]}")
if int(all[1]) < 20:
    if int(_all[2]) <= 4:
        print("you need version more than 23~20.04-1")
