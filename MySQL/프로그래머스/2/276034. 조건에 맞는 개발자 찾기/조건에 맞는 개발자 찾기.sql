-- 코드를 작성해주세요
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS
WHERE (SKILL_CODE & (SELECT CODE
                   FROM SKILLCODES
                   WHERE NAME = 'Python')) = (SELECT CODE
                   FROM SKILLCODES
                   WHERE NAME = 'Python') OR
                   (SKILL_CODE & (SELECT CODE
                   FROM SKILLCODES
                   WHERE NAME = 'C#')) = (SELECT CODE
                   FROM SKILLCODES
                   WHERE NAME = 'C#')
ORDER BY ID;
                   
