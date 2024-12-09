CREATE TABLE sales_data (
    id INTEGER PRIMARY KEY,
    product TEXT NOT NULL,
    total_sales INTEGER NOT NULL,
    year INTEGER NOT NULL,
    region TEXT NOT NULL
);

INSERT INTO sales_data (product, total_sales, year, region) VALUES
('Barbie Doll', 5000, 2023, 'North America'),
('Sofa Covers', 3000, 2023, 'North America'),
('Coffee Mug', 4500, 2023, 'North America'),
('Pillows', 2000, 2022, 'Europe'),
('Sneakers', 6000, 2023, 'North America'),
('Headphones', 5000, 2023, 'North America'),
('Backpack', 3000, 2023, 'North America'),
('Suitcase', 4500, 2023, 'North America'),
('Detergent', 2000, 2022, 'Europe'),
('Soap', 6000, 2023, 'North America');

CREATE TABLE inventory (
    id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    stock INTEGER NOT NULL
);

INSERT INTO inventory (product_name, stock) VALUES
('Waterbottle', 45),
('Macbook Pro', 60),
('Coffee Thermos', 30),
('Blanket', 25),
('Vitamins', 10),
('Macbook Air', 60),
('Tea', 39),
('Lamp', 21),
('Charger', 24);


CREATE TABLE accounts (
    id INTEGER PRIMARY KEY,
    account_holder TEXT NOT NULL,
    balance REAL NOT NULL,
    currency TEXT NOT NULL,
    region TEXT NOT NULL
);

INSERT INTO accounts (account_holder, balance, currency, region) VALUES
('Account A', 15000.00, 'USD', 'Europe'),
('Account B', 12000.00, 'USD', 'Europe'),
('Account C', 8000.00, 'USD', 'Europe'),
('Account D', 17000.00, 'USD', 'Asia'),
('Account E', 20000.00, 'USD', 'North America'),
('Account F', 12000.00, 'USD', 'North America'),
('Account G', 88000.00, 'USD', 'North America'),
('Account H', 170000.00, 'USD', 'Asia');


CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
);

INSERT INTO employees (name, age) VALUES
('Alice Smith', 35),
('Bob Johnson', 40),
('Charlie Brown', 32),
('David White', 28),
('Don Green', 29),
('Sally Trinity', 21),
('Sarah Fash', 23),
('Eve Black', 50);

CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    active BOOLEAN NOT NULL
);

INSERT INTO customers (name, email, active) VALUES
('John Doe', 'john.doe@example.com', true),
('Jane Smith', 'jane.smith@example.com', true),
('Emily Davis', 'emily.davis@example.com', false),
('Michael Brown', 'michael.brown@example.com', true),
('Emma Wilson', 'emma.wilson@example.com', true),
('Aaron Lilac', 'a.lilac@example.com', true),
('Mike Roger', 'mike.r@example.com', true),
('Izzy Tike', 'izzy.tike@example.com', true);
