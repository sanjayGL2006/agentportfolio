import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)

def create_resume(output_path):
    # Page setup - 0.35 inch margins for clean multi-page / single document flow
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=30,
        rightMargin=30,
        topMargin=28,
        bottomMargin=28
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
        fontSize=10,
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
        alignment=2
    )

    style_section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=PRIMARY,
        spaceBefore=8,
        spaceAfter=4
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
        leading=11.5,
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
        Paragraph("SANJAY GL", style_name),
        Spacer(1, 2),
        Paragraph("BCA Student &nbsp;|&nbsp; Full-Stack Developer &nbsp;|&nbsp; AI & Web Technology Enthusiast", style_title),
    ]

    contact_text = (
        "<b>Phone:</b> +91 81239 81877 &nbsp;|&nbsp; <b>Email:</b> sanjaygl2006@gmail.com<br/>"
        "<b>Location:</b> Shivamogga, Karnataka, India<br/>"
        "<b>LinkedIn:</b> linkedin.com/in/sanjay-gl-b86631336<br/>"
        "<b>GitHub:</b> github.com/sanjayGL2006 &nbsp;|&nbsp; <b>Portfolio:</b> sanjaygl30ai.vercel.app"
    )
    right_header = [Paragraph(contact_text, style_contact)]

    header_table = Table([[left_header, right_header]], colWidths=[310, 242])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.2, color=ACCENT, spaceBefore=0, spaceAfter=6))

    # Professional Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", style_section_heading))
    summary_text = (
        "Motivated and results-driven BCA student (2nd Year, 4th Semester) at PES Institute of Advanced Management Studies, "
        "Shivamogga, with strong hands-on experience in full-stack web development using Python Flask, JavaScript, HTML/CSS, "
        "Java, and SQL. Recognised as Star Performer during AICTE internship at Oasis Infobyte. Passionate about building "
        "real-world applications, AI integrations, and clean user interfaces. Actively seeking part-time, freelance, and "
        "internship opportunities to apply and grow technical skills."
    )
    story.append(Paragraph(summary_text, style_body))

    # Education
    story.append(Paragraph("EDUCATION", style_section_heading))
    edu1_table = Table([
        [Paragraph("Bachelor of Computer Applications (BCA) &nbsp;|&nbsp; 2nd Year, 4th Semester", style_item_title), Paragraph("2023 – 2026 (Expected)", style_item_date)]
    ], colWidths=[412, 140])
    edu1_table.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(edu1_table)
    story.append(Paragraph("PES Institute of Advanced Management Studies (PESIAMS) — Shivamogga, Karnataka", style_item_subtitle))
    story.append(Spacer(1, 3))

    edu2_table = Table([
        [Paragraph("Pre-University Course (PCMCs / Science)", style_item_title), Paragraph("Completed 2023", style_item_date)]
    ], colWidths=[412, 140])
    edu2_table.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(edu2_table)
    story.append(Paragraph("PES PU College — Shivamogga, Karnataka", style_item_subtitle))

    # Internships & Work Experience
    story.append(Paragraph("INTERNSHIPS & WORK EXPERIENCE", style_section_heading))

    exp1_table = Table([
        [Paragraph("Web Development & Designing Intern &nbsp;|&nbsp; Oasis Infobyte · AICTE OIB-SIP", style_item_title), Paragraph("Feb 2026 – Mar 2026", style_item_date)]
    ], colWidths=[412, 140])
    exp1_table.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(exp1_table)
    story.append(Paragraph("Remote &nbsp;|&nbsp; Certificate ID: OIB/F1/IP353", style_item_subtitle))
    story.append(Paragraph("• Completed 1-month AICTE-recognised remote internship in Web Development and Designing.", style_bullet))
    story.append(Paragraph("• Built and deployed real-world web projects under ISO 9001:2015 certified program.", style_bullet))
    story.append(Paragraph("• Recognised as Star Performer for exceptional dedication and outstanding contributions.", style_bullet))
    story.append(Spacer(1, 3))

    exp2_table = Table([
        [Paragraph("Software Engineering Virtual Experience &nbsp;|&nbsp; JPMorgan Chase · Forage", style_item_title), Paragraph("2025", style_item_date)]
    ], colWidths=[412, 140])
    exp2_table.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(exp2_table)
    story.append(Paragraph("Virtual", style_item_subtitle))
    story.append(Paragraph("• Completed JPMorgan Chase Software Engineering Job Simulation via Forage.", style_bullet))
    story.append(Paragraph("• Worked with Java-based tasks simulating real-world financial software engineering.", style_bullet))
    story.append(Spacer(1, 3))

    exp3_table = Table([
        [Paragraph("Web Development Intern &nbsp;|&nbsp; CodSoft", style_item_title), Paragraph("2025", style_item_date)]
    ], colWidths=[412, 140])
    exp3_table.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(exp3_table)
    story.append(Paragraph("Remote", style_item_subtitle))
    story.append(Paragraph("• Completed Web Development and Full-Stack internship remotely via CodSoft.", style_bullet))
    story.append(Paragraph("• Delivered UI/UX design and interactive web projects as part of internship deliverables.", style_bullet))
    story.append(Spacer(1, 3))

    exp4_table = Table([
        [Paragraph("Virtual Internship Program &nbsp;|&nbsp; AICTE EduSkills", style_item_title), Paragraph("2025", style_item_date)]
    ], colWidths=[412, 140])
    exp4_table.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(exp4_table)
    story.append(Paragraph("Remote", style_item_subtitle))
    story.append(Paragraph("• Completed AICTE-recognised virtual internship via EduSkills Foundation.", style_bullet))

    # Projects
    story.append(Paragraph("PROJECTS", style_section_heading))

    # Project 1: PureWeaves
    p1_table = Table([
        [Paragraph("PureWeaves — Saree & Textile E-Commerce Platform", style_item_title), Paragraph("Python Flask · JS · HTML/CSS · SQLite", style_item_date)]
    ], colWidths=[362, 190])
    p1_table.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(p1_table)
    story.append(Paragraph("• Built a full-stack e-commerce platform for saree kuchu and South Indian textile products.", style_bullet))
    story.append(Paragraph("• Developed REST API with Flask backend, product catalog, cart, wishlist, and WhatsApp order integration.", style_bullet))
    story.append(Paragraph("• Deployed frontend on Vercel and backend on Render; implemented PWA service worker.", style_bullet))
    story.append(Paragraph("• Handled SEO keyword strategy, branding (Handcrafted with Love), and mobile-first UI design.", style_bullet))
    story.append(Spacer(1, 3))

    # Project 2: Vinayaka
    p2_table = Table([
        [Paragraph("Vinayaka — AI Educational Chatbot", style_item_title), Paragraph("Flask · Gemini API · OpenAI · Voice", style_item_date)]
    ], colWidths=[362, 190])
    p2_table.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(p2_table)
    story.append(Paragraph("• Built an AI-powered educational chatbot with Gemini/OpenAI cascade fallback.", style_bullet))
    story.append(Paragraph("• Implemented multilingual support and voice assistant features for student accessibility.", style_bullet))
    story.append(Spacer(1, 3))

    # Project 3: Vibe Chat
    p3_table = Table([
        [Paragraph("Vibe Chat — Real-Time Chat Application", style_item_title), Paragraph("Python Flask · SocketIO · HTML/CSS/JS", style_item_date)]
    ], colWidths=[362, 190])
    p3_table.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(p3_table)
    story.append(Paragraph("• Developed a real-time web chat application using Flask-SocketIO.", style_bullet))
    story.append(Paragraph("• Implemented room-based messaging, user sessions, and a dark-themed UI.", style_bullet))
    story.append(Spacer(1, 3))

    # Project 4: GrabNotes
    p4_table = Table([
        [Paragraph("GrabNotes — Flask Notes Management System", style_item_title), Paragraph("Python Flask · SQLite · REST API", style_item_date)]
    ], colWidths=[362, 190])
    p4_table.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(p4_table)
    story.append(Paragraph("• Built a notes management system with subject/unit folder structure and REST API.", style_bullet))
    story.append(Paragraph("• Implemented verification workflow and Google Drive integration.", style_bullet))
    story.append(Spacer(1, 3))

    # Other Projects
    story.append(Paragraph("<b>Other Projects:</b>", style_item_title))
    story.append(Paragraph("• <b>BMI Calculator:</b> Flask + Canvas charts + JSON history tracking.", style_bullet))
    story.append(Paragraph("• <b>Weather App:</b> CLI and browser-based using Open-Meteo + Nominatim APIs.", style_bullet))
    story.append(Paragraph("• <b>Random Password Generator:</b> Flask backend with cryptographic security + dark cyberpunk UI.", style_bullet))
    story.append(Paragraph("• <b>Personal Portfolio Website:</b> Dark cyber theme, 84+ certificates, interactive skills and projects sections.", style_bullet))

    # Technical Skills
    story.append(Paragraph("TECHNICAL SKILLS", style_section_heading))
    skills_data = [
        [Paragraph("Languages:", style_skill_cat), Paragraph("Python · Java · JavaScript · HTML5 · CSS3 · SQL", style_body)],
        [Paragraph("Frameworks & Libraries:", style_skill_cat), Paragraph("Flask · SocketIO · React (basics) · Bootstrap", style_body)],
        [Paragraph("Databases:", style_skill_cat), Paragraph("SQLite · MySQL · MongoDB (basics)", style_body)],
        [Paragraph("Tools & Platforms:", style_skill_cat), Paragraph("Git · GitHub · VS Code · Vercel · Render · Postman · Figma (basics)", style_body)],
        [Paragraph("Cloud & DevOps:", style_skill_cat), Paragraph("Google Cloud (basics) · Azure Fundamentals · IBM Cloud", style_body)],
        [Paragraph("Other:", style_skill_cat), Paragraph("REST APIs · PWA · Prompt Engineering · AI Workflow Automation · Process Mining (Celonis)", style_body)]
    ]
    skills_table = Table(skills_data, colWidths=[125, 427])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(skills_table)

    # Key Certifications
    story.append(Paragraph("KEY CERTIFICATIONS", style_section_heading))
    certs_list = [
        "• AICTE Web Development Internship — Oasis Infobyte (Star Performer) · 2026",
        "• Python (Basic & Advanced) — HackerRank · Udemy · Coursera · 2025–2026",
        "• JavaScript (Basic), SQL (Basic & Intermediate), Java (Basic), CSS — HackerRank · 2025",
        "• Blockchain Technology & Applications — NPTEL · 2025",
        "• Database Management Systems — NPTEL / IIT Madras · 2025",
        "• Cybersecurity Fundamentals — Cisco Networking Academy · 2025",
        "• Microsoft Azure Fundamentals (AZ-900) — Microsoft · 2025",
        "• Introduction to Cloud Computing — IBM / Coursera · 2025",
        "• AI and Machine Learning Essentials — DeepLearning.AI · 2025",
        "• Data Structures and Algorithms in Java — Coding Ninjas · 2025",
        "• React.js & Frontend Development — Scrimba · Simplilearn · 2025",
        "• Process Mining — Celonis Academy · 2025",
        "• Safe & Responsible Use of AI Quiz — MeitY / ISEA / Digital India (Government of India) · 2025",
        "• National Road Safety Quiz — Ministry of Road Transport & Highways / MyGov · 2025"
    ]
    for c in certs_list:
        story.append(Paragraph(c, style_bullet))

    # Achievements & Awards
    story.append(Paragraph("ACHIEVEMENTS & AWARDS", style_section_heading))
    achievements_list = [
        "• <b>Star Performer Award:</b> AICTE Oasis Infobyte Web Dev Internship (2026)",
        "• <b>PRAVIDHI:</b> State Level BCA Tech Fest Coding Event, JSS College for Women, Mysore (2026)",
        "• <b>National Integration Camp Participant:</b> NSS / Ministry of Youth Affairs, Government of India",
        "• <b>My Bharat Youth Integration Camp:</b> Government of India Portal",
        "• <b>Cyber Security Cadet:</b> CDAC & ISEA Digital India / MeitY",
        "• <b>74+ Certificates:</b> Across Tech, Internship, Government & Leadership domains"
    ]
    for a in achievements_list:
        story.append(Paragraph(a, style_bullet))

    # Volunteer & Extra-Curricular
    story.append(Paragraph("VOLUNTEER & EXTRA-CURRICULAR", style_section_heading))
    vol_list = [
        "• <b>NSS Volunteer:</b> PES IAMS Shivamogga. Active participant in national camps, social service drives, and community awareness programs.",
        "• <b>Digital India Cybersecurity Awareness Pledge:</b> MeitY / Digital India",
        "• <b>Say No to Tobacco Pledge:</b> Ministry of Health & Family Welfare, Government of India"
    ]
    for v in vol_list:
        story.append(Paragraph(v, style_bullet))

    # Languages
    story.append(Paragraph("LANGUAGES", style_section_heading))
    story.append(Paragraph("Kannada (Native) &nbsp;·&nbsp; English (Professional) &nbsp;·&nbsp; Tamil (Mother tongue)", style_body))

    # Declaration
    story.append(Paragraph("DECLARATION", style_section_heading))
    story.append(Paragraph("I hereby declare that the information provided above is true and correct to the best of my knowledge and belief.", style_body))
    story.append(Spacer(1, 4))
    dec_table = Table([
        [Paragraph("<b>Place:</b> Shivamogga, Karnataka<br/><b>Date:</b> June 2026", style_body), Paragraph("<b>Sanjay GL</b>", style_item_date)]
    ], colWidths=[300, 252])
    dec_table.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(dec_table)

    doc.build(story)
    print(f"Successfully generated updated PDF resume at: {output_path}")

if __name__ == "__main__":
    out_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "Sanjay_GL_Resume.pdf")
    create_resume(out_file)
