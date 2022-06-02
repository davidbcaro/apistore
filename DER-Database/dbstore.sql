create database dbstore;
use dbstore;

create table Product(
product_id int primary key,
name varchar(191) not null,
product_description varchar(191) not null,
price double not null
);

create table `Order`(
order_id int primary key,
fk_customer_id int not null,
creation_date date not null,
delivery_address varchar (191) not null,
total double not null
);

create table Customer(
customer_id int primary key,
name varchar(191) not null,
email varchar(191) not null
);

create table Customer_product(
fk_customer_id int not null,
fk_product_id int not null
);

create table Order_detail(
order_detail_id int primary key,
fk_order_id int not null,
fk_product_id int not null,
quantity int not null
);

alter table Customer_product add constraint fk_customer foreign key (fk_customer_id) references Customer (customer_id);
alter table Customer_product add constraint fk_product foreign key (fk_product_id) references Product (product_id);
alter table Customer_product add constraint fk_customer_product primary key (fk_customer_id, fk_product_id);
alter table `Order` add constraint fk_customer_id foreign key (fk_customer_id) references Customer (customer_id);
alter table Order_detail add constraint fk_order_id foreign key (fk_order_id) references `Order` (order_id);
alter table Order_detail add constraint fk_product_id foreign key (fk_product_id) references Product (product_id);