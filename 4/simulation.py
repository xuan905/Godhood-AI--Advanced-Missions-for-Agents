# simulation.py
# 功能：整合模擬兩個 Agent 多回合修煉
# 修仙隱喻：元神在仙界中分神運轉，多回合修煉累積經驗與仙法
"""
模擬特色

兩個 Agent 協作：模擬門派弟子互動。

多回合修煉：每回合隨機分派任務。

行動記錄：自動保存到 action_log.json，可回顧。

記憶累積：短期/長期記憶與知識圖譜 KLP 自動更新。

知識圖譜可視化：每次修煉後可視化仙界事件關聯。

反饋機制：Agent 根據最近行動回顧調整策略。

仙界隱喻：元神分神修煉法術，累積修煉心得。
"""
from agent_core import AgentCore
from communication_hub import CommunicationHub
from task_allocator import TaskAllocator
from collaboration_manager import CollaborationManager
from feedback_loop import FeedbackLoop
from memory_system import MemorySystem
from knowledge_graph import KnowledgeGraph
from action_logger import log_action, get_recent_actions
import random
import time

# 初始化系統
agent1 = AgentCore("元神·凌霄")
agent2 = AgentCore("元神·清玄")

comm_hub = CommunicationHub()
task_allocator = TaskAllocator()
collab_mgr = CollaborationManager()
feedback1 = FeedbackLoop(agent1.name)
feedback2 = FeedbackLoop(agent2.name)

# 註冊 Agent 協作
collab_mgr.register_agent(agent1.name)
collab_mgr.register_agent(agent2.name)

# 預設行動列表
actions = ["探索靈脈", "修煉法術", "採集靈石", "挑戰妖獸", "陣法佈置"]

# 模擬多回合修煉
rounds = 5
for r in range(1, rounds+1):
    print(f"\n=== 第 {r} 回合修煉 ===")
    
    # 分派隨機任務
    task_allocator.add_task(agent1.name, random.choice(actions), priority=random.randint(1,3))
    task_allocator.add_task(agent2.name, random.choice(actions), priority=random.randint(1,3))

    # Agent 執行任務
    for agent in [agent1, agent2]:
        tasks = task_allocator.get_tasks(agent.name)
        for t in tasks:
            effect = f"法力+{random.randint(5,20)}"
            agent.perform_action(t["task"], effect)
            # 發訊息給另一個 Agent
            comm_hub.send_message(agent.name, agent2.name if agent==agent1 else agent1.name,
                                  f"{agent.name} 完成任務 {t['task']}，效果: {effect}")
    
    # 協作管理
    action_map = {agent1.name: tasks[0]["task"], agent2.name: tasks[0]["task"]}
    collab_mgr.coordinate_actions(action_map)
    
    # 反饋與回顧
    feedback1.evaluate()
    feedback2.evaluate()

    # 知識圖譜自動更新
    agent1.knowledge.build_from_short_memory()
    agent2.knowledge.build_from_short_memory()

    # 暫停模擬，感受回合間仙界呼吸
    time.sleep(1)

# 最終顯示知識圖譜
print("\n=== 仙界知識圖譜 ===")
agent1.knowledge.visualize()

# 顯示最近行動
print("\n=== 最近行動紀錄 ===")
for act in get_recent_actions(n=10):
    print(f"{act['time']} | {act['agent']} -> {act['action']} | {act['detail']}")
