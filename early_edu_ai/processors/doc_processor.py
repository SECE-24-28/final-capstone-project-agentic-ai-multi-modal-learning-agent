import fitz

class DocProcessor:
    def process(self, file_path):
        ext = file_path.split('.')[-1].lower()
        if ext == 'pdf':
            return self.process_pdf(file_path)
        elif ext == 'txt':
            return self.process_txt(file_path)
        return {"text": ""}

    def process_pdf(self, path):
        doc = fitz.open(path)
        text = ""
        for page in doc:
            text += page.get_text()
        return {"text": text}

    def process_txt(self, path):
        with open(path, 'r',
                  encoding='utf-8') as f:
            text = f.read()
        return {"text": text}