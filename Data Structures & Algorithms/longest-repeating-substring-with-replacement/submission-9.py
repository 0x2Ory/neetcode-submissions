class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        res = 0
        l = 0
        
        for r in range(len(s)):
            # 1. Zeichen hinzufügen
            counts[s[r]] = counts.get(s[r], 0) + 1
            
            # 2. Schleife: Solange das Fenster UNGÜLTIG ist, schrumpfen wir es von links
            # Wir müssen 'max(counts.values())' nutzen, um die ECHTE Frequenz im aktuellen Fenster zu kennen!
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                # Wichtig: Wenn ein Zähler auf 0 sinkt, löschen wir ihn, damit max() schneller bleibt
                #if counts[s[l]] == 0:
                #   del counts[s[l]]
                l += 1  # Fenster schrumpft aktiv
            
            # 3. Jetzt ist das Fenster garantiert gültig -> Rekord updaten
            res = max(res, (r - l) + 1)
            
        return res
