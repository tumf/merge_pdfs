import sys
from PyPDF2 import PdfReader, PdfWriter


def get_output_filename(args):
    if '-o' in args:
        o_index = args.index('-o')
        if o_index + 1 < len(args):
            output_filename = args[o_index + 1]
            # Add .pdf extension if it's missing
            if not output_filename.lower().endswith('.pdf'):
                output_filename += '.pdf'
            return output_filename, args[:o_index] + args[o_index+2:]
    return 'merged.pdf', args


if len(sys.argv) < 3:
    print("Merge PDFs version 0.1.0")
    print("USAGE: python src/merge.py <pdf1> <pdf2> <pdf3> ... "
          "[-o output_filename]")
    sys.exit()

output_pdf_filename, pdf_paths = get_output_filename(sys.argv[1:])

output_pdf = PdfWriter()

for pdf_path in pdf_paths:
    pdf = PdfReader(pdf_path)
    for page in pdf.pages:
        output_pdf.add_page(page)

with open(output_pdf_filename, 'wb') as output_file:
    output_pdf.write(output_file)

print(f'Merged PDF saved as {output_pdf_filename}')
