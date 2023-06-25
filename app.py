from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

# PostgreSQL database connection
connect_to_db = psycopg2.connect(
    host="10.43.92.150",
    port="5432",
    database="todolist_db",
    user="postgres",
    password="mysecretpassword"
)

@app.route('/')
def index():
    # Fetch tasks from the database
    print("- Connect_to_db")
    cursor = connect_to_db.cursor()
    print(cursor)
    
    # Check if the table exists
    cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'todolist_table')")
    table_exists = cursor.fetchone()[0]
    
    if not table_exists:
        # Create the table if it doesn't exist
        cursor.execute("CREATE TABLE todolist_table (id SERIAL PRIMARY KEY, task TEXT NOT NULL)")
        connect_to_db.commit()
        print("- Table 'todolist_table' created successfully.")
    else:
        print("- Table 'todolist_table' already exists.")    
    
    
    print("- read tasks from db")
    cursor.execute("SELECT * FROM todolist_table ORDER BY id")
    tasks = cursor.fetchall()
    print("- tasks :")
    print(tasks)

    cursor.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    print("- adding the following task :", task)
    cur = connect_to_db.cursor()
    cur.execute("INSERT INTO todolist_table (task) VALUES (%s)", (task,))
    connect_to_db.commit()
    cur.close()
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    id = request.form['id']
    cur = connect_to_db.cursor()
    print("- deleting the following task id :", id)
    cur.execute("DELETE FROM todolist_table WHERE id = %s", (id,))
    connect_to_db.commit()
    cur.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
