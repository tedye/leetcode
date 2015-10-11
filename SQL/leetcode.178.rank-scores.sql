# Write your MySQL query statement below
 SELECT Score,  (SELECT COUNT(DISTINCT(Score)) FROM  Scores b WHERE b.Score > a.Score) + 1 AS Rank
       FROM Scores a
       ORDER by Score DESC