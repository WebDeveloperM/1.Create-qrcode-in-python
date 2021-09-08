import qrcode
import image
from qrcode.main import make
qr = qrcode.QRCode(
    version=15, 
    box_size=10, 
    border=5
)

data = "https://www.youtube.com/watch?v=GHy7vzPcKEc"

qr.add_data(data)
qr.make(fit=True)
img =qr.make_image(fill="black", back_color="white")
img.save("test.png")