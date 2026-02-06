import os

filename = "index.html"

if os.path.exists(filename):
    print(f"Fail '{filename}' wujud ✅")
else:
    print(f"Fail '{filename}' TIDAK wujud ❌")


with open(filename, "r", encoding="utf-8") as file:
    content = file.read()
    if "alert(" in content:
        print("Fungsi alert() wujud ✅")
    else:
        print("Fungsi alert() TIDAK wujud ❌")
