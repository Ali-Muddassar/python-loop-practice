"""
loop inside loop here i defined 2 loop
first is ---> for num in range(4): 3 tak chalega 
second is --->  for i in range(3): 2 tak chalega
i=0, j=0
i=0, j=1
i=0, j=2
i=1, j=0
i=1, j=1
i=1, j=2
i=2, j=0
i=2, j=1
i=2, j=2
i=3, j=0
i=3, j=1
i=3, j=2
check its working 
"""

for num in range(4):
    for i in range(3):
        print(f"i={num}, j={i}")
