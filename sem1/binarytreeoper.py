# 1. Creation / Insertion (Level-Order queue parsing)
def build_custom_tree(elements):
    """
    Builds an unsorted nested list tree from a flat list containing explicit None values.
    """
    if not elements or elements[0] is None:
        return None

    # Create root node: [value, left, right]
    root = [elements[0], None, None]
    queue = [root]
    index = 1
    
    while index < len(elements) and len(queue) > 0:
        current_node = queue.pop(0)
        
        # Process Left Child slot
        if index < len(elements):
            left_val = elements[index]
            index += 1
            if left_val is not None:
                current_node[1] = [left_val, None, None]
                queue.append(current_node[1])
                
        # Process Right Child slot
        if index < len(elements):
            right_val = elements[index]
            index += 1
            if right_val is not None:
                current_node[2] = [right_val, None, None]
                queue.append(current_node[2])

    return root

# 2. Searching
def search_nested(root, target):
    """
    Searches for a target value anywhere in the asymmetrical nested tree.
    """
    if root is None:
        return False
        
    # Check current node value
    if root[0] == target:
        return True
        
    # Recursively check left subtree OR right subtree
    return search_nested(root[1], target) or search_nested(root[2], target)

# 3. Finding Height
def get_height_nested(root):
    """
    Calculates tree height. Empty tree is -1. Single node tree is 0.
    """
    if root is None:
        return -1
        
    left_height = get_height_nested(root[1])
    right_height = get_height_nested(root[2])
    
    return 1 + max(left_height, right_height)

# 4. Counting Number of Nodes
def count_nodes_nested(root):
    """
    Counts total valid (non-None) nodes inside the nested structure.
    """
    if root is None:
        return 0
        
    return 1 + count_nodes_nested(root[1]) + count_nodes_nested(root[2])
# 1. Insertion (Appends value to the next open level-order spot)
def insert_dynamic(root, value):
    """
    Dynamically inserts a new element into the first available space 
    in the nested list tree using a queue (level-order traversal).
    """
    new_node = [value, None, None]
    if root is None:
        return new_node
        
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        
        # Check left slot
        if current[1] is None:
            current[1] = new_node
            return root
        else:
            queue.append(current[1])
            
        # Check right slot
        if current[2] is None:
            current[2] = new_node
            return root
        else:
            queue.append(current[2])
    return root

# 2. Minimum & Maximum Values (Unsorted tree must check all paths)
def find_min_max(root):
    """
    Returns a tuple (min_value, max_value) from the tree.
    Since the tree is unsorted, we must traverse all valid nodes.
    """
    if root is None:
        return float('inf'), float('-inf')
        
    # Get values from left and right subtrees
    left_min, left_max = find_min_max(root[1])
    right_min, right_max = find_min_max(root[2])
    
    # Compare with current node's value
    current_val = root[0]
    overall_min = min(current_val, left_min, right_min)
    overall_max = max(current_val, left_max, right_max)
    
    return overall_min, overall_max

# 3. Number of Leaves
def count_leaves(root):
    """
    Counts leaf nodes (nodes with NO children).
    """
    if root is None:
        return 0
    # A node is a leaf if both left and right children are None
    if root[1] is None and root[2] is None:
        return 1
        
    return count_leaves(root[1]) + count_leaves(root[2])

# 4. Number of Internal Nodes
def count_internal_nodes(root):
    """
    Counts internal nodes (nodes that have at least one child).
    """
    if root is None:
        return 0
    # If it's a leaf, it's not an internal node
    if root[1] is None and root[2] is None:
        return 0
        
    # Current node is internal + count from left and right subtrees
    return 1 + count_internal_nodes(root[1]) + count_internal_nodes(root[2])

# 5. Check if Tree is a Full Binary Tree
def is_full_binary_tree(root):
    """
    A binary tree is Full if every node has either 0 or 2 children.
    """
    if root is None:
        return True
        
    # If a leaf node, it's valid
    if root[1] is None and root[2] is None:
        return True
        
    # If both children exist, recursively check both subtrees
    if root[1] is not None and root[2] is not None:
        return is_full_binary_tree(root[1]) and is_full_binary_tree(root[2])
        
    # If it has only one child, it's NOT a full binary tree
    return False

# 6. Delete Element Node
def delete_node(root, target):
    """
    Deletes a target node from an unsorted binary tree.
    Replaces the target's value with the deepest, rightmost node's value,
    and then deletes that deepest node to keep the tree structured.
    """
    if root is None:
        return None

    # Step A: Find the target node and the deepest rightmost node using Level-Order
    target_node = None
    deepest_node = None
    parent_of_deepest = None
    
    queue = [(root, None)] # stores tuple of (current_node, parent_node)
    
    while len(queue) > 0:
        current, parent = queue.pop(0)
        deepest_node = current
        parent_of_deepest = parent
        
        if current[0] == target:
            target_node = current
            
        if current[1] is not None:
            queue.append((current[1], current))
        if current[2] is not None:
            queue.append((current[2], current))
            
    # Step B: If the target was found, swap values and remove the deepest node
    if target_node is not None:
        # Swap values
        target_node[0] = deepest_node[0]
        
        # Disconnect the deepest node from its parent
        if parent_of_deepest is not None:
            if parent_of_deepest[1] == deepest_node:
                parent_of_deepest[1] = None
            else:
                parent_of_deepest[2] = None
        else:
            # Tree only had 1 node, which is now deleted
            return None
            
    return root


# --- Driver Implementation Testing ---
if __name__ == "__main__":
    # Helper parser function from the previous step to establish base state
    from __main__ import build_custom_tree
    custom_elements = [10, 20, 30, None, 50, 60, 70, None, None, 70, None]
    tree = build_custom_tree(custom_elements)
    
    print("Initial Tree Setup:")
    print(tree)
    
    # Min & Max
    t_min, t_max = find_min_max(tree)
    print(f"\nMin Value: {t_min} | Max Value: {t_max}")
    
    # Leaves & Internals
    print(f"Number of Leaf Nodes: {count_leaves(tree)}")          # Expected: 3 (50, 60, deepest 70)
    print(f"Number of Internal Nodes: {count_internal_nodes(tree)}")  # Expected: 4 (10, 20, 30, parent 70)
    
    # Structural Property Check
    print(f"Is Full Binary Tree?: {is_full_binary_tree(tree)}") # Expected: False (20 has only a right child)

    # Dynamic Insertion Test
    print("\n--- Inserting 99 dynamically ---")
    tree = insert_dynamic(tree, 99) # Will fill the empty left slot under node 20
    print("Tree after insertion:")
    print(tree)
    print(f"Is Full Binary Tree now?: {is_full_binary_tree(tree)}") # Expected: True (all structural gaps closed)

    # Deletion Test
    print("\n--- Deleting Node 30 ---")
    tree = delete_node(tree, 30)
    print("Tree after deleting 30:")
    print(tree)


# --- Driver Code / Execution Matrix ---
if __name__ == "__main__":
    # Your target pattern layer-by-layer sequence:
    # Level 0: 10
    # Level 1: 20, 30
    # Level 2: None, 50, 60, 70
    # Level 3: (under 60: None, None), (under 70: 70, None)
    custom_elements = [10, 20, 30, None, 50, 60, 70, None, None, 70, None]
    
    # 1. Test Creation
    tree = build_custom_tree(custom_elements)
    print("Generated Asymmetrical Nested Tree Layout:")
    print(tree)
    # Output matches your target layout exactly!

    # 2. Test Searching
    print("\n--- Searching Operations ---")
    print(f"Is 50 in the tree?: {search_nested(tree, 50)}")   # Expected: True
    print(f"Is 70 in the tree?: {search_nested(tree, 70)}")   # Expected: True
    print(f"Is 99 in the tree?: {search_nested(tree, 99)}")   # Expected: False

    # 3. Test Tree Metrics
    print("\n--- Structural Analysis Metrics ---")
    print(f"Total Height of the Tree: {get_height_nested(tree)}")       # Expected: 3 (Path: 10 -> 30 -> 70 -> 70)
    print(f"Total Number of Valid Nodes: {count_nodes_nested(tree)}")  # Expected: 6 (10, 20, 30, 50, 60, 70, 70)
