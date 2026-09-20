# 02_Basic

> 📌 **課程主題筆記**: 本文件由 `02_Basic.ppt` 完整擷取，包含所有投影片內容、階層清單、程式碼區塊、表格、圖表標籤與註記，共 63 頁投影片。

## Slide 1

- 資料結構
- Data Structure

- Chapter 1: Basic Concept
- 國立聯合大學
- 資訊管理學系
- 温敏淦

---

## Slide 2: System Life Cycle (1)

- In a system, programs undergo a development process.
  - Requirements
  - Analysis
  - Design
  - Refinement and Coding
  - Verification

---

## Slide 3: System Life Cycle (2)

- Requirements
  - A set of specifications
  - Describe the information we are given.
  - The results we have to produce.

---

## Slide 4: System Life Cycle (3)

- Analysis
  - Break the problem down into manageable pieces.
  - Bottom-up approach
    - No master plan, loosely connected.
  - Top-down approach
    - A high-level plan, preferred for complex software systems.

---

## Slide 5: System Life Cycle (4)

- Design
  - The creation of abstract data types.
  - The operations performed on data objects.
  - Both are language independent.
- Refinement and coding
  - Data object’s representation can determine the efficiency of the algorithms.
- Verification
  - Correctness proofs
  - Testing
  - Error removal

---

## Slide 6: Abstraction and Encapsulation

- Specification vs. Implementation
- Information hiding

---

## Slide 7: Abstraction Data Type

- Data Type
  - A data type is a collection of objects and set of operations that act on those objects.
- Abstraction Data Type (ADT)
  - Specification of the objects and the specification of the operations is separated from the representation of the objects and the implementation of the operations.

---

## Slide 8: ADT of NatureNumber

- ADT NaturalNumber is
- objects: An ordered subrange of the integers starting at zero and ending at the maximum integer (MAXINT) on the computer.
- functions: for all x, y～NaturalNumber, TRUE, FALSE～Boolean and where +, -, <, ==, and = are the usual integer operations
- Nat_Num Zero() ::= 0
- Boolean IsZero(x) ::= if (x) return FALSE else return TRUE
```c
Boolean Equal(x,y) :: == if(x==y) return true else return false
	Nat_Num Successor :: == if(x==MAXINT) return x else return x+1
```
- Nat_Num Add(x, y) :: == if(x+y<=MAXINT) return x+y else return MAXINT
- Nat_Num Subtract(x,y) :: == if(x<y) return 0 else return x-y

---

## Slide 9: Algorithm Specification

- Algorithm: A finite set of instructions that accomplishes a particular task and satisfy the following criteria:
  - Input: Zero or more quantities are externally supplied.
  - Output: At least one quantity is produced.
  - Definiteness: Clear and unambiguous.
  - Finiteness: Terminates after a number of steps.
  - Effectiveness: Must be basic enough to be carried out by a person using only pencil and pen.

---

## Slide 10: Selection Sort(1)

```c
Algorithm  v.s. Program
In computational theory, a program does not have to satisfy the finiteness.
Example 1.2 [Selection sort] Sort a collection of n >=1 integers.
From those integers that are currently unsorted, find the smallest and place it next in the sorted list.
for (i = 0; i < n ; i++) {
Examine a[i] to a[n-1] and suppose the smallest i integer is at a[j];
Interchange a[i] and a[j] ;
}
```

---

## Slide 11: Selection Sort(2)

```c
void sort (int list[], int n)
{
	int i, j, min, temp;
	for (i = 0; i < n ; i++ ) {
		min = i  ;
		/* find smallest integer in a[i] to a[n-1] */
		for (j = i+1 ; j < n ; j++)
			if (list[j] < list[min]) min = j;
		SWAP(list[i], list[min]);
	}
}
```

---

## Slide 12: Binary Search(1)

```c
Algorithm for binary searching an ordered list
while (there are more integers to check){
	middle = (left + right) / 2;
	if (searchnum < list[middle])
		right = middle – 1;
	else if (searchnum == list[middle];
		return middle;
	else left = middle + 1;
}
return -1;
```

---

## Slide 13

```c
Comparison of two integers
Function
int COMPARE(int x, int y)
{  /* compare x and y, return –1 for less than, o for equal, 1 for greater */
	if ( x < y) return –1;
	else if (x == y) return 0;
	else return 1;
}
Macro
	#define COMPARE(x, y) ((x) < (y)) ? –1: ((x) == (y)) ? 0: 1)
```

---

## Slide 14

```c
int binsearch( int list[], int searchnum, int left, int right)
{	int middle;
	while( left <=right ) {
		middle=(left+right)/2;
		switch( COMPARE(list[middle], searchnum){
		  case -1: left=middle+1; break;
		  case 0: return middle;
		  case 1: right=middle-1;
		}
	}
return -1;
}
```

---

## Slide 15: Recursive Algorithms

- Recursive functions
- Direct recursion
  - Functions call themselves before they are done.
- Indirect recursion
  - Functions call other functions that again invoke the calling function.
- Terminating condition: When satisfied, the function directly computes the output without calling itself.

---

## Slide 16: Recursion for binsearch

```c
int binsearch( int list[], int searchnum, int left, int right)
{	int middle;
	 if(left<=right) { //<-while( left <=right )
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
```

---

## Slide 17: Recursive Permutation Generator

- Example: Print out all possible permutations of {a, b, c, d}
  - We can construct the set of permutations by printing
    - a followed by all permutations of (b, c, d)
    - b followed by all permutations of (a, c, d)
    - c followed by all permutations of (a, b, d)
    - d followed by all permutations of (a, b, c)

---

## Slide 18

```c
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
```

- perm(list,0,n)

---

## Slide 19: Others Recursion Algorithms

- Fibonacci numbers
- Towers of Hanoi
- Ackerman’s function
  - A(m,n)=
```c
n+1 if m==0;
```
    - A(m-1,1) if n==0
    - A(m-1,A(m, n-1)) otherwise

---

## Slide 20: 1.7 The Criteria to Judge a Program

- Does it meet the original specification of the task?
- Does it work correctly?
- Is there documentation that describes how to use it and how it works?
- Effectively use functions to create logical units?
- Is the code readable?
- Effectively use primary and secondary storage?
- Running time acceptable?

---

## Slide 21: Performance Analysis

- Space complexity
  - The amount of memory a program needs to run to completion.
- Time complexity
  - The amount of computer time a program needs to run to completion.

---

## Slide 22: Space Complexity (1)

- Fixed part
  - Independent of the characteristics (e.g. number, size) of the inputs and outputs.
    - Instruction space
    - Space for simple variables, constants
    - Fixed-size component variables
- Variable part
  - Component variables whose size is dependent on the particular problem instance.
  - Using recursive functions.

---

## Slide 23: Space Complexity (2)

- S(P): The space requirement of any program P.
  - S(P) = c + SP (I)
  - c: Fixed Part
  - SP (I): Variable Part
  - I: Instance characteristics
- Example
```c
float abc(float a, float b, float c) {
       return a + b + b*c + (a +b – c)/(a + b) + 4.0 ; }
```
  - Sabc(I) = 0.

---

## Slide 24: Space Complexity Examples (1)

```c
float sum (float list[], int n) {
   float s = 0 ;
	int i;
for (i = 0; i < n; i++)
s += list[i] ;
return s ;
}
Pascal copy the array. Ssum(n) = n.
C does not copy the array. Ssum(n) = 0.
```

---

## Slide 25: Space Complexity Examples (2)

```c
float rsum (float *a, const int n) {
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
```

---

## Slide 26: Time Complexity

- The time T(P) of program P
- Compile time
  - Independent to the instance characteristics.
- Run (or execution) time (TP)
- Obtain an exact formula of TP is not easy.
  - The true value of TP (n) for any given n can be obtained only experimentally.
- Program step
  - A syntactically or semantically meaningful segment of a program.

---

## Slide 27: One Step

```c
a=4;
c=b+30;
return a + b * c + (a+b-c)/(a+b) + 4.0
```

---

## Slide 28: C++ steps

- 0 step
  - Comments, declarative, function statements,
- 1 step
  - Expressions, function call, and assignment, memory management (new, delete,…), iterative (for, while), jump (break, goto, return, continue)
- Multi-steps
  - switch-case, if-else

---

## Slide 29: Time Complexity Example (1)

```c
float sum (float *a, int n)  { /* 2n + 3*/
float s = 0 ;
int i;
count++ ;
for (i = 0; i< n; i++) {
	count++ ; /* for the for loop */
	s += a[i] ;
	count++ ; /* for the assignment*/
}
count++ ; /* for the last time of for */
count++ ; /* for return ;  */
return s ;
}
```

---

## Slide 30: Time Complexity Example (2)

```c
float rsum (float *a, int n) { /* 2n+2 /
	count++ ; /* for if conditional  */
   if (n <= 0) {
		count++ ; /* for return */
		return 0 ;
	}
	else {
		count++ ; /* for return  */
		return (rsum(a, n-1) + a[n-1]) ;
	}
}
```

---

## Slide 31: Time Complexity Example (3)

- 2 + trsum (n – 1) steps, n > 0.
- trsum(n) = 2 + trsum (n - 1)
- = 2 + 2 + trsum (n – 2)
- = 2 * 2 + trsum (n - 2)
- = 2 * 3 + trsum (n - 3)
- .
- .
- = 2n + trsum (0) = 2n + 2

---

## Slide 32: Example: Matrix Addition (1)

```c
void add (int a[][MAX_SIZE], b[][MAX_SIZE], c[][MAX_SIZE], int rows, int cols) {
int i, j;
for (i = 0; i < rows; i++)
	for (j = 0; j < cols; j++)
		c[i][j] = a[i][j] + b[i][j] ;
}
```

---

## Slide 33: Example: Matrix Addition (2)

```c
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
```

---

## Slide 34: Summary of Step

- The number of steps is itself a function of the instance characteristics.
- Any specific instance may have several characteristics.
- We need to know exactly which characteristics of the problem instance are to be used.
- A step is any computation unit that is independent of the characteristics.

---

## Slide 35: Asymptotic Notation

- Motivation to determine step counts
  - Compare the time complexities of two programs that compute the same function.
  - Predict the growth in run time as the instance characteristics change.
- Example: Binary search
  - Successful search
  - Unsuccessful search
- Asymptotic notation
  - Determine the exact step count is very difficult.

---

## Slide 36: Three Kinds of Step Counts

- Best-case
  - The minimum number of steps that can be executed for the given parameters.
- Worst-case
  - The maximum number of steps that can be executed for the given parameters.
- Average-case
  - The average number of steps that can be executed with the given parameters.

---

## Slide 37: Big O

- Definition [Big “O”]:
  - f(n) = O(g(n)) iff there exist positive constants c and n0 such that f(n) ≤ cg(n) for all n, n ≥ n0.
  - Upper bound on f(n)
  - O(1): a constant.
  - f(n) = O(g(n)) to be informative, g(n) should be as small a function of n as one can come up with for which f(n) = O(g(n)) .

---

## Slide 38: Example of Big “O”

- 3n+2 = O(n)
  - f(n)=3n+2, g(n)=n, c=4 n0=2
  - 3n+2 ≤ 4n for all n ≥ 2.
- 10n2+4n+2 = O(n2)
  - f(n)= 10n2+4n+2, g(n)=n2, c=11 n0=5
  - 10n2+4n+2 ≤ 11n2 for n ≥ 5.

---

## Slide 39: Common of Big O

- O(1): constant
- O(log n): logarithmic
- O(n): linear
- O(n log n): log linear
- O(n2): quadratic
- O(n3): cubic
- O(2n): exponential
- O(n!): factorial

---

## Slide 40: Big O and small o

- f(n) = o(g(n)) to be informative, g(n) should be as small a function of n as one can come up with for which f(n) = o(g(n)) .

---

## Slide 41: Omega

- Definition [Omega]
  - f(n) = Ω(g(n)) iff there exist positive constants c and n0 such that f(n) ≥ cg(n) for all n, n ≥ n0.
  - The function g(n) is only a lower bound on f(n).
  - f(n) = Ω(g(n)) to be informative, g(n) should be as large a function of n as one can come up with for which f(n) = Ω(g(n)) is true.

---

## Slide 42: Examples of Omega

- 3n+2 = Ω(n)
  - f(n)=3n+2, g(n)=n, c=3, n0=1
  - 3n+2 ≥ 3n for all n ≥ 1.
- 10n2+4n+2 = Ω(n2)
  - f(n)= 10n2+4n+2, g(n)= n2, c=1, n0=1
  - 10n2+4n+2 ≥ n2 for all n ≥ 1.

---

## Slide 43: Theta

- Definition [Theta]:
  - f(n) = Θ(g(n)) iff there exist positive constants c1, c2 and n0 such that c1g(n) ≤ f(n) ≤ c2g(n) for all n, n ≥ n0.
- Lower bound and upper bound on f(n)
- The theta notation is more precise than both “big oh” and omega notations.

---

## Slide 44: Examples of Theta

```c
3n+2 = Θ(n) as 3n+2 ≥ 3n for all n ≥ 2, and 3n+2 ≤ 4n for all n ≥ 2.
10n2+4n+2 = Θ(n2)
6*2n+n2 = Θ(2n)
10n2+4n+2 ≠ Θ(1)
```

---

## Slide 45: Real Cases of Theta

- Asymptotic complexity of matrix addition
  - Θ(rows * cols)
- Asymptotic complexity of binary search
  - worst case: Θ(log n)
  - best case: Θ(1)
- Asymptotic complexity of permutation
  - Θ(n (n!))
- Asymptotic complexity of magic square: Θ(n2)

---

## Slide 46: Time Performance in C (1)

```c
#include <time.h>
…
clock_t start, stop;
…
start = clock();
seqsearch(…);
stop = clock();
duration = ((double) (stop - start) ) / CLK_TCK;
```

---

## Slide 47: Time Performance in C (2)

```c
#include <time.h>
…
time_t start, stop;
…
start = time(NULL);
binsearch(…);
stop = time(NULL);
duration = ((double) difftime(stop, start);
```

---

## Slide 48: Function Values

| log n | n | n log n | n2 | n3 | 2n |
| --- | --- | --- | --- | --- | --- |
| 0 | 1 | 0 | 1 | 1 | 2 |
| 1 | 2 | 2 | 4 | 8 | 4 |
| 2 | 4 | 8 | 16 | 64 | 16 |
| 3 | 8 | 24 | 64 | 512 | 256 |
| 4 | 16 | 64 | 256 | 4096 | 65536 |
| 5 | 32 | 160 | 1024 | 32768 | 4294967296 |

---

## Slide 49

> 🖼️ *(包含圖形 / 示意圖)*

---

## Slide 50: Summary

- Algorithm
- Recursion and loop
- ADT (Abstract Data Type)
- Space Complexity
- Time Complexity

---

## Slide 51: Towers Of Hanoi/Brahma

> 📊 **圖表元素 / 標籤:** B, C, 4, 3, 2, 1

- A

- 64 gold disks to be moved from tower A to tower C
- each tower operates as a stack
- cannot place big disk on top of a smaller one

> 💡 **備忘稿 / Notes:**
> Could use animation of towers of hanoi from animations page on Web site.
> Also known as Towers of Brahma.
> According to legend, on the day of creation Buddhist monks began the task of moving disks from tower A to tower C. When they get done, the world will come to an end.

---

## Slide 52: Towers Of Hanoi/Brahma

> 📊 **圖表元素 / 標籤:** B, C, 3, 2, 1

- A

- 3-disk Towers Of Hanoi/Brahma

---

## Slide 53

> 📊 **圖表元素 / 標籤:** B, C, 2, 1, 3

- A

- 3-disk Towers Of Hanoi/Brahma

---

## Slide 54

> 📊 **圖表元素 / 標籤:** B, C, 1, 2, 3

- A

- 3-disk Towers Of Hanoi/Brahma

---

## Slide 55

> 📊 **圖表元素 / 標籤:** B, C, 3, 1, 2

- A

- 3-disk Towers Of Hanoi/Brahma

---

## Slide 56

> 📊 **圖表元素 / 標籤:** B, C, 3, 2, 1

- A

- 3-disk Towers Of Hanoi/Brahma

---

## Slide 57

> 📊 **圖表元素 / 標籤:** B, C, 3, 2, 1

- A

- 3-disk Towers Of Hanoi/Brahma

---

## Slide 58

> 📊 **圖表元素 / 標籤:** B, C, 2, 3, 1

- A

- 3-disk Towers Of Hanoi/Brahma

---

## Slide 59

> 📊 **圖表元素 / 標籤:** B, C, 3, 2, 1

- A

- 3-disk Towers Of Hanoi/Brahma

- 7 disk moves

---

## Slide 60

> 📊 **圖表元素 / 標籤:** A, B, C, 1

- n > 0 gold disks to be moved from A to C using B
- move top n-1 disks from A to B using C

---

## Slide 61: Recursive Solution

> 📊 **圖表元素 / 標籤:** B, C, 1

- A

- move top disk from A to C

---

## Slide 62

> 📊 **圖表元素 / 標籤:** B, C, 1

- A

- move top n-1 disks from B to C using A

---

## Slide 63

> 📊 **圖表元素 / 標籤:** B, C, 1

- A

- moves(n) = 0 when n = 0
- moves(n) = 2*moves(n-1) + 1 = 2n-1 when n > 0

---
