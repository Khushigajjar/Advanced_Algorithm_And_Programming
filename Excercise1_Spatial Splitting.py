class Vertex:
    def __init__(self, val):
        self.val = val
        self.next = None


class SocialGraph:
    def __init__(self, n):
        self.n = n
        self.m = 0
        self.Mgraph = [[False for i in range(n)] for j in range(n)]
        self.Lgraph = [None for i in range(n)]
    
    
    def LL_INSERT(self, head, val):
        new_vertex = Vertex(val)
        new_vertex.next = head
        return new_vertex
    
    
    def LL_REMOVE(self, head, val):
        if head is None:
            return None
        if head.val == val:
            return head.next
        head.next = self.LL_REMOVE(head.next, val)
        return head
    
    
    def LL_SEARCH(self, head, val):
        curr = head
        while curr is not None:
            if curr.val == val:
                return curr
            curr = curr.next
        return None
    
    
    def add_friendship(self, u, v):
        if u == v:
            return
        
        if self.Mgraph[u][v] == True:
            return
        
        self.Mgraph[u][v] = True
        self.Mgraph[v][u] = True
        
        self.Lgraph[u] = self.LL_INSERT(self.Lgraph[u], v)
        self.Lgraph[v] = self.LL_INSERT(self.Lgraph[v], u)
        
        self.m = self.m + 1
    
    
    def remove_friendship(self, u, v):
        if self.Mgraph[u][v] == False:
            return
        
        self.Mgraph[u][v] = False
        self.Mgraph[v][u] = False
        
        self.Lgraph[u] = self.LL_REMOVE(self.Lgraph[u], v)
        self.Lgraph[v] = self.LL_REMOVE(self.Lgraph[v], u)
        
        self.m = self.m - 1
    
    
    def are_friends_matrix(self, u, v):
        return self.Mgraph[u][v]
    
    
    def are_friends_list(self, u, v):
        return self.LL_SEARCH(self.Lgraph[u], v) is not None
    
    
    def get_friends_matrix(self, u):
        for j in range(self.n):
            if self.Mgraph[u][j] == True:
                print(j)
    
    
    def get_friends_list(self, u):
        curr = self.Lgraph[u]
        
        while curr is not None:
            print(curr.val)
            curr = curr.next
    
    
    def get_degree_matrix(self, u):
        count = 0
        
        for j in range(self.n):
            if self.Mgraph[u][j] == True:
                count = count + 1
        
        return count
    
    
    def get_degree_list(self, u):
        count = 0
        curr = self.Lgraph[u]
        
        while curr is not None:
            count = count + 1
            curr = curr.next
        
        return count
    
    def get_num_users(self):
        return self.n
    
    
    def get_num_edges(self):
        return self.m
    
    
    
    def is_complete_graph(self):
        max_edges = self.n * (self.n - 1) // 2
        return self.m == max_edges
    
    
    def graph_density(self):
        if self.n < 2:
            return 0
        
        return (2 * self.m) / (self.n * (self.n - 1))
    
    
    def degree_distribution(self):
        dist = [0] * (self.n)
        
        for u in range(self.n):
            d = self.get_degree_list(u)
            dist[d] = dist[d] + 1
        
        return dist
    
    
    def matrix_to_list(self):
        for u in range(self.n):
            self.Lgraph[u] = None
            
            for v in range(self.n):
                if self.Mgraph[u][v] == True:
                    self.Lgraph[u] = self.LL_INSERT(self.Lgraph[u], v)
    
    
    def list_to_matrix(self):
        for u in range(self.n):
            curr = self.Lgraph[u]
            
            while curr is not None:
                v = curr.val
                self.Mgraph[u][v] = True
                self.Mgraph[v][u] = True
                curr = curr.next
    



# Example user names for testing

names = ["Khushi", "Yuji", "Rahul", "Dhara", "Darshil"]


def print_matrix_with_names(g, names):
    print("\nAdjacency Matrix:")
    print("     ", end="")
    for name in names:
        print(f"{name:8}", end="")
    print()

    for i in range(g.n):
        print(f"{names[i]:5}", end=" ")
        for j in range(g.n):
            print(f"{int(g.Mgraph[i][j]):8}", end="")
        print()


def print_list_with_names(g, names):
    print("\nAdjacency List:")
    for i in range(g.n):
        print(f"{names[i]:5} -> ", end="")
        curr = g.Lgraph[i]
        while curr is not None:
            print(names[curr.val], end=" -> ")
            curr = curr.next
        print("None")


g = SocialGraph(5)

print("Initial number of users:", g.get_num_users())
print("Initial number of edges:", g.get_num_edges())



# Add friendships

g.add_friendship(0, 1)  
g.add_friendship(0, 2)  
g.add_friendship(1, 2)  
g.add_friendship(3, 4)  

print("\nAfter adding friendships:")
print_matrix_with_names(g, names)
print_list_with_names(g, names)

print("\nAre Khushi and Yuji friends (matrix)?", g.are_friends_matrix(0, 1))
print("Are Khushi and Rahul friends (list)?", g.are_friends_list(0, 2))


# Duplicate & self-loop

g.add_friendship(0, 1)  
g.add_friendship(2, 2) 

print("Number of edges:", g.get_num_edges())


# Get friends

print("\nFriends of Khushi (matrix):")
g.get_friends_matrix(0)

print("Friends of Khushi (list):")
g.get_friends_list(0)


# Degree

print("\nDegree of Khushi (matrix):", g.get_degree_matrix(0))
print("Degree of Khushi (list):", g.get_degree_list(0))



# Remove friendships

g.remove_friendship(0, 1) 
g.remove_friendship(0, 4)  

print("\nAfter removing friendship Khushi-Yuji:")
print_matrix_with_names(g, names)
print_list_with_names(g, names)

print("Number of edges:", g.get_num_edges())


# Graph properties

print("\nGraph density:", g.graph_density())
print("Is complete graph:", g.is_complete_graph())


# Complete graph test

g2 = SocialGraph(3)
g2.add_friendship(0,1)
g2.add_friendship(0,2)
g2.add_friendship(1,2)

print("Is complete graph:", g2.is_complete_graph())


# Degree distribution

g3 = SocialGraph(4)
g3.add_friendship(0,1)
g3.add_friendship(0,2)
g3.add_friendship(1,2)
g3.add_friendship(2,3)

print("\nDegree Distribution:", g3.degree_distribution())


# Matrix → List → Matrix

g4 = SocialGraph(4)
g4.add_friendship(0,1)
g4.add_friendship(0,2)
g4.add_friendship(1,2)

print("\nBefore conversion:")
print_matrix_with_names(g4, names[:4])
print_list_with_names(g4, names[:4])

g4.matrix_to_list()

print("\nAfter matrix_to_list():")
print_list_with_names(g4, names[:4])

g4.list_to_matrix()

print("\nAfter list_to_matrix():")
print_matrix_with_names(g4, names[:4])