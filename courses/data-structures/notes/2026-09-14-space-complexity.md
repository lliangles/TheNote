別擔心，第一章筆記會亂是正常的，因為它把「軟體開發概念」和「演算法分析數學」混在一起。你現在老師上到 1.7 The Criteria to Judge a Program，其實就是準備從「寫程式」進入「分析程式好壞」。我幫你把第一章主線和 1.7 重新串一次，你對照筆記看就會清楚很多。

---

第一章主線

系統生命週期 → ADT → 演算法 → 遞迴 → 效能分析（1.7）

前面那些 Requirements、Analysis、Design，你只要知道：

· Requirements：規格、輸入、輸出
· Analysis：Bottom-up 探索型；Top-down 高階規劃，複雜系統常用
· Design：建立 ADT，和語言無關
· Refinement & Coding：資料表示法會影響效率
· Verification：正確性證明、測試、除錯

ADT 重點一句話：

把「規格」和「實作」分開，使用者只要知道怎麼用，不需要知道裡面怎麼做。

演算法五特性：
Input、Output、Definiteness、Finiteness、Effectiveness。
其中 Program 在計算理論上不一定要滿足 Finiteness，但演算法要。

遞迴：

· 直接遞迴：自己叫自己
· 間接遞迴：A 叫 B，B 再叫 A
· 一定要有終止條件
· 漢諾塔：moves(n) = 2^n - 1

---

1.7 到底在幹嘛？

1.7 在講兩件事：

1. 判斷一個程式好不好

老師列的標準：

· 是否符合原始規格？
· 是否正確？
· 有沒有文件說明怎麼用、怎麼運作？
· 有沒有有效使用函式來建立邏輯單位？
· 程式碼可讀嗎？
· 有沒有有效使用主要/次要儲存？
· 執行時間可接受嗎？

這些是「質化」標準。接下來就進入「量化」分析：Performance Analysis。

---

Performance Analysis：空間複雜度 + 時間複雜度

空間複雜度 Space Complexity

公式：

```
S(P) = c + Sp(I)
```

· c：固定部分，和輸入大小無關。例如指令空間、簡單變數、常數。
· Sp(I)：變動部分，和問題實例有關。例如遞迴的堆疊、動態配置的陣列。
· I：instance characteristics，問題實例特徵。

例子：

```cpp
float abc(float a, float b, float c) {
    return a + b + b*c + (a+b-c)/(a+b) + 4.0;
}
```

沒有陣列、沒有遞迴，所以 Sabc(I) = 0。

```cpp
float sum(float list[], int n) {
    float s = 0;
    for (int i = 0; i < n; i++)
        s += list[i];
    return s;
}
```

· 在 Pascal：陣列會複製一份，所以 Ssum(n) = n。
· 在 C：陣列不複製，只傳位址，所以 Ssum(n) = 0。

遞迴版：

```cpp
float rsum(float *a, const int n) {
    if (n <= 0) return 0;
    else return rsum(a, n-1) + a[n-1];
}
```

每次遞迴會在 stack 放：float a、const int n、return value、return address，共約 16 bytes。遞迴 n+1 次，所以空間約 16n 或 4(n+1)。總之是 O(n)。

時間複雜度 Time Complexity

時間複雜度不是真的去量秒數，而是算 step count。

· 一個 step 可以是一個表達式、賦值、函式呼叫、for/while、return 等。
· if-else、switch-case 可能算多個 step。
· 精確算很麻煩，所以用 Asymptotic Notation。

三種情況：

· Best-case：最少步數
· Worst-case：最多步數
· Average-case：平均步數

漸進記號

· Big O：上界，f(n) = O(g(n))，表示 f 不會長得比 g 快太多。
· Omega：下界，f(n) = Ω(g(n))。
· Theta：緊確界，上下界夾住，f(n) = Θ(g(n))。

例子：

· 3n+2 = O(n)，取 c=4, n0=2。
· 10n²+4n+2 = O(n²)，取 c=11, n0=5。
· 3n+2 = Θ(n)，因為 3n ≤ 3n+2 ≤ 4n。

成長速率排序：

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
```

---

你筆記裡容易看不懂的地方

1. Selection sort
   · 概念：每輪找未排序中最小的，放到前面。
   · 程式碼中 min = i，內層找 list[j] < list[min]，最後 SWAP(list[i], list[min])。
   · 時間複雜度：O(n²)。
2. COMPARE 函式/巨集
   · 回傳 -1、0、1 代表小於、等於、大於。
   · 巨集寫法要注意括號：((x) < (y)) ? -1 : ((x) == (y)) ? 0 : 1。
3. 遞迴 binary search
   · 用 if (left <= right)，不是 while。
   · 中間比較後，左半或右半再遞迴呼叫自己。
4. Permutation
   · 把每個元素輪流放到位置 i，再遞迴處理 i+1 之後。
   · 記得換回來（backtracking）。
   · 你的筆記中 cout<<list[j]); 多了一個 )。
5. rsum 空間
   · 遞迴每次呼叫會佔 stack，所以空間是 O(n)。
   · 不是 0，因為有遞迴堆疊。

---

你現在只要先記這 5 句

1. ADT = 規格與實作分離。
2. 演算法五特性：Input、Output、Definiteness、Finiteness、Effectiveness。
3. 空間複雜度 = 固定部分 + 變動部分；遞迴通常會增加堆疊空間。
4. 時間複雜度用 step count 估，再看 Big O / Omega / Theta。
5. 成長速率：常數 < log < n < n log n < n² < n³ < 2ⁿ < n!。

老師現在上 1.7，接下來應該會進到 Time Complexity 的 step count 計算、Asymptotic Notation，然後可能帶 Towers of Hanoi 的遞迴分析。你如果把「空間複雜度公式」和「Big O 定義」先弄懂，後面就會順很多。

你要不要告訴我，1.7 裡面是「空間複雜度例子」還是「Big O 數學定義」最卡？我可以針對那個再講白話一點。











Space Complexity Examples (2)
float rsum (float * a, const int n) {
    if (n <= 0) return 0 ;
	else return (rsum(a, n-1) + a[n-1]) ; 
}
It will run n times recursion (n+1 times).
Space needed in a recursion in stack (16 bytes)
float a: 4 bytes
const int n: 4 bytes
return value:4 bytes
return address: 4 bytes
Srsum(n)=16n //or =4(n+1)

~29

# step count（步數計算） 
的經典例子，老師上課說「for 有可能沒記錄到所以多寫一個 count」指的就是：迴圈條件判斷最後一次失敗（跳出迴圈）的那一次，沒有被迴圈裡面的 count++ 算到，所以要在迴圈外面補一個 count++。
#會考
我們把程式碼拆開，一行一行對應：

```cpp
float sum (float *a, int n) { /* 2n + 3 */
    float s = 0; 
    int i;
    count++;                     // ① 初始化
    for (i = 0; i < n; i++) {
        count++;                 // ② 迴圈條件檢查（成功進入迴圈）
        s += a[i];
        count++;                 // ③ 迴圈內的賦值
    }
    count++;                     // ④ 迴圈條件檢查（最後一次失敗）
    count++;                     // ⑤ return
    return s;
}
```

各步驟對應：

· ① 第一個 count++：代表初始化。float s = 0; 和 int i; 通常宣告不算執行步數，但 i = 0 或 s = 0 這種賦值算 1 步。這裡把整個初始化算成 1 步。
· ② 迴圈內的 count++：每次 i < n 成立、進入迴圈時執行一次。因為迴圈體總共執行 n 次，所以這裡會被執行 n 次。
· ③ s += a[i] 後面的 count++：代表迴圈內部的賦值動作，執行 n 次。
· ④ 迴圈結束後的 count++：當 i 增加到 n 時，i < n 會變成 false，迴圈結束。這次條件檢查沒有進入迴圈，所以迴圈裡面的 count++ 不會記錄到它。因此要在迴圈外面補一個 count++，代表「最後一次條件判斷失敗」。
· ⑤ 最後的 count++：代表 return s; 這個返回動作，執行 1 次。

加總：

· 初始化：1 步
· 迴圈條件檢查：n 次成功 + 1 次失敗 = n + 1 步
· 迴圈內賦值：n 步
· return：1 步

總步數 = 1 + (n + 1) + n + 1 = 2n + 3

所以 2n + 3 就是這樣來的。

> [!NOTE]
> 小提醒：
> 
> 有些教材會把 i++ 也單獨算一步，或把 for 的初始化、條件、增量合併計算，所以不同書可能得到不同係數。但這裡老師的算法是：初始化 1 步、條件判斷 n+1 步、迴圈本體 n 步、return 1 步，總共 2n+3。你只要跟著這個邏輯，考試時就不會亂掉。

你這個遞迴 rsum 的步數計算，老師說是 2n+2，其實就是把「呼叫次數」乘上「每次呼叫的步數」。我們慢慢拆開來看。

---
#？

1. 這個遞迴總共會被呼叫幾次？

rsum(a, n) 的邏輯是：

· 如果 n <= 0，直接回傳 0。
· 否則回傳 rsum(a, n-1) + a[n-1]。

所以當你一開始呼叫 rsum(a, n)，它會依序呼叫：

```
rsum(a, n)
rsum(a, n-1)
rsum(a, n-2)
...
rsum(a, 1)
rsum(a, 0)
```

總共呼叫了 n+1 次（從 n 到 0，包含 0 那次）。

這就是老師說的「遞迴是 n+1」的意思：遞迴呼叫的次數是 n+1 次。

---

2. 每一次呼叫裡面有幾步？

看程式碼中老師標記 count++ 的地方：

```cpp
float rsum (float *a, int n) {
    count++ ; /* for if conditional  */   // 第 1 步：判斷 n <= 0
    if (n <= 0) {
        count++ ; /* for return */        // 第 2 步：return 0
        return 0 ;
    }
    else {
        count++ ; /* for return  */       // 第 2 步：return ...
        return (rsum(a, n-1) + a[n-1]) ;
    }
}
```

不管 n 是多少，每次呼叫都會：

1. 執行一次 if 條件判斷 → 1 步
2. 執行一次 return（不管是回傳 0 還是回傳遞迴結果）→ 1 步

所以每一次呼叫固定貢獻 2 步。

注意：return 裡面的 rsum(a, n-1) + a[n-1] 這個加法、陣列存取，在這個簡化模型中都沒有另外算步數，老師只計算有標 count++ 的地方。所以每次就是 2 步。

---

3. 總步數 = 呼叫次數 × 每次步數

· 呼叫次數：n+1 次
· 每次步數：2 步

所以總步數：

```
(n + 1) × 2 = 2n + 2
```

這就是 2n+2 的由來。

---

4. 遞推式展開也一樣

老師寫的遞推：

```
t_rsum(n) = 2 + t_rsum(n-1)   , n > 0
t_rsum(0) = 2
```

意思是：

· 處理 n 個元素時，先花 2 步（這次呼叫的條件判斷和 return），然後還要去處理 n-1 的遞迴。
· 當 n=0 時，只花 2 步就結束。

展開：

```
t_rsum(n) = 2 + t_rsum(n-1)
          = 2 + 2 + t_rsum(n-2)
          = 2*2 + t_rsum(n-2)
          = 2*3 + t_rsum(n-3)
          ...
          = 2*n + t_rsum(0)
          = 2n + 2
```

所以結果一樣是 2n+2。

---

5. 白話總結

· 這個遞迴從 n 一路呼叫到 0，總共呼叫 n+1 次。
· 每次呼叫都固定做兩件事：判斷 n <= 0、執行 return。
· 所以總步數 = (n+1) * 2 = 2n+2。
· 老師說的「遞迴是 n+1」就是指呼叫次數，不是步數。
· 遞推式只是另一種算法，結果相同。

這樣應該就清楚為什麼是 2n+2 了。如果還有哪一行卡住，再告訴我。
# 矩陣

上面還有問題等等解，但這題

``` cpp 
void add (int **a, int **b, int **c, int m, int n){
	int i, j;
	for (i = 0; i < m; i++)     {
		count++ ; /* for i for loop */ 
		for (j = 0; j < n; j++)     {
			count++ ; /* for j for loop */
			c[i][j] = a[i][j] + b[i][j] ;
			count++ ; /* for assignment  */ 
		} 
		count++ ; /* last time of j for loop */
	}
	count++ ; /* last time of i for loop */
} 

````

時間複雜度為2m(2n+2)+1，嗎？
然後後面幫我原文對照翻譯+解釋（從please.34開始
Summary of Step

- The number of steps is itself a function of the instance characteristics.
- Any specific instance may have several characteristics.
- We need to know exactly which characteristics of the problem instance are to be used.
- A step is any computation unit that is independent of the characteristics. 

Asymptotic Notation

Motivation to determine step counts
Compare the time complexities of two programs that compute the same function.
Predict the growth in run time as the instance characteristics change.
Example: Binary search
Successful search
Unsuccessful search
Asymptotic notation
Determine the exact step count is very difficult. 

Three Kinds of Step Counts
	Best-case
	The minimum number of steps that can be executed for the given parameters.
	蒙地卡羅演算法
	Worst-case
	The maximum number of steps that can be executed for the given parameters.
		如何找到
		
	Average-case
	The average number of steps that can be executed with the given parameters.
Big O（大 O 符號）是用來描述演算法在最壞情況下時間複雜度（或空間複雜度）的上界。 根據投影片的定義，當我們說 \(f(n) = O(g(n))\) 時，代表當資料量 \(n\) 變得非常大時，\(f(n)\) 的成長速度不會超過 \(g(n)\) 的常數倍。Big O 的核心定義拆解數學公式：\(f(n)\le c\cdot g(n)\quad \text{對於所有 }n\ge n_{0}\)關鍵要素：\(c\) 與 \(n_{0}\)：必須存在這兩個正整數常數。\(n \geq n_0\)：代表我們只關心「當資料量 \(n\) 成長到足夠大（超過 \(n_{0}\)）之後」的趨勢，忽略前期的微小差異。上界（Upper bound）：\(g(n)\) 是 \(f(n)\) 的天花板，函數效率再怎麼差也不會超越這個邊界。投影片中的重要觀念\(O(1)\)：代表常數時間（Constant time）。無論輸入的資料量 \(n\) 有多大，程式執行所花費的時間（或步驟）都是固定的。資訊精確性（Informative）：雖然 \(f(n) = n\) 可以說是 \(O(n^2)\)，但這不夠精確。為了讓 Big O 具有參考價值，我們會尋找最小、最貼近 \(f(n)\) 的 \(g(n)\) 函數，因此我們會說 \(f(n) = O(n)\)。