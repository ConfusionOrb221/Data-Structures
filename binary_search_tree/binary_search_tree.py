"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value == self.value:
            self.right = BSTNode(value)
        elif value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif self.value < target:
            if self.right == None:
                return False
            else: 
                return self.right.contains(target)
        else:
            if self.left == None:
                return false
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        max = self.value
        branch = self.right
        while(branch):
            max = branch.value
            branch = branch.right
        return max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if(self.left):
            self.left.in_order_print()

        print(self.value)
        if(self.right):
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        stack = [self]
        while(len(stack) != 0):
            temp = []
            for x in stack:
                print(x.value)
                if x.left != None:
                    temp.append(x.left)
                if x.right != None:
                    temp.append(x.right)
            stack = temp

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        current = self
        stack = []
        while(True):
            if current is not None:
                if(current.right != None):
                    stack.append(current)
                print(current.value)
                current = current.left
            elif (stack):
                current = stack.pop() # we get the popped version of current because the current version is None since thats what we check for in the first if statement.
                current = current.right
            else:
                break
            
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)
        if self.left != None:
            self.left.pre_order_dft()
        if self.right != None:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left != None:
            self.left.post_order_dft()
        if self.right != None:
            self.right.post_order_dft()
        
        print(self.value)

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()
print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()  