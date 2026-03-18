import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from task2_student_ranking import rank_students

class TestTask2(unittest.TestCase):
    def test_ranking_logic(self):
        # 測資：(姓名, 分數, 年齡)
        students = [
            ("amy", 88, 20),
            ("bob", 88, 19),
            ("zoe", 92, 21),
            ("ian", 88, 19),
            ("eva", 92, 20)
        ]
        # 取前 3 名
        result = rank_students(students, 3)
        
        # 預期結果：eva (92,20) > zoe (92,21) > bob (88,19)
        expected = [
            ("eva", 92, 20),
            ("zoe", 92, 21),
            ("bob", 88, 19)
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()