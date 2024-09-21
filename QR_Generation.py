import qrcode
from PIL import Image, ImageDraw

def generate_qr_with_logo(link, logo_path, output_path, qr_size=300, logo_size_ratio=0.2):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction to fit the logo
        box_size=10,  # Size of each box (increase for larger QR codes)
        border=4,  # Thickness of the border (boxes)
    )
    qr.add_data(link)
    qr.make(fit=True)

    # Create the QR code image
    qr_img = qr.make_image(fill='black', back_color='white').convert('RGB')

    # Open the logo image
    logo = Image.open(logo_path)

    # Calculate the logo size based on the ratio and QR code size
    qr_width, qr_height = qr_img.size
    logo_size = int(qr_size * logo_size_ratio)
    logo = logo.resize((logo_size, logo_size))

    # Create a drawing context to draw the empty rectangle
    draw = ImageDraw.Draw(qr_img)

    # Calculate the position where the logo will be placed (center of the QR code)
    logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

    # Draw a white rectangle to make space for the logo
    white_rect_position = [
        (qr_width - logo_size) // 2, (qr_height - logo_size) // 2,
        (qr_width + logo_size) // 2, (qr_height + logo_size) // 2
    ]
    draw.rectangle(white_rect_position, fill="white")

    # Paste the logo onto the QR code
    qr_img.paste(logo, logo_position, mask=logo)

    # Save the resulting QR code
    qr_img.save(output_path)

    print(f"QR code with logo saved at: {output_path}")

# Example usage
link = "https://chat.whatsapp.com/BXLZ3h4PoBJKi97aQ0vnEq"
logo_path = "TRF.png"
output_path = "qr_with_logo.png"

generate_qr_with_logo(link, logo_path, output_path)
