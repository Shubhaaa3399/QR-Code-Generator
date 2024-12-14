import qrcode

# Function to generate QR Code
def generate_qr_code(data, filename="qrcode.png"):
    # Create QR Code
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code (1 is the smallest, 40 is the largest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls error correction (L is the least, H is the most)
        box_size=10,  # size of each box in the QR code
        border=4,  # thickness of the border
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill="black", back_color="white")
    
    # Save the image
    img.save(filename)
    print(f"QR code saved as {filename}")

# Example usage:
data = "https://www.example.com"  # The data to encode in the QR code (could be a URL, text, etc.)
generate_qr_code(data, "my_qr_code.png")
