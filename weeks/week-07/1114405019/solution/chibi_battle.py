from collections import namedtuple, Counter, defaultdict

# 使用 namedtuple 定義武將
General = namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def_', 'spd', 'is_leader'])

class ChibiBattle:
    """吞食天地戰役引擎"""

    def __init__(self):
        self.generals = {}
        # 使用 Counter 和 defaultdict
        self.stats = {
            'damage': Counter(),        # 傷害統計
            'losses': defaultdict(int)  # 兵力損失
        }

    # 實作讀取 generals.txt 的函式，並正確處理 if line == 'EOF': break
    def load_generals(self, filename):
        """讀取武將資料，EOF 結尾"""
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line == 'EOF':
                    break
                if not line:
                    continue
                parts = line.split()
                faction, name, hp, atk, def_, spd, is_leader = parts
                general = General(
                    faction=faction,
                    name=name,
                    hp=int(hp),
                    atk=int(atk),
                    def_=int(def_),
                    spd=int(spd),
                    is_leader=(is_leader == 'True')
                )
                self.generals[name] = general

    # 實作戰鬥邏輯：依 speed 排序武將
    def get_battle_order(self):
        """根據速度決定戰鬥順序"""
        return sorted(self.generals.values(), key=lambda g: g.spd, reverse=True)

    def calculate_damage(self, attacker_name, defender_name):
        """計算傷害: 攻擊 - 防禦"""
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]
        damage = max(1, attacker.atk - defender.def_)
        # 使用 Counter 統計傷害排名
        self.stats['damage'][attacker_name] += damage
        # 使用 defaultdict 追蹤兵力損失
        self.stats['losses'][defender_name] += damage
        return damage

    def simulate_wave(self, wave_num):
        """模擬一波戰鬥"""
        order = self.get_battle_order()
        # 蜀吳聯軍對魏軍
        attackers = [g for g in order if g.faction in ['蜀', '吳']][:wave_num * 2]  # 每波增加攻擊者
        defenders = [g for g in self.generals.values() if g.faction == '魏']
        for _ in range(wave_num):  # 每波攻擊多次
            for attacker in attackers:
                for target in defenders:
                    self.calculate_damage(attacker.name, target.name)

    def simulate_battle(self):
        """模擬三波完整戰役"""
        for wave in range(1, 4):
            self.simulate_wave(wave)

    def get_damage_ranking(self, top_n=5):
        """傷害排名 (Top N)"""
        return self.stats['damage'].most_common(top_n)

    def get_faction_stats(self):
        """按勢力統計傷害"""
        faction_damage = defaultdict(int)
        for general_name, damage in self.stats['damage'].items():
            faction = self.generals[general_name].faction
            faction_damage[faction] += damage
        return dict(faction_damage)

    def get_defeated_generals(self):
        """取得戰敗將領"""
        defeated = []
        for name, total_loss in self.stats['losses'].items():
            if total_loss >= self.generals[name].hp:
                defeated.append(name)
        return defeated