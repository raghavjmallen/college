# 1. BST Insertion
def bst_insert(root, value):
    """
    Inserts a value into the correct sorted position in a BST.
    """
    if root is None:
        return [value, None, None]
    
    # If the value is smaller, recursively insert on the left
    if value < root[0]:
        root[1] = bst_insert(root[1], value)
    # If the value is larger, recursively insert on the right
    elif value > root[0]:
        root[2] = bst_insert(root[2], value)
        
    return root

# 2. BST Searching
def bst_search(root, target):
    """
    Searches for a value in the BST. Returns True if found, False otherwise.
    Fast performance because it skips half the tree at each step.
    """
    if root is None:
        return False
        
    if root[0] == target:
        return True
    
    # Go left if target is smaller, otherwise go right
    if target < root[0]:
        return bst_search(root[1], target)
    else:
        return bst_search(root[2], target)

# Helper function to find the minimum value node in a subtree (used for deletion)
def find_min_node(root):
    current = root
    # Keep sliding down the leftmost branches
    while current is not None and current[1] is not None:
        current = current[1]
    return current

# 3. BST Deletion
def bst_delete(root, target):
    """
    Deletes a target value from the BST while keeping its sorted order intact.
    """
    if root is None:
        return None

    # Step A: Navigate to find the node to delete
    if target < root[0]:
        root[1] = bst_delete(root[1], target)
    elif target > root[0]:
        root[2] = bst_delete(root[2], target)
    else:
        # Target node found! Handle the 3 deletion cases:

        # Case 1 & 2: Node has 0 children (Leaf) or only 1 child
        if root[1] is None:
            return root[2] # Replace with right child (or None)
        elif root[2] is None:
            return root[1] # Replace with left child

        # Case 3: Node has 2 children
        # Find the smallest node in the right subtree (In-order Successor)
        successor = find_min_node(root[2])
        # Replace current node's value with the successor's value
        root[0] = successor[0]
        # Delete that successor node from the right subtree
        root[2] = bst_delete(root[2], successor[0])

    return root


# --- Verification Code ---
if __name__ == "__main__":
    # Create a BST by inserting numbers sequentially
    # Values will automatically sort themselves
    bst_tree = None
    elements = [50, 30, 70, 20, 40, 60, 80]
    
    for x in elements:
        bst_tree = bst_insert(bst_tree, x)
        
    print("Initial Sorted BST List Layout:")
    print(bst_tree)
    # Visual Layout built under the hood:
    #       50
    #      /  \
    #    30    70
    #   /  \  /  \
    #  20  40 60 80

    # Test Searching
    print("\n--- Testing BST Search ---")
    print(f"Is 40 in the BST?: {bst_search(bst_tree, 40)}")  # Expected: True
    print(f"Is 99 in the BST?: {bst_search(bst_tree, 99)}")  # Expected: False

    # Test Deletion
    print("\n--- Testing BST Deletion (Node 30) ---")
    # Deleting 30 (which has 2 children: 20 and 40)
    # The minimum value of its right branch (40) should take its place.
    bst_tree = bst_delete(bst_tree, 30)
    print("BST after deleting node 30:")
    print(bst_tree)
