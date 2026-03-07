import tracemalloc
import sys

def example_3_manual_profiling():
    """Example 3: Manual line-by-line profiling simulation"""
    print("\n" + "="*70)
    print("EXAMPLE 3: Manual Line-by-Line Memory Tracking")
    print("="*70)
    
    tracemalloc.start()
    
    # Track memory at each step
    print("\nStep-by-step memory tracking:")
    
    # Step 1
    tracemalloc.reset_peak()
    list1 = [i for i in range(100000)]
    current, peak = tracemalloc.get_traced_memory()
    print(f"After creating list1: {peak / 1024 / 1024:.2f} MB")
    
    # Step 2
    tracemalloc.reset_peak()
    list2 = [i**2 for i in range(100000)]
    current, peak = tracemalloc.get_traced_memory()
    print(f"After creating list2: {peak / 1024 / 1024:.2f} MB")
    
    # Step 3: Cleanup
    tracemalloc.reset_peak()
    del list1
    current, peak = tracemalloc.get_traced_memory()
    print(f"After deleting list1: {peak / 1024 / 1024:.2f} MB")
    print(f"Current memory usage after cleanup: {current / 1024 / 1024:.2f} MB")
    
    tracemalloc.stop()
example_3_manual_profiling()
