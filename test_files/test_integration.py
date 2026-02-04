"""
Integration tests for task management features
Tests the complete workflow of task operations
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, tasks, archived_tasks
import unittest


class TestTaskManagement(unittest.TestCase):
    
    def setUp(self):
        """Set up test client and clear data"""
        self.client = app.test_client()
        app.config['TESTING'] = True
        tasks.clear()
        archived_tasks.clear()
    
    def test_complete_task_workflow(self):
        """Test complete workflow: add, modify color, archive"""
        # Add task
        self.client.post('/add', data={'title': 'Complete Workflow Task', 'color': 'blue'})
        self.assertEqual(len(tasks), 1)
        
        # Update color
        self.client.post('/update_color/0', data={'color': 'green'})
        self.assertEqual(tasks[0]['color'], 'green')
        
        # Archive task
        self.client.get('/archive/0')
        self.assertEqual(len(tasks), 0)
        self.assertEqual(len(archived_tasks), 1)
        self.assertEqual(archived_tasks[0]['title'], 'Complete Workflow Task')
    
    def test_multiple_tasks(self):
        """Test managing multiple tasks"""
        # Add multiple tasks
        self.client.post('/add', data={'title': 'Task 1', 'color': 'red'})
        self.client.post('/add', data={'title': 'Task 2', 'color': 'blue'})
        self.client.post('/add', data={'title': 'Task 3', 'color': 'green'})
        self.assertEqual(len(tasks), 3)
        
        # Delete middle task
        self.client.get('/delete/1')
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]['title'], 'Task 1')
        self.assertEqual(tasks[1]['title'], 'Task 3')
    
    def test_invalid_index(self):
        """Test operations with invalid indices"""
        tasks.append({'title': 'Only Task', 'color': 'white'})
        
        # Try to delete invalid index
        self.client.get('/delete/5')
        self.assertEqual(len(tasks), 1)  # Task should still be there
        
        # Try to archive invalid index
        self.client.get('/archive/10')
        self.assertEqual(len(tasks), 1)
        self.assertEqual(len(archived_tasks), 0)
        
        # Try to update color of invalid index
        self.client.post('/update_color/99', data={'color': 'red'})
        self.assertEqual(tasks[0]['color'], 'white')  # Color unchanged
    
    def test_task_order_preservation(self):
        """Test that task order is maintained"""
        self.client.post('/add', data={'title': 'First', 'color': 'white'})
        self.client.post('/add', data={'title': 'Second', 'color': 'white'})
        self.client.post('/add', data={'title': 'Third', 'color': 'white'})
        
        self.assertEqual(tasks[0]['title'], 'First')
        self.assertEqual(tasks[1]['title'], 'Second')
        self.assertEqual(tasks[2]['title'], 'Third')


if __name__ == '__main__':
    unittest.main()
