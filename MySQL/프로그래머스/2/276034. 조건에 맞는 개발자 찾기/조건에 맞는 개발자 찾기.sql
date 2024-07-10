-- 직관적으로, 비트연산 &를 이용해서 파이썬을 사용하거나 C#을 사용하는 사람인지 파악하였습니다.
-- 조인 또는 with 문을 사용하여 추후 업데이트 예정입니다.

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
                   
