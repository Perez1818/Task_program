from task import Task

class TaskList:
  """
  Summary: A list of Task objects
  Attributes: task_list(list): a text file that contains a list of tasks 
  """
  def __init__(self):
    """Opens the file and strips any spaces and sorts the list in order"""
    self._task_list = []
    with open('tasklist.txt') as file:
        for idx ,line in enumerate(file):
            task = line.strip().split(',')
            self._task_list.append(Task(task [0] ,task [1] ,task [2]))
    self._task_list.sort()

  def add_task(self ,desc ,date ,time):
    """Adds a task to the file and sorts it again"""
    self._task_list.append(Task(desc ,date ,time))
    self._task_list.sort()

  def mark_complete(self):
    """Returns the task_list but with the first task 'popped'"""
    self._task_list.pop(0)

  def save_file(self):
    """Opens the file to read and write and updates the new task_list """
    with open('tasklist.txt' ,'r') as f:
      existing_data = set(f.readlines())

      existing_data.update(self._task_list)

      with open('tasklist.txt' ,'w') as f:
          for line in self._task_list:
              f.writelines(repr(line) +'\n')

  def __getitem__(self ,index):
    """Returns the Task fromthe list at the specified index"""
    return self._task_list[index]

  def __len__(self):
    """Returns the number of items in the tasklist"""
    return len(self._task_list)

  def __iter__(self):
    """
    Initializes the iterator by resetting the index.
    Returns:
        TaskIterator: The iterator instance.
    """
    self._n = 0
    return self

  def __next__(self):
    """
    Provides the next task in the iteration.
    Returns:
        str: The next task in the iteration.
    Raises:
        StopIteration: When all tasks have been iterated.
    """
    if self._n < len(self._task_list):
      task = self._task_list[self._n]
      self._n += 1
      return task
    else:
      raise StopIteration
    