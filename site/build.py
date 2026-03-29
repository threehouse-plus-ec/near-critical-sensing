#!/usr/bin/env python3
"""Build static HTML pages from markdown source files."""

import markdown
import re
import os

SITE_DIR = "/home/claude/site"
SRC_DIR = os.path.join(SITE_DIR, "src")
CSS_PATH = "css/scholarly.css"

# Markdown extensions for footnotes, tables, etc.
MD_EXTENSIONS = ['footnotes', 'tables', 'smarty', 'toc']
MD_EXTENSION_CONFIGS = {
    'footnotes': {
        'BACKLINK_TEXT': '↩',
    },
    'smarty': {
        'smart_quotes': True,
        'smart_dashes': True,
    }
}

def get_css():
    """Read the CSS file content for inlining."""
    css_path = os.path.join(SITE_DIR, "css", "scholarly.css")
    with open(css_path, 'r') as f:
        return f.read()

def html_template(title, body, nav_links=None, subtitle=None):
    """Wrap body HTML in a complete page with inlined CSS."""
    css = get_css()
    
    nav = ""
    if nav_links:
        links = " ".join(f'<a href="{href}">{text}</a>' for text, href in nav_links)
        nav = f'<nav class="site-nav">{links}</nav>'
    
    subtitle_html = ""
    if subtitle:
        subtitle_html = f'<p><em>{subtitle}</em></p>'
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="css/scholarly.css">
  <style>
{css}
  </style>
</head>
<body>
  <main>
    {nav}
    {body}
  </main>
</body>
</html>
"""

def convert_md_to_html(md_text):
    """Convert markdown to HTML with extensions."""
    md = markdown.Markdown(
        extensions=MD_EXTENSIONS,
        extension_configs=MD_EXTENSION_CONFIGS
    )
    return md.convert(md_text)

def extract_front_matter(md_text):
    """Extract front-matter lines (Version, Date, Status, Endorsement) from markdown."""
    lines = md_text.split('\n')
    front_lines = []
    body_lines = []
    in_front = False
    front_done = False
    
    for line in lines:
        if not front_done and line.startswith('**Version:**'):
            in_front = True
        if in_front:
            if line.startswith('**') and ':' in line:
                # Clean up markdown bold
                clean = line.replace('**', '').strip()
                front_lines.append(clean)
            elif line.strip() == '':
                if front_lines:
                    front_done = True
                    in_front = False
                body_lines.append(line)
            else:
                front_done = True
                in_front = False
                body_lines.append(line)
        else:
            body_lines.append(line)
    
    return front_lines, '\n'.join(body_lines)

def build_page(src_filename, out_filename, title, nav_links, subtitle=None):
    """Build one HTML page from a markdown source file."""
    src_path = os.path.join(SRC_DIR, src_filename)
    out_path = os.path.join(SITE_DIR, out_filename)
    
    with open(src_path, 'r') as f:
        md_text = f.read()
    
    # Extract front matter
    front_lines, body_md = extract_front_matter(md_text)
    
    # Convert body
    body_html = convert_md_to_html(body_md)
    
    # Build front matter block
    front_html = ""
    if front_lines:
        items = "".join(f"<p>{line}</p>" for line in front_lines)
        front_html = f'<div class="front-matter">{items}</div>'
    
    # Insert front matter after first heading
    if front_html:
        body_html = body_html.replace('</h1>', f'</h1>\n{front_html}', 1)
    
    full_html = html_template(title, body_html, nav_links, subtitle)
    
    with open(out_path, 'w') as f:
        f.write(full_html)
    
    print(f"  Built: {out_filename}")

def build_landing_page():
    """Build the index/landing page."""
    body = """
<h1>Amplifiers at the Boundary</h1>
<p><em>A project on the epistemology of near-critical sensing</em></p>

<div class="front-matter">
<p>U. Warring · Physikalisches Institut, Albert-Ludwigs-Universität Freiburg</p>
<p>2026 · Local candidate framework (Harbour / Sail)</p>
</div>

<p>This project examines atmospheric instruments from the 15th to the 19th century through an epistemological lens, asking not <em>when</em> each device was invented but <em>what kind of knowledge</em> it produces. The central finding is a distinction between <strong>calibrated state instruments</strong> (barometers, thermometers, hygrometers), whose output can be inverted to recover an atmospheric variable, and <strong>sentinel instruments</strong> (storm glasses, leech barometers, frog barometers), whose output amplifies regime transitions but cannot be read backwards to recover any single quantity.</p>

<p>The project consists of two documents:</p>

<h2>Documents</h2>

<h3><a href="dossier.html">Historical Dossier: From Natural Signs to Measurement Networks</a></h3>
<p>A comprehensive historical survey of atmospheric instruments organised by epistemological function across six layers: state, transport, integration, radiation, electrical, and sentinel. Includes primary-source citations, historiographic references, and a detailed timeline. This is the <strong>Coastline</strong> document — it maps the historical territory.</p>
<p><em>Version 0.1.3 (frozen) · ~12,000 words</em></p>

<h3><a href="essay.html">Essay: Amplifiers at the Boundary</a></h3>
<p>An interpretive essay arguing that the 19th-century sentinel tradition — displaced because its devices were non-invertible — was asking a question that modern science now takes seriously: <em>how close is a system to a qualitative change?</em> Connects storm-glass physics to bifurcation theory, critical slowing down, and early warning signals, and proposes that near-critical sensing be recognised as a distinct measurement paradigm. This is the <strong>Sail</strong> document — it interprets and argues.</p>
<p><em>Version 0.2.1 (circulation-ready) · ~5,500 words</em></p>

<h2>How the two documents differ</h2>

<p>The <strong>dossier</strong> is documentary and historical. It establishes facts, dates, attributions, and sources. Its categories (state / transport / integration / radiation / electrical / sentinel) are explicitly marked as analytic rather than actor-native. It does not argue for a thesis; it maps an instrument landscape.</p>

<p>The <strong>essay</strong> is interpretive and argumentative. It takes the sentinel concept from the dossier and develops it into a physics argument about the relationship between sensitivity, invertibility, and proximity to regime boundaries. It is self-contained — it can be read without the dossier — but it references the dossier as a companion for readers who want fuller historical detail.</p>

<hr>

<p style="font-size: 0.85rem; color: #555;">Source texts maintained in Markdown. See <a href="https://github.com/">repository</a> for source files, licence, and citation information.</p>
"""
    
    full_html = html_template(
        "Amplifiers at the Boundary — Project Landing Page",
        body
    )
    
    out_path = os.path.join(SITE_DIR, "index.html")
    with open(out_path, 'w') as f:
        f.write(full_html)
    print("  Built: index.html")

def main():
    print("Building site...")
    
    nav = [
        ("Home", "index.html"),
        ("Dossier", "dossier.html"),
        ("Essay", "essay.html"),
    ]
    
    # Landing page
    build_landing_page()
    
    # Dossier
    build_page(
        "dossier-atmospheric-instruments.md",
        "dossier.html",
        "From Natural Signs to Measurement Networks",
        nav
    )
    
    # Essay
    build_page(
        "amplifiers-at-the-boundary.md",
        "essay.html",
        "Amplifiers at the Boundary",
        nav,
        subtitle="On the epistemology of near-critical sensing"
    )
    
    print("Done.")

if __name__ == "__main__":
    main()
