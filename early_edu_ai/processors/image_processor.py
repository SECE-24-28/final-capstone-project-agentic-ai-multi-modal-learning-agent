import easyocr

class ImageProcessor:
    def __init__(self):
        print("Loading EasyOCR...")
        self.reader = easyocr.Reader(['en', 'ta'])
        print("EasyOCR ready!")

    def extract_text(self, image_path):
        results = self.reader.readtext(image_path)
        text = " ".join([r[1] for r in results
                        if r[2] > 0.5])
        return {"text": text}