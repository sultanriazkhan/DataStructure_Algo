import tracemalloc
#for memory leak list must be outside the function to persist after the function call, simulating a memory leak
leaked_data=[]
def memory_leak_function():
    # this function simulates a memory leak by creating a large list and not releasing it[Just fot learning]
    for i in range(1000000):
        leaked_data.append(i)
    
tracemalloc.start()
memory_leak_function()
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 10**6} MB; Peak memory usage: {peak / 10**6} MB")
tracemalloc.stop()