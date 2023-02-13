-- Creating second  table and store data into them
CREATE TABLE IF NOT EXISTS second_table(
id INT,
name VARCHAR(256),
score INT
);

INSERT INTO second_table(id, name, score)
VALUES (1, "Bob", 14), (2, "John", 10), (3,"George", 8), (4, "Alex", 3)
