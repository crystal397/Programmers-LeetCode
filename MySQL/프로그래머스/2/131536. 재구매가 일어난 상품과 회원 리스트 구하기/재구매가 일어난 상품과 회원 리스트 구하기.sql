-- 중복값을 찾기 위해 
-- 먼저, GROUP BY로 필요한 조건을 묶고
-- 묶은 그룹 중 중복이 1보다 큰 경우(= 중복되었다고 간주)를 출력하였습니다.

SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) > 1
ORDER BY USER_ID, PRODUCT_ID DESC
