# 09_HashingM

> 📌 **課程主題筆記**: 本文件由 `09_HashingM.ppt` 完整擷取，包含所有投影片內容、階層清單、程式碼區塊、表格、圖表標籤與註記，共 30 頁投影片。

## Slide 1

- 資料結構
- Data Structure

- Chapter 8: Hashing
- 國立聯合大學
- 資訊管理學系
- 温敏淦

---

## Slide 2: Outline

- Static Hashing
  - Hash Tables
  - Hashing Functions
    - Mid-square
    - Division
    - Folding
    - Digit Analysis
  - Overflow Handling
    - Linear Open Addressing, Quadratic probing, Rehashing
    - Chaining

---

## Slide 3: Dictionaries

- Many example of dictionaries are found in many applications, Ex. spelling checker
- We define the dictionary as a set of name-attribute pairs.
- Example: In a dictionary (symbol table) for a compiler
  - the name is an identifier
  - the attributes might include an initial value
  - a list of lines that use the identifier.

---

## Slide 4: Dictionaries

- Operations on dictionary :
  - Determine if a particular name is in the dictionary
  - Retrieve/modify the attributes of that name
  - Insert/delete a name and its attributes
- Implementations
  - Binary search tree: the worst case of time complexity is O(n)
  - Some balanced binary trees (chapter 10): O(log n).
- Hashing
  - A technique for get, insert, and delete operations that has very good expected performance O(1).

---

## Slide 5: Search Techniques

- Search tree methods
  - Identifier comparisons
- Hashing methods
  - Relies on a formula called the hash function.
- Types of hashing
  - Static hashing
  - Dynamic hashing

---

## Slide 6: Hash Tables (1/6)

- In static hashing, we store the identifiers in a fixed size table called a hash table
- Arithmetic function, h
  - To determine the address of an identifier, x, in the table
  - h(x) gives the hash, or home address, of x in the table, named 0~b-1
- Hash table, ht
  - Stored in sequential memory locations that are partitioned into b buckets, ht[0], …, ht[b-1].
  - Each bucket has s slots

---

## Slide 7: Hash Tables (2/6)

- hash table (ht)

- 0
- 1
- 2
- .
- .
- b-2
- b-1

- h(x): 0 … (b-1)

- b buckets

- 1 2 ………. s

- s slots

---

## Slide 8: Hash Tables (3/6)

- The key density of a hash table is the ratio n/T
  - n is the number of pairs in the table
  - T is the number of possible keys
- The loading density or loading factor of a hash table is a = n/(sb)
  - s is the number of slots
  - b is the number of buckets

---

## Slide 9: Hash Tables (4/6)

- Two identifiers, i1 and i2 are synonyms with respect to f if f(i1) = f(i2)
  - We enter distinct synonyms into the same bucket as long as the bucket has slots available
- An overflow occurs when we hash a new identifier into a full bucket
- A collision occurs when we hash two non-identical identifiers into the same bucket.
- When the bucket size is 1, collisions and overflows occur simultaneously.

---

## Slide 10: Hash Tables (5/6)

- Example 8.1: Hash table
  - b = 26 buckets and s = 2 slots. Distinct identifiers n = 10
  - The loading factor, , is 10/52 = 0.19.
  - Associate the letters, a-z, with the numbers, 0-25, respectively
  - Define a fairly simple hash function, h(x), as the first character of x.

> 📊 **圖表元素 / 標籤:** Synonyms

- binary

- global

---

## Slide 11: Hash Tables (6/6)

- The time required to enter, delete, or search for identifiers does not depend on the number of identifiers n in use; it is O(1).
- Hash function requirements:
  - Easy to compute and produces few collisions.
  - Unfortunately, since the ration b/T and s is usually small, we cannot avoid collisions. => Overflow handling mechanisms are needed

---

## Slide 12: Hashing Functions (1/7)

- A hash function, h, transforms an key, k, into a bucket address in the hash table.
- We want a hash function that is easy to compute and that minimizes the number of collisions.
- Hashing functions should be unbiased.
  - That is, if we randomly choose an key, k, from the key space, the probability that h(k) = i is 1/b for all buckets i.
  - We call a hash function that satisfies unbiased property a uniform hash function.
- Division, Mid-square, Folding, Digit Analysis

---

## Slide 13: Hashing Functions (2/7)

- Division h (k) = k % D :
  - Using the modulus (%) operator.
  - We divide the key k by some number D and use the remainder as the hash address for k.
    - This gives bucket addresses that range from 0 to D - 1, where D = the table size.
- The choice of D is critical.
  - If D is divisible by 2, then odd keys to odd buckets and even keys to even buckets. (biased!!)
  - small prime factors, 2,3,5,7,=>biased
  - Prime number is a good choice.
  - Choose D as odd number and increasing the number of buckets from b to 2b+1 when ht[] requires more space

---

## Slide 14: Hashing Functions (3/7)

- Mid-square hm(x)=middle(x2):
  - Frequently used in symbol table applications.
  - We compute hm by squaring the identifier and then using an appropriate number of bits from the middle of the square to obtain the bucket address.
  - The number of bits used to obtain the bucket address depends on the table size. If we use r bits, the range of the value is 0~2r-1.
  - Since the middle bits of the square usually depend upon all the characters in an identifier, there is high probability that different identifiers will produce different hash addresses.

---

## Slide 15: Example of Mid Square

- Example: Choose middle 3 digits
  - hm(122)=middle3(14884)=488

---

## Slide 16: Hashing Functions (4/7)

- Folding
  - Partition key x into several parts
  - All parts except for the last one have the same length
  - Add the parts together to obtain the hash address
- Two possibilities (divide x into several parts)
  - Shift folding: Shift all parts except for the last one, so that the least significant bit of each part lines up with corresponding bit of the last part. k=12320324111220
    - x1=123, x2=203, x3=241, x4=112, x5=20, address=699
  - Folding at the boundaries: reverses even partitions before adding
    - x1=123, x2=302, x3=241, x4=211, x5=20, address=897

---

## Slide 17: Hashing Functions (5/7)

- Folding example:

- 123 203 241 112 20

- P1

- P2

- P3

- P4

- P5

- 123

- shift folding

- 203

- 241

- 112

- 20

- 699

- folding at the boundaries

- 123 203 241 112 20

- MSD ---> LSD
- LSD <--- MSD

---

## Slide 18: Hashing Functions (6/7)

- Digit Analysis
  - Used with static files
    - A static file is one in which all the key are known in advance.
  - Using this method,
    - First, transform the identifiers into numbers using some radix, r.
    - Second, examine the digits of each key, deleting those digits that have the most skewed distribution.
    - We continue deleting digits until the number of remaining digits is small enough to give an address in the range of the hash table.

---

## Slide 19: Hashing Functions (7/7)

- Digital Analysis example:
  - All the identifiers are known in advance
  - ST1 = 682203
  - ST2 = 682171
  - ST3 = 693214
  - ST4 = 695252
  - ST5 = 691340
  - Select 3 digits from n
  - Criterion: Delete the digits having the most skewed distributions

---

## Slide 20: Converting keys to integers

- Program 8.1 p.464

---

## Slide 21: Secures Hash Functions

- message authentication
  - weak collision resistance
    - h(M)=h(M’) difficult to find M’
  - strong collision resistance
    - h(M)=h(M’) difficult to find h
  - one-way property
    - h(M) difficult to find M
- SHA

---

## Slide 22: Overflow Handling

- Open addressing
  - linear probing (linear open addressing)
  - quadratic probing
  - rehashing
  - random probing
- Chaining

---

## Slide 23: Overflow Handling (1/7)

- Linear open addressing (Linear probing)
  - Compute h(x) for key x
  - Examine the buckets: ht[(h(x)+j)%b], 0  j  b-1 (bucket size)
    - The bucket contains x.
    - The bucket contains the empty string (insert to it)
    - The bucket contains a nonempty string other than x (examine the next bucket) (circular rotation)
    - Return to the home bucket ht[h(x)], if the table is full we report an error condition and exit

---

## Slide 24: Overflow Handling (2/7)

> 🖼️ *(包含圖形 / 示意圖)*

- Additive transformation and Division

- Hash table with linear probing (13 buckets, 1 slot/bucket)

> 🖼️ *(包含圖形 / 示意圖)*

- insertion

---

## Slide 25: Overflow Handling (3/7)

- Hash table with linear probing (26 buckets, 1 slot/bucket)

- Problem of Linear Probing
  - Identifiers tend to cluster together
  - Adjacent cluster tend to coalesce
  - Increase the search time
  - Example: suppose we enter the C built-in functions into a 26-bucket hash table in order. The hash function uses the first character in each function name

- ctime

- float

- acos

- atoi

- atol

- char

- define

- ceil

- cos

- floor

- exp

- Enter:

> 🖼️ *(包含圖形 / 示意圖)*

- Enter sequence:

- acos, atoi, char, define, exp, ceil, cos, float, atol, floor, ctime

- # of key comparisons=35/11=3.18

---

## Slide 26: Overflow Handling (4/7)

- Alternative techniques to improve open addressing approach:
  - Rehashing
  - Quadratic probing
  - random probing
- Rehashing
  - Try h1, h2, …, hm in sequence if collision occurs
  - disadvantage
    - comparison of identifiers with different hash values
    - use chain to resolve collisions

---

## Slide 27: Overflow Handling (5/7)

- Quadratic Probing
  - Linear probing searches buckets (h(x)+i)%b
  - Quadratic probing uses a quadratic function of i as the increment
  - Examine buckets h (x), (h(x)+i2)%b, (h(x)-i2)%b, for 1<=i<=(b-1)/2
  - When b is a prime number of the form 4j+3, j is an integer, the quadratic search examines every bucket in the table
```c
Example: h (x)=5, j=1 (b=7)
h(x)%b = 5, (h(x)+1)%b=6, (h(x)-1)%b=4
(h(x)+4)%b=2, (h(x)-4) % b=1, (h(x)+9)%b=0
(h(x)-9)%b=(-4)%7=?
```

| Prime | j | Prime | j |
| --- | --- | --- | --- |
| 3 | 0 | 43 | 10 |
| 7 | 1 | 59 | 14 |
| 11 | 2 | 127 | 31 |
| 19 | 4 | 251 | 62 |
| 23 | 5 | 503 | 125 |
| 31 | 7 | 1019 | 254 |

---

## Slide 28: Overflow Handling (6/7)

- Random Probing
  - Random probing uses a random function s(i) of i as the increment
  - Examine buckets h(x), (h(x)+s(i))%b, for 1<=i<=(b-1)
  - s(i) is a pre-defined random function to generate a random number

---

## Slide 29: Overflow Handling (7/7)

- Chaining
  - Linear probing and its variations perform poorly because inserting an key requires the comparison of key with different hash values.
  - In this approach we maintained a list of synonyms for each bucket.
  - To insert a new element
    - Compute the hash address h (x)
    - Examine the identifiers in the list for h(x).
  - Since we would not know the sizes of the lists in advance, we should maintain them as linked chains

---

## Slide 30: Results of Hash Chaining

- acos, atoi, char, define, exp, ceil, cos, float, atol, floor, ctime
- h(x)=first character of x

- # of key comparisons=21/11=1.91

---
