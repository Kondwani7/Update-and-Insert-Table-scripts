import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password7#',
    database='the_room'
)

mycursor = db.cursor()

#update table stored procedure
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password7#',
    database='the_room'
)

mycursor = db.cursor()
#update procedure
mycursor.execute("
delimiter $$
create procedure update_pathfindertemp(in user_id int, in name text, in email text, in age int, 
									   in job_title text,in company text,in annual_salary real)
begin
	update pathfindertemp set name = name, email = email, age = age, job_title = job_title,
							  company = company, annual_salary = annual_salary
                              where user_id = id;
end;
$$

call update_pathfindertemp(2,'Betty','betty@gmail.com',26,'junior fullstack developer','Google',48000)
")
#see mycursor output
for x in mycursor:
    print(x)
