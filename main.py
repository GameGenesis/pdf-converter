import os
import random
from fpdf import FPDF

images = [str(i) for i in os.listdir('images')]

# Layout ('P', 'L')
# Unit ('mm', 'cm', 'in')
# Format ('A3', 'A4' (default), 'Letter', 'Legal', (100, 150))

pdf = FPDF()

pics_per_page = 2
current_pics = pics_per_page

x = 0
y = 0

for image in images:
    current_pics += 1
    if current_pics >= pics_per_page:
        pdf.add_page()
        current_pics = 0
    else:
        pdf.ln(10)

    pdf.image(os.path.join(os.getcwd(), 'images', image), w=(pdf.w - pdf.l_margin*2))

pdf.output('test.pdf', 'F')