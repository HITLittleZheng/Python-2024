--模糊查询 %  _
select * from class where name like "A%";
select * from class where name like "___";

--集合中查找具有draw的
select * from hobby where hobby like "%draw%";

--字段重命名
select name  姓名,score  分数 from class;

select name ,score  from class as cls;

--排序
select * from class order by score;

select * from class
where sex="m"
order by score desc;

--复合排序 age优先 其次score
select * from class order by age,score desc;


--limit
select * from class limit 2;

--第一的女生
select * from class where sex='w'
order by score desc
limit 1;

--第二的女生  offset表示跳过几个
select * from class where sex='w'
order by score desc
limit 1 offset 1;

update class set score=score+1
where sex="m" limit 1;

--union查询：可以是不同字段也可以是不同表，
--但是查询字段数量必须一致
select * from class where sex="w"
union all
select * from class where score>75;

select name,sex,score from class where sex="w"
union
select name,age,score from class where score>75;

select name,age,score from class where score>75
union
select name,hobby,price from hobby;

--子查询
--子查询语句作为一张表 起名字
select *
from (select * from class where score>80) as c
where name="Tom";

--子查询语句作为一个值
select * from class where score >
(select score from class where name="Tom");

--子句作为一个集合
select * from class where name in
(select name from hobby);


