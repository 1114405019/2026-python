"""OrderedDict

1. 保留插入順序的字典
2. 可與 json 一起序列化
3. 適合需要順序輸出的情境
"""

from collections import OrderedDict
import json

# OrderedDict 建立後保留鍵值對的插入順序
d = OrderedDict()
d['foo'] = 1; d['bar'] = 2

# json.dumps 仍可序列化 OrderedDict，並保留順序
json.dumps(d)
