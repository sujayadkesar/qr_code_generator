import os
os.system('sudo apt install python3-pip')
os.system('pip3 install pyqrcode')
import pyqrcode



def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


os.system('clear')

print("\n")
os.system('toilet -f wideterm -F border  Qr code generator')

print("\n\n*******************\n")
print(colored(0, 255, 255, "@SUJAY_ADKESAR : https://sujayadkesar.github.io/portfolio"))
print(colored(0, 255, 255, "https://github.com/sujayadkesar/qr_code_generator"))
print("\n*******************\n")


data_from_user = input("\n\n[*] Enter the url or text that has to be converted into QR code:-\t")
data = "{}".format(data_from_user)


url = pyqrcode.create(data)
url.show()
# print(url.terminal(quiet_zone=1))

print('[*] TO generate another one run it once again!')
