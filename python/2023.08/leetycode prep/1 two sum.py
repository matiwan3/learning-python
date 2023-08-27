class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_indices = {}  # Dictionary to store visited numbers and their indices
        
        for index, num in enumerate(nums):
            complement = target - num  # Find the number needed to achieve the target
            
            if complement in num_indices:
                return [num_indices[complement], index]
            
            num_indices[num] = index  # Store the current number and its index
        
        # If no solution is found
        return []

# 1. do metody przekazywane są array z liczbami oraz target liczbowy
# 2. stworzono dictionary na odwiedzone wczesniej liczby i ich indeksy
# 3. stworzenie petli ktora iteruje dla "index" i "num" po liscie nums przy uzyciu "enumarate" func (used to loop through nums array)
# 4. stworzenie zmiennej complement ktora znajduje numer potrzebny do osiagniecia celu. (target 9, lista 4,3,6,7,1,8 => complement = 9 - 4 == 5)
# 5. sprawdzenie warunku czy dany complement znajduje się w dictionary ze znalezionymi liczbami wczesniej i jesli tak to funkcja zwraca liste z dwoma wartosciami: indeksami wartosci ktore daja sumę dla targetu
# 6. pętla zapisuje w dla num_indicies[num] = index (dla kazdej liczby zapisywany jest jej index w  