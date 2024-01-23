--多表查询，如果字段名重复时必须使用 table.col
select c.name,c.score,h.hobby,h.price
from class as c,hobby as h
where c.name="Lily";

--连长表没有关联并不意味着没有关系
select c.name,c.score,h.hobby,h.price
from class as c,hobby as h
where c.name=h.name;

--每个部门工资大于18000的员工  姓名  工资  部门
select  person.name,person.salary,dept.dname
from dept,person
where dept.id = person.dept_id and salary>18000;

内连接
select  person.name,person.salary,dept.dname
from dept inner join person
on dept.id = person.dept_id
where salary>18000;

左连接
select  person.name,person.salary,dept.dname
from person left join dept
on dept.id = person.dept_id
where salary>18000;


右连接统计每个部门员工人数
select  dname,count(name)
from person as p right join dept
on dept.id = p.dept_id
group by dname;








