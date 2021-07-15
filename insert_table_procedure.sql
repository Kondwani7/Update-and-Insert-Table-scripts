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