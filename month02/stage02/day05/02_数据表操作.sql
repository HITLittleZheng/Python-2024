--创建一个数据表
create table student(
name char(30),
sex enum("男","女"),
age tinyint,
height float
);

--查看创建的数据表
show tables;

--class数据表
create table class(
id int primary key auto_increment,
name varchar(30) not null,
age tinyint unsigned,
sex enum("m","w","o"),
score float default 0
);

CREATE TABLE `class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `age` tinyint(3) unsigned DEFAULT NULL,
  `sex` enum('m','w','o') DEFAULT NULL,
  `score` float DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


create table hobby(
id int primary key auto_increment,
name varchar(30) not null,
hobby set("sing","dance","draw"),
level char comment "A,B or C",
price decimal(7,2),
remark text
);

--查看字段信息
desc class;

--查看数据表创建语句
show create table class;



