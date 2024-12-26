# Sorting-Visualization

# Sorting Algorithms Visualization

This Python project demonstrates and visualizes the functioning of various sorting algorithms. It uses matplotlib to provide an animated representation of the sorting process for better understanding.

## Features
- **Sorting Algorithms**: Includes Bubble Sort, Merge Sort, and Quick Sort.
- **Real-time Visualization**: Displays how the array is sorted step by step.
- **Interactive Input**: Allows users to choose the number of elements and the sorting algorithm.

## How It Works
1. The program generates a random list of integers based on user input.
2. The user selects a sorting algorithm:
   - **Bubble Sort**: Compares adjacent elements and swaps them if they are in the wrong order.
   - **Merge Sort**: Recursively divides the array into halves, sorts, and merges them.
   - **Quick Sort**: Selects a pivot, partitions the array, and recursively sorts the partitions.
3. The selected sorting algorithm sorts the list, while the visualization updates dynamically.

## How to Use
1. Run the script: `python script_name.py`.
2. Enter the number of elements to sort.
3. Choose a sorting algorithm:
   - Enter **1** for Bubble Sort.
   - Enter **2** for Merge Sort.
   - Enter **3** for Quick Sort.
4. Watch the sorting process animated on the screen.

## Requirements
- Python 3.x
- Matplotlib library (`pip install matplotlib`)

## Notes
- The animations might take some time, especially for a large number of elements or less efficient algorithms like Bubble Sort.
- The program is meant for educational purposes to visualize sorting algorithms and their behavior.
