import mysql.connector
import itertools

def xor(text, key):
    infkey = itertools.chain.from_iterable(itertools.repeat(key))
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(text, infkey))

dbuser = 'root'
encrypted_passwd = 'Password7#'
key = 'key'

db = mysql.connector.connect(
    host='localhost',
    user=dbuser,
    passwd=encrypted_passwd,
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
