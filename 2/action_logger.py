# action_logger.py
# 功能：記錄 Agent 與玩家行動，便於策略分析
# 修仙隱喻：元神筆記，完整記錄修煉過程

"""
特點：

記錄 Agent 與玩家行動

保持 時間戳，方便策略分析與回溯

仙界隱喻：元神筆記完整記錄修煉過程

可調整 get_recent_actions(n) 查看近期行動
"""

import json
import os
from datetime import datetime

LOG_FILE = "action_log.json"

# 初始化行動紀錄
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        action_log = json.load(f)
else:
    action_log = []

def log_action(agent_name, action_type, detail):
    """
    記錄一次行動
    :param agent_name: Agent 或玩家名稱
    :param action_type: 行動類型（探索/戰鬥/採集等）
    :param detail: 行動細節或結果
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {
        "time": timestamp,
        "agent": agent_name,
        "action": action_type,
        "detail": detail
    }
    action_log.append(entry)
    print(f"[{timestamp}] {agent_name} 行動：{action_type} -> {detail}")
    # 存檔，保持元神筆記更新
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(action_log, f, indent=2, ensure_ascii=False)

def get_recent_actions(n=5):
    """取得最近 n 條行動紀錄"""
    return action_log[-n:]

# 範例測試
if __name__ == "__main__":
    log_action("高階Agent", "探索靈脈", "獲得法力10")
    log_action("玩家", "採集草藥", "獲得草藥3個")
    print("最近行動紀錄：")
    for act in get_recent_actions(5):
        print(act)
