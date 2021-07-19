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
create procedure insert_pathfindertemp(in id int, in name text, in email text, in age int, 
									   in job_title text,in company text,in annual_salary real)
begin
	insert into pathfindertemp(id,name, email, age, job_title, company, annual_salary) 
					    values(id, name, email, age, job_title, company, annual_salary);
end;                                       
$$
--example
call insert_pathfindertemp(7,'gotter','gotter@gmail.com',39,'East Africa head of Risk','KPMG',120000);
")
#see mycursor output
for x in mycursor:
    print(x)
