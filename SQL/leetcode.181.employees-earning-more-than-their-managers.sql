# Write your MySQL query statement below
SELECT Name AS Employee 
    FROM Employee e 
    WHERE e.ManagerId IS NOT NULL AND e.Salary > (SELECT Salary 
                          FROM Employee 
                          WHERE e.ManagerId = Id)