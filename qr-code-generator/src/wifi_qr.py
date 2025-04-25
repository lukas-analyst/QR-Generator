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
    # Načtení údajů o WiFi síti
    ssid = input("Zadejte název WiFi sítě (SSID): Pavucina")
    security = input("Zadejte typ zabezpečení (WPA, WEP, nopass): ")
    password = input("Zadejte heslo k WiFi síti (nechte prázdné pro otevřenou síť): ")

    # Vytvoření dat ve formátu pro WiFi QR kód
    wifi_data = f"WIFI:S:{ssid};T:{security};P:{password};;"

    # Název výstupního souboru
    output_filename = "wifi_qr.png"

    # Generování QR kódu
    generate_qr_code(wifi_data, output_filename)
    print(f"QR kód pro WiFi byl uložen jako {output_filename}.")