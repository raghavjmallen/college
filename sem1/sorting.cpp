#include <iostream>
#include <vector>
#include <algorithm>

// Selection Sort Function
void selectionSort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        std::swap(arr[i], arr[min_idx]);
    }
}

// Optimized Bubble Sort Function
void bubbleSortOptimized(std::vector<int>& arr) {
    int n = arr.size();
    bool swapped;
    for (int i = 0; i < n - 1; i++) {
        swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) {
            break;
        }
    }
}

// Insertion Sort Function using Vectors
void insertionSort(std::vector<int>& arr) {
    int n = arr.size();
    // Start from index 1 because a single element is already "sorted"
    for (int i = 1; i < n; i++) {
        int key = arr[i]; // Pick up the element we want to insert
        int j = i - 1;    // Set up the pointer to look at elements to its left

        // Keep shifting elements to the right as long as they are greater than the key
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j]; // Copy the larger element one slot over
            j = j - 1;           // Move the pointer one step to the left
        }
        
        // Drop the key into its correct, sorted position
        arr[j + 1] = key;
    }
}

// Helper function to print the vector
void printArray(const std::vector<int>& arr) {
    for (int val : arr) {
        std::cout << val << " ";
    }
    std::cout << "\n";
}

int main() {
    // Creating matching vectors for testing
    std::vector<int> data1 = {64, 25, 12, 22, 11};
    std::vector<int> data2 = {64, 25, 12, 22, 11};
    std::vector<int> data3 = {64, 25, 12, 22, 11};

    selectionSort(data1);
    std::cout << "Selection Sorted: ";
    printArray(data1);

    bubbleSortOptimized(data2);
    std::cout << "Bubble Sorted:    ";
    printArray(data2);

    insertionSort(data3);
    std::cout << "Insertion Sorted: ";
    printArray(data3);

    return 0;
}
