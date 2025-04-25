from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    qr_type = request.form.get("qr_type")
    filename = "generated_qr.png"

    if qr_type == "wifi":
        ssid = request.form.get("ssid")
        security = request.form.get("security")
        password = request.form.get("password")
        data = f"WIFI:S:{ssid};T:{security};P:{password};;"
    elif qr_type == "url":
        url = request.form.get("url")
        data = url
    elif qr_type == "payment":
        account = request.form.get("account")
        amount = request.form.get("amount")
        vs = request.form.get("vs")
        ks = request.form.get("ks")
        msg = request.form.get("msg")
        data = f"SPD*1.0*ACC:{account}*AM:{amount}"
        if vs:
            data += f"*X-VS:{vs}"
        if ks:
            data += f"*X-KS:{ks}"
        if msg:
            data += f"*MSG:{msg}"
    else:
        return "Neplatný typ QR kódu", 400

    generate_qr_code(data, filename)
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)