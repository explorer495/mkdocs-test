# CSS and Format Experimentation - Heading 1

Some text here for the page intro.

## Heading 2

Some text here for a heading 2 section.

### Heading 3

Some more text here for a heading 3 subsection.

#### Heading 4

Maybe a heading 4 subsection.

##### Heading 5

Cater for heading 5 as well.

## Code blocks - H2

Adding a full code block of C++ to test colours and syntax high lighting.

```cpp
#include <iostream>  // Standard I/O library
#include <vector>    // For dynamic arrays
#include <string>    // For string manipulation
#include <map>       // For key-value pairs

// A simple namespace to organize code
namespace MyLibrary {

const double PI_VALUE = 3.1415926535; // A global constant

/**
 * @brief Represents a generic item with properties.
 * This is a multi-line comment to test comment colors.
 */
class GenericItem {
private:
    std::string itemName;
    int itemId;
    double itemPrice;
    bool isAvailable;

public:
    // Constructor with default values
    GenericItem(const std::string& name = "Default Item", int id = 0, double price = 0.0, bool available = true)
        : itemName(name), itemId(id), itemPrice(price), isAvailable(available) {}

    // Member function to display item details
    void displayDetails() const {
        std::cout << "Item Name: " << itemName << std::endl;
        std::cout << "Item ID: " << itemId << std::endl;
        std::cout << "Price: $" << itemPrice << std::endl;
        std::cout << "Available: " << (isAvailable ? "Yes" : "No") << std::endl;
    }

    // Getter for itemPrice
    double getPrice() const {
        return itemPrice;
    }

    // Setter for itemPrice (with a simple check)
    void setPrice(double newPrice) {
        if (newPrice >= 0.0) {
            this->itemPrice = newPrice;
        } else {
            std::cerr << "Warning: Price cannot be negative." << std::endl;
        }
    }
}; // Don't forget the semicolon after class definition!

// Template function to find the maximum of two values
template <typename T>
T findMax(T a, T b) {
    return (a > b) ? a : b; // Ternary operator test
}

} // end namespace MyLibrary

// Main function - entry point of the program
int main() {
    using namespace MyLibrary; // Use MyLibrary namespace

    // Create instances of GenericItem
    GenericItem item1("Laptop", 101, 1200.50, true);
    GenericItem* item2 = new GenericItem("Mouse", 202, 25.99, false); // Using 'new'

    // Display details using a loop
    std::vector<GenericItem> inventory;
    inventory.push_back(item1);
    inventory.push_back(*item2);

    std::cout << "--- Inventory Details ---" << std::endl;
    for (const auto& item : inventory) { // Range-based for loop
        item.displayDetails();
        std::cout << "-------------------------" << std::endl;
    }

    // Test the template function
    int maxInt = findMax(10, 20);
    double maxDouble = findMax(PI_VALUE, item2->getPrice()); // Accessing member via pointer

    std::cout << "Maximum integer: " << maxInt << std::endl;
    std::cout << "Maximum double: " << maxDouble << std::endl;

    // Exception handling test
    try {
        if (item1.getPrice() < 1.0) {
            throw "Price too low!"; // Throwing a string literal
        }
        item1.setPrice(1500.00); // Change price
    } catch (const char* msg) { // Catching a C-style string
        std::cerr << "Error: " << msg << std::endl;
    }

    // Clean up dynamic memory
    delete item2; // Using 'delete'
    item2 = nullptr; // Best practice to nullify pointer after delete

    // Return 0 for successful execution (integer literal)
    return 0;
}
```
