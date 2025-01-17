#284. Peeking Iterator
"""
Time Complexity : O(1)
Space Complexity : O(1)
"""
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.temp = None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.temp == None:
            self.temp = self.it.next()
            return self.temp
        
        elif self.temp != None:
            return self.temp        

    def next(self):
        """
        :rtype: int
        """
        if self.temp != None:
            val = self.temp
            self.temp = None
            return val
        
        elif self.temp == None:
            return self.it.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.temp is not None:
            return True
        
        return self.it.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
