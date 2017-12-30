class doubleLinkedList:
  class node:
    def __init__(self,data):
      self.value=data
      self.prev=None
      self.next=None

  def __init__(self):
    self.head=None

  def addNode(self,data):
    newNode=self.node(data)

    if(self.head==None):
      self.head=newNode
    else:
      newNode.next=self.head
      self.head.prev=newNode
      self.head=newNode

  def search(self,data):
    nodeCopy=self.head
    index=0

    while(nodeCopy!=None):
      if(nodeCopy.value==data):
        return index
      index=index+1
      nodeCopy=nodeCopy.next

    return None

  def removeNode(self,data):
    nodeCopy=self.head

    while(nodeCopy!=None):
      if(nodeCopy.value==data):
        nodeCopy.prev.next=nodeCopy.next
        nodeCopy.next.prev=nodeCopy.prev
      nodeCopy=nodeCopy.next

  def showingLinkedList(self):
    nodeCopy=self.head

    while(nodeCopy!=None):
      print(nodeCopy.value)
      nodeCopy=nodeCopy.next
