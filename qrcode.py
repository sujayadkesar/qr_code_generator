import os
import pyqrcode
import png


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

name_from_user = input("\n[*] Enter the filename to save qr code image:-\t")

url = pyqrcode.create(data_from_user)

url.png('{}.png'.format(name_from_user))

print('[*] TO generate another one run it once again!')
