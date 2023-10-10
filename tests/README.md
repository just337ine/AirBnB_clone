# BaseModel Unit Testing 📚

This repository contains unit tests for the `BaseModel` class in the AirBnB_clone project. The `BaseModel` class is a foundational piece of the larger project and serves as the base class for all other classes.

## 🚀 Getting Started

To run the tests locally, you need Python3 installed. Clone the repository and navigate to the root directory.

### Prerequisites

- Python3

### Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ugwujustine/AirBnB_clone.git

2. Navigate to the repository:
   ```
   cd AirBnB_clone
   ```

3. Run the tests:
   ```
   python3 -m unittest tests/test_models/test_base_model.py
   ```

## 🔍 What's Tested?

- **Creation Test**: Validates instance creation and attribute presence.
- **String Representation**: Checks the `__str__` method's output.
- **Save Method**: Ensures the `updated_at` attribute updates correctly.
- **To Dictionary Method**: Validates instance's dictionary representation.
- **Instance Creation from Dictionary**: Tests instance creation from dictionary.
- **Datetime Format**: Validates datetime format in dictionary representation.


