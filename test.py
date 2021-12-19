import os

test = os.popen("uname -v").read().split(" ")[0].split("-")[0].split("~")[1]
print(test)
