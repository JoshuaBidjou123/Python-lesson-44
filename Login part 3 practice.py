@app.route('/register', methods= ['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and username in request.form and password in request.form and email email in request.form:
useranme = request.form['username']
password = request.form['password']
email = request.form['email']
mydb = mysql.connector.connect(
    host='remotemysql.com',
    user='Rz8hqnlk4',
    password='nd6wK03xe)',
    database='Rx8hqnlk4'    
)
mycursor = mydb.cursor()
print(username)
mycursor.execute('SELECT * FROM LoginDetails WHERE Name = %s AND Email-id = %s', (username, email))
account = mycursor.fetchone()
print(account)
if account:
    msg = 'Account already exists!'
    elif not re.match(r'^9^\d'*@[^\d]*\.\.\.)
