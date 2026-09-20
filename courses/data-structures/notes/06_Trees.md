# 06_Trees

> 📌 **課程主題筆記**: 本文件由 `06_Trees.ppt` 完整擷取，包含所有投影片內容、階層清單、程式碼區塊、表格、圖表標籤與註記，共 118 頁投影片。

## Slide 1

- 資料結構
- Data Structure

- Chapter 5: Trees
- 國立聯合大學
- 資訊管理學系
- 温敏淦

---

## Slide 2: 5.1 Trees

- Definition: A tree is a finite set of one or more nodes such that:
  - There is a specially designated node called the root.
  - The remaining nodes are partitioned into n ≥ 0 disjoint sets T1, …, Tn, where each of these sets is a tree. We call T1, …, Tn the subtrees of the root.

---

## Slide 3: Pedigree Genealogical Chart

- Dusty

- Brandy

- Honey Bear

- Kelly

- Richard

- John

- Terry

- Jack

- Anthony

- Michelle

- Mary

- Karen

- Joe

- Mike

- Angela

- Binary Tree

---

## Slide 4: Lineal Genealogical Chart

- Proto Indo-European

- Italic

- Hellenic

- Germanic

- Osco-Umbrian

- Latin

- Greek

- North Germanic

- West Germanic

- Osco

- Umbrian

- Spanish

- French

- Italian

- Icelandic

- Norwegian

- Swedish

- Low

- High

- Yiddish

---

## Slide 5: Tree Terminology

- Normally we draw a tree with the root at the top.
- The degree of a node is the number of subtrees of the node.
- The degree of a tree is the maximum degree of the nodes in the tree.
- A node with degree zero is a leaf or terminal node.
- A node that has subtrees is the parent of the roots of the subtrees, and the roots of the subtrees are the children of the node.
- Children of the same parents are called siblings.

---

## Slide 6: Tree Terminology (Cont.)

- The ancestors of a node are all the nodes along the path from the root to the node.
- The descendants of a node are all the nodes that are in its subtrees.
- Assume the root is at level 1, then the level of a node is the level of the node’s parent plus one.
- The height or the depth of a tree is the maximum level of any node in the tree.

---

## Slide 7: A Sample Tree

- Level

- A

- 1

- 2

- B

- C

- D

- 3

- E

- F

- G

- H

- I

- J

- 4

- K

- L

- M

---

## Slide 8: List Representation of Trees

> 🖼️ *(包含圖形 / 示意圖)*

- (A(B(E(K,L),F),C(G),D(H(M),I,J)))

- A

- 0

- B

- F

- 0

- C

- G

- 0

- D

- I

- J

- 0

- E

- K

- L

- 0

- H

- M

- 0

- Same representation to previous figure

---

## Slide 9: Possible Node Structure For A Tree of Degree

- Lemma 5.1: If T is a k-ary tree (i.e., a tree of degree k) with n nodes, each having a fixed size as in Figure 5.4, then n(k-1) + 1 of the nk child fileds are 0, n ≥ 1.

- nk-(n-1)

- Child k

- …

- Child 4

- Child 3

- Child 2

- Child 1

- Data

- Wasting memory!

---

## Slide 10: Representation of Trees

> 🖼️ *(包含圖形 / 示意圖)*

- Left Child-Right Sibling Representation
  - Each node has two links (or pointers).
  - Each node only has one leftmost child and one closest sibling.

- A

- data

- left child

- right sibling

- B

- C

- D

- E

- F

- G

- H

- I

- J

- K

- L

- M

---

## Slide 11: Degree Two Tree Representation

- A

- B

- C

- E

- F

- K

- G

- D

- Binary Tree!

- L

- H

- M

- I

- J

---

## Slide 12: 5.2 Binary Tree

- Definition: A binary tree is a finite set of nodes that is either empty or consists of a root and two disjoint binary trees called the left subtree and the right subtree.
- There is no tree with zero nodes. But there is an empty binary tree.
- Binary tree distinguishes between the order of the children while in a tree we do not.

---

## Slide 13: Tree Representations

- A

- A

- A

- B

- B

- B

- A

- A

- A

- B

- C

- B

- B

- C

- C

- Left child-right sibling

- Binary tree

---

## Slide 14: Binary Tree Examples

- A

- A

> 📊 **圖表元素 / 標籤:** A, B

- B

- B

- C

- C

- D

- E

- F

- G

> 📊 **圖表元素 / 標籤:** A, B

- D

- H

- I

- E

- Complete tree

- Skewed tree

---

## Slide 15: The Properties of Binary Trees

- Lemma 5.2 [Maximum number of nodes]
  - The maximum number of nodes on level i of a binary tree is 2i-1, i ≥ 1.
  - The maximum number of nodes in a binary tree of depth k is 2k – 1, k ≥ 1.
- Lemma 5.3 [Relation between number of leaf nodes and nodes of degree 2]: For any non-empty binary tree, T, if n0 is the number of leaf nodes and n2 the number of nodes of degree 2, then n0 = n2 + 1.
- Definition: A full binary tree of depth k is a binary tree of depth k having 2k – 1 nodes, k ≥ 0.

- n=n0+n1+n2 n=B+1 B=n1+n2*2
- n1+n2*2+1 = n0+n1+n2

---

## Slide 16: Complete Binary Tree

- Definition: A binary tree with n nodes and depth k is complete iff its nodes correspond to the nodes numbered from 1 to n in the full binary tree of depth k.

- level

- 1

- 1

- 2

- 2

- 3

- 3

- 6

- 4

- 7

- 5

- 4

- 12

- 13

- 8

- 9

- 14

- 15

- 10

- 11

---

## Slide 17: Array Representation of A Binary Tree

- Lemma 5.4: If a complete binary tree with n nodes is represented sequentially, then for any node with index i, 1 ≤ i ≤ n, we have:
  - parent(i) is at if i ≠1. If i = 1, i is at the root and has no parent.
  - left_child(i) is at 2i if 2i ≤ n. If 2i > n, then i has no left child.
  - right_child(i) is at 2i + 1 if 2i + 1 ≤ n. If 2i + 1 > n, then i has no right child.
- Position zero of the array is not used.

---

## Slide 18: Proof of Lemma 5.4 (2)

- Assume that for all j, 1 ≤ j ≤ i, left_child(j) is at 2j. Then two nodes immediately preceding left_child(i + 1) are the right and left children of i. The left child is at 2i. Hence, the left child of i + 1 is at 2i + 2 = 2(i + 1) unless 2(i + 1) > n, in which case i + 1 has no left child.

---

## Slide 19: Array Representation of Binary Trees

- A

- [1]

> 📊 **圖表元素 / 標籤:** A, B, C, D, E, [1], [2], [3], [4], [5], [6], [7], [8], [9], [16]

- [2]

- B

- C

- [3]

- [4]

- D

- [5]

- E

- [6]

- F

- G

- [7]

- [8]

- H

- I

- [9]

---

## Slide 20: Linked Representation

```c
class Tree;
class TreeNode {
friend class Tree;
private:
	TreeNode *LeftChild;
	char data;
	TreeNode *RightChild;
};
class Tree {
public:
// Tree operations
.
private:
	TreeNode *root;
};
```

---

## Slide 21: Node Representation

- data

- LeftChild

- RightChild

- LeftChild

- data

- RightChild

---

## Slide 22: Linked List Representation For The Binary Trees

- root

- root

- A

- 0

> 📊 **圖表元素 / 標籤:** A

- B

- 0

- C

- B

- C

- 0

- D

> 📊 **圖表元素 / 標籤:** E

- F

- 0

- G

- 0

- D

- 0

> 📊 **圖表元素 / 標籤:** H, 0, I

- 0

- E

- 0

---

## Slide 23: 5.3 Tree Traversal

- When visiting each node of a tree exactly once, this produces a linear order for the node of a tree.
- There are 3 traversals if we adopt the convention that we traverse left before right: LVR (inorder), LRV (postorder), and VLR (preorder).
- When implementing the traversal, a recursion is perfect for the task.

---

## Slide 24: Binary Tree With Arithmetic Expression

- +

- *

- E

- *

- D

- /

- C

- A

- B

- A/B*C*D+E +**/ABCDE AB/C*D*E+

---

## Slide 25: Tree Traversal

- Inorder Traversal: A/B*C*D+E
  - => Infix form (program 5.1)
- Preorder Traversal: +**/ABCDE
  - => Prefix form (program 5.2)
- Postorder Traversal: AB/C*D*E+
  - => Postfix form (program 5.3)

---

## Slide 26

```c
template <class T>
void Tree<T>::Preorder(){
  Preorder(root);
}
template <class T>
void Tree<T>::Preorder(TreeNode<T> *p){
  if(p){
  Visit(p);
   Preorder(p->leftChild);
   Preorder(p->rightChild);
}
```

```c
template <class T>
void Tree<T>::Inorder(){
  Inorder(root);
}
template <class T>
void Tree<T>::Inorder(TreeNode<T> *p){
  if(p){
    Inorder(p->leftChild);
    Visit(p);
    Inorder(p->rightChild);
  }
}
```

- program 5.2

```c
template <class T>
void Tree<T>::Postorder(){
  Postorder(root);
}
template <class T>
void Tree<T>::Postorder(TreeNode<T> *p){
  if(p){
   Postorder(p->leftChild);
   Posteorder(p->rightChild);
   Visit(p);
}
```

- program 5.1

- program 5.3

---

## Slide 27: Iterative Inorder Traversal

```c
void Tree::NonrecInorder()
// nonrecursive inorder traversal using a stack
{
	Stack<TreeNode *> s;	// declare and initialize stack
	TreeNode *CurrentNode = root;
	while (1) {
		while (CurrentNode) { // move down LeftChild fields
		      s.Push(CurrentNode);	// add to stack
		      CurrentNode = CurrentNode->LeftChild;
		}
		if (s.IsEmpty()) return;	// stack is empty
	        CurrentNode = s.Top();
              s.Pop();
		Visit(CurrentNode);    //cout << CurrentNode->data << endl;
		CurrentNode = CurrentNode->RightChild;
	}
}
```

- O(2n0+n1=n0+n1+n2+1=n+1)

- n0 = n2 + 1

- O(n)

---

## Slide 28: Level-Order Traversal

- All previous mentioned schemes use stacks.
- Level-order traversal uses a queue.
- Level-order scheme visit the root first, then the root’s left child, followed by the root’s right child.
- All the node at a level are visited before moving down to another level.

---

## Slide 29: Level-Order Traversal of A Binary Tree

> 🖼️ *(包含圖形 / 示意圖)*

```c
void Tree::LevelOrder()
// Traverse the binary tree in level order
{
	Queue<TreeNode *> q;
	TreeNode *CurrentNode = root;
	while (CurrentNode) {
		cout << CurrentNode->data<<endl;
		if (CurrentNode->LeftChild) q.Push(CurrentNode->LeftChild);
		if (CurrentNode->RightChild) q.Push(CurrentNode->RightChild);
              if(q.IsEmpty())return;
		CurrentNode = q.Front();
              q.Pop();
	}
}
```

- +*E*D/CAB

---

## Slide 30: Traversal Without A Stack

- Use of parent field to each node.
- Use of two bits per node to represents binary trees as threaded binary trees.
- Program 5.8(exercise)
  - Space complexity O(1)

---

## Slide 31: 5.4 Some Other Binary Tree Functions

- With the inorder, postorder, or preorder mechanisms, we can implement all needed binary tree functions. E.g.,
  - Copying Binary Trees (program 5.9)
  - Testing Equality (program 5.10)
    - Two binary trees are equal if their topologies are the same and the information in corresponding nodes is identical.

---

## Slide 32

```c
template <class T>
bool Tree<T>::operator==(Tree &t){
  return Equal(root,t.root);
}
template <class T>
bool Tree<T>::Equal(TreeNode<T> *p, TreeNode<T>*q){
  if(!p&&!q) return true;
  return(p&&q && p->data==q->data &&
  Equal(p->leftChild,q->leftChild) &&
  Equal(p->rightChild,q->rightChild)
}
```

- program 5.10

```c
template <class T>
void Tree<T>::Tree(Tree <T> *s){
  root=Copy(s.root);
}
template <class T>
TreeNode<T> *Tree <T>::Copy(TreeNode<T> *p){
  if(!p)return 0;
  return new TreeNode<T>(p->data,
      Copy(p->LeftChild),
      Copy(p->RightChild));
}
```

- program 5.9

---

## Slide 33: The Satisfiability Problem

- Expression Rules
  - A variable is an expression
  - If x and y are expressions then
  - are expressions
  - Parentheses can be used to alter the normal order of evaluation, which is not before and before or.

---

## Slide 34: Propositional Formula In A Binary Tree

- x3

- x1

- x3

- x2

- x1

- O(g2n)

- n variable testing

---

## Slide 35: Perform Formula Evaluation

- To evaluate an expression, we can traverse its tree in postorder.
- To perform evaluation, we assume each node has four fields
  - LeftChild
  - data
    - first:operator
    - second:result value
  - RightChild

- data

- LeftChild

- RightChild

- second

- first

---

## Slide 36: First Version of Satisfiability Algorithm

```c
For all 2n possible truth value combinations for the n variables
{
  generate the next combination;
  replace the variables by their values;
  evaluate the formula by traversing the tree it points to in postorder;
  if (formula.Data().second()) {cout << current combination; return;}
}
cout << “no satisfiable combination”;
```

---

## Slide 37: Evaluating A Formula

```c
void SatTree::PostOrderEval()  // Driver
{
	PostOrderEval(root);
}
void SatTree::PostOrderEval(SatNode * p)
{
	if (p) {
		PostOrderEval(p->LeftChild);
		PostOrderEval(p->RightChild);
		switch (p->data.first) {
		  case Not: p->data.second =!p->RightChild-> data.second; break;
		  case And: p-> data.second =p->LeftChild->data.second && p->RightChild-> data.second;
		                    break;
		  case Or: p-> data.second = p->LeftChild->data.second || p->RightChild-> data.second;
			break;
		  case True: p-> data.second = TRUE; break;
		  case False: p-> data.second = FALSE;
		}
	}
}
```

---

## Slide 38: 5.5 Threaded Binary Tree

- Threading Rules
  - A 0 RightChild field at node p is replaced by a pointer to the node that would be visited after p when traversing the tree in inorder. That is, it is replaced by the inorder successor of p.
  - A 0 LeftChild link at node p is replaced by a pointer to the node that immediately precedes node p in inorder (i.e., it is replaced by the inorder predecessor of p).

---

## Slide 39: Threaded Tree Corresponding to Figure 5.10(b)

- A

- B

- C

- D

- E

- F

- G

- H

- I

- Inorder sequence: H, D, I, B, E, A, F, C, G

---

## Slide 40: Threads

- To distinguish between normal pointers and threads, two boolean fields, LeftThread and RightThread, are added to the record in memory representation.
  - t->LeftThread = TRUE
    - => t->LeftChild is a thread
  - t->LeftThread = FALSE
    - => t->LeftChild is a pointer to the left child.

---

## Slide 41: Threads (Cont.)

- To avoid dangling threads, a head node is used in representing a binary tree.
- The original tree becomes the left subtree of the head node.
- Empty Binary Tree

- LeftThread

- LeftChild

- RightChild

- RightThread

- data

- TRUE

- FALSE

---

## Slide 42: Memory Representation of Threaded Tree of Figure 5.20

- -

- f

- f

- A

- f

- f

- B

- f

- f

- B

- f

- f

> 📊 **圖表元素 / 標籤:** f, D

- t

- E

- t

- f

- D

- f

- t

- E

- t

- H

- t

- I

- t

- t

- t

- H D I B E A D B E -

---

## Slide 43: Inorder Traversal of a Threaded Binary Tree

```c
Char* ThreadedInorderIterator::Next()
//Find the inorder successor of CurrentNode in a threaded binary tree
{
    ThreadedNode <T>*temp = CurrentNode -> RightChild;
    if (! CurrentNode -> RightThread)
         while (! temp -> LeftThread)
               temp = temp -> LeftChild;
    CurrentNode = temp;
    if (CurrentNode == root)
         return 0;
    else
         return  &CurrentNode -> data;
}
```

---

## Slide 44: Inserting A Node to A Threaded Binary Tree

- Inserting a node r as the right child of a node s.
  - If s has an empty right subtree, then the insertion is simple and diagram in Figure 5.23(a).
  - If the right subtree of s is not empty, the this right subtree is made the right subtree of r after insertion. When this is done, r becomes the inorder predecessor of a node that has a LeftThread==TRUE field, and consequently there is an thread which has to be updated to point to r. The node containing this thread was previously the inorder successor of s. Figure 5.23(b) illustrates the insertion for this case.

---

## Slide 45: Insertion of r As A Right Child of s in A Threaded Binary Tree

- s

- s

- r

- r

- after

- before

---

## Slide 46: Insertion of r As A Right Child of s in A Threaded Binary Tree (Cont.)

- s

- s

- r

- r

- after

- before

---

## Slide 47: Program 5.14 Inserting r As The Right Child of s

```c
void ThreadedTree::InsertRight(ThreadNode *s, ThreadedNode *r)
// Insert r as the right child of s
{
	r->RightChild = s->RightChild;
	r->RightThread = s->RightThread;
	r->LeftChild = s;
	r->LeftThread = TRUE;	// LeftChild is a thread
	s->RightChild = r;	// attach r to s
	s->RightThread = FALSE;
	if (!r->RightThread) {
		ThreadedNode <T>*temp = InorderSucc(r); // returns the inorder successor of r
		temp->LeftChild = r;
	}
}
```

- Program ???

---

## Slide 48: 5.6 Heap Priority Queues

- In a priority queue, the element to be deleted is the one with highest (or lowest) priority.
- An element with arbitrary priority can be inserted into the queue according to its priority.
- A data structure supports the above two operations is called max (min) priority queue.

---

## Slide 49: Examples of Priority Queues

- Suppose a server that serve multiple users. Each user may request different amount of server time. A priority queue is used to always select the request with the smallest time. Hence, any new user’s request is put into the priority queue. This is the min priority queue.
- If each user needs the same amount of time but willing to pay more money to obtain the service quicker, then this is max priority queue.

---

## Slide 50: Priority Queue Representation

- Unorder Linear List
  - Addition complexity: O(1)
  - Deletion complexity: O(n)
- Chain
  - Addition complexity: O(1)
  - Deletion complexity: O(n)
- Ordered List
  - Addition complexity: O(n)
  - Deletion complexity: O(1)

---

## Slide 51: Max (Min) Heap

- Heaps are frequently used to implement priority queues. The complexity is O(log n).
- Definition: A max (min) tree is a tree in which the key value in each node is no smaller (larger) than the key values in its children (if any). A max heap is a complete binary tree that is also a max tree. A min heap is a complete binary tree that is also a min tree.

---

## Slide 52: Max Heap Examples

- 9

- 14

- 3

- 6

- 12

- 7

- 8

- 10

- 6

- 5

---

## Slide 53: Insertion Into A Max Heap (1)

- 20

- 20

- 15

- 2

- 15

- 2

- 10

- 10

- 1

- 14

- 14

---

## Slide 54: Insertion Into A Max Heap (2)

- 20

- 20

- 2

- 15

- 5

- 5

- 15

- 2

- 14

- 10

- 10

- 2

- 14

- 5

- bubbling up

---

## Slide 55: Insertion Into A Max Heap (3)

- 20

- 20

- 15

- 15

- 2

- 2

- 14

- 10

- 10

- 21

- 14

- Program 5.16

---

## Slide 56: Program 5.16 Inserting a node into max heap

```c
Template <class<T>coid MaxHeap<T>::Push(const T&e){
  if(heapSize==capacity){
    ChangeSize_1D(heap,capacity,2*capacity);
    capacity*=2;
  }
  int currentNode=++heapSize;
  while(currentNode!=1 && heap[currentNode/2]<e){  //bubbling up
    heap[currentNode]=heap[currentNode/2];  //swap downward
    currentNode/=2;
  }
  heap[currentNode]=e;
}
```

- O(log n)

---

## Slide 57: Delete from A Max Heap

- 20

- 15

- 14

- 15

- 2

- 2

- 14

- 10

- 10

- Trickle down

---

## Slide 58: Deletion From A Max Heap Program 5.17

```c
template <class T>
void <T>* MaxHeap <T>::Pop()
// Delete from the max heap
{
	if (!IsEmpty()) {throw ”Heap is empty. Cannot delete”;}
	heap[1].~T();
     T lastE=heap[heapSize--];
     int currentNode=1;
     int child=2;
	while(child<=heapSize)
	{
		if (child < heapSize&&heap[child]<heap[child+1])child++;
		if (lastE>=heap[child]) break;
		heap[currentNode] = heap[child];
		chrrentNode = child; child *= 2;
	}
	heap[currentNode] = lastE;
}
```

---

## Slide 59: 5.7 Binary Search Tree – Dictionary implementation

- {key:value}

- Heap needs O(n) to perform deletion of a non-priority queue. This may not be the best solution.
- Binary search tree provide a better performance for search, insertion, and deletion.
- Definition: A binary serach tree is a binary tree. It may be empty. If it is not empty then it satisfies the following properties:
  - Every element has a key and no two elements have the same key (i.e., the keys are distinct)
  - The keys (if any) in the left subtree are smaller than the key in the root.
  - The keys (if any) in the right subtree are larger than the key in the root.
  - The left and right subtrees are also binary search trees.

---

## Slide 60: Binary search Trees

- 60

- 30

- 20

- 70

- 5

- 40

- 15

- 25

- 80

- 65

- 2

- 14

- 10

- 22

- Binary search trees

- Not binary search tree

---

## Slide 61: Searching A Binary Search Tree

- If the root is 0, then this is an empty tree. No search is needed.
- If the root is not 0, compare the x with the key of root.
  - If x equals to the key of the root, then it’s done.
  - If x is less than the key of the root, then no elements in the right subtree can have key value x. We only need to search the left tree.
  - If x larger than the key of the root, only the right subtree is to be searched.

---

## Slide 62: Searching A Binary Search Tree

- Program 5.18 recursive version

```c
if(!p)return 0; //not found
if(k<p->data.first)return Get(p->leftChild,k);
if(k>p->data.first)return Get(p->rightChild,k);
return &p->data;
```

- Program 5.19 iterative version

```c
currentnode=root;
while(currentNode){
  if(k<currentNode->data.first)
    currentNode=currentNode->LeftChild;
  else if(if(k>currentNode->data.first)
     currentNode=currentNode->rightChild;
  else return &currentNode->data;
return 0; //not found
```

---

## Slide 63: Search Binary Search Tree by Rank

- Search the binary search tree for the rth smallest element

- Rank =>order of the sorted sequence inoder traversal sequence
- To search a binary search tree by the ranks of the elements in the tree, we need additional field “LeftSize”.
- LeftSize is the number of the elements in the left subtree of a node plus one.
- It is obvious that a binary search tree of height h can be searched by key as well as by rank in O(h) time.

---

## Slide 64: Search by Rank

- 20

- 4,L=4

- 3,L=3

- 15

- 25

- 6,L=2

- 22

- 1,L=1

- 10

- 5,L=1

- 2,L=1

- 14

---

## Slide 65: Searching A Binary Search Tree by Rank

```c
template <class K, class E>
pair<K,E>* BST<Type>::RankGet(int r)
// Search the binary search tree for the rth smallest element
{
	TreeNode<pair<K,E>> *currentNode = root;
	while(currentNode)
	{
		if (r < currentNode->leftSize) currentNode=currentNode->leftChild;
		if (r > currentNode->leftSize){
		   r -= currentNode->leftSize;
		   currentNode = currentNode->rightChild;
		}else
                 return &currentNode->data;
	}
	return 0;
}
```

---

## Slide 66: Insertion To A Binary Search Tree

- Before insertion is performed, a search must be done to make sure that the value to be inserted is not already in the tree.
- If the search fails, then we know the value is not in the tree. So it can be inserted into the tree on the failure branch.
- It takes O(h) to insert a node to a binary search tree.

- distinct

---

## Slide 67: Inserting Into A Binary Search Tree

- 35

- 80

- 30

- 30

- 40

- 5

- 40

- 5

- 2

- 80

- 2

---

## Slide 68: Insertion Into A Binary Search Tree

- data

- LeftChild

- RightChild

- second

- first

- value

- key

```c
Template <class k,class E>
void BST<K,E>::Insert(const pair<K,E> &thePair)
// insert thePair into the binary search tree
{
	// Search for thePair.key, pp is the parent of p
	TreeNode<pair<K,E>>*p = root,*pp = 0;
	while(p) {
		pp = p;
		if (thePair.first < p->data.first) p = p->LeftChild;
 		else if (thePair.first > p->data.first) p = p->RightChild;
		else{p->data.second=thePair.second;  return;}  // thePair.first is already in tree
	}
	// Perform insertion
	p = new TreeNode<pair<K,E>>(thePair) ;	
	if (root) {
          if (thePair.first < pp->data.first) pp->LeftChild = p;
	   else pp->RightChild = p;
	else root = p;
}
```

- O(h)

---

## Slide 69: Deletion From A Binary Search Tree

- Delete a leaf node
  - A leaf node which is a right child of its parent
  - A leaf node which is a left child of its parent
- Delete a non-leaf node
  - A node that has one child
    - Link parent link-field to child node
  - A node that has two children
    - Replaced by the largest element in its left subtree, or
    - Replaced by the smallest element in its right subtree
    - Then delete candidate node (leaf or one child)
- Again, the delete function has complexity of O(h)

---

## Slide 70: Deleting From A Binary Search Tree

- 30

- 30

- 30

- 40

- 5

- 2

- 40

- 5

- 2

- 80

- 35

- 2

- 80

---

## Slide 71: Deleting From A Binary Search Tree

- 30

- 30

- 30

- 30

- 30

- 2

- 40

- 5

- 2

- 40

- 5

- 2

- 40

- 2

- 2

- 80

- 2

- 80

- 80

---

## Slide 72: Deleting From A Binary Search Tree

- 30

- 30

- 5

- 30

- 5

- 30

- 2

- 40

- 5

- 2

- 40

- 5

- 2

- 40

- 2

- 2

- 80

- 2

- 80

- 80

---

## Slide 73: Joining and Splitting Binary Trees

- keys of tree A < x->key < keys of tree B

- C.ThreeWayJoin(A, x, B): Creates a binary search tree C that consists of binary search tree A, B, and element x.
- C.TwoWayJoin(A, B): Joins two binary search trees A and B to obtain a single binary search tree C.
- A.Split(i, B, x, C): Binary search tree A splits into three parts: B (a binary search tree that contains all elements of A that have key less than i); if A contains a key i than this element is copied into x and a pointer to x returned; C is a binary search tree that contains all records of A that have key larger than i.

- keys of tree B < i < keys of tree C

---

## Slide 74: ThreeWayJoin(A, x, B)

- 81

- 30

- 90

- 81

- 40

- 5

- 94

- 85

- 2

- 80

- 35

- 84

- 92

- A

- B

- x

---

## Slide 75: TwoWayJoin(A, B)

- 80

- 84

- 30

- 90

- 40

- 5

- 94

- 85

- 2

- 80

- 35

- 84

- 92

- A

- B

---

## Slide 76: A.Split(i, B, x, C)

- i = 30

- x

- 30

- 40

- 5

- 2

- 80

- 35

- B

- 81

- 75

- A

- C

---

## Slide 77: A.Split(i, B, x, C)

- i = 80

- Z

- Y

- L

- i = 80

- 30

- R

- t

- 30

- L

- 81

- 40

- 5

- R

- t

- C

- 5

- 40

- L

- 2

- 80

- 35

- t

- 2

- 80

- 35

- 75

- 81

- 75

- x

- A

- B

- Program 5.22

---

## Slide 78: 5.8 Selection Trees

- When trying to merge k ordered sequences (assume in non-decreasing order) into a single sequence, the most intuitive way is probably to perform k – 1 comparison each time to select the smallest one among the first number of each of the k ordered sequences. This goes on until all numbers in every sequences are visited.
- There should be a better way to do this.
- selection tree is a complete binary tree which is implement by sequential array
  - node i  parent node is node i/2, sibling node is node(i+1) or node(i-1)

---

## Slide 79: Winner Tree

- A winner tree is a complete binary tree in which each node represents the smaller of its two children. Thus the root represents the smallest node in the tree.
- Each leaf node represents the first record in the corresponding run.
- Each non-leaf node in the tree represents the winner of its right and left subtrees.
- tree node data structure
  - data {run,index}

---

## Slide 80: Winner Tree For k = 8

- 1

- 6

- 2

- 3

- 6

- 8

- 4

- 5

- 7

- 6

- 9

- 6

- 8

- 17

- 8

- 9

- 10

- 11

- 12

- 13

- 14

- 15

- 10

- 9

- 20

- 6

- 8

- 9

- 90

- 17

- 10

- 9

- 20

- 6

- 8

- 9

- 90

- 17

- 15

- 20

- 20

- 15

- 15

- 11

- 95

- 18

- 16

- 38

- 30

- 25

- 50

- 16

- 99

- 20

- 28

- run2

- run1

- run4

- run8

- run6

- run5

- run3

- run7

---

## Slide 81: Winner Tree For k = 8

- 1

- 8

- 2

- 3

- 9

- 8

- 4

- 5

- 7

- 6

- 9

- 15

- 8

- 17

- 8

- 9

- 10

- 11

- 12

- 13

- 14

- 15

- 10

- 9

- 20

- 15

- 8

- 9

- 90

- 17

- 15

- 20

- 20

- 25

- 15

- 11

- 95

- 18

- 16

- 38

- 30

- 28

- 50

- 16

- 99

- 20

- run2

- run1

- run4

- run8

- run6

- run5

- run3

- run7

---

## Slide 82: Analysis of Winner Tree

- The number of levels in the tree is
  - The time to restructure the winner tree is O(log2k).
- Since the tree has to be restructured each time a number is output, the time to merge all n records is O(n log2k).
- The time required to setup the selection tree for the first time is O(k).
- Total time needed to merge the k runs is O(n log2k).

---

## Slide 83: Loser Tree

- A selection tree in which each nonleaf node retains a pointer to the loser is called a loser tree.
- Again, each leaf node represents the first record of each run.
- An additional node, node 0, has been added to represent the overall winner of the tournament.

---

## Slide 84: Loser Tree

- 0

- Overall winner

- 6

- 1

- 8

- 2

- 3

- 9

- 17

- 4

- 5

- 7

- 6

- 10

- 20

- 9

- 90

- 9

- 10

- 11

- 12

- 13

- 14

- 15

- 10

- 9

- 20

- 6

- 8

- 9

- 90

- 17

- 1

- 2

- 3

- 4

- 5

- 6

- 7

- 8

- run

---

## Slide 85: Loser Tree

- 0

- Overall winner

- 8

- 1

- 9

- 2

- 3

- 15

- 17

- 4

- 5

- 7

- 6

- 10

- 20

- 9

- 90

- 9

- 10

- 11

- 12

- 13

- 14

- 15

- 10

- 9

- 20

- 15

- 8

- 9

- 90

- 17

- 1

- 2

- 3

- 4

- 5

- 6

- 7

- 8

- run

---

## Slide 86: 5.9 Forests

- Definition: A forest is a set of n ≥ 0 disjoint trees.
- When we remove a root from a tree, we’ll get a forest. E.g., Removing the root of a binary tree will get a forest of two trees.

---

## Slide 87: Transforming A Forest Into A Binary Tree

- Definition: If T1, …, Tn is a forest of trees, then the binary tree corresponding to this forest, denoted by B(T1, …, Tn),
  - is empty if n = 0
  - B has root equal to root (T1); has left subtree equal to B(T11, T12,…, T1m), where T11, T12,…, T1m are the subtrees of root (T1); and has right subtree B(T2, …, Tn).

---

## Slide 88: Transforming A Forest Into A Binary Tree

- A

- E

- G

- B

- D

- F

- C

- H

- I

- A

- E

- G

- B

- D

- F

- C

- H

- I

---

## Slide 89: Transforming A Forest Into A Binary Tree

- A

- B

- E

- G

- C

- D

- F

- H

- I

---

## Slide 90: Transforming A Forest Into A Binary Tree

- A

- B

- E

- C

- F

- G

- D

- H

- I

---

## Slide 91: Transforming A Forest Into A Binary Tree

- A

- B

- E

- C

- G

- F

- D

- H

- I

---

## Slide 92: Forest traversal

- Preorder traversal
  - Same as forest-binary-tree preorder traversal
  - Definition
    - Is empty return
    - Visit root of the first tree
    - Preorder traversal to visit sub-trees of the first tree
    - Preorder traversal to visit others forest tree
- Inorder traversal
  - Same as forest-binary-tree inorder traversal
  - Definition
    - Is empty return
    - Inorder traversal to visit sub-trees of the first tree
    - Visit root of the first tree
    - Inorder traversal to visit others forest tree

---

## Slide 93: Forest traversal

- Postorder traversal
  - maybe Different from forest-binary-tree postorder traversal
  - Definition
    - Is empty return
    - Postorder traversal to visit sub-trees of the first tree
    - Postorder traversal to visit others forest tree
    - Visit root of the first tree

---

## Slide 94: B

- Preorder
  - BEFKLCGDHIMJ
- Inorder
  - EKFLBGCHMIJD
- Postorder
  - KLFEGMJIHDCB

- C

- E

- G

- D

- F

- L

- K

- H

- I

- J

- M

- B

- C

- D

- E

- F

- G

- H

- J

- I

- K

- L

- M

---

## Slide 95: 5.10 Set Representation

- Trees can be used to represent sets.
- Disjoint set union: If Si and Sj are two disjoint sets, then their union Si ∪Sj = {all elements x such that x is in Si or Sj}.
- Find(i). Find the set containing element i.

---

## Slide 96: Possible Tree Representation of Sets

- 0

- 2

- 4

- 6

- 7

- 8

- 3

- 5

- 1

- 9

- S3

- S2

- S1

---

## Slide 97: Possible Representations of Si ∪Sj

- 4

- 0

- 6

- 4

- 9

- 1

- 7

- 8

- 0

- 1

- 9

- 6

- 7

- 8

---

## Slide 98: Unions of Sets

- To obtain the union of two sets, just set the parent field of one of the roots to the other root.
- To figure out which set an element is belonged to, just follow its parent link to the root and then follow the pointer in the root to the set name.

---

## Slide 99: Data Representation for S1, S2, S3

- Set
- Name

- Pointer

- S1

- 0

- 2

- 4

- S2

- 6

- 7

- 8

- 3

- 5

- 1

- 9

- S3

---

## Slide 100: Array Representation of S1, S2, S3

- We could use an array for the set name. Or the set name can be an element at the root.
- Assume set elements are numbered 0 through n-1.

- i

- [7]

- [9]

- [2]

- [4]

- [6]

- [8]

- [1]

- [3]

- [5]

- [0]

- 0

- 4

- -1

- -1

- 0

- 0

- 4

- 2

- 2

- -1

- parent

---

## Slide 101: Union-Find Operations

- For a set of n elements each in a set of its own, then the result of the union function is a degenerate tree.
- The time complexity of the following union-find operation is O(n2).
  - union(0, 1), union(1, 2), …, union(n-2, n-1)
  - find(0), find (1), …, find(n-1)<=1+2+…+n
- The complexity can be improved by using weighting rule for union.

---

## Slide 102: Degenerate Tree

- n-1

- Union operation
- O(n) n-1

- union(0, 1), find(0)

- union(1, 2), find(0)

- n-2

- Find operation
- O(n2)

- union(n-2, n-1), find(0)

- 0

---

## Slide 103: Weighting Rule

- Definition [Weighting rule for union(i, j)]: If the number of nodes in the tree with root i is less than the number in the tree with root j, then make j the parent of i; otherwise make i the parent of j.

---

## Slide 104: Trees Obtained Using The Weighting Rule

- 0

- 1

- n-1

- 0

- 2

- n-1

- 0

- 3

- n-1

- 1

- 1

- 2

- 0

- 0

- 4

- n-1

- 1

- 2

- 3

- 1

- n-1

- 2

- 3

- Program 5.25 sets union by Weighting Rule

---

## Slide 105: Weighted Union

- Lemma 5.5: Assume that we start with a forest of trees, each having one node. Let T be a tree with m nodes created as a result of a sequence of unions each performed using function WeightedUnion. The height of T is no greater than .
- For the processing of an intermixed sequence of u – 1 unions and f find operations, the time complexity is O(u + f*log u).

---

## Slide 106: Trees Achieving Worst-Case Bound

- [-1]

- [-1]

- [-1]

- [-1]

- [-1]

- [-1]

- [-1]

- [-1]

- 0

- 1

- 2

- 3

- 4

- 5

- 6

- 7

- (a) Initial height trees

- [-2]

- [-2]

- [-2]

- [-2]

- 0

- 2

- 4

- 6

- 1

- 3

- 5

- 7

- (b) Height-2 trees following union (0, 1), (2, 3), (4, 5), and (6, 7)

---

## Slide 107: Trees Achieving Worst-Case Bound (Cont.)

- [-8]

- [-4]

- [-4]

- 0

- 4

- 0

- 6

- 5

- 2

- 2

- 1

- 1

- 4

- 6

- 5

- 7

- 3

- 3

- (c) Height-3 trees following union (0, 2), (4, 6)

- 7

- (d) Height-4 trees following union (0, 4)

---

## Slide 108: Collapsing Rule

- Definition [Collapsing rule]: If j is a node on the path from i to its root and parent[i]≠ root(i), then set parent[j] to root(i).
- The first run of find operation will collapse the tree. Therefore, all following find operation of the same element only goes up one link to find the root.

---

## Slide 109: Collapsing Find

- Program 5.26 Collapsing Rule

- [-8]

- [-8]

- 0

- 0

- 4

- 2

- 2

- 6

- 7

- 1

- 1

- 4

- 5

- 3

- 6

- 5

- 3

- After collapsing

- 7

- Before collapsing

---

## Slide 110: Analysis of Weighted Union and Collapsing Find

- The use of collapsing rule roughly double the time for an individual find. However, it reduces the worst-case time over a sequence of finds.
- Lemma 5.6 [Tarjan and Van Leeuwen]: Assume that we start with a forest of trees, each having one node. Let T(f, u) be the maximum time required to process any intermixed sequence of f finds and u unions. Assume that u ≥ n/2. Then
  - k1(n + fα(f + n, n)) ≤ T(f, u) ≤ k2(n + fα(f + n, n))
  - for some positive constants k1 and k2.
- 5.10.3

---

## Slide 111: 5.11 Distinct Binary Trees

- 1

- 1

- 1

- 2

- 2

- (1, 2)

- (2, 1)

---

## Slide 112: Distinct Binary Trees

- 1

- 1

- 1

- 1

- 1

- 2

- 3

- 2

- 2

- 2

- 2

- 3

- 3

- 3

- 3

- (1, 2, 3)

- (1, 3, 2)

- (2, 1, 3)

- (2, 3, 1)

- (3, 2, 1)

---

## Slide 113: Uniqueness of A Binary Tree

- In section 5.3 we introduced preorder, inorder, and postorder traversal of a binary tree. Now suppose we are given a sequence (e.g., inorder sequence BCAEDGHFI), does the sequence uniquely define a binary tree?

---

## Slide 114: Constructing A Binary Tree From Its Inorder & preorder Sequence

- inorder sequence BCAEDGHFI
- Preorder sequence ABCDEFGHI

- A

- A

- B, C

- B

- D, E, F, G, H, I

- D, E, F, G, H, I

- C

- Exercise 5,6 construct the binary tree using (inorder,preorder)
- and (inorder,postorder) sequence

---

## Slide 115: Constructing A Binary Tree From Its Inorder Sequence (Cont.)

- 1

- A

- 2

- 4

- B

- D

- 3

- 6

- 5

- C

- F

- E

- 9

- 7

- I

- G

- 8

- H

- Preorder: 1, 2, 3, 4, 5, 6, 7, 8, 9

- Inorder: 2, 3, 1, 5, 4, 7, 8, 6, 9

---

## Slide 116: Distinct Binary Trees (Cont.)

- The number of distinct binary trees is equal to the number of distinct inorder permutations obtainable from binary trees having the preorder permutation, 1, 2, …, n. same as push the preorder sequence into stack and pop from stack by all possible ways
- Computing the product of n matrices are related to the distinct binary tree problem.
- M1 * M2 * … * Mn
```c
n = 3    (M1 * M2) * M3 	 M1 * (M2 * M3 )
	n = 4    ((M1 * M2) * M3) * M4
```
- (M1 * (M2 * M3)) * M4
- M1 * ((M2 * M3) * M4 )
- (M1 * (M2 * (M3 * M4 )))
- ((M1 * M2) * (M3 * M4 ))
- Let bn be the number of different ways to compute the product of n matrices. b2 = 1, b3 = 2, and b4 = 5.

---

## Slide 117: Distinct Binary Trees (Cont.)

- The number of distinct binary trees of n nodes is

- bn

- bi

- bn-i-1

---

## Slide 118: Distinct Binary Trees (Cont.)

- Assume we let which is the generating function for the number of binary trees.
- By the recurrence relation we get

---
