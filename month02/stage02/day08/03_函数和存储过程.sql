--函数中不能直接写select,函数执行过程不负责展示数据
delimiter  $$
create function func() returns int
begin
 return (select score from class where id=1);
end $$
delimiter  ;

--函数中如果有写操作语句，那么函数只能 放在select后，不能放在where子句中
delimiter  $$
create function func1() returns int
begin
 update class set score=88 where id=1;
 return (select score from class where id=1);
end $$
delimiter  ;

--带有参数的函数
delimiter  $$
create function func2(uid int)
returns varchar(30)
begin
  return (select name from class where id=uid);
end $$
delimiter  ;


基础的存储过程
delimiter   $$
create procedure proc()
begin
  update class set score=89 where id=1;
  update hobby set price=9999 where id=1;
  select * from class order by score;
end $$
delimiter   ;

call proc();



参数和变量
delimiter   $$
create procedure proc1()
begin
  declare a int;  -- 局部变量
  -- 两种赋值方法
  set a=1;
  select age from class where id=1 into a;
  select a;  -- 相当于打印
end $$
delimiter   ;

call proc1();


IN : 传入的实参可以在存储过程中使用
OUT : 传入的实参不可在存储过程中使用，
      但是可以在存储过程中修改该形参，
      修改后会影响外部实参值

delimiter   $$
create procedure proc_out(OUT a int)
begin
  select a;
  set a=66666;
  select a;
end $$
delimiter   ;

set @num=1;
call proc_in(@num);


--查看创建语句
show create function func;
show create procedure proce;

查看一个数据库中创建的所有存储过程或者函数
show procedure status  where db="stu";
show function status  where db="stu";

删除函数存储过程
drop function if exists func02;
drop procedure if exists proc1;















