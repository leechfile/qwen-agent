import os
import argparse
import fitz  # PyMuPDF库

def pdf_to_txt(pdf_path, txt_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

def convert_folder(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                txt_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".txt")
                pdf_to_txt(pdf_path, txt_path)
                print(f"Converted: {pdf_path} to {txt_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF files in a folder to TXT files.")
    parser.add_argument("input_folder", help="Input folder containing PDF files")
    parser.add_argument("output_folder", help="Output folder to save TXT files")

    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    convert_folder(input_folder, output_folder)
