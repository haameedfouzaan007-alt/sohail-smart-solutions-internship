#include <iostream>
using namespace std;

int main() {
    int numbers[] = {10, 20, 30, 40, 50, 60};
    int size = 6;
    int target = 60;

    int low = 0;
    int high = size - 1;
    bool found = false;

    while (low <= high) {
        int mid = (low + high) / 2;

        if (numbers[mid] == target) {
            cout << "Target found at index " << mid << endl;
            found = true;
            break;
        }
        else if (numbers[mid] < target) {
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }

    if (!found) {
        cout << "Target not found in the array." << endl;
    }

    return 0;
}