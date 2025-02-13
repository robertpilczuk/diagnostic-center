from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_pdf(test_result):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.drawString(100, 750, f"Test Name: {test_result.test_name}")
    pdf.drawString(100, 730, f"Patient: {test_result.patient.user.get_full_name()}")
    pdf.drawString(100, 710, f"Doctor: {test_result.doctor.user.get_full_name()}")
    pdf.drawString(
        100, 690, f"Date: {test_result.created_at.strftime('Y-%m-%d %H:%M:%S')}"
    )
    pdf.drawString(100, 670, "Results:")
    pdf.drawString(100, 650, test_result.result)
    pdf.save()
    buffer.seek(0)
    return buffer
