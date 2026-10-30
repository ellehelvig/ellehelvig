"""Generate self-contained profile SVGs. Run with Python 3 from any directory."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEMES = {
    "dark": dict(bg="#070910", surface="#0d111c", text="#f5f7fb",
                 muted="#a4aec2", violet="#a99fff", cyan="#61ddec",
                 border="#596780", grid="#182132"),
    "light": dict(bg="#f5f7fb", surface="#ffffff", text="#172033",
                  muted="#4b5870", violet="#5140b5", cyan="#086779",
                  border="#73809b", grid="#e3e8f2"),
}


def text(x, y, value, size, color, mono=False, weight=400):
    font = "ui-monospace, SFMono-Regular, Consolas, monospace" if mono else "system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(value)}</text>'


def frame(w, h, title, theme, content):
    t = THEMES[theme]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title, quote=True)}">'
            f'<title>{escape(title)}</title><defs><linearGradient id="accent"><stop stop-color="{t["violet"]}"/><stop offset="1" stop-color="{t["cyan"]}"/></linearGradient>'
            f'<pattern id="grid" width="48" height="48" patternUnits="userSpaceOnUse"><path d="M48 0H0V48" fill="none" stroke="{t["grid"]}"/></pattern></defs>'
            f'<rect width="{w}" height="{h}" rx="16" fill="{t["bg"]}"/>'
            f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="16" fill="url(#grid)"/>'
            f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="16" fill="none" stroke="{t["border"]}"/>'
            f'<rect x="32" y="28" width="80" height="4" rx="2" fill="url(#accent)"/>{content}</svg>\n')


def profile(theme, mobile):
    t = THEMES[theme]
    w, h, x = (720, 480, 40) if mobile else (1280, 440, 64)
    title = "Elle Helvig. HR transformation leader designing responsible AI for people work. Focus: governance, evaluation, and adoption."
    body = text(x, 88, "HR TRANSFORMATION / APPLIED AI", 20, t["violet"], True)
    body += text(x, 181, "Elle Helvig", 66 if mobile else 80, t["text"], weight=650)
    lines = ["Designing responsible AI", "for people work."] if mobile else ["Designing responsible AI for people work."]
    for i, line in enumerate(lines):
        body += text(x, 243 + i*45, line, 36, t["muted"])
    y = 340 if mobile else 314
    for i, (label, width) in enumerate([("GOVERNANCE", 185), ("EVALUATION", 185), ("ADOPTION", 155)]):
        cx = x + i*203
        body += f'<rect x="{cx}" y="{y}" width="{width}" height="44" rx="8" fill="{t["surface"]}" stroke="{t["border"]}"/>'
        body += text(cx+16, y+28, label, 19, t["cyan"], True)
    return frame(w, h, title, theme, body)


CARDS = {
    "playbook": ("01", "FLAGSHIP", ["HR AI Transformation", "Playbook"], "Operating model", "Opportunity to responsible adoption"),
    "resolve": ("02", "LIVE DEMO", ["Resolve"], "Workflow demonstration", "Rules, human review, and clear limits"),
    "portfolio": ("03", "PORTFOLIO", ["Portfolio"], "Case studies", "Design choices and project evidence"),
}


def card(kind, theme, mobile):
    t = THEMES[theme]
    number, tag, lines, category, sub = CARDS[kind]
    w, h, x = (720, 330, 40) if mobile else (1280, 240, 48)
    title = f"{number}. {' '.join(lines)}. {category}. {tag}."
    body = text(x, 79 if mobile else 69, f"{number} / {category.upper()}", 19, t["muted"], True)
    tx = w - 224
    body += f'<rect x="{tx}" y="105" width="176" height="38" rx="8" fill="{t["surface"]}" stroke="{t["border"]}"/>'
    body += text(tx+16, 130, tag, 19, t["cyan"], True)
    # Narrow cards place the tag below all title and description lines.
    if mobile:
        body = text(x, 78, f"{number} / {category.upper()}", 19, t["muted"], True)
        body += f'<rect x="{x}" y="259" width="176" height="38" rx="8" fill="{t["surface"]}" stroke="{t["border"]}"/>'
        body += text(x+16, 284, tag, 19, t["cyan"], True)
    title_lines = lines if mobile else [" ".join(lines)]
    for i, line in enumerate(title_lines):
        body += text(x, (133 if mobile else 133)+i*47, line, 43 if mobile else 48, t["text"], weight=600)
    body += text(x, 230 if mobile else 186, sub, 27, t["violet"])
    return frame(w, h, title, theme, body)


if __name__ == "__main__":
    for theme in THEMES:
        for mobile in [False, True]:
            suffix = f'{"mobile-" if mobile else ""}{theme}'
            (ROOT / "assets" / f"profile-{suffix}.svg").write_text(profile(theme, mobile))
            for kind in CARDS:
                (ROOT / "assets" / f"card-{kind}-{suffix}.svg").write_text(card(kind, theme, mobile))
