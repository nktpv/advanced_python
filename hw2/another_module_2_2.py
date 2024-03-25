from latex_tab_img_generation.latex_gen import generate_latex_table, generate_latex_image
import subprocess
from pdflatex import PDFLaTeX
from pathlib import Path


data = [
    ["Name", "Surname", "Age", "Job", "Sex"],
    ["John", "Snow", 20, "Fighter", "Male"],
    ["Alice", "Tucker", 30, "Clerk", "Female"],
    ["Alan", "Zahan", 23, "Barista", "Female"],
    ["Nik","Pakunov", 25, "ML", "no experience"]
]

latex_table = generate_latex_table(data)
image_path = "artifacts/photo_2_2.png"
latex_image = generate_latex_image(image_path)
latex_result = latex_table + "\n" + latex_image
full_latex_document = f"""
\\documentclass{{article}}
\\usepackage{{graphicx}}
\\begin{{document}}
{latex_result}
\\end{{document}}
"""
latex_doc_path = "artifacts/doc_2_2.tex"

with open(latex_doc_path, "w") as file:
    file.write(full_latex_document)

# proc = subprocess.Popen(['pdflatex', '-interaction=nonstopmode', Path(latex_doc_path).absolute()])
# proc.communicate()

pdfl = PDFLaTeX.from_texfile(latex_doc_path)
pdf, log, completed_process = pdfl.create_pdf()

with open("artifacts/doc_2_2.pdf", "wb") as pdfout:
    pdfout.write(pdf)
