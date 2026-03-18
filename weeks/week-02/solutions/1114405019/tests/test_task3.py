import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from task3_log_summary import summarize_logs

class TestTask3(unittest.TestCase):
    def test_log_summary(self):
        # 準備測資：(使用者, 動作)
        logs = [
            ("alice", "login"), ("bob", "login"), ("alice", "view"),
            ("alice", "logout"), ("bob", "view"), ("bob", "view"),
            ("chris", "login"), ("bob", "logout")
        ]
        user_counts, top_action, top_count = summarize_logs(logs)
        
        # 預期結果：bob 4 次, alice 3 次, chris 1 次
        expected_users = [("bob", 4), ("alice", 3), ("chris", 1)]
        self.assertEqual(user_counts, expected_users)
        self.assertEqual(top_action, "login")
        self.assertEqual(top_count, 3)

    def test_empty_log(self):
        # 邊界測試：空輸入
        user_counts, top_action, top_count = summarize_logs([])
        self.assertEqual(user_counts, [])
        self.assertEqual(top_action, None)

if __name__ == '__main__':
    unittest.main()