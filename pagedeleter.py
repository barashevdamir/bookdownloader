from PyPDF2 import PdfWriter, PdfReader
pages_to_keep = [0] # page numbering starts from 0
for i in range(1,351):
    source = f'book{i}.pdf'
    infile = PdfReader(source, 'rb')
    output = PdfWriter()

    for j in pages_to_keep:
        p = infile.pages[j]
        output.add_page(p)

    with open(f'newbook{i}.pdf', 'wb') as f:
        output.write(f)