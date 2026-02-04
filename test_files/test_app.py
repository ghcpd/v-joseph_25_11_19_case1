"""
Test suite for Flask Project Management System
Tests all endpoints and verifies documentation accuracy
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, tasks, archived_tasks
import unittest


class TestFlaskApp(unittest.TestCase):
    
    def setUp(self):
        """Set up test client and clear data before each test"""
        self.client = app.test_client()
        app.config['TESTING'] = True
        tasks.clear()
        archived_tasks.clear()
    
    def test_index_route(self):
        """Test the main index route loads successfully"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_add_task_with_title_only(self):
        """Test adding task with only title (as documented in README)"""
        response = self.client.post('/add', data={'title': 'Test Task'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['title'], 'Test Task')
        # Check if color is set to default 'white'
        self.assertEqual(tasks[0]['color'], 'white')
    
    def test_add_task_with_color(self):
        """Test adding task with title and color"""
        response = self.client.post('/add', data={'title': 'Colored Task', 'color': 'red'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['color'], 'red')
    
    def test_delete_task(self):
        """Test deleting a task using GET /delete/<index>"""
        tasks.append({'title': 'Task to Delete', 'color': 'white'})
        response = self.client.get('/delete/0', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(tasks), 0)
    
    def test_archive_task_route_method(self):
        """Test archive endpoint - README says POST but implementation uses GET"""
        tasks.append({'title': 'Task to Archive', 'color': 'blue'})
        
        # Test with GET (actual implementation)
        response = self.client.get('/archive/0', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(archived_tasks), 1)
        self.assertEqual(len(tasks), 0)
        
        # Test with POST (documented method) - should fail
        tasks.append({'title': 'Another Task', 'color': 'green'})
        response = self.client.post('/archive/1')
        # POST should return 405 Method Not Allowed
        self.assertEqual(response.status_code, 405)
    
    def test_change_color_route_name(self):
        """Test color change - README says /change_color but implementation is /update_color"""
        tasks.append({'title': 'Task', 'color': 'white'})
        
        # Test documented route (should fail)
        response = self.client.post('/change_color/0', data={'color': 'yellow'})
        self.assertEqual(response.status_code, 404)
        
        # Test actual route (should work)
        response = self.client.post('/update_color/0', data={'color': 'yellow'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(tasks[0]['color'], 'yellow')
    
    def test_archived_tasks_display(self):
        """Test that archived tasks are displayed"""
        tasks.append({'title': 'Task', 'color': 'white'})
        self.client.get('/archive/0')
        
        response = self.client.get('/')
        self.assertIn(b'Archived Tasks', response.data)
        self.assertIn(b'Task', response.data)


if __name__ == '__main__':
    unittest.main()
