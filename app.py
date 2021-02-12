import dbcreds
import mariadb
import sys

def connect():
    return mariadb.connect(
        user=dbcreds.user,
        password=dbcreds.password,
        host=dbcreds.host,
        port=dbcreds.port,
        database=dbcreds.database
    )
    
    
def view_blog():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM blog_post")
        result = cursor.fetchall()
        row_count = cursor.rowcount
        hr()
        print("Returned " + str(row_count) + " results")
        hr()
        for row in result:
            print(row)

    except:
        hr()
        print("DB Error")
        hr()
        sys.exit
    
    finally:
        if (cursor != None):
            cursor.close()
        if (conn != None):
            conn.rollback()
            conn.close()
            
            
def add_blog():
    username = input("username: ")
    content = input("content: ")

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO blog_post (username, content) VALUES (?, ?)",
        [username, content]
    )
    conn.commit()

    if (cursor.rowcount == 1):
        hr()
        print("New blog posted successfully!!!")
    else:
        hr()
        print("There was an error")

    cursor.close()
    conn.close()
    
def hr():
    print()
    print("------------------------------")
    print()

while True:
    hr()
    print("1. View blog")
    print("2. Add new blog")
    print("3. Exit")
    hr()
    choice = int(input("Choice: "))
    if choice == 1:
        view_blog()
    elif choice == 2:
        add_blog()
    elif choice == 3:
        hr()
        print("Goodbye!")
        break
