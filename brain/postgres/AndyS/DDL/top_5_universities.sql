DROP TABLE IF EXISTS project_two.Top_5_Universities;
CREATE TABLE project_two.Top_5_Universities AS
SELECT *
FROM project_two.Global_Exchange_Universities
ORDER BY Overall_QS_Rank
LIMIT 5; 