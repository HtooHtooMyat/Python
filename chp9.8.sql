
create table parents (
ID_Number  number,
house  varchar2 (30));

create table kid (
Kid_Id   number,
House  varchar2 (30));

insert into parents values (1, 'Oak');
insert into parents  values (2, 'Elm');
insert into Kid values (10, 'Maple');
insert into Kid values (20, 'Elm');
select * from parents;
select * from kid;
select * from parents where house  in (select House from kid);

select * from parents where house  not in (select House from kid);
insert into kid values (30,Null);
select * from parents where house  not in (select House from kid where house is not null);
