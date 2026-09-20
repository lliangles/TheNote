---
tags:
  - 課程筆記
  - 資料結構
date: 2026-07-21
aliases:
  - "Chapter 1: Basic Concept"
---
# TOC
別慌，這兩份 PPT 其實就是資料結構的開頭：Ch1 基礎概念 + Ch2 陣列。我幫你濃縮成考前/複習重點，你先抓大方向，不要被程式碼嚇到。

---
[[L2 Arry]]


Ch1 Basic Concept 基礎概念

1. 系統生命週期

· Requirements → Analysis → Design → Refinement & Coding → Verification
· 分析常用：
  · Bottom-up：沒有總體規劃，鬆散連接
  · Top-down：高階規劃，複雜系統較常用

2. ADT（抽象資料型別）

· Data Type = 物件集合 + 操作集合
· ADT = 把「規格」和「實作」分開
· 重點：資訊隱藏、規格與實作分離
· 例：NaturalNumber ADT：Zero、IsZero、Equal、Successor、Add、Subtract

3. 演算法特性

一定要有：

· Input：0 個或多個輸入
· Output：至少 1 個輸出
· Definiteness：明確無歧義
· Finiteness：有限步後結束
· Effectiveness：每一步都夠基本、可執行

4. 遞迴

· 直接遞迴：自己呼叫自己
· 間接遞迴：A 呼叫 B，B 再呼叫 A
· 一定要有終止條件
· 常見例子：
  · Binary Search
  · Permutation
  · Fibonacci
  · Towers of Hanoi
· 漢諾塔移動次數：
  · moves(n) = 2*moves(n-1) + 1 = 2^n - 1

5. 複雜度分析

· Space complexity：S(P) = c + Sp(I)
· Time complexity：用 step count 估算
· 三種情況：
  · Best case
  · Worst case
  · Average case

6. 漸進記號

· Big O：上界，f(n) = O(g(n))
· Omega：下界，f(n) = Ω(g(n))
· Theta：緊確界，f(n) = Θ(g(n))
· 常見成長速率：
  · O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)

---

如果是要考試，優先順序：

1. ADT 是什麼：規格 vs 實作
2. Big O / Omega / Theta
3. 遞迴與漢諾塔公式
4. 多項式非零項表示與加法
5. 稀疏矩陣三元組
6. 快速轉置三步驟
7. 二維陣列 row-major / column-major 位址公式
8. KMP failure function 概念

---

別急，這兩章看起來很多，但其實主線只有：
ADT → 演算法分析 → 陣列儲存 → 稀疏矩陣 → 字串匹配。

你如果告訴我「哪一頁或哪個主題最卡」，例如多項式加法、快速轉置、KMP、Big O，我可以針對那個部分用更白話的方式再講一次。


# System Life Cycle (1)

In a system, programs undergo a development process.
### Requirements
	A set of specifications 系統規格
	Describe the information we are given. 輸入
	The results we have to produce 輸出
### Analysis
Break the problem down into manageable pieces. 
	在建構的過程思考： Bottom-up approach 
		No master plan, loosely connected.
		探索型的系統，完成雛型
    已經釐清彼此關係： Top-down approach
		A high-level plan, preferred for complex software systems.
		 通常作為雛型系統的進一步重建
### Design
	The creation of abstract data types. 資料型態
	The operations performed on data objects. 資料處理
	Both are language independent.
### Refinement and coding
	Data object’s representation can determine the efficiency of the algorithms.
	 資料抽象表示法如何節省時間
### Verification  
	Correctness proofs 正確性證明（人工）
	Testing 測試（利用測資取得結果）
	Error removal（）
   Requirement accepted ?
   軟體開發管理責任
	- 必須釐清使用者須求 requirements 
	- 必須經過測試資料驗證
   
# Abstraction 抽象 and Encapsulation 封裝
### Specification vs. Implementation
抽象（Abstraction）黑箱，藏複雜的內部運作細節
規格（Specification）：定義介面或類別的功能與外在行為，讓使用者知道該如何呼叫。
實現（Implementation）：背後實際寫程式碼去完成這些功能的過程。使用者不需要看懂內部程式碼，就能直接使用。 [1] (https://www.instagram.com/reel/DR7EcWXD_vM/)資訊隱藏（Information Hiding）與封裝資訊隱藏：限制對物件內部資料或實作細節的存取，避免外部程式碼隨意破壞資料。封裝：將「資料（屬性）」與「操作資料的方法（行為）」綁定在同一個單位（如類別）裡面。藉由限制直接存取，保護資料安全。
Information hiding


# Abstraction Data Type

Data Type
	A data type is a collection of ==objects== and  set of operations that act on those objects.
Abstraction Data Type (ADT)
Specification of the objects and the specification of the operations is ==separated from==(分離於) the representation of the objects and the implementation(執行) of the operations.


# ADT of NatureNumber

ADT NaturalNumber is 
	objects: An ordered subrange of the integers starting at zero and ending at the maximum integer (MAXINT) on the computer. 
	functions: for all x, y～NaturalNumber, TRUE, FALSE～Boolean and where +, -, <, = =, and = are the usual integer operations
	Nat_Num Zero()  ::= 0
	Boolean IsZero(x) ::= if (x) return FALSE else return TRUE
	Boolean Equal(x,y) :: == if(x= =y) return true else return false
	Nat_Num Successor :: == if(x= =MAXINT) return x else return x+1 
	Nat_Num Add(x, y) :: == if(x+y<=MAXINT) return x+y else return MAXINT
	Nat_Num Subtract(x,y) :: == if(x<y) return 0 else return x-y //為了回傳自然數避免負數
Successor 後繼者
# Algorithm Specification #送分題

Algorithm: A finite set of instructions that accomplishes a particular task and satisfy the following criteria: （13：30）
一種有限集合的指令，為了滿足
**Input**: Zero or more quantities are externally supplied. 可以零輸入
**Output**: At least one quantity is produced. 至少要有一個輸出！！不能沒有
**Definiteness**明確性: Clear and unambiguous. 明確且不易混淆
**Finiteness**有限性: Terminates after a number of steps. 必須在有限步驟後自動結束(不可無限迴圈)
**Effectiveness**有效性: Must be basic enough to be carried out by a person using only pencil and pen.足夠能夠理解

# Selection Sort(1)

Algorithm  v.s. Program
In computational theory, a program does ==not== have to satisfy the **finiteness**（有限性）.
Example 1.2 [Selection sort] Sort a collection of n >=1 integers.
From those integers that are currently unsorted, find the smallest and place it next in the sorted list.

```cpp
for (i = 0; i < n ; i++) {
Examine a[i] to a[n-1] and suppose the smallest i integer is at a[j];` 
Interchange a[i] and a[j] ;
}
```

``` cpp 
void sort (int list[], int n) 
{
	int i, j, min;
	for (i = 0; i < n ; i++ ) {
		min = i  ;//未排序
		/* find smallest integer in a[i] to a[n-1] */ 
		for (j = i+1 ; j < n ; j++)
			if (list[j] < list[min]) min = j;
		SWAP(list[i], list[min]);
	}
} 
```


## Binary Search(1)

Algorithm for binary searching an ordered list
``` cpp 
while (there are more integers to check){ 
	middle = (left + right) / 2; 
	if (searchnum < list[middle]) 
		right = middle – 1; 
	else if (searchnum == list[middle]; 
		return middle;
	else left = middle + 1;
}
return -1;
````

Comparison of two integers

1. **Function**
``` cpp
int COMPARE(int x, int y)
{  /* compare x and y, return –1 for less than, o for equal, 1 for greater */
	if ( x < y) return –1;
	else if (x == y) return 0;
	else return 1;//x>y
}
````

2. **Macro**巨集
```cpp 
	#define COMPARE(x, y) ((x) < (y)) ? –1: ((x) == (y)) ? 0: 1)
	//因為x本身又有可能是運算式，故需要(x)
	int binsearch( int list[], int searchnum, int left, int right)
{	int middle;
	while( left <=right ) {
		middle=(left+right)/2;
		switch( COMPARE(list[middle], searchnum)){
		  case -1: left=middle+1; break;
		  case 0: return middle;
		  case 1: right=middle-1;
		}
	}
return -1;
}
````

# Recursive Algorithms

Recursive functions
Direct recursion 直接呼叫
	Functions call themselves before they are done. 
Indirect recursion 
	Functions call other functions that again invoke the calling function.
Terminating condition
	When satisfied, the function directly computes the output without calling itself.
遞迴？
## Recursive binsearch 遞迴二分
```cpp 
int binsearch( int list[], int searchnum, int left, int right)
{	int middle;
	 if(left<=right) { //如果是用micro使用<-while( left <=right ) 
		middle=(left+right)/2;
		switch( COMPARE(list[middle], searchnum){
		  case -1: 
			return binsearch(list, searchnum, middle+1, right);
		  case 0: return middle;
		  case 1: right=middle-1;
			return binsearch(list, searchnum, left, middle-1);
		}
	}
return -1;
}
````

## Recursive Permutation Generator #實作
Example: Print out all possible permutations of {a, b, c, d}
We can construct the set of permutations by printing
a followed by all permutations of (b, c, d)
b followed by all permutations of (a, c, d)
c followed by all permutations of (a, b, d)
d followed by all permutations of (a, b, c)
先分解題目！
perm(list,0,n)?

```cpp 
void SWAP{char &a,char &b){
  char c; c=a; a=b; b=c;
}
void perm( char *list, int i, int n){
	if( i== n-1 ){
		for( j=0; j<n; j++ )cout<<list[j]);
		cout<<endl;
	}else{
		for( j=i; j<n; j++){
			SWAP( list[i], list[j]);
			perm( list, i+1, n);
			SWAP( list[j], list[i]);
		}
	}
}

````

## Others Recursion Algorithms

Fibonacci numbers 前2相加等於3
fib(n-1)+fib(n-2)
Towers of Hanoi
Ackerman’s function 
	A(m,n)=
	n+1 if m= =0;
	A(m-1,1) if n= =0
	A(m-1,A(m, n-1)) otherwise
### 1.7 The Criteria to Judge a Program 




Does it meet the **original specification 原始規格** of the task?
Does it work **correctly 正確**?
Is there **documentation that describes** how to use it and how it works?
Effectively use functions **有效使用函式** to create **logical units..邏輯單位**,
Is the code readable?
Effectively use **primary and secondary storage**?
Running time acceptable? ;

· 是否符合原始規格？
· 是否正確？
· 有沒有文件說明怎麼用、怎麼運作？
· 有沒有有效使用函式來建立邏輯單位？
· 程式碼可讀嗎？
· 有沒有有效使用主要/次要儲存？
· 執行時間可接受嗎？

這些是「質化」標準。接下來就進入「量化」分析：Performance Analysis。
### Performance Analysis 
主要還是在分析RAM(main memory)
量化」能分析（Performance Analysis）
## 效能分析的兩大維度

* 空間複雜度（Space Complexity）：程式執行到結束所需的記憶體總量。
* 時間複雜度（Time Complexity）：程式執行到結束所需的電腦時間總量。

Space complexity 
	The amount of memory a program needs to run to completion.
Time complexity
	The amount of computer time a program needs to run to completion. 

## 空間複雜度的組成公式
### Space Complexity
任何程式 $P$ 的空間需求 $S(P)$，都可以拆解為以下公式：
$$\mathbf{S(P) = c + SP(I)}$$ 
這兩個部分的詳細定義如下：

| 組成部分 | 定義 | 包含內容 |
|---|---|---|
| $c$：固定部分 (Fixed part) | 與輸入/輸出資料的特徵（如數量、大小）無關的空間。 | 1. 指令空間（Instruction space） 2. 簡單變數、常數空間 3. 固定大小的複合變數 |
| $SP(I)$：變動部分 (Variable part) | 大小取決於特定問題實例（Instance $I$）的複合變數空間。 | 1. 動態配置的陣列或結構 2. 遞迴函式（Recursive functions）呼叫時所需的系統堆疊空間 |

Fixed part c
	Independent of the characteristics (e.g. number, size) of the inputs and outputs. 
		Instruction space
		Space for simple variables, constants
		Fixed-size component variables 
Variable part
	Component variables whose size is dependent on the particular problem instance.
	Using recursive functions.
S(P): The space requirement of any program P. （沒有需要系統堆疊空間就沒有
	S(P) = c + SP (I) 
	c: Fixed Part
	SP (I): Variable Part
	I: Instance characteristics
#### Example

```cpp
float abc(float a, float b, float c) {
       return a + b + b*c + (a +b – c)/(a + b) + 4.0 ; }
Sabc(I) = 0. //因為沒有遞和陣列
````

C++

## 不同呼叫方法會對時間複雜度產生差距
陣列
```
float sum (float list[], int n) {
   float s = 0 ; 
	int i;
for (i = 0; i < n; i++)
s += list[i] ;
return s ; 
} 
Pascal copy the array. Ssum(n) = n.//因為是用Pascal是用 call by value 生成新陣列，所以
C does not copy the array. Ssum(n) = 0.//因為c++是用 用 call by point 就是固定傳陣列, 所以時間複雜度是0
````
回答方式：
Pascal copy the array. Ssum(n) = n.//因為是用Pascal是用 call by value 生成新陣列和新元素，所以是n
C does not copy the array. Ssum(n) = 0.//因為c++是用 用 call by point 就是固定傳陣列, 所以時間複雜度是0
那python 呢


遞迴版：

```cpp
float rsum(float *a, const int n) {
    if (n <= 0) return 0;
    else return rsum(a, n-1) + a[n-1];
}
```

每次遞迴會在 stack 放：float a、const int n、return value、return address，共約 16 bytes。遞迴 n+1 次，所以空間約 16n 或 4(n+1)。總之是 O(n)。
[[Space Complexity Examples (2)]]


###  Questions 

> [!example] Q 
> 

>[!a]- ans. 
>a

#### 💡 Answer

>[!info]
> - **Correct answer** ：
> - Notet：

![[.excalidraw]]