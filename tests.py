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

        self.assertEqual(len(tasks), 1);
        self.assertEqual(tasks[0]['description'], 'Buy milk');
        self.assertEqual(tasks[0]['status'], 'todo');
        task.delete_task(1);

    def test_update_task(self):
        task.add_task('Buy tea')
        task.update_task(1, "We hate tea. Buy coffee instead")
        
        tasks = task.load_tasks()
        self.assertEqual(tasks[0]['description'], "We hate tea. Buy coffee instead")
        task.delete_task(1)

    def test_delete_task(self):
        task.add_task('Cauliflower')
        task.delete_task(1)
        tasks = task.load_tasks()

        self.assertEqual(len(tasks), 0)

    def test_mark_task(self):
        task.add_task('Hello')
        task.mark_task(1, 'Actually Bye')
        tasks = task.load_tasks()

        self.assertEqual(tasks[0]['status'], 'Actually Bye')
        task.delete_task(1)

if __name__ == '__main__':
    unittest.main()
