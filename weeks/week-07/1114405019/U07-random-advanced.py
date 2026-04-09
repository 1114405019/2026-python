# U07. 隨機種子與安全亂數（3.11）
# random 模組為偽隨機，相同種子產生相同序列；密碼學請用 secrets

# Remember（記憶）
# - random 模組是偽隨機，可重現（適合測試）
# - 相同種子產生相同序列
# - 密碼學應用必須用 secrets 模組，不可預測

import random
import secrets

# 相同種子 → 相同序列（可重現）
random.seed(42)
seq1 = [random.randint(1, 100) for _ in range(5)]
random.seed(42)
seq2 = [random.randint(1, 100) for _ in range(5)]
print(f"相同種子序列相等: {seq1 == seq2}")  # True

# 不同 Random 實例各自獨立
rng1 = random.Random(1)
rng2 = random.Random(2)
print(f"不同實例: {rng1.random():.3f}, {rng2.random():.3f}")  # 各自的隨機流

# 密碼學安全亂數（不可預測，不能設種子）
rand_int = secrets.randbelow(100)
print(f"安全隨機整數: {rand_int}")  # 預期輸出: 0-99 的隨機數
rand_hex = secrets.token_hex(16)
print(f"安全 hex 字串: {rand_hex}")  # 預期輸出: 32 字元 hex 字串
rand_bytes = secrets.token_bytes(16)
print(f"安全 bytes: {rand_bytes}")  # 預期輸出: 16 位元組的 bytes

# 重要：random 模組不適合密碼、token、session key 等安全場景
# 只適合遊戲、模擬、測試等非安全用途
