聚合练习 使用 books
1. 统计每位作家出版图书的平均价格
select author,avg(price) from books
group by author;

2. 统计每个出版社出版的带有备注的图书数量
select press,count(comment) from books
group by press;

3. 统计同一时间出版图书的最高价格和最低价格
select publish_time,max(price),min(price)
from books group by publish_time;

4. 筛选出那些出版过超过50元图书的出版社，
并按照其出版图书的平均价格降序排序
select press,avg(price) from books
group by press
having max(price) > 50
order by avg(price) desc;

练习： 如下字段需要存储，请设计表关系，建立数据表

微信号  姓名   电话    图片    内容
 id    user  tel   image   content
时间   位置      点赞      评论
time  site    `like`     comment

create table user(
id int primary key auto_increment,
user varchar(30) not null,
tel char(11)
);

create table friends(
id int primary key auto_increment,
image varchar(50),
content text,
time datetime,
site text,
user_id int ,
foreign key(user_id) references user(id)
);

create table mylike(
id int primary key auto_increment,
user_id int ,
friends_id int,
`like` bit default 0,
comment text,
foreign key(user_id) references user(id) ,
foreign key(friends_id) references friends(id)
);
