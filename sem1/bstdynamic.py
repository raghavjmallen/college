def create_tree_dynamically():
    """
    Interactively builds a binary tree by prompting the user for child values.
    Typing 'None' or leaving it blank skips that child branch.
    """
    print("--- Dynamic Binary Tree Creator ---")
    print("Instructions: Enter node values. Type 'None' or leave blank to stop a child branch.\n")
    
    # 1. Initialize the Root Node
    root_val = input("Enter the value for the ROOT node: ").strip()
    if not root_val or root_val.lower() == 'none':
        print("Empty tree created.")
        return None
        
    root = [root_val, None, None]
    queue = [root]  # Queue to manage level-by-level user prompts
    
    # 2. Process Level by Level
    while len(queue) > 0:
        current_node = queue.pop(0)
        current_val = current_node[0]
        
        # --- Handle Left Child Prompt ---
        left_input = input(f"Enter LEFT child for [{current_val}]: ").strip()
        if left_input and left_input.lower() != 'none':
            # Create left node and link it to current_node[1]
            left_node = [left_input, None, None]
            current_node[1] = left_node
            # Queue it so we can ask for its children later
            queue.append(left_node)
        else:
            current_node[1] = None
            
        # --- Handle Right Child Prompt ---
        right_input = input(f"Enter RIGHT child for [{current_val}]: ").strip()
        if right_input and right_input.lower() != 'none':
            # Create right node and link it to current_node[2]
            right_node = [right_input, None, None]
            current_node[2] = right_node
            # Queue it so we can ask for its children later
            queue.append(right_node)
        else:
            current_node[2] = None

    return root

# --- Execution Example ---
if __name__ == "__main__":
    # This will trigger the interactive input console loop
    my_custom_tree = create_tree_dynamically()
    
    print("\n--- Final Generated Tree Layout ---")
    print(my_custom_tree)
