from collections import deque

class SmartPrinter:
  def __init__(self):
    self.urgent = deque()
    self.normal = deque()

  def add_job(self, job, priority="normal"):
    if priority == "urgent":
      self.urgent.append(job)
      print(job," added to urgent queue")
    else:
      self.normal.append(job)
      print(job, "added to normal queue")

  def job_print(self):
    if self.urgent:
      print("Printing Urgent job : ", self.urgent.popleft())
    elif self.normal:
      print("Printing Normal jobs: ",self.normal.popleft())
    else:
      print("No Jobs to print")

  def display(self):
    print("Urgent Prints: ", list(self.urgent))
    print("Normal Prints: ", list(self.normal))


printer = SmartPrinter()

printer.add_job("Doc1","urgent")
printer.add_job("Result")
printer.add_job("PanCard", "urgent")
printer.add_job("Project")

printer.display()
printer.job_print()
printer.job_print()
printer.job_print()
printer.job_print()
