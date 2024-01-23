--聚合函数
select avg(attack) from sanguo;
select sum(attack) from sanguo;

select max(attack) as 最大值,min(attack) as 最小值
from sanguo;

--count不会统计null值 统计所有记录可以使用 *
select count(*) from sanguo;

--如果一个字段值筛选后都一样则可以与聚合函数一起放在select后
select country,avg(attack) from sanguo
where country="蜀";

select gender,max(attack),min(attack) from sanguo
where gender="男";


