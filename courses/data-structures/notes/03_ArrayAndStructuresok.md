# 03_ArrayAndStructuresok

> 📌 **課程主題筆記**: 本文件由 `03_ArrayAndStructuresok.ppt` 完整擷取，包含所有投影片內容、階層清單、程式碼區塊、表格、圖表標籤與註記，共 49 頁投影片。

## Slide 1

- 資料結構
- Data Structure

- Chapter 2: Array
- 國立聯合大學
- 資訊管理學系
- 溫敏淦

---

## Slide 2: C++ Class

- Class
  - class ame
  - Data member
  - Member function
  - public, protected, private
    - friend function, friend class

---

## Slide 3: Class

- Definition vs. implenment
  - ADT
    - implementation-independent
      - xxx.h
    - inline function
  - implementation
    - xxx.c, xxx.cpp
- Access member of class
  - Object.member; //variable
  - Object->member; //pointer

---

## Slide 4: Class

```c
static member variable
class variable
class, struct, union
```

---

## Slide 5: C++ Class

```c
#ifndef RECTANGLE_H
#define RECTANGLE_H
	class Rectangle{
	public:
		Rectangle();
		~Rectangle();
		int GetHeight();
		int GetWidth();
	private:
	int xLow, yLow, height, width;
#endif
```

---

## Slide 6: Struct in C

```c
struct  person {
	char name[10];
	int age;
	float salary;
};
typedef struct person{
	char name[10];
	int age;
	float salary;
} SPerson;
```

```c
struct person p1;
SPerson p2;
```

---

## Slide 7: Unions in Structures

```c
struct data {
    int shape;
    union{
      int square;
      char triangle;
      char circle;
    }info;
 }myshape;
```

```c
myshape.info.circle=…;
myshape.info.square=…;
```

---

## Slide 8: ADT of Array

- ADT Array is
  - Objects: A set of pairs <index, value> where for each value of index there is a value from the set item. Index is a finite ordered set of one or more dimensions, for example {0,…,n-1} for one dimension, {(0,0), (0,1),(0,2),(1,0),(1,1),…,(2,2)} for two dimensions.
  - Functions:
    - Array Create(j, list, initValue)
    - Item Retrieve(i)
    - Array Store(i, x)

> 🖼️ *(包含圖形 / 示意圖)*

---

## Slide 9: Array in C

```c
int list[5], *plist[20];
int one[]={0, 1, 2, 3, 4}
int *list1;
list1=list; /*  list1=&(list[0]);*/
cout << *(list+2);
```

---

## Slide 10

```c
#define MAX_SIZE 100
float sum(float [], int);
float input[MAX_SIZE], answer;
void main(void)
{
	int i;
	for(i=0; i<MAX_SIZE;i++)
		input[i]=i;
	answer=sum(input, MAX_SIZE);
	cout << “The sum is: “<< answer<<endl;
}
float sum( float list[], int n)
{
	int i; float tempsum=0;
	for( i=0; i<n; i++)
		tempsum+=list[i];
	return tempsum;
}
```

---

## Slide 11: Polynomial

- A(x)=3x20+2x5+4, B(x)=x4+10x3+3x2+1

> 🖼️ *(包含圖形 / 示意圖)*

> 🖼️ *(包含圖形 / 示意圖)*

> 🖼️ *(包含圖形 / 示意圖)*

---

## Slide 12: Polynomial Representations

```c
Representation 3
class Polynomial;  // forward delcaration
class term {
	friend Polynomial;
	private:
	      float coef;		// coefficient
	      int exp;		// exponent
};
private:
	term *termArray;
      int capacity;
	int Terms;
term Polynomial:: termArray[MaxTerms];
```

```c
Representation 1
private:
	int degree;	// degree ≤ MaxDegree
	float coef [MaxDegree + 1];
Representation 2
private:
	int degree;
	float *coef;
	Polynomial::Polynomial(int d)
{
	degree = d;
	coef = new float [degree+1];
}
```

- x10000+1??

---

## Slide 13: Polynomial Addition

- 只存非零值(non-zero)：一元多項式
  - Add the following two polynomials:
  - A(x) = 2x1000 + 1
  - B(x) = x4 + 10x3 + 3x2 + 1

- 0

- 1

- 2

- 0

- 1

- 2

- 3

- 4

- B_coef

- 4

- 3

- A_coef

- 2

- 1

- 10

- 1

- 2

- 1

- B_exp

- 0

- A_exp

- 2

- 4

- 3

- 0

- 1000

- 0

- 1

- 2

- 3

- 5

- 4

- C_coef

- 5

> 📊 **圖表元素 / 標籤:** 10, 3, 1, 4, 2, 1000, 0

- C_exp

---

## Slide 14: Polynomial Addition

```c
Polynomial Polynomial:: Add(Polynomial B)
// return the sum of A(x) ( in *this) and B(x)
{
	Polynomial C; int a = 0; int b =0t; float d;
	while ((a <= Terms) && (b <= B.Terms))
	    switch (compare(termArray[a].exp, B.termArray[b].exp)) {
		case ‘=‘:
		      d = termArray[a].coef +B.termArray[b].coef;
		      if ( d ) C.NewTerm(d, termArray[a].exp);
			a++; b++;
			break;
		case ‘<‘:
		      C.NewTerm(B.termArray[b].coef, B.termArray[b].exp);
		      b++;
		      break;
		case ‘>’:
		      C.NewTerm(termArray[a].coef, termArray[a].exp);
		      a++;
	} // end of switch and while
	// add in remaining terms of A(x)
	for (; a<= Terms; a++)
	   C.NewTerm(termArray[a].coef, termArray[a].exp);
	// add in remaining terms of B(x)
	for (; b<= B.Terms; b++)
	   C.NewTerm(B.termArray[b].coef, B.termArray[b].exp);
	return C;
} // end of Add
```

- O(m+n)

---

## Slide 15: Program 2.9 Adding a new Term

```c
void Polynomial::NewTerm(float c, int e)
// Add a new term to C(x)
{
	if (Terms==capacity) {
		capacity*=2;
           term *temp=new term[capacity]
           copy(termArray,termArray+Terms,temp);
           delete[] termArray;
		termArray=temp;
	}
	termArray[Terms].coef = c;
	termArray[Terms].exp = e;
	Terms++;
} // end of NewTerm
```

---

## Slide 16: Sparse Matrices

---

## Slide 17: Sparse Matrix Representation

- Use triple <row, column, value>
- Store triples row by row
- For all triples within a row, their column indices are in ascending order.
- Must know the number of rows and columns and the number of nonzero elements

---

## Slide 18: Sparse Matrix Representation (Cont.)

```c
class SparseMatrix; // forward declaration
class MatrixTerm {
	friend class SparseMatrix
	private:
		int row, col, value;
};
In class SparseMatrix:
private:
	int Rows, Cols, Terms,space;
	MatrixTerm smArray[MaxTerms];
```

---

## Slide 19: Sparse Matrices

---

## Slide 20: Transposing A Matrix

```c
The Operations on 2-dim Array
Transpose
for (i = 0; i < rows; i++ )
    for (j = 0; j < columns; j++ )
          B[j][i] = A[i][j];
```

---

## Slide 21: Transposing A Matrix

- Intuitive way:
  - for (each row i)
  - take element (i, j, value) and store it in (j, i, value) of the transpose
- More efficient way:
  - for (all elements in column j)
  - place element (i, j, value) in position (j, i, value)

---

## Slide 22: Program 2.10 Transposing a Matrix

```c
SparseMatrix SparseMatrix::Transpose()
// return the transpose of a (*this)
{
	SparseMatrix b;
	b.Rows = Cols;	// rows in b = columns in a
	b.Cols = Rows;	// columns in b = rows in a
	b.Terms = Terms;	// terms in b = terms in a
	if (Terms > 0) 	// nonzero matrix
	{
		int CurrentB = 0;
		for (int c = 0; c < Cols; c++)   // transpose by columns
		      for (int i = 0; i < Terms; i++)
		      // find elements in column c
			if (smArray[i].col == c) {
			   b.smArray[CurrentB].row = c;
			   b.smArray[CurrentB].col = smArray[i].row;
			   b.smArray[CurrentB].value = smArray[i].value;
			   CurrentB++;
			}
	}  // end of if (Terms > 0)
}  // end of transpose
```

- O(terms*columns)

---

## Slide 23: Fast Matrix Transpose

```c
The O(terms*columns) time => O(rows*columns2) when terms is the order of rows*columns
A better transpose function in Program 2.11. It first computes how many terms in each columns of matrix a before transposing to matrix b. Then it determines where is the starting point of each row for matrix b. Finally it moves each term from a to b.
```

---

## Slide 24: Fast Transpose

- Calculate the number of each column
- Calculate the start position of each column
- Transpose each term in the matrix according to the start position information.

---

## Slide 25: Sparse Matrices

---

## Slide 26: Program 2.11 Fast Matrix Transposing

```c
SparseMatrix SparseMatrix::Transpose()
// The transpose of a(*this) is placed in b and is found in Q(terms + columns) time.
{
	int *RowSize = new int[Cols];
	int *RowStart = new int[Cols];
	SparseMatrix b;
	b.Rows = Cols; b.Cols = Rows; b.Terms = Terms;
	if (Terms > 0) 	// nonzero matrix
	{
	      // compute RowSize[i] = number of terms in row i of b
	      for (int i = 0; I < Cols; i++) RowSize[i] = 0;	// Initialize
	      for ( i = 0; i < Terms; i++)  RowSize[smArray[i].col]++;
	      // RowStart[i] = starting position of row i in b
	      RowStart[0] = 0;
	      for (i = 1; i < Cols; i++)  RowStart[i] = RowStart[i-1] + RowSize[i-1];
```

- O(columns)

- O(terms)

- O(columns-1)

---

## Slide 27: Program 2.11 Fast Matrix Transposing (Cont.)

```c
for (i =0; I < Terms; i++)   // move from a to b
			{
			      int j = RowStart[smArray[i].col];
			      b.smArray[j].row = smArray[i].col;
			      b.smArray[j].col = smArray[i].row;
			      b.smArray[j].value = smArray[i].value;
			      RowStart[smArray[i].col]++;
			} // end of for
		} // end of if
		delete [] RowSize;
		delete [] RowStart;
		return b;
} // end of FastTranspose
```

- O(terms)

- O(terms+columns)
- O(rows * columns)

---

## Slide 28: Matrix Multiplication

- Definition: Given A and B, where A is mxn and B is nxp, the product matrix Result has dimension mxp. Its [i][j] element is
- for 0 ≤ i < m and 0 ≤ j < p.

---

## Slide 29: Sparse Matrix Multiplication

> 🖼️ *(包含圖形 / 示意圖)*

- Textbook: pp. 104~106

---

## Slide 30

---

## Slide 31

```c
while(currentRowIndex<terms){
  currColB=bXpose.smArray[0].row;
  currColIndex=0;
  while(currColIndex<=b.terms){
     if(smArray[currRowIndex].row != currRowA){
      d.StoreSum(sum,currRowA,currColB);
	sum=0;
	currRowIndex=currRowBegin;
	while(bXpose.smArray[currColIndex].row==currColB)
		currColIndex++;
	currColB=bXpose.smArray[currColIndex].row;
     }else if(if(bXpose.smArray[currColIndex].row != currColB{
	d.StoreSum(sum,currRowA,currColB);
	sum=0;
	currRowIndex=currRowBegin;
	currColB=bXpose.smArray[currColIndex].row;
     }else
	 if(smArray[currRowIndex].col<bXpose.smArray[currColIndex].col)
	   currRowIndex++;
	 else if(smArray[currRowIndex].col==bXpose.smArray[currColIndex].col){
	    sum+=smArray[currRowIndex].value*bXpose.smArray[currColIndex].value;
	    currRowIndex++; currColIndex++;
	 }else
	   currColIndex++;
  }
```

---

## Slide 32

```c
while(smArray[currRowIndex].row==currRowA) currRowIndex++;
  currRowBegin=currRowIndex;
  currRowA=smArray[currRowIndex].rows;
}
Return d;
```

---

## Slide 33: Representation of Arrays

- Multidimensional arrays are usually implemented by one dimensional array via either row major order or column major order.
- Example: One dimensional array

- α

- α+1

- α+2

- α+3

- α+4

- α+5

- α+6

- α+7

- α+8

- α+9

- α+10

- α+11

- A[0]

- A[1]

- A[2]

- A[3]

- A[4]

- A[5]

- A[6]

- A[7]

- A[8]

- A[9]

- A[10]

- A[11]

---

## Slide 34: Array

- The Operations on 1-dim Array
  - Store
    - 將新值寫入陣列中某個位置
    - A[3] = 45
    - O(1)

> 📊 **圖表元素 / 標籤:** A, 0, 1, 2, 3, ..., 45

---

## Slide 35: Array

```c
char A[3][4];	// row-major
logical structure	physical structure
```

- 1

- 2

- 3

- 0

- A[0][0]

- 0

- A[0][1]

- 1

- A[0][2]

- 2

- A[0][3]

- A[1][0]

- A[2][1]

- A[1][1]

- A[1][2]

- A[1][3]

- Mapping:
- A[i][j]=A[0][0]+i*4+j

---

## Slide 36: Two Dimensional Array Row Major Order

- Col 0

- Col 1

- Col 2

- Col u2 - 1

- Row 0

- X

- X

- X

- X

- X

- X

- X

- X

- Row 1

- Row u1 - 1

- X

- X

- X

- X

- u2
- elements

- u2
- elements

- Row u1 - 1

- Row i

- Row 0

- Row 1

- i * u2 element

---

## Slide 37: Array mapping

- Multidimensional array implemented by row major order.
```c
type A[u1][u2][u3]…[un];
```
  - Address of A[i1] [i2] [i3]…[in]
  - =address ofA[0][0]…[0]+
  - (i1*u2*u3*…*un)+ (i2*u3*u4*…*un)+…
  - +in-1*un+in

---

## Slide 38: The address of elements in 2-dim array

  - 二維陣列宣告為A[r][c]，每個陣列元素佔len bytes，且其元第1個元素A[0][0]的記憶體位址為，並以列為主(row major)來儲存此陣列，則
    - A[0][3]位址為+3*len
    - A[3][0]位址為+(3*c+0)*len
    - ...
    - A[m][n]位址為+(m* c + n)*len
  - A[0][0]位址為，目標元素A[m][n]位址的算法
    - Loc(A[m][n]) = Loc(A[0][0]) + [(m0)*c+(n0)]*元素大小

---

## Slide 39: Array

```c
char A[3][4];	// column-major
logical structure	physical structure
```

- 1

- 2

- 3

- 0

- A[0][0]

- 0

- A[1][0]

- 1

- A[2][0]

- 2

- A[0][1]

- A[1][1]

- A[2][1]

- A[2][1]

- A[0][2]

- A[1][2]

- Mapping:
- A[i][j]=A[0][0]+j*3+i

---

## Slide 40: String

- Usually string is represented as a character array.
- General string operations include comparison, string concatenation, copy, insertion, string matching, printing, etc.

- H

- e

- l

- l

- o

- W

- o

- r

- l

- d

- \0

---

## Slide 41: Pattern Matching

- Given a text string (Long) s and a pattern (Short) P, find out the pattern in the text.
  - s : “If you are not doing that today, it is a good day to make a few phone calls for the planning of a get-together.”
  - P : “to”
- Applications
  - Text editor
  - DNA Sequencing Matching
  - …

---

## Slide 42: Concept

- Check each position in the text T to see if the pattern P starts in that position and matches.

- T:

- s

- m

- a

- l

- l

- p

- i

- g

- P:

- a

- l

- l

- P:

- a

- l

- l

- P:

- a

- l

- l

---

## Slide 43: Pattern Matching in C

```c
int pm(char *text,char *pattern)
{
	int n = strlen(text);    // n is length of textint m = strlen(pattern); // m is length of patternint j;for(int i=0; i <= (n-m); i++) {	j = 0;	while ((j < m) && text[i+j] == pattern[j] )		j++;	if (j == m)		return i;   // match at i}return -1;   // no match
}
```

---

## Slide 44: String Matching

- Search by keyword
  - int String::Find(String pat)
  - Heuristics rule

```c
int String::Find(String pat){
  for(int start=0;start<=Length()-pat.Length();start++){
     int j;
     for(j=0;j<pat.Length()&&str[start+j]==pat.str[j];j++);
     if(j==pat.Length())return start;
  }
  return -1;
}
```

---

## Slide 45: String Matching The Knuth-Morris-Pratt Algorithm

```c
Definition: If p = p0p1…pn-1 is a pattern, then its failure function, f, is defined as
If a partial match is found such that si-j … si-1 = p0p1…pj-1 and si ≠ pj then matching may be resumed by comparing si and pf(j–1)+1 if j ≠ 0. If j = 0, then we may continue by comparing si+1 and p0.
```

---

## Slide 46: Fast Matching Example

- Suppose exists a string s and a pattern pat = ‘abcabcacab’, let’s try to match pattern pat in string s.
- j 0 1 2 3 4 5 6 7 8 9
- pat a b c a b c a c a b
- f -1 -1 -1 0 1 2 3 -1 0 1
- i -1 -1 -1 -1 0 1 2 3 -1 0
- s = ‘- a b c a ? ? . . . ?’
- pat = ‘a b c a b c a c a b’
- ‘a b c a b c a c a b’

- j = 4, pf(j-1)+1 = p1

- New start matching point

---

## Slide 47

```c
Void String::FailureFunction(){
  int lengthP=Length();
  f[0]=-1;
  for(int j=1;j<lengthP;j++){
    int i=f[j-1];
    while(str[j]!=str[i+1]&&(i>=0)) i=f[i];
    if(str[j]==str[i+1])
      f[j]=i+1;
    else
      f[j]=-1;
  }
}
```

---

## Slide 48

```c
int String::FastFind(String pat){
  int posP=0,posS=0;
  int lengthP=pat.Length(),lengthS=Length();
  while(posP<lengthP && posS<lengthS)
     if(pat.str[posP]==str[posS]){
        posP++; posS++;
     }else if(posP==0) posS++;
	       else posP=pat.f[posP-1]+1;
  if(posP<lengthP)return -1;
  else return posS-lengthP;
}
```

---

## Slide 49: Strings

- ADT of String, Textbook: pp. 114
- Function in C: (pp.89)
  - strcat, strncat
  - strcmp, strncmp
  - strcpy, strncpy
  - strlen
  - strchr, strrchr
  - strtok
  - strstr
  - …

---
