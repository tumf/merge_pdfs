import sys
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
import tempfile
import click


def is_pdf(file) -> bool:
    try:
        img = Image.open(file)
        img.verify()  # Verify if it's an image
        return img.format == 'PDF'
    except:
        raise f"The file should be image: {file}"

def convert_image_to_pdf(image_file, pdf_path):
    image = Image.open(image_file)
    image.convert("RGB").save(pdf_path)

@click.command()
@click.argument('files', nargs=-1)
@click.option('-o', '--output', type=str, default='merged.pdf',
              help='The output PDF file name.')
def merge_pdfs(files, output):
    if len(files) < 2:
        click.echo("Merge PDFs version 0.1.0")
        click.echo("USAGE: python src/merge.py <pdf1> <pdf2> <pdf3> ... "
              "[-o output_filename]")
        sys.exit(0)
    src_paths = files
    output_pdf_filename = output
    output_pdf = PdfWriter()

    for src_path in src_paths:
        if is_pdf(src_path):
            pdf_path = src_path
            pdf = PdfReader(pdf_path)
        else:
            with tempfile.NamedTemporaryFile(delete=True, suffix='.pdf') as temp_pdf:
                convert_image_to_pdf(src_path, temp_pdf.name)
                pdf_path = temp_pdf.name
                pdf = PdfReader(pdf_path)

        for page in pdf.pages:
            output_pdf.add_page(page)

    with open(output_pdf_filename, 'wb') as output_file:
        output_pdf.write(output_file)

    click.echo(f'Merged PDF saved as {output_pdf_filename}')


if __name__ == "__main__":
    merge_pdfs(sys.argv)
