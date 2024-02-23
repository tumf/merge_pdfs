# Merge PDFs

This project provides a simple tool to merge multiple PDF files into a single PDF document. It leverages the PyPDF2 library to handle PDF manipulation tasks such as splitting, merging, cropping, and transforming PDF files.

## Installation

To install the necessary dependencies for this project, run the following command:

To use this tool, please follow the steps below:

1. Ensure Python 3.10 or higher is installed on your system.
2. Install Poetry if it's not already installed. You can do this by running the command: `pip install poetry`
3. Navigate to the project directory and install the required dependencies by running: `poetry install`

## Usage

To merge PDF files, run the command: `poetry run python merge_pdfs.py <pdf1> <pdf2> <pdf3> ...` where `<pdf1> <pdf2> <pdf3> ...` are the PDF files you wish to merge.

### Options

The `-o` option allows you to specify the name of the output PDF file. For example, use it as `poetry run python merge_pdfs.py <pdf1> <pdf2> -o output.pdf`. In this case, the merged PDF will be saved with the name `output.pdf`.
