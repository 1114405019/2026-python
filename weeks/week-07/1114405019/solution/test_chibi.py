import unittest
from collections import Counter
from chibi_battle import ChibiBattle

class TestChibiBattle(unittest.TestCase):
    """測試 ChibiBattle 引擎"""

    def setUp(self):
        """每個測試前準備"""
        self.game = ChibiBattle()

    def test_load_generals_from_file(self):
        """測試 1: 正確讀取 9 位武將"""
        self.game.load_generals('../generals.txt')
        self.assertEqual(len(self.game.generals), 9)
        self.assertIn('劉備', self.game.generals)
        self.assertIn('曹操', self.game.generals)

    def test_parse_general_attributes(self):
        """測試 2: 正確解析武將屬性"""
        self.game.load_generals('../generals.txt')
        general = self.game.generals['關羽']
        self.assertEqual(general.name, '關羽')
        self.assertEqual(general.atk, 28)
        self.assertEqual(general.def_, 14)
        self.assertEqual(general.spd, 85)
        self.assertEqual(general.faction, '蜀')

    def test_faction_distribution(self):
        """測試 3: 三國分布正確"""
        self.game.load_generals('../generals.txt')
        factions = Counter(g.faction for g in self.game.generals.values())
        self.assertEqual(factions['蜀'], 3)
        self.assertEqual(factions['吳'], 3)
        self.assertEqual(factions['魏'], 3)

    def test_eof_parsing(self):
        """測試 4: 正確識別 EOF 結尾"""
        self.game.load_generals('../generals.txt')
        self.assertEqual(len(self.game.generals), 9)  # 不會超過 9

    def test_battle_order_by_speed(self):
        """測試 5: 根據速度排序戰鬥順序"""
        self.game.load_generals('../generals.txt')
        battle_order = self.game.get_battle_order()
        self.assertEqual(battle_order[0].spd, 85)  # 最快
        self.assertEqual(battle_order[-1].spd, 60)  # 最慢

    def test_calculate_damage(self):
        """測試 6: 正確計算傷害 (攻擊 - 防禦)"""
        self.game.load_generals('../generals.txt')
        damage = self.game.calculate_damage('關羽', '夏侯惇')
        self.assertEqual(damage, 28 - 14)  # = 14

    def test_damage_counter_accumulation(self):
        """測試 7: Counter 自動累加傷害"""
        self.game.load_generals('../generals.txt')
        self.game.calculate_damage('關羽', '夏侯惇')
        self.game.calculate_damage('關羽', '曹操')
        self.assertEqual(self.game.stats['damage']['關羽'], 26)  # 14 + 12

    def test_simulate_one_wave(self):
        """測試 8: 模擬一波戰鬥"""
        self.game.load_generals('../generals.txt')
        self.game.simulate_wave(1)
        total_damage = sum(self.game.stats['damage'].values())
        self.assertGreater(total_damage, 0)

    def test_simulate_three_waves(self):
        """測試 9: 模擬三波完整戰役"""
        self.game.load_generals('../generals.txt')
        self.game.simulate_battle()
        shu_wu_damage = sum(
            dmg for name, dmg in self.game.stats['damage'].items()
            if self.game.generals[name].faction in ['蜀', '吳']
        )
        wei_damage = sum(
            dmg for name, dmg in self.game.stats['damage'].items()
            if self.game.generals[name].faction == '魏'
        )
        self.assertGreater(shu_wu_damage, wei_damage)

    def test_troop_loss_tracking(self):
        """測試 10: defaultdict 追蹤兵力損失"""
        self.game.load_generals('../generals.txt')
        self.game.simulate_battle()
        self.assertGreater(self.game.stats['losses']['夏侯惇'], 0)

    def test_damage_ranking_most_common(self):
        """測試 11: most_common() 傷害排名"""
        self.game.load_generals('../generals.txt')
        self.game.simulate_battle()
        ranking = self.game.get_damage_ranking()
        damages = [dmg for _, dmg in ranking]
        self.assertEqual(damages, sorted(damages, reverse=True))

    def test_faction_damage_stats(self):
        """測試 12: 按勢力統計傷害"""
        self.game.load_generals('../generals.txt')
        self.game.simulate_battle()
        faction_stats = self.game.get_faction_stats()
        self.assertGreater(faction_stats['蜀'], 0)
        self.assertGreater(faction_stats['吳'], 0)
        # 魏軍沒有攻擊，所以沒有傷害
        self.assertEqual(faction_stats.get('魏', 0), 0)

    def test_defeated_generals(self):
        """測試 13: 正確識別戰敗將領"""
        self.game.load_generals('../generals.txt')
        self.game.simulate_battle()
        defeated = self.game.get_defeated_generals()
        self.assertGreater(len(defeated), 0)

if __name__ == '__main__':
    unittest.main()