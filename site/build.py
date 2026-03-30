#!/usr/bin/env python3
"""Build static HTML pages from markdown source files.

Reads markdown from the repository's canonical locations:
  - atmospheric-dossier/dossier-atmospheric-instruments-v0.1.3-FROZEN.md
  - essay/amplifiers-at-the-boundary-v0.4.0.md

Outputs HTML to site/ for GitHub Pages deployment.
"""

import markdown
import os
import sys

# Resolve paths relative to this script's parent (repo root)
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_DIR = os.path.join(REPO_ROOT, "site")
CSS_PATH = os.path.join(SITE_DIR, "css", "scholarly.css")

# Source files — canonical markdown locations
SOURCES = {
    "dossier": os.path.join(REPO_ROOT, "atmospheric-dossier",
                            "dossier-atmospheric-instruments-v0.1.3-FROZEN.md"),
    "essay": os.path.join(REPO_ROOT, "essay",
                          "amplifiers-at-the-boundary-v0.4.0.md"),
}

# Markdown extensions
MD_EXTENSIONS = ['footnotes', 'tables', 'smarty', 'toc']
MD_EXTENSION_CONFIGS = {
    'footnotes': {'BACKLINK_TEXT': '\u21a9'},
    'smarty': {'smart_quotes': True, 'smart_dashes': True},
}

NAV_LINKS = [
    ("Home", "index.html"),
    ("Dossier", "dossier.html"),
    ("Essay", "essay.html"),
]


def get_css():
    """Read the CSS file content for inlining."""
    with open(CSS_PATH, 'r') as f:
        return f.read()


def html_template(title, body_html, nav=True):
    """Wrap body HTML in a complete page with inlined CSS."""
    css = get_css()
    nav_html = ""
    if nav:
        links = " ".join(
            f'<a href="{href}">{text}</a>' for text, href in NAV_LINKS
        )
        nav_html = f'<nav class="site-nav">{links}</nav>'

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
    {nav_html}
    {body_html}
  </main>
</body>
</html>
"""


def convert_md(md_text):
    """Convert markdown to HTML with extensions."""
    md = markdown.Markdown(
        extensions=MD_EXTENSIONS,
        extension_configs=MD_EXTENSION_CONFIGS,
    )
    return md.convert(md_text)


def extract_front_matter(md_text):
    """Extract Version/Date/Status/Endorsement lines into a front-matter block."""
    lines = md_text.split('\n')
    front_lines = []
    body_lines = []
    in_front = False
    front_done = False

    for line in lines:
        if not front_done and line.startswith('**Version:**'):
            in_front = True
        if in_front:
            if line.startswith('**') and ':**' in line:
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


def build_document(src_path, out_filename, title):
    """Build one HTML page from a markdown source file."""
    if not os.path.exists(src_path):
        print(f"  WARNING: Source not found: {src_path}")
        return False

    with open(src_path, 'r') as f:
        md_text = f.read()

    front_lines, body_md = extract_front_matter(md_text)
    body_html = convert_md(body_md)

    # Insert front-matter block after first <h1>
    if front_lines:
        items = "".join(f"<p>{line}</p>" for line in front_lines)
        front_block = f'<div class="front-matter">{items}</div>'
        body_html = body_html.replace('</h1>', f'</h1>\n{front_block}', 1)

    full_html = html_template(title, body_html)
    out_path = os.path.join(SITE_DIR, out_filename)
    with open(out_path, 'w') as f:
        f.write(full_html)
    print(f"  Built: {out_filename}")
    return True


def build_landing_page():
    """Build the index/landing page."""
    body = """
<h1>Near-Critical Sensing</h1>
<p><em>A project on the epistemology and physics of boundary-sensitive measurement</em></p>

<div class="front-matter">
<p>U. Warring &middot; Physikalisches Institut, Albert-Ludwigs-Universit&auml;t Freiburg</p>
<p>2026 &middot; Local candidate framework (Harbour architecture)</p>
</div>

<p>This project examines sensing and measurement systems that operate near regime boundaries &mdash; from 19th-century weather glasses to quantum systems near exceptional points. It asks what kind of knowledge each device produces, and why some sensing modes persist while others are displaced.</p>

<p>The central finding is a distinction between <strong>calibrated state instruments</strong> (invertible: from the reading, one recovers the measured quantity) and <strong>sentinel instruments</strong> (non-invertible: the output amplifies proximity to a transition but cannot be read backwards to recover any single variable). That distinction, first developed historically, turns out to connect directly to modern physics: bifurcation theory, critical slowing down, early warning signals, and non-Hermitian quantum sensing near exceptional points.</p>

<h2>Documents</h2>

<h3><a href="dossier.html">Historical Dossier: From Natural Signs to Measurement Networks</a></h3>
<p>A comprehensive historical survey of atmospheric instruments (15th&ndash;19th century) organised by epistemological function across six analytic layers: state, transport, integration, radiation, electrical, and sentinel. Includes primary-source citations, historiographic references, and a detailed timeline. This is the <strong>Coastline</strong> document &mdash; it maps the historical territory.</p>
<p><em>Version 0.1.3 (frozen) &middot; ~12,000 words</em></p>

<h3><a href="essay.html">Essay: Amplifiers at the Boundary</a></h3>
<p>An interpretive essay arguing that the sentinel tradition was displaced because its devices were non-invertible, and that the question sentinels were trying to answer &mdash; <em>how close is a system to a qualitative change?</em> &mdash; is now central to modern science. Connects storm-glass physics to bifurcation theory, critical slowing down, early warning signals, and non-Hermitian quantum boundary sensing. This is the <strong>Sail</strong> document &mdash; it interprets and argues.</p>
<p><em>Version 0.4.0 (polished) &middot; ~7,500 words</em></p>

<h3>Quantum Dossier: Quantum Systems Near Critical Points <em>(in progress)</em></h3>
<p>A trapped-ion-centred survey of quantum systems near structural, spectral, topological, and dissipative boundaries. Organised by boundary type, not by platform. Includes a dedicated treatment of the EP sensing controversy (signal enhancement vs. noise penalty). This is a second <strong>Coastline</strong> document &mdash; it maps the quantum territory.</p>
<p><em>Section 0 frozen (v0.1.1) &middot; Section 1 drafted &middot; Sections 2&ndash;8 pending &middot; Projected ~18,000 words</em></p>

<h2>How the documents relate</h2>

<p>The <strong>historical dossier</strong> is documentary. It establishes facts, dates, attributions, and sources. Its categories are explicitly marked as analytic rather than actor-native.</p>

<p>The <strong>essay</strong> is argumentative. It takes the sentinel concept from the dossier and develops it into a physics argument about the relationship between sensitivity, invertibility, and proximity to regime boundaries. It is self-contained but references the dossier as a companion.</p>

<p>The <strong>quantum dossier</strong> is technical. It extends the boundary-sensing framework into quantum systems, using trapped ions as the anchor platform. It is standalone &mdash; it can be read without the other two documents &mdash; but shares the same organising principle: amplified response near a boundary, with attendant degradation of information recoverability.</p>

<hr>

<p style="font-size: 0.85rem; color: #555;">Source: <a href="https://github.com/threehouse-plus-ec/near-critical-sensing">github.com/threehouse-plus-ec/near-critical-sensing</a> &middot; Licence: <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a></p>
"""

    full_html = html_template(
        "Near-Critical Sensing \u2014 Project Landing Page", body, nav=False
    )
    out_path = os.path.join(SITE_DIR, "index.html")
    with open(out_path, 'w') as f:
        f.write(full_html)
    print("  Built: index.html")


def main():
    print(f"Building site from {REPO_ROOT} ...")

    # Check sources exist
    ok = True
    for name, path in SOURCES.items():
        if not os.path.exists(path):
            print(f"  WARNING: {name} source not found at {path}")
            ok = False

    if not ok:
        print("  Some sources missing. Building what is available.")

    build_landing_page()

    build_document(
        SOURCES["dossier"],
        "dossier.html",
        "From Natural Signs to Measurement Networks",
    )

    build_document(
        SOURCES["essay"],
        "essay.html",
        "Amplifiers at the Boundary",
    )

    print("Done.")


if __name__ == "__main__":
    main()
