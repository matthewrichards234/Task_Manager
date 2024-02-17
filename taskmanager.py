from node import Node

class TaskManager:
  def __init__(self):
    self.head = None

  def add_task_to_end(self, task_to_add): # Tail of LL
    pass

  def add_task_to_front(self, task_to_add): # Head of LL
    # Create new node.
    new_node = Node(task_to_add)

    # Base case; LL is empty.
    if self.head is None:
      self.head = new_node
      return

    # Make new node point to current head.
    new_node.set_next_node(self.head)

    # Head is now the new node pushed on.
    self.head = new_node

  def display_tasks(self):
    temp = self.head
    if temp is None:
      print("To-Do list is empty. Please add a task.")
    else:
      while temp != None:
        print(temp.get_data(), end=' -> ')
        temp = temp.get_next_node()
      print()

  def remove_task(self, task_to_remove): # Will let the user choose which task they want to remove.
    temp = self.head

    # Will allow us to check if the head of the LL.
    previous = None

    # Traverse Linked List. 
    while temp is not None:
      # If temp node contains the value to remove.
      if temp.get_data() == task_to_remove:
        # If the element to remove is the head.
        if previous is None:
          self.head = temp.get_next_node()
        else:
          # Remove temp node by updating the next pointer of the previous node.
          previous = temp.get_next_node()
        return True # Task removed successfully.
      # Move to the next node.
      previous = temp
      temp = temp.get_next_node()

    return False # Element not found in the linked list
    # Print message if not found for user

  def mark_task_completion(self, completed_task):
    temp = self.head
    while temp:
      if temp.get_data() == completed_task:
        temp.data += " (Completed)"
        return
      temp = temp.get_next_node()

# Test cases
if __name__ == "__main__":
    manager = TaskManager()

    # Test adding tasks
    manager.add_task_to_front("Task 1")
    manager.add_task_to_front("Task 2")
    manager.add_task_to_front("Task 3")

    # Test displaying tasks
    print("Tasks:")
    manager.display_tasks()

    # Test removing tasks
   # manager.remove_task("Task 2")

    # Test marking tasks as completed
    manager.mark_task_completion("Task 3")

    # Display tasks after modifications
    print("\nTasks after modifications:")
    manager.display_tasks()