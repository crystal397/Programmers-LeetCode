-- DATE format을 YYYY-MM-DD 형식으로의 변환을 위해, date_format(DATE, '%Y-%m-%d')를 사용하였으며 
--              YYYY만 추출해서 값 비교를 위해, YEAR(DATE)를 사용하였습니다.

SELECT BOOK_ID, date_format(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK
WHERE YEAR(PUBLISHED_DATE) = '2021' 
    AND CATEGORY = "인문"
ORDER BY PUBLISHED_DATE
