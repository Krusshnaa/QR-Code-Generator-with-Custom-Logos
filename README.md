# Create Your Custom QRs with Logos in Python

This Python project allows you to generate QR codes for any link and customize them by embedding a logo in the center of the QR code. The project uses the `qrcode` and `Pillow` (PIL) libraries to create high-quality QR codes and place logos inside them.

## Features

- Generate QR codes from any link or text.
- Customize your QR code by embedding a logo or image in the center.
- Automatic resizing of the logo to fit the QR code.
- High error correction ensures the QR code remains scannable even with a logo.
- The logo area is cleared, so the QR code does not overlap with the logo.

## Requirements

Before running the project, make sure you have Python installed and the required libraries:

- **Python 3.x**
- **qrcode**
- **Pillow**

You can install the required libraries by running:

```bash
pip install qrcode Pillow
```
## How to Use
- Clone the repository or download the script to your local machine.
- Place the image you want to use as a logo in the same directory as the script.
- Update the link, logo_path, and output_path variables with your desired values.

## Example Code
```python
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
link = "https://your_link"
logo_path = "log_path.png"
output_path = "path_to_qr_with_logo.png"

generate_qr_with_logo(link, logo_path, output_path)
```
## Parameters  

-**link**: The URL or text you want to encode in the QR code.
-**logo_path**: Path to the logo image you want to embed in the QR code.
-**output_path**: The path where the final QR code image with the logo will be saved.
-**qr_size** (Optional): The size of the QR code (default is 300 pixels).
-**logo_size_ratio** (Optional): The ratio of the logo size relative to the QR code (default is 0.2).
## Example Command to Run the Script

```bash
python generate_qr_with_logo.py
```
## Example Output
The QR code will be saved as a PNG file, with the logo embedded in the center. The script ensures that the logo doesn’t interfere with the QR code by leaving a clear space in the middle.

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute this project as long as proper attribution is provided.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests if you have suggestions or improvements.

## Credits
This project makes use of the following open-source libraries:
- [qrcode](https://pypi.org/project/qrcode/)
- [Pillow](https://pypi.org/project/Pillow/)


