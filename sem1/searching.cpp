#include <iostream>
#include <vector>
#include <algorithm> // Included for std::sort

// Linear Search Function
// Works on any array. Scans from index 0 to n-1.
int linearSearch(const std::vector<int>& arr, int target) {
    int n = arr.size();
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            return i; // Target found! Return its index position.
        }
    }
    return -1; // Scanned the entire list and found nothing.
}

// Binary Search Function
// REQUIRES the array to be sorted first.
int binarySearch(const std::vector<int>& arr, int target) {
    int low = 0;
    int high = arr.size() - 1;

    while (low <= high) {
        // Calculate the middle index of the current boundaries
        int mid = low + (high - low) / 2;

        if (arr[mid] == target) {
            return mid; // Target found at the middle index!
        }
        else if (arr[mid] < target) {
            // Target is in the right half, move the lower wall up
            low = mid + 1;
        }
        else {
            // Target is in the left half, move the upper wall down
            high = mid - 1;
        }
    }
    return -1; // Target does not exist in the vector.
}

int main() {
    // 1. Linear Search Sample (Unsorted data)
    std::vector<int> unsortedData = {64, 25, 12, 22, 11};
    int target1 = 22;
    
    int result1 = linearSearch(unsortedData, target1);
    std::cout << "Linear Search: Found " << target1 << " at index " << result1 << "\n";

    // 2. Binary Search Sample (Data MUST be sorted)
    std::vector<int> sortedData = {11, 12, 22, 25, 64};
    int target2 = 25;
    
    int result2 = binarySearch(sortedData, target2);
    std::cout << "Binary Search: Found " << target2 << " at index " << result2 << "\n";

    return 0;
}
