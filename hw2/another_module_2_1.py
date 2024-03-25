import os
from hw2.common.latex_tab_img_generation.latex_gen import generate_latex_table

data = [
    ["Name", "Surname", "Age", "Job", "Sex"],
    ["John", "Snow", 20,"Fighter", "Male"],
    ["Alice", "Tucker", 30, "Clerk", "Female"],
    ["Alan", "Zahan", 23, "Barista", "Female"],
    ["Nik","Pakunov", 25, "ML", "no experience"]
]

if not os.path.exists('artifacts'):
    os.makedirs('artifacts')

file_path = os.path.join('artifacts', 'table_2_1.tex')
latex_code = generate_latex_table(data)
full_latex_document = f"""
\\documentclass{{article}}
\\usepackage{{graphicx}}
\\begin{{document}}
{latex_code}
\\end{{document}}
"""

with open(file_path, "w") as file:
    file.write(full_latex_document)

print(f"File saved at: {file_path}")