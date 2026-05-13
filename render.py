#!/usr/bin/env python3
"""
Next Maven Carousel Renderer — v2 (Editorial Dark/Light Theme System)

Per-slide theme switching:
  - "theme": "dark"  → Dark Purple bg + White text + Aquamarine accents (NM signature)
  - "theme": "light" → Cream bg + Dark Purple text + Aquamarine highlights
  - If "theme" missing: hook/cta default to dark, body defaults to light.

Fonts:
  - English headlines: LEXEND DECA (brand primary)
  - English body:      Inter (brand secondary)
  - Chinese (zh):      寒蝉端黑体 / ChillDuanSans
  - Code blocks:       Consolas (system mono)
"""
import json, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# ── Canvas ────────────────────────────────────────────────────────────────────
W, H    = 1080, 1350          # Instagram 4:5 portrait
PAD     = 96                  # was 72 — new spec is airier
TOP_H   = 80
BOT_H   = 80
C_TOP   = TOP_H + 28
C_BOT   = H - BOT_H - 24
C_W     = W - PAD * 2
C_H     = C_BOT - C_TOP
CR      = 20                  # card corner radius
CPX     = 40                  # card padding x
CPY     = 32                  # card padding y

# ── Fonts ─────────────────────────────────────────────────────────────────────
FONT_DIR = Path(__file__).parent / "assets" / "fonts"
MONO_DIR = Path("C:/Windows/Fonts")

def _pick(*candidates):
    """Return the first font path that exists, else the last candidate."""
    for p in candidates:
        if Path(p).exists():
            return str(p)
    return str(candidates[-1])

# Headlines & labels → LEXEND DECA (brand primary); fall back to ChillDuanSans_Heavy
LEXEND_B  = _pick(FONT_DIR / "LexendDeca-Bold.ttf",
                  FONT_DIR / "LexendDeca-Bold.otf",
                  FONT_DIR / "ChillDuanSans_Heavy.otf")
LEXEND_SB = _pick(FONT_DIR / "LexendDeca-SemiBold.ttf",
                  FONT_DIR / "LexendDeca-SemiBold.otf",
                  FONT_DIR / "ChillDuanSans_Heavy.otf")
LEXEND_M  = _pick(FONT_DIR / "LexendDeca-Medium.ttf",
                  FONT_DIR / "LexendDeca-Medium.otf",
                  FONT_DIR / "ChillDuanSans_Medium.otf")

# Body & UI → Inter (brand secondary); fall back to ChillDuanSans
INTER_R   = _pick(FONT_DIR / "Inter-Regular.ttf",
                  FONT_DIR / "Inter-Regular.otf",
                  FONT_DIR / "ChillDuanSans_Regular.otf")
INTER_M   = _pick(FONT_DIR / "Inter-Medium.ttf",
                  FONT_DIR / "Inter-Medium.otf",
                  FONT_DIR / "ChillDuanSans_Medium.otf")
INTER_SB  = _pick(FONT_DIR / "Inter-SemiBold.ttf",
                  FONT_DIR / "Inter-SemiBold.otf",
                  FONT_DIR / "ChillDuanSans_Heavy.otf")

# Chinese
ZH_HEAVY  = _pick(FONT_DIR / "ChillDuanSans_Heavy.otf")
ZH_MED    = _pick(FONT_DIR / "ChillDuanSans_Medium.otf")
ZH_REG    = _pick(FONT_DIR / "ChillDuanSans_Regular.otf")
ZH_LIGHT  = _pick(FONT_DIR / "ChillDuanSans_Light.otf")

# Mono (code blocks)
MONO_R = _pick(MONO_DIR / "consola.ttf",  FONT_DIR / "ChillDuanSans_Regular.otf")
MONO_B = _pick(MONO_DIR / "consolab.ttf", FONT_DIR / "ChillDuanSans_Heavy.otf")

def _f(path, size):
    return ImageFont.truetype(path, size)

def load_fonts(lang="en"):
    """Return a font dict keyed by role. English uses Lexend+Inter; ZH uses ChillDuan."""
    if lang == "zh":
        return {
            "topbar":      _f(ZH_HEAVY, 26),
            "counter":     _f(INTER_M,  26),   # numbers always in Inter
            "label":       _f(ZH_HEAVY, 26),
            "headline_xl": _f(ZH_HEAVY, 88),
            "headline_lg": _f(ZH_HEAVY, 72),
            "headline_md": _f(ZH_HEAVY, 58),
            "headline_sm": _f(ZH_HEAVY, 48),
            "body_lg":     _f(ZH_MED,   40),
            "body":        _f(ZH_REG,   36),
            "body_sm":     _f(ZH_REG,   30),
            "body_bold":   _f(ZH_HEAVY, 36),
            "card_label":  _f(ZH_HEAVY, 24),
            "card_body":   _f(ZH_REG,   34),
            "code":        _f(MONO_R,   30),
            "code_kw":     _f(MONO_B,   30),
            "caption":     _f(ZH_LIGHT, 24),
            "pill":        _f(ZH_MED,   27),
        }
    # English
    return {
        "topbar":      _f(LEXEND_M,  26),
        "counter":     _f(INTER_M,   26),
        "label":       _f(LEXEND_M,  26),
        "headline_xl": _f(LEXEND_B,  96),     # was 88
        "headline_lg": _f(LEXEND_B,  76),     # was 72
        "headline_md": _f(LEXEND_B,  58),
        "headline_sm": _f(LEXEND_SB, 46),
        "body_lg":     _f(INTER_R,   38),
        "body":        _f(INTER_R,   34),
        "body_sm":     _f(INTER_R,   28),
        "body_bold":   _f(INTER_SB,  34),
        "card_label":  _f(LEXEND_M,  22),
        "card_body":   _f(INTER_R,   32),
        "code":        _f(MONO_R,    28),
        "code_kw":     _f(MONO_B,    28),
        "caption":     _f(INTER_M,   24),
        "pill":        _f(INTER_M,   26),
    }

# ── Theme system ──────────────────────────────────────────────────────────────
THEMES = {
    "dark": {
        "bg":             "#2D1E2F",    # Dark Purple
        "headline":       "#FFFFFF",
        "body":           "#E0F5F1",    # Light Green (soft, not pure white)
        "label":          "#A7FAFF",    # Aquamarine
        "divider":        "#A7FAFF",
        "muted":          "#8A8E9C",
        "hairline":       "#FFFFFF",    # used at low alpha
        "hairline_a":     38,           # 15% alpha
        # highlights
        "accent_hi_bg":   "#A7FAFF",
        "accent_hi_fg":   "#2D1E2F",
        # pills
        "pill_bg":        "#3D2E3F",
        "pill_border":    "#A7FAFF",
        "pill_border_a":  90,           # ~35%
        "pill_fg":        "#FFFFFF",
        "pill_active_bg": "#A7FAFF",
        "pill_active_fg": "#2D1E2F",
        # cards (callout on dark = translucent aqua)
        "card_bg":        "#A7FAFF",
        "card_bg_a":      30,           # 12% alpha
        "card_border":    "#A7FAFF",
        "card_label":     "#A7FAFF",
        "card_text":      "#FFFFFF",
        # comparison
        "cmp_old_bg":     "#FF899F",
        "cmp_old_bg_a":   48,           # ~20%
        "cmp_old_label":  "#FF899F",
        "cmp_new_bg":     "#8AFFE9",
        "cmp_new_bg_a":   38,           # ~15%
        "cmp_new_label":  "#8AFFE9",
        # images
        "img_border":     "#FFFFFF",
        "img_border_a":   51,           # 20%
    },
    "light": {
        "bg":             "#F5EFE6",    # Cream
        "headline":       "#2D1E2F",
        "body":           "#454252",    # Grey (official brand grey)
        "label":          "#00635D",    # Dark Green
        "divider":        "#6ABAAB",    # Forest Green
        "muted":          "#8A8076",
        "hairline":       "#2D1E2F",
        "hairline_a":     26,           # 10% alpha
        # highlights
        "accent_hi_bg":   "#A7FAFF",
        "accent_hi_fg":   "#2D1E2F",
        # pills
        "pill_bg":        "#FFFFFF",
        "pill_border":    "#2D1E2F",
        "pill_border_a":  255,
        "pill_fg":        "#2D1E2F",
        "pill_active_bg": "#A7FAFF",
        "pill_active_fg": "#2D1E2F",
        # cards (callout on light = solid dark purple)
        "card_bg":        "#2D1E2F",
        "card_bg_a":      255,
        "card_border":    None,
        "card_label":     "#A7FAFF",
        "card_text":      "#FFFFFF",
        # comparison
        "cmp_old_bg":     "#FAE8E8",
        "cmp_old_bg_a":   255,
        "cmp_old_label":  "#FF899F",
        "cmp_new_bg":     "#E0F5F1",
        "cmp_new_bg_a":   255,
        "cmp_new_label":  "#00635D",
        # images
        "img_border":     "#2D1E2F",
        "img_border_a":   26,           # 10%
    },
}

# Theme-agnostic constants (same on both themes)
C_CODE_BG    = "#1E1318"
C_CODE_KW    = "#A7FAFF"
C_CODE_TEXT  = "#C0B8B0"
C_TRAFFIC    = ["#FF5F57", "#FFBD2E", "#28C940"]
C_ACCENT     = "#A7FAFF"
C_ACCENT_PNK = "#FF899F"
C_ACCENT_GRN = "#6ABAAB"

def get_palette(slide: dict) -> dict:
    """Return the palette for a slide based on its 'theme' field.

    Defaults: hook + cta → dark, body → light.
    """
    if "theme" in slide and slide["theme"] in THEMES:
        return THEMES[slide["theme"]]
    if slide.get("type") in ("hook", "cta"):
        return THEMES["dark"]
    return THEMES["light"]

# ── Color helpers ─────────────────────────────────────────────────────────────
def rgb(hex_c):
    h = hex_c.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def rgba(hex_c, a=255):
    return rgb(hex_c) + (a,)

# ── Text helpers ──────────────────────────────────────────────────────────────
def wrap(text, font, max_w, draw):
    lines = []
    for para in text.split("\n"):
        words = para.split()
        if not words:
            lines.append(""); continue
        cur = []
        for w in words:
            test = " ".join(cur + [w])
            if draw.textbbox((0, 0), test, font=font)[2] <= max_w:
                cur.append(w)
            else:
                if cur: lines.append(" ".join(cur))
                cur = [w]
        if cur: lines.append(" ".join(cur))
    return lines

def lh(font, draw, sp=1.45):
    bb = draw.textbbox((0, 0), "Ag", font=font)
    return int((bb[3] - bb[1]) * sp)

def th(text, font, max_w, draw, sp=1.45):
    return lh(font, draw, sp) * len(wrap(text, font, max_w, draw))

def draw_plain(draw, text, xy, font, color, max_w, sp=1.45, align="left"):
    x, y = xy
    lines = wrap(text, font, max_w, draw)
    lhv = lh(font, draw, sp)
    for ln in lines:
        if align == "center":
            lw = draw.textbbox((0, 0), ln, font=font)[2]
            draw.text((x + (max_w - lw) // 2, y), ln, font=font, fill=rgb(color))
        else:
            draw.text((x, y), ln, font=font, fill=rgb(color))
        y += lhv
    return y

def draw_rich(draw, text, xy, font, def_c, acc_c, max_w,
              sp=1.3, acc_bg=None, acc_fg=None):
    """Draw text with *accent* words. If acc_bg given: filled pill behind word.
    acc_fg = text color ON the accent pill (falls back to def_c)."""
    x, y = xy
    parts = text.split("*")
    words = []
    for i, p in enumerate(parts):
        for w in p.split():
            words.append((w, i % 2 == 1))

    lines, cur = [], []
    for word, acc in words:
        test = " ".join(w for w, _ in cur) + (" " if cur else "") + word
        if draw.textbbox((0, 0), test, font=font)[2] <= max_w:
            cur.append((word, acc))
        else:
            if cur: lines.append(cur)
            cur = [(word, acc)]
    if cur: lines.append(cur)

    lhv = lh(font, draw, sp)
    for ln in lines:
        dx = x
        for word, acc in ln:
            wbb = draw.textbbox((dx, y), word, font=font)
            if acc:
                if acc_bg:
                    # Rounded pill highlight behind word
                    pad_x, pad_y = 6, 3
                    draw.rounded_rectangle(
                        [(wbb[0] - pad_x, wbb[1] - pad_y),
                         (wbb[2] + pad_x, wbb[3] + pad_y)],
                        radius=8, fill=rgb(acc_bg))
                    fg = acc_fg if acc_fg else def_c
                    draw.text((dx, y), word, font=font, fill=rgb(fg))
                else:
                    draw.text((dx, y), word, font=font, fill=rgb(acc_c))
            else:
                draw.text((dx, y), word, font=font, fill=rgb(def_c))
            dx += draw.textbbox((0, 0), word + " ", font=font)[2]
        y += lhv
    return y

# ── Chrome (top/bottom bars) ──────────────────────────────────────────────────
def _hairline(draw, p, x1, y, x2):
    """Thin horizontal separator using palette hairline color + alpha."""
    # Pillow doesn't alpha-blend line() on RGB; simulate by lightening
    # Use an overlay approach via a temporary RGBA buffer would be heavy;
    # just pick a solid color approximating the blend.
    base = rgb(p["bg"])
    hc   = rgb(p["hairline"])
    a    = p["hairline_a"] / 255
    blend = tuple(int(base[i] * (1 - a) + hc[i] * a) for i in range(3))
    draw.line([(x1, y), (x2, y)], fill=blend, width=1)

def draw_top_bar(draw, fonts, palette, brand, num, total):
    p = palette
    brand_str   = brand.upper()
    counter_str = f"{num:02d} / {total:02d}"
    draw.text((PAD, 26), brand_str, font=fonts["topbar"], fill=rgb(p["headline"]))
    cw = draw.textbbox((0, 0), counter_str, font=fonts["counter"])[2]
    draw.text((W - PAD - cw, 26), counter_str,
              font=fonts["counter"], fill=rgb(p["muted"]))
    _hairline(draw, p, PAD, TOP_H + 4, W - PAD)

def draw_bot_bar(draw, fonts, palette, num, total, lang="en"):
    p     = palette
    swipe = "SWIPE →" if lang == "en" else "左滑 →"
    page  = f"{num:02d} / {total:02d}"
    by    = H - BOT_H
    _hairline(draw, p, PAD, by - 4, W - PAD)
    draw.text((PAD, by + 26), swipe, font=fonts["caption"], fill=rgb(p["label"]))
    pw = draw.textbbox((0, 0), page, font=fonts["caption"])[2]
    draw.text((W - PAD - pw, by + 26), page,
              font=fonts["caption"], fill=rgb(p["muted"]))

def draw_label(draw, fonts, palette, text, y):
    """Small-caps category label with accent dot trio beneath."""
    p = palette
    draw.text((PAD, y), text.upper(), font=fonts["label"], fill=rgb(p["label"]))
    bb = draw.textbbox((PAD, y), text.upper(), font=fonts["label"])
    # three small accent dots — editorial signature
    dot_y = bb[3] + 14
    for i in range(3):
        cx = PAD + i * 18
        draw.ellipse([(cx, dot_y), (cx + 7, dot_y + 7)], fill=rgb(p["label"]))
    return dot_y + 7 + 14

def draw_divider(draw, palette, y):
    """Solid accent bar — 80×6, not a thin line."""
    p = palette
    draw.rounded_rectangle([(PAD, y + 8), (PAD + 80, y + 14)],
                           radius=3, fill=rgb(p["divider"]))
    return y + 32

def base_slide(palette):
    return Image.new("RGB", (W, H), rgb(palette["bg"]))

# ── Content blocks ────────────────────────────────────────────────────────────
def block_callout_card(img, draw, fonts, palette, x, y, w, text, label=None):
    """Dark purple callout on light / translucent aqua callout on dark."""
    p   = palette
    tmp = ImageDraw.Draw(img)
    lbl_h = 0
    if label:
        bb = tmp.textbbox((0, 0), label.upper(), font=fonts["card_label"])
        lbl_h = (bb[3] - bb[1]) + 16
    body_h = th(text, fonts["card_body"], w - CPX * 2, tmp, 1.5)
    total  = lbl_h + body_h + CPY * 2

    # Background (with alpha if needed)
    if p["card_bg_a"] < 255:
        overlay = Image.new("RGBA", (w, total), (0, 0, 0, 0))
        od = ImageDraw.Draw(overlay)
        od.rounded_rectangle([(0, 0), (w, total)], radius=CR,
                             fill=rgba(p["card_bg"], p["card_bg_a"]))
        img.paste(overlay, (x, y), overlay)
    else:
        draw.rounded_rectangle([(x, y), (x + w, y + total)],
                               radius=CR, fill=rgb(p["card_bg"]))
    # Border (dark theme only)
    if p["card_border"]:
        draw.rounded_rectangle([(x, y), (x + w, y + total)],
                               radius=CR, outline=rgb(p["card_border"]), width=2)

    cy = y + CPY
    if label:
        draw.text((x + CPX, cy), label.upper(),
                  font=fonts["card_label"], fill=rgb(p["card_label"]))
        bb = draw.textbbox((0, 0), label.upper(), font=fonts["card_label"])
        cy += (bb[3] - bb[1]) + 16
    draw_plain(draw, text, (x + CPX, cy), fonts["card_body"],
               p["card_text"], w - CPX * 2, sp=1.5)
    return y + total

def block_comparison_card(img, draw, fonts, palette, x, y, w, text,
                          label, label_c, bg_c, bg_a, side_c):
    p   = palette
    tmp = ImageDraw.Draw(img)
    bb  = tmp.textbbox((0, 0), label.upper(), font=fonts["card_label"])
    lbl_h = (bb[3] - bb[1]) + 16
    body_h = th(text, fonts["card_body"], w - CPX * 2, tmp, 1.5)
    total  = lbl_h + body_h + CPY * 2

    if bg_a < 255:
        overlay = Image.new("RGBA", (w, total), (0, 0, 0, 0))
        ImageDraw.Draw(overlay).rounded_rectangle(
            [(0, 0), (w, total)], radius=CR, fill=rgba(bg_c, bg_a))
        img.paste(overlay, (x, y), overlay)
    else:
        draw.rounded_rectangle([(x, y), (x + w, y + total)],
                               radius=CR, fill=rgb(bg_c))
    # Side accent bar
    draw.rounded_rectangle([(x, y + 12), (x + 5, y + total - 12)],
                           radius=3, fill=rgb(side_c))

    cy = y + CPY
    draw.text((x + CPX, cy), label.upper(),
              font=fonts["card_label"], fill=rgb(label_c))
    cy += lbl_h
    # Body text uses palette body color for readability in either theme
    draw_plain(draw, text, (x + CPX, cy), fonts["card_body"],
               p["body"], w - CPX * 2, sp=1.5)
    return y + total

def block_code(img, draw, fonts, x, y, w, lines):
    """macOS-style dark code block — identical on both themes."""
    tmp = ImageDraw.Draw(img)
    lhv   = lh(fonts["code"], tmp, 1.7)
    hdr_h = 52
    body_h = len(lines) * lhv + CPY
    total = hdr_h + body_h + CPY

    draw.rounded_rectangle([(x, y), (x + w, y + total)],
                           radius=CR, fill=rgb(C_CODE_BG))
    # Traffic lights
    dy = y + hdr_h // 2 - 6
    for di, dc in enumerate(C_TRAFFIC):
        draw.ellipse([(x + CPX + di * 22, dy),
                      (x + CPX + di * 22 + 12, dy + 12)], fill=rgb(dc))
    # Code
    cy = y + hdr_h + CPY // 2
    for (kw, rest) in lines:
        kw_w = draw.textbbox((0, 0), kw + "  ", font=fonts["code_kw"])[2]
        draw.text((x + CPX, cy), kw, font=fonts["code_kw"], fill=rgb(C_CODE_KW))
        draw.text((x + CPX + kw_w, cy), rest,
                  font=fonts["code"], fill=rgb(C_CODE_TEXT))
        cy += lhv
    return y + total

def block_pills(img, draw, fonts, palette, x, y, tags, active_idx=None):
    """Tool pill tags. Styles switch per theme."""
    p = palette
    ph, ppx, gap = 56, 32, 14
    px, row_y = x, y
    for i, tag in enumerate(tags):
        tw = draw.textbbox((0, 0), tag, font=fonts["pill"])[2]
        pw = tw + ppx * 2
        if px + pw > W - PAD:
            px = x; row_y += ph + 12
        is_act = (active_idx is not None and i == active_idx)
        if is_act:
            draw.rounded_rectangle([(px, row_y), (px + pw, row_y + ph)],
                                   radius=ph // 2, fill=rgb(p["pill_active_bg"]))
            fg = p["pill_active_fg"]
        else:
            draw.rounded_rectangle([(px, row_y), (px + pw, row_y + ph)],
                                   radius=ph // 2, fill=rgb(p["pill_bg"]))
            # Border — approximate alpha by blending with bg
            border_col = rgb(p["pill_border"])
            if p["pill_border_a"] < 255:
                bgc = rgb(p["pill_bg"])
                a = p["pill_border_a"] / 255
                border_col = tuple(int(bgc[j] * (1-a) + border_col[j] * a)
                                   for j in range(3))
            draw.rounded_rectangle([(px, row_y), (px + pw, row_y + ph)],
                                   radius=ph // 2, outline=border_col, width=2)
            fg = p["pill_fg"]
        tb = draw.textbbox((0, 0), tag, font=fonts["pill"])
        t_h = tb[3] - tb[1]
        draw.text((px + ppx, row_y + (ph - t_h) // 2 - tb[1]),
                  tag, font=fonts["pill"], fill=rgb(fg))
        px += pw + gap
    return row_y + ph + 10

def block_bullets(draw, fonts, palette, x, y, bullets, max_w):
    p = palette
    for bullet in bullets:
        dot_y = y + 16
        draw.ellipse([(x, dot_y), (x + 11, dot_y + 11)], fill=rgb(p["divider"]))
        ey = draw_rich(draw, bullet, (x + 32, y), fonts["body"],
                       p["body"], p["divider"], max_w - 32, sp=1.45,
                       acc_bg=p["accent_hi_bg"], acc_fg=p["accent_hi_fg"])
        y = ey + 18
    return y

def block_hero_image(img, draw, palette, image_path, x, y, max_w, max_h):
    """Full-width image with soft gradient overlay at bottom for text legibility."""
    p = palette
    try:
        ref = Image.open(str(image_path)).convert("RGBA")
        # Fill width, crop height
        ratio = max_w / ref.width
        nw = max_w
        nh = min(int(ref.height * ratio), max_h)
        ref = ref.resize((nw, int(ref.height * ratio)), Image.LANCZOS)
        # Center-crop vertically if too tall
        if ref.height > nh:
            top = (ref.height - nh) // 2
            ref = ref.crop((0, top, nw, top + nh))
        # Rounded mask
        mask = Image.new("L", (nw, nh), 0)
        ImageDraw.Draw(mask).rounded_rectangle([(0, 0), (nw, nh)],
                                                radius=CR, fill=255)
        out = Image.new("RGBA", (nw, nh), (0, 0, 0, 0))
        out.paste(ref, (0, 0), mask)
        # Gradient overlay — darken bottom 40% for text over-layability
        overlay = Image.new("RGBA", (nw, nh), (0, 0, 0, 0))
        od = ImageDraw.Draw(overlay)
        bg_rgb = rgb(p["bg"])
        for row in range(int(nh * 0.6), nh):
            t_ = (row - nh * 0.6) / (nh * 0.4)
            a = int(180 * t_)
            od.line([(0, row), (nw, row)], fill=bg_rgb + (a,))
        overlay_mask = Image.new("L", (nw, nh), 0)
        ImageDraw.Draw(overlay_mask).rounded_rectangle(
            [(0, 0), (nw, nh)], radius=CR, fill=255)
        out = Image.alpha_composite(out, overlay)
        img.paste(out.convert("RGB"), (x, y), out)
        # Border
        border = Image.new("RGBA", (nw, nh), (0, 0, 0, 0))
        ImageDraw.Draw(border).rounded_rectangle(
            [(0, 0), (nw, nh)], radius=CR,
            outline=rgba(p["img_border"], p["img_border_a"]), width=2)
        img.paste(border, (x, y), border)
        return y + nh + 20
    except Exception as e:
        print(f"  Hero image error: {e}")
        return y

def block_image(img, draw, palette, image_path, x, y, max_w, max_h):
    """Inline image — fit within max_w × max_h, centered, rounded corners."""
    p = palette
    try:
        ref = Image.open(str(image_path)).convert("RGBA")
        scale = min(max_w / ref.width, max_h / ref.height)
        nw, nh = int(ref.width * scale), int(ref.height * scale)
        ref = ref.resize((nw, nh), Image.LANCZOS)
        ox = x + (max_w - nw) // 2
        mask = Image.new("L", (nw, nh), 0)
        ImageDraw.Draw(mask).rounded_rectangle([(0, 0), (nw, nh)], radius=CR, fill=255)
        out = Image.new("RGBA", (nw, nh), (0, 0, 0, 0))
        out.paste(ref, (0, 0), mask)
        img.paste(out.convert("RGB"), (ox, y), out)
        border = Image.new("RGBA", (nw, nh), (0, 0, 0, 0))
        ImageDraw.Draw(border).rounded_rectangle(
            [(0, 0), (nw, nh)], radius=CR,
            outline=rgba(p["img_border"], p["img_border_a"]), width=2)
        img.paste(border, (ox, y), border)
        return y + nh + 20
    except Exception as e:
        print(f"  Image error: {e}")
        return y

def block_logo_row(img, draw, palette, image_paths, x, y, max_w, box_size=140):
    """Row of small square logo tiles — ideal for tool-comparison slides."""
    p = palette
    n = len(image_paths)
    if n == 0: return y
    gap = 24
    total_w = n * box_size + (n - 1) * gap
    start_x = x + (max_w - total_w) // 2
    for i, ip in enumerate(image_paths):
        bx = start_x + i * (box_size + gap)
        # White tile background for logo visibility on either theme
        draw.rounded_rectangle([(bx, y), (bx + box_size, y + box_size)],
                               radius=18, fill=rgb("#FFFFFF"))
        try:
            logo = Image.open(str(ip)).convert("RGBA")
            pad = 20
            inner = box_size - pad * 2
            ratio = min(inner / logo.width, inner / logo.height)
            lw, lh_ = int(logo.width * ratio), int(logo.height * ratio)
            logo = logo.resize((lw, lh_), Image.LANCZOS)
            lx = bx + (box_size - lw) // 2
            ly = y + (box_size - lh_) // 2
            img.paste(logo, (lx, ly), logo)
        except Exception as e:
            print(f"  Logo error {ip}: {e}")
    return y + box_size + 20

def block_split_images(img, draw, palette, left_path, right_path,
                       x, y, max_w, max_h=420, labels=None):
    """Two side-by-side images for before/after comparisons."""
    p = palette
    gap = 16
    each_w = (max_w - gap) // 2
    for i, ip in enumerate([left_path, right_path]):
        bx = x + i * (each_w + gap)
        try:
            ref = Image.open(str(ip)).convert("RGBA")
            ratio = min(each_w / ref.width, max_h / ref.height)
            nw, nh = int(ref.width * ratio), int(ref.height * ratio)
            ref = ref.resize((nw, nh), Image.LANCZOS)
            mask = Image.new("L", (nw, nh), 0)
            ImageDraw.Draw(mask).rounded_rectangle(
                [(0, 0), (nw, nh)], radius=CR, fill=255)
            out = Image.new("RGBA", (nw, nh), (0, 0, 0, 0))
            out.paste(ref, (0, 0), mask)
            px_ = bx + (each_w - nw) // 2
            img.paste(out.convert("RGB"), (px_, y), out)
            if labels and i < len(labels):
                draw.text((px_, y + nh + 8), labels[i].upper(),
                          fill=rgb(p["label"]))
        except Exception as e:
            print(f"  Split image error: {e}")
    return y + max_h + 40

# ── Slide renderers ───────────────────────────────────────────────────────────
def render_hook(config, slide, fonts, cdir):
    p    = get_palette(slide)
    img  = base_slide(p)
    draw = ImageDraw.Draw(img)
    lang = config.get("language", "en")
    n, t = slide["number"], config["total_slides"]
    brand = config["profile"]["display_name"]

    draw_top_bar(draw, fonts, p, brand, n, t)
    draw_bot_bar(draw, fonts, p, n, t, lang)

    y = C_TOP + 16
    if slide.get("label"):
        y = draw_label(draw, fonts, p, slide["label"], y) + 6

    hook  = slide["text"].rstrip(".")
    clean = hook.replace("*", "")
    hfont = fonts["headline_xl"] if len(clean) < 50 else fonts["headline_lg"]
    y = draw_rich(draw, hook, (PAD, y), hfont,
                  p["headline"], p["divider"], C_W, sp=1.12,
                  acc_bg=p["accent_hi_bg"], acc_fg=p["accent_hi_fg"])
    y = draw_divider(draw, p, y)

    if slide.get("subtitle"):
        y = draw_plain(draw, slide["subtitle"], (PAD, y + 8),
                       fonts["body_lg"], p["body"], C_W, sp=1.5) + 20

    if slide.get("pills"):
        y += 12
        y = block_pills(img, draw, fonts, p, PAD, y,
                        slide["pills"], slide.get("pills_active"))
    elif slide.get("image"):
        ip = cdir / "reference" / slide["image"]
        if ip.exists():
            y += 12
            layout = slide.get("image_layout", "inline")
            if layout == "hero":
                block_hero_image(img, draw, p, ip, PAD, y, C_W, max_h=480)
            else:
                block_image(img, draw, p, ip, PAD, y, C_W, max_h=380)
    return img

def render_body(config, slide, fonts, cdir):
    p    = get_palette(slide)
    img  = base_slide(p)
    draw = ImageDraw.Draw(img)
    lang = config.get("language", "en")
    n, t = slide["number"], config["total_slides"]
    brand = config["profile"]["display_name"]

    draw_top_bar(draw, fonts, p, brand, n, t)
    draw_bot_bar(draw, fonts, p, n, t, lang)

    # Estimate content height for vertical centering
    tmp = ImageDraw.Draw(img)
    est = 0
    if slide.get("label"):   est += 54
    if slide.get("title"):
        clean = slide["title"].replace("*", "")
        tfont = fonts["headline_xl"] if len(clean) < 35 else fonts["headline_lg"]
        est += th(clean, tfont, C_W, tmp, 1.12) + 32 + 20
    if slide.get("text"):
        txf = fonts["body_lg"] if not slide.get("title") else fonts["body"]
        est += th(slide["text"].replace("*", ""), txf, C_W, tmp, 1.55) + 18
    if slide.get("bullets"):
        for b in slide["bullets"]:
            est += th(b.replace("*", ""), fonts["body"], C_W - 32, tmp, 1.45) + 18
    if slide.get("comparison"):
        for k in ("old", "new"):
            cmp_ = slide["comparison"].get(k)
            if cmp_:
                est += th(cmp_["text"], fonts["card_body"],
                          C_W - CPX * 2, tmp, 1.5) + CPY * 2 + 44 + 16
    if slide.get("card"):
        est += th(slide["card"]["text"], fonts["card_body"],
                  C_W - CPX * 2, tmp, 1.5) + CPY * 2 + 44 + 28
    if slide.get("code_block"):
        est += 52 + len(slide["code_block"]) * lh(fonts["code"], tmp, 1.7) + CPY*2 + 28
    if slide.get("pills"):
        est += 66

    avail = C_H
    y = C_TOP + (max(16, (avail - est) // 3) if est < avail * 0.62 else 16)

    if slide.get("label"):
        y = draw_label(draw, fonts, p, slide["label"], y) + 4

    if slide.get("title"):
        title = slide["title"] if lang == "zh" else slide["title"]
        title_draw = title.rstrip(".")
        # Auto-accent last word if no *markers*
        if "*" not in title_draw:
            parts = title_draw.rsplit(" ", 1)
            if len(parts) == 2:
                title_draw = parts[0] + " *" + parts[1] + "*"
        tclean = title_draw.replace("*", "")
        tfont  = fonts["headline_xl"] if len(tclean) < 35 else fonts["headline_lg"]
        y = draw_rich(draw, title_draw, (PAD, y), tfont,
                      p["headline"], p["divider"], C_W, sp=1.12,
                      acc_bg=p["accent_hi_bg"], acc_fg=p["accent_hi_fg"])
        y = draw_divider(draw, p, y)

    if slide.get("text"):
        has_title = bool(slide.get("title"))
        txfont = fonts["body_lg"] if not has_title else fonts["body"]
        y = draw_rich(draw, slide["text"], (PAD, y + 4), txfont,
                      p["body"], p["divider"], C_W, sp=1.55,
                      acc_bg=p["accent_hi_bg"], acc_fg=p["accent_hi_fg"]) + 18

    if slide.get("bullets"):
        y = block_bullets(draw, fonts, p, PAD, y, slide["bullets"], C_W)

    if slide.get("comparison"):
        comp = slide["comparison"]
        y += 12
        if comp.get("old"):
            o = comp["old"]
            y = block_comparison_card(img, draw, fonts, p, PAD, y, C_W,
                                      o["text"],
                                      label=o.get("label", "OLD WAY"),
                                      label_c=p["cmp_old_label"],
                                      bg_c=p["cmp_old_bg"],
                                      bg_a=p["cmp_old_bg_a"],
                                      side_c=p["cmp_old_label"]) + 18
        if comp.get("new"):
            nw_ = comp["new"]
            y = block_comparison_card(img, draw, fonts, p, PAD, y, C_W,
                                      nw_["text"],
                                      label=nw_.get("label", "NEW WAY"),
                                      label_c=p["cmp_new_label"],
                                      bg_c=p["cmp_new_bg"],
                                      bg_a=p["cmp_new_bg_a"],
                                      side_c=p["cmp_new_label"]) + 18

    if slide.get("card"):
        cd = slide["card"]
        y += 8
        y = block_callout_card(img, draw, fonts, p, PAD, y, C_W,
                               cd["text"], label=cd.get("label")) + 22

    if slide.get("code_block"):
        y += 8
        y = block_code(img, draw, fonts, PAD, y, C_W, slide["code_block"]) + 22

    if slide.get("pills"):
        y += 12
        y = block_pills(img, draw, fonts, p, PAD, y,
                        slide["pills"], slide.get("pills_active"))

    layout = slide.get("image_layout", "inline")
    if slide.get("image"):
        ip = cdir / "reference" / slide["image"]
        if not ip.exists():
            ip = Path(slide["image"])
        if ip.exists():
            remaining = C_BOT - y - 24
            if layout == "hero":
                block_hero_image(img, draw, p, ip, PAD, y + 8, C_W,
                                 max_h=max(300, min(520, remaining)))
            else:
                block_image(img, draw, p, ip, PAD, y + 8, C_W,
                            max_h=max(180, min(380, remaining)))

    if slide.get("images") and slide.get("image_layout") == "logo_row":
        paths = [cdir / "reference" / i for i in slide["images"]]
        paths = [p_ for p_ in paths if p_.exists()]
        if paths:
            y = block_logo_row(img, draw, p, paths, PAD, y + 12, C_W)

    if slide.get("images") and slide.get("image_layout") == "split":
        paths = [cdir / "reference" / i for i in slide["images"]]
        if all(p_.exists() for p_ in paths[:2]):
            block_split_images(img, draw, p, paths[0], paths[1],
                               PAD, y + 12, C_W, max_h=380,
                               labels=slide.get("image_labels"))

    return img

def render_cta(config, slide, fonts, cdir):
    """CTA is always dark theme — NM signature close."""
    p    = THEMES["dark"]
    img  = Image.new("RGB", (W, H), rgb(p["bg"]))
    # Aquamarine corner glow
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ar, ag, ab = rgb(C_ACCENT)
    ImageDraw.Draw(glow).ellipse([W - 500, -260, W + 260, 520],
                                  fill=(ar, ag, ab, 20))
    glow = glow.filter(ImageFilter.GaussianBlur(180))
    img  = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")
    draw = ImageDraw.Draw(img)

    lang    = config.get("language", "en")
    n, t    = slide["number"], config["total_slides"]
    brand   = config["profile"]["display_name"].upper()
    counter = f"{n:02d} / {t:02d}"
    draw.text((PAD, 26), brand, font=fonts["topbar"], fill=rgb(p["label"]))
    cw = draw.textbbox((0, 0), counter, font=fonts["counter"])[2]
    draw.text((W - PAD - cw, 26), counter,
              font=fonts["counter"], fill=rgb(p["muted"]))
    _hairline(draw, p, PAD, TOP_H + 4, W - PAD)
    _hairline(draw, p, PAD, H - BOT_H - 4, W - PAD)
    footer = "FOLLOW FOR MORE" if lang == "en" else "記得 FOLLOW"
    draw.text((PAD, H - BOT_H + 26), footer,
              font=fonts["caption"], fill=rgb(p["muted"]))

    cx = W // 2
    y  = int(H * 0.15)

    # Name
    name  = config["profile"]["display_name"]
    nfont = fonts["headline_md"]
    nw    = draw.textbbox((0, 0), name, font=nfont)[2]
    draw.text((cx - nw // 2, y), name, font=nfont, fill=rgb(p["headline"]))
    y += draw.textbbox((0, 0), name, font=nfont)[3] + 20

    # Handle
    handle = config["profile"]["handle"]
    hw = draw.textbbox((0, 0), handle, font=fonts["body"])[2]
    draw.text((cx - hw // 2, y), handle, font=fonts["body"], fill=rgb(p["label"]))
    y += 70

    # Divider
    draw.rounded_rectangle([(cx - 48, y), (cx + 48, y + 5)],
                           radius=2, fill=rgb(p["divider"]))
    y += 44

    # CTA body
    cta = slide.get("text", "Follow for daily AI insights")
    cta_h = th(cta, fonts["body_lg"], C_W - 40, draw, 1.45)
    draw_plain(draw, cta, (PAD + 20, y), fonts["body_lg"],
               p["body"], C_W - 40, sp=1.45, align="center")
    y += cta_h + 48

    # Gradient pill button
    if slide.get("button_text"):
        btn   = slide["button_text"]
        bfont = fonts["body_bold"]
        btw   = draw.textbbox((0, 0), btn, font=bfont)[2]
        bw, bh = btw + 88, 72
        bx    = cx - bw // 2

        grad = Image.new("RGBA", (bw, bh), (0, 0, 0, 0))
        lc, rc = rgb(C_ACCENT), rgb("#65CBFF")    # Aqua → Blue
        for px_ in range(bw):
            t_ = px_ / bw
            col = tuple(int(lc[i] + (rc[i] - lc[i]) * t_) for i in range(3))
            ImageDraw.Draw(grad).line([(px_, 0), (px_, bh)], fill=col + (255,))
        mask = Image.new("L", (bw, bh), 0)
        ImageDraw.Draw(mask).rounded_rectangle([(0, 0), (bw, bh)],
                                                radius=bh // 2, fill=255)
        pill = Image.new("RGBA", (bw, bh), (0, 0, 0, 0))
        pill.paste(grad, (0, 0), mask)

        glow2 = Image.new("RGBA", (bw + 44, bh + 44), (0, 0, 0, 0))
        glow2.paste(pill, (22, 22), pill)
        glow2 = glow2.filter(ImageFilter.GaussianBlur(14))
        img.paste(glow2, (bx - 22, y - 22), glow2)
        img.paste(pill, (bx, y), pill)
        draw = ImageDraw.Draw(img)

        bbt = draw.textbbox((0, 0), btn, font=bfont)
        draw.text((bx + (bw - btw) // 2, y + (bh - (bbt[3] - bbt[1])) // 2 - bbt[1]),
                  btn, font=bfont, fill=rgb("#2D1E2F"))

    return img

# ── Main ──────────────────────────────────────────────────────────────────────
def render(cdir):
    cdir   = Path(cdir)
    config = json.loads((cdir / "config.json").read_text(encoding="utf-8"))
    lang   = config.get("language", "en")
    fonts  = load_fonts(lang)
    slides = config["slides"]
    config["total_slides"] = len(slides)
    print(f"Rendering {len(slides)} slides ({lang})...")
    (cdir / "reference").mkdir(exist_ok=True)

    for i, slide in enumerate(slides):
        slide["number"] = i + 1
        stype = slide.get("type", "body")
        theme = slide.get("theme",
                          "dark" if stype in ("hook", "cta") else "light")
        if   stype == "hook": img = render_hook(config, slide, fonts, cdir)
        elif stype == "cta":  img = render_cta(config, slide, fonts, cdir)
        else:                 img = render_body(config, slide, fonts, cdir)
        out = cdir / f"slide_{i+1}.png"
        img.save(str(out), "PNG")
        print(f"  OK slide_{i+1}.png  [{stype:5s}  theme={theme}]")

    print(f"\nDone → {cdir}")

if __name__ == "__main__":
    render(sys.argv[1] if len(sys.argv) > 1 else "carousel-test")