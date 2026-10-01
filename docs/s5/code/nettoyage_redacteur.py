import re

def main(texte: str) -> dict:
    t = re.sub(r"<think>.*?</think>", "", texte or "", flags=re.S)
    t = re.sub(r"^.*?</think>", "", t, flags=re.S)
    t = t.replace("**", "").replace("__", "")
    t = re.sub(r"(?m)^#{1,6}\s*", "", t)
    t = t.replace("‑", "-")

    # Dédoublonnage : un point déjà classé ❌ ou ⚠️ ne réapparaît pas dans 🔎 INCOHÉRENCES
    garder_toujours = ("ETA-", "chu", "EMT", "émission", "registre", "hors famille")
    lignes = t.split("\n")
    section = None
    deja_m, deja_mc = set(), set()
    for l in lignes:
        s = l.strip()
        if s.startswith("❌") or s.startswith("⚠"):
            section = True
        elif s.startswith("🔎") or s.startswith("✅") or s.startswith("─") or s.startswith("PROCHAINE"):
            section = None
        elif section and s:
            deja_m.update(re.findall(r"\bM(\d{1,2})\b", s))
            deja_mc.update(re.findall(r"MC-(\d{2})", s))
    sortie, garde, dans_incoh = [], [], False
    for l in lignes:
        s = l.strip()
        if s.startswith("🔎"):
            dans_incoh = True
            sortie.append(l)
            continue
        if dans_incoh and (s.startswith("─") or s.startswith("✅") or s.startswith("PROCHAINE")):
            if not garde:
                sortie.append("Aucune détectée.")
            else:
                for i, g in enumerate(garde, 1):
                    sortie.append(re.sub(r"^\s*(\d+[.)]|[-•])\s*", f"{i}. ", g))
            dans_incoh, garde = False, []
            sortie.append(l)
            continue
        if dans_incoh:
            if not s or s.lower().startswith("aucune"):
                continue
            if not any(k in s for k in garder_toujours):
                m = set(re.findall(r"\bM(\d{1,2})\b", s))
                mc = set(re.findall(r"MC-(\d{2})", s))
                if (m and m <= deja_m) or (not m and mc and mc <= deja_mc):
                    continue
            garde.append(l)
            continue
        sortie.append(l)
    return {"result": "\n".join(sortie).strip()}
