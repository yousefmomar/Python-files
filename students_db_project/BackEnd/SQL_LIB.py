import sqlite3 

def create_tbl():

    conn=sqlite3.connect("studens.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY,fn TEXT,ln TEXT,term INTEGER,gpa REAL)")
    conn.commit()
    conn.close()

def insert(fn,ln,term,gpa):

    conn=sqlite3.connect("studens.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO students VALUES (NULL,?,?,?,?)",(fn.lower(),ln.lower(),term,gpa))
    conn.commit()
    conn.close()

def view_all():

    conn=sqlite3.connect("studens.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM students")
    rows=cur.fetchall()
    conn.close()
    return(rows)

def delete(id):

    conn=sqlite3.connect("studens.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,fn,ln,term,gpa):
    
    conn=sqlite3.connect("studens.db")
    cur=conn.cursor()
    cur.execute("UPDATE students SET fn=?,ln=?,term=?,gpa=? WHERE id=?",(fn.lower(),ln.lower(),term,gpa,id))
    conn.commit()
    conn.close()

def search(id="",fn="",ln="",term="",gpa=""):

    conn=sqlite3.connect("studens.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM students WHERE id=? OR fn=? OR ln=? OR term=? OR gpa=?",(id,fn.lower(),ln.lower(),term,gpa))
    rows=cur.fetchall()
    conn.close()
    return(rows)

def delete_all():

    conn=sqlite3.connect("studens.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM students")
    conn.commit()
    conn.close()

#main
create_tbl()

print(view_all())
print(delete_all())