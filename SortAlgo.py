class BubbleSort(object):
    def sort(self, arr, reverse = False, display =False):
        swap = 1
        for i in xrange(len(arr)-1, -1, -1):
            if swap == 0:
                break
            swap = 0
            for j in xrange(0,i):
                if (not reverse and arr[j] > arr[j+1]) or (reverse and arr[j] < arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swap = 1
                if display:
                    print(arr)
        return(arr)

class SelectionSort(object):
    def sort(self, arr, reverse = False, display = False):
        for i in xrange(len(arr)-1):
            minIndx = i
            for j in xrange(i+1, len(arr)):
                if (not reverse and arr[minIndx] > arr[j]) or (reverse and arr[minIndx] < arr[j]):
                    minIndx = j
            arr[i] , arr[minIndx] = arr[minIndx], arr[i]
            if display:
                print(arr)
        return(arr)
        
class InsertionSort(object):
    def sort(self, arr, reverse = False, display = False):
        for i in xrange(1,len(arr)):
            val = arr[i]
            Indx = i
            while(((not reverse and arr[Indx-1] > val) or (reverse and arr[Indx-1] < val)) and Indx >=1):
                arr[Indx] = arr[Indx-1]
                Indx-=1
                if display:
                    print(arr)
            arr[Indx] = val
        return(arr)
        
class ShellSort(object):
    def sort(self, arr, reverse = False, display = False):
        h=1
        while h < len(arr)/9:
            h=3*h+1
        if display:
            print("h = ", h)
        while h>0:
            for i in xrange(h+1,len(arr)):
                val = arr[i]
                Indx = i
                while(((not reverse and arr[Indx-h] > val) or (reverse and arr[Indx-h] < val)) and Indx >h):
                    arr[Indx] = arr[Indx-h]
                    Indx-=h
                    if display:
                        print(arr)
                arr[Indx] = val
            h=h/3
        return(arr)                                                 

class MergeSort(object):
    arr = []
    def sort(self, arr, reverse = False, display = False):
        tmpArr=[0]*len(arr)
        self.arr = arr
        self.Mergesort(tmpArr, 0, len(arr)-1, reverse, display)
        return self.arr

    def Mergesort(self, tmpArr, left, right, reverse = False, display = False):
        if left < right:
            mid = (left+right)/2
            if display:
                print('Mergesort left to mid ', left, mid, right)
            self.Mergesort(tmpArr, left, mid, reverse, display)
            if display:
                print('Mergesort mid to right ', left, mid, right)
            self.Mergesort(tmpArr, mid+1, right, reverse, display)
            self.Merge(tmpArr, left, mid+1, right, reverse, display)

    def Merge(self, tmpArr, left, mid, right, reverse, display):
        left_start = left
        left_begin = left
        left_end = mid-1
        if display:
            print('Merge', left, mid, right)
        while(left<=left_end and mid<=right):
            if((not reverse and self.arr[left]<=self.arr[mid]) or (reverse and self.arr[left]>=self.arr[mid])):
                tmpArr[left_start] = self.arr[left]
                left_start+=1
                left+=1
            else:
                tmpArr[left_start]=self.arr[mid]
                left_start+=1
                mid+=1
        while(left<=left_end):
            tmpArr[left_start] = self.arr[left]
            left_start+=1
            left+=1
        while(mid<=right):
            tmpArr[left_start]=self.arr[mid]
            left_start+=1
            mid+=1
        for i in range(right - left_begin + 1):
            self.arr[right] = tmpArr[right]    
            right = right -1
        if display:
            print(' '.join([str(i) for i in self.arr]))

class QuickSort(object):
    arr = []
    def sort(self, arr, reverse = False, display = False):
        self.arr=arr
        self.quickSort(0, len(arr)-1, reverse, display)
        return self.arr

    def quickSort(self, low, high, reverse=False, display = False):
        if low < high:
            pivot = self.partition(low, high, reverse, display)
            if display:
                print('QuickSort', low, pivot-1)
            self.quickSort(low, pivot-1, reverse, display)
            if display:
                print('QuickSort', pivot, high)
            self.quickSort(pivot+1, high, reverse, display)
        
    def partition(self, low, high, reverse=False, display=False):
        left, right, pivot_item = (low, high, self.arr[low])
        if display:
            print('Partition left, right, pivot_item :: ', left, right, pivot_item)
        while(left < right):
            while((not reverse and self.arr[left]<=pivot_item) or (reverse and self.arr[left]>=pivot_item)):
                left+=1
            while((not reverse and self.arr[right]>pivot_item) or (reverse and self.arr[right]<pivot_item)):
                right-=1
            if left < right:
                self.arr[left], self.arr[right] = self.arr[right], self.arr[left]
        self.arr[low], self.arr[right] = self.arr[right], pivot_item
        if display:
            print(self.arr)
        return right
