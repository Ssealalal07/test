from fpdf import FPDF
from factories.abstract_factory import Header, Table, Image, ReportFactory

class PDFHeader(Header):
    def __init__(self, pdf):
        self.pdf = pdf

    def render(self, text):
        self.pdf.set_font('Arial', 'B', 20)
        self.pdf.cell(200, 10, txt=text, align='C')


class PDFTable(Table):
    def __init__(self, pdf):
        self.pdf = pdf

    def render(self, data):
        self.pdf.set_font('Arial', size=12)
        for row in data:
            for item in row:
                self.pdf.cell(40, 10, txt=str(item), border=1)
            self.pdf.ln()# перенос строки

class PDFImage(Image):
    def __init__(self, pdf):
        self.pdf = pdf

    def render(self, path):
        self.pdf.image(path, w=100)

class PDFReportFactory(ReportFactory):
    def __init__(self):
        self.pdf =FPDF()
        self.pdf.add_page()

    def create_header(self) -> Header:
        return PDFHeader(self.pdf)

    def create_table(self) -> Table:
        return PDFTable(self.pdf)

    def create_image(self) -> Image:
        return PDFImage(self.pdf)

    def save(self, filename):
        self.pdf.output(filename)




# [  ['id', 'name', 'city'],
#     [1, 'Sasha', 'NSK'],
# ]


# pdf = FPDF()
# pdf.set_font()
# pdf.cell()