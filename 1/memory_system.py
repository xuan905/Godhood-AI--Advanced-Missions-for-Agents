# memory_system.py
# 功能：高階 Agent 記憶系統，管理短期與長期修煉記錄
# 修仙比喻：元神筆記分為短期感悟與長期心法傳承

class MemorySystem:
    def __init__(self):
        self.short_term = []   # 短期記憶：當日修煉心得或臨時任務
        self.long_term = []    # 長期記憶：元神核心心法、歷代經驗

    def remember_short(self, note):
        """記錄短期修煉或任務筆記"""
        self.short_term.append(note)
        print(f"[短期記憶] 記錄筆記：{note}")

    def remember_long(self, note):
        """記錄長期心法或元神核心知識"""
        self.long_term.append(note)
        print(f"[長期記憶] 核心筆記加入：{note}")

    def recall_short(self):
        """回顧近期心得與行動"""
        print("=== 短期記憶回顧 ===")
        for idx, note in enumerate(self.short_term, 1):
            print(f"{idx}. {note}")
        print("=== 結束回顧 ===\n")

    def recall_long(self):
        """回顧核心心法與元神知識"""
        print("=== 長期記憶回顧 ===")
        for idx, note in enumerate(self.long_term, 1):
            print(f"{idx}. {note}")
        print("=== 結束回顧 ===\n")


# 範例使用
if __name__ == "__main__":
    memory = MemorySystem()
    
    # 短期修煉心得
    memory.remember_short("今日吸收天地靈氣，提升法力20點")
    memory.remember_short("擊敗小妖，學會閃避招式")
    
    # 長期心法筆記
    memory.remember_long("掌握玄靈元神運行法則")
    memory.remember_long("元神法力循環與真氣積蓄技巧")
    
    # 回顧記憶
    memory.recall_short()
    memory.recall_long()
