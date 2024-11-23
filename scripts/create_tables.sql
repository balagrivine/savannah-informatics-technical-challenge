-- This script creates sql tables in the database


-- Create a customers table if it does not exist in the db
CREATE TABLE IF NOT EXISTS customers (
	id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR(100) UNIQUE NOT NULL,
	password VARCHAR(200),
	shipping_address VARCHAR(100) NOT NULL,
	created_at DATE DEFAULT NOW()
);

-- Create a products table if it does not exist in the db
CREATE TABLE IF NOT EXISTS products (
	id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	description VARCHAR(200) NOT NULL,
	price DECIMAL(10, 2) NOT NULL,
	stock_quantity INTEGER DEFAULT 0
);

-- Create an orders table if it does not exist in the db
CREATE TABLE IF NOT EXISTS orders (
	id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	order_date DATE NOT NULL,
	price DECIMAL(10, 2) NOT NULL,
	customer_id INTEGER,
	FOREIGN KEY (customer_id) REFERENCES customers (id)
);

-- Create an order_details tale if it does not exist in the db
CREATE TABLE IF NOT EXISTS order_details (
	id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	order_id INTEGER NOT NULL,
	product_id INTEGER NOT NULL,
	quantity INTEGER DEFAULT 0,
	FOREIGN KEY (order_id) REFERENCES orders (id),
	FOREIGN KEY (product_id) REFERENCES products (id)
);
