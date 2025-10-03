# 功能：記錄行動
# 修仙隱喻：元神筆記，完整記錄修煉過程

import json, os
from datetime import datetime

LOG_FILE = "action_log.json"

if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        action_log = json.load(f)
else:
    action_log = []

def log_action(agent_name, action, detail=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {"time": timestamp, "agent": agent_name, "action": action, "detail": detail}
    action_log.append(entry)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(action_log, f, indent=2, ensure_ascii=False)
    print(f"[{timestamp}] {agent_name} 行動：{action} -> {detail}")

def get_recent_actions(agent_name=None, n=5):
    if agent_name:
        filtered = [a for a in action_log if a["agent"]==agent_name]
    else:
        filtered = action_log
    return filtered[-n:]
