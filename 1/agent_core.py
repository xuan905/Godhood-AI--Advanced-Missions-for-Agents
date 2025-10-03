# agent_core.py
# 功能：定義高階 Agent 類別，包含記憶、法力、屬性管理
# 修仙比喻：建立元神與靈根，準備修煉仙法

class HighLevelAgent:
    def __init__(self, name):
        self.name = name
        self.hp = 100                  # 元神血量
        self.mana = 100                # 靈力法力
        self.level = 1                 # 修煉等級
        self.experience = 0            # 修煉經驗
        self.inventory = []            # 元神法寶
        self.memory = []               # 元神筆記，記錄修煉與行動歷程

    def add_experience(self, amount):
        """增加經驗，提升修煉等級"""
        self.experience += amount
        if self.experience >= 100:
            self.level_up()

    def level_up(self):
        """提升元神等級"""
        self.level += 1
        self.experience = 0
        self.hp += 20
        self.mana += 20
        print(f"{self.name} 的元神進階！等級提升至 {self.level}")

    def add_to_inventory(self, item):
        """獲得法寶或資源"""
        self.inventory.append(item)
        print(f"{self.name} 獲得 {item}，元神法寶添增")

    def remember(self, note):
        """記錄行動或修煉心得"""
        self.memory.append(note)
        print(f"{self.name} 記錄修煉筆記：{note}")

    def status(self):
        """顯示元神狀態"""
        print(f"=== {self.name} 狀態 ===")
        print(f"血量: {self.hp}, 法力: {self.mana}, 等級: {self.level}, 經驗: {self.experience}")
        print(f"法寶: {self.inventory}")
        print(f"筆記數量: {len(self.memory)}\n")


# 範例使用
if __name__ == "__main__":
    agent = HighLevelAgent("玄靈元神")
    agent.status()
    agent.add_experience(50)
    agent.add_to_inventory("天雷法杖")
    agent.remember("今日修煉心法，感悟天地靈氣")
    agent.status()
