class Task:
  def __init__(self ,desc ,date ,time):
    """
    Represents a singular task in the tasklist
    Attributes:
    description(str in list): desc a string that describes the task
    date(int in list): date an int that describes the precise month/day/year of the task
    time(int in list): time an int that describes the hour/minute of the task
    """
    self._desc = desc
    self._date = date
    self._time = time

  
  @property 
  def date(self):
    """
    Getter method for accessing the date property.
    Returns:
        datetime.date: The date attribute.
    """
    return self._date    
    
  def __str__(self):
    """Returns an f string of a task in a specific format"""
    return f'{self._desc} - Due: {self._date} at {self._time}'

  def __repr__(self):
    """Returns an f string of a task in a specific format"""
    return f"{self._desc},{self._date},{self._time}"

  def __lt__(self ,other):
    """Returns the task that is less than another task. Using the month/day/year and hour/minute to compare"""
    d1 ,t1 = self._date.split('/') ,self._time.split(':')
    d2 ,t2 = other._date.split('/') ,other._time.split(':')
    return (d1[2] ,d1[0] ,d1[1] ,t1[0] ,t1[1] ,self._desc) < (d2[2] ,d2[0] ,d2[1] ,t2[0],t2[1], other._desc)
  
  