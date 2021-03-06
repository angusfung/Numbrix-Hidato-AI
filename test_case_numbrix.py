#Solution
#3x3
'''
a0 
  3  2  9
  4  1  8
  5  6  7
'''

a0 = ([3, -1, 9],
        [-1, 1,-1],
        [5,-1,-1])
     
'''
a1
  9  2  3
  8  1  4
  7  6  5
'''

a1 = ([-1, -1, 3],
        [-1, 1, -1],
        [-1,6, -1])
        
'''
a2
  1  2  3
  6  5  4
  7  8  9
 12 11 10
'''

#Has minimum and maximum numbers defined
a2 = ([1,-1,-1],
        [-1,5,-1],
        [7,-1,9],
        [12,-1,-1])

'''
a3
  1  2  3
  6  5  4
  7  8  9
 12 11 10
'''

a3 = ([-1,-1,3],
        [-1,5,-1],
        [7,-1,9],
        [-1,11,-1])

#4x4
'''
a4 
  1  2  3  4
 14 13  6  5
 15 12  7  8
 16 11 10  9
'''

a4 = ([-1,2,-1,-1],
        [14, -1, 6, 5],
        [15, 12, -1, 8],
        [-1, -1, -1, -1])
        
'''
a5
  1  2 13 12
  4  3 14 11
  5 16 15 10
  6  7  8  9
'''  
   
a5 = ([1, 2, -1, 12],
       [4, -1, 14, -1],
       [-1 ,-1, 15, 10],
       [6, 7, -1, 9])

'''
a6
  4  3  2  1
  5  6  7  8
 12 11 10  9
 13 14 15 16
 '''
 
a6 = ([-1,-1,-1,1],
        [-1,-1,7,-1],
        [12,-1,-1,-1],
        [-1,-1,-1,16])

'''
a7
  4  3  2  1
  5  6  7  8
 12 11 10  9
 13 14 15 16
'''

a7 = ([-1,-1,-1,-1],
        [-1,-1,7,-1],
        [-1,-1,-1,-1],
        [-1,-1,15,-1])

#6x5 grid   
'''
a8
 29 28 25 24 23
 30 27 26 21 22
  5  4  1 20 19
  6  3  2 17 18
  7 10 11 16 15
  8  9 12 13 14
''' 

a8 = ([29,-1,25,-1,-1],
        [-1,-1,-1,-1,22],
        [-1,4,-1,20,-1],
        [6,-1,2,-1,18],
        [-1,-1,-1,16,-1],
        [-1,-1,-1,-1,-1])        

#6x6
'''
a9
 16 15 10  9  8  7
 17 14 11  4  5  6
 18 13 12  3  2  1
 19 24 25 26 33 34
 20 23 28 27 32 35
 21 22 29 30 31 36
'''

a9 = ([-1,15,-1,9,8,-1],
        [17,-1,-1,-1,-1,6],
        [-1,-1,12,-1,-1,1],
        [-1,-1,-1,-1,-1,34],    
        [20,-1,-1,27,-1,-1],
        [-1,22,-1,-1,-1,36])

#8x8 (50% vacancy)
'''        
a10 
  1  4  5 44 45 64 63 62
  2  3  6 43 46 57 58 61
  9  8  7 42 47 56 59 60
 10 19 20 41 48 55 54 53
 11 18 21 40 49 50 51 52
 12 17 22 39 36 35 34 33
 13 16 23 38 37 28 29 32
 14 15 24 25 26 27 30 31
'''
  
a10 =  ([1,-1,5,-1,45,-1,63,-1],
        [-1,3,-1,43,-1,-1,-1,61],
        [9,-1,7,42,47,-1,59,60],
        [10,-1,20,-1,48,55,-1,53],    
        [-1,-1,21,-1,-1,50,-1,-1],
        [12,-1,-1,-1,-1,35,-1,33],
        [13,-1,23,38,-1,28,-1,32],
        [-1,15,-1,-1,26,-1,30,-1])       

#10x10 (50% vacancy)
'''
a11 
 86 87 88 89 90 91 94 95 98 99
 85 84 83 82 81 92 93 96 97100
 76 77 78 79 80 69 68 67 66 65
 75 74 73 72 71 70 61 62 63 64
 46 47 48 49 50 51 60 59 58 57
 45 44 43 42 41 52 53 54 55 56
 24 25 26 27 40 39 38 37 36 35
 23 22 21 28 29 30 31 32 33 34
  2  3 20 19 18 17 16 15 14 13
  1  4  5  6  7  8  9 10 11 12
'''

a11 =([-1,-1,88,-1,90,91,-1,95,-1,99],
    [85,-1,83,-1,81,92,-1,96,-1,-1],
    [76,-1,-1,79,80,-1,68,-1,66,-1],
    [-1,74,73,-1,71,70,-1,62,-1,64],
    [46,-1,48,49,-1,51,60,-1,58,-1],
    [45,-1,43,-1,41,-1,53,54,-1,56],
    [-1,25,-1,27,-1,39,-1,37,-1,35],
    [23,-1,21,-1,29,-1,31,-1,33,-1],
    [ 2, 3,20,19,-1,17,-1,15,-1,13],
    [ 1, -1, 5, 6,-1,-1, 9,-1,11,-1])    