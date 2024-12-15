# QR Code Generator in Python

This Python script allows you to generate QR codes from any given data (such as a URL, text, or any string). The QR code is saved as an image file (default is `qrcode.png`, but you can specify any filename).

## Requirements

To run this script, you need the `qrcode` Python library. You can install it via `pip`:

```bash
pip install qrcode[pil]
```
This will install both qrcode and the necessary Pillow library to handle image generation

--------------

## Usage

1. **Import the Library:** First, import the qrcode library in your script.
```python
import qrcode
```
2. **Generate QR Code:** Use the generate_qr_code() function to create and save a QR code image. You can pass the data you want to encode (like a URL, text, etc.), and optionally specify a filename for the saved image.
```python
data = "https://www.example.com"  # This can be any string, URL, or text you want to encode
generate_qr_code(data, "my_qr_code.png")
```

**With this you can generate any qr code for the URL you want, just replace the URL in the data veriable and you are set**
