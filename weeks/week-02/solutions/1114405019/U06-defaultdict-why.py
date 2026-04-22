# U06. defaultdict 為何比手動初始化乾淨（1.6）
"""
defaultdict 為何比手動初始化乾淨

collections.defaultdict 在訪問不存在的鍵時會自動創建預設值，
避免了手動檢查和初始化的繁瑣程式碼，使程式碼更簡潔和易讀。
"""

from collections import defaultdict

# 基礎用法
print("=== 基礎用法 ===")

# 傳統字典的問題
traditional = {}
words = ['apple', 'banana', 'apple', 'cherry', 'banana']

for word in words:
    if word not in traditional:
        traditional[word] = 0
    traditional[word] += 1

print(f"傳統方法統計: {traditional}")

# 使用 defaultdict
word_count = defaultdict(int)  # 預設值為 0
for word in words:
    word_count[word] += 1  # 自動創建鍵並初始化為 0

print(f"defaultdict 統計: {dict(word_count)}")

# 進階應用
print("\n=== 進階應用 ===")

# 不同類型的預設值
# list 預設值
list_dict = defaultdict(list)
categories = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot'), ('fruit', 'orange')]

for category, item in categories:
    list_dict[category].append(item)

print("分類統計 (list):")
for category, items in list_dict.items():
    print(f"  {category}: {items}")

# set 預設值
set_dict = defaultdict(set)
for category, item in categories:
    set_dict[category].add(item)

print("\n分類統計 (set):")
for category, items in set_dict.items():
    print(f"  {category}: {items}")

# 自訂函數作為預設值工廠
def default_score():
    return {'correct': 0, 'total': 0, 'percentage': 0.0}

score_dict = defaultdict(default_score)
tests = [('Alice', True), ('Bob', False), ('Alice', True), ('Charlie', True), ('Bob', True)]

for student, correct in tests:
    score_dict[student]['total'] += 1
    if correct:
        score_dict[student]['correct'] += 1
    score_dict[student]['percentage'] = score_dict[student]['correct'] / score_dict[student]['total']

print("\n學生成績統計:")
for student, scores in score_dict.items():
    print(f"  {student}: {scores['correct']}/{scores['total']} ({scores['percentage']:.1%})")

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: 文字分析
def analyze_text(text):
    """分析文字中的單詞頻率和字母統計"""
    word_freq = defaultdict(int)
    letter_freq = defaultdict(int)

    words = text.lower().split()
    for word in words:
        word_freq[word] += 1
        for letter in word:
            if letter.isalpha():
                letter_freq[letter] += 1

    return word_freq, letter_freq

sample_text = "The quick brown fox jumps over the lazy dog"
word_freq, letter_freq = analyze_text(sample_text)

print("文字分析:")
print(f"單詞頻率: {dict(word_freq)}")
print(f"字母頻率: {dict(letter_freq)}")

# 案例2: 購物清單管理
class ShoppingManager:
    def __init__(self):
        self.items_by_category = defaultdict(list)
        self.total_by_category = defaultdict(float)

    def add_item(self, category, item, price):
        self.items_by_category[category].append(item)
        self.total_by_category[category] += price

    def get_summary(self):
        summary = {}
        for category in self.items_by_category:
            summary[category] = {
                'items': self.items_by_category[category],
                'total': self.total_by_category[category],
                'count': len(self.items_by_category[category])
            }
        return summary

manager = ShoppingManager()
purchases = [
    ('水果', '蘋果', 30),
    ('水果', '香蕉', 20),
    ('蔬菜', '胡蘿蔔', 25),
    ('水果', '橘子', 35),
    ('蔬菜', '青菜', 40),
    ('飲料', '牛奶', 65)
]

for category, item, price in purchases:
    manager.add_item(category, item, price)

print("\n購物總結:")
summary = manager.get_summary()
for category, data in summary.items():
    print(f"{category}:")
    print(f"  項目: {data['items']}")
    print(f"  數量: {data['count']}")
    print(f"  總價: ${data['total']:.0f}")

# 案例3: 網路日誌分析
def analyze_logs(logs):
    """分析不同IP的訪問統計"""
    ip_stats = defaultdict(lambda: {'requests': 0, 'errors': 0, 'bytes': 0})

    for log in logs:
        ip, status, size = log
        ip_stats[ip]['requests'] += 1
        ip_stats[ip]['bytes'] += size
        if status >= 400:
            ip_stats[ip]['errors'] += 1

    return ip_stats

# 模擬日誌數據
logs = [
    ('192.168.1.1', 200, 1024),
    ('192.168.1.2', 404, 0),
    ('192.168.1.1', 200, 2048),
    ('192.168.1.3', 500, 512),
    ('192.168.1.2', 200, 1024),
    ('192.168.1.1', 200, 512)
]

ip_stats = analyze_logs(logs)

print("\nIP訪問統計:")
for ip, stats in ip_stats.items():
    success_rate = (stats['requests'] - stats['errors']) / stats['requests'] * 100
    print(f"{ip}:")
    print(f"  請求數: {stats['requests']}")
    print(f"  錯誤數: {stats['errors']}")
    print(f"  總流量: {stats['bytes']} bytes")
    print(f"  成功率: {success_rate:.1f}%")

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. defaultdict(default_factory) 自動為不存在鍵創建預設值
2. 常見工廠函數: int, list, set, dict
3. 自訂工廠: lambda 或函數返回複雜預設值
4. 避免 KeyError: 不需要手動檢查鍵是否存在
5. 程式碼簡潔: 減少 if-else 初始化邏輯
6. 適用場景: 計數、分類、統計、快取
7. 記憶體: 只在需要時創建預設值
"""

from collections import defaultdict

pairs = [('a', 1), ('a', 2), ('b', 3)]

# 手動版：一直判斷 key 是否存在
d = {}
for k, v in pairs:
    if k not in d:
        d[k] = []
    d[k].append(v)

# defaultdict：省掉初始化分支
d2 = defaultdict(list)
for k, v in pairs:
    d2[k].append(v)
