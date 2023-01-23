import sqlite3

# Connect to the database or create it if it doesn't exist
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create the DEPARTMENT table
table_create_query = '''
CREATE TABLE IF NOT EXISTS DEPARTMENT (
    ID INTEGER PRIMARY KEY,
    NAME TEXT,
    LOCATION TEXT
);
'''
cursor.execute(table_create_query)

# Create the EMPLOYEE table
table_create_query = '''
CREATE TABLE IF NOT EXISTS EMPLOYEE (
    ID INTEGER PRIMARY KEY,
    NAME TEXT,
    SALARY INTEGER,
    DEPT_ID INTEGER,
    FOREIGN KEY(DEPT_ID) REFERENCES DEPARTMENT(ID)
);
'''
cursor.execute(table_create_query)

# Insert some sample data into the DEPARTMENT table
table_insert_query = '''
INSERT INTO DEPARTMENT (ID, NAME, LOCATION)
VALUES (1, 'Executive', 'Sydney'),
       (2, 'Production', 'Sydney'),
       (3, 'Resources', 'Cape Town'),
       (4, 'Technical', 'Texas'),
       (5, 'Management', 'Paris');
'''
cursor.execute(table_insert_query)

# Insert some sample data into the EMPLOYEE table
table_insert_query = '''
INSERT INTO EMPLOYEE (ID, NAME, SALARY, DEPT_ID)
VALUES (1, 'Candice', 4685, 1),
       (2, 'Julia', 2559, 2),
       (3, 'Bob', 4405, 4),
       (4, 'Scarlet', 2350, 1),
       (5, 'Ileana', 1151, 4);
'''
cursor.execute(table_insert_query)

#Commit the transaction
conn.commit()

# Run the query
query = '''
SELECT d.NAME as [Department], COUNT(e.ID) as [Employee_Count]
FROM DEPARTMENT d
LEFT JOIN EMPLOYEE e ON d.ID = e.DEPT_ID
GROUP BY d.NAME
ORDER BY COUNT(e.ID) DESC, d.NAME ASC;
'''
cursor.execute(query)

# Print the results
print('Department\tEmployee_Count')
for row in cursor.fetchall():
    print(row[0], '\t\t', row[1])

# close the cursor and connection
cursor.close()
conn.close()
