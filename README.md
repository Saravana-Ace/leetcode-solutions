# LeetCode Solutions 🚀

A comprehensive collection of my LeetCode problem solutions, featuring automated submission tracking and organized problem categorization.

## 📊 Repository Stats

- **Total Solutions**: 90+ problems solved
- **Languages**: Python
- **Topics Covered**: Arrays, Strings, Trees, Graphs, Dynamic Programming, Binary Search, Sliding Window, and more
- **Automated Tracking**: Real-time solution updates via GitHub automation

## 🗂️ Problem Categories

### Arrays & Two Pointers
- [Two Sum](two_sum.py) - Hash map approach for O(n) solution
- [3Sum](3_sum.py) - Three pointer technique with duplicate handling
- [Two Sum II](two_sum_two.py) - Sorted array optimization
- [Container With Most Water](max_subarray.py) - Kadane's algorithm implementation
- [Product of Array Except Self](Product%20of%20Array%20Except%20Self.py) - Prefix/suffix product arrays

### Binary Search
- [Binary Search](binary_search.py) - Classic implementation
- [Find Minimum in Rotated Sorted Array](find_min_in_rotated_sorted_array.py) - Modified binary search
- [Search in Rotated Sorted Array](search_in_rotated_sorted_array.py) - Handling rotation pivot
- [First Bad Version](first_bad_version.py) - Binary search on versions

### Trees & Binary Trees
- [Maximum Depth of Binary Tree](max_depth_of_binary_tree.py) - DFS and BFS approaches
- [Invert Binary Tree](invert_binary_tree.py) - Tree manipulation
- [Balanced Binary Tree](balanced_binary_tree.py) - Height calculation with early termination
- [Lowest Common Ancestor](lowest_common_anc.py) - DFS with parent tracking
- [Level Order Traversal](level_order_traversal.py) - BFS implementation

### Linked Lists
- [Merge Two Sorted Lists](merge_sorted_lists2.py) - Multiple solution approaches
- [Remove Nth Node From End](removenth_node_from_end_of_list.py) - Two-pointer technique
- [Reverse Linked List](reverse_linked_list.py) - Iterative pointer manipulation
- [Linked List Cycle](linked_list_cycle2.py) - Floyd's algorithm and value modification

### String Manipulation & Sliding Window
- [Longest Substring Without Repeating Characters](longest_substring_wo_repeating_chars.py) - Multiple sliding window implementations
- [Valid Anagram](valid_anagram.py) - Character frequency comparison
- [Group Anagrams](group_anagrams.py) - Hash map with sorted keys
- [Minimum Window Substring](minimum_window_substring.py) - Advanced sliding window with Counter
- [Permutation in String](permutation_in_string.py) - Character frequency matching

### Dynamic Programming
- [Coin Change](coin_change.py) - BFS approach for optimal solution
- [Maximum Subarray](max_subarray.py) - Kadane's algorithm variations
- [Palindromic Substrings](palindromic_substrings.py) - Center expansion technique

### Graph Algorithms
- [Clone Graph](clone_graph.py) - BFS with node mapping
- [Course Schedule](course_schedule.py) - Cycle detection in directed graph
- [Flood Fill](flood_fill.py) - BFS/DFS for connected components
- [01 Matrix](01_matrix.py) - Multi-source BFS

### Heaps & Priority Queues
- [K Closest Points to Origin](k_closest_points.py) - Min heap implementation
- [Kth Largest Element](k_closest_quick_select.py) - Quick select algorithm
- [Sliding Window Maximum](sliding_window_maximum.py) - Monotonic deque

### Advanced Algorithms
- [Median of Two Sorted Arrays](median_of_two_sorted_arrays.py) - Binary search on smaller array
- [Valid Sudoku](Valid%20Sudoku.py) - Hash sets for validation
- [Implement Trie](implement_trie.py) - Prefix tree data structure

## 🤖 Automated Solution Tracking

This repository features an automated system that tracks my LeetCode submissions and updates the repository in real-time.

### Features:
- **Automatic Code Retrieval**: Fetches accepted solutions from LeetCode
- **Real-time Updates**: Monitors for new submissions every 10 seconds
- **Git Integration**: Automatically commits and pushes new solutions
- **Session Management**: Secure authentication handling

### Setup Files:
- [`get_submission_code.py`](Automated_Push/get_submission_code.py) - Main automation script
- [`queries.py`](Automated_Push/queries.py) - GraphQL queries for LeetCode API
- [`setup.py`](Automated_Push/setup.py) - Configuration setup

## 🛠️ Technical Highlights

### Algorithm Patterns
- **Two Pointers**: Efficient array traversal techniques
- **Sliding Window**: Variable and fixed-size window optimizations
- **Binary Search**: Multiple variations and edge case handling
- **DFS/BFS**: Tree and graph traversal strategies
- **Dynamic Programming**: Bottom-up and top-down approaches

### Data Structures Used
- Hash Maps/Sets for O(1) lookups
- Stacks and Queues for LIFO/FIFO operations
- Heaps for priority-based operations
- Tries for prefix operations
- Deques for sliding window maximum

### Code Quality Features
- Multiple solution approaches for comparison
- Detailed comments explaining algorithm logic
- Time and space complexity considerations
- Edge case handling

## 📈 Problem Difficulty Distribution

- **Easy**: ~40% (Foundational concepts and basic algorithms)
- **Medium**: ~55% (Complex logic and multiple data structures)
- **Hard**: ~5% (Advanced algorithms and optimization)

## 🎯 Key Learnings

1. **Pattern Recognition**: Identifying common problem patterns speeds up solution development
2. **Trade-offs**: Understanding when to optimize for time vs. space complexity
3. **Multiple Approaches**: Many problems have several valid solutions with different trade-offs
4. **Edge Cases**: Comprehensive testing includes boundary conditions and special cases

## 🔧 Setup & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/leetcode-solutions.git
   ```

2. For automated tracking setup:
   ```bash
   cd Automated_Push
   pip install -r requirements.txt
   python setup.py
   ```

3. Run individual solutions:
   ```bash
   python solution_name.py
   ```

## 📚 Resources

- [LeetCode Platform](https://leetcode.com/)
- [NeetCode Roadmap](https://neetcode.io/) - Structured learning path
- [Algorithm Patterns](https://github.com/SeanPrashad/leetcode-patterns) - Common patterns guide

## 🤝 Contributing

Feel free to:
- Suggest optimizations for existing solutions
- Add alternative approaches
- Report any issues with the automation system
- Share insights on problem-solving strategies

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Happy Coding!** 🎉

*This repository is continuously updated with new solutions as I progress through LeetCode challenges.*