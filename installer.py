import os

print("[*] Updating . . . . . .")
os.system('sudo apt update -y')
os.system('clear')

print("[*] Installing python pip package installer . . . . . .")
os.system('sudo apt install python3-pip')


print("[*] Installing pyfiglet . . . . . .")
os.system('pip3 install pyfiglet')

print("[*] Installing qrcode . . . . .")
os.system('pip3 install qrcode==6.1')
os.system('pip3 install pyqrcode')
os.system('clear')

os.system('sudo apt install toilet -y')
os.system('pip3 install pypng')
os.system('clear')


print("[*] All the requirements downloaded successfully .....")
print("[*] You may proceed to run the qr code generator program!")
print("__________________________")
