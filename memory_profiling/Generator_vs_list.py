# ============================================================================
# EXAMPLE 6: Generator vs List Memory Comparison
# ============================================================================

import tracemalloc

import sys

def example_6_generators_vs_lists():
    """Example 6: Memory efficiency of generators"""
    print("\n" + "="*70)
    print("EXAMPLE 6: Generators vs Lists Memory Comparison")
    print("="*70)
    
    # Test with lists
    print("\nUsing LIST (stores everything in memory):")
    tracemalloc.start()
    
    list_data = [i for i in range(1000000)]
    current, peak = tracemalloc.get_traced_memory()
    list_memory = peak / 1024 / 1024
    print(f"Memory used: {list_memory:.2f} MB")
    print(f"Size: {len(list_data)}")
    
    tracemalloc.stop()
    
    # Test with generators
    print("\nUsing GENERATOR (computes on-the-fly):")
    tracemalloc.start()
    
    gen_data = (i for i in range(1000000))
    current, peak = tracemalloc.get_traced_memory()
    gen_memory = peak / 1024 / 1024
    print(f"Memory used: {gen_memory:.2f} MB")
    print(f"Size: Can't len() a generator!")
    
    # Consuming generator still uses memory
    sum_gen = sum(i for i in range(1000000))
    current, peak = tracemalloc.get_traced_memory()
    gen_consumed = peak / 1024 / 1024
    print(f"Memory after consuming: {gen_consumed:.2f} MB")
    
    tracemalloc.stop()
    
    print(f"\nSavings with generator: {list_memory - gen_memory:.2f} MB")
example_6_generators_vs_lists()