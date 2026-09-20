# 08_SortM2

> 📌 **課程主題筆記**: 本文件由 `08_SortM2.ppt` 完整擷取，包含所有投影片內容、階層清單、程式碼區塊、表格、圖表標籤與註記，共 99 頁投影片。

## Slide 1

- 資料結構
- Data Structure

- Chapter 7: Sort
- 國立聯合大學
- 資訊管理學系
- 温敏淦

---

## Slide 2: Motivation of Sorting

- The term list here is a collection of records.
- Each record has one or more fields.
- Each record has a key to distinguish one record with another.
- For example, the phone directory is a list. Name, phone number, and even address can be the key, depending on the application or need.

---

## Slide 3: Sequential Search

- One way to search for a record with the specified key is to examine the list of records in left-to-right order.

```c
template <class E, class K>
int SeqSearch (E *a, const int n, const K& k)
{// Search a[1:n] from left to right . Return least i such that
  // the key of a[i] equals k. If there is no such i, return 0.
	int i;
	for (i = 1 ; i <= n && a[i] != k ; i++ );
	if (i > n) return 0;
	return i;
}
```

- The average number of comparisons

---

## Slide 4: Sequential Search

- The number of comparisons for a record key i is n – i +1.
- The average number of comparisons for a successful search is
- For the phone directory lookup, there should be a better way than this.

---

## Slide 5: IRS Tax Verification Example

- Now, let’s look at another searching problem: Tax verification.
- The IRS gets salary reports from employers. IRS also gets tax filing reports from employees about their salary. Need to verify the two numbers match for each individual employee.

---

## Slide 6: Verifying Two Lists With Sequential Search(program 7.2)

```c
void Verify1(Element* F1, Element* F2, const int n, const int m)
// Compare two unordered lists F1 and F2 of size n and m, respectively
{
	Boolean *marked = new Boolean[m];
	for (int i = 1; i <= m; i++)  marked[i] = FALSE;
	for (i = 1; i<= n; i++)
	{
	   int j = SeqSearch(F2, m, F1[i].getKey());
	   if (j == 0) cout << F1[i].getKey() <<“not in F2 “ << endl;
	   else
	   {
		if (F1[i].other != F2[j].other)
		   cout << “Discrepancy in “<<F[i].getKey()<<“:”<<F1[i].other
			<< “and “ << F2[j].other << endl;
		marked[j] = TRUE;  // marked the record in F2[j] as being seen
	   }
	}
	for (i = 1; i <= m; i++)
	   if (!marked[i]) cout << F2[i].getKey() <<“not in F1. “ << endl;
	delete [ ] marked;
}
```

- O(mn)

---

## Slide 7: Search

- A binary search only takes O(log n) time to search a sequential list with n records.
- In fact, if we look up the name start with W in the phone directory, we start search toward the end of the directory rather than the middle. This search method is based on interpolation scheme.
- An interpolation scheme relies on a ordered list.

---

## Slide 8: Binary Search

- Can be used only when the list is ordered.

```c
int BinarySearch (int *a, const int x, const int n)
{ // Search the sorted array a[0], …, a[n-1] for x
	int left = 0, right = n-1 ;
	while (left <= right)
	{ // there are more elements
		int middle = (left + right)/2;
		if (x < a[middle]) right=middle-1;
		else if (x > a[middle]) left = middle+1;
		else return middle;
	} // end of while
	return -1; // not found
}
```

---

## Slide 9: Sorting Application

- So far we have seen two uses of sorting
  - An aid in searching
  - A means for matching entries in lists
- Sorting is used in other applications.
  - Estimated 25% of all computing time is spent on sorting
- No one sorting method is the best for all initial orderings of the list being sorted.

---

## Slide 10: Sorting

- Two ways to store a collection of records
  - Sequential
  - Non-sequential
- Assume a sequential list f. To retrieve a record with key f[i].key from such a list, we can do search in the following order:
  - f[n].key, f[n-1].key, …, f[1].key => sequential search

---

## Slide 11: Fast Verification of Two Lists

```c
void Verify2(Element* F1, Element* F2, const int n, const int m)
// Same task as Verfy1. But sort F1 and F2 so that the keys are in
// increasing order. Assume the keys in each list are identical
{
	sort(F1, n);
	sort(F2, m);
	int i = 1; int j = 1;
	while ((i <= n) && (j <= m))
	   switch(compare(F1[i].getKey(), F2[j].getKey()))
	   {
		case ‘<‘: cout<<F1[i].getKey() <<“not in F2”<< endl;
			  i++;  break;
		case ‘=‘: if (F1[i].other != F2[j].other)
			    cout << “Discrepancy in “ << F1[i].getKey()<<“:”
			    <<F1[i].other<<“ and “<<F2[j].other << endl;
			  i++; j++; break;
		case ‘>’: cout <<F2[j].getKey()<<“ not in F1”<<endl;
			  j++;
	   }
	if (i <= n)PrintRest(F1, i, n, 1); //print records I through n of F1
	else if (j <= m) PrintRest(F2, j, m, 2);  // print records j through m of F2
}
```

- O(max{n log n, m log m})

---

## Slide 12: Insertion Sort (I)

```c
template <class T>
void Insert(cones T& e, T *a, int i)
{ // Insert e into the ordered sequence a [1:i] such that the
 // resulting sequence a[1: i + 1] is also ordered。
 // The array a must have space allocated for at least i + 2 elements.
	a[0] = e;
	while (e < a[i])
	{
		a[i + 1] = a [i];
		i --;
	}
	a[i + 1] = e;
}
```

- Insertion into a sorted list

---

## Slide 13: Insertion Sort (II)

> 🖼️ *(包含圖形 / 示意圖)*

```c
template <class T>
void InsertionSort(T *a, const int n)
{ // Sort a[1: n] into nondecreasing order.
	for (int j = 2; j <= n ; j++){
		T temp = a[j];
		Insert(temp, a, j – 1);
	}
}
```

---

## Slide 14: Analysis of Insertion Sort

- The complexity (worse case and average case):
- Example 7.1

| j | [1] | [2] | [3] | [4] | [5] |
| --- | --- | --- | --- | --- | --- |
| - | 5 | 4 | 3 | 2 | 1 |
| 2 | 4 | 5 | 3 | 2 | 1 |
| 3 | 3 | 4 | 5 | 2 | 1 |
| 4 | 2 | 3 | 4 | 5 | 1 |
| 5 | 1 | 2 | 3 | 4 | 5 |

---

## Slide 15: Example 7.2

- n=5, only record 5 is LOO (left out of order)

| j | [1] | [2] | [3] | [4] | [5] |
| --- | --- | --- | --- | --- | --- |
| - | 2 | 3 | 4 | 5 | 1 |
| 2 | 2 | 3 | 4 | 5 | 1 |
| 3 | 2 | 3 | 4 | 5 | 1 |
| 4 | 2 | 3 | 4 | 5 | 1 |
| 5 | 1 | 2 | 3 | 4 | 5 |

---

## Slide 16: Insertion Sort Ananlysis

- If there are k LOO records in a list, the computing time for sorting the list via insertion sort is O((k+1)n) = O(kn).
- Therefore, if k << n, then insertion sort might be a good sorting choice.

---

## Slide 17: Insertion Sort Variations

- Binary insertion sort: the number of comparisons in an insertion sort can be reduced if we replace the sequential search by binary search. The number of records moves remains the same.
- List insertion sort: The elements of the list are represented as a linked list rather than an array. The number of record moves becomes zero because only the link fields require adjustment. However, we must retain the sequential search.

---

## Slide 18: Formal Description of Sorting

- Given a list of records (R1, R2, …, Rn). Each record has a key Ki. The sorting problem is then that of finding permutation, σ, such that
- Kσ(i) ≤ K σ(i+1) , 1 ≤ i ≤ n – 1. The desired ordering is (Rσ(1), Rσ(2), Rσ(n)).

---

## Slide 19: Formal Description of Sorting (Cont.)

- If a list has several key values that are identical, the permutation, σs, is not unique. Let σs be the permutation of the following properties:
  - (1) Kσ(i) ≤ K σ(i+1) , 1 ≤ i ≤ n – 1
  - (2) If i < j and Ki == Kj in the input list, then Ri precedes Rj in the sorted list.
- The above sorting method that generates σs is stable.

---

## Slide 20: Categories of Sorting Method

- Internal Method: Methods to be used when the list to be sorted is small enough so that the entire sort list can be carried out in the main memory.
  - Insertion sort, quick sort, merge sort, heap sort and radix sort.
- External Method: Methods to be used on larger lists.

---

## Slide 21: 7.3 Quick Sort

- Quick sort is developed by C. A. R. Hoare. The quick sort scheme has the best average behavior among the sorting methods.
- Quick sort differs from insertion sort in that the pivot key Ki is placed at the correct spot with respect to the whole list. Kj ≤ Ks(i) for j < s(i) and Kj ≥ s(i) for j > s(i).
- Therefore, the sublist to the left of S(i) and to the right of s(i) can be sorted independently.

---

## Slide 22: Quick Sort

- The Quick Sort scheme developed by C.A. R. Hoare has the best average behavior among the sorting methods.
- Pivot:

- ≦ pivot

- >pivot

- pivot

- Quick Sort

- Quick Sort

- 22

---

## Slide 23: Quick Sort

```c
template <class T>
void QuickSort(T *a, const int left, const int right)
{ // Sort a[left:right] into nondecreasing order.
 // a[left] is arbitrarily chosen as the pivot. Variables i and j
 // are used to partition the subarray so that at any time a[m] ≤ pivot, m < i,
 // and a[m] ≥ pivot, m > j. It is assumed that a[left] ≤ a[right + 1].
	if (left < right) {
		int i = left,
			j = right + 1,
			pivot = a[left];
		do {
			do i++; while (a[i] < pivot);
			do j--; while (a[j] > pivot);
			if (i < j) swap (a[i], a[j]);
		} while (i < j);
		swap (a[left], a[j]);
		QuickSort(a, left, j - 1);
		QuickSort(a, j + 1, right);
	}
}
```

- 23

---

## Slide 24: Quick Sort Example

- Example 7.3: The input list has 10 records with keys (26, 5, 37, 1, 61, 11, 59, 15, 48, 19).

| R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | left | right |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [26 | 5 | 37 | 1 | 61 | 11 | 59 | 15 | 48 | 19] | 1 | 10 |
| [11 | 5 | 19 | 1 | 15] | 26 | [59 | 61 | 48 | 37] | 1 | 5 |
| [1 | 5] | 11 | [19 | 15] | 26 | [59 | 61 | 48 | 37] | 1 | 2 |
| 1 | 5 | 11 | [19 | 15] | 26 | [59 | 61 | 48 | 37] | 4 | 5 |
| 1 | 5 | 11 | 15 | 19 | 26 | [59 | 61 | 48 | 37] | 7 | 10 |
| 1 | 5 | 11 | 15 | 19 | 26 | [48 | 37] | 59 | [61] | 7 | 8 |
| 1 | 5 | 11 | 15 | 19 | 26 | 37 | 48 | 59 | [61] | 10 | 10 |
| 1 | 5 | 11 | 15 | 19 | 26 | 37 | 48 | 59 | 61 |  |  |

---

## Slide 25: Quick Sort (Cont.)

- In QuickSort(), list[n+1] has been set to have a key at least as large as the remaining keys.
- Analysis of QuickSort
  - The worst case O(n2)
  - If each time a record is correctly positioned, the sublist of its left is of the same size of the sublist of its right. Assume T(n) is the time taken to sort a list of size n:
  - T(n) ≤ cn + 2T(n/2), for some constant c
  - ≤ ≤ cn + 2(cn/2 +2T(n/4))
  - ≤ 2cn + 4T(n/4)
  - :
  - :
  - ≤ cn log2n + T(1) = O(n logn)

---

## Slide 26: Lemma 7.1

- Lemma 7.1: Let Tavg(n) be the expected time for function QuickSort to sort a list with n records. Then there exists a constant k such that Tavg(n) ≤ kn logen for n ≥ 2.

---

## Slide 27: Analysis of Quick Sort

- Unlike insertion sort (which only needs additional space for a record), quick sort needs stack space to implement the recursion.
- If the lists split evenly, the maximum recursion depth would be log n and the stack space is of O(log n).
- The worst case is when the lists split into a left sublist of size n – 1 and a right sublist of size 0 at each level of recursion. In this case, the recursion depth is n, the stack space of O(n).
- The worst case stack space can be reduced by a factor of 4 by realizing that right sublists of size less than 2 need not be stacked. Asymptotic reduction in stack space can be achieved by sorting smaller sublists first. In this case the additional stack space is at most O(log n).

---

## Slide 28: Quick Sort Variations

- Quick sort using a median of three: Pick the median of the first, middle, and last keys in the current sublist as the pivot. Thus, pivot = median{Kl, K(l+r)/2, Kr}.

---

## Slide 29: 7.4 Decision Tree

- So far both insertion sorting and quick sorting have worst-case complexity of O(n2).
- If we restrict the question to sorting algorithms in which the only operations permitted on keys are comparisons and interchanges, then O(n logn) is the best possible time.
- This is done by using a tree that describes the sorting process. Each vertex of the tree represents a key comparison, and the branches indicate the result. Such a tree is called decision tree.

---

## Slide 30: Decision Tree for Insertion Sort

- K1 ≤ K2

- No

- Yes

- K2 ≤ K3

- K1 ≤ K3

- No

- No

- Yes

- Yes

- stop

- K2 ≤ K3

- stop

- K1 ≤ K3

- No

- Yes

- No

- IV

- Yes

- I

- stop

- stop

- stop

- stop

- V

- VI

- II

- III

---

## Slide 31: Decision Tree (Cont.)

- Theorem 7.1: Any decision tree that sorts n distinct elements has a height of at least log2(n!) + 1
- Corollary: Any algorithm that sorts only by comparisons must have a worst-case computing time of Ω(n log n)

---

## Slide 32: 7.5 Merge Sort

- Merge two ordered lists:
  - Use O(n) additional space.
  - The two lists to be merged are initList[1:m] and initList[m+1:n]. The result list is initList[1:n].

- sorted

- sorted

- merge

- sorted

- 32

---

## Slide 33: Merging Two Sorted Lists

```c
template <class T>
void Merge(T *initList, T *mergedList, const int l, const int m, const int n){
             for (int i1 = l, iResult = l, i2 = m + 1;
		i1 <= m && i2 <= n;
		iResult++)
		if (initList[i1] <= initList [i2])
		{
			mergedList [iResult] = initList [i1];
			i1++;
		}
		else
		{
			mergedList [iResult] = initList [i2];
			i2++;
		}
	// copy remaining records, if any, of first list
	copy (initList + i1, initList + m + 1, mergedList + iResult);
	// copy remaining records, if any, of second list
	copy (initList + i2, initList + n + 1, mergedList + iResult);
}
```

- 33

---

## Slide 34: Analysis of Simple Merge

- If an array is used, additional space for n – l +1 records is needed.
- If linked list is used instead, then additional space is not needed.

---

## Slide 35: 7.5.2 Iterative Merge Sort

- Treat the input as n sorted lists, each of length 1.
- Lists are merged by pairs to obtain n/2 lists, each of size 2 (if n is odd, the one list is of length 1).
- The n/2 lists are then merged by pairs, and so on until we are left with only one list.

---

## Slide 36: Merge Tree

- 26

- 5

- 77

- 1

- 61

- 11

- 59

- 15

- 48

- 19

- 5 26

- 1 77

- 11 61

- 15 59

- 19 48

- 1 5 26 77

- 11 15 59 61

- 19 48

- 1 5 11 15 26 59 61 77

- 19 48

- 1 5 11 15 19 26 48 59 61 77

---

## Slide 37: Merge Sort

```c
template <class T>
void MergeSort(T *a,const int n)
{// Sort a[1:n] into nondecreasing order.
	T *tempList = new T[n+1];
	// l is the length of the sublist currently being merged
	for (int l =1; l < n; l*= 2)
	{
	     MergePass(a, tempList, n, l);
	     l*=2;
	    MergePass(tempList, a, n, l); // interchange the role of a and tempList
}
	delete [] tempList;
}
```

- O(nlogn)

- 37

---

## Slide 38: Merge Pass

```c
template <class T>
void MergePass(T *initList, T *resultList, const int n, const int s)
{// Adjacent pairs of sublists of size s are merged from
 //initList to resultList. n is the number of records in initList.
	for (int i = 1; // i is first position in first of the sublists being merged
	i <= n-2*s+1; // enough elements for two sublists of length s?
	i+ = 2*s)
	  Merge(initList, resultList, i, i + s -1, i + 2 * s -1);
// merge remaining list of size < 2 * s
if ((i + s -1) < n ) Merge(initList, resultList, i, i + s -1, n);
else copy(initList + i, initList + n + 1, resultList + i);
}
```

- 38

---

## Slide 39: Analysis of MergeSort

- Total of passes are made over the data. Each pass of merge sort takes O(n) time.
- The total of computing time is O(n log n)
- Stable sort

---

## Slide 40: Recursive Merge Sort

- Recursive merge sort divides the list to be sorted into two roughly equal parts:
  - the left sublist [left : (left+right)/2]
  - the right sublist [(left+right)/2 +1 : right]
- These sublists are sorted recursively, and the sorted sublists are merged.
- To avoid copying, the use of a linked list (integer instead of real link) for sublist is desirable.

---

## Slide 41: Sublist Partitioning For Recursive Merge Sort

- 26

- 5

- 77

- 1

- 61

- 11

- 59

- 15

- 48

- 19

- 5 26

- 11 59

- 19 48

- 5 26 77

- 11 15 59

- 19 48

- 1 61

- 1 5 26 61 77

- 11 15 19 48 59

- 1 5 11 15 19 26 48 59 61 77

---

## Slide 42: Recursive Merge Sort (program 7.10)

```c
template <class T>
int rMergeSort(T* a, int* link, const int left, const int right)
{// a[left:right] is to be sorted. link[i] is initially 0 for all i.
 // rMergesort returns the index of the first element in the sorted chain.
	if (left >= right) return left;
	int mid = (left + right) /2;
	return ListMerge(a, link,
  rMergeSort(a, link, left, mid),	         // sort left half
  rMergeSort(a, link, mid + 1, right));      // sort right half
}
```

- 42

---

## Slide 43: Merging Sorted Chains (program 7.11)

```c
tamplate <class T>
int ListMerge(T* a, int* link, const int start1, const int start2)
{// The sorted chains beginning at start1and start2, respectively, are merged
 // link[0] is used as a temporary header, Return start of merged chain.
	int iResult = 0; // last record of result chain
	for (int i1 = start1, i2 =start2; i1 && i2; )
		if (a[i1] <= a[i2]) {
		        link[iResult] = i1;
		        iResult = i1; i1 = link[i1];
}
else {
	link[iResult] = i2;
	iResult = i2; i2 =link[i2];
}
	// attach remaining records to result chian
	if (i1 = = 0) link[iResult] = i2;
	else link[iResult] = i1;
	return link[0];
}
```

- 43

---

## Slide 44

> 🖼️ *(包含圖形 / 示意圖)*

> 🖼️ *(包含圖形 / 示意圖)*

---

## Slide 45

> 🖼️ *(包含圖形 / 示意圖)*

> 🖼️ *(包含圖形 / 示意圖)*

---

## Slide 46: Natural Merge Sort

- Natural merge sort takes advantage of the prevailing order within the list before performing merge sort.
- It runs an initial pass over the data to determine the sublists of records that are in order.
- Then it uses the sublists for the merge sort.

---

## Slide 47: Natural Merge Sort Example

- 26

- 5 77

- 1 61

- 11 59

- 15 48

- 19

- 5 26 77

- 1 11 59 61

- 15 19 48

- 1 5 11 26 59 61 77

- 15 19 48

- 1 5 11 15 19 26 48 59 61 77

---

## Slide 48: 7.6 Heap Sort

- Merge sort needs additional storage space proportional to the number of records in the file being sorted, even though its computing time is O(n log n)
- O(1) merge only needs O(1) space but the sorting algorithm is much slower.
- We will see that heap sort only requires a fixed amount of additional storage and achieves worst-case and average computing time O(n log n).
- Heap sort uses the max-heap structure.

---

## Slide 49: Heap Sort (Cont.)

- For heap sort, first of all, the n records are inserted into an empty heap.
- Next, the records are extracted from the heap one at a time.
- With the use of a special function adjust(), we can create a heap of n records faster.

---

## Slide 50: Program 7.13 (Adjusting A Max Heap)

```c
void adjust (Element* tree, const int root, const int n)
// Adjust the binary tree with root root to satisfy the heap property. The left and right subtrees of root
// already satisfy the heap property. No node has index greater than n.
{
   Element e = tree[root];
   int k = e.getKey();
   for (int j = 2*root; j <= n; j *= 2)
   {
      if (j < n)
         if (tree[j].getKey() < tree[j+1].getKey()) j++;
      // compare max child with k. If k is max, then done.
      if (k >= tree[j].getKey()) break;
      tree[j/2] = tree[j];     // move jth record up the tree
    }
    tree[j/2] = e;
}
```

- trickle down

---

## Slide 51: Program 7.14 (Heap Sort)

```c
void HeapSort (Element* list, const int n)
// The list list = (list[1], …, list[n]) is sorted into nondecreasing order of the field key.
{
   for (int i = n/2; i >= 1; i--) // convert list into a heap
      adjust(list, i, n);
   for (i = n-1; i >= 1; i--) // sort list
   {
      Element t = list[i+1]; // interchange list1 and list i+1
      list[i+1] = list[1];
      list[1] = t;
      adjust(list, 1, i);
    }
}
```

- O(n log n)

---

## Slide 52: Converting An Array Into A Max Heap

- 26

- 77

- [1]

- [1]

- [2]

- 5

- 77

- 61

- 59

- [2]

- [3]

- [3]

- 1

- 61

- 11

- 59

- [4]

- 48

- 19

- 11

- 26

- [5]

- [4]

- [5]

- [6]

- [7]

- [7]

- [6]

- 15

- 48

- 19

- 15

- 1

- 5

- [8]

- [9]

- [10]

- [10]

- [8]

- [9]

- (b) Initial heap

- (a) Input array

---

## Slide 53: Heap Sort Example

- 59

- 61

- [1]

- [1]

- 48

- 26

- 48

- 59

- [2]

- [2]

- [3]

- [3]

- 15

- 19

- 11

- 1

- 15

- 19

- 11

- 26

- [4]

- [5]

- [5]

- [7]

- [7]

- [6]

- [6]

- 5

- 5

- 1

- [8]

- [8]

- [9]

- Heap size = 8, Sorted = [61, 77]

- Heap size = 9, Sorted = [77]

---

## Slide 54: Sorting Several Keys

- A list of records are said to be sorted with respect to the keys K1, K2, …, Kr iff for every pair of records i and j, i < j and (K1i, K2i, …, Kri) ≤ (K1j, K2j, …, Krj).
- The r-tuple (x1, x2, …, xr) is less than or equal to the r-tuple (y1, y2, …, yr) iff either xi = yi, 1 ≤ i ≤ j, and xj+1 < yj+1 for some j < r or xi = yi , 1 ≤ i ≤ r.
- Two popular ways to sort on multiple keys
  - sort on the most significant key into multiple piles. For each pile, sort on the second significant key, and so on. Then piles are combined. This method is called sort on most-significant-digit-first (MSD).
  - The other way is to sort on the least significant digit first (LSD).
- Example, sorting a deck of cards: suite and face value.
  - Spade > Heart > Diamond > Club

---

## Slide 55: Sorting Several Keys (Cont.)

- LSD and MSD only defines the order in which the keys are to be sorted. But they do not specify how each key is sorted.
- Bin sort can be used for sorting on each key. The complexity of bin sort is O(n).
- LSD and MSD can be used even when there is only one key.
  - E.g., if the keys are numeric, then each decimal digit may be regarded as a subkey. => Radix sort.

---

## Slide 56: Radix Sort

- In a radix sort, we decompose the sort key using some radix r.
  - The number of bins needed is r.
- Assume the records R1, R2, …, Rn to be sorted based on a radix of r. Each key has d digits in the range of 0 to r-1.
- Assume each record has a link field. Then the records in the same bin are linked together into a chain:
  - f[i], 0 ≤ i ≤ r (the pointer to the first record in bin i)
  - e[i], (the pointer to the end record in bin i)
  - The chain will operate as a queue.
  - Each record is assumed to have an array key[d], 0 ≤ key[i] ≤ r, 0 ≤ i ≤ d.

---

## Slide 57: Program 7.15 (LSD Radix Sort)

```c
template <class T>int RadixSort (T *a,int *link, const int d, const int r, const int n)
{
   int e[r], f[r];   // queue pointers
   for (int i = 1; i <= n; i++)link[i] = i + 1; // link into a chain starting at current
   link[n] = 0; int first= 1;
   for (i = d – 1; i >= 0; i--)  // sort on key key[i]
   {  fill(f,f+r,0);  //for (int j = 0; j < radix; j++) f[j] = 0; // initialize bins to empty queues
      for (current=first; current; current = link[current]) {  // put records into queues
         int k = digit(a[current],I,r);
         if (f[k] == 0) f[k] = current;
         else link[e[k]]=current;
         e[k] = current;
      }
      for (j = 0; !f[j]; j++); // find the first non-empty queue
      first = f[j]; int last = e[j];
      for (int k = j+1; k < r; k++){  // concatenate remaining queues
         if (f[k]){
            link[last]= f[k];
            last = e[k];
         }
      }
      link[last]= 0;
   }
return first;
}
```

- d passes

- O(n)

- O(r)

- O(d(n+r))

---

## Slide 58: Radix Sort Example

- list[1]

- list[10]

- list[9]

- list[8]

- list[7]

- list[6]

- list[5]

- list[4]

- list[3]

- list[2]

- 179

- 208

- 306

- 93

- 859

- 984

- 55

- 9

- 271

- 33

- e[0]

- e[1]

- e[2]

- e[3]

- e[4]

- e[5]

- e[6]

- e[7]

- e[8]

- e[9]

- 9

- 33

- 859

- 271

- 93

- 984

- 55

- 306

- 208

- 179

> 📊 **圖表元素 / 標籤:** f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8], f[9]

- list[1]

- list[10]

- list[9]

- list[8]

- list[7]

- list[6]

- list[5]

- list[4]

- list[3]

- list[2]

- 271

- 93

- 33

- 984

- 55

- 306

- 208

- 179

- 859

- 9

---

## Slide 59: Radix Sort Example (Cont.)

- list[1]

- list[10]

- list[9]

- list[8]

- list[7]

- list[6]

- list[5]

- list[4]

- list[3]

- list[2]

- 271

- 93

- 33

- 984

- 55

- 306

- 208

- 179

- 859

- 9

- e[0]

- e[1]

- e[2]

- e[3]

- e[4]

- e[5]

- e[6]

- e[7]

- e[8]

- e[9]

- 9

- 208

- 859

- 179

- 306

- 33

- 55

- 271

- 984

- 93

> 📊 **圖表元素 / 標籤:** f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8], f[9]

- list[1]

- list[10]

- list[9]

- list[8]

- list[7]

- list[6]

- list[5]

- list[4]

- list[3]

- list[2]

- 306

- 208

- 9

- 33

- 55

- 859

- 271

- 179

- 984

- 93

---

## Slide 60: Radix Sort Example (Cont.)

- list[1]

- list[10]

- list[9]

- list[8]

- list[7]

- list[6]

- list[5]

- list[4]

- list[3]

- list[2]

- 306

- 208

- 9

- 33

- 55

- 859

- 271

- 179

- 984

- 93

- e[0]

- e[1]

- e[2]

- e[3]

- e[4]

- e[5]

- e[6]

- e[7]

- e[8]

- e[9]

- 93

- 55

- 33

- 271

- 9

- 179

- 208

- 859

- 984

- 306

> 📊 **圖表元素 / 標籤:** f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8], f[9]

- list[1]

- list[10]

- list[9]

- list[8]

- list[7]

- list[6]

- list[5]

- list[4]

- list[3]

- list[2]

- 9

- 33

- 55

- 93

- 179

- 208

- 271

- 306

- 859

- 948

---

## Slide 61

---

## Slide 62: 7.8 List And Table Sorts

- Apart from radix sort and recursive merge sort, all the sorting methods we have looked at so far require excessive data movement.
- When the amount of data to be sorted is large, data movement tends to slow down the process.
- It is desirable to modify sorting algorithms to minimize the data movement.
- Methods such as insertion sort or merge sort can be modified to work with a linked list rather than a sequential list. Instead of physical movement, an additional link field is used to reflect the change in the position of the record in the list.

---

## Slide 63: Program 7.16 (Rearranging Records Using A Doubly Linked List

```c
template <class T>void list (T *a,int *linka, const int n, int first)
{
   int *linkb=new int[n];
   int prev = 0;
   for (int current = first; current; current = linka[current])      // convert chain into a doubly linked list
   {
      linkb[current] = prev;
      prev = current;
   }
   for (int i = 1; i < n; i++) // move listfirst to position i while maintaining the list
   {
      if (first != i) {
        if (linka[i]) linkb[linka[i]]= first;
        linka[linkb[i]] = first;
        swap(a[first],a[i]); swap(linka[first],linkb[i]); swap(linkb[first],linkb[i]);
      }
      first = linka[i];
    }
}
```

- O(n)

- Assume each record is m words

- O(nm)

---

## Slide 64: Example 7.9

| i | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key | 26 | 5 | 77 | 1 | 61 | 11 | 59 | 15 | 48 | 19 |
| linka | 9 | 6 | 0 | 2 | 3 | 8 | 5 | 10 | 7 | 1 |

| i | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key | 26 | 5 | 77 | 1 | 61 | 11 | 59 | 15 | 48 | 19 |
| linka | 9 | 6 | 0 | 2 | 3 | 8 | 5 | 10 | 7 | 1 |
| linkb | 10 | 4 | 5 | 0 | 7 | 2 | 9 | 6 | 1 | 8 |

- Configuration after first iteration of the for loop of list1, first = 4

---

## Slide 65: Example 7.9 (Cont.)

| i | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key | 1 | 5 | 77 | 26 | 61 | 11 | 59 | 15 | 48 | 19 |
| linka | 2 | 6 | 0 | 9 | 3 | 8 | 5 | 10 | 7 | 4 |
| linkb | 0 | 4 | 5 | 10 | 7 | 2 | 9 | 6 | 4 | 8 |

- Configuration after first iteration of the for loop of list1, first = 2

| i | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key | 1 | 5 | 77 | 26 | 61 | 11 | 59 | 15 | 48 | 19 |
| linka | 2 | 6 | 0 | 9 | 3 | 8 | 5 | 10 | 7 | 4 |
| linkb | 0 | 4 | 5 | 10 | 7 | 2 | 9 | 6 | 4 | 8 |

- Configuration after second iteration of the for loop of list1, first = 6

---

## Slide 66: Example 7.9 (Cont.)

| i | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key | 1 | 5 | 11 | 26 | 61 | 77 | 59 | 15 | 48 | 19 |
| link | 2 | 6 | 8 | 9 | 6 | 0 | 5 | 10 | 7 | 4 |
| linkb | 0 | 4 | 2 | 10 | 7 | 5 | 9 | 6 | 4 | 8 |

- Configuration after third iteration of the for loop of list1, first = 8

| i | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key | 1 | 5 | 11 | 15 | 61 | 77 | 59 | 26 | 48 | 19 |
| link | 2 | 6 | 8 | 10 | 6 | 0 | 5 | 9 | 7 | 8 |
| linkb | 0 | 4 | 2 | 6 | 7 | 5 | 9 | 10 | 8 | 8 |

- Configuration after fourth iteration of the for loop of list1, first = 10

---

## Slide 67: Example 7.9 (Cont.)

| i | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key | 1 | 5 | 11 | 15 | 19 | 77 | 59 | 26 | 48 | 61 |
| linka | 2 | 6 | 8 | 10 | 8 | 0 | 10 | 9 | 7 | 6 |
| linkb | 0 | 4 | 2 | 6 | 8 | 10 | 9 | 10 | 8 | 7 |

- Configuration after third iteration of the for loop of list1, first = 8

| i | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key | 1 | 5 | 11 | 15 | 19 | 26 | 59 | 77 | 48 | 61 |
| linka | 2 | 6 | 8 | 10 | 8 | 9 | 10 | 0 | 7 | 8 |
| linkb | 0 | 4 | 2 | 6 | 8 | 10 | 9 | 10 | 8 | 7 |

- Configuration after fourth iteration of the for loop of list1, first = 9

---

## Slide 68: Example 7.9 (Cont.)

| i | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key | 1 | 5 | 11 | 15 | 19 | 26 | 48 | 77 | 59 | 61 |
| linka | 2 | 6 | 8 | 10 | 8 | 9 | 9 | 8 | 10 | 8 |
| linkb | 0 | 4 | 2 | 6 | 8 | 10 | 8 | 8 | 9 | 9 |

- Configuration after third iteration of the for loop of list1, first = 9

| i | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key | 1 | 5 | 11 | 15 | 19 | 26 | 48 | 59 | 77 | 61 |
| linka | 2 | 6 | 8 | 10 | 8 | 9 | 9 | 10 | 9 | 8 |
| linkb | 0 | 4 | 2 | 6 | 8 | 10 | 8 | 9 | 9 | 9 |

- Configuration after fourth iteration of the for loop of list1, first = 10

---

## Slide 69: Example 7.9 (Cont.)

| i | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key | 1 | 5 | 11 | 15 | 19 | 26 | 48 | 59 | 61 | 77 |
| linka | 2 | 6 | 8 | 10 | 8 | 9 | 9 | 10 | 8 | 10 |
| linkb | 0 | 4 | 2 | 6 | 8 | 10 | 8 | 9 | 9 | 10 |

---

## Slide 70: Program 7.17(Rearranging Records Using Only One Link)

```c
template <class T> void list2(T *a, int *link,const int n, int first)
// Same function as list1 except that a second link field linkb is not required
{
   for (int i = 1; i < n; i++)
   {
      while (first < i ) first = link [first];
      int q = link[first];  // listq is next record in nondecreasing order
      if (first != i)
      // interchange listi and listfirst moving listfirst to its correct spot as listfirst has ith smallest key.
       // Also set link from old position of listi to new one
      {
         swap(a[i],a[first]);
         link[first] = link[i]; link[i] = first;
      }
      first = q;
   }
}
```

- O(n)

- O(nm)

---

## Slide 71: Example 7.10 (Rearranging Records Using Only One Link)

| i | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key | 26 | 5 | 77 | 1 | 61 | 11 | 59 | 15 | 48 | 19 |
| link | 9 | 6 | 0 | 2 | 3 | 8 | 5 | 10 | 7 | 1 |

| i | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key | 1 | 5 | 77 | 26 | 61 | 11 | 59 | 15 | 48 | 19 |
| link | 4 | 6 | 0 | 9 | 3 | 8 | 5 | 10 | 7 | 1 |

- Configuration after first iteration of the for loop of list1, first = 2

| i | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key | 1 | 5 | 77 | 26 | 61 | 11 | 59 | 15 | 48 | 19 |
| link | 4 | 6 | 0 | 9 | 3 | 8 | 5 | 10 | 7 | 1 |

- Configuration after second iteration of the for loop of list1, first = 6

---

## Slide 72: Example 7.10 (Rearranging Records Using Only One Link)

| i | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key | 1 | 5 | 11 | 26 | 61 | 77 | 59 | 15 | 48 | 19 |
| link | 4 | 6 | 6 | 9 | 3 | 0 | 5 | 10 | 7 | 1 |

- Configuration after third iteration of the for loop of list1, first = 8

| i | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key | 1 | 5 | 11 | 15 | 61 | 77 | 59 | 26 | 48 | 19 |
| link | 4 | 6 | 6 | 8 | 3 | 0 | 5 | 9 | 7 | 1 |

- Configuration after fourth iteration of the for loop of list1, first = 10

---

## Slide 73: Example 7.10 (Rearranging Records Using Only One Link)

| i | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key | 1 | 5 | 11 | 15 | 19 | 77 | 59 | 26 | 48 | 61 |
| link | 4 | 6 | 6 | 8 | 10 | 0 | 5 | 9 | 7 | 3 |

- Configuration after fifth iteration of the for loop of list1, first = 1

| i | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key | 1 | 5 | 11 | 15 | 19 | 26 | 59 | 77 | 48 | 61 |
| link | 4 | 6 | 6 | 8 | 1 | 8 | 5 | 0 | 7 | 3 |

- Configuration after sixth iteration of the for loop of list1, first = 9

---

## Slide 74: Table Sort

- The list-sort technique is not well suited for quick sort and heap sort.
- One can maintain an auxiliary table, t, with one entry per record. The entries serve as an indirect reference to the records.
- Initially, t[i] = i. When interchanges are required, only the table entries are exchanged.
- It may be necessary to physically rearrange the records according to the permutation specified by t sometimes.

---

## Slide 75: Table Sort (Cont.)

- The function to rearrange records corresponding to the permutation t[1], t[2], …, t[n] can be considered as an application of a theorem from mathematics:
  - Every permutation is made up of disjoint cycles. The cycle for any element i is made up of i, t[i], t2[i], …, tk[i], where tj[i]=t[tj-1[i]], t0[i]=i, tk[i]=i.

---

## Slide 76: Program 7.18 (Table Sort)

```c
void table(Element* list, const int n, int *t)
{
   for (int i = 1; i < n; i++) {
      if (t[i] != i) {
         Element p = list[i]; int j = i;
         do {
            int k = t[j]; list[j] = list[k]; t[j] = j;
            j = k;
         } while (t[j] != i)
         list[j] = p;
         t[j] = j;
      }
   }
}
```

---

## Slide 77: Table Sort Example

- 4

- 5

|  | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key | 35 | 14 | 12 | 42 | 26 | 50 | 31 | 18 |
| t | 3 | 2 | 8 | 5 | 7 | 1 | 4 | 6 |

- Initial configuration

- 1

- 2

- 3

| key | 12 | 14 | 18 | 42 | 26 | 35 | 31 | 50 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t | 1 | 2 | 3 | 5 | 7 | 6 | 4 | 8 |

- Configuration after rearrangement of first cycle

| key | 12 | 14 | 18 | 26 | 31 | 35 | 42 | 50 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |

- Configuration after rearrangement of second cycle

---

## Slide 78: Analysis of Table Sort

- To rearrange a nontrivial cycle including k distinct records one needs k+1 moves. Total of record moves
- Since the records on all nontrivial cycles must be different, then
- The total number of record moves is maximum
- when and there are cycles.
- Assume that one record move costs O(m) time, the total computing time is O(mn).

---

## Slide 79: Summary Of Internal Sorting

- No one method is best for all conditions.
  - Insertion sort is good when the list is already partially ordered. And it is best for small number of n.
  - Merge sort has the best worst-case behavior but needs more storage than heap sort.
  - Quick sort has the best average behavior, but its worst-case behavior is O(n2).
  - The behavior of radix sort depends on the size of the keys and the choice of r.

---

## Slide 80: External Sorting

- There are some lists that are too large to fit in the memory of a computer. So internal sorting is not possible.
- Some records are stored in the disk (tape, etc.). System retrieves a block of data from a disk at a time. A block contains multiple records.
- The most popular method for sorting on external storage devices is merge sort.
  - Segments of the input list are sorted.
  - Sorted segments (called runs) are written onto external storage.
  - Runs are merged until only run is left.

---

## Slide 81: Example 7.12

- Consider a computer which is capable of sorting 750 records is used to sort 4500 records.
- Six runs are generated with each run sorting 750 records.
- Allocate three 250-record blocks of internal memory for performing merging runs. Two for input run 2 runs and the last one is for output.
- Three factors contributing to the read/write time of disk:
  - seek time
  - latency time
  - transmission time

---

## Slide 82: Example 7.12 (Cont.)

- run3 (1501 – 2250)

- run6 (3751 – 4500)

- run5 (3001 – 3750)

- run4 (2251 – 3000)

- run2 (751 – 1500)

- run1 (1 – 750)

---

## Slide 83: Example 7.12 (Cont.)

- tIO = ts + tl +trw
- tIS = time to internal sort 750 records
- ntm = time to merge n records from input buffers to the output buffer
- ts = maximum seek time
- tl = maximum latency time
- trw = time to read or write on block of 250 records

---

## Slide 84: Example 7.12 (Cont.)

|  | Operation | Time |
| --- | --- | --- |
| (1) | Read 18 blocks of input, 18tIO, internally sort, 6tIS , write 18 blocks, 18tIO | 36tIO + 6tIS |
| (2) | Merge runs 1 to 6 in pairs | 36tIO + 4500tm |
| (3) | Merge two runs fo 1500 records each, 12 blocks | 24tIO + 3000tm |
| (4) | Merge one run of 3000 records with one run of 1500 records | 36tIO + 4500tm |
|  | Total time | 132tIO + 12000tm+ 6tIS |

---

## Slide 85: K-Way Merging

- To merge m runs via 2-way merging will need passes.
- If we use higher order merge, the number of passes over would be reduced.
- With k-way merge on m runs, we need
- passes over.
- But is it always true that the higher order of merging, the less computing time we will have?
  - Not necessary!
  - k-1 comparisons are needed to determine the next output.
  - If loser tree is used to reduce the number of comparisons, we can achieve complexity of O(n log2 m)
  - The data block size reduced as k increases. Reduced block size implies the increase of data passes over

---

## Slide 86: Buffer Handling for Parallel Operation

- To achieve better performance, multiple input buffers and two output buffers are used to avoid idle time.
- Evenly distributing input buffers among all runs may still have idle time problem. Buffers should be dynamically assigned to whoever needs to retrieve more data to avoid halting the computing process.
- We should take advantage of task overlapping and keep computing process busy and avoid idle time.

---

## Slide 87: Buffering Algorithm

- Step 1: Input the first block of each of the k runs, setting up k linked queues, each having one block of data.
- Step 2: Let LastKey[i] be the last key input from run i. Let NextRun be the run for which LastKey is minimum.
- Step 3: Use a function kwaymerge to merge records from the k input queues into the output buffer.
- Step 4: Wait for any ongoing disk I/O to complete.
- Step 5: If an input buffer has been read, add it to the queue for the appropriate run.
- Step 6: If LastKey[NextRun] != +infinity, then initiate reading the next block from run NextRun into a free input buffer.
- Step 7: Initiate the writing of output buffer.
- Step 8: If a record with key +infinity has not been merged into the output buffer, go back to Step 3. Otherwise, wait for the ongoing write to complete and then terminate.

---

## Slide 88: Optimal Merging of Runs

- 26

- 26

- 20

- 6

- 15

- 11

- 5

- 15

- 6

- 2

- 4

- 5

- 2

- 4

- weighted external path length = 2*2 + 4*2 + 5*2 + 15*2
- = 52

- weighted external path length = 2*3 + 4*3 + 5*2 + 15*1
- = 43

---

## Slide 89: Huffman Code

- Assume we want to obtain an optimal set of codes for messages M1, M2, …, Mn+1. Each code is a binary string that will be used for transmission of the corresponding message.
- At receiving end, a decode tree is used to decode the binary string and get back the message.
- A zero is interpreted as a left branch and a one as a right branch. These codes are called Huffman codes.
- The cost of decoding a code word is proportional to the number bits in the code. This number is equal to the distance of the corresponding external node from the root node.
- If qi is the relative frequency with which message Mi will be transmitted, then the expected decoding time is
- where di is the distance of the external node for message Mi from the root node.

---

## Slide 90: Huffman Codes (Cont.)

- The expected decoding time is minimized by choosing code words resulting in a decode tree with minimal weighted external path length.

- 1

- 0

- M4

- 1

- 0

- M3

- 0

- 1

- M1

- M2

---

## Slide 91: Huffman Function

```c
class BinaryTree {
public:
   BinaryTree(BinaryTree bt1, BinaryTree bt2) {
      root->LeftChild = bt1.root;
      root->RightChild = bt2.root;
      root->weight = bt1.root->weight + bt2.root->weight;
   }
private:
   BinaryTreeNode *root;
}
void huffman (List<BinaryTree> l)
// l is a list of single node binary trees as decribed above
{
   int n = l.Size();  // number of binary trees in l
   for (int i = 0; i < n-1; i++) {  // loop n-1 times
      BinaryTree first = l.DeleteMinWeight();
      BinaryTree second = l.DeleteMinWeight();
      BinaryTree *bt = new BinaryTree(first, second);
      l.Insert(bt);
   }
}
```

- O(nlog n)

---

## Slide 92: Huffman Tree Example

- 16

- 10

- 5

- 5

- 7

- 9

- 5

- 3

- 2

- (c)

- 3

- 2

- (a)

- 39

- (b)

- 23

- 16

- 23

- 10

- 13

- 10

- 13

- 7

- 9

- 5

- 5

- 5

- 5

- (e)

- (d)

- 3

- 2

- 3

- 2

---

## Slide 93

---

## Slide 94: O(1) Space Merge

- A second merge algorithm only requires O(1) additional space.
- Assume total of n records to be merged into a list, where n is a perfect square. And the numbers of records in the left sublist and the right sublist are multiple of

---

## Slide 95: O(1) Space Merge Steps

- Step 1: Identify the records with largest keys. This is done by following right to left along the two lists to be merged.
- Step 2: Exchange the records of the second list that were identified in Step 1 with those just to the left of those identified from the first list so that the records with largest keys are contiguous.
- Step 3: Swap the block of largest with the leftmost block (unless it is already the leftmost block). Sort the rightmost block.
- Step 4: Reorder the blocks, excluding the block of largest records, into nondecreasing order of the last key in the blocks.
- Step 5: Perform as many merge substeps as needed to merge the blocks, other than the block with the largest keys.
- Step 6: Sort the block with the largest keys.

---

## Slide 96: O(1) Space Merge Example (First 8 Lines)

- 0 2 4 6 8 a c e g i j k l m n t w z|1 3 5 7 9 b d f h o p q r s u v x y
- 0 2 4 6 8 a c e g i j k l m n t w z 1 3 5 7 9 b d f h o p q r s u v x y
- 0 2 4 6 8 a|c e g i j k|u v x y w z|1 3 5 7 9 b|d f h o p q|r s l m n t
- u v x y w z|c e g i j k|0 2 4 6 8 a|1 3 5 7 9 b|d f h o p q|l m n r s t
- u v x y w z 0 2 4 6 8 a|1 3 5 7 9 b|c e g I j k|d f h o p q|l m n r s t
- 0 v x y w z u 2 4 6 8 a|1 3 5 7 9 b|c e g I j k|d f h o p q|l m n r s t
- 0 1 x y w z u 2 4 6 8 a|v 3 5 7 9 b|c e g I j k|d f h o p q|l m n r s t
- 0 1 2 y w z u x 4 6 8 a|v 3 5 7 9 b|c e g I j k|d f h o p q|l m n r s t

---

## Slide 97: O(1) Space Merge Example (Last 8 Lines)

- 0 1 2 3 4 5 u x w 6 8 a|v y z 7 9 b|c e g i j k|d f h o p q|l m n r s t
- 0 1 2 3 4 5 6 7 8 u w a|v y z x 9 b|c e g i j k|d f h o p q|l m n r s t
- 0 1 2 3 4 5 6 7 8 9 a w|v y z x u b|c e g i j k|d f h o p q|l m n r s t
- 0 1 2 3 4 5 6 7 8 9 a w v y z x u b c e g i j k|d f h o p q|l m n r s t
- 0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k v z u|y x w o p q|l m n r s t
- 0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k v z u y x w o p q|l m n r s t
- 0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q y x w|v z u r s t
- 0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t|v z u y x w

---

## Slide 98: Analysis of O(1) Space Merge

- Step 1 and 2 and the swapping of Step 3 each take O( ) time and O(1) space.
- The sort of Step 3 can be done in O(n) time and O(1) space using an insertion sort.
- Step 4 can be done in O(n) time and O(1) space using a selection sort. (Selection sort sorts m records using O(m2) key comparisons and O(m) record moves. So it needs O(n) comparisons and the time to move blocks is O(n).
- If insertion sort is used in Step 4, then the time becomes O(n1.5) since insertion sort needs O(m2) record moves ( records per block * n record moves).

---

## Slide 99: Analysis of O(1) Space Merge (Cont.)

- The total number of merge substeps is at most . The total time for Step 5 is O(n).
- The sort of Step 6 can be done in O(n) by using either a selection sort or an insertion sort.
- Therefore, the total time is O(n) and the additional space used is O(1).

---
