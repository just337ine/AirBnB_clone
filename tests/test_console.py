import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsoleFeatures(unittest.TestCase):
    
    def setUp(self):
        self.console = HBNBCommand()
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.patcher.start()

    def tearDown(self):
        self.mock_stdout.close()
        self.patcher.stop()

    def test_help(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("help")
            output = mock_stdout.getvalue()
            self.assertIn("Documented commands (type help <topic>):", output)
    
    def test_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)
    
    def test_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("show BaseModel 1")
            output = mock_stdout.getvalue().strip()
            self.assertIn("[BaseModel] (1)", output)
    
    def test_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("destroy BaseModel 1")
            output = mock_stdout.getvalue().strip()
            self.assertFalse(output)

    def test_all(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_update(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("update BaseModel 1 name 'NewName'")
            self.console.onecmd("show BaseModel 1")
            output = mock_stdout.getvalue().strip()
            self.assertIn("[BaseModel] (1)", output)
            self.assertIn("'name': 'NewName'", output)
            
    def test_count(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("count BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_update_dict(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("update BaseModel 1 {'name': 'NewName'}")
            self.console.onecmd("show BaseModel 1")
            output = mock_stdout.getvalue().strip()
            self.assertIn("[BaseModel] (1)", output)
            self.assertIn("'name': 'NewName'", output)

if __name__ == "__main__":
    unittest.main()
