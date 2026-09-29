import qrcode

link = "https://play.google.com/store/apps/details?id=br.com.zero48mobi.taxi.drivermachine&hl=pt_BR"

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=4,
)

qr.add_data(link)
qr.make(fit=True)

imagem = qr.make_image(fill_color="black", back_color="white")

# Caminho exato onde o PNG será salvo
caminho = (
    r"C:\Users\rober\OneDrive\Imagens\qrcodezero48apps\qrcode_zero48_Motorista.png"
)

imagem.save(caminho)

print("✅ QR Code PNG criado!")
print(f"📁 Salvo em: {caminho}")
print(f"🔗 Link: {link}")
