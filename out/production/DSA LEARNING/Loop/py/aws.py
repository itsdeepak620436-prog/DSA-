"""
AWS Core Services — 8-Slide Presentation Generator
Run: python aws_presentation.py
Output: AWS_Core_Services.pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.dml import MSO_THEME_COLOR

# ── Color Palette ──────────────────────────────────────────────────────────────
BG_DARK      = RGBColor(0x1B, 0x1B, 0x2F)   # dark navy
BG_SLIDE2    = RGBColor(0x16, 0x1A, 0x2E)   # slightly lighter navy
ACCENT_BLUE  = RGBColor(0x00, 0xBC, 0xE5)   # EC2 column
ACCENT_ORNG  = RGBColor(0xFF, 0x99, 0x00)   # Lambda / highlights
ACCENT_PURP  = RGBColor(0x7B, 0x2C, 0xBF)   # DynamoDB column
ACCENT_TEAL  = RGBColor(0x00, 0xD2, 0xBE)   # S3 column
ACCENT_RED   = RGBColor(0xE8, 0x14, 0x3C)   # RDS column
ACCENT_GREEN = RGBColor(0x1E, 0x88, 0xE5)   # VPC
ACCENT_GOLD  = RGBColor(0xFF, 0xC1, 0x07)   # Route 53
WHITE        = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY   = RGBColor(0xCC, 0xCC, 0xCC)
DIM_GRAY     = RGBColor(0x88, 0x88, 0xAA)

# ── Helpers ───────────────────────────────────────────────────────────────────
def new_prs():
    prs = Presentation()
    prs.slide_width  = Inches(13.33)
    prs.slide_height = Inches(7.5)
    return prs

def blank_layout(prs):
    return prs.slide_layouts[6]          # truly blank

def fill_bg(slide, color):
    from pptx.oxml.ns import qn
    from lxml import etree
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_text(slide, text, left, top, width, height,
             font_size=24, bold=False, color=WHITE,
             align=PP_ALIGN.LEFT, italic=False, wrap=True):
    txb = slide.shapes.add_textbox(left, top, width, height)
    tf  = txb.text_frame
    tf.word_wrap = wrap
    p   = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size  = Pt(font_size)
    run.font.bold  = bold
    run.font.color.rgb = color
    run.font.italic = italic
    return txb

def add_rect(slide, left, top, width, height, fill_color, alpha=None):
    shape = slide.shapes.add_shape(
        1,  # MSO_SHAPE_TYPE.RECTANGLE
        left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.fill.background()          # no border
    return shape

def add_bullet_box(slide, items, left, top, width, height,
                   accent, font_size=15, title_size=20, title=""):
    """A colored box with a title and bullet items."""
    rect = add_rect(slide, left, top, width, height, RGBColor(0x22, 0x22, 0x44))
    # title
    if title:
        add_text(slide, title, left + Inches(0.15), top + Inches(0.1),
                 width - Inches(0.3), Inches(0.45),
                 font_size=title_size, bold=True, color=accent)
    # bullets
    for i, item in enumerate(items):
        y = top + Inches(0.6) + Inches(0.35) * i
        add_text(slide, f"▸  {item}",
                 left + Inches(0.15), y,
                 width - Inches(0.3), Inches(0.32),
                 font_size=font_size, color=WHITE)
    return rect

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE BUILDERS
# ══════════════════════════════════════════════════════════════════════════════

def slide_1_title(prs):
    """Title slide"""
    s = prs.slides.add_slide(blank_layout(prs))
    fill_bg(s, BG_DARK)

    # Decorative top bar
    add_rect(s, Inches(0), Inches(0), Inches(13.33), Inches(0.12), ACCENT_ORNG)

    # Main title
    add_text(s, "☁️  Core AWS Services",
             Inches(1), Inches(1.4), Inches(11.33), Inches(1.2),
             font_size=56, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

    # Subtitle
    add_text(s, "The Building Blocks of Cloud Computing",
             Inches(1), Inches(2.5), Inches(11.33), Inches(0.6),
             font_size=26, bold=False, color=ACCENT_ORNG, align=PP_ALIGN.CENTER, italic=True)

    # Description box
    add_rect(s, Inches(1.5), Inches(3.3), Inches(10.33), Inches(1.1),
             RGBColor(0x25, 0x25, 0x50))
    add_text(s,
             "Amazon Web Services (AWS) provides cloud services that allow businesses "
             "and developers to build, store, process, and connect applications — "
             "without managing physical infrastructure.",
             Inches(1.7), Inches(3.45), Inches(9.9), Inches(0.9),
             font_size=17, color=LIGHT_GRAY, align=PP_ALIGN.CENTER)

    # Four category pills
    categories = [
        ("☁️  Compute — EC2, Lambda",         ACCENT_BLUE),
        ("🗄️  Storage — S3, EBS",              ACCENT_TEAL),
        ("🛢️  Database — RDS, DynamoDB",       ACCENT_RED),
        ("🌐  Networking — VPC, Route 53",     ACCENT_GREEN),
    ]
    for i, (cat, col) in enumerate(categories):
        x = Inches(1.5) + Inches(2.9) * i
        add_rect(s, x, Inches(4.65), Inches(2.75), Inches(0.7), RGBColor(0x22, 0x22, 0x44))
        add_text(s, cat, x + Inches(0.05), Inches(4.75), Inches(2.65), Inches(0.55),
                 font_size=14, bold=True, color=col, align=PP_ALIGN.CENTER)

    # Speaker cue
    add_text(s,
             '🎤 Say:  "AWS offers hundreds of cloud services, but today I will focus on '
             'eight important services from four major categories: compute, storage, '
             'database, and networking."',
             Inches(1), Inches(5.7), Inches(11.33), Inches(0.8),
             font_size=12, color=DIM_GRAY, align=PP_ALIGN.CENTER, italic=True)

    # Bottom bar
    add_rect(s, Inches(0), Inches(7.38), Inches(13.33), Inches(0.12), ACCENT_ORNG)

def slide_2_compute(prs):
    """Compute Services: EC2 & Lambda"""
    s = prs.slides.add_slide(blank_layout(prs))
    fill_bg(s, BG_SLIDE2)
    add_rect(s, Inches(0), Inches(0), Inches(13.33), Inches(0.12), ACCENT_ORNG)

    # Slide heading
    add_text(s, "Compute Services",
             Inches(0.5), Inches(0.25), Inches(12), Inches(0.7),
             font_size=36, bold=True, color=WHITE)
    add_text(s, "EC2  &  Lambda",
             Inches(0.5), Inches(0.85), Inches(12), Inches(0.5),
             font_size=22, bold=False, color=LIGHT_GRAY, italic=True)

    # ── EC2 Column ───────────────────────────────────────────────────────────
    add_rect(s, Inches(0.4), Inches(1.5), Inches(5.9), Inches(5.3),
             RGBColor(0x0D, 0x47, 0x87))   # dark blue bg

    add_text(s, "💻  Amazon EC2", Inches(0.6), Inches(1.65), Inches(5.5), Inches(0.55),
             font_size=24, bold=True, color=ACCENT_BLUE)
    add_text(s, "Elastic Compute Cloud", Inches(0.6), Inches(2.15), Inches(5.5), Inches(0.35),
             font_size=14, color=LIGHT_GRAY, italic=True)

    ec2_items = [
        "Provides virtual servers in the cloud",
        "Choose CPU, RAM, storage & OS",
        "Suitable for websites, apps & backend servers",
        "Pay according to the resources you use",
    ]
    for i, item in enumerate(ec2_items):
        y = Inches(2.65) + Inches(0.62) * i
        add_rect(s, Inches(0.55), y, Inches(0.08), Inches(0.35), ACCENT_BLUE)
        add_text(s, item, Inches(0.75), y, Inches(5.4), Inches(0.5),
                 font_size=16, color=WHITE)

    # Example box
    add_rect(s, Inches(0.55), Inches(5.15), Inches(5.6), Inches(0.7),
             RGBColor(0x15, 0x60, 0xA0))
    add_text(s, "📌  Example: Hosting a web application on a virtual server",
             Inches(0.7), Inches(5.22), Inches(5.3), Inches(0.55),
             font_size=14, color=ACCENT_BLUE, italic=True)

    # ── Center divider / VS ─────────────────────────────────────────────────
    add_text(s, "VS", Inches(5.95), Inches(3.5), Inches(1.4), Inches(0.7),
             font_size=32, bold=True, color=ACCENT_ORNG, align=PP_ALIGN.CENTER)

    # ── Lambda Column ────────────────────────────────────────────────────────
    add_rect(s, Inches(7.0), Inches(1.5), Inches(5.9), Inches(5.3),
             RGBColor(0x2D, 0x0A, 0x4E))   # dark purple bg

    add_text(s, "⚡  AWS Lambda", Inches(7.2), Inches(1.65), Inches(5.5), Inches(0.55),
             font_size=24, bold=True, color=ACCENT_PURP)
    add_text(s, "Serverless Compute", Inches(7.2), Inches(2.15), Inches(5.5), Inches(0.35),
             font_size=14, color=LIGHT_GRAY, italic=True)

    lambda_items = [
        "Runs code without managing a server",
        "Executes code when an event occurs",
        "Automatically scales according to demand",
        "Pay mainly for the time your code runs",
    ]
    for i, item in enumerate(lambda_items):
        y = Inches(2.65) + Inches(0.62) * i
        add_rect(s, Inches(7.15), y, Inches(0.08), Inches(0.35), ACCENT_PURP)
        add_text(s, item, Inches(7.35), y, Inches(5.4), Inches(0.5),
                 font_size=16, color=WHITE)

    add_rect(s, Inches(7.15), Inches(5.15), Inches(5.6), Inches(0.7),
             RGBColor(0x4A, 0x15, 0x80))
    add_text(s, "📌  Example: Automatically processing an uploaded image",
             Inches(7.3), Inches(5.22), Inches(5.3), Inches(0.55),
             font_size=14, color=ACCENT_PURP, italic=True)

    # Bottom note
    add_text(s,
             '🎤 Say:  "EC2 is useful when we need control over a virtual server, while '
             'Lambda is useful when we only want to run code in response to an event '
             'without managing servers."',
             Inches(0.5), Inches(6.95), Inches(12.33), Inches(0.5),
             font_size=11, color=DIM_GRAY, italic=True)

    add_rect(s, Inches(0), Inches(7.38), Inches(13.33), Inches(0.12), ACCENT_ORNG)

def slide_3_storage(prs):
    """Storage Services: S3 & EBS"""
    s = prs.slides.add_slide(blank_layout(prs))
    fill_bg(s, BG_SLIDE2)
    add_rect(s, Inches(0), Inches(0), Inches(13.33), Inches(0.12), ACCENT_TEAL)

    add_text(s, "Storage Services",
             Inches(0.5), Inches(0.25), Inches(12), Inches(0.7),
             font_size=36, bold=True, color=WHITE)
    add_text(s, "S3  &  EBS",
             Inches(0.5), Inches(0.85), Inches(12), Inches(0.5),
             font_size=22, color=LIGHT_GRAY, italic=True)

    # S3 column
    add_rect(s, Inches(0.4), Inches(1.5), Inches(5.9), Inches(5.0),
             RGBColor(0x0A, 0x3D, 0x3D))
    add_text(s, "📦  Amazon S3", Inches(0.6), Inches(1.65), Inches(5.5), Inches(0.55),
             font_size=24, bold=True, color=ACCENT_TEAL)
    add_text(s, "Simple Storage Service — Object Storage",
             Inches(0.6), Inches(2.15), Inches(5.5), Inches(0.35),
             font_size=14, color=LIGHT_GRAY, italic=True)

    s3_items = [
        "Stores files: images, videos, documents, backups",
        "Highly scalable and durable",
        "Accessible via internet or applications",
    ]
    for i, item in enumerate(s3_items):
        y = Inches(2.65) + Inches(0.55) * i
        add_rect(s, Inches(0.55), y, Inches(0.08), Inches(0.35), ACCENT_TEAL)
        add_text(s, item, Inches(0.75), y, Inches(5.4), Inches(0.5),
                 font_size=16, color=WHITE)

    add_rect(s, Inches(0.55), Inches(4.55), Inches(5.6), Inches(0.65),
             RGBColor(0x15, 0x60, 0x60))
    add_text(s, "📌  Example: Storing user profile pictures or website files",
             Inches(0.7), Inches(4.62), Inches(5.3), Inches(0.5),
             font_size=14, color=ACCENT_TEAL, italic=True)

    # Easy diff badge
    add_rect(s, Inches(0.55), Inches(5.4), Inches(5.6), Inches(0.7),
             RGBColor(0x05, 0x7A, 0x7A))
    add_text(s, "💡  S3 = Store files / objects  (globally)",
             Inches(0.7), Inches(5.47), Inches(5.3), Inches(0.55),
             font_size=15, bold=True, color=ACCENT_TEAL)

    # EBS column
    add_rect(s, Inches(7.0), Inches(1.5), Inches(5.9), Inches(5.0),
             RGBColor(0x3D, 0x1A, 0x0A))
    add_text(s, "💾  Amazon EBS", Inches(7.2), Inches(1.65), Inches(5.5), Inches(0.55),
             font_size=24, bold=True, color=ACCENT_ORNG)
    add_text(s, "Elastic Block Store — Block Storage",
             Inches(7.2), Inches(2.15), Inches(5.5), Inches(0.35),
             font_size=14, color=LIGHT_GRAY, italic=True)

    ebs_items = [
        "Provides block storage for EC2 instances",
        "Works like a virtual hard disk",
        "Suitable for OS, applications & databases",
        "Data persists even when EC2 is stopped",
    ]
    for i, item in enumerate(ebs_items):
        y = Inches(2.65) + Inches(0.5) * i
        add_rect(s, Inches(7.15), y, Inches(0.08), Inches(0.35), ACCENT_ORNG)
        add_text(s, item, Inches(7.35), y, Inches(5.4), Inches(0.5),
                 font_size=16, color=WHITE)

    add_rect(s, Inches(7.15), Inches(4.55), Inches(5.6), Inches(0.65),
             RGBColor(0x60, 0x40, 0x15))
    add_text(s, "📌  Example: Hosting OS & databases on EC2",
             Inches(7.3), Inches(4.62), Inches(5.3), Inches(0.5),
             font_size=14, color=ACCENT_ORNG, italic=True)

    add_rect(s, Inches(7.15), Inches(5.4), Inches(5.6), Inches(0.7),
             RGBColor(0x80, 0x50, 0x05))
    add_text(s, "💡  EBS = Virtual hard disk for EC2  (inside VPC)",
             Inches(7.3), Inches(5.47), Inches(5.3), Inches(0.55),
             font_size=15, bold=True, color=ACCENT_ORNG)

    add_rect(s, Inches(0), Inches(7.38), Inches(13.33), Inches(0.12), ACCENT_TEAL)

def slide_4_database(prs):
    """Database Services: RDS & DynamoDB"""
    s = prs.slides.add_slide(blank_layout(prs))
    fill_bg(s, BG_SLIDE2)
    add_rect(s, Inches(0), Inches(0), Inches(13.33), Inches(0.12), ACCENT_RED)

    add_text(s, "Database Services",
             Inches(0.5), Inches(0.25), Inches(12), Inches(0.7),
             font_size=36, bold=True, color=WHITE)
    add_text(s, "RDS  &  DynamoDB",
             Inches(0.5), Inches(0.85), Inches(12), Inches(0.5),
             font_size=22, color=LIGHT_GRAY, italic=True)

    # RDS column
    add_rect(s, Inches(0.4), Inches(1.5), Inches(5.9), Inches(5.0),
             RGBColor(0x3D, 0x0A, 0x0A))
    add_text(s, "🏛️  Amazon RDS", Inches(0.6), Inches(1.65), Inches(5.5), Inches(0.55),
             font_size=24, bold=True, color=ACCENT_RED)
    add_text(s, "Relational Database Service — SQL",
             Inches(0.6), Inches(2.15), Inches(5.5), Inches(0.35),
             font_size=14, color=LIGHT_GRAY, italic=True)

    rds_items = [
        "Managed relational database service",
        "Supports MySQL, PostgreSQL & others",
        "AWS handles backups & maintenance",
        "Uses tables, rows & columns",
    ]
    for i, item in enumerate(rds_items):
        y = Inches(2.65) + Inches(0.5) * i
        add_rect(s, Inches(0.55), y, Inches(0.08), Inches(0.35), ACCENT_RED)
        add_text(s, item, Inches(0.75), y, Inches(5.4), Inches(0.5),
                 font_size=16, color=WHITE)

    add_rect(s, Inches(0.55), Inches(4.75), Inches(5.6), Inches(0.65),
             RGBColor(0x60, 0x15, 0x15))
    add_text(s, "📌  Example: Storing customer or employee records",
             Inches(0.7), Inches(4.82), Inches(5.3), Inches(0.5),
             font_size=14, color=ACCENT_RED, italic=True)

    add_rect(s, Inches(0.55), Inches(5.55), Inches(5.6), Inches(0.7),
             RGBColor(0x80, 0x05, 0x05))
    add_text(s, "💡  RDS = Relational / SQL  (structured tables)",
             Inches(0.7), Inches(5.62), Inches(5.3), Inches(0.55),
             font_size=15, bold=True, color=ACCENT_RED)

    # DynamoDB column
    add_rect(s, Inches(7.0), Inches(1.5), Inches(5.9), Inches(5.0),
             RGBColor(0x1A, 0x0A, 0x3D))
    add_text(s, "🔑  DynamoDB", Inches(7.2), Inches(1.65), Inches(5.5), Inches(0.55),
             font_size=24, bold=True, color=ACCENT_PURP)
    add_text(s, "Fully Managed NoSQL Database",
             Inches(7.2), Inches(2.15), Inches(5.5), Inches(0.35),
             font_size=14, color=LIGHT_GRAY, italic=True)

    ddb_items = [
        "Fully managed NoSQL database",
        "Fast and flexible data access",
        "Automatically scales with demand",
        "Ultra-low latency for high-traffic apps",
    ]
    for i, item in enumerate(ddb_items):
        y = Inches(2.65) + Inches(0.5) * i
        add_rect(s, Inches(7.15), y, Inches(0.08), Inches(0.35), ACCENT_PURP)
        add_text(s, item, Inches(7.35), y, Inches(5.4), Inches(0.5),
                 font_size=16, color=WHITE)

    add_rect(s, Inches(7.15), Inches(4.75), Inches(5.6), Inches(0.65),
             RGBColor(0x40, 0x15, 0x80))
    add_text(s, "📌  Example: Gaming apps, shopping carts, high-traffic apps",
             Inches(7.3), Inches(4.82), Inches(5.3), Inches(0.5),
             font_size=14, color=ACCENT_PURP, italic=True)

    add_rect(s, Inches(7.15), Inches(5.55), Inches(5.6), Inches(0.7),
             RGBColor(0x55, 0x05, 0xA5))
    add_text(s, "💡  DynamoDB = NoSQL  (flexible, key-value, ultra-fast)",
             Inches(7.3), Inches(5.62), Inches(5.3), Inches(0.55),
             font_size=15, bold=True, color=ACCENT_PURP)

    add_rect(s, Inches(0), Inches(7.38), Inches(13.33), Inches(0.12), ACCENT_RED)

def slide_5_vpc(prs):
    """Networking: VPC"""
    s = prs.slides.add_slide(blank_layout(prs))
    fill_bg(s, BG_SLIDE2)
    add_rect(s, Inches(0), Inches(0), Inches(13.33), Inches(0.12), ACCENT_GREEN)

    add_text(s, "Networking: VPC",
             Inches(0.5), Inches(0.25), Inches(12), Inches(0.7),
             font_size=36, bold=True, color=WHITE)
    add_text(s, "Virtual Private Cloud — Your Private Network on AWS",
             Inches(0.5), Inches(0.85), Inches(12), Inches(0.45),
             font_size=18, color=LIGHT_GRAY, italic=True)

    # Diagram area
    # Internet
    add_rect(s, Inches(5.5), Inches(1.55), Inches(2.3), Inches(0.5), RGBColor(0x33, 0x33, 0x55))
    add_text(s, "🌐  Internet", Inches(5.5), Inches(1.6), Inches(2.3), Inches(0.4),
             font_size=15, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

    # Arrows (using narrow rects rotated — simplified as lines via text arrows)
    add_text(s, "         ↓           ", Inches(5.5), Inches(2.1), Inches(2.3), Inches(0.25),
             font_size=18, color=ACCENT_GREEN, align=PP_ALIGN.CENTER)

    # Internet Gateway
    add_rect(s, Inches(5.2), Inches(2.35), Inches(2.9), Inches(0.5), RGBColor(0x15, 0x50, 0x50))
    add_text(s, "🔗  Internet Gateway", Inches(5.2), Inches(2.4), Inches(2.9), Inches(0.4),
             font_size=14, bold=True, color=ACCENT_TEAL, align=PP_ALIGN.CENTER)

    add_text(s, "         ↓           ", Inches(5.5), Inches(2.9), Inches(2.3), Inches(0.25),
             font_size=18, color=ACCENT_GREEN, align=PP_ALIGN.CENTER)

    # VPC box
    add_rect(s, Inches(1.5), Inches(3.2), Inches(10.3), Inches(2.6),
             RGBColor(0x0A, 0x30, 0x30))
    add_text(s, "🛡️  VPC — Virtual Private Cloud",
             Inches(1.65), Inches(3.3), Inches(9.5), Inches(0.4),
             font_size=16, bold=True, color=ACCENT_GREEN)
    add_rect(s, Inches(1.5), Inches(3.2), Inches(10.3), Inches(0.06), ACCENT_GREEN)

    # Public Subnet
    add_rect(s, Inches(1.7), Inches(3.8), Inches(4.5), Inches(1.8),
             RGBColor(0x12, 0x40, 0x40))
    add_text(s, "Public Subnet", Inches(1.85), Inches(3.85), Inches(4.0), Inches(0.35),
             font_size=14, bold=True, color=ACCENT_TEAL)
    add_text(s, "💻 EC2 Instance\n(Web Server)",
             Inches(1.85), Inches(4.2), Inches(4.0), Inches(0.7),
             font_size=13, color=WHITE)

    # Private Subnet
    add_rect(s, Inches(7.1), Inches(3.8), Inches(4.5), Inches(1.8),
             RGBColor(0x1A, 0x1A, 0x40))
    add_text(s, "Private Subnet", Inches(7.25), Inches(3.85), Inches(4.0), Inches(0.35),
             font_size=14, bold=True, color=ACCENT_PURP)
    add_text(s, "🛢️  Database\n(RDS / DynamoDB)",
             Inches(7.25), Inches(4.2), Inches(4.0), Inches(0.7),
             font_size=13, color=WHITE)

    # Key components list (right side of diagram)
    components = [
        ("🔹 Subnets", "Divide the network into smaller sections"),
        ("🔹 Route Tables", "Control where traffic goes"),
        ("🔹 Security Groups", "Firewall — control traffic"),
    ]
    for i, (comp, desc) in enumerate(components):
        y = Inches(3.95) + Inches(0.38) * i
        add_text(s, comp, Inches(0.5), y, Inches(1.2), Inches(0.35),
                 font_size=13, bold=True, color=ACCENT_GREEN)
        add_text(s, desc, Inches(0.5), y + Inches(0.22), Inches(1.2), Inches(0.35),
                 font_size=11, color=LIGHT_GRAY)

    # Speaker cue
    add_text(s,
             '🎤 Say:  "VPC is like our own private network in the AWS cloud. It allows us '
             'to control how our resources communicate with each other and with the internet."',
             Inches(0.5), Inches(6.2), Inches(12.33), Inches(0.55),
             font_size=11, color=DIM_GRAY, italic=True)

    add_rect(s, Inches(0), Inches(7.38), Inches(13.33), Inches(0.12), ACCENT_GREEN)

def slide_6_route53(prs):
    """Networking: Route 53"""
    s = prs.slides.add_slide(blank_layout(prs))
    fill_bg(s, BG_SLIDE2)
    add_rect(s, Inches(0), Inches(0), Inches(13.33), Inches(0.12), ACCENT_GOLD)

    add_text(s, "Networking: Route 53",
             Inches(0.5), Inches(0.25), Inches(12), Inches(0.7),
             font_size=36, bold=True, color=WHITE)
    add_text(s, "DNS & Domain Management Service",
             Inches(0.5), Inches(0.85), Inches(12), Inches(0.45),
             font_size=18, color=LIGHT_GRAY, italic=True)

    # Left: Functions list
    add_rect(s, Inches(0.4), Inches(1.5), Inches(5.6), Inches(5.0),
             RGBColor(0x33, 0x28, 0x00))
    add_text(s, "📖  Main Functions", Inches(0.6), Inches(1.65), Inches(5.2), Inches(0.45),
             font_size=20, bold=True, color=ACCENT_GOLD)

    funcs = [
        ("🔄", "Converts domain names → IP addresses"),
        ("📝", "Registers & manages domain names"),
        ("🚦", "Routes users to your applications"),
        ("❤️", "Health checking & traffic routing"),
    ]
    for i, (icon, text) in enumerate(funcs):
        y = Inches(2.25) + Inches(0.65) * i
        add_rect(s, Inches(0.55), y, Inches(0.5), Inches(0.45),
                 RGBColor(0x55, 0x44, 0x00))
        add_text(s, icon, Inches(0.55), y, Inches(0.5), Inches(0.45),
                 font_size=18, align=PP_ALIGN.CENTER)
        add_text(s, text, Inches(1.15), y + Inches(0.08), Inches(4.7), Inches(0.5),
                 font_size=16, color=WHITE)

    # Right: How it works flow
    add_rect(s, Inches(6.3), Inches(1.5), Inches(6.5), Inches(3.2),
             RGBColor(0x33, 0x2A, 0x00))
    add_text(s, "🔀  How It Works", Inches(6.5), Inches(1.65), Inches(5.8), Inches(0.4),
             font_size=20, bold=True, color=ACCENT_GOLD)

    # Flow steps
    steps = [
        ("1", "User types:", "www.mywebsite.com", ACCENT_GOLD),
        ("2", "Route 53 looks up:", "the real IP address", ACCENT_TEAL),
        ("3", "Routes user to:", "the AWS Application", ACCENT_BLUE),
    ]
    for i, (num, label, value, col) in enumerate(steps):
        y = Inches(2.25) + Inches(0.7) * i
        # number circle (simplified as rect)
        add_rect(s, Inches(6.5), y, Inches(0.4), Inches(0.4), col)
        add_text(s, num, Inches(6.5), y, Inches(0.4), Inches(0.4),
                 font_size=14, bold=True, color=BG_DARK, align=PP_ALIGN.CENTER)
        add_text(s, f"{label}", Inches(7.05), y + Inches(0.05), Inches(2.3), Inches(0.35),
                 font_size=13, color=LIGHT_GRAY)
        add_text(s, value, Inches(7.05), y + Inches(0.3), Inches(5.5), Inches(0.35),
                 font_size=15, bold=True, color=WHITE)
        if i < 2:
            add_text(s, "       ↓", Inches(8.5), y + Inches(0.42), Inches(0.5), Inches(0.3),
                     font_size=14, color=col)

    # Comparison box
    add_rect(s, Inches(6.3), Inches(4.9), Inches(6.5), Inches(1.5),
             RGBColor(0x44, 0x3D, 0x00))
    add_text(s, "💡  Why Route 53?",
             Inches(6.5), Inches(5.0), Inches(5.5), Inches(0.35),
             font_size=16, bold=True, color=ACCENT_GOLD)
    add_text(s,
             "Users remember names, not numbers.\n"
             "Instead of:  54.123.45.67\n"
             "They type:   www.mywebsite.com",
             Inches(6.5), Inches(5.35), Inches(5.8), Inches(0.9),
             font_size=13, color=WHITE)

    # Speaker cue
    add_text(s,
             '🎤 Say:  "Route 53 works like the internet\'s phonebook. It helps users reach '
             'our application using a domain name instead of an IP address."',
             Inches(0.5), Inches(6.5), Inches(12.33), Inches(0.5),
             font_size=11, color=DIM_GRAY, italic=True)

    add_rect(s, Inches(0), Inches(7.38), Inches(13.33), Inches(0.12), ACCENT_GOLD)

def slide_7_together(prs):
    """How Services Work Together"""
    s = prs.slides.add_slide(blank_layout(prs))
    fill_bg(s, BG_DARK)
    add_rect(s, Inches(0), Inches(0), Inches(13.33), Inches(0.12), ACCENT_ORNG)

    add_text(s, "How AWS Services Work Together",
             Inches(0.5), Inches(0.2), Inches(12), Inches(0.65),
             font_size=34, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_text(s, "Building an Online Shopping Website 🛒",
             Inches(0.5), Inches(0.8), Inches(12), Inches(0.4),
             font_size=20, color=ACCENT_ORNG, align=PP_ALIGN.CENTER, italic=True)

    # ── Architecture diagram ─────────────────────────────────────────────────
    # Route 53
    add_rect(s, Inches(5.2), Inches(1.4), Inches(2.9), Inches(0.5),
             RGBColor(0x55, 0x44, 0x00))
    add_text(s, "📖  Route 53", Inches(5.2), Inches(1.45), Inches(2.9), Inches(0.4),
             font_size=15, bold=True, color=ACCENT_GOLD, align=PP_ALIGN.CENTER)

    # Arrow down
    add_text(s, "     ↓      ", Inches(5.5), Inches(1.95), Inches(2.3), Inches(0.25),
             font_size=16, color=LIGHT_GRAY, align=PP_ALIGN.CENTER)

    # VPC
    add_rect(s, Inches(1.5), Inches(2.3), Inches(10.3), Inches(3.8),
             RGBColor(0x0A, 0x2A, 0x2A))
    add_rect(s, Inches(1.5), Inches(2.3), Inches(10.3), Inches(0.07), ACCENT_GREEN)
    add_text(s, "🌐  VPC — Virtual Private Cloud",
             Inches(1.65), Inches(2.38), Inches(9.0), Inches(0.35),
             font_size=15, bold=True, color=ACCENT_GREEN)

    # EC2 box
    add_rect(s, Inches(2.0), Inches(2.85), Inches(2.8), Inches(1.3),
             RGBColor(0x0D, 0x47, 0x87))
    add_text(s, "💻  EC2\nWeb Server", Inches(2.1), Inches(2.95), Inches(2.5), Inches(0.7),
             font_size=14, bold=True, color=ACCENT_BLUE, align=PP_ALIGN.CENTER)

    # Lambda box
    add_rect(s, Inches(2.0), Inches(4.35), Inches(2.8), Inches(1.1),
             RGBColor(0x2D, 0x0A, 0x4E))
    add_text(s, "⚡  Lambda\nImage Processor", Inches(2.1), Inches(4.45), Inches(2.5), Inches(0.6),
             font_size=13, bold=True, color=ACCENT_PURP, align=PP_ALIGN.CENTER)

    # S3 box
    add_rect(s, Inches(5.2), Inches(2.85), Inches(2.8), Inches(2.6),
             RGBColor(0x0A, 0x3D, 0x3D))
    add_text(s, "📦  S3\nProduct Images\n& Assets",
             Inches(5.3), Inches(3.0), Inches(2.5), Inches(1.0),
             font_size=14, bold=True, color=ACCENT_TEAL, align=PP_ALIGN.CENTER)

    # RDS box
    add_rect(s, Inches(8.5), Inches(2.85), Inches(2.8), Inches(1.3),
             RGBColor(0x3D, 0x0A, 0x0A))
    add_text(s, "🏛️  RDS\nOrders &\nCustomers",
             Inches(8.6), Inches(2.95), Inches(2.5), Inches(0.7),
             font_size=14, bold=True, color=ACCENT_RED, align=PP_ALIGN.CENTER)

    # DynamoDB box
    add_rect(s, Inches(8.5), Inches(4.35), Inches(2.8), Inches(1.1),
             RGBColor(0x1A, 0x0A, 0x3D))
    add_text(s, "🔑  DynamoDB\nShopping Cart",
             Inches(8.6), Inches(4.45), Inches(2.5), Inches(0.6),
             font_size=14, bold=True, color=ACCENT_PURP, align=PP_ALIGN.CENTER)

    # Connection arrows (using arrows)
    add_text(s, "→", Inches(4.85), Inches(3.35), Inches(0.4), Inches(0.4),
             font_size=20, color=LIGHT_GRAY, align=PP_ALIGN.CENTER)
    add_text(s, "→", Inches(8.0), Inches(3.35), Inches(0.4), Inches(0.4),
             font_size=20, color=LIGHT_GRAY, align=PP_ALIGN.CENTER)
    add_text(s, "↓", Inches(5.55), Inches(4.4), Inches(0.4), Inches(0.4),
             font_size=20, color=LIGHT_GRAY, align=PP_ALIGN.CENTER)
    add_text(s, "↓", Inches(5.55), Inches(2.75), Inches(0.4), Inches(0.4),
             font_size=20, color=LIGHT_GRAY, align=PP_ALIGN.CENTER)

    # Role table at bottom
    add_rect(s, Inches(0.4), Inches(6.3), Inches(12.5), Inches(0.95),
             RGBColor(0x1E, 0x1E, 0x3A))

    role_data = [
        ("☁️ Route 53", "Directs user to the website"),
        ("🌐 VPC",      "Secures the entire network"),
        ("💻 EC2",      "Runs the web server"),
        ("⚡ Lambda",   "Auto-processes uploaded images"),
        ("🗄️ S3",       "Stores product images & assets"),
        ("🏛️ RDS",      "Manages orders & customer data"),
        ("🔑 DynamoDB", "Handles shopping cart & sessions"),
    ]
    col_w = Inches(12.5) / 4
    for i, (svc, role) in enumerate(role_data):
        col = i % 4
        row = i // 4
        x = Inches(0.55) + col_w * col
        y = Inches(6.38) + row * Inches(0.42)
        add_text(s, f"{svc}  →  {role}", x, y, col_w - Inches(0.1), Inches(0.4),
                 font_size=12, color=WHITE)

    add_rect(s, Inches(0), Inches(7.38), Inches(13.33), Inches(0.12), ACCENT_ORNG)

def slide_8_summary(prs):
    """Summary & Key Takeaways"""
    s = prs.slides.add_slide(blank_layout(prs))
    fill_bg(s, BG_DARK)
    add_rect(s, Inches(0), Inches(0), Inches(13.33), Inches(0.12), ACCENT_ORNG)

    add_text(s, "Summary & Key Takeaways",
             Inches(0.5), Inches(0.2), Inches(12), Inches(0.65),
             font_size=36, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

    # 8 service cards in 2 rows x 4 cols
    services = [
        ("💻",  "EC2",       "Virtual servers",    "Full control over OS & config",              ACCENT_BLUE),
        ("⚡",  "Lambda",    "Serverless compute", "Event-driven, auto-scaling tasks",           ACCENT_PURP),
        ("📦",  "S3",        "Object storage",     "Files, images, backups, static sites",       ACCENT_TEAL),
        ("💾",  "EBS",       "Block storage",      "Persistent disks for EC2",                   ACCENT_ORNG),
        ("🏛️", "RDS",       "SQL Database",       "Structured, relational data",                ACCENT_RED),
        ("🔑",  "DynamoDB",  "NoSQL Database",     "Fast, flexible, high-scale data",            ACCENT_PURP),
        ("🌐",  "VPC",       "Private network",    "Isolated, secure cloud network",             ACCENT_GREEN),
        ("📖",  "Route 53",  "DNS Service",        "Domain names & traffic routing",             ACCENT_GOLD),
    ]

    card_w = Inches(2.95)
    card_h = Inches(1.55)
    for i, (icon, name, what, when, col) in enumerate(services):
        row = i // 4
        col_idx = i % 4
        x = Inches(0.45) + card_w * col_idx
        y = Inches(1.1) + Inches(1.75) * row

        # Card bg
        add_rect(s, x, y, card_w, card_h, RGBColor(0x22, 0x22, 0x44))
        # Accent top bar
        add_rect(s, x, y, card_w, Inches(0.08), col)

        add_text(s, f"{icon}  {name}", x + Inches(0.1), y + Inches(0.12),
                 card_w - Inches(0.2), Inches(0.45),
                 font_size=20, bold=True, color=col)
        add_text(s, what, x + Inches(0.1), y + Inches(0.55),
                 card_w - Inches(0.2), Inches(0.35),
                 font_size=13, color=LIGHT_GRAY)
        add_text(s, f"when: {when}", x + Inches(0.1), y + Inches(0.88),
                 card_w - Inches(0.2), Inches(0.55),
                 font_size=11, color=DIM_GRAY, italic=True)

    # Closing statement
    add_text(s,
             "These eight AWS services form the backbone of modern cloud applications. "
             "With AWS, you focus on building — and AWS handles the infrastructure.",
             Inches(1), Inches(5.55), Inches(11.33), Inches(0.7),
             font_size=16, color=LIGHT_GRAY, align=PP_ALIGN.CENTER, italic=True)

    # Thank you
    add_text(s, "Thank You!  🙏",
             Inches(1), Inches(6.45), Inches(11.33), Inches(0.6),
             font_size=28, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

    add_text(s, "☁️  Built on AWS  |  Questions?",
             Inches(1), Inches(6.95), Inches(11.33), Inches(0.35),
             font_size=14, color=DIM_GRAY, align=PP_ALIGN.CENTER)

    add_rect(s, Inches(0), Inches(7.38), Inches(13.33), Inches(0.12), ACCENT_ORNG)

# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    prs = new_prs()
    slide_1_title(prs)
    slide_2_compute(prs)
    slide_3_storage(prs)
    slide_4_database(prs)
    slide_5_vpc(prs)
    slide_6_route53(prs)
    slide_7_together(prs)
    slide_8_summary(prs)

    output = "AWS_Core_Services.pptx"
    prs.save(output)
    print(f"✅  Saved: {output}  ({len(prs.slides)} slides)")