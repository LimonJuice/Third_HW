class TreeNode:

    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key, lc, rc):
        self.key = key
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self

        if self.hasRightChild():
            self.rightChild.parent = self

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def findMax(self):
        current = self
        while current.hasRightChild():
            current = current.rightChild
        return current

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent


class BinaryTree:

    def __init__(self):
        self.root = None
        self.size = 0
    
    def insertArr(self, arr=[]):
        for i in arr:
            sekf.put(i)

    def put(self,key):
        if self.root:
            self._put(key,self.root)
        else:
            self.root = TreeNode(key)
        self.size = self.size + 1

    
    def _put(self,key,currentNode):
        if key < currentNode.key: 
            if currentNode.hasLeftChild():
                   self._put(key,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,parent=currentNode)
        else:  
            if currentNode.hasRightChild():
                   self._put(key,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,parent=currentNode)

    
    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.key
           else:
                  return None
       else:
           return None

        
    def _get(self,key,currentNode):
       if currentNode.key == key: 
           return currentNode
       elif key < currentNode.key and currentNode.hasLeftChild(): 
           return self._get(key,currentNode.leftChild)
       elif key > currentNode.key and currentNode.hasRightChild(): 
           return self._get(key,currentNode.rightChild)
       else:
           return None

    
    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False

    
    def remove(self,currentNode):
         if currentNode.isLeaf(): 
           if currentNode == currentNode.parent.leftChild:
               currentNode.parent.leftChild = None
           else:
               currentNode.parent.rightChild = None
         elif currentNode.hasBothChildren():
             succ = currentNode.findSuccessor()
             succ.spliceOut()
             currentNode.key = succ.key

         else: 
           if currentNode.hasLeftChild(): 
             if currentNode.isLeftChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.leftChild
             elif currentNode.isRightChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.leftChild
             else:
                 currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
           else: 
             if currentNode.isLeftChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.rightChild
             elif currentNode.isRightChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.rightChild
             else:
                 currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)

    def delete(self,key):
      if self.size > 1:
         delet = self._get(key,self.root)
         if delet:
             self.remove(delet)
             self.size = self.size-1
         else:
             return None
      elif self.size == 1 and self.root.key == key:
         self.root = None
         self.size = self.size - 1
      else:
          return None
 
    def findMax(self):
      current = self.root
      while current.hasRightChild():
          current = current.rightChild
      return current.key
