"""字典運算

1. 以 zip 組合 values/keys 進行 min/max/sorted
2. min 可透過 key 參數比較字典鍵值
3. 利用 dict key 取得最小鍵
"""

prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}

# zip(prices.values(), prices.keys()) 可以根據價格比較，並回傳對應鍵
min(zip(prices.values(), prices.keys()))
max(zip(prices.values(), prices.keys()))
sorted(zip(prices.values(), prices.keys()))

# 直接以字典鍵做比較，可取得最小價格對應的 key
min(prices, key=lambda k: prices[k])  # 回傳 key
