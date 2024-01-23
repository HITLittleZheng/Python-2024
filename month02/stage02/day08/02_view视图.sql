--创建一个视图
create view good_stu_view as
select name,age,score from class
where score>75;

--多表视图
create or replace view stu_hobby_view as
select class.name,score,hobby,price
from class inner join hobby
on class.name = hobby.name;

错误 ： 写操作同时涉及到多个表
update stu_hobby_view set score=88,price=40000
where name="Emma";

正确： 只涉及单张表
update stu_hobby_view set price=40000
where name="Emma";

--区分视图和表
show full tables in stu;

--删除视图
drop view if exists stu_hobby_view;

--修改视图
alter view good_student_view
as select name,age,sex,score from class
where score>=80;

