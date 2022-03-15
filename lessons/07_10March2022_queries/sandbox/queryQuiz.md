# Date
10 March 2022

# Title
QueryQuiz

What is the average salary of computer science teachers?

```
SELECT avg(Instructor.salary) FROM Instructor WHERE Instructor.deptName == "CompSci";
```

What is the average salary of computer science teachers who make less than 98000?

```
SELECT avg(Instructor.salary) FROM Instructor WHERE Instructor.deptName == "CompSci" AND Instructor.salary < 98000;
```


---



What are the salaries of instructors who worked during the Spring?

```
SELECT Instructor.ID,Instructor.Name, Instructor.Salary, Teaches.semester FROM Instructor, Teaches WHERE Instructor.ID == Teaches.ID AND Teaches.semester == "Spring" ;
```


What are the salaries of instructors who worked during the Fall?


```
SELECT AVG(Instructor.Salary), Teaches.semester FROM Instructor, Teaches WHERE Instructor.ID == Teaches.ID AND Teaches.semester == "Fall";
```

---

What are the Instructor names and their IDs who taught which Students (show names and IDs)?

```
SELECT instructor.name, instructor.id, instructor.studentID, student.name FROM instructor, student WHERE student.id == instructor.studentID;
```

What are the Instructor names and their IDs who taught which Students (show names and IDs)?

```
SELECT instructor.name, instructor.id, instructor.studentID, student.name FROM instructor, student WHERE student.id == instructor.studentID;
```
---
