### Task 1: Sequence Clean 測試紀錄

# 第一次執行 (Red)
PS ...\1114405019> python tests/test_task1.py
Traceback (most recent call last):
  File "...\tests\test_task1.py", line 2, in <module>
    from task1_sequence_clean import clean_sequence
ModuleNotFoundError: No module named 'task1_sequence_clean'

# 第二次執行 (Green)
PS ...\1114405019> $env:PYTHONPATH = "."; python tests/test_task1.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

### Task 2: Sequence Clean 測試紀錄

# 第一次執行 (Red)
PS C:\Users\yiteng\Downloads\week02\2026-python\weeks\week-02\solutions\1114405019> $env:PYTHONPATH = "."; python tests/test_task2.py
Traceback (most recent call last):
  File "C:\Users\yiteng\Downloads\week02\2026-python\weeks\week-02\solutions\1114405019\tests\test_task2.py", line 6, in <module>
    from task2_student_ranking import rank_students
ImportError: cannot import name 'rank_students' from 'task2_student_ranking' (C:\Users\yiteng\Downloads\week02\2026-python\weeks\week-02\solutions\1114405019\task2_student_ranking.py)

# 第二次執行 (Green)
PS C:\Users\yiteng\Downloads\week02\2026-python\weeks\week-02\solutions\1114405019> $env:PYTHONPATH = "."; python tests/test_task2.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

### Task 3: Sequence Clean 測試紀錄

# 第一次執行 (Red)
PS C:\Users\yiteng\Downloads\week02\2026-python\weeks\week-02\solutions\1114405019> $env:PYTHONPATH = "."; python tests/test_task3.py
Traceback (most recent call last):
  File "C:\Users\yiteng\Downloads\week02\2026-python\weeks\week-02\solutions\1114405019\tests\test_task3.py", line 6, in <module>
    from task3_log_summary import summarize_logs
ImportError: cannot import name 'summarize_logs' from 'task3_log_summary' (C:\Users\yiteng\Downloads\week02\2026-python\weeks\week-02\solutions\1114405019\task3_log_summary.py)

# 第二次執行 (Green)
PS C:\Users\yiteng\Downloads\week02\2026-python\weeks\week-02\solutions\1114405019> $env:PYTHONPATH = "."; python tests/test_task3.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
