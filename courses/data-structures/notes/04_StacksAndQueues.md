# 04_StacksAndQueues

> 📌 **課程主題筆記**: 本文件由 `04_StacksAndQueues.ppt` 完整擷取，包含所有投影片內容、階層清單、程式碼區塊、表格、圖表標籤與註記，共 41 頁投影片。

## Slide 1

- 資料結構
- Data Structure

- Chapter 3: Stacks and Queues
- 國立聯合大學
- 資訊管理學系
- 溫敏淦

---

## Slide 2: Templates in C++

- Template function in C++ makes it easier to reuse classes and functions.
- A template can be viewed as a variable that can be instantiated to any data type, irrespective of whether this data type is a fundamental C++ type or a user-defined type.

---

## Slide 3: Selection Sort Template

```c
Template <class T>
void sort(T *a, int n)
// sort the n Ts a[0] to a[n-1] into nondecreasing order
{
	for (int i = 0; i < n; i++)
	{
	      int j = i;
	      // find smallest T in a[i] to a[n-1]
	      for (int k = i+1; k < n; k++)
		if (a[k] < a[j]) { j = k;}
	      // interchange
	      T temp = a[i]; a[i] = a[j]; a[j] = temp;
	}
}
		float farray[100];
		int intarray[200];
		myClass objarray[150];
		………..
		sort(farray, 100);
		sort(intarray, 200);
		sort(objarray, 150);
```

---

## Slide 4: Template (Cont.)

- Can we use the sort template for the Rectangle class?
- Well, not directly. We’ll need to use operator overloading to implement “>” for Rectangle class.

---

## Slide 5: Stack

- What is a stack? A stack is an ordered list in which insertions and deletions are made at one end called the top. It is also called a Last-In-First-Out (LIFO) list.

---

## Slide 6: Stack (Cont.)

- Given a stack S = (a0, …, an-1), a0 is the bottom element, an-1 is the top element, and ai is on top of element ai-1, 0 < i < n.

- a3

- a3

- a2

- a2

- a1

- a1

- a0

- a0

- Push (Add)

- Pop (Delete)

---

## Slide 7: System Stack

- Whenever a function is invoked, the program creates a structure, referred to as an activation record or a stack frame, and places iton top of the system stack.

- previous frame pointer

- fp

- a1

- return address

- local variables

- fp

- previous frame pointer

- previous frame pointer

- return address

- return address

- main

- main

---

## Slide 8: ADT 3.1 Abstract Data Type Stack

```c
Template <class T>
class Stack
{   // objects: A finite ordered list with zero or more elements
	private:
	      T *stack;
	      // Create an empty stack whose maximum size is MaxStackSize
	      int top;
	      // if number of elements in the stack is equal to the maximum size
	      // of the stack, return TRUE(1) else return FALSE(0)
	      int capacity;
};
Template <class T>
Stack<T>::Stack(int stackCapacity):capacity(stackCapacity){
  if(capacity<1) throw “stack capacity must be >0”;
  statck=new T[capacity];
  top= -1;
}
```

---

## Slide 9: ADT 3.1 Abstract Data Type Stack

```c
Template <class T>
class Stack
{   // objects: A finite ordered list with zero or more elements
	public:
	      Stack (int StackCapcity = DefaultSize);
	      // Create an empty stack whose maximum size is MaxStackSize
	      Boolean IsFull();
	      // if number of elements in the stack is equal to the maximum size
	      // of the stack, return TRUE(1) else return FALSE(0)
	      Boolean IsEmpty();
	      // if number of elements in the stack is 0, return TRUE(1) else return FALSE(0)
	      void Push(const T& item);
	      // if IsFull(), then StackFull(); else insert item into the top of the stack.
	      T* Pop(T& );
	      // if IsEmpty(), then StackEmpty() and return 0;
	      // else remove and return a pointer to the top element of the stack.
	      T& Top() const;
};
```

---

## Slide 10: Implementation of Stack by Array

- an-1

- a2

- a1

- a0

- an-1

- a0

- a1

- a2

- Array index

- 0

- 1

- 2

- 3

- n-1

---

## Slide 11: Queue

- A queue is an ordered list in which all insertions take place at one end and all deletions take place at the opposite end. It is also known as First-In-First-Out (FIFO) lists.

- an-1

- a0

- a1

- a2

- rear

- front

---

## Slide 12: ADT 3.2 Abstract Data Type Queue

```c
Template <class T>
class Queue
{
	// objects: A finite ordered list with zero or more elements
	public:
	      Queue(int MaxQueueSize = DefaultSize);
	      // Create an empty queue whose maximum size is MaxQueueSize
	      Boolean IsFull() const;
	      // if number of elements in the queue is equal to the maximum size of
	      // the queue, return TRUE(1); otherwise, return FALSE(0)
	      void Add(const T& item);
	      // if IsFull(), then QueueFull(); else insert item at rear of the queue
	      Boolean IsEmpty() const;
	      // if number of elements in the queue is equal to 0, return TRUE(1)
	      // else return FALSE(0)
	      T* Delete(T&);
	      // if IsEmpty(), then QueueEmpty() and return 0;
	      // else remove the item at the front of the queue and return a pointer to it
	      T& Front() const;
	      T& Rear() const;
};
```

---

## Slide 13: Queue Manipulation Issue

- It’s intuitive to use array for implementing a queue. However, queue manipulations (add and/or delete) will require elements in the array to move. In the worse case, the complexity is of O(MaxSize).

---

## Slide 14: Shifting Elements in Queue

- rear

- front

- front

- rear

- rear

- front

---

## Slide 15: Circular Queue

- To resolve the issue of moving elements in the queue, circular queue assigns next element to q[0] when rear == MaxSize – 1.
- Pointer front will always point one position counterclockwise from the first element in the queue.
- Queue is empty when front == rear. But it is also true when queue is full. This will be a problem.

---

## Slide 16: Circular Queue (Cont.)

- rear

- 4

- 4

- J4

- n-4

- n-4

- J3

- 3

- 3

- J1

- J2

- n-3

- n-3

- J2

- J1

- 2

- 2

- J3

- J4

- n-2

- n-2

- 1

- 1

- n-1

- n-1

- 0

- 0

- front

- rear

- front

---

## Slide 17: Circular Queue (Cont.)

- To resolve the issue when front == rear on whether the queue is full or empty, one way is to use only MaxSize – 1 elements in the queue at any time.
- Each time when adding an item to the queue, newrear is calculated before adding the item. If newrear == front, then the queue is full.
- Another way to resolve the issue is using a flag to keep track of last operation. The drawback of the method is it tends to slow down Add and Delete function.

---

## Slide 18: Subtyping and Inheritance in C++

- Inheritance is used to express subtype relationships between two ADTs.
- If B inherits from A, then B IS-a A. Also, A is more general than B.
  - VW Beetle IS-a Car; Eagle IS-a Bird

---

## Slide 19: Inheritance

- A derived class inherits all the non-private members (data and functions) of the base class.
- Inherited members from public inheritance have the same level of access in the derived class as they did in the base class.
- The derived class can reuse the implementation of a function in the base class or implement its own function, with the exception of constructor and destructor.

---

## Slide 20: virtual function

```c
void showFooByPtr(Foo1 *foo) {
    foo->show();
}
void showFooByRef(Foo1 &foo) {
    foo.show();
}
int main() {
    Foo1 f1;
    Foo2 f2;
    // 動態繫結
    showFooByPtr(&f1);
    showFooByPtr(&f2);
    cout << endl;
    // 動態繫結
    showFooByRef(f1);
    showFooByRef(f2);
    cout << endl;
    // 靜態繫結
    f1.show();
    f2.show();
    char c=getch();
    return 0;
}
```

```c
class Foo1 {
public:
     virtual void show() { // 虛擬函式
        cout << "Foo1's show" << endl;
    }
};
```

```c
class Foo2 : public Foo1 {
public:
     void show() { // overriding
        cout << "Foo2's show" << endl;
    }
};
```

---

## Slide 21: Class Inheritance Example

- class Bag
- { public:
- Bag (int MaxSize = DefaultSize); // constructor
- virtual ~Bag(); // destructor
- virtual void Add(int); // insert element into bag
- virtual int* Delete (int&); //delete element from bag
- virtual Boolean IsFull(); // return TRUE if the bag is full; FALSE otherwise
- virtual Boolean IsEmpty(); // return TRUE if the bag is empty; FALSE otherwise
- protected:
- virtual void Full(); // action when bag is full
- virtual void Empty(); // action when bag is empty
```c
int *array;
	      int MaxSize;		// size of array
	      int top;		// highest position in array that contains an element
}
```

---

## Slide 22: Class Inheritance Example(Cont.)

```c
class Stack : public Bag
{	
	public:
	      Stack(int MaxSize = DefaultSize);	// constructor
	      ~Stack();				// destructor
	      int* Delete(int&);			// delete element from stack
};
Stack:: Stack (int MaxStackSize) : Bag(MaxStackSize) { }
// Constructor for Stack calls constructor for Bag
Stack::~Stack() { }
// Destructor for Bag is automatically called when Stack is destroyed. This ensures that array is deleted.
int* Stack::Delete(int& x)
{	if (IsEmpty()) {Empty(); return 0; }
	x = array[top--];
	return &x;
}
```

---

## Slide 23: Class Inheritance Example (Cont.)

```c
Bag b(3);   	// uses Bag constructor to create array of size 3
Stack s(3);	// uses Stack constructor to create array of size 3
b.Add(1); b.Add(2); b.Add(3);
// use Bag::Add. Bag::Add calls functions Bag::IsFull and Bag::Full
s.Add(1); s.Add(2); s.Add(3);
// Stack::Add not defined, so use Bag::Add. Bag::Add calls Bag::IsFull
// and Bag::Full because these have not been redefined in Stack
int x;
b.Delete(x);      // uses Bag::Delete, which calls Bag::IsEmpty and Bag::Emtpy
s.Delete(x);
// uses Stack::Delete, which calls Bag::IsEmtpy and Bag::Emtpy because these
// have not been redefined in Stack.
```

---

## Slide 24: The Maze Problem

- Entrance

- Exit

---

## Slide 25: The Maze Problem (Cont.)

- Stack is used in solving the maze problem for storing the coordinates and direction.
- Use of another mxp array to mark any position that has been visited before.

---

## Slide 26: Allowable Moves

- N

| q | move[q].a | move[q].b |
| --- | --- | --- |
| N | -1 | 0 |
| NE | -1 | 1 |
| E | 0 | 1 |
| SE | 1 | 1 |
| S | 1 | 0 |
| SW | 1 | -1 |
| W | 0 | -1 |
| NW | -1 | -1 |

- [i-1][j]

- [i-1][j-1]

- [i-1][j+1]

- NE

- NW

- X

- [i][j-1]

- [i][j+1]

- W

- E

- [i][j]

- [i+1][j]

- [i+1][j-1]

- [i+1][j+1]

- SW

- S

- SE

---

## Slide 27

```c
while(d<8){
          int g=i+move[d].a; int h=j+move[d].b;
          if(g==m)&&(h==p){
            cout<<stack;
            cout<<i<<" "<<j<<endl;
            cout<<m<<" "<<p<<endl;
            return;
           }
      if((!maze[g][h])&&(!mark[g][h])){
         mark[g][h]=1;
         temp.x=i;temp.y=j;temp.dir=d+1;
         stack.Push(temp);
         i=g;j=h;d=N;
      }else d++;
   }}
   cout<<"No Path in maze."<<endl;
}
```

```c
void Path(const int m, const int p)
{
  mark[1][1]=1;
  Stack <Items> stack(m*p);
  Items temp(1,1,E);
  Stack.Push(temp);
  while(!stack.IsEmpty()){
     temp=stack.Top();
     stack.Pop();
     int i=temp.x; int j=temp.y;
     int d=temp.dir;
```

---

## Slide 28: Expression

- X=6/2+4-5*2+5-6*3
- X= 3 +4-5*2+5-6*3
- X= 7-5*2+5-6*3
- X= 7- 10+5-6*3
- X= -3 +5-6*3
- X= 2 -6*3
- X= 2 - 18
- X= -16

- 28

---

## Slide 29: Infix

- Operand => Number/data
- Operator => + - * / ….
- Most operators will function on the operands in the two sides of operator
- Hard to process in computer

- 29

---

## Slide 30: Evaluation Expression in C++

- When evaluating operations of the same priorities, it follows the direction from left to right.

| Priority | Operator |
| --- | --- |
| 1 | Unary minus, ! |
| 2 | *, /, % |
| 3 | +, - |
| 4 | <, <=, >=, > |
| 5 | ==, != |
| 6 | && |
| 7 | \|\| |

---

## Slide 31: Postfix Notation

- Expressions are converted into Postfix notation before compiler can accept and process them.
- X = A/B – C + D * E – A * C
- Infix A/B–C+D*E–A*C
- Postfix => AB/C-DE*+AC*-

| Operation | Postfix |
| --- | --- |
| T1 = A / B | T1C-DE*+AC*- |
| T2 = T1 - C | T2 DE*+AC*- |
| T3 = D * E | T2T3+AC*- |
| T4 = T2 + T3 | T4AC*- |
| T5 = A * C | T4 T5 - |
| T6 = T4 - T5 | T6 |

---

## Slide 32: Evaluation of Postfix

- Meet operand (Number), push into stack
- Meet operator (+,-,*,/)
  - Pop two operands
  - Evaluate the two operand by the operator
  - Push the result into stack
- Meet eos
  - Pop from stack (It is the final result)

- 32

---

## Slide 33: Example 6 2 / 3 – 4 2 * +

| Token | Stack [0] [1] [2] | Top |
| --- | --- | --- |
| 6 2 / 3 - 4 2 * + | 6 6 2 6/2 3 3 3-3 0 4 0 4 2 0 4*2 0+8 | 0 1 0 1 0 1 2 1 0 |

- 33

---

## Slide 34: Evaluate in C++

```c
token=getToken();
while( token != eos ){
	if( token==operand)
		push(operand);
	else{
		op2=pop;
		op1=pop;
		push ( op1 operator op2 );
   }
	token=getToken();
}
return pop;
```

- 34

---

## Slide 35: Infix to Postfix by Hand

- Fully parenthesize the expression.
- Move all binary operators so that they replace their corresponding parentheses.
- Delete all parentheses.

- 35

---

## Slide 36: Example

- Origin: a/b-c+d*e-a*c
- Step 1: Fully parenthesize
  - ((((a/b)-c)+(d*e))-(a*c))
- Step 2: Move all operators
  - ((((a b /)-c)+(d*e))-(a*c))
  - ((((a b /) c -)+(d*e))-(a*c))
  - ((((a b /) c -)+(d e *))-(a*c))
  - ((((a b /) c -) (d e *) +)-(a*c))
  - ((((a b /) c -) (d e *) +)-(a c *))
  - ((((a b /)c -) (d e *) +) (a c *) -)
- Step 3: Remove parentheses
  - a b / c – d e * + a c * -

- ((((a/b)-c)+(d*e))-(a*c))

- 36

---

## Slide 37: Postfix

| Infix | Postfix |
| --- | --- |
| 2+3*4 a*b+5 (1+2)*7 a*b/c ((a/(b-c+d))*(e-a)*c) a/b-c+d*e-a*c | 2 3 4 * + a b * 5 + 1 2 + 7 * a b * c / a b c – d + / e a - * c * a b / c – d e * + a c * - |

- 37

---

## Slide 38: Parentheses

- If meet ‘( ‘ put ‘(‘ into stack
  - Never pop ‘(‘ till meet ‘)’
- If meet ‘)’
  - Pop all operators till meet ‘(‘
- ( ) + - * / %
- isp {0, 19, 12,12,13,13}
- icp {20, 19, 12, 12, 13,13 }

- 2026/9/20

- CH3: Stack and Queue

- 38

---

## Slide 39: Infix to Postfix in C++

```c
token=getToken();
while( token != eos)
	if( token == operand )
		ouput token;
	else if( token==‘)’)
		 output pop(stack) till ‘(’;
	else
		while( isp[stack[top]] >= icp[token] )
			output pop(stack);
		push(token);
while( !stackEmpty(stack) )
	output pop(stack);
```

- 39

---

## Slide 40: Infix to Postfix in C++

```c
void postfix(Expression e){
  Stack<Token> stack;
  stack.Push(“#”);
  for(Token x=NextToken(e);x!=“#”;x=NextToken(e))
	if( x == operand ) cout<<x;
	else if(x==“)”){
     for(;stack.Top()!=“(“;stack.Pop())
        cout<<stack.Top();
     stack.Pop();
   }else{
     for(;isp(stack.Top()<=icp(x);stack.Pop())
        cout<<stack.Top();
     stack.Push(x);
  }
```

- 40

---

## Slide 41: Infix to Postfix in C++

```c
for(;!stack.IsEmpty();cout<<stack.Top()stack.Pop())
     cout<<stack.Top();
   cout<<endl;
}
```

- 41

---
