# godhood_agent_simulation.py
# 綜合範例：多工具協作 + API + 排程 + 錯誤防護 + 行動紀錄
# 修仙隱喻：元神分神運轉仙法，逐步修煉升級

"""
"""

from tool_core import ToolCore
from api_connector import APIConnector
from plugin_manager import PluginManager
from task_scheduler import TaskScheduler
from error_guard import ErrorGuard
from action_logger import log_action

import random
import time

# 初始化各模組
tools = ToolCore()
api = APIConnector("https://api.mocki.io/v1")  # 模擬 API
plugins = PluginManager()
scheduler = TaskScheduler()
guard = ErrorGuard()

# 註冊工具
tools.register_tool("煉丹爐", lambda x: f"煉丹完成，法力+{x}")
tools.register_tool("靈石採集器", lambda x: f"採集到靈石 {x} 個")

# 註冊插件
plugins.load_plugin("仙法加持", lambda x: f"施展仙法，力量+{x}")
plugins.load_plugin("靈氣感知", lambda: f"感知到靈脈 {random.randint(1,3)} 處")

# 模擬多回合修煉
for round_num in range(1, 6):
    print(f"\n=== 回合 {round_num} ===")

    # 隨機任務
    action = random.choice(["煉丹", "採集靈石", "施展仙法", "感知靈脈"])

    def execute_action(act):
        if act == "煉丹":
            result = tools.use_tool("煉丹爐", random.randint(5,15))
        elif act == "採集靈石":
            result = tools.use_tool("靈石採集器", random.randint(1,5))
        elif act == "施展仙法":
            result = plugins.execute_plugin("仙法加持", random.randint(10,20))
        elif act == "感知靈脈":
            result = plugins.execute_plugin("靈氣感知")
        else:
            result = "空閒修煉"
        log_action("高階Agent", act, result)

    # 將任務加入排程
    scheduler.add_task(lambda act=action: guard.safe_execute(execute_action, act))

    # 每回合短暫等待，模擬修煉過程
    time.sleep(0.5)

# 執行所有任務
scheduler.run_all()

print("\n=== 修煉結束，查看最近行動 ===")
from action_logger import get_recent_actions
for act in get_recent_actions(10):
    print(act)
