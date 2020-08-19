```Python

True    # 1
False   # 0

"""
(boolean) ||
A         B         A OR B
False     False     False
False     True      True
True      False     True
True      True      True

(bitwise) |
A      B     A OR B
0      0     0   
0      1     1
1      0     1
1      1     1

(bitwise) ^
A      B     A XOR B
0      0     0   
0      1     1
1      0     1
1      1     0

(bitwise) &
A      B     A AND B
0      0     0   
0      1     0
1      0     0
1      1     1


A       NOT A
0       1
1       0

    10110
  & 10011
----------
    10010

Shifting --> moving the bits left or right
    BIT SHIFT RIGHT --> kind of like dividing by 2^n
        14   >> 1 == 7
        1110 >> 1 == 0111

        14   >> 2 == 3
        1110 >> 2 == 0011

        14   >> 3 == 1
        1110 >> 3 == 0001


    BIT SHIFT LEFT --> kind of like multiplying by 2^n
        14        << 1 == 28
        0000 1110 << 1 == 0001 1100 (4 + 8 + 16)

        14        << 2 == 56
        0000 1110 << 2 == 0011 1000 (8 + 16 + 32)

        14        << 3 == 112
        0000 1110 << 3 == 0111 0000 (16 + 32 + 64)

"""

```