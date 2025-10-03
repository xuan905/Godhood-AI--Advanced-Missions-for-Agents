# 功能：長期追蹤任務成果與法力增長
# 修仙隱喻：修士在仙界歷練，累積修煉心得

from memory_system import MemorySystem

class GoalMonitor:
    def __init__(self):
        self.memory = MemorySystem()

    def track_progress(self):
        # 簡單示範統計短期記憶行動
        short_mem = self.memory.recall_short()
        return {"已執行任務數": len(short_mem)}
