 将books表 拆分为 图书  作家  出版社
 三张数据表，自行设计字段和表关系
 E-R图表达并创建之

create table author(
id int primary key auto_increment,
aname varchar(30),
gender char
);

create table press(
id int primary key auto_increment,
pname varchar(30),
tel char(11)
);

create table book(
id int primary key auto_increment,
bname varchar(30),
price float,
author_id int,
press_id int,
foreign key(author_id) references author(id),
foreign key(press_id) references press(id)
);

create table author_press(
id int primary key auto_increment,
author_id int,
press_id int,
foreign key(author_id) references author(id),
foreign key(press_id) references press(id)
);