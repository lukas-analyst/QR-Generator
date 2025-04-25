import qrcode

def generate_qr_code(data, filename):
    # Vytvoření QR kódu
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Vytvoření obrázku QR kódu
    img = qr.make_image(fill_color="black", back_color="white")

    # Uložení obrázku jako PNG
    img.save(filename)

if __name__ == "__main__":
    # Načtení vstupních dat
    input_data = input("Zadejte text nebo URL pro generování QR kódu: ")
    output_filename = "qr_code.png"

    # Generování QR kódu
    generate_qr_code(input_data, output_filename)
    print(f"QR kód byl uložen jako {output_filename}.")