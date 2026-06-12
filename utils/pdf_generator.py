from reportlab.platypus import (
SimpleDocTemplate,
Paragraph,
Spacer
)

from reportlab.lib.styles import (
getSampleStyleSheet
)

def create_report():
    doc = SimpleDocTemplate(
        "reports/generated_reports/business_report.pdf"
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "AI Sales Intelligence Report",
            styles['Title']
        )
    )

    elements.append(
        Spacer(1,20)
    )

    elements.append(
        Paragraph(
            "Executive Business Summary",
            styles['Heading2']
        )
    )

    elements.append(
        Paragraph(
            """
            Revenue trend is positive.
            Customer engagement is increasing.
            Inventory remains healthy.
            AI Forecast predicts future growth.
            """,
            styles['BodyText']
        )
    )

    doc.build(elements)

