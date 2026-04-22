# Python 模組、類別與例外處理深度解析

## 概述

本文深入探討 Python 中的模組導入、類別定義、例外處理機制以及相關的時間複雜度分析。通過理解這些基礎概念，開發者可以編寫更健壯和可維護的代碼。

## 語法解析

### 模組導入 (Import)

Python 使用 `import` 語句來導入模組：

```python
import module_name
from module_name import specific_item
from module_name import item1, item2
import module_name as alias
```

- `import module`：導入整個模組
- `from module import item`：導入特定項目
- `as alias`：提供別名

### 類別定義 (Class Definition)

```python
class ClassName:
    def __init__(self, parameters):
        # 初始化方法
        self.attribute = value
    
    def method(self, parameters):
        # 實例方法
        return result
```

- `class` 關鍵字定義類別
- `__init__` 是構造函數
- `self` 參考實例本身

### 例外處理 (Exception Handling)

```python
try:
    # 可能拋出例外的代碼
    risky_operation()
except ExceptionType as e:
    # 處理特定例外
    handle_error(e)
except (Type1, Type2):
    # 處理多種類型
    handle_multiple_errors()
else:
    # 沒有例外時執行
    success_operation()
finally:
    # 總是執行
    cleanup()
```

## 比較表格

| 例外處理方式 | 適用場景 | 代碼複雜度 | 效能影響 | 可讀性 |
|--------------|----------|------------|----------|--------|
| try-except | 預期例外 | 中等 | 低 | 高 |
| if-else 檢查 | 避免例外 | 低 | 中等 | 中等 |
| 裸 except | 捕獲所有 | 高 | 高 | 低 |
| 多重 except | 不同處理 | 高 | 低 | 高 |
| finally | 資源清理 | 中等 | 低 | 高 |

## Big O 複雜度分析

### 時間複雜度

- **模組導入**：$O(1)$ 常數時間（已編譯模組）
- **類別實例化**：$O(1)$ 通常常數時間
- **屬性訪問**：$O(1)$ 字典查找
- **方法調用**：$O(1)$ 加上方法體複雜度
- **例外拋出**：$O(1)$ 但處理開銷大
- **例外捕獲**：$O(1)$ 查找處理器

### 空間複雜度

- **模組導入**：$O(M)$ 其中 $M$ 為模組大小
- **類別實例**：$O(A)$ 其中 $A$ 為屬性數量
- **例外對象**：$O(1)$ 通常小常數

## 實用範例

### 模組使用

```python
from collections import deque

q = deque(maxlen=2)
q.append(1)
q.append(2)
q.append(3)  # 自動丟掉最舊的元素
```

### 類別定義與使用

```python
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    
    def get_id(self):
        return self.user_id

u = User(42)
uid = u.get_id()
```

### 例外處理

```python
def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False
```

## 設計模式與最佳實踐

### 模組組織
- 使用 `__init__.py` 定義包
- 避免循環導入
- 使用相對導入保持可移植性

### 類別設計
- 使用描述性名稱
- 實現 `__str__` 和 `__repr__`
- 遵循單一責任原則

### 例外處理
- 捕獲具體例外而非基類 Exception
- 使用 finally 確保資源清理
- 提供有意義的錯誤信息

## 常見複雜度陷阱

- **列表操作**：`append()` 通常 $O(1)$，但可能觸發 $O(n)$ 擴容
- **字典操作**：平均 $O(1)$，最壞 $O(n)$
- **集合操作**：平均 $O(1)$ 查找
- **字串連接**：重複 `+` 為 $O(n^2)$

## 結論

掌握 Python 的模組、類別和例外處理機制是編寫健壯代碼的基礎。通過理解語法、比較不同方法以及分析複雜度，開發者可以做出更明智的設計決策，提高代碼的效能和可維護性。