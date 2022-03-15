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




sqlite> select * from Instructor;
10101|Miller|S1|CompSci|90000
10102|Johnson|S1|CompSci|90000
10103|Charleson|S2|CompSci|70000
10104|Thompson|S2|CompSci|100000
10105|Mauler|S3|Math|99000
10106|Jackson|S3|CompSci|98000
10107|Chesterfield|S3|CompBio|97000
10108|Jenkins|S4|CompBio|101000
10109|William|S4|Math|99000
10110|Watson|S4|CompSci|98000
10111|Nelson|S5|CompBio|97000
10112|Farber|S5|CompBio|101000


sqlite> select * from Student;
xS10|Ralph|CompSci|3
xS11|Emory|CompSci|3
xS12|Jameson|CompSci|3
S1|Michaels|CompSci|3
S2|Peterson|CompSci|3
S3|Mullen|CompSci|4
S4|Scotts|CompSci|2
S5|Beuller|CompSci|1


sqlite> select * from Teaches;
10101|CS-101|1|Fall|2009
10101|CS-201|1|Spring|2010
10101|CS-301|1|Fall|2009
10101|CS-401|1|Fall|2009
10101|CS-102|1|Fall|2009
10102|CS-202|1|Spring|2010
10103|CS-302|1|Fall|2010
10104|CS-402|1|Spring|2011
10104|CS-502|1|Fall|2016
10105|CS-604|1|Spring|2016


Q: What are the Instructor names and their IDs who taught which Students (show names and IDs)?

A:
```
SELECT instructor.name, instructor.id, instructor.studentID, student.name FROM instructor, student WHERE student.id == instructor.studentID;
```
---

Q: What are the Instructor names and their IDs who taught which Students (show names and IDs) for classes taught in the year 2010?


Structured Query:
  SELECT
	teaches.year, instructor.name, instructor.id, instructor.studentID, student.name
FROM
	instructor, student, Teaches
WHERE
	student.id == instructor.studentID
	AND
	teaches.ID = Instructor.ID
	AND
	teaches.year == "2010";

Query:
```
SELECT teaches.year, instructor.name, instructor.id, instructor.studentID, student.name FROM instructor, student, Teaches WHERE student.id == instructor.studentID AND teaches.ID = Instructor.ID AND teaches.year == "2010";
```
Output:
```
2010|Miller|10101|S1|Michaels
2010|Johnson|10102|S1|Michaels
2010|Charleson|10103|S2|Peterson
```

---

Q: What are the Instructor names and their IDs who taught which Students (show names and IDs) for classes taught in the year 2010. In which semester were they teaching?

Structured query:

  SELECT
	teaches.year, teaches.semester, instructor.name, instructor.id, instructor.studentID, student.name
FROM
	instructor, student, Teaches
WHERE
	student.id == instructor.studentID
	AND
	teaches.ID = Instructor.ID
	AND
	teaches.year == "2010";


Query:
```
  SELECT teaches.year, teaches.semester, instructor.name, instructor.id, instructor.studentID, student.name FROM instructor, student, Teaches WHERE student.id == instructor.studentID AND teaches.ID = Instructor.ID AND teaches.year == "2010";
```

Output:
```
2010|Spring|Miller|10101|S1|Michaels
2010|Spring|Johnson|10102|S1|Michaels
2010|Fall|Charleson|10103|S2|Peterson
```


---
