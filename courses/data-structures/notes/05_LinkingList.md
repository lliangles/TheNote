# 05_LinkingList

> 📌 **課程主題筆記**: 本文件由 `05_LinkingList.ppt` 完整擷取，包含所有投影片內容、階層清單、程式碼區塊、表格、圖表標籤與註記，共 74 頁投影片。

## Slide 1

- 資料結構
- Data Structure

- Chapter 4: Linking List
- 國立聯合大學
- 資訊管理學系
- 溫敏淦

---

## Slide 2: Review of Sequential Representations

- Previously introduced data structures, including array, queue, and stack, they all have the property that successive nodes of data object were stored a fixed distance apart.
- The drawback of sequential mapping for ordered lists is that operations such as insertion and deletion become expensive.
- Also sequential representation tends to have less space efficiency when handling multiple various sizes of ordered lists.

---

## Slide 3: Linked List

- A better solutions to resolve the aforementioned issues of sequential representations is linked lists.
- Elements in a linked list are not stored in sequential in memory. Instead, they are stored all over the memory. They form a list by recording the address of next element for each element in the list. Therefore, the list is linked together.
- A linked list has a head pointer that points to the first element of the list.
- By following the links, you can traverse the linked list and visit each element in the list one by one.

---

## Slide 4: Linked List Insertion

- To insert an element, GAT, into the three letter linked list (BAT,CAT,EAT,FAT,HAT):
  - Get a node that is currently unused; let its address be x.
  - Set the data field of this node to GAT.
  - Set the link field of x to point to the node after FAT, which contains HAT.
  - Set the link field of the node cotaining FAT to x.

---

## Slide 5: Linked List Insertion And Deletion

- first

- CAT

- BAT

- EAT

- FAT

- HAT

- GAT

- first

- CAT

- BAT

- EAT

- FAT

- GAT

- HAT

---

## Slide 6: Designing a List in C++

- Design Attempt 1: Use a global variable first which is a pointer of ThreeLetterNode.
  - Unable to access to private data members: data and link.
- Design Attempt 2: Make member functions public.
  - Defeat the purpose of data encapsulation.
- Design Attempt 3: Use of two classes. Create a class that represents the linked list. The class contains the items of another objects of another class.

---

## Slide 7: Program 4.1 Composite Classes

```c
class ThreeLetterList;  // forward delcarion
class ThreeLetterNode {
	friend class ThreeLetterList;
	private:
	      char data[3];
	      ThreeLetterNode * link;
};
class ThreeLetterList {
	public:
	      // List Manipulation operations
	.
	.
	private:
	      ThreeLetterNode *first;
};
```

---

## Slide 8: Nested Classes

```c
The Three Letter List problem can also use nested classes to represent its structure.
class ThreeLetterList {
public:
      // List Manipulation operations
.
.
private:
class ThreeLetterNode {  // nested class
public:
      char data[3];
      ThreeLetterNode *link;
};
ThreeLetterNode *first;
};
```

---

## Slide 9: Pointer Manipulation in C++

- Addition of integers to pointer variable is permitted in C++ but sometimes it has no logical meaning.
- Two pointer variables of the same type can be compared.
  - x == y, x != y, x == 0

> 📊 **圖表元素 / 標籤:** a, x

- x

- a

- b

- x

- y

> 📊 **圖表元素 / 標籤:** b, y

- b

- b

- y

- x = y

- *x = * y

---

## Slide 10: Define A Linked List Template

- A linked list is a container class, so its implementation is a good template candidate.
- Member functions of a linked list should be general that can be applied to all types of objects.
- When some operations are missing in the original linked list definition, users should not be forced to add these into the original class design.
- Users should be shielded from the detailed implementation of a linked list while be able to traverse the linked list.
- Solution => Use of ListIterator

---

## Slide 11: Program 4.6 Template of Linked Lists

```c
template <class T> classChain;
template <class T> class ChainNode {
	friend class Chain<T>;
	private:
	      T data;
	      ChainNode <T> *link;
};
template <class T> class Chain {
	public:
	      Chain () {first = 0;};
	      // List manipulation operations
	      .
	      .
	private:
	      ChainNode <T> *first;
};
```

---

## Slide 12: Program 4.10 Template of Linked Lists (Cont.)

```c
template <class T> class ChainIterator {
public:
	ChainIterator(ChainNode <T> *startNode=0){current=startNode;}
	T& operator*()const{return current->data;}
	T* operator->()const{return &current->data;}
	ChainIterator& operator++(){current=current->link; return *this;}
	ChainIterator& operator++(int){ChainIterator old=*this;
         current=current->link; return old;}
	bool operator !=(const ChainIterator right) const{return current!=right.current;}
	bool operator ==(const ChainIterator right) const{return current==right.current;}
Private:
	ChainNode<T>* current;  // points to a node in list
};
```

---

## Slide 13: Program 4.11 Attaching A Node To The End Of A List

```c
template <class T>
void Chain<T>::InsertBack(const T& e)
{
	if (first) {
	      last->link = new ChainNode<T>(e);
	      last = last->link;
     } else
         first = last = new ChainNode<T>(e);
}
```

---

## Slide 14: Program 4.11 Attaching A Node To The begin Of A List

```c
template <class T>
void Chain<T>::InsertFront(const T& e)
{
	if (first) {
	      ChainNode<T> *x=new ChainNode<T>(e);
	     x->link=first;
        first=x;
     } else
         first = last = new ChainNode<T>(e);
}
```

---

## Slide 15: Deletion A target Node

```c
template <class T>
void Chain<T>::InsertBefore(T tdata){
   ChainNode<T> *p=0,*n=first;
   while(n&&n->data!=tdata)
     p=n; n=n->link;
	if (n) {
      if(p){
	     p->link=n->link;    delete n;
      }
     } else
         cout<<“target node is not found.”<<endl;
}
```

---

## Slide 16: Program 4.12 Concatenating Two Chains

```c
template <class T>
void Chain<T>:: Concatenate(Chain<T>& b)
{
	if (first){last->link=b.first; last=b.last;}
    else { first = b.first; last=b.last;}
    b.first=b.last=0;
}
```

---

## Slide 17: Program 4.13: Reverse List

```c
Template <class T>
void Chain<T>:: Reverse()
{
  ChinaNode <T> *current=first, *previous=0;
  while(current){
    ChainNode <T> *r=previous;
    previous=current;
    current=current->link;
    previous->link=r;
  }
  first=previous;
}
```

---

## Slide 18: When Not To Reuse A Class

- If efficiency becomes a problem when reuse one class to implement another class.
- If the operations required by the application are complex and specialized, and therefore not offered by the class.

---

## Slide 19: Circular Lists

- By having the link of the last node points to the first node, we have a circular list.
  - Need to make sure when current is pointing to the last node by checking for current->link == first.
  - Insertion and deletion must make sure that the circular structure is not broken, especially the link between last node and first node.

---

## Slide 20: Circular lists

- first

- X2

- X1

- X3

- data link

- X2

- X1

- X3

- last

- Head

- ------

- CAT

- BAT

- EAT

- WAT

---

## Slide 21: Diagram of A Circular List

- first

- last

---

## Slide 22: Insert Front & Back(rear)

```c
template <class T>
Void circularList <T>::InsertFront(const t& e){
  ChainNode <T> *newNode=new ChinaNode <T>(e);
  if(last){
    newNode->link=last->link;
    last->link=newNode;
  }else{
    last=newNode;
    newNode->link=newNode;
  }
}
```

```c
Last=newNode;
```

---

## Slide 23: Memory Leak

- When polynomials are created for computation and then later on out of the program scope, all the memory occupied by these polynomials is supposed to return to system. But that is not the case. Since ListNode<Term> objects are not physically contained in List<Term> objects, the memory they occupy is lost to the program and is not returned to the system. This is called memory leak.
- Memory leak will eventually occupy all system memory and causes system to crash.
- To handle the memory leak problem, a destructor is needed to properly recycle the memory and return it back to the system.

---

## Slide 24: List Destructor

```c
template <class Type>
List<Type>::~List()
// Free all nodes in the chain
{
	ListNode<Type>* next;
	for (; first; first = next) {
		next = first->link;
		delete first;
	}
}
```

---

## Slide 25: 4.5 Free Pool

- When items are created and deleted constantly, it is more efficient to have a circular list to contain all available items.
- When an item is needed, the free pool is checked to see if there is any item available. If yes, then an item is retrieved and assigned for use.
- If the list is empty, then either we stop allocating new items or use new to create more items for use.

---

## Slide 26: Free space list

```c
template <class T>
ChainNode <T>* CircularList <T>::GetNode(){
	ChainNode<T>* x;
	if(av){x=av; av=av->link;}
    else x=new ChainNode <T>;
    return x;
}
void CircularList<T>::RetNode(ChainNode<T>*& x){
  x->link=av; av=x; x=0;
}
void CircularList <T>::~CircularList(){
  if(last){
     ChainNode<T> *first=last->link;
     last->link=av; av=first; last=0;
} }
```

- Get a new node for list

- delete a node from list

- delete all nodes from list

---

## Slide 27: 4.6 Linked Stacks and Queues

- top

- front

- rear

- 0

- Linked Queue

- 0

- Linked Stack

- Program 4.19~4.22 (pp 198)

---

## Slide 28: 4.7 Revisit Polynomials

> 📊 **圖表元素 / 標籤:** 14, 3, 2, 8, 1, 0, a.first, -3, 10, 6, b.first

---

## Slide 29: Program 4.23 Polynomial Class Definition

```c
struct Term
// all members of Terms are public by default
{
	int coef;		// coefficient
	int exp;		// exponent
	Term Set(int c, int e) {coef = c; exp = e; return *this};
};
class Polynomial
{
	public:
	private:
	      Chain<Term> poly;
};
```

---

## Slide 30: Operating On Polynomials

- With linked lists, it is much easier to perform operations on polynomials such as adding and deleting.
  - E.g., adding two polynomials a and b

- a.first

- 1

- 0

- 14

- 0

- 8

- 3

- 2

- p

- 6

- 10

- 14

- 0

- 8

- b.first

- 10

- -3

- q

- (i) p->exp == q->exp

- c.first

- 0

- 14

- 11

---

## Slide 31: Operating On Polynomials

- a.first

- 1

- 0

- 14

- 0

- 8

- 3

- 2

- p

- 6

- 10

- 14

- 0

- 8

- b.first

- 10

- -3

- q

- c.first

- 0

- 14

- 0

- 11

- 10

- -3

- (ii) p->exp < q->exp

---

## Slide 32: Operating On Polynomials

- a.first

- 1

- 0

- 14

- 0

- 8

- 3

- 2

- p

- 6

- 10

- 14

- 0

- 8

- b.first

- 10

- -3

- q

- c.first

> 📊 **圖表元素 / 標籤:** 11, 14, 0

- 10

- -3

- 0

- 8

- 2

- (iii) p->exp > q->exp

- Program 4.24 (pp 206)
- O(m+n)

---

## Slide 33: Using Circular Lists For Polynomials

- By using circular lists for polynomials and free pool mechanism, the deleting of a polynomial can be done in a fixed amount of time independent of the number of terms in the polynomial.

---

## Slide 34: Polynomials with Circular List Structures

- last

- 1

- 0

- 14

- 8

- 3

- 2

- head

- 0

- -

- 14

- -1

- 3

- 1

- Program 4.25 (pp 209)
  - empty list
  - polynomials addition can be implemented by one loop

- head

- -

- -1

---

## Slide 35: 4.9 Linked List for Sparse Matrix

- Sequential representation of sparse matrix suffered from the same inadequacies as the similar representation of Polynomial.
- Circular linked list representation of a sparse matrix has two types of nodes:
  - head node: head, down, right, and next
  - entry node: head, down, row, col, right, value
- Head node i is the head node for both row i and column i.
- Each head node is belonged to three lists: a row list, a column list, and a head node list.
- For an nxm sparse matrix with r nonzero terms, the number of nodes needed is max{n, m} + r + 1.

---

## Slide 36: Node Structure for Sparse Matrices

- down

- head

- right

- down

- head

- right

- bool

- next

- value

- row

- col

- i

- j

- aij

- Head node

- Typical node

- Setup for aij

- A 4x4 sparse matrix

- Program 4.29 (pp 219)union {next, triple}

---

## Slide 37: Linked Representation of A Sparse Matrix

- H1

- H3

- H2

- H0

- Matrix head

> 📊 **圖表元素 / 標籤:** 4, 0, 2

- H0

- 11

> 📊 **圖表元素 / 標籤:** 1, 0

- H1

- 12

- 2

- 1

- H2

- -4

> 📊 **圖表元素 / 標籤:** 3

- H3

- -15

---

## Slide 38: sparse matrix—linking list version

```c
struct Triple>int row,col,val;}
class Matrix;
class MatrixNode{
  friend class Matrix;
  friend istream& operator>>(istream&,Matrix&);
  private:
    MatrixNode *down,*right;
    bool head;
    union{
      MatrixNode *nest;
      Triple triple;   //data
    }
    MatrixNode(bool,Triple *);
};
```

```c
MatrixNode::MatrixNode(bool b,Triple * t){
  head=b;
  if(b){right=down=this;}
  else triple=*t;
}
```

---

## Slide 39: Reading In A Sparse Matrix and Destractor of Matrix

- Assume the first line consists of the number of rows, the number of columns, and the number of nonzero terms. Then followed by num-terms lines of input, each of which is of the form: row, column, and value.
- Initially, the next field of head node i is to keep track of the last node in column i. Then the column field of head nodes are linked together after all nodes has been read in.
- Program 4.30, pp.221
- Program 4.31, pp.222

---

## Slide 40: Reading in a sparse matrix

```c
istream& operator>>(istream& is,Matrix& matrix){
  Triple s;
  is>>s.row>>s.col>>s.value;
  int p=max(s.row,s.col);
  matrix.headnode=new MatrixNode(false,&s);
  if(p==0){
    matrix.headnode->right=matrix.headnode; return is;}
  MatrixNode **head=new MatrixNode*[p];
  for(int i=0;i<p;i++)
    head[i]=new MatrixNode(true,0);
  int currentRow=0;
  int MatrixNode *last=head[0];
```

---

## Slide 41: Linked Representation of A Sparse Matrix

- H1

- H3

- H2

- H0

- Matrix headnode

> 📊 **圖表元素 / 標籤:** 4

- 0
- 1
- 2
- 3

> 📊 **圖表元素 / 標籤:** 0, 2

- H0

- 11

> 📊 **圖表元素 / 標籤:** 1, 0

- H1

- 12

- 2

- 1

- H2

- -4

> 📊 **圖表元素 / 標籤:** 3

- H3

- -15

- *right => row link
- *left => col link
- *next => head link

- head[i]

---

## Slide 42: Reading in a sparse matrix

```c
for(i=0;i<s.value;i++){
  Triple t;
  is>>t.row>>t.col>>t.value;
  if(t.row>currentRow){
    last->right=head[currentRow];
    currentRow=t.row;
    last=head[currentRow];
  }
  last=last->right
      =new MatrixNode(false, &t);
  head[t.col]->next=head[t.col]->
                     next->down=last;
}
```

```c
last->right=head[currentRow];
  for(i=0;i>s.col;i++)
    head[i]->next->down=head[i];
 for(i=0;i<p-1;i++)
    head[i]->next=head[i+1];
  head[p-1]->next=matrix.headnode;
  matrix.headnode->right=head[0];
  delete[] head;
  return is;
}
```

---

## Slide 43: Complexity Analysis

- Input complexity: O(max{n, m} + r) = O(n + m + r)
- Complexity of ~Maxtrix(): Since each node is in only one row list, it is sufficient to return all the row lists of a matrix. Each row is circularly linked, so they can be erased in a constant amount of time. The complexity is O(m+n).

---

## Slide 44: 4.10 Doubly Linked Lists

- The problem of a singly linked list is that supposed we want to find the node precedes a node ptr, we have to start from the beginning of the list and search until find the node whose link field contains ptr.
- To efficiently delete a node, we need to know its preceding node. Therefore, doubly linked list is useful.
- A node in a doubly linked list has at least three fields: left link field (llink), a data field (item), and a right link field (rlink).

---

## Slide 45: Doubly Linked List

- A head node may also be used in a doubly linked list to allow us to implement our operations more easily.

- rlink

- item

- llink

- Head Node

- rlink

- item

- llink

- Empty List

---

## Slide 46: Deletion From A Doubly Linked Circular List

- rlink

- item

- llink

- (Header Node) first

- Program 4.33 (pp 226)

```c
void DblList::Delete(DblListNode *x){
  if(x==first)throw “Deleteion of header node isn’t permitted.”
  else{
    x->left->right=x->right;
    x->right->left=x->left;
    delete x;
  }
}
```

---

## Slide 47: Insertion Into An Empty Doubly Linked Circular List

- node

- node x

- newnode p

- Program 4.34 (pp 227)

```c
void DblList::Insert(DblListNode *p, DblListNode *x){
  p->left=x; p->right=x->right;
  x->right->left=p; x->right=p;
}
```

---

## Slide 48: 4.11 Generalized Lists

- Definition: A generalized list, A, is a finite sequence of n ≥ 0 elements, α0, α1, α2, …, αn-1, where αi, is either an atom or a list. The elements αi,0≤ i ≤ n – 1, that are not atoms are said to be the sublists of A.
- A list A is written as A = (α0, …, αn-1 ), and the length of the list is n.
- Conventionally, a capital letter is used to represent a list and a lower case letter is to represent an atom.
- The α0 is the head of list A and the rest (α1, …, αn-1) is the tail of list A.

---

## Slide 49: Generalized List Examples

```c
A = ( ): the null, or empty, list; its length is zero.
B = (a, (b, c)): a list of length of two; its first element is the atom a, and its second element is the linear list (b, c).
C = (B, B, ( )): A list of length of three whose first two elements are the list B, and the third element is the null list C.
D = (a,D): is a recursive list of length two; D corresponds to the infinite list D = (a, (a, (a, …))).
```

---

## Slide 50: Generalized Lists

- head(B) = ‘a’ and tail(B) = ((b, c)), head(tail(B) ) = (b, c) and tail(tail(B)) = ().
- Lists may be shared by other lists
- Lists may be recursive.

---

## Slide 51: Generalized List Application Example

- Consider the polynomial P(x, y, z) with various variables. It is obvious the sequential representation is not suitable to this.
- What if a linear list is used?
  - The size of the node will vary in size, causing problems in storage management.
- Let’s try the generalized list.

---

## Slide 52: Generalized List Application Example

- P(x, y, z) can be rewritten as follows:
- The above can be written as Cz2 + Dz. Both C and D are polynomials themselves but with variables x and y only.
- If we look at polynomial C only, it is actually of the form Ey3 + Fy2, where E and F are polynomial of x only.
- Continuing this way, every polynomial consists of a variable plus coefficient-exponent pairs. Each coefficient is itself a polynomial.

---

## Slide 53: PolyNode Class in C++

```c
enum Triple{ var, ptr, no };
class PolyNode
{
	PolyNode *next;
	int exp;
	Triple trio;
	union {
		char vble;
		PolyNode *down;
		int coef;
	};
};
```

---

## Slide 54: PolyNode in C++ (Cont.)

- trio == var: the node is a head node.
  - vble indicates the name of the variable. Or it is an integer point to the variable in a variable table.
  - exp is set to 0.
- trio == ptr: coefficient itself is a list and is pointed by the field dlink. exp is the exponent of the variable on which the list is based on.
- trio == no, coefficient is an integer and is stored in coef. exp is the exponent of the variable on which the list is based on.

---

## Slide 55: Representing 3x2y

- trio

- vble

- exp

- link

- trio

- vble

- exp

- link

- var

- y

- 0

- ptr

- 1

- 0

- var

- x

- 0

- no

- 3

- 2

- 0

- P

---

## Slide 56: Representation of P(x, y, z)

- P(x, y, z)

- v

- z

- 0

- p

- 2

- p

- 1

- 0

- v

- y

- 0

- p

- 3

- p

- 2

- 0

- v

- y

- 0

- p

- 4

- p

- 1

- 0

- v

- x

- 0

- n

- 2

- 0

- 0

- v

- x

- 0

- n

- 3

- 8

- 0

- v

- x

- 0

- n

- 1

- 10

- n

- 2

- 8

- 0

- v

- x

- 0

- n

- 1

- 4

- n

- 6

- 3

- 0

---

## Slide 57: Generalized List Representation Example

- a.first = 0 Empty list

- b.first

- f

- a

- t

- 0

- B=(a, (b, c))

- f

- b

- f

- c

- 0

- c.first

- t

- t

- t

- 0

- 0

- C=(B, B, ())

- d.first

- f

- a

- t

- 0

- D=(a, D)

---

## Slide 58: Recursive Algorithms For Lists

- A recursive algorithm consists of two components:
  - The recursive function (the workhorse); declared as a private function
  - A second function that invokes the recursive function at the top level (the driver); declared as a public function.

---

## Slide 59: Program 4.35 Copying A List

```c
// Driver
void GenList::Copy(const GenList& l)
{
	first = Copy(l.first);
}
// Workhorse
GenListNode* GenList::Copy(GenListNode *p)
// Copy the nonrecursive list with no shared sublists pointed at by p
{
	GenListNode *q = 0;
	if (p) {
		q = new GenListNode<T>;
		q->tag = p->tag;
		if (p->tag) q->down=Copy(p->down)
		else q->data = p->data;
		q->next = Copy(p->next);
	}
	return q;
}
```

---

## Slide 60: Linked Representation for A

- r

- b

- first

- t

- t

- 0

- t

- u

- v

- s

- f

- a

- f

- b

- 0

- t

- f

- e

- 0

- w

- x

- f

- c

- f

- d

- 0

- A((a,b),((c,d),e)

---

## Slide 61: Recursiveness GenList::Copy

| Level of recursion | Value of p | Continuing level | p | Continuing level | p |
| --- | --- | --- | --- | --- | --- |
| 1 | b | 2 | r | 3 | u |
| 2 | s | 3 | u | 4 | v |
| 3 | t | 4 | w | 5 | 0 |
| 4 | 0 | 5 | x | 4 | v |
| 3 | t | 6 | 0 | 3 | u |
| 2 | s | 5 | x | 2 | r |
| 1 | b | 4 | w | 3 | 0 |
|  |  |  |  | 2 | r |
|  |  |  |  | 1 | b |

---

## Slide 62: Important List Functions

- List Equality (Program 4.36)
- List Depth (Program 4.37)
  - An empty list has depth 0.

---

## Slide 63: Reference Counts, Shared and Recursive Lists

- Lists may be shared by other lists for the purpose of space saving.
- Lists that are shared by other lists create problems when performing add or delete functions. For example, let’s look at the previous A, B, C, D example. When deleting the front node of list A would requires List B to update its pointers.
- The use of the data field of a head node to record the reference count can resolve the aforementioned problem. The list can not be deleted unless the reference count is 0.

---

## Slide 64: Example of Reference Counts, Shared and Recursive Lists

- a.first

- f

- 1

- 0

- B=(a, (b, c))

- b.first

- f

- 3

- f

- a

- t

- 0

- f

- 1

- f

- b

- f

- c

- 0

- c.first

- f

- 1

- t

- t

- t

- 0

- C=(B, B, ())

- d.first

- f

- 2

- f

- a

- t

- 0

- f

- 1

- 0

- D=(a, D)

---

## Slide 65: Erasing A List Recursively

```c
// Driver
GenList::~GenList()
// Each head node has a reference count. We assume first ≠ 0.
{
	Delete(first);
	first = 0;
}
// Workhorse
void GenList::Delete(GenListNode* x)
{
	x->ref--;	// decrement reference coutn of head node.
	if (!x->ref)
	{
		GenListNode *y = x; // y traverses top-level of x.
		while (y->next) { y= y->next; if (y->tag == 1) Delete (y->down);}
		y->next= av; // Attach top-level nodes to av list
		av = x;
	}
}
```

---

## Slide 66: Issue In Erasing Recursive Lists

- When erasing a recursive list (either direct recursive or indirect recursive), the reference count does not become 0. Then the nodes are not returned to available list. This will cause memory leak issue.

---

## Slide 67

---

## Slide 68: 4.8 Equivalence Class

- For any polygon x, x ≡ x. Thus, ≡ is reflexive.
- For any two polygons x and y, if x ≡ y, then y ≡ x. Thus, the relation ≡ is symetric.
- For any three polygons x, y, and z, if x ≡ y and y ≡ z, then x ≡ z. The relation ≡ is transitive.

---

## Slide 69: Equivalence

- Definition: A relation ≡ over a set S, is said to be an equivalence relation over S iff it is symmetric, reflexive, and transitive over S.
- Example: Supposed 12 polygons 0 ≡ 4, 3 ≡ 1, 6 ≡ 10, 8 ≡ 9, 7 ≡ 4, 6 ≡ 8, 3 ≡ 5, 2 ≡ 11, and 11 ≡ 0. Then they are partitioned into three equivalence classes:
- {0, 2, 4, 7, 11}; {1 , 3, 5}; {6, 8, 9 , 10}

---

## Slide 70: Equivalence (Cont.)

- Two phases to determine equivalence
  - In the first phase the equivalence pairs (i, j) are read in and stored.
  - In phase two, we begin at 0 and find all pairs of the form (0, j). Continue until the entire equivalence class containing 0 has been found, marked, and printed.
- Next find another object not yet output, and repeat the above process.

---

## Slide 71: Equivalence

- Definition: A relation ≡ over a set S, is said to be an equivalence relation over S iff it is symmetric, reflexive, and transitive over S.
- Example: Supposed 12 polygons 0 ≡ 4, 3 ≡ 1, 6 ≡ 10, 8 ≡ 9, 7 ≡ 4, 6 ≡ 8, 3 ≡ 5, 2 ≡ 11, and 11 ≡ 0. Then they are partitioned into three equivalence classes:
- {0, 2, 4, 7, 11}; {1 , 3, 5}; {6, 8, 9 , 10}

---

## Slide 72: Equivalence (Cont.)

- Two phases to determine equivalence
  - In the first phase the equivalence pairs (i, j) are read in and stored.
  - In phase two, we begin at 0 and find all pairs of the form (0, j). Continue until the entire equivalence class containing 0 has been found, marked, and printed.
- Next find another object not yet output, and repeat the above process.

---

## Slide 73: Equivalence Classes (Cont.)

- If a Boolean array pairs[n][n] is used to hold the input pairs, then it might waste a lot of space and its initialization requires complexity Θ(n2) .
- The use of linked list is more efficient on the memory usage and has less complexity, Θ(m+n) .

---

## Slide 74: Linked List Representation

- [0]

- [1]

- [2]

- [3]

- [4]

- [5]

- [6]

- [7]

- [8]

- [9]

- [10]

- [11]

- data

- 11

- 3

- 11

- 5

- 7

- 3

- 8

- 4

- 6

- 8

- 6

- 0

- link

- 0

- 0

- 0

- 0

- 0

- 0

- data

- 4

- 1

- 0

- 10

- 9

- 2

- link

- 0

- 0

- 0

- 0

- 0

- 0

- Program 4.27,4.28 (pp 213~215)
- O(m+n)

---
