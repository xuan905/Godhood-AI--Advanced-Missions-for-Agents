# knowledge_graph.py
# 功能：將事件與行動關聯，生成知識圖譜
# 修仙隱喻：元神構建仙界地圖，關聯靈脈與妖獸

"""
特點：

將事件與行動關聯形成 知識圖譜

與 memory_system.py 結合，利用短期記憶自動生成關聯

可視化仙界地圖，節點代表 靈脈/事件/妖獸

仙界隱喻：元神構建仙界地圖，關聯靈脈與妖獸
"""

import json
import os
import networkx as nx
import matplotlib.pyplot as plt
from memory_system import MemorySystem

GRAPH_FILE = "knowledge_graph.json"

class KnowledgeGraph:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.memory = MemorySystem()
        self.load_graph()

    def load_graph(self):
        if os.path.exists(GRAPH_FILE):
            with open(GRAPH_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                for node, edges in data.items():
                    for target in edges:
                        self.graph.add_edge(node, target)

    def save_graph(self):
        data = {}
        for node in self.graph.nodes:
            data[node] = list(self.graph.successors(node))
        with open(GRAPH_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    # 將事件與行動加入知識圖譜
    def add_relation(self, source, target):
        print(f"建立關聯：{source} -> {target}")
        self.graph.add_edge(source, target)
        self.save_graph()
    
    

    # 自動從短期記憶建立關聯
    def build_from_short_memory(self):
        for event in self.memory.recall_short():
            source = event.get("event") or event.get("action")
            target = event.get("effect") or "未知效果"
            self.add_relation(source, target)
    # """簡單評分：出現越多連接的行動分數越高"""
    def evaluate_action(self, action):
        """簡單評分：出現越多連接的行動分數越高"""
        if action in self.graph:
            return len(list(self.graph.successors(action)))
        return 0
    
    # 顯示知識圖譜
    def visualize(self):
        plt.figure(figsize=(10, 6))
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, arrows=True)
        plt.title("仙界知識圖譜")
        plt.show()

# 範例測試
if __name__ == "__main__":
    kg = KnowledgeGraph()
    # 手動加入事件與行動
    kg.add_relation("探索靈脈", "獲得法力")
    kg.add_relation("遭遇妖獸", "血量減少10")
    # 從短期記憶自動建立關聯
    kg.build_from_short_memory()
    # 視覺化知識圖譜
    kg.visualize()
