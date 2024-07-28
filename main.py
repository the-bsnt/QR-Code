import qrcode
import qrcode.constants
from PIL import Image
virat_img = Image.open("Kholi_image.jpg")


profile = {
    "name": "Virat Kholi",
    "age": 38,
    "city": "Mumbai",
    "country": "India",
    "phone": "1234567890",
    "email": "virat@gmail.com",
    "img": "http://127.0.0.1:5500/index.html"
}

features = qrcode.QRCode(
    version=1, box_size=50, border=2, error_correction=qrcode.constants.ERROR_CORRECT_L
)
features.add_data(profile)
features.make(fit=True)

img = features.make_image(fill_color="red", back_color="white")

img.save("kholi.png")
