# memory_system.py
# 功能：高階 Agent 記憶系統，管理短期與長期記錄
# 修仙隱喻：元神管理修煉筆記，洞察歷練

import json
import os

SHORT_TERM_FILE = "short_term_memory.json"
LONG_TERM_FILE = "long_term_memory.json"

class MemorySystem:
    def __init__(self):
        # 短期記憶：當前任務或戰鬥事件
        self.short_term = self.load_memory(SHORT_TERM_FILE)
        # 長期記憶：累積歷練與知識圖譜
        self.long_term = self.load_memory(LONG_TERM_FILE)

    def load_memory(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save_memory(self, memory, filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(memory, f, indent=2, ensure_ascii=False)

    # 記錄短期事件
    def remember_short(self, event):
        print(f"短期記憶更新：{event}")
        self.short_term.append(event)
        self.save_memory(self.short_term, SHORT_TERM_FILE)

    # 記錄長期歷練
    def remember_long(self, lesson):
        print(f"長期記憶更新：{lesson}")
        self.long_term.append(lesson)
        self.save_memory(self.long_term, LONG_TERM_FILE)

    # 查詢短期記憶
    def recall_short(self):
        return self.short_term

    # 查詢長期記憶
    def recall_long(self):
        return self.long_term

# 範例測試
if __name__ == "__main__":
    memory = MemorySystem()
    # 模擬短期事件
    memory.remember_short({"event": "遇到妖獸", "effect": "血量減少10"})
    # 模擬長期歷練
    memory.remember_long({"lesson": "學會躲避妖獸攻擊", "level": 1})
    print("短期記憶：", memory.recall_short())
    print("長期記憶：", memory.recall_long())
