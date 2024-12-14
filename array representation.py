import random
import time

# Sorting Algorithms with Visualization
def bubble_sort(arr, update):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                update(arr)
    return arr

def merge_sort(arr, update, start=0, end=None):
    if end is None:
        end = len(arr)
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(arr, update, start, mid)
        merge_sort(arr, update, mid, end)
        merge(arr, start, mid, end, update)
    return arr

def merge(arr, start, mid, end, update):
    left = arr[start:mid]
    right = arr[mid:end]
    i = j = 0
    for k in range(start, end):
        if j >= len(right) or (i < len(left) and left[i] < right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        update(arr)

def quick_sort(arr, update, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high, update)
        quick_sort(arr, update, low, pi - 1)
        quick_sort(arr, update, pi + 1, high)
    return arr

def partition(arr, low, high, update):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            update(arr)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    update(arr)
    return i + 1

# Visualization Helper
def visualize_sorting(sort_function, arr):
    def update_text(data):
        print(data)
        time.sleep(210
                   )  # Pause to visualize each step

    def run_sort():
        sort_function(arr, update_text)

    run_sort()

# Sorting Algorithm Selection
def main():
    n = int(input("Enter the number of elements to sort: "))
    arr = [random.randint(1, 100) for i in range(n)]
    print(f"Original Array: {arr}")

    print("Select a sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Merge Sort")
    print("3. Quick Sort")

    choice = int(input("Enter your choice (1/2/3): "))
    if choice == 1:
        print("Visualizing Bubble Sort...")
        visualize_sorting(bubble_sort, arr.copy())
    elif choice == 2:
        print("Visualizing Merge Sort...")
        visualize_sorting(merge_sort, arr.copy())
    elif choice == 3:
        print("Visualizing Quick Sort...")
        visualize_sorting(quick_sort, arr.copy())
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
