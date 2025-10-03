# environment_interface.py
# 功能：模擬仙界環境感知
# 修仙比喻：修仙者觀察天地靈氣，感知四方妖獸與靈脈

import random

class EnvironmentInterface:
    def __init__(self):
        self.resources = ["靈石", "靈草", "法寶精華", "丹藥"]
        self.dangers = ["妖獸", "陷阱", "天劫", "敵派修士"]
        print("[環境初始化] 仙界靈氣瀰漫，感知天地萬象")

    def sense_resources(self):
        """偵測附近資源"""
        found = random.choices(self.resources, k=random.randint(1, 3))
        print(f"[資源感知] 仙界靈脈顯現，發現資源：{found}")
        return found

    def sense_dangers(self):
        """偵測附近危險"""
        detected = random.choices(self.dangers, k=random.randint(0, 2))
        if detected:
            print(f"[危險感知] 元神感知到危險：{detected}")
        else:
            print("[危險感知] 目前四周安全，無異動")
        return detected

# 範例使用
if __name__ == "__main__":
    env = EnvironmentInterface()
    
    # 模擬多次感知
    for _ in range(3):
        env.sense_resources()
        env.sense_dangers()
