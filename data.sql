CREATE TABLE students (
    id INT IDENTITY PRIMARY KEY,
    class INT,
    rollnumber INT,
    marks DECIMAL(5, 2)
);
INSERT INTO students (class, rollnumber, marks) VALUES (10, 101, 85.5);
INSERT INTO students (class, rollnumber, marks) VALUES (9, 202, 92.0);
INSERT INTO students (class, rollnumber, marks) VALUES (11, 303, 78.3);
INSERT INTO students (class, rollnumber, marks) VALUES (12, 404, 91.7);
INSERT INTO students (class, rollnumber, marks) VALUES (10, 505, 67.8);
INSERT INTO students (class, rollnumber, marks) VALUES (9, 606, 88.9);
INSERT INTO students (class, rollnumber, marks) VALUES (11, 707, 76.2);
INSERT INTO students (class, rollnumber, marks) VALUES (12, 808, 94.5);
INSERT INTO students (class, rollnumber, marks) VALUES (10, 909, 72.1);
INSERT INTO students (class, rollnumber, marks) VALUES (9, 111, 89.0);
INSERT INTO students (class, rollnumber, marks) VALUES (11, 222, 65.4);
INSERT INTO students (class, rollnumber, marks) VALUES (12, 333, 92.8);
INSERT INTO students (class, rollnumber, marks) VALUES (10, 444, 73.6);
INSERT INTO students (class, rollnumber, marks) VALUES (9, 555, 88.7);
INSERT INTO students (class, rollnumber, marks) VALUES (11, 666, 70.9);
INSERT INTO students (class, rollnumber, marks) VALUES (12, 777, 95.2);
INSERT INTO students (class, rollnumber, marks) VALUES (10, 888, 79.4);
INSERT INTO students (class, rollnumber, marks) VALUES (9, 999, 91.1);
INSERT INTO students (class, rollnumber, marks) VALUES (11, 121, 84.6);
INSERT INTO students (class, rollnumber, marks) VALUES (12, 232, 68.7);

-- Create the finance table
CREATE TABLE finance (
    transaction_id INT PRIMARY KEY,
    date DATE,
    description VARCHAR(255),
    amount DECIMAL(10, 2),
    account_id INT
);

-- Insert random data into the finance table
INSERT INTO finance (transaction_id, date, description, amount, account_id)
VALUES
    (1, '2023-01-15', 'Groceries', 75.50, 101),
    (2, '2023-01-18', 'Gasoline', 45.25, 102),
    (3, '2023-01-20', 'Restaurant', 85.75, 103),
    (4, '2023-02-02', 'Utilities', 120.00, 104),
    (5, '2023-02-05', 'Rent', 1500.00, 105),
    (6, '2023-02-10', 'Clothing', 62.99, 101),
    (7, '2023-03-03', 'Electronics', 399.99, 102),
    (8, '2023-03-10', 'Entertainment', 25.00, 103),
    (9, '2023-03-15', 'Insurance', 200.00, 104),
    (10, '2023-03-20', 'Medical', 75.50, 105);
