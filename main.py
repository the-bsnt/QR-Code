import qrcode
import qrcode.constants


profile = {
    "name": "Virat Kholi",
    "age": 38,
    "city": "Mumbai",
    "country": "India",
    "phone": "1234567890",
    "email": "virat@gmail.com",
    "img": "http://167.71.229.99:8000/",
}

features = qrcode.QRCode(
    version=1, box_size=50, border=2, error_correction=qrcode.constants.ERROR_CORRECT_L
)
features.add_data(profile)
features.make(fit=True)

img = features.make_image(fill_color="black", back_color="white")

img.save("kholi_qr.png")
