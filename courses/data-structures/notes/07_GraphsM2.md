# 07_GraphsM2

> 📌 **課程主題筆記**: 本文件由 `07_GraphsM2.ppt` 完整擷取，包含所有投影片內容、階層清單、程式碼區塊、表格、圖表標籤與註記，共 89 頁投影片。

## Slide 1

- 資料結構
- Data Structure

- Chapter 6: Graphs
- 國立聯合大學
- 資訊管理學系
- 温敏淦

---

## Slide 2: Konigsberg Bridge Problem

- A river Pregel flows around the island Keniphof and then divides into two.
- Four land areas A, B, C, D have this river on their borders.
- The four lands are connected by 7 bridges a – g.
- Determine whether it’s possible to walk across all the bridges exactly once in returning back to the starting land area.

---

## Slide 3: Konigsberg Bridge Problem (Cont.)

- C

- c

- d

- g

- A
- Kneiphof

- e

- D

- C

- g

- f

- a

- c

- d

- B

- b

- e

- A

- D

- b

- a

- f

- B

---

## Slide 4: Euler’s Graph

- Define the degree of a vertex to be the number of edges incident to it
- Euler showed that there is a walk starting at any vertex, going through each edge exactly once and terminating at the start vertex iff the degree of each vertex is even. This walk is called Eulerian.
- No Eulerian walk of the Konigsberg bridge problem since all four vertices are odd edges.

---

## Slide 5: Application of Graphs

- Analysis of electrical circuits
- Finding shortest routes
- Project planning
- Identification of chemical compounds
- Statistical mechanics
- Genertics
- Cybernetics
- Linguistics
- Social Sciences, and so on …

---

## Slide 6: Definition of A Graph

- A graph, G, consists tof two sets, V and E.
  - V is a finite, nonempty set of vertices.
  - E is set of pairs of vertices called edges.
- The vertices of a graph G can be represented as V(G).
- Likewise, the edges of a graph, G, can be represented as E(G).
- Graphs can be either undirected graphs or directed graphs.
- For a undirected graph, a pair of vertices (u, v) or (v, u) represent the same edge.
- For a directed graph, a directed pair <u, v> has u as the tail and the v as the head. Therefore, <u, v> and <v, u> represent different edges.

---

## Slide 7: Three Sample Graphs

- 0

- 0

- 0

- 1

- 2

- 1

- 2

- 1

- 3

- 3

- 4

- 5

- 6

- 2

- V(G1) = {0, 1, 2, 3}

- V(G2) = {0, 1, 2, 3, 4, 5, 6}

- V(G3) = {0, 1, 2}

- E(G1) = {(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)}

- E(G2) = {(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)}

- E(G3) = {<0, 1>, <1, 0>, <1, 2>}

- (a) G1

- (b) G2

- (c) G3

---

## Slide 8: Graph Restrictions

- A graph may not have an edge from a vertex back to itself.
  - (v, v) or <v, v> are called self edge or self loop. If a graph with self edges, it is called a graph with self edges.
- A graph may not have multiple occurrences of the same edge.
  - If without this restriction, it is called a multigraph.

---

## Slide 9: Examples of Graph like Structures

- 0

- 0

- 1

- 1

- 3

- 2

- 2

- (b) Multigraph

- (a) Graph with a self edge

---

## Slide 10: Complete Graph

- The number of distinct unordered pairs (u, v) with u≠v in a graph with n vertices is n(n-1)/2.
- A complete undirected graph is an undirected graph with exactly n(n-1)/2 edges.
- A complete directed graph is a directed graph with exactly n(n-1) edges.

---

## Slide 11: Graph Edges

- If (u, v) is an edge in E(G), vertices u and v are adjacent and the edge (u, v) is the incident on vertices u and v.
- For a directed graph, <u, v> indicates u is adjacent to v and v is adjacent from u.

---

## Slide 12: Subgraph and Path

- Subgraph: A subgraph of G is a graph G’ such that V(G’) V(G) and E(G’) E(G).
- Path: A path from vertex u to vertex v in graph G is a sequence of vertices u, i1, i2, …, ik, v, such that (u, i1), (i1, i2), …, (ik, v) are edges in E(G).
  - The length of a path is the number of edges on it.
  - A simple path is a path in which all vertices except possibly the first and last are distinct.
  - A path (0, 1), (1, 3), (3, 2) can be written as 0, 1, 3, 2.
- Cycle: A cycle is a simple path in which the first and last vertices are the same.
- Similar definitions of path and cycle can be applied to directed graphs.

---

## Slide 13: G1 and G3 Subgraphs

- 0

- 0

- 0

- 1

- 2

- 1

- 2

- 1

- 2

- 3

- (i)

- (ii)

- (iii)

- 3

- (iv)

- (a) Some subgraphs of G1

- 0

- 0

- 0

- 0

- 1

- 1

- 1

- 2

- (i)

- 2

- 2

- (ii)

- (iv)

- (a) Some subgraphs of G3

- (iii)

---

## Slide 14: Connected Graph

- Two vertices u and v are connected in an undirected graph iff there is a path from u to v (and v to u).
- An undirected graph is connected iff for every pair of distinct vertices u and v in V(G) there is a path from u to v in G.
- A connected component of an undirected is a maximal connected subgraph.
- A tree is a connected acyclic graph.

---

## Slide 15: Strongly Connected Graph

- A directed graph G is strongly connected iff for every pair of distinct vertices u and v in V(G), there is directed path from u to v and also from v to u.
- A strongly connected component is a maximal subgraph that is strongly connected.

---

## Slide 16: Graphs with Two Connected Components

- H2

- H1

- 4

- 0

- 5

- 6

- 1

- 2

- 7

- 3

- G4

---

## Slide 17: Strongly Connected Components of G3

- 0

- 2

- 1

---

## Slide 18: Degree of A Vertex

- Degree of a vertex: The degree of a vertex is the number of edges incident to that vertex.
- If G is a directed graph, then we define
  - in-degree of a vertex: is the number of edges for which vertex is the head.
  - out-degree of a vertex: is the number of edges for which the vertex is the tail.
- For a graph G with n vertices and e edges, if di is the degree of a vertex i in G, then the number of edges of G is

---

## Slide 19: Abstract of Data Type Graphs

```c
class Graph
{
public:
	virtual ~Graph() {}
	bool IsEmpty() const{return n = = 0};
	int NumberOfVertices() const{return n};
	int NumberOfEdges() const{return e};
	virtual int Degree(int u) const = 0;
	virtual bool ExistsEdge(int u, int v) const = 0;
	virtual void InsertVertex(int v) = 0;
	virtual void InsertEdge(int u, int v) = 0;
	virtual void DeleteVertex(int v) = 0;
	virtual void DeleteEdge(int u, int v) = 0;
	private:
		int n;	
		int e;	
};
```

---

## Slide 20: 1.Adjacency Matrices

- 0

- 1

- 2

- 3

- (a) G1

- (b) G3

- (c) G4

---

## Slide 21: Adjacent Matrix

- Let G(V, E) be a graph with n vertices, n ≥ 1. The adjacency matrix of G is a two-dimensional nxn array, A.
  - A[i][j] = 1 iff the edge (i, j) is in E(G).
  - The adjacency matrix for a undirected graph is symmetric, it may not be the case for a directed graph.
- For an undirected graph the degree of any vertex i is its row sum.
- For a directed graph, the row sum is the out-degree and the column sum is the in-degree.

---

## Slide 22: Adjacent Lists

- 0

- 1

- 2

- 3

- HeadNodes

- [0]

- 3

- 1

- 2

- 0

- [1]

- 2

- 3

- 0

- 0

- [2]

- 1

- 3

- 0

- 0

- [3]

- 0

- 1

- 2

- 0

- (a) G1

- HeadNodes

- [0]

- 1

- 0

- [1]

- 2

- 0

- 0

- [2]

- 0

- (b) G3

---

## Slide 23: Adjacent Lists (Cont.)

- HeadNodes

- [0]

- 2

- 1

- 0

- [1]

- 3

- 0

- 0

- [2]

- 0

- 3

- 0

- [3]

- 1

- 1

- 0

- [4]

- 5

- 0

- [5]

- 6

- 4

- 0

- [6]

- 5

- 7

- 0

- [7]

- 6

- 0

- (c) G4

---

## Slide 24: 2.Adjacency Lists

- Instead of using a matrix to represent the adjacency of a graph, we can use n linked lists to represent the n rows of the adjacency matrix.
- Each node in the linked list contains two fields: data and link.
  - data: contain the indices of vertices adjacent to a vertex i.
  - Each list has a head node.
- For an undirected graph with n vertices and e edges, we need n head nodes and 2e list nodes.
- The degree of any vertex may be determined by counting the number nodes in its adjacency list.
- The number of edges in G can be determined in O(n + e).
- For a directed graph (also called digraph),
  - the out-degree of any vertex can be determined by counting the number of nodes in its adjacency list.
  - the in-degree of any vertex can be obtained by keeping another set of lists called inverse adjacency lists.

---

## Slide 25: Inverse Adjacency Lists for G3

- 0

- 1

- [0]

- 1

- 0

- 0

- 0

- [1]

- 2

- 1

- 0

- [2]

---

## Slide 26: 3.Sequential Representation of Graph G4

- 1

- 12

- 0

- 11

- 10

- 9

- 8

- 6

- 5

- 7

- 17

- 4

- 18

- 19

- 20

- 21

- 22

- 2

- 3

- 13

- 14

- 15

- 16

> 📊 **圖表元素 / 標籤:** 9, 11, 13, 15, 17, 18, 20, 22, 23, 2, 1, 3, 0, 5, 6, 4, 7

- Node[n+2*e+1]

- 4

- 0

- 5

- 6

- 1

- 2

- 7

- 3

---

## Slide 27: Orthogonal List Representation for G3

- From

- head nodes (shown twice)

- 0

- 1

- 2

- 0

- 0

- 1

- 0

- 0

- To

- 1

- 1

- 0

- 0

- 1

- 2

- 0

- 0

- 0

- 2

- 0

- 1

- 2

---

## Slide 28: 4.Multilists

- In the adjacency-list representation of an undirected graph, each edge (u, v) is represented by two entries.
- Multilists: To be able to determine the second entry for a particular edge and mark that edge as having been examined, we use a structure called multilists.
  - Each edge is represented by one node.
  - Each node will be in two lists.

- m(boolean)

- vertex1

- vertex2

- link1

- link2

---

## Slide 29: Adjacency Multilists for G1

- 0

- 1

- 2

- 3

- HeadNodes

- edge (0, 1)

- 0

- 1

- N1

- N3

- [0]

- N0

- [1]

- 0

- 2

- N2

- N3

- edge (0, 2)

- N1

- [2]

- 0

- 3

- 0

- N4

- N2

- edge (0, 3)

- [3]

- edge (1, 2)

- 1

- 2

- N4

- N5

- N3

- The lists are

- 1

- 3

- 0

- N5

- edge (1, 3)

- N4

- Vertex 0: N0 -> N1 -> N2

- Vertex 1: N0 -> N3 -> N4

- edge (2, 3)

- 2

- 3

- 0

- 0

- N5

- Vertex 2: N1 -> N3 -> N5

- Vertex 3: N2 -> N4 -> N5

---

## Slide 30: Weighted Edges

- Very often the edges of a graph have weights associated with them.
  - distance from one vertex to another
  - cost of going from one vertex to an adjacent vertex.
  - To represent weight, we need additional field, weight, in each entry.
  - A graph with weighted edges is called a network.

---

## Slide 31: 6.2Graph Operations

- A general operation on a graph G is to visit all vertices in G that are reachable from a vertex v.
  - Depth-first search
  - Breath-first search

---

## Slide 32: 6.2.1Depth-First Search

- Starting from vertex, an unvisited vertex w adjacent to v is selected and a depth-first search from w is initiated.
- When the search operation has reached a vertex u such that all its adjacent vertices have been visited, we back up to the last vertex visited that has an unvisited vertex w adjacent to it and initiate a depth-first search from w again.
- The above process repeats until no unvisited vertex can be reached from any of the visited vertices.
- Program 6.1

---

## Slide 33

```c
virtual void Graph::DFS(){  //Driver
  visited=new bool[n];
  fill(visited,visited+n,false);
  DFS(0);
  delete[] visited;
}
//Workhorse
virtual void Graph::DFS(const int v){
  visited[v]=true;
  for(each vertex w adjacent to v)
    if(!visited[w])DFS(w);
}
```

- program 6.1

---

## Slide 34: Graph G and Its Adjacency Lists

- 0

- 1

- 2

- 3

- 4

- 5

- 6

- HeadNodes

- 7

- [0]

- 1

- 2

- 0

- [1]

- 0

- 3

- 4

- 0

- [2]

- 0

- 5

- 6

- 0

- [3]

- 1

- 7

- 0

- [4]

- 1

- 7

- 0

- [5]

- 2

- 7

- 0

- [6]

- 2

- 7

- 0

- [7

- 3

- 4

- 5

- 6

- 0

---

## Slide 35: Analysis of DFS

- If G is represented by its adjacency lists, the DFS time complexity is O(e).
- If G is represented by its adjacency matrix, then the time complexity to complete DFS is O(n2).

---

## Slide 36: 6.2.2 Breath-First Search

- Starting from a vertex v, visit all unvisited vertices adjacent to vertex v.
- Unvisited vertices adjacent to these newly visited vertices are then visited, and so on.
- If an adjacency matrix is used, the BFS complexity is O(n2).
- If adjacency lists are used, the time complexity of BFS is O(e).
- Program 6.2

---

## Slide 37

```c
virtual void Graph::BFS(int v){
  visited=new bool[n];
  fill(visited,visited+n,false);
  visited[v]=true;
  Queue<int>q;
  q.enQ(v);
  while(!q.IsEmpty()){
    v=q.deQ();
    for(all vertex w adjacent to v)
       if(!visited[w]){
        q.enQ(w);
        visited[w]=true;
      }
    }
    delete[] visited;
}
```

- program 6.2

---

## Slide 38: Depth-First and Breath-First Spanning Trees/connected component

- 0

- 1

- 2

- 3

- 4

- 5

- 6

- 7

- 0

- 0

> 📊 **圖表元素 / 標籤:** 3, 4, 1, 2, 5, 6

- 7

- 7

- (a) DFS (0) spanning tree

- (b) BFS (0) spanning tree

---

## Slide 39: 6.2.3 Connected Components

```c
virtual void Graph::Components(){  //by DFS
  visited=new bool[n];
  fill(visited,visited+n,false);
  for(i=0;i<n;i++){
    if(!visited[i]){
        DFS(i);
        OutputNewComponent();
    }
  }
  delete[] visited;
}//also can get by BFS
```

---

## Slide 40: 6.2.4 Spanning Tree

- Any tree consisting solely of edges in G and including all vertices in G is called a spanning tree.
- Spanning tree can be obtained by using either a depth-first or a breath-first search.
- When a nontree edge (v, w) is introduced into any spanning tree T, a cycle is formed.
- A spanning tree is a minimal subgraph, G’, of G such that V(G’) = V(G), and G’ is connected. (Minimal subgraph is defined as one with the fewest number of edges).
- Any connected graph with n vertices must have at least n-1 edges, and all connected graphs with n – 1 edges are trees. Therefore, a spanning tree has n – 1 edges.

---

## Slide 41: A Complete Graph and Three of Its Spanning Trees

---

## Slide 42: A Connected Graph and Its Biconnected Components

- 0

- 8

- 9

- 0

- 8

- 9

- 1

- 7

- 7

- 1

- 7

> 📊 **圖表元素 / 標籤:** 2, 3

- 5

- 1

- 7

- 4

- 6

- 3

- 5

- 2

- 3

- 5

- 4

- 6

- (a) A connected graph

- (b) Its biconnected components

---

## Slide 43: Biconnected Components

- Definition: A vertex v of G is an articulation point iff the deletion of v, together with the deletion of all edges incident to v, leaves behind a graph that has at least two connected components.
- Definition: A biconnected graph is a connected graph that has no articulation points.
- Definition: A biconnected component of a connected graph G is a maximal biconnected subgraph H of G. By maximal, we mean that G contains no other subgraph that is both biconnected and properly contains H.

---

## Slide 44: Biconnected Components (Cont.)

- Two biconnected components of the same graph can have at most one vertex in common.
- No edge can be in two or more biconnected components.
- The biconnected components of G partition the edges of G.
- The biconnected components of a connected, undirected graph G can be found by using any depth-first spanning tree of G.
- A nontree edge (u, v) is a back edge with respect to a spanning tree T iff either u is an ancestor of v or v is an ancestor of u.
- A nontree edge that is not back edge is called a cross edge.
- No graph can have cross edges with respect to any of its depth-first spanning trees.

---

## Slide 45: Biconnected Components (Cont.)

- The root of the depth-first spanning tree is an articulation point iff it has at least two children.
- Any other vertex u is an articulation point iff it has at least one child, w, such that it is not possible to reach an ancestor of u using a path composed solely of w, descendants of w, and a single back edge.
- Define low(w) as the lowest depth-first number that can be reached fro w using a path of descendants followed by, at most, one back edge.

---

## Slide 46: articulation point

- u is an articulation point iff u is either the root of the spanning tree and has two or more children or u is not the root and u has a child w such that low(w) ≥ dfn(u).

---

## Slide 47: Depth-First Spanning Tree

> 🖼️ *(包含圖形 / 示意圖)*

- 1

- (1)

- 3

- 0

- 8

- 9

- 9

- 10

- 5

- 2

- 6

- (6)

- (1)

- 4

- 5

- back edge

- 1

- 7

- 4

- 8

- 6

- 2

- 6

- 1

- 3

- (6)

- 7

- (1)

- 2

- 3

- 5

- 3

- 4

- (1)

- 1

- 7

- (6)

- 8

- 4

- 6

- 7

- 2

- 0

- (10)

- 8

- 9

- 10

- 5

- 9

- (9)

- (5)

---

## Slide 48: dfn and low values for the Spanning Tree

| vertex | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dfn | 5 | 4 | 3 | 1 | 2 | 6 | 7 | 8 | 10 | 9 |
| low | 5 | 1 | 1 | 1 | 1 | 6 | 6 | 6 | 10 | 9 |

- Program 6.4 DfnLow
- Program 6.5 Biconnected

---

## Slide 49: Program 6.4 DfnLow

```c
virtual void Graph::DfnLow(const int x){  //by DFS at x
  num=1;
  dfn=new int[n];  low=new int[n];
  fill(dfn,dfn+n,0); fill(low,low+n,0);
  DfnLow(x,-1);
  delete[]dfn,low;
}
virtua; void Graph::DfnLow(const int u,const int v){
  dfn[u]=low[u]=num++;
  for(each w adjacent from u)){
    if(dfn[w]==0){
        dfnLow(w,u);
        low[u]=min(low[u],low[w]);
    }else if(w!=v)
       low[u]=min(low[u],dfn[w]); //back edge
}
```

---

## Slide 50: Program 6.5 Biconnected

```c
virtual void Graph::Biconnected (){
  num=1;
  dfn=new int[n];  low=new int[n];
  fill(dfn,dfn+n,0); fill(low,low+n,0);
 Biconnected(0,-1);
  delete[]dfn,low;
}
virtual void Graph:: Biconnected (const int u,const int v){
  dfn[u]=low[u]=num++;
  for(each w adjacent from u)){
    if(v!=w&&dfn[w]<dfn[u])STACK.push(u,w);
    if(dfn[w]==0){
      Biconnected(w,u);
      low[u]=min(low[u],low[w]);
      if(low[w]>dfn[u]){
          outputBiComponent();  //from STACK
      }
    }else if(w!=v)
       low[u]=min(low[u],dfn[w]); //back edge
}
```

---

## Slide 51: 6.3 Minimal Cost Spanning Tree (p.352)

- The cost of a spanning tree of a weighted, undirected graph is the sum of the costs (weights) of the edges in the spanning tree.
- A minimum-cost spanning tree is a spanning tree of least cost.
- Three greedy-method algorithms available to obtain a minimum-cost spanning tree of a connected, undirected graph.
  - Kruskal’s algorithm
  - Prim’s algorithm
  - Sollin’s algorithm

---

## Slide 52: Kruskal’s Algorithm

- Kruskal’s algorithm builds a minimum-cost spanning tree T by adding edges to T one at a time.
- The algorithm selects the edges for inclusion in T in nondecreasing order of their cost.
- An edge is added to T if it does not form a cycle with the edges that are already in T.
- Theorem 6.1: Let G be any undirected, connected graph. Kruskal’s algorithm generates a minimum-cost spanning tree.
- Program 6.6 (p.355)
  - Sorting O(eloge) vs. Min heap O(e)+O(loge)
  - Cycle testing->set & union

---

## Slide 53: Stages in Kruskal’s Algorithm

- 0

- 0

- 0

- 28

- 1

- 1

- 1

- 10

- 10

- 14

- 16

- 5

- 6

- 2

- 5

- 6

- 2

- 5

- 6

- 2

- 24

- 18

- 25

- 12

- 4

- 4

- 4

- 3

- 3

- 3

- 22

- (a)

- (b)

- (c)

---

## Slide 54: Stages in Kruskal’s Algorithm (Cont.)

- 0

- 0

- 0

- 1

- 1

- 1

- 10

- 10

- 10

- 14

- 14

- 16

- 5

- 6

- 2

- 5

- 6

- 2

- 5

- 6

- 2

- 12

- 12

- 12

- 4

- 4

- 4

- 3

- 3

- 3

- (d)

- (e)

- (f)

---

## Slide 55: Stages in Kruskal’s Algorithm (Cont.)

- 0

- 0

- 1

- 10

- 1

- 10

- 14

- 16

- 14

- 16

- 5

- 6

- 2

- 5

- 6

- 2

- 25

- 12

- 12

- 4

- 4

- 3

- 22

- 3

- 22

- (g)

- (g)

---

## Slide 56: Prim’s Algorithm

- Similar to Kruskal’s algorithm, Prim’s algorithm constructs the minimum-cost spanning tree edge by edge.
- The difference between Prim’s algorithm and Kruskal’s algorithm is that the set of selected edges forms a tree at all times when using Prim’s algorithm while a forest is formed when using Kruskal’s algorithm.
- In Prim’s algorithm, , a least-cost edge (u, v) is added to T such that T∪ {(u, v)} is also a tree. This repeats until T contains n-1 edges.
- Prim’s algorithm in program 6.7 has a time complexity O(n2).

---

## Slide 57: Stages in Prim’s Alogrithm

- 0

- 0

- 0

- 1

- 1

- 1

- 10

- 10

- 10

- 5

- 6

- 2

- 5

- 6

- 2

- 5

- 6

- 2

- 25

- 25

- 4

- 4

- 4

- 3

- 3

- 3

- 22

- (b)

- (a)

- (c)

---

## Slide 58: Stages in Prim’s Alogrithm (Cont.)

- 0

- 0

- 0

- 1

- 1

- 1

- 10

- 10

- 10

- 14

- 16

- 16

- 5

- 6

- 2

- 5

- 6

- 2

- 5

- 6

- 2

- 25

- 25

- 25

- 12

- 12

- 12

- 4

- 4

- 4

- 3

- 3

- 3

- 22

- 22

- 22

- (f)

- (e)

- (d)

---

## Slide 59: Sollin’s Algorithm

- Contrast to Kruskal’s and Prim’s algorithms, Sollin’s algorithm selects multiple edges at each stage.
- At the beginning, the selected edges and all the n vertices form a spanning forest.
- During each stage, an minimum-cost edge is selected for each tree in the forest.
- It’s possible that two trees in the forest to select the same edge. Only one should be used.
- Also, it’s possible that the graph has multiple edges with the same cost. So, two trees may select two different edges that connect them together. Again, only one should be retained.

---

## Slide 60: Stages in Sollin’s Algorithm

- 0

- 0

- 1

- 1

- 10

- 10

- 14

- 16

- 14

- 5

- 6

- 2

- 5

- 6

- 2

- 25

- 12

- 12

- 4

- 4

- 3

- 22

- 3

- 22

- (b)

- (a)

---

## Slide 61: 6.4 Shortest Paths (p.360)

- Usually, the highway structure can be represented by graphs with vertices representing cities and edges representing sections of highways.
- Edges may be assigned weights to represent the distance or the average driving time between two cities connected by a highway.
- Often, for most drivers, it is desirable to find the shortest path from the originating city to the destination city.

---

## Slide 62: Single Source/All Destinations: Nonnegative Edge Costs

- Let S denotes the set of vertices to which the shortest paths have already been found.
  - If the next shortest path is to vertex u, then the path begins at v, ends at u, and goes through only vertices that are in S.
  - The destination of the next path generated must be the vertex u that has the minimum distance among all vertices not in S.
  - The vertex u selected in 2) becomes a member of S.
- The algorithm is first given by Edsger Dijkstra. Therefore, it’s sometimes called Dijstra Algorithm.
- Program 6.8 ShortestPath
  - O(n2)

---

## Slide 63: Program 6.8 ShortestPath

```c
virtual void Graph:: ShortestPath(const int n,const int v){
  for(int i=0i<n;i++){s[i]=false; dist[i]=length[v][i];}
  s[v]=true; dist[v]=0;
  for(i=0;i<n-2;i++){
    int u=Choose(n);  //select u  dist[u]=min{dist[w],s[w]=false;}
    s[u]=true;
    for(int w=0;w<n;w++)
      if(!s[w]&&dist[u]+length[u][w]<dist[w])
        dist[w]= dist[u]+length[u][w];
  }
}
```

---

## Slide 64: Graph and Shortest Paths From Vertex 0 to all destinations

- 45

- 10

- 50

- 0

- 1

- 2

- Path

- Length

- 35

- 1) 0, 3

- 10

- 15

- 10

- 20

- 30

- 20

- 2) 0, 3, 4

- 25

- 3) 0, 3, 4, 1

- 45

- 5

- 3

- 4

- 3

- 15

- 4) 0, 2

- 45

- (b) Shortest paths from 0

- (a) Graph

---

## Slide 65: Diagram for Example 6.5

- Boston

- 4

- 1500

- Chicago

- 3

- 250

- 1200

- 1000

- San Francisco

- 800

- 5

- New York

- 2

- 1

- Denver

- 1400

- 300

- 1000

- 900

- 1700

- 0

- 1000

- 7

- 6

- Miami

- Los Angeles

- New Orleans

---

## Slide 66: Action of Shortest Path

> 📊 **圖表元素 / 標籤:** 0, 1, 2, 3, 4, 5, 6, 7, 300, 800, 1700, 1000, 1400, 1200, 1500, 250, 900, Los Angeles, San Francisco, Denver, New Orleans, Miami, New York, Boston, Chicago

```c
virtual void Graph:: ShortestPath(const int n,const int v){
  for(int i=0i<n;i++){s[i]=false; dist[i]=length[v][i];}
  s[v]=true; dist[v]=0;
  for(i=0;i<n-2;i++){
    int u=Choose(n);  //select u  dist[u]=min{dist[w],s[w]=false;}
    s[u]=true;
    for(int w=0;w<n;w++)
      if(!s[w]&&dist[u]+length[u][w]<dist[w])
        dist[w]= dist[u]+length[u][w];
  }
}
```

| iteration | S | Vertex selected | Distance | Distance | Distance | Distance | Distance | Distance | Distance | Distance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| iteration | S | Vertex selected | LA | SF | DEN | CHI | BOST | NY | MIA | NO |
| iteration | S | Vertex selected | [0] | [1] | [2] | [3] | [4] | [5] | [6] | [7] |
| Initial | -- | --- | +∞ | +∞ | +∞ | 1500 | 0 | 250 | +∞ | +∞ |
| 1 | {4} | 5 | +∞ | +∞ | +∞ | 1250 | 0 | 250 | 1150 | 1650 |
| 2 | {4,5} | 6 | +∞ | +∞ | +∞ | 1250 | 0 | 250 | 1150 | 1650 |
| 3 | {4,5,6} | 3 | +∞ | +∞ | 2450 | 1250 | 0 | 250 | 1150 | 1650 |
| 4 | {4,5,6,3} | 7 | 3350 | +∞ | 2450 | 1250 | 0 | 250 | 1150 | 1650 |
| 5 | {4,5,6,3,7} | 2 | 3350 | 3250 | 2450 | 1250 | 0 | 250 | 1150 | 1650 |
| 6 | {4,5,6,3,7,2} | 1 | 3350 | 3250 | 2450 | 1250 | 0 | 250 | 1150 | 1650 |
|  | {4,5,6,3,7,2,1} |  |  |  |  |  |  |  |  |  |

---

## Slide 67: 6.4.2 Single Source/All Destinations: General Weights

- When negative edge lengths are permitted, the graph must not have cycles of negative length.

- 5

- -5

- 7

- 0

- 1

- 2

- (a) Directed graph with a negative-length edge

- -2

- 0

- 1

- 2

- 1

- 1

- (b) Directed graph with a cycle of negative length

---

## Slide 68: 6.4.2 Single Source/All Destinations: General Weights

- When there are no cycles of negative length, there is a shortest path between any two vertices of an n-vertex graph that has at most n-1 edges on it.
  - If the shortest paht from v to u with at most k, k > 1, edges has no more than k – 1 edges, then distk[u] = distk-1[u].
  - If the shortest path from v to u with at most k, k > 1, edges has exactly k edges, then it is comprised of a shortest path from v to some vertex j followed by the edge <j, u>. The path from v to j has k – 1 edges, and its length is distk-1[j].
- The distance can be computed in recurrence by the following:
- The algorithm is also referred to as the Bellman and Ford Algorithm (Program 6.9). Adjacent matrix O(n3), Adjacent list O(ne)

- Dynamic programming

---

## Slide 69: Program 6.9 ShortestPath general edge

```c
virtual void Graph:: BellmanFord(const int n,const int v){
  for(int i=0;i<n;i++)dist[i]=length[v][i];
  for(k=2;k<n;k++)
    for(each u such that u!=v and u has at least one incoming edge){
      for(each<i,u> in the graph)
      if(dist[u]>dist[i]+length[i][u])
        dist[u]= dist[i]+length[i][u];
  }
}
```

---

## Slide 70: Shortest Paths with Negative Edge Lengths

| k | distk[7] | distk[7] | distk[7] | distk[7] | distk[7] | distk[7] | distk[7] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| k | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| 1 | 0 | 6 | 5 | 5 | ∞ | ∞ | ∞ |
| 2 | 0 | 3 | 3 | 5 | 5 | 4 | ∞ |
| 3 | 0 | 1 | 3 | 5 | 2 | 4 | 7 |
| 4 | 0 | 1 | 3 | 5 | 0 | 4 | 5 |
| 5 | 0 | 1 | 3 | 5 | 0 | 4 | 3 |
| 6 | 0 | 1 | 3 | 5 | 0 | 4 | 3 |

- -1

- 1

- 4

- 3

- 6

- 1

- -2

- 5

- 0

- 2

- 6

- -2

- 5

- 3

- 3

- 5

- -1

- (a) A directed graph

- (b) distk

---

## Slide 71: All-Pairs Shortest Paths

- In all-pairs shortest-path problem, we are to find the shortest paths between all pairs of vertices u and v, u ≠ v.
  - Use n independent single-source/all-destination problems using each of the n vertices of G as a source vertex. Its complexity is O(n3) (or O(n2 logn + ne) if Fibonacci heaps are used).
  - On graphs with negative edges the run time will be O(n4) if adjacency matrices are used and O(n2e) if adjacency lists are used.

---

## Slide 72: All-Pairs Shortest Paths (Cont.)

- A simpler algorithm with complexity O(n3) is available. It works faster when G has edges with negative length, as long as the graphs have at least c*n edges for some suitable constant c.
  - An-1[i][j]: the length of the shortest i-to-j path in G
  - Ak[i][j]: the length of the shortest path from i to j going through no intermediate vertex of index greater than k.
  - A-1[i][j]: is just the length[i][j]
- The shortest path from i to j going through no vertex with index greater than k does not go through the vertex with index k. so its length is Ak-1[i][j].
- The shortest path goes through vertex k. The path consists of subpath from i to k and another one from k to j.
- Ak[i][j] = min{Ak-1[i][j], Ak-1[i][k]+ Ak-1[k][j] }, k ≥ 0

---

## Slide 73: Program 6.10 all-pairs ShortestPath

```c
virtual void Graph:: AllLength(const int n){
  for(int i=0;i<n;i++)
    for(int j=0;j<n;j++)
      a[i][j]=length[i][j];
  for(k=0;k<n;k++)
    for(i=0;i<n;i++)
      for(j=0;j<n;j++)
        if(a[i][k]+a[k][j]<a[i][j])
          a[i][j]=a[i][k]+a[k][j];
  }
}
```

---

## Slide 74: Example for All-Pairs Shortest-Paths Problem

| A0 | 0 | 1 | 2 |
| --- | --- | --- | --- |
| 0 | 0 | 4 | 11 |
| 1 | 6 | 0 | 2 |
| 2 | 3 | 7 | 0 |

| A-1 | 0 | 1 | 2 |
| --- | --- | --- | --- |
| 0 | 0 | 4 | 11 |
| 1 | 6 | 0 | 2 |
| 2 | 3 | ∞ | 0 |

- 6

- 0

- 1

- 4

- (b) A-1

- (c) A0

- 11

- 2

- 3

- 2

| A1 | 0 | 1 | 2 |
| --- | --- | --- | --- |
| 0 | 0 | 4 | 6 |
| 1 | 6 | 0 | 2 |
| 2 | 3 | 7 | 0 |

| A2 | 0 | 1 | 2 |
| --- | --- | --- | --- |
| 0 | 0 | 4 | 6 |
| 1 | 5 | 0 | 2 |
| 2 | 3 | 7 | 0 |

- (d) A1

- (e) A2

- Program 6.10
- O(n3)

---

## Slide 75: 6.5.1Activity-on-Vertex (AOV) Networks

- Definition: A directed graph G in which the vertices represent tasks or activities and the edges represent precedence relations between tasks is an activity-on-vertex network or AOV network.
- Definition: Vertex i in an AOV network G is a predecessor of vertex j iff there is a directed path from vertex i to vertex j. i is an immediate predecessor of j iff <i, j> is an edge in G. If i is a predecessor of j, then j is an successor of i. If i is an immediate predecessor of j, then j is an immediate successor of i.

---

## Slide 76: Activity-on-Vertex (AOV) Networks (Cont.)

- Definition: A relation · is transitive iff it is the case that for all triples, i, j, k, i.j and j·k => i·k. A relation · is irreflexive on a set S if for no element x in S it is the case that x·x. A precedence relation that is both transitive and irreflexive is a partial order.
- Definition: A topological order is a linear ordering of the vertices of a graph such that, for any two vertices i and j, if i is a predecessor of j in the network, then i precedes j in the linear ordering.

---

## Slide 77: An Activity-on-Vertex (AOV) Network

| Course number | Course name | Prerequisites |
| --- | --- | --- |
| C1 | Programming I | None |
| C2 | Discrete Mathematics | None |
| C3 | Data Structures | C1, C2 |
| C4 | Calculus I | None |
| C5 | Calculus II | C4 |
| C6 | Linear Algebra | C5 |
| C7 | Analysis of Algorithms | C3, C6 |
| C8 | Assembly Language | C3 |
| C9 | Operating Systems | C7, C8 |
| C10 | Programming Languages | C7 |
| C11 | Compiler Design | C10 |
| C12 | Artificial Intelligence | C7 |
| C13 | Computational Theory | C7 |
| C14 | Parallel Algorithms | C13 |
| C15 | Numerical Analysis | C5 |

---

## Slide 78: An Activity-on-Vertex (AOV) Network (Cont.)

- C9

- C10

- C11

- C1

- C8

- C12

- C2

- C14

- C3

- C7

- C13

- C4

- C5

- C6

- C15

- Topology order : C1,C2,C4,C5,C3,C6,C8,C7,C10,C13,C12,C14,C15,C11,C9
- C4,C5,C2,C1,C6,C3,C8,C15,C7,C9,C10,C11,C12,C13,C14

---

## Slide 79: Figure 6.36 Action of Program 6.11 on an AOV network

- Program 6.11 Topology order : 0,3,2,5,1,4

- 1

- 1

- 1

- 0

- 2

- 4

- 2

- 4

- 2

- 4

- 3

- 5

- 3

- 5

- 5

- (a) Initial

- (c) Vertex 3 deleted

- (b) Vertex 0 deleted

- 1

- 1

- 4

- 4

- 4

- 5

- (f) Vertex 1 deleted

- (e) Vertex 5 deleted

- (d) Vertex 2 deleted

---

## Slide 80: Figure 6.37 Internal representation used by topological sorting algorithm

- first

- count

- data

- link

- 0

- [0]

- 1

- 2

- 3

- 0

- [1]

- 1

- 4

- 0

- [2]

- 1

- 4

- 5

- 0

- 1

- [3]

- 5

- 4

- 0

- 0

- 3

- [4]

- [5]

- 0

- 2

---

## Slide 81: Program 6.12 TopologicalOrder

```c
virtual void Graph:: TopologicalOrder(){
  int top=-1;
  for(int i=0;i<n;i++)
    if(count[i]==0){count[i]=top; top=i;}
  for(int i=0;i<n;i++){
    if(top==-1) throw “Network has a cycle”;
    cout<<j<<endl;
    Chain <>::ChainTeroator ji=adjLists[j].begin;
    while(ji){
      count[*ji]--;
      if(count[*ji]==0){count[*ji]=top; top=*ji;
      ji++
    }
  }
}
```

---

## Slide 82: 6.5.2An AOE Network Adjacency lists for Figure 6.39 (a)

- first

- count

- vertex

- dur

- link

- 0

- [0]

- 1

- 6

- 3

- 5

- 0

- 2

- 4

- [1]

- 1

- 0

- 4

- 1

- [2]

- 1

- 0

- 4

- 1

- 1

- [3]

- 0

- 5

- 2

- 2

- [4]

- 6

- 9

- 0

- 7

- 7

- [5]

- 1

- 0

- 7

- 4

- a4 = 1

- 1

- 6

- a10 = 2

- [6]

- 1

- 0

- 8

- 2

- a1 = 6

- a7= 9

- start

- finish

- 0

- 4

- 8

- 2

- [7]

- 0

- 8

- 4

- a2 = 4

- a8= 7

- a5 = 1

- 2

- [8]

- 0

- a11 = 4

- 2

- 7

- a3 = 5

- a9 = 4

- 3

- 5

- a6 = 2

---

## Slide 83: 6.5.2An AOE Network

- ee(6)=16
- Le(6)=16

- ee(1)=6
- Le(1)=6

- 1

- 6

- ee(4)=7
- Le(4)=7

- ee(0)=0
- Le(0)=0

- ee(8)=18
- Le(8)=18

- a10 = 2

- a7= 9

- a4 = 1

- a1 = 6

- start

- finish

- 0

- 4

- 8

- ee(2)=4
- Le(2)=6

- ee(7)=14
- Le(7)=14

- a8= 7

- a2 = 4

- vertex(event)
- Earliest start time : ee(j)
- Latest start time : le(j)
- edge(activity)
- Earliest time:e(i)
- Latest time : l(i)

- a5 = 1

- a11 = 4

- 2

- 7

- a3 = 5

- ee(5)=7
- Le(5)=10

- ee(3)=5
- Le(3)=8

- Critical path
- Critical activities
- : e(i)= l(i)

- a9 = 4

- 3

- 5

- a6 = 2

| event | interpretation |
| --- | --- |
| 0 | Start of project |
| 1 | Completion of activity a1 |
| 4 | Completion of activities a4 and a5 |
| 7 | Completion of activities a8 and a9 |
| 8 | Completion of project |

---

## Slide 84: Computation of ee

- ee(6)=16
- Le(6)=16

- ee(1)=6
- Le(1)=6

- 1

- 6

- ee(4)=7
- Le(4)=7

- ee(0)=0
- Le(0)=0

- ee(8)=18
- Le(8)=18

- a10 = 2

- a7= 9

- a4 = 1

- a1 = 6

- start

- 0

- 4

- 8

- ee(2)=4
- Le(2)=6

- ee(7)=14
- Le(7)=14

- a8= 7

- a2 = 4

- a5 = 1

- a11 = 4

- 2

- 7

- a3 = 5

- ee(5)=7
- Le(5)=10

- ee(3)=5
- Le(3)=8

- a9 = 4

| ee | [0] | [1] | [2] | [3] | [4] | [5] | [6] | [7] | [8] | Stack |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Initial | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | [0] |
| output 0 | 0 | 6 | 4 | 5 | 0 | 0 | 0 | 0 | 0 | [3,2,1] |
| output 3 | 0 | 6 | 4 | 5 | 0 | 7 | 0 | 0 | 0 | [5,2,1] |
| output 5 | 0 | 6 | 4 | 5 | 0 | 7 | 0 | 11 | 0 | [2,1] |
| output 2 | 0 | 6 | 4 | 5 | 5 | 7 | 0 | 11 | 0 | [1] |
| output 1 | 0 | 6 | 4 | 5 | 7 | 7 | 0 | 11 | 0 | [4] |
| output 4 | 0 | 6 | 4 | 5 | 7 | 7 | 0 | 14 | 0 | [7,6] |
| output 7 | 0 | 6 | 4 | 5 | 7 | 7 | 16 | 14 | 18 | [6] |
| output 6 | 0 | 6 | 4 | 5 | 7 | 7 | 16 | 14 | 18 | [8] |
| output 8 |  |  |  |  |  |  |  |  |  |  |

- 3

- 5

- Topological order

- le[j]=min{le[i]-<j,i>}

---

## Slide 85: Computation of le

- ee(6)=16
- Le(6)=16

- ee(1)=6
- Le(1)=6

- 1

- 6

- ee(4)=7
- Le(4)=7

- ee(0)=0
- Le(0)=0

- ee(8)=18
- Le(8)=18

- a10 = 2

- a7= 9

- a4 = 1

- a1 = 6

- start

- 0

- 4

- 8

- ee(2)=4
- Le(2)=6

- ee(7)=14
- Le(7)=14

- a8= 7

- a2 = 4

- a5 = 1

- a11 = 4

- 2

- 7

- a3 = 5

- ee(5)=7
- Le(5)=10

- ee(3)=5
- Le(3)=8

- a9 = 4

- Using reverse topology order<0,3,5,2,1,4,7,6,8>
- le[8]=ee[8]
- le[6]=min{le[8]-2}=16
- le[7]=min{le[8]-4}=14
- le[4]=min{le[6]-9,le[7]-7}=7
- le[1]=min{le[4]-1}=6
- le[2]=min{le[4]-1}=6
- le[5]=min{le[7]-4}=10
- le[3]=min{le[5]-2}=8
- le[0]=min{le[1]-6,le[2]-4,le[3]-5}=0
- le[j]=min{le[i]-<j,i>}

- 3

- 5

| ee | [0] | [1] | [2] | [3] | [4] | [5] | [6] | [7] | [8] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| output 6 | 0 | 6 | 4 | 5 | 7 | 7 | 16 | 14 | 18 |

---

## Slide 86: Critical paths

- a4 = 1
- e(4)=6

- 1

- 6

- a10 = 2

- a1 = 6
- e(1)=0

- a7= 9
- e(7)=e(8)=7

- 0

- 4

- 8

- a2 = 4

- a8= 7

- a5 = 1
- e(5)=4

- a11 = 4

- 2

- 7

- a3 = 5

- a9 = 4

- e[i]=ee[k], k a[i] x
- l[i]=le[x]-a[i]
- Fig. 6.41

- a6 = 2

- 3

- 5

|  | [0] | [1] | [2] | [3] | [4] | [5] | [6] | [7] | [8] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ee | 0 | 6 | 4 | 5 | 7 | 7 | 16 | 14 | 18 |
| le | 0 | 6 | 6 | 8 | 7 | 10 | 16 | 14 | 18 |

|  | [0] | [1] | [2] | [3] | [4] | [5] | [6] | [7] | [8] | [9] | [10] | [11] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| e | 0 | 0 | 0 | 0 | 6 | 4 | 5 | 7 | 7 | 7 | 16 | 14 |
| l | 0 | 0 | 2 | 3 | 6 | 6 | 8 | 7 | 7 | 10 | 16 | 14 |

- 1

- 6

- a1 = 6

- a10 = 2

- a4 = 6

- a7= 9

- start

- finish

- 0

- 4

- 8

- a8= 7

- a11 = 4

- 7

---

## Slide 87

---

## Slide 88: 6.4.4Transitive Closure

- Definition: The transitive closure matrix, denoted A+, of a graph G, is a matrix such that A+[i][j] = 1 if there is a path of length > 0 from i to j; otherwise, A+[i][j] = 0.
- Definition: The reflexive transitive closure matrix, denoted A*, of a graph G, is a matrix such that A*[i][j] = 1 if there is a path of length >= 0 from i to j; otherwise, A*[i][j] = 0.

---

## Slide 89: Graph G and Its Adjacency Matrix A, A+, A*

- 4

- 0

- 1

- 2

- 3

- (a) Digraph G

- (b) Adjacency matrix A

- (c) A+

- (d) A*

---
