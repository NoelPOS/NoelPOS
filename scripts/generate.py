"""Render the profile's terminal cards as animated SVGs, in dark and light.

assets/hello-{dark,light}.svg     a request to /v1/engineers/noel answered as JSON
assets/neofetch-{dark,light}.svg  a dot-matrix portrait beside a neofetch-style panel

Standard library only. Run from the repository root:  python3 scripts/generate.py
The daily workflow runs it so the live numbers stay current.
"""

import datetime as dt
import json
import re
import urllib.request
import zlib
from html import escape
from pathlib import Path

USER = "NoelPOS"
CODING_SINCE = dt.date(2022, 11, 1)  # first semester of the CS degree
ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

FONT = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"
FS = 14          # font size
LH = 21          # line height
PAD = 24         # inner padding
BAR = 40         # title bar height
W = 860          # card width

THEMES = {
    "dark": {
        "bg": "#0d1117", "bar": "#161b22", "border": "#30363d", "text": "#e6edf3",
        "muted": "#8b949e", "prompt": "#7ee787", "key": "#79c0ff", "str": "#a5d6ff",
        "num": "#ffa657", "bool": "#ff7b72", "accent": "#d2a8ff", "dot": "#7ee787",
    },
    "light": {
        "bg": "#ffffff", "bar": "#f6f8fa", "border": "#d0d7de", "text": "#1f2328",
        "muted": "#656d76", "prompt": "#1a7f37", "key": "#0550ae", "str": "#0a3069",
        "num": "#953800", "bool": "#cf222e", "accent": "#8250df", "dot": "#1a7f37",
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
        html = fetch(f"https://github.com/users/{USER}/contributions")
        m = re.search(r"([\d,]+)\s+contributions?\s+in the last year", re.sub(r"\s+", " ", html))
        if m:
            stats["contributions"] = int(m.group(1).replace(",", ""))
    except Exception as exc:  # keep the previous numbers rather than fail the run
        print("contributions:", exc)
    try:
        user = json.loads(fetch(f"https://api.github.com/users/{USER}"))
        stats["repos"] = user["public_repos"]
        stats["followers"] = user["followers"]
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
<style>
/* Visible by default: the animations only hide things while they wait their turn,
   so a viewer that never runs them still gets the finished card. */
.r {{ animation: show 0.01s linear both; }}
.c {{ animation: blink 1.1s step-end infinite; }}
@keyframes show {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
@keyframes blink {{ 0%, 49% {{ opacity: 1; }} 50%, 100% {{ opacity: 0; }} }}
@media (prefers-reduced-motion: reduce) {{ .r, .c, .k {{ animation: none !important; }} }}
</style>
<g font-family="{FONT}" font-size="{FS}" style="white-space:pre">
{body}
</g>
</svg>
"""


def reveal(at):
    """Attributes that keep an element hidden until `at` seconds."""
    return f'class="r" style="animation-delay:{at:.2f}s"'


def typed(x, y, t, prompt, command, start, per_char=0.045):
    """A prompt followed by a command that types itself out; returns (svg, end time).

    CSS only (GitHub plays CSS animations in README images): a block the
    colour of the background sits over the command and steps right one
    character at a time.
    """
    cw = FS * 0.6
    cx = x + len(prompt) * cw
    width = len(command) * cw + 12
    dur = len(command) * per_char
    name = f"type{zlib.crc32(f'{command}{start}'.encode())}"
    svg = (f'<text x="{x}" y="{y}" fill="{t["prompt"]}" xml:space="preserve">{escape(prompt)}</text>'
           f'<text x="{cx:.1f}" y="{y}" fill="{t["text"]}" xml:space="preserve">{escape(command)}</text>'
           f'<style>@keyframes {name} {{ from {{ transform: translateX(0); }} '
           f'to {{ transform: translateX({width:.1f}px); }} }}</style>'
           f'<rect class="k" x="{cx - 1:.1f}" y="{y - FS:.1f}" width="{width:.1f}" height="{FS + 6}" fill="{t["bg"]}" '
           f'style="transform: translateX({width:.1f}px); '
           f'animation: {name} {dur:.2f}s steps({len(command)}) {start:.2f}s both"/>')
    return svg, start + dur


def line(x, y, spans, at):
    inner = "".join(f'<tspan fill="{color}">{escape(text)}</tspan>' for text, color in spans)
    return f'<text x="{x}" y="{y}" {reveal(at)} xml:space="preserve">{inner}</text>'


def cursor(t, x, y, at):
    return (f'<g {reveal(at)}><rect class="c" x="{x:.1f}" y="{y - FS + 2}" width="8" height="{FS + 2}" '
            f'fill="{t["prompt"]}"/></g>')


# ---------------------------------------------------------------- hello card

def hello(t):
    x = PAD
    y = BAR + PAD + 6
    parts = []
    svg, done = typed(x, y, t, "noel@bangkok:~$ ", "curl -i localhost:8080/v1/engineers/noel", 0.6)
    parts.append(svg)

    k, s, n, b, m, tx = t["key"], t["str"], t["num"], t["bool"], t["muted"], t["text"]

    def kv(key, value, color, comma=True):
        return [("  ", tx), (f'"{key}"', k), (": ", tx), (value, color), (("," if comma else ""), tx)]

    def arr(key, items, comma=True):
        out = [("  ", tx), (f'"{key}"', k), (": [", tx)]
        for i, item in enumerate(items):
            out += [(f'"{item}"', s), (", " if i < len(items) - 1 else "", tx)]
        return out + [("]" + ("," if comma else ""), tx)]

    rows = [
        [("HTTP/1.1 ", m), ("200 OK", t["prompt"])],
        [("content-type: ", m), ("application/json", tx)],
        [("x-response-time: ", m), ("350ms", n), ("   ", tx), ("# was 850ms before I tuned it", m)],
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
    at = done + 0.45
    for row in rows:
        y += LH
        if row:
            parts.append(line(x, y, row, at))
        at += 0.07
    y += LH * 1.6
    parts.append(f'<text x="{x}" y="{y}" fill="{t["prompt"]}" {reveal(at + 0.2)} xml:space="preserve">noel@bangkok:~$ </text>')
    parts.append(cursor(t, x + 16 * FS * 0.6 + 2, y, at + 0.2))
    height = int(y + PAD + 4)
    label = ("Terminal: curl -i localhost:8080/v1/engineers/noel returns HTTP 200 with JSON - "
             "name Noel Paing Oak Soe, Software Engineer at EffortX Foundation in Bangkok, focused on backend, "
             "distributed systems, cloud and reliability, currently building VetMiMi, open to work.")
    return window(t, height, "noel@bangkok: ~ - zsh", "\n".join(parts), label)


# ---------------------------------------------------------------- neofetch card

def neofetch(t, stats, today):
    portrait = json.loads((ROOT / "data" / "portrait.json").read_text())
    pitch = 4.2
    px, py = PAD + 6, BAR + PAD + 30
    cmd, done = typed(PAD, BAR + PAD + 6, t, "noel@bangkok:~$ ", "neofetch", 0.4, 0.07)

    # dots appear row by row, like a scan line
    rows = {}
    for x, y in portrait["pts"]:
        rows.setdefault(y, []).append(x)
    dots = []
    for y, xs in sorted(rows.items()):
        circles = "".join(f'<circle cx="{px + x * pitch:.1f}" cy="{py + y * pitch:.1f}" r="1.45"/>' for x in xs)
        dots.append(f'<g {reveal(done + 0.3 + y * 0.018)}>{circles}</g>')
    art_w = portrait["w"] * pitch
    art_h = portrait["h"] * pitch

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
    ix = px + art_w + 44
    iy = py + 6
    at = done + 0.5
    out = []
    for item in info:
        spans = item if isinstance(item, list) else [(item[0], t["accent"]), (": ", t["text"]), (item[1], t["text"])]
        out.append(line(ix, iy, spans, at))
        iy += LH
        at += 0.09
    iy += 8
    blocks = "".join(f'<rect x="{ix + i * 26}" y="{iy - 12}" width="22" height="14" rx="2" fill="{c}"/>'
                     for i, c in enumerate(PALETTE))
    out.append(f'<g {reveal(at)}>{blocks}</g>')

    bottom = max(py + art_h, iy) + 14
    out.append(f'<text x="{PAD}" y="{bottom + LH}" font-size="11" fill="{t["muted"]}" {reveal(at + 0.2)}>'
               f'refreshed {today.isoformat()} by a GitHub Action</text>')
    height = int(bottom + LH + PAD)

    body = (cmd + f'\n<g fill="{t["dot"]}">' + "".join(dots) + "</g>\n" + "\n".join(out))
    label = ("neofetch-style card: dot-matrix portrait of Noel beside system info - Software Engineer at EffortX "
             f"Foundation; TypeScript, Java, Go, C#, Python; NestJS, Spring Boot, ASP.NET Core; PostgreSQL, Redis; "
             f"AWS, Docker, Terraform; {contributions} contributions.")
    return window(t, height, "noel@bangkok: ~ - neofetch", body, label)


def main():
    ASSETS.mkdir(exist_ok=True)
    cache = ROOT / "data" / "stats.json"
    stats = json.loads(cache.read_text()) if cache.exists() else {}
    stats.update(live_stats())
    cache.write_text(json.dumps(stats, indent=2) + "\n")
    today = dt.datetime.now(dt.timezone(dt.timedelta(hours=7))).date()
    for name, theme in THEMES.items():
        (ASSETS / f"hello-{name}.svg").write_text(hello(theme))
        (ASSETS / f"neofetch-{name}.svg").write_text(neofetch(theme, stats, today))
    print("stats:", stats)


if __name__ == "__main__":
    main()
