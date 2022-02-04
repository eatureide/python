class GameStarts:
    # 跟踪游戏的统计信息

    def __init__(self, ai_game):
        # 初始化统计信息
        self.settings = ai_game.settings
        self.reset_starts()

    def reset_starts(self):
        # 初始化游戏运行其间可能变化的统计信息
        self.ship_left = self.settings.ship_limit