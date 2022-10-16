import os

os.system('sudo apt update -y')
os.system('clear')
os.system('sudo apt install python3-pip')
os.system('pip3 install opencv-python')
os.system('pip3 install pyfiglet')
os.system('qrcode')
os.system('clear')


os.system('pip install opencv-python')
import cv2
from pyfiglet import Figlet


def colored(r,g,b,text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


qrcodes = qrcode.QRCode(
    version=10,    # as number increases the code image will be complicated and the image will be bigger
    box_size=10,   # size of the qr code image
    border=5       # white part of the qr code in all 4 sides
)

os.system('clear')

# heading = Figlet(font='big')
# print(colored(255, 165, 0, heading.renderText("QR Code generator")))

os.system('sudo apt install toilet -y')
os.system('clear')
print("\n")
os.system('toilet -f wideterm -F border  Qr code generator')



print("\n\n*******************\n")
print(colored(0,255,255,"@SUJAY_ADKESAR : https://sujayadkesar.github.io/portfolio"))
print(colored(0,255,255,"https://github.com/sujayadkesar/qr_code_generator"))
print("\n*******************\n")



data_from_user = input("\n\n[*] Enter the url or text that has to be converted into QR code:-\t")
data = "{}".format(data_from_user)

qrcodes.add_data(data)
qrcodes.make(fit=True)
img = qrcodes.make_image(fill="black", back_color="white")

a = input("[*] Enter the name to save qrcode image (with no spaces) :-\t")
b = "{}.png".format(a)
img.save(b)

display_img = cv2.imread(b)
display_img = Image.fromarray(display_img, "RGB")

display_img.show()
