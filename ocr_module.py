import os
from doctr.io import DocumentFile
from doctr.models import ocr_predictor

ocr_model = ocr_predictor(pretrained=True)
def ocr(local_pdf_path, output_dir=None):
    doc = DocumentFile.from_pdf(local_pdf_path)
    result_text = ocr_model(doc).render()

    if output_dir is None:
        output_dir = os.path.dirname(local_pdf_path)
    output_text_path = os.path.join(output_dir, "ocr_result.txt")
    
    with open(output_text_path, "w", encoding="utf-8") as text_file:
        text_file.write(result_text)
    
    return output_text_path
