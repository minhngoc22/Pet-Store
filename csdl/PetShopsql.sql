CREATE DATABASE PetShop;
USE PetShop;

-- Bảng người dùng
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    passH VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE,
    role ENUM('Customer', 'Nhân viên', 'admin') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Users (username, passH, email, role) VALUES
('kh1', '123', 'nguyena@example.com', 'Customer'),
('nv1', '123', 'tranb@example.com', 'Nhân viên'),
('admin', '123', 'admin@example.com', 'admin');

-- Bảng khách hàng
CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) UNIQUE,
    email VARCHAR(100) UNIQUE,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Customers (name, phone, email, address) VALUES
('Nguyễn Văn A', '0123456789', 'nguyena@example.com', '123 Đường Lê Lợi, Hà Nội'),
('Trần Thị B', '0987654321', 'tranb@example.com', '456 Đường Nguyễn Trãi, TP.HCM');

-- Bảng thú cưng
CREATE TABLE Pets (
    pet_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    species VARCHAR(50),
    breed VARCHAR(100),
    age INT,
    price DECIMAL(10,2),
    status ENUM('Còn hàng', 'Đã bán') DEFAULT 'Còn hàng'
);

INSERT INTO Pets (name, species, breed, age, price, status) VALUES
('Milo', 'Chó', 'Golden Retriever', 2, 12000000.00, 'Còn hàng'),
('Mèo Mun', 'Mèo', 'Xiêm', 1, 7000000.00, 'Đã bán');

-- Bảng sản phẩm
CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock INT DEFAULT 0
);

INSERT INTO Products (name, category, price, stock) VALUES
('Thức ăn cho chó', 'Thực phẩm', 200000.00, 100),
('Đồ chơi cho mèo', 'Đồ chơi', 150000.00, 50);

-- Bảng nhân viên
CREATE TABLE Employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) UNIQUE,
    email VARCHAR(100) UNIQUE,
    position VARCHAR(50),
    salary DECIMAL(10,2)
);

INSERT INTO Employees (name, phone, email, position, salary) VALUES
('Trần Thị B', '0987654321', 'tranb@example.com', 'Quản lý', 15000000.00);

-- Bảng đơn hàng
CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_price DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

INSERT INTO Orders (customer_id, total_price) VALUES
(1, 400000.00),
(2, 750000.00);

-- Bảng chi tiết đơn hàng
CREATE TABLE OrderDetails (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

INSERT INTO OrderDetails (order_id, product_id, quantity, price) VALUES
(1, 1, 2, 400000.00),
(2, 2, 5, 750000.00);
