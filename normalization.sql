
CREATE DATABASE college_db;
USE college_db;

CREATE TABLE StudentCourse_1NF (
    student_id INT NOT NULL,
    student_name VARCHAR(50) NOT NULL,
    course VARCHAR(50) NOT NULL,
    PRIMARY KEY (student_id, course)
);

SELECT * FROM StudentCourse_1NF;