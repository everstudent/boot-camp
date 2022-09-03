from datetime import datetime
import os
import glob


class Singleton(type):
  _instances = {}
  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
    return cls._instances[cls]




class logger(metaclass=Singleton):
  __root = '' # private property

  # construct with optional log root dir
  def __init__(self, root = '/tmp'):
    self.__root = root

  # returns root to public consumer 
  def get_root(self):
    return self.__root

  # path to today's log file
  def get_logfile_path(self):
    return self.get_root() + '/' + datetime.now().strftime("%Y_%m_%d") + '.log'

  # write message to today's log
  def write_log(self, message):
    try:
      with open(self.get_logfile_path(), 'a') as f:
        f.write('[' + datetime.now().strftime("%H:%M:%S") + '] ' + message + "\n");
        return True
    except:
      return False
  
  # drop today's logs
  def clear_log(self):
    try:
      os.remove(self.get_logfile_path())
      return True
    except:
      return False
 
  # returns list of today's logs
  def get_logs(self):
    lines = []
    try:
      with open(self.get_logfile_path(), 'r') as f:
        for line in f:
          lines.append(line.strip())
    except:
      return []

    return lines

  # returns last event from today's logs
  def get_last_event(self):
    lines = self.get_logs()
    
    if len(lines) == 0:
      return False

    return lines[len(lines)-1]

  # returns all log files
  def get_all_logs(self):
    files = []
    for f in glob.glob(self.get_root() + '/*.log'):
      files.append(f)

    return files



# create logger instance
l = logger()


# log something
l.write_log('Opa')

# get logs
print(l.get_logs())
print(l.get_last_event())
print(l.get_all_logs())

# check singleton (should output True)
l_second = logger()
print(l_second == l)