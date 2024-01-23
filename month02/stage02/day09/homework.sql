函数练习：
books表完成 ，编写一个函数，传入两本书的名字，
得到两本书的价格之差

delimiter $$
create function get_price(book1 varchar(30),book2 varchar(30))
returns float
begin
  declare p1 float;
  declare p2 float;
  set p1=(select price from books where bname=book1);
  set p2=(select price from books where bname=book2);
  return p1-p2;
end $$
delimiter ;



存储过程练习：
books表，使用存储过程完成，
将2020年以前出版的图书价格增加3元，
参数传入一个作家的名字，将该作家的图书，
在此基础上再涨2元，
按照图书价格打印出图书信息，
只要书名，作者和价格即可

delimiter $$
create procedure change_price(IN name varchar(30))
begin
   update books set price=price+3 where publish_time < "2020-01-01";
   update books set price=price+2 where author=name;
   select bname,author,price from books order by price;
end $$
delimiter ;

