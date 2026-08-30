import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)

def create_resume(output_path):
    # Page setup - 0.35 inch margins (25 points) for single page fit
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=28,
        rightMargin=28,
        topMargin=24,
        bottomMargin=24
    )

    styles = getSampleStyleSheet()

    # Color Palette
    PRIMARY = colors.HexColor("#0f172a")      # Dark Slate
    ACCENT = colors.HexColor("#0284c7")       # Ocean Blue
    TEXT_DARK = colors.HexColor("#334155")    # Charcoal body text
    TEXT_MUTED = colors.HexColor("#64748b")   # Slate muted

    # Typography Styles
    style_name = ParagraphStyle(
        'NameStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=25,
        textColor=PRIMARY
    )

    style_title = ParagraphStyle(
        'TitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13,
        textColor=ACCENT
    )

    style_contact = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=TEXT_MUTED,
        alignment=0
    )

    style_section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=13,
        textColor=PRIMARY,
        spaceAfter=3
    )

    style_item_title = ParagraphStyle(
        'ItemTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=PRIMARY
    )

    style_item_subtitle = ParagraphStyle(
        'ItemSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11,
        textColor=ACCENT
    )

    style_item_date = ParagraphStyle(
        'ItemDate',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=TEXT_MUTED,
        alignment=2
    )

    style_body = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=TEXT_DARK
    )

    style_bullet = ParagraphStyle(
        'BulletCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=11,
        textColor=TEXT_DARK,
        leftIndent=8
    )

    style_skill_cat = ParagraphStyle(
        'SkillCategory',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=PRIMARY
    )

    story = []

    # Header Table: Name & Title on Left, Contact info on Right
    left_header = [
        Paragraph("SANJAY G. L.", style_name),
        Spacer(1, 1),
        Paragraph("Full-Stack Software Engineer & AI/ML Developer", style_title),
    ]

    contact_text = (
        "<b>Email:</b> sanjaygl2006@gmail.com &nbsp;|&nbsp; <b>Phone:</b> +91 8123981877<br/>"
        "<b>Location:</b> Shivamogga, Karnataka, India<br/>"
        "<b>Portfolio:</b> sanjaygl30ai.vercel.app &nbsp;|&nbsp; <b>GitHub:</b> github.com/sanjayGL2006<br/>"
        "<b>LinkedIn:</b> linkedin.com/in/sanjaygl2006"
    )
    right_header = [Paragraph(contact_text, style_contact)]

    header_table = Table([[left_header, right_header]], colWidths=[290, 266])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.2, color=ACCENT, spaceBefore=0, spaceAfter=5))

    # Summary Section
    story.append(Paragraph("PROFESSIONAL SUMMARY", style_section_heading))
    summary_text = (
        "Motivated Full-Stack Web Developer and AI/ML enthusiast pursuing BCA (3rd Year) at PESIAMS. "
        "Demonstrated expertise in building production-ready Web Applications, REST APIs, Deep Learning models, "
        "and automated database migration workflows. Proven track record of developing 35+ full-stack projects, "
        "implementing robust CI/CD pipelines, and writing clean, scalable Python and JavaScript code."
    )
    story.append(Paragraph(summary_text, style_body))
    story.append(Spacer(1, 5))

    # Technical Skills Section
    story.append(Paragraph("TECHNICAL SKILLS", style_section_heading))
    skills_data = [
        [
            Paragraph("Languages & Core:", style_skill_cat),
            Paragraph("Python, JavaScript (ES6+), TypeScript, C, C++, Java, HTML5, CSS3, SQL", style_body)
        ],
        [
            Paragraph("Frameworks & Web:", style_skill_cat),
            Paragraph("React.js, Flask, FastAPI, Node.js, Express, Tailwind CSS, Bootstrap, REST APIs", style_body)
        ],
        [
            Paragraph("AI & Machine Learning:", style_skill_cat),
            Paragraph("TensorFlow, Keras, PyTorch, OpenCV, Scikit-Learn, Pandas, NumPy, YOLOv8, Gemini API", style_body)
        ],
        [
            Paragraph("Databases & Cloud:", style_skill_cat),
            Paragraph("SQLite, MySQL, PostgreSQL, Supabase (Vector DB & Auth), Google Cloud Run, Vercel", style_body)
        ],
        [
            Paragraph("Tools & Platforms:", style_skill_cat),
            Paragraph("Git, GitHub, Docker, Kubernetes, Linux (Bash), VS Code, ReportLab, Postman", style_body)
        ]
    ]
    skills_table = Table(skills_data, colWidths=[115, 441])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 5))

    # Experience Section
    story.append(Paragraph("WORK & INTERNSHIP EXPERIENCE", style_section_heading))
    
    exp_header1 = Table([
        [Paragraph("AI / ML Intern", style_item_title), Paragraph("2026 – Present", style_item_date)]
    ], colWidths=[416, 140])
    exp_header1.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('VALIGN', (0,0), (-1,-1), 'MIDDLE')]))
    story.append(exp_header1)
    story.append(Paragraph("Milano Infotech — Shivamogga, Karnataka", style_item_subtitle))
    story.append(Paragraph("• Architecting deep learning models and image recognition pipelines using OpenCV and TensorFlow.", style_bullet))
    story.append(Paragraph("• Integrating AI/ML model inference endpoints with Flask/FastAPI REST APIs for production environments.", style_bullet))
    story.append(Paragraph("• Assisting in dataset preprocessing, validation scoring, and real-time inference optimization.", style_bullet))
    story.append(Spacer(1, 4))

    exp_header2 = Table([
        [Paragraph("Web Development & Engineering Intern", style_item_title), Paragraph("2025", style_item_date)]
    ], colWidths=[416, 140])
    exp_header2.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('VALIGN', (0,0), (-1,-1), 'MIDDLE')]))
    story.append(exp_header2)
    story.append(Paragraph("Oasis Infobyte — Remote", style_item_subtitle))
    story.append(Paragraph("• Developed responsive, cross-browser web interfaces utilizing HTML5, CSS3, JavaScript, and React.", style_bullet))
    story.append(Paragraph("• Built interactive UI components, form validation engines, and serverless backend integrations.", style_bullet))
    story.append(Paragraph("• Collaborated on code reviews, version control workflows, and UI component optimization.", style_bullet))
    story.append(Spacer(1, 5))

    # Featured Projects Section
    story.append(Paragraph("FEATURED PROJECTS", style_section_heading))

    # Project 1: DataGauge
    p1_head = Table([
        [Paragraph("DataGauge — Dataset Quality Monitoring System", style_item_title), Paragraph("Python, FastAPI, React, Pandas, SQLite", style_item_date)]
    ], colWidths=[356, 200])
    p1_head.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(p1_head)
    story.append(Paragraph("• Engineered full-stack platform for CSV/Excel file validation, automated 0–100 quality scoring, and PDF report generation.", style_bullet))
    story.append(Spacer(1, 3))

    # Project 2: DermAI
    p2_head = Table([
        [Paragraph("DermAI — AI-Powered Skincare Diagnosis App", style_item_title), Paragraph("Python, Flask, TensorFlow, OpenCV", style_item_date)]
    ], colWidths=[356, 200])
    p2_head.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(p2_head)
    story.append(Paragraph("• Developed CNN model (94% accuracy) screening skin lesions with web triage guidance and patient summaries.", style_bullet))
    story.append(Spacer(1, 3))

    # Project 3: Paperless Office
    p3_head = Table([
        [Paragraph("Paperless Office & Billing Management System", style_item_title), Paragraph("Node.js, Electron, SQLite, PDFKit", style_item_date)]
    ], colWidths=[356, 200])
    p3_head.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(p3_head)
    story.append(Paragraph("• Created desktop billing system managing inventory tracking, tax calculations, and instant PDF invoicing.", style_bullet))
    story.append(Spacer(1, 3))

    # Project 4: Accident Risk Prediction
    p4_head = Table([
        [Paragraph("Accident Risk Prediction System", style_item_title), Paragraph("Flask, Scikit-Learn, Random Forest", style_item_date)]
    ], colWidths=[356, 200])
    p4_head.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(p4_head)
    story.append(Paragraph("• Implemented Random Forest ML model (98% accuracy) analyzing traffic parameters to predict road risk zones.", style_bullet))
    story.append(Spacer(1, 5))

    # Education Section
    story.append(Paragraph("EDUCATION & CERTIFICATIONS", style_section_heading))

    edu1_head = Table([
        [Paragraph("Bachelor of Computer Applications (BCA)", style_item_title), Paragraph("2023 – Present (3rd Year)", style_item_date)]
    ], colWidths=[396, 160])
    edu1_head.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(edu1_head)
    story.append(Paragraph("PES Institute of Advanced Management Studies (PESIAMS) — Shivamogga, Karnataka", style_item_subtitle))
    story.append(Paragraph("• Relevant Coursework: Data Structures, Database Management Systems (SQL), Operating Systems, Computer Networks.", style_bullet))
    story.append(Spacer(1, 3))

    edu2_head = Table([
        [Paragraph("30-Hour Blockchain Technology Certification", style_item_title), Paragraph("PESIAMS (2026)", style_item_date)]
    ], colWidths=[396, 160])
    edu2_head.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(edu2_head)

    story.append(Paragraph("• <b>Verified Certifications:</b> 90+ verified industry certifications in Web Development, Python, Cybersecurity, and AI.", style_bullet))
    story.append(Spacer(1, 5))

    # Leadership & Community
    story.append(Paragraph("LEADERSHIP & COMMUNITY INVOLVEMENT", style_section_heading))
    story.append(Paragraph("• <b>NSS & Youth for Seva Volunteer:</b> Active member of National Service Scheme (NSS) and Youth for Seva (YFS), organizing community outreach and tech literacy programs.", style_bullet))

    doc.build(story)
    print(f"Successfully generated 1-page PDF resume at: {output_path}")

if __name__ == "__main__":
    out_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "Sanjay_GL_Resume.pdf")
    create_resume(out_file)
