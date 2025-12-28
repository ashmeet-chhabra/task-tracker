import unittest
import tempfile
import os
import json

import task_cli as task

# core features test

class TestTaskCLI(unittest.TestCase):
    def test_add_task(self):
        task.add_task("Buy milk")
        tasks = task.load_tasks()

        self.assertEqual(len(tasks), 1)

if __name__ == '__main__':
    unittest.main()
