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
    print("Generátor QR kódu pro platbu na bankovní účet")

    # Načtení údajů pro platbu
    account_number = input("Zadejte číslo účtu (ve formátu IBAN nebo číslo/číslo banky): ")
    amount = input("Zadejte částku (např. 100.50): ")
    variable_symbol = input("Zadejte variabilní symbol (nepovinné, stiskněte Enter pro přeskočení): ")
    constant_symbol = input("Zadejte konstantní symbol (nepovinné, stiskněte Enter pro přeskočení): ")
    specific_symbol = input("Zadejte specifický symbol (nepovinné, stiskněte Enter pro přeskočení): ")
    message = input("Zadejte poznámku pro příjemce (nepovinné, stiskněte Enter pro přeskočení): ")

    # Vytvoření dat ve formátu QR Platba
    qr_payment_data = f"SPD*1.0*ACC:{account_number}*AM:{amount}"
    if variable_symbol:
        qr_payment_data += f"*X-VS:{variable_symbol}"
    if constant_symbol:
        qr_payment_data += f"*X-KS:{constant_symbol}"
    if specific_symbol:
        qr_payment_data += f"*X-SS:{specific_symbol}"
    if message:
        qr_payment_data += f"*MSG:{message}"

    # Název výstupního souboru
    output_filename = "payment_qr.png"

    # Generování QR kódu
    generate_qr_code(qr_payment_data, output_filename)
    print(f"QR kód pro platbu byl uložen jako {output_filename}.")