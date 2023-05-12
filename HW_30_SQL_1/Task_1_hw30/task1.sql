
CREATE TABLE table_1 (

    name text,
    surname text,
    phone_number integer
);

select * from table_1;

alter table table_1
rename to contacts;

alter table contacts
add email text;

insert into contacts
values ('Rick', 'Rickson', 123456789, 'rickson@mail.com');

insert into contacts
values ('Mick', 'Mickson', 5254545245, 'mickson@mail.com');

insert into contacts
values ('Nick', 'Nickson', 66533243, 'nickson@mail.com');

insert into contacts
values ('Jack', 'Jackson', 986634532, 'jackson@mail.com');

insert into contacts
values ('John', 'Johnson', 23456364353, 'johnson@mail.com');

select ROWID, * from contacts;

update contacts
set email = 'john_johnson@meil.com'
where ROWID = 5;

select ROWID, * from contacts;

insert into contacts
values ('Jack', 'Jefferson', 3532523, 'jeffersom@mail.com');

select * from contacts;

delete from contacts
where name = 'Jack' and surname like 'Jef%';

select * from contacts;