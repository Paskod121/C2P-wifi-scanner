import subprocess

#Accueil
print()
print("Scanner wifi")
print("_" * 12)
print()

print("Scan...")
print()

try :
    reseau = subprocess.run(
        ['netsh', 'wlan', 'show', 'networks'],
        capture_output = True,
        text = True,
        encoding = "utf-8"
    )

    print(reseau.stdout)

except Exception as error :
    print("erreur", error)