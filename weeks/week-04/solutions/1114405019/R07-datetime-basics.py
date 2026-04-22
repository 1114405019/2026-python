# R07-datetime-basics.py. Datetime Basics (2.20)

import time

x = time.time()
print(int(x)) # current timestamp, integer seconds

y = 86400  # seconds in a day
print(x + y) # timestamp one day later

x = 3600  # seconds in an hour
y = 24
print(x * y) # 86400, seconds in a day
