--create table Id_not_null CANNOT BE NULL ID
CREATE TABLE IF NOT EXISTS Id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);