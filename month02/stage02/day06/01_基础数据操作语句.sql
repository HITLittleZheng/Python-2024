-- 基础查询
select * from class where score>80;
select * from class where age + 1=18;

--取整除法     / 真除
select * from class where age div 2=9;

字符串可以比较大小且不区分大小写
select * from class where name > "Lily";
select * from class where name = "lily";

-- 字段前binary区分大小写
select * from class where binary name="lily";

--查询分数在70-80之间的
select * from class
where score between 70 and 80;

--in 集合范围内的
select * from class where age in (16,18,20);

--判断空值用is
select * from class where sex is null;

select * from class
where sex='m' and score>80;

修改操作
update class set sex='m' where name="Alex";

update class set name="Joy",score=60
where name="Jot";

update class set age=age+1;

删除操作
delete from class where sex is null;


--alter语句
--新增一个字段
alter table hobby
add phone char(11) after price;

--删除一个字段
alter table hobby drop level;

--修改字段数据类型
alter table hobby modify phone char(16);

--替换原有字段
alter table hobby change phone tel char(16);


--时间数据类型
create table marathon (
id int primary key auto_increment,
athlete varchar(32),
birthday date,
r_time datetime comment "报名时间",
performance time
);

insert into marathon values
(1,"尼古拉斯","1994-10-23","2021-12-1 10:10:10","2:56:28"),
(2,"托瓦斯","1997-9-2","2021-11-30 18:13:20","2:33:33");

insert into marathon values
(3,"托尼","2000-1-3","2021-11-30 16:14:10","2:29:28");


select * from marathon
where birthday>="2000-01-01";

select * from marathon where r_time<now();

alter table marathon
modify r_time datetime default now();

insert into marathon (athlete,birthday) values
("刚刚","2000-4-3");





