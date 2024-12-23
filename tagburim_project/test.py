import unittest
from unittest.mock import patch, MagicMock
import mysql.connector


class TestDatabaseFunctions(unittest.TestCase):

    @patch('mysql.connector.connect')
    def test_print_table_details_and_update(self, mock_connect):
        
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        
       
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        
        
        mock_cursor.description = [('id',), ('name',)]
        mock_cursor.fetchall.return_value = [(1, 'Alice'), (2, 'Bob')]
        
       
        with patch('builtins.input', side_effect=['name', 'Charlie', 'id = 1']):
            print_table_details_and_update(
                host="localhost",
                user="root",
                password="your_password",
                database="users",
                table_name="USERS.STUDENTS"
            )
        
       
        mock_connect.assert_called_once_with(
            host="localhost",
            user="root",
            password="your_password",
            database="users"
        )
        
        
        mock_cursor.execute.assert_any_call("SELECT * FROM USERS.STUDENTS")
        
        
        mock_cursor.execute.assert_any_call(
            "UPDATE USERS.STUDENTS SET name = %s WHERE id = 1",
            ('Charlie',)
        )
        
        
        mock_connection.commit.assert_called_once()
        
        
        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()



import unittest
from unittest.mock import patch, MagicMock
import mysql.connector

class TestDatabaseFunctions(unittest.TestCase):
    
    @patch('mysql.connector.connect')
    def test_print_table_details_and_update(self, mock_connect):
        
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        
        
        mock_cursor.description = [('id',), ('name',)]
        mock_cursor.fetchall.return_value = [(1, 'Alice'), (2, 'Bob')]
        
       
        with patch('builtins.input', side_effect=['name', 'Charlie', 'id = 1']):
            
            print_table_details_and_update(
                host="localhost",
                user="root",
                password="your_password",
                database="users",
                table_name="USERS.STUDENTS"
            )
        
        
        mock_cursor.execute.assert_any_call('SELECT * FROM USERS.STUDENTS')
        mock_cursor.execute.assert_any_call(
            'UPDATE USERS.STUDENTS SET name = %s WHERE id = 1',
            ('Charlie',)
        )

if __name__ == '__main__':
    unittest.main()
