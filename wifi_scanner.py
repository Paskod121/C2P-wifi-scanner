#Les importations
import subprocess

#aceuil
print()
print("Scanner wifi ")
print("-" * 12)
print()

print("Scaning...")
print()

#Execution de la commande netsh wlan show networks
try : 
    reseau = subprocess.run(
        ['netsh', 'wlan', 'show', 'networks'],
        capture_outpout = True,
        text = True,
        encoding = "utf-8"
    )
    
    
except probleme as errer:
   print("erreur", errer)