import qrcode

cuisines = {
    "American" : "https://faraz19m.github.io/DishDash/cuisines/american.html",
    "Chinese" : "https://faraz19m.github.io/DishDash/cuisines/chinese.html",
    "French": "https://faraz19m.github.io/DishDash/cuisines/french.html",
    "Indian": "https://faraz19m.github.io/DishDash/cuisines/indian.html",
    "Italian" : "https://faraz19m.github.io/DishDash/cuisines/italian.html",
    "Japanese": "https://faraz19m.github.io/DishDash/cuisines/japanese.html",
    "Luxembourgish" : "https://faraz19m.github.io/DishDash/cuisines/luxembourgish.html",
    "Portugese" : "https://faraz19m.github.io/DishDash/cuisines/portugese.html"
}

for name, url in cuisines.items():
    qr = qrcode.QRCode(box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(f"assets/qr-codes/{name.lower()}.png")