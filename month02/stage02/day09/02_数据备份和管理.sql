--复制数据内容到新表中
create table student
select name,age,score from class
where score>70;

--创建新的用户
create user "vip"@"%" identified by "123";

--为新用户增加权限
grant select,update on stu.class to "vip"@"%"
identified by "123" with grant option;

--收回权限
revoke update on stu.class from "vip"@"%";


drop user "vip"@"%";


