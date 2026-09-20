# 🗄️ 資料庫 Ch07: 進階 SQL 查詢與視圖操作 (Advanced SQL, Views & Triggers)

> **授課教師**：陳士杰 教授  
> **教材對齊**：`Course 6. SQL`, `MySQL_Ch3.pdf`, `MySQL_Ch4.pdf`  
> **核心主題**：分組聚合 (`GROUP BY`, `HAVING`)、子查詢 (`IN`, `EXISTS`, Correlated Subquery)、多表結合 (`LEFT/RIGHT OUTER JOIN`)、視圖 (View) 定義與可更新性限制、觸發程序 (Triggers) 與預存程序 (Stored Procedures)

---

## 1. 分組聚合進階語法 (`GROUP BY` & `HAVING`)

```sql
SELECT Dno, COUNT(*) AS EmpCount, AVG(Salary) AS AvgSal
FROM EMPLOYEE
WHERE Salary > 30000          -- 1. WHERE: 針對原始單筆資料列進行過濾
GROUP BY Dno                  -- 2. GROUP BY: 依部門分組
HAVING COUNT(*) >= 3          -- 3. HAVING: 針對分組聚合後的統計結果進行過濾
ORDER BY AvgSal DESC;         -- 4. ORDER BY: 排序輸出
```

> [!WARNING]
> **SQL 關鍵陷阱**：
> `WHERE` 子句中**絕對不能包含聚合函數**（如 `WHERE AVG(Salary) > 50000` 是語法錯誤），必須使用 `HAVING AVG(Salary) > 50000`！

---

## 2. 巢狀子查詢 (Nested Subqueries)

1. **集合成員檢定 (`IN`, `NOT IN`)**：
   ```sql
   SELECT Lname, Fname FROM EMPLOYEE
   WHERE Dno IN (SELECT Dnumber FROM DEPARTMENT WHERE Dname = 'Research');
   ```
2. **存在性檢定 (`EXISTS`, `NOT EXISTS`)**：
   - 相關子查詢 (Correlated Subquery)：內部子查詢參照了外部查詢的欄位，對外部每筆資料列執行一次：
   ```sql
   -- 查詢參與了所有由部門 5 主辦之專案的員工姓名 (對應關聯代數除法)
   SELECT E.Fname, E.Lname FROM EMPLOYEE E
   WHERE NOT EXISTS (
       SELECT P.Pnumber FROM PROJECT P WHERE P.Dnum = 5
       AND NOT EXISTS (
           SELECT * FROM WORKS_ON W 
           WHERE W.Essn = E.Ssn AND W.Pno = P.Pnumber
       )
   );
   ```

---

## 3. 外結合 (Outer Joins)

一般 Inner Join 只保留兩表皆有配對成功的元組。若需保留未配對資料：
- **`LEFT OUTER JOIN`**：左表資料全數保留，右表若無配對則補 `NULL`。
- **`RIGHT OUTER JOIN`**：右表資料全數保留，左表無配對補 `NULL`。
- **`FULL OUTER JOIN`**：兩表資料全數保留，任一方無配對皆補 `NULL`。

---

## 4. 視圖 (View) 與安全性

視圖是儲存在資料庫中的**虛擬表格 (Virtual Table)**，由一段 SQL 查詢定義而成，資料庫內部通常不實體儲存資料（除非為 Materialized View）。

```sql
CREATE VIEW Dept_Sal_Summary AS
SELECT D.Dname, COUNT(E.Ssn) AS TotalEmp, SUM(E.Salary) AS TotalSalary
FROM DEPARTMENT D JOIN EMPLOYEE E ON D.Dnumber = E.Dno
GROUP BY D.Dname;
```

### 視圖的可更新性 (Updatable Views) 限制：
若視圖包含以下元素，**嚴禁**透過視圖執行 `INSERT` / `UPDATE` / `DELETE`：
1. 包含聚合函數 (`SUM`, `AVG`, `COUNT`, `MAX`, `MIN`)。
2. 包含 `GROUP BY` 或 `HAVING` 子句。
3. 包含 `DISTINCT` 關鍵字。
4. 定義自多個表格的結合 (Join)，除非符合單一基表的主鍵映射規範。

---

## 5. 觸發程序與預存程序 (Triggers & Stored Procedures)

- **觸發程序 (Trigger)**：事件驅動 (Event-driven, ECA 規則：Event-Condition-Action)。當特定表格發生 `INSERT`, `UPDATE`, `DELETE` 時自動觸發執行，用於維護複雜業務邏輯與稽核日誌。
- **預存程序 (Stored Procedure)**：預先編譯並儲存在 DB 伺服器端的 SQL 程式碼塊，減少網路傳輸開銷，提升執行效能。

---

## 🎯 課堂速記與期末考檢核重點

> [!TIP]
> 1. **SQL 綜合大題**：手寫包含多表關聯、相關子查詢、`GROUP BY` 與 `HAVING` 之完整 SQL 敘述。
> 2. **View 可更新性判別**：給定一個 View 定義，解釋使用者能否透過此 View 執行 `UPDATE`。

```markdown
<!-- 上課重點即時填寫區 -->
> [!note] 課堂速記 (隨堂記錄陳老師補充)
> - 
```
