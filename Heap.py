class  BinHeap:
    def __init__(self):
        self.heapLst=[0]
        self.currentSize=0

    def percUp(self,i):
        while i//2>0:
            if self.heapLst[i]<self.heapLst[i//2]:
                temp=self.heapLst[i//2]
                self.heapLst[i//2]=self.heapLst[i]
                temp=self.heapLst[i]
            i=i//2

    def insertion(self, x):
        self.heapLst.append(x)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            sm = self.minChild(i)
            if self.heapLst[i] > self.heapLst[sm]:
                temp = self.heapLst[i]
                self.heapLst[i] = self.heapLst[sm]
                self.heapLst[sm] = temp
            i = sm
            
            
    def minChild(self, i):
           if i * 2 + 1 > self.currentSize:
               return i * 2
           else:
               if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                   return i * 2
               else:
                   return i * 2 + 1

      def delMin(self):
          retval = self.heapList[1]
          self.heapLst[1] = self.heapLst[self.currentSize]
          self.currentSize = self.currentSize - 1
          self.heapLst.pop()
          self.percDown(1)
          return retval
            
            
    def maxChild(self, i):
        if i * 2 + 1 < self.currentSize:
            return i * 2
        else:
            if self.heapLst[i * 2] > self.heapLst[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMax(self):
        retval = self.heapLst[1]
        self.heapLst[1] = self.heapLst[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapLst.pop()
        self.percUp(1)
        return retval

    def buildHeap(self, lst):
        i = len(lst) // 2
        self.currentSize = len(lst)
        self.heapLst = [0] + lst[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
