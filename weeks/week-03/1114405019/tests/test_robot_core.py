import unittest

from robot_core import RobotManager


class TestRobotManager(unittest.TestCase):
    def test_rotate_left_from_north(self):
        manager = RobotManager(width=5, height=5, x=0, y=0, dir="N")
        manager.execute_command("L")
        self.assertEqual(manager.current_state(), (0, 0, "W", False))

    def test_rotate_right_from_north(self):
        manager = RobotManager(width=5, height=5, x=0, y=0, dir="N")
        manager.execute_command("R")
        self.assertEqual(manager.current_state(), (0, 0, "E", False))

    def test_rotate_four_times_right_returns_to_north(self):
        manager = RobotManager(width=5, height=5, x=0, y=0, dir="N")
        for _ in range(4):
            manager.execute_command("R")
        self.assertEqual(manager.current_state(), (0, 0, "N", False))

    def test_forward_inside_boundary_does_not_get_lost(self):
        manager = RobotManager(width=2, height=2, x=0, y=0, dir="N")
        manager.execute_command("F")
        self.assertEqual(manager.current_state(), (0, 1, "N", False))

    def test_forward_outside_boundary_marks_lost(self):
        manager = RobotManager(width=2, height=2, x=0, y=2, dir="N")
        manager.execute_command("F")
        self.assertEqual(manager.current_state(), (0, 2, "N", True))

    def test_lost_robot_stops_executing_following_commands(self):
        manager = RobotManager(width=1, height=1, x=0, y=1, dir="N")
        manager.execute_command("F")
        self.assertTrue(manager.lost)
        manager.execute_command("R")
        manager.execute_command("F")
        self.assertEqual(manager.current_state(), (0, 1, "N", True))

    def test_first_lost_leaves_scent(self):
        manager = RobotManager(width=1, height=1, x=0, y=1, dir="N")
        manager.execute_command("F")
        self.assertIn((0, 1, "N"), manager.scent)
        self.assertTrue(manager.lost)

    def test_second_robot_ignores_danger_at_same_position_direction(self):
        scent = {(0, 1, "N")}
        manager = RobotManager(width=1, height=1, x=0, y=1, dir="N", scent=scent)
        manager.execute_command("F")
        self.assertFalse(manager.lost)
        self.assertEqual(manager.current_state(), (0, 1, "N", False))

    def test_scent_does_not_apply_for_different_direction(self):
        scent = {(1, 0, "N")}
        manager = RobotManager(width=1, height=1, x=1, y=0, dir="E", scent=scent)
        manager.execute_command("F")
        self.assertTrue(manager.lost)
        self.assertIn((1, 0, "E"), manager.scent)
        self.assertEqual(manager.current_state(), (1, 0, "E", True))

    def test_multiple_commands_stop_after_lost(self):
        manager = RobotManager(width=2, height=2, x=0, y=2, dir="N")
        for cmd in "FRFFF":
            manager.execute_command(cmd)
        self.assertEqual(manager.current_state(), (0, 2, "N", True))

    def test_invalid_command_raises_value_error(self):
        manager = RobotManager(width=5, height=5, x=0, y=0, dir="N")
        with self.assertRaises(ValueError):
            manager.execute_command("X")

    def test_scent_preserved_between_robot_instances(self):
        manager1 = RobotManager(width=1, height=1, x=0, y=1, dir="N")
        manager1.execute_command("F")
        self.assertIn((0, 1, "N"), manager1.scent)

        manager2 = RobotManager(width=1, height=1, x=0, y=1, dir="N", scent=manager1.scent)
        manager2.execute_command("F")
        self.assertFalse(manager2.lost)


if __name__ == "__main__":
    unittest.main()
