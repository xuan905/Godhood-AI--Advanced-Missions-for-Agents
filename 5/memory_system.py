# 功能：短期與長期記憶管理
# 修仙隱喻：元神筆記，記錄修煉心得

import json, os

MEMORY_FILE = "memory.json"

class MemorySystem:
    def __init__(self):
        self.short_term = []
        self.long_term = []
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.long_term = data.get("long_term", [])

    def remember_short(self, record):
        self.short_term.append(record)

    def remember_long(self, record):
        self.long_term.append(record)
        self.save()

    def recall_short(self):
        return self.short_term

    def recall_long(self):
        return self.long_term

    def save(self):
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump({"long_term": self.long_term}, f, indent=2, ensure_ascii=False)
