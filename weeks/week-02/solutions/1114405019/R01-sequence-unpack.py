"""序列解包

1. tuple/list 位置解包
2. 多層嵌套結構解包
3. 使用佔位符忽略不必要元素
"""

# 簡單 tuple 解包：左側變數數量必須與右側元素數量一致
p = (4, 5)
x, y = p

# 也可以解包 list，並將嵌套 tuple 的子元素繼續解開
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
name, shares, price, (year, mon, day) = data

# 使用 '_' 作為占位符，忽略不需要的值
_, shares, price, _ = data
