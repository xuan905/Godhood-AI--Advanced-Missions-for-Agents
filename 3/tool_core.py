# 功能：定義多工具管理類別，統一呼叫與狀態追蹤
# 修仙隱喻：元神掌控法寶核心，統籌靈器運轉

class ToolCore:
    def __init__(self):
        self.tools = {}

    def register_tool(self, name, func):
        """註冊工具或法寶"""
        self.tools[name] = func
        print(f"[ToolCore] 元神掌控新法寶：{name}")

    def use_tool(self, name, *args, **kwargs):
        """使用指定工具"""
        if name in self.tools:
            print(f"[ToolCore] 施展法寶：{name}")
            return self.tools[name](*args, **kwargs)
        else:
            print(f"[ToolCore] 法寶 {name} 未註冊")
            return None
