import qrcode

data = "https://flybozon.github.io/"
img = qrcode.make(data)
img.save("qrcode.png")
