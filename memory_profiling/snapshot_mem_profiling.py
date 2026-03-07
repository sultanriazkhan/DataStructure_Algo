import tracemalloc
import sys
def example_2_snapshot_analysis():
    """Example 2: Analyze where memory goes"""
    print("\n" + "="*70)
    print("EXAMPLE 2: Detailed Snapshot Analysis")
    print("="*70)
    
    tracemalloc.start()
    
    # Create different data structures
    list_data = [i for i in range(100000)]
    dict_data = {i: i**2 for i in range(100000)}
    string_data = "x" * 1000000
    
    # Take snapshot
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    
    print("\nTop 5 memory allocations:")
    for stat in top_stats[:5]:
        print(stat)
    
    tracemalloc.stop()
example_2_snapshot_analysis()
