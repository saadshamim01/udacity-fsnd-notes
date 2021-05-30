create table person_table(

    id bigserial not null primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    gender varchar(10) not null,
    date_of_birth timestamp not null,
    email varchar(150) not null
    );


insert into person_table(
    first_name,
    last_name,
    gender,
    date_of_birth,
    email
    )
Values ('Anne', 'Smith', 'FEMALE', '01-01-1998', 'anne@gmail.com');

insert into person_table(
    first_name,
    last_name,
    gender,
    date_of_birth,
    email
    )
Values ('Saad', 'Shamim', 'MALE', '01-01-1998', 'saadshamim01@gmail.com');

