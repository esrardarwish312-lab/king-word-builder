import json
from pathlib import Path
from collections import Counter

class WordEngine:
    def __init__(self):
        base = Path(__file__).parent
        path = base / "data" / "dictionary_final.json"
        frequency_path = base / "data" / "english_frequency_50k.txt"

        with open(path, encoding="utf-8") as f:
            self.dictionary = json.load(f)

        self.frequency = {}

        with open(frequency_path, encoding="utf-8") as f:
            for rank, line in enumerate(f, 1):
                parts = line.split()
                if parts:
                    self.frequency[parts[0].lower()] = rank

    def generate(self, original, level="All"):
        original = original.lower().strip()

        if not original.isalpha():
            return []

        available = Counter(original)
        results = []

        for word, data in self.dictionary.items():
            if len(word) < 2 or len(word) >= len(original):
                continue

            if Counter(word) - available:
                continue

            rank = self.frequency.get(word, 999999)

            if level == "Easy" and rank > 5000:
                continue
            if level == "Medium" and not 5000 < rank <= 15000:
                continue
            if level == "Advanced" and rank <= 15000:
                continue

            results.append({
                "word": word.upper(),
                "data": data,
                "rank": rank
            })

        results.sort(key=lambda x: (
            len(x["word"]),
            x["rank"],
            x["word"]
        ))

        return results
