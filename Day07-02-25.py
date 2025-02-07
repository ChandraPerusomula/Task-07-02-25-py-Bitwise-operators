#Bitwise AND Operator:-
#Python Bitwise AND (&) operator takes two equal-length bit patterns as parameters. The two-bit integers are compared. If the bits in the compared positions of the bit patterns are 1, then the resulting bit is 1. If not, it is 0.


# 1. Bitwise AND  &     when both bits are 1 the result is 1 otherwise result is O    
# 2. Bitwise OR   |     when both bits are 0 the results is 0 otherwise result is 1
# 3. Bitwise NOT  ~	    works with a single value and returns its one’s complement. This means it toggles all bits in the value, transforming 0 bits to 1 and 1 bits to 0, resulting in the one’s complement of the binary number.
# 4. Bitwise XOR  ^      when both bits are 0 the results is 0 otherwise result is 1
# 5. Bitwise right shift  >>  Shifts the bits of the number to the right and fills 0 on voids left( fills 1 in the case of a negative number) as a result. Similar effect as of dividing the number with some power of two.
# 6. Bitwise left shift   <<  Shifts the bits of the number to the left and fills 0 on voids right as a result. Similar effect as of multiplying the number with some power of two.


# Print bitwise AND operation
   
Solo=86181
Leveling=29071

print('Solo & Leveling = ', Solo & Leveling)
print('Solo | Leveling = ', Solo | Leveling)
print('~Leveling =',~Leveling)
print('Solo ^ Leveling = ', Solo ^ Leveling)
print('Solo >> Leveling = ', Solo >> Leveling)
print('Solo << 3 = ', Solo << 3)
print('Leveling << 4 = ',Leveling << 4)



