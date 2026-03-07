import tracemalloc
import sys

def example_1_basic_tracemalloc():
    """Example 1: Basic memory tracking"""
    print("\n" + "="*70)
    print("EXAMPLE 1: Basic Memory Tracking with tracemalloc")
    print("="*70)
    
    # Start tracing
    tracemalloc.start()
    
    # Allocate some memory
    small_list = [1, 2, 3, 4, 5]
    medium_list = list(range(100000))
    large_list = list(range(10000000))
    
    # Get memory snapshot
    current, peak = tracemalloc.get_traced_memory()
    
    print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
    print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
    
    tracemalloc.stop()
example_1_basic_tracemalloc()