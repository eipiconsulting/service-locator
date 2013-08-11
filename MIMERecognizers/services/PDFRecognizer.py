from ..MIMERecognizerService import MIMERecognizerService
from lookup import ServiceProvider


@ServiceProvider(MIMERecognizerService)
class PDFRecognizer(MIMERecognizerService):
    def recognizes_extension(self, extension):
        return extension == ".pdf"

    def get_MIME_type(self):
        return "application/pdf"
