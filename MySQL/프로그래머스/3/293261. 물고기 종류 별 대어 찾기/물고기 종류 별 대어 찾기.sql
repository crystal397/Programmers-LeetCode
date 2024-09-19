# -- 코드를 작성해주세요
SELECT B.ID, A.FISH_NAME, B.LENGTH
FROM FISH_NAME_INFO A
LEFT JOIN (
    SELECT a.ID, a.FISH_TYPE, a.LENGTH
    FROM FISH_INFO a
    INNER JOIN (
        SELECT FISH_TYPE, MAX(LENGTH) AS LENGTH
        FROM FISH_INFO
        GROUP BY FISH_TYPE) b
    ON a.FISH_TYPE = b.FISH_TYPE and a.LENGTH = b.LENGTH
    ) B                                                               
ON A.FISH_TYPE = B.FISH_TYPE
ORDER BY A.ID