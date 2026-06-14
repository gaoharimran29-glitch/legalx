from pypdf import PdfReader
import os

PDF_FOLDER = "data"

for file in os.listdir(PDF_FOLDER):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(PDF_FOLDER, file)

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        txt_name = file.replace(".pdf", ".txt")
        txt_path = os.path.join(PDF_FOLDER, txt_name)

        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Converted: {file} -> {txt_name}")

print("All PDFs converted!")