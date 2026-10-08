"""Render the profile's terminal cards as SVGs, in dark and light.

assets/hello-{dark,light}.svg     a request to /v1/engineers/noel answered as JSON
assets/neofetch-{dark,light}.svg  a halftone portrait beside a neofetch-style panel

The cards are deliberately static: GitHub does not reliably play animations in
README images, and a card stuck on its first frame would show an empty terminal.

Standard library only. Run from the repository root:  python3 scripts/generate.py
The daily workflow runs it so the live numbers stay current.
"""

import datetime as dt
import json
import re
import urllib.request
from html import escape
from pathlib import Path

USER = "NoelPOS"
CODING_SINCE = dt.date(2022, 11, 1)  # first semester of the CS degree
ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

FONT = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"
FS = 14          # font size
CW = FS * 0.6    # approximate monospace character width
LH = 21          # line height
PAD = 24         # inner padding
BAR = 40         # title bar height
W = 860          # card width
PROMPT = "noel@bangkok:~$ "

THEMES = {
    "dark": {
        "bg": "#0d1117", "bar": "#161b22", "border": "#30363d", "text": "#e6edf3",
        "muted": "#8b949e", "prompt": "#7ee787", "key": "#79c0ff", "str": "#a5d6ff",
        "bool": "#ff7b72", "accent": "#d2a8ff", "dot": "#7ee787", "invert": False,
    },
    "light": {
        "bg": "#ffffff", "bar": "#f6f8fa", "border": "#d0d7de", "text": "#1f2328",
        "muted": "#656d76", "prompt": "#1a7f37", "key": "#0550ae", "str": "#0a3069",
        "bool": "#cf222e", "accent": "#8250df", "dot": "#1a7f37", "invert": True,
    },
}
PALETTE = ["#ff7b72", "#ffa657", "#e3b341", "#7ee787", "#56d4dd", "#79c0ff", "#d2a8ff", "#f778ba"]


# ---------------------------------------------------------------- live data

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": f"{USER}-profile"})
    with urllib.request.urlopen(req, timeout=20) as res:
        return res.read().decode()


def live_stats():
    """Public numbers, exactly as a signed-out visitor sees them."""
    stats = {}
    try:
        html = re.sub(r"\s+", " ", fetch(f"https://github.com/users/{USER}/contributions"))
        m = re.search(r"([\d,]+) contributions? in the last year", html)
        if m:
            stats["contributions"] = int(m.group(1).replace(",", ""))
    except Exception as exc:  # keep the previous numbers rather than fail the run
        print("contributions:", exc)
    try:
        user = json.loads(fetch(f"https://api.github.com/users/{USER}"))
        stats["repos"] = user["public_repos"]
    except Exception as exc:
        print("user:", exc)
    return stats


def uptime(today):
    months = (today.year - CODING_SINCE.year) * 12 + today.month - CODING_SINCE.month
    years, months = divmod(months, 12)
    return f"{years} years, {months} months"


# ---------------------------------------------------------------- svg helpers

def window(t, height, title, body, label):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" viewBox="0 0 {W} {height}" role="img" aria-label="{escape(label)}">
<title>{escape(label)}</title>
<rect x="0.5" y="0.5" width="{W - 1}" height="{height - 1}" rx="10" fill="{t['bg']}" stroke="{t['border']}"/>
<path d="M0.5 {BAR} V10.5 a10 10 0 0 1 10 -10 H{W - 10.5} a10 10 0 0 1 10 10 V{BAR} Z" fill="{t['bar']}" stroke="{t['border']}"/>
<circle cx="22" cy="20" r="6" fill="#ff5f57"/><circle cx="42" cy="20" r="6" fill="#febc2e"/><circle cx="62" cy="20" r="6" fill="#28c840"/>
<text x="{W / 2}" y="25" text-anchor="middle" font-family="{FONT}" font-size="12" fill="{t['muted']}">{escape(title)}</text>
<g font-family="{FONT}" font-size="{FS}">
{body}
</g>
</svg>
"""


def line(x, y, spans):
    inner = "".join(f'<tspan fill="{color}">{escape(text)}</tspan>' for text, color in spans)
    return f'<text x="{x:.1f}" y="{y:.1f}" xml:space="preserve">{inner}</text>'


def prompt(t, x, y, command="", cursor=False):
    out = line(x, y, [(PROMPT, t["prompt"]), (command, t["text"])])
    if cursor:
        out += (f'<rect x="{x + len(PROMPT) * CW + 1:.1f}" y="{y - FS + 2}" width="8" height="{FS + 2}" '
                f'fill="{t["prompt"]}"/>')
    return out


# ---------------------------------------------------------------- hello card

def hello(t):
    x, y = PAD, BAR + PAD + 6
    k, s, b, tx = t["key"], t["str"], t["bool"], t["text"]

    def kv(key, value, color, comma=True):
        return [("  ", tx), (f'"{key}"', k), (": ", tx), (value, color), ("," if comma else "", tx)]

    def arr(key, items):
        out = [("  ", tx), (f'"{key}"', k), (": [", tx)]
        for i, item in enumerate(items):
            out += [(f'"{item}"', s), (", " if i < len(items) - 1 else "", tx)]
        return out + [("],", tx)]

    rows = [
        [("HTTP/1.1 ", t["muted"]), ("200 OK", t["prompt"])],
        [("content-type: ", t["muted"]), ("application/json", tx)],
        [],
        [("{", tx)],
        kv("name", '"Noel Paing Oak Soe"', s),
        kv("role", '"Software Engineer"', s),
        kv("company", '"EffortX Foundation"', s),
        kv("based_in", '"Bangkok, Thailand"', s),
        arr("focus", ["backend", "distributed systems", "cloud", "reliability"]),
        kv("currently_building", '"VetMiMi: booking + WebRTC video in Go"', s),
        kv("education", '"B.Sc. Computer Science, GPA 3.88"', s),
        kv("open_to_work", "true", b, comma=False),
        [("}", tx)],
    ]
    parts = [prompt(t, x, y, "curl -i localhost:8080/v1/engineers/noel")]
    for row in rows:
        y += LH
        if row:
            parts.append(line(x, y, row))
    y += LH * 1.6
    parts.append(prompt(t, x, y, cursor=True))
    label = ("Terminal: curl -i localhost:8080/v1/engineers/noel returns HTTP 200 with JSON - "
             "name Noel Paing Oak Soe, Software Engineer at EffortX Foundation in Bangkok, focused on backend, "
             "distributed systems, cloud and reliability, currently building VetMiMi, open to work.")
    return window(t, int(y + PAD + 4), "noel@bangkok: ~ - zsh", "\n".join(parts), label)


# ---------------------------------------------------------------- neofetch card

def halftone(t, x0, y0, pitch):
    """Dots whose size follows the photo's brightness; light mode prints dark on white."""
    portrait = json.loads((ROOT / "data" / "portrait.json").read_text())
    dots = []
    for x, y, v in portrait["cells"]:
        tone = 1 - v if t["invert"] else v
        r = 0.3 + tone * pitch * 0.56
        dots.append(f'<circle cx="{x0 + (x + 0.5) * pitch:.1f}" cy="{y0 + (y + 0.5) * pitch:.1f}" r="{r:.2f}"/>')
    svg = f'<g fill="{t["dot"]}">' + "".join(dots) + "</g>"
    return svg, portrait["cols"] * pitch, portrait["rows"] * pitch


def neofetch(t, stats, today):
    top = BAR + PAD + 6
    pitch = 4.8
    art, art_w, art_h = halftone(t, PAD, top + 14, pitch)

    contributions = f'{stats["contributions"]:,} in the last year' if "contributions" in stats else "-"
    info = [
        [("noel", t["prompt"]), ("@", t["text"]), ("github", t["prompt"])],
        [("-" * 15, t["muted"])],
        ("Role", "Software Engineer (backend)"),
        ("Company", "EffortX Foundation"),
        ("Uptime", uptime(today) + " of writing code"),
        ("Languages", "TypeScript, Java, Go, C#, Python"),
        ("Backend", "NestJS, Spring Boot, ASP.NET Core"),
        ("Frontend", "React, Next.js, React Native"),
        ("Data", "PostgreSQL, Redis, MongoDB, RabbitMQ"),
        ("Cloud", "AWS, Docker, Terraform, GitHub Actions"),
        ("Testing", "Playwright, Testcontainers, JUnit"),
        ("Contributions", contributions),
        ("Public repos", str(stats.get("repos", "-"))),
        ("Location", "Bangkok, TH (UTC+7)"),
    ]
    ix = PAD + art_w + 40
    iy = top + 14 + (art_h - (len(info) * LH + 22)) / 2 + FS  # centre the panel beside the portrait
    out = []
    for item in info:
        spans = item if isinstance(item, list) else [(item[0], t["accent"]), (": ", t["text"]), (item[1], t["text"])]
        out.append(line(ix, iy, spans))
        iy += LH
    out.append("".join(f'<rect x="{ix + i * 26:.1f}" y="{iy - 8:.1f}" width="22" height="14" rx="2" fill="{c}"/>'
                       for i, c in enumerate(PALETTE)))

    bottom = max(top + 14 + art_h, iy + 10) + 10
    out.append(f'<text x="{PAD}" y="{bottom + 14:.1f}" font-size="11" fill="{t["muted"]}">'
               f'refreshed {today.isoformat()} by a GitHub Action</text>')
    body = prompt(t, PAD, top, "neofetch") + "\n" + art + "\n" + "\n".join(out)
    label = ("neofetch-style card: halftone portrait of Noel beside system info - Software Engineer at EffortX "
             "Foundation; TypeScript, Java, Go, C#, Python; NestJS, Spring Boot, ASP.NET Core; PostgreSQL, Redis; "
             f"AWS, Docker, Terraform; {contributions} contributions.")
    return window(t, int(bottom + 14 + PAD), "noel@bangkok: ~ - neofetch", body, label)


def main():
    ASSETS.mkdir(exist_ok=True)
    cache = ROOT / "data" / "stats.json"
    stats = json.loads(cache.read_text()) if cache.exists() else {}
    stats.update(live_stats())
    stats.pop("followers", None)
    cache.write_text(json.dumps(stats, indent=2) + "\n")
    today = dt.datetime.now(dt.timezone(dt.timedelta(hours=7))).date()
    for name, theme in THEMES.items():
        (ASSETS / f"hello-{name}.svg").write_text(hello(theme))
        (ASSETS / f"neofetch-{name}.svg").write_text(neofetch(theme, stats, today))
    print("stats:", stats)


if __name__ == "__main__":
    main()
