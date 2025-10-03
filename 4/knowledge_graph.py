# 功能：建立知識圖譜
# 修仙隱喻：元神構建仙界地圖，關聯靈脈與妖獸

import networkx as nx
import matplotlib.pyplot as plt
from memory_system import MemorySystem
import json, os

GRAPH_FILE = "knowledge_graph.json"

class KnowledgeGraph:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.memory = MemorySystem()
        if os.path.exists(GRAPH_FILE):
            with open(GRAPH_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                for node, edges in data.items():
                    for target in edges:
                        self.graph.add_edge(node, target)

    def add_relation(self, source, target):
        self.graph.add_edge(source, target)
        self.save_graph()
        print(f"[知識圖譜] {source} -> {target}")

    def build_from_short_memory(self):
        for event in self.memory.recall_short():
            self.add_relation(event.get("action","未知"), event.get("effect","未知"))

    def visualize(self):
        plt.figure(figsize=(10,6))
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='lightgreen', node_size=2000, arrows=True)
        plt.title("仙界知識圖譜")
        plt.show()

    def save_graph(self):
        data = {node: list(self.graph.successors(node)) for node in self.graph.nodes}
        with open(GRAPH_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
