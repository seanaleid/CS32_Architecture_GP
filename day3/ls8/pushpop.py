SP = 5
memory_stack = [0] * 10

registers = [0] * 10
register[7] = 5
reg1 = 12
reg2 = 23
reg3 = 0
reg7 = 5

# PUSH, 2
# step 1
register[7]-=1
SP-=1
# step 2
memory_stack[SP] = reg2

# POP, 3
# step 1
reg3 = memory_stack[SP]
# step 2
SP+=1

PC+=operatition_size