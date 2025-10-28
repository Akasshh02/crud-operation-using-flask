from flask import Flask,render_template,url_for,request,redirect,flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = '123'

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="root"
app.config["MYSQL_DB"]="employee"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)

@app.route('/')
def home():
    return render_template("home.html")
    
@app.route("/newemployee",methods=["GET","POST"])
def newemployee():
    if request.method =="POST":
        employeename=request.form["employeename"]
        age=request.form["age"]
        location=request.form["location"]
        contactno=request.form["contactno"]
        role=request.form["role"]
        department=request.form["department"]
        con=mysql.connection.cursor()
        sql="insert into employee(employeename,age,location,contactno,role,department) values(%s,%s,%s,%s,%s,%s)"
        con.execute(sql,[employeename,age,location,contactno,role,department])
        mysql.connection.commit()
        con.close()
        flash("Form submitted successfully!", "success")
        return redirect(url_for("home"))
    return render_template("newemployee.html")
                
@app.route("/employeedata")
def employeedata():
    con=mysql.connection.cursor()
    sql="select *from employee"
    con.execute(sql)
    res=con.fetchall()
    return render_template("employeedata.html",datas=res)

@app.route("/editemployee/<string:id>",methods=["GET","POST"])
def editemployee(id):
    con=mysql.connection.cursor()
    if request.method=='POST':
        employeename=request.form["employeename"]
        age=request.form["age"]
        location=request.form["location"]
        contactno=request.form["contactno"]
        role=request.form["role"]
        department=request.form["department"]
        sql="update employee set employeename=%s,age=%s,location=%s,contactno=%s,role=%s,department=%s where emp_id=%s"
        con.execute(sql,[employeename,age,location,contactno,role,department,id])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
        con.mysql.connection.cursor
    sql="select *from employee where emp_id=%s"
    con.execute(sql,[id])
    res=con.fetchone()
    return render_template("editemployee.html",data=res)
    
@app.route("/deleteemployee,<string:id>",methods=["GET","POST"])
def deleteemployee(id):
    con=mysql.connection.cursor()
    sql="delete from employee where emp_id=%s"
    con.execute(sql,id)
    mysql.connection.commit()
    con.close()
    return redirect(url_for("home"))
    
if(__name__ == '__main__'):
    app.run(debug=True)
