from factories.pdf_factory import PDFReportFactory
from  factories.docx_factory import DocxReportFactory

data = [
    ['Name', 'Age', 'City'],
    ['Ann', 56, 'Moscow'],
    ['Ivan', 36, 'SPB']
]

image_path = 'assets/image.png'
header_text = 'Report Abstract Factory'

def generate_report(factory, filename):
    header = factory.create_header()
    table = factory.create_table()
    image = factory.create_image()

    header.render(header_text)
    table.render(data)
    image.render(image_path)
    factory.save(filename)

generate_report(PDFReportFactory(), 'report.pdf')
generate_report(DocxReportFactory(), 'report.docx')