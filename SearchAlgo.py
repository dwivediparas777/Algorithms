class UnOrderedLinearSearch(object):
    def search(self, arr, element, display = False):
        for i in range(len(arr)):
            if display:
                print(0, i, len(arr)-1)
            if element == arr[i]:
                return (True, i)
        return (False, -999)

class OrderedLinearSearch(object):
    def search(self, arr, element, display = False):
        for i in range(len(arr)):
            if display:
                print(0, i, len(arr)-1)
            if element == arr[i]:
                return (True, i)
            elif element < arr[i]:
                return (False, -999)
        return (False, -999)

class BinarySearch(object):
    def search(self, arr, element, display = False):
        low = 0
        high = len(arr)-1
        while(low <= high):
            mid = (low + high)/2
            if display:
                print(low, mid, high)
            if arr[mid] == element:
                return(True, mid)
            elif arr[mid] < element:
                low = mid + 1
            else:
                high = mid - 1
        return(False, -999)

class InterpolationSearch(object):
    def search(self, arr, element, display = False):
        low = 0
        high = len(arr)-1
        m_tmp, l_tmp, h_tmp = (0,0,0)
        while(low <= high):
            mid = low + (((element - arr[low]) * (high - low)) / (arr[high] - arr[low]))
            if display:
                print(low, mid, high)
            if arr[mid] == element:
                return(True, mid)
            elif arr[mid] < element:
                low = mid + 1
            else:
                high = mid - 1
            if m_tmp == mid and l_tmp == low and h_tmp == high:
                break
            else:
                m_tmp, l_tmp, h_tmp = (mid, low, high)
        return(False, -999)
