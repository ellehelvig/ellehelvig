"""Generate the original teal profile headers. Personal copy remains reserved."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def header(width=1200,height=320,mobile=False):
 title='Human insight. Applied AI. HR transformation by Elle Helvig.'
 if mobile:
  body='''<text x="36" y="49" font-size="12" letter-spacing="2" fill="#b8d0c0">ELLE HELVIG / HR TRANSFORMATION</text><text x="36" y="130" font-size="53" letter-spacing="-2" fill="#fafbf4">Human insight.</text><text x="36" y="199" font-size="57" font-family="Georgia,serif" font-style="italic" letter-spacing="-2" fill="#b7ded0">Applied AI.</text><path d="M36 238H564" stroke="#fafbf430"/><text x="36" y="279" font-size="13" fill="#d0dbcd">WORK REDESIGN · GOVERNANCE · ADOPTION</text>'''
 else:
  body='''<text x="46" y="49" font-size="12" letter-spacing="2.5" fill="#b8d0c0">ELLE HELVIG / HR TRANSFORMATION</text><text x="46" y="132" font-size="64" letter-spacing="-2.5" fill="#fafbf4">Human insight.</text><text x="46" y="211" font-size="70" font-family="Georgia,serif" font-style="italic" letter-spacing="-2.5" fill="#b7ded0">Applied AI.</text><text x="48" y="275" font-size="12" letter-spacing="1.6" fill="#d0dbcd">WORK REDESIGN · GOVERNANCE · ADOPTION</text><g transform="translate(930 161)"><ellipse rx="172" ry="103" transform="rotate(-25)" fill="none" stroke="#789c89"/><ellipse rx="172" ry="103" transform="rotate(35)" fill="none" stroke="#789c89"/><circle r="74" fill="#cddfb1"/><text y="9" text-anchor="middle" font-size="27" letter-spacing="-1" fill="#26352a">People × AI</text><circle cx="-138" cy="-79" r="8" fill="#b7ded0"/><circle cx="133" cy="88" r="7" fill="#b7ded0"/></g>'''
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img"><title>{title}</title><rect width="{width}" height="{height}" rx="22" fill="#253b32"/><g font-family="Arial,Helvetica,sans-serif">{body}</g></svg>\n'

if __name__ == "__main__":
    (ROOT / "assets/profile-modern.svg").write_text(header(), encoding="utf-8")
    (ROOT / "assets/profile-modern-mobile.svg").write_text(header(600, 320, True), encoding="utf-8")
