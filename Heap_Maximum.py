class  HeapMaximum:
    def __init__(self, arr=[]):
        self.heapLst=[0]
        self.currentSize=0
        
        
    def insertArr(self, arr=[]):
        for i in arr:
            self.insert(i)
            
            
    def percUp(self,i):
        half=i//2
        while half>0:
            if self.heapLst[i]<self.heapLst[half]:
                temp=self.heapLst[half]
                self.heapLst[half]=self.heapLst[i]
                self.heapLst[i]=temp
            i=half

    def insertion(self, x):
        self.heapLst.append(x)
        self.currentSize=self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2)<=self.currentSize:
            sm=self.minChild(i)
            if self.heapLst[i]>self.heapLst[sm]:
                temp=self.heapLst[i]
                self.heapLst[i]=self.heapLst[sm]
                self.heapLst[sm]=temp
            i=sm           
            
    def maxChild(self, i):
        doub=i * 2
        if doub + 1<self.currentSize:
            return doub
        else:
            if self.heapLst[doub]>self.heapLst[doub + 1]:
                return doub
            else:
                return doub + 1

    def getMax(self) :
        return self.heapLst[1]
            
            
    def delMax(self):
        retval=self.heapLst[1]
        self.heapLst[1]=self.heapLst[self.currentSize]
        self.currentSize=self.currentSize - 1
        self.heapLst.pop()
        self.percUp(1)
        return retval

