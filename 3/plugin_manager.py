# 功能：管理插件或附加功能模組
# 修仙隱喻：元神調動輔助法寶，增強戰鬥與修煉能力

class PluginManager:
    def __init__(self):
        self.plugins = {}

    def load_plugin(self, name, plugin_func):
        self.plugins[name] = plugin_func
        print(f"[PluginManager] 元神掌控輔助法寶：{name}")

    def execute_plugin(self, name, *args, **kwargs):
        if name in self.plugins:
            print(f"[PluginManager] 使用輔助法寶：{name}")
            return self.plugins[name](*args, **kwargs)
        else:
            print(f"[PluginManager] 輔助法寶 {name} 未載入")
            return None
