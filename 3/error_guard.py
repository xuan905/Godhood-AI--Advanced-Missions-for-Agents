# 功能：錯誤監控與防護機制
# 修仙隱喻：元神防止走火入魔，保持修煉穩定

class ErrorGuard:
    def __init__(self):
        self.errors = []

    def safe_execute(self, func, *args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            self.errors.append(str(e))
            print(f"[ErrorGuard] 元神穩定防護：捕捉錯誤 -> {e}")
            return None
