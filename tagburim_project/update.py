import mysql.connector

def print_table_details_and_update(host, user, password, database, table_name):
    try:
        # الاتصال بقاعدة البيانات
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        
        if connection.is_connected():
            print(f"Connected to the database '{database}'")

            cursor = connection.cursor()
            
            # استعلام لجلب البيانات من الجدول
            query = f"SELECT * FROM {table_name}"
            cursor.execute(query)
            
            # طباعة أسماء الأعمدة
            column_names = [desc[0] for desc in cursor.description]
            print(f"Table: {table_name}")
            print(f"Columns: {', '.join(column_names)}")
            
            # طباعة بيانات الجدول
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            
            # تحديث البيانات بناءً على مدخلات المستخدم
            column_to_update = input("Enter the column you want to update: ")
            new_value = input("Enter the new value: ")
            condition = input("Enter the condition (e.g., id = 2): ")
            
            # استعلام لتحديث البيانات
            update_query = f"UPDATE {table_name} SET {column_to_update} = %s WHERE {condition}"
            cursor.execute(update_query, (new_value,))
            connection.commit()
            
            print(f"Table {table_name} updated successfully.")
    
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed.")


print_table_details_and_update(
    host="localhost",
    user="root",
    password="your_password",  
    database="users",        
    table_name="USERS.STUDENTS"      
)
