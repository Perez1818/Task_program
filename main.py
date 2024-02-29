import check_input
from tasklist import TaskList

# Estefania Perez
# November 30, 2023
# Description: Maintains a task list for the user and can be modified/saved by the user

def main_menu():
  """
  Summary: Displays the main menu option and asks the user for a choice between 1-5.
  Args: None
  Returns: A number 1-5 representing the users choice
  """
  choice = check_input.get_int_range('1. Display current task\n'
                                     '2. Display all task\n'
                                     '3. Mark current task complete\n'
                                     '4. Add new task\n'
                                     '5. Search by date\n'
                                     '6. Save and quit\n'
                                     'Enter choice: ' ,1 ,6)
  return choice

def get_time():
  """
  Summary: Asks the user for the hour(0-23) and minute(0-59) for the task they are
  creating and if the minute or hour is a single digit it adds a zero in front of it.
  Args: None
  Returns: the hour and minute as a string in the form the variable called time(HH:MM)
  """
  hour = check_input.get_int_range('Enter hour: ' ,0 ,23)
  minute = check_input.get_int_range('Enter minute: ' ,0 ,59)

  if hour < 10:
    hour = '0' + str(hour)
  if minute < 10:
    minute = '0' + str(minute)
  time = str(hour) + ':' + str(minute)
  return time


def get_date():
  """
  Summary: Asks the user for the month(0-12), day(1-31), year(2000-3000) for the task
  they are creating and if the day or month is a single digit it adds a zero in front
  of it.
  Args: None
  Returns: the month, day, and year as a string in the form the variable called
  date(MM/DD/YY)
  """
  month = check_input.get_int_range('Enter month: ' ,1 ,12)
  day = check_input.get_int_range('Enter day: ' ,1 ,31)
  year = check_input.get_int_range('Enter the year: ' ,2000 ,3000)

  if month < 10:
    month = '0' + str(month)
  if day < 10:
    day = '0' + str(day)
  date = str(month) + '/' + str(day) + '/' + str(year)
  return date


def main():
  # Declaring the class TaskList and creating a boolean
  task_list = TaskList()
  placer = True
  # While loop used to keep the programming going on terms of the user
  while placer:
    print("-Tasklist-")
    print("Tasks to complete: " + str(len(task_list)))
    user_choice = main_menu()
    # Mutiple if statements created to satisfy all known possibilites
    # that might be applied by the user
    if user_choice == 1:
      if len(task_list) == 0:
        print("No current task")
      print("Current task is:")
      print(task_list[0])

    elif user_choice == 2:
      for i in task_list:
        print(str(i))

    elif user_choice == 3:
      if len(task_list) > 1:
        print(f"Marking current task as complete:\n{task_list[0]}")
        task_list.mark_complete()
        print(f"New current task is:\n{task_list[0]}")
      elif len(task_list) == 1:
        task_list.mark_complete()
        print("There are no more tasks to complete")
      else:
        print("\nThere are no more tasks to complete")
    elif user_choice == 4:
      desc = input("Enter a task: ")
      print("Enter due date:")
      date = get_date()
      time = get_time()
      task_list.add_task(desc ,date ,time)

    elif user_choice == 5:
      print("Enter date to search")
      date = get_date()
      found = False
      for task in task_list:
        if date == task.date:
          found = True
          print(task)
          break
      if not found:
        print("Could not find the task")

    elif user_choice == 6:
      
      task_list.save_file()
      placer = False

    print()


main()
