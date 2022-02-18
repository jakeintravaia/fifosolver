class Page:
  def __init__(self, value):
    self.value = value

cache = []
inserts = [0, 3, 4, 3, 8, 6, 9, 1, 4, 9, 7, 9, 5, 3, 1, 2, 4] # Change these values according to problem set
cache_size = 4 # Change this as needed
faults = 0 # Global variable used to track fault count

def main():
  global cache_size
  # Initialize empty pages
  for i in range((cache_size - 1), -1, -1):
    p = Page(-1)
    cache.append(p)
  insertPage()

def insertPage():
  global cache_size
  global faults
  page_index = 0
  for i in inserts:
    fifo = cache[page_index]
    if not pageExists(i) and cacheFull():
      print("***PAGE FAULT***")
      faults += 1
    if not pageExists(i):
      fifo.value = i
      if page_index < (cache_size -1):
        page_index += 1
      else:
        page_index = 0
    elif pageExists(i):
      cache[getIndex(i)].value = i
    print("PAGE INSERT {}".format(i))
    printPages()
  printSummary()


def printSummary():
  global faults
  print("Total Inserts: {}".format(len(inserts)))
  print("Total Faults: {}".format(faults))

def cacheFull():
  if all(x.value != -1 for x in cache):
    return True
  else:
    return False

def getIndex(value):
  for page in cache:
    if page.value == value:
      return cache.index(page)

def pageExists(value):
  if any(x.value == value for x in cache):
    return True
  else:
    return False

def printPages():
  border = ("="*20)
  print(border)
  for page in cache:
    if page.value == -1:
      print("Value: EMPTY")
    else:
      print("Value: {}".format(page.value))
  print(border)


if __name__ == "__main__":
  main()