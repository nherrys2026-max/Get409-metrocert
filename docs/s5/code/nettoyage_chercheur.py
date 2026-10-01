import re

def main(texte: str) -> dict:
    t = re.sub(r"<think>.*?</think>", "", texte or "", flags=re.S)
    t = re.sub(r"^.*?</think>", "", t, flags=re.S)
    t = t.replace("**", "").replace("__", "")
    t = re.sub(r"(?m)^#{1,6}\s*", "", t)
    t = t.replace("‑", "-")

    # Bilan recalculé à partir des lignes M1 à M15 (le modèle ne compte plus)
    statuts = {}
    for l in t.split("\n"):
        m = re.match(r"\s*M(\d{1,2})\b", l)
        if not m:
            continue
        n = int(m.group(1))
        s = re.search(r":\s*(PRÉSENT|MANQUANT|À VÉRIFIER|NON APPLICABLE)", l)
        if 1 <= n <= 15 and s and n not in statuts:
            statuts[n] = s.group(1)
    if len(statuts) >= 10 and "BILAN" in t:
        cat = {k: [f"M{n}" for n in sorted(statuts) if statuts[n] == k]
               for k in ("PRÉSENT", "MANQUANT", "À VÉRIFIER", "NON APPLICABLE")}
        bilan = f"BILAN (recalculé sur {len(statuts)} mentions) :\n" + "\n".join(
            f"{k} : {', '.join(v) if v else '—'} ({len(v)})" for k, v in cat.items())
        t = t[:t.index("BILAN")] + bilan
    return {"result": t.strip()}
