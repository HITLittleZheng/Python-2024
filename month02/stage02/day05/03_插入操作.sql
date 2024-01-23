--按照字段插入记录
insert into class values
(7,"James",17,"m",91),
(8,"Emma",17,"w",93);

--选择字段插入
insert into class (name,age,score) value
("Tonny",18,76),
("Alex",19,84);

insert into class (name,age,sex) value
("Abby",19,'w'),
("Jot",18,'m');

insert into class (name,age,sex) value
("Sunny",1800,'m');

--hobby表数据
insert into hobby
(name,hobby,level,price,remark) values
("Lily","sing,dance","B",45800.888,"骨骼惊奇练舞奇才"),
("Joy","draw","A",24800,"当代达芬奇"),
("Lucy","sing","C",9900,"未来邓丽君");

insert into hobby
(name,hobby,level,price) values
("Lily","draw,dance","B",45000),
("Joy","dance","C",11800);
