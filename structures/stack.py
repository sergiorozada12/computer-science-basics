class stack:
  class node:
    def __init__(self,data):
      self.value=data
      self.next=None

  def __init__(self):
    self.head=None

  def pop(self):
    if (self.head==None):
      return

    self.head=self.head.next

  def push(self,data):
    newNode=self.node(data)

    if(self.head==None):
      self.head=newNode

    newNode.next=self.head
    self.head=newNode

  def peek(self):
    if(self.head==None):
      return -1

    dataToReturn=self.head.value
    return dataToReturn

  def isEmpty(self):
    return self.head==None
