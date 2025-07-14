DROP TABLE IF EXISTS project_two.Best_University_Per_Country;
CREATE TABLE project_two.Best_University_Per_Country AS
SELECT DISTINCT ON (Country) *
FROM project_two.Global_Exchange_Universities
ORDER BY Country, Overall_QS_Rank; 