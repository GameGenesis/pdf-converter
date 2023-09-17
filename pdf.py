import os
from fpdf import FPDF
from PIL import Image

# Layout ('P', 'L')
# Unit ('mm', 'cm', 'in')
# Format ('A3', 'A4' (default), 'Letter', 'Legal', (100, 150))

def convert_pdf(images, file_path, images_per_page=2, margin_btw_pics=10, fill_width=False):
    pdf = FPDF()

    pics_per_page = min(images_per_page, len(images))
    current_pics = pics_per_page

    for image in images:
        image_path = os.path.join(image)

        width, height = Image.open(image_path).size

        current_pics += 1
        if current_pics >= pics_per_page:
            pdf.add_page()
            current_pics = 0
        else:
            pdf.ln(margin_btw_pics)

        max_width = pdf.w - pdf.l_margin*2
        max_height = (pdf.h - pdf.t_margin*2 - margin_btw_pics*pics_per_page) // pics_per_page

        aspect_ratio = min(max_width/width, max_height/height)

        if not fill_width:
            # Keeps width and height (fill height)
            pdf.image(image_path, w=width*aspect_ratio, h=height*aspect_ratio)
        else:
            # To fill width, take max width instead (dropdown)
            pdf.image(image_path, w=max_width, h=height*aspect_ratio)

    file_name = file_path.split()[-1]
    file_dir = file_path[:-len(file_name)]
    pdf.output(f"{file_path}.pdf", 'F')