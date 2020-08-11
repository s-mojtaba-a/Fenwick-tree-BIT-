# The idea comes from the fact that we can express each natural 
# number as sum of some differente multiples of 2

class fenwick:
    def __init__(self,n):
        self.array=[0 for _ in range(n+1)]
        self.length=n

    def sum(self,i):  # gives sum of elements from index 1 to index i
        sum = 0
        while i>0 :
            sum = sum + self.array[i]
            i-=i & (-i) # computing the next index to be added to sum
        return sum


    def modify(self,a,i):
        ''' i = the index to be modified
        
            a = the value to be add to the index i  
        '''
        while i <= self.length :
            self.array[i]+=a
            i=i+(i&(-i))  # computing the next index to be modified
        

    def sumation(self,i,j):
        ''' gives sum of elements from index i to index j '''

        return(self.sum(j)-self.sum(i-1))


if __name__ == '__main__':  # just for a test :)
    my_fen=fenwick(10)
    my_fen.modify(7,9)
    my_fen.modify(2,1)
    my_fen.modify(-3,5)
    my_fen.modify(1,2)
    my_fen.modify(-2,6)
    my_fen.modify(13,3)
    my_fen.modify(8,4)
    print(my_fen.array)
    print(my_fen.sumation(1,9))

