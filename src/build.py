# -*- coding: utf-8 -*-
"""Assemble index.html : l'interface (app.html) + les styles (themes/) + les données (data.py).

    python src/build.py
"""
import json
import re
from pathlib import Path

from data import E, FERIES, GRANDS_RDV, PERLES, TIPS, VACANCES, YEAR

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
THEMES = HERE / "themes"

# Ordre de la cascade : polices, base, Riso (isolé sous .th-riso), commun, puis un fichier par style.
STYLES = ["suisse", "cahier", "heatmap", "timbres", "ecran", "ticket", "departs", "ardoise", "metro", "bd", "gameboy"]


def ov(text):
    """Titre imprimé deux fois : le style Riso décale la seconde couche en rose, les autres la masquent."""
    return f'<span class="ov"><span class="b">{text}</span><span class="p" aria-hidden="true">{text}</span></span>'


def recap():
    """Page « L'essentiel de 2027 », identique pour tous les styles (seul le CSS change)."""
    feries = "".join(f"<li><b>{d}</b><span class='w'>{w}</span>{n}</li>" for d, w, n in FERIES)
    rows = "".join(
        f"<tr><td>{r[0]}</td>" + ("".join(f"<td>{c}</td>" for c in r[1:]) if len(r) == 4 else f'<td colspan="3">{r[1]}</td>') + "</tr>"
        for r in VACANCES)
    rdv = "".join(f"<li><b>{d}</b>{n}</li>" for d, n in GRANDS_RDV)
    return f"""
<section class="page recap">
  <div class="rtitle">{ov("L’essentiel de 2027")}</div>
  <div class="rgrid">
    <div class="rc"><div class="lbl">Jours fériés</div><ul class="fer">{feries}</ul></div>
    <div class="rc"><div class="lbl">Vacances scolaires 2026-2027</div>
<table>
<tr><th></th><th>Zone A</th><th>Zone B</th><th>Zone C</th></tr>
{rows}
</table>
<p class="small">Fin des vacances de Noël 2026 : lundi 04.01. Rentrée 2027 : jeudi 02.09.<br>
Zone A : Besançon, Bordeaux, Clermont-Ferrand, Dijon, Grenoble, Limoges, Lyon, Poitiers. Zone B : Aix-Marseille, Amiens, Lille, Nancy-Metz, Nantes, Nice, Normandie, Orléans-Tours, Reims, Rennes, Strasbourg. Zone C : Créteil, Montpellier, Paris, Toulouse, Versailles.</p>
<div class="extra">
  <div><b>Changement d'heure</b>28.03 heure d'été<br>31.10 heure d'hiver</div>
  <div><b>Saisons</b>20.03 printemps · 21.06 été<br>23.09 automne · 22.12 hiver</div>
</div></div>
    <div class="rc"><div class="lbl">Les grands rendez-vous</div><ul class="big">{rdv}</ul></div>
  </div>
</section>"""


def scope(css, prefix):
    """Préfixe chaque sélecteur par `prefix` pour isoler un style des autres."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    out = []
    for sel, body in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
        sel = ", ".join(f"{prefix} {s.strip()}" for s in sel.split(","))
        out.append(f"{sel} {{{body}}}")
    return "\n".join(out)


def read(name):
    return (THEMES / f"{name}.css").read_text(encoding="utf-8")


def main():
    styles = "\n".join([read("_polices"), read("_base"), scope(read("riso"), ".th-riso"), read("_commun")]
                       + [read(s) for s in STYLES])
    data = {
        "YEAR": YEAR,
        "events": {f"{m}-{d}": items for (m, d), items in sorted(E.items())},
        "tips": TIPS,
        "perles": [[list(md), n, i] for md, n, i in PERLES],
        "recap": recap(),
    }
    app = ((HERE / "app.html").read_text(encoding="utf-8")
           .replace("/*STYLES*/", styles)
           .replace("/*DATA*/", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
    (ROOT / "index.html").write_text(app, encoding="utf-8")
    nb = sum(len(v) for v in E.values())
    fun = sum(1 for v in E.values() for t in v if t.startswith("~"))
    print(f"index.html : {len(app) // 1024} Ko · {nb} dates dont {fun} décalées · {len(STYLES) + 1} styles")


if __name__ == "__main__":
    main()
