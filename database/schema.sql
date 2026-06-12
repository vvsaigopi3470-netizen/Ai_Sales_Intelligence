CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(50) DEFAULT 'Employee',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products(
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(150),
    category VARCHAR(100),
    price DOUBLE,
    stock INT,
    supplier VARCHAR(100)
);

CREATE TABLE customers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(150),
    city VARCHAR(100),
    phone VARCHAR(20)
);

CREATE TABLE sales(
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    customer_id INT,
    quantity INT,
    revenue DOUBLE,
    sale_date DATE,

    FOREIGN KEY(product_id)
    REFERENCES products(id),

    FOREIGN KEY(customer_id)
    REFERENCES customers(id)
);

CREATE TABLE inventory(
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    stock_level INT,
    reorder_point INT,

    FOREIGN KEY(product_id)
    REFERENCES products(id)
);