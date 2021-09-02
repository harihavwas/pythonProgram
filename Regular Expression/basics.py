"""
x='[abc]'       --> Either a b or c
x='[^abc]'      --> Except abc
x='[a-z]'       --> a to z
x='[A-Z]'       --> A to Z
x='[a-zA-Z]'    --> Both lower and upper case
x='[0-9]'       --> Check Digits
x='[a-zA-Z0-9]' --> Special symbols
x='\s' --> Check space
x='\d' --> Check the digit
x='\D' --> Except Digit
x='\w' --> All words except special characters
x='\W' --> For special characters
"""

# Quantifiers
"""
x='a+' --> A including group
x='a*' --> Count including zero number of a 
x='a?' --> Count a as each including zero no of a
x='a{2}' --> 2 no of a position
x='a{2,3} --> Minimum 2 a and maximum 3 a
x='^a' --> Check starting with a
x='a$' --> Check ending with a
"""