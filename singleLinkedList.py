class linkedList:

  class node:
    def __init__(self,mvalueNode):
      self.valueNode = mvalueNode
      self.next = None

  def __init__(self):
    self.head = None

  def addNode(self,valueNodeToAdd):
    newNode=self.node(valueNodeToAdd)
    if(self.head == None):
        self.head = newNode
    else:
        newNode.next = self.head
        self.head = newNode

  def removeNode(self,valueNodeToRemove):
    current = self.head
    previous = None
    Found = False
    while (current.valueNode!=None) & ~Found:
        if(current.valueNode == valueNodeToRemove):
            previous.next = current.next
            Found = True
        else:
            previous=current
            current=current.next

  def findNode(self,valueNodeFind):
    nodeToIterate=self.head
    index=0
    while(nodeToIterate!=None):
        if(nodeToIterate.valueNode == valueNodeFind):
            return index
        nodeToIterate=nodeToIterate.next
        index=index+1
    return None

  def showingLinkedList(self):
    nodeToIterate=self.head
    while(nodeToIterate!=None):
        print(nodeToIterate.valueNode)
        nodeToIterate=nodeToIterate.next

a = linkedList()
for i in range (5):
    a.addNode(i)
a.showingLinkedList()
print(a.findNode(3))
a.removeNode(3)
a.showingLinkedList()
