# AirBnB Clone 🏡

This repository contains the implementation of the AirBnB clone project, including test scripts located in the `Demos` directory.

## 🎉 Demos Directory 🎉

The `Demos` folder contains test scripts that ensure the functionality of different modules of the project:

## 📂 File Structure:

AirBnB_clone/
│
└── Demos/
│
├── Task-3-test.py - 🚀 BaseModel Test for Task 3
├── Task-4-test.py - 🌌 Create BaseModel from Dictionary for Task 4
└── Task-5-test.py - 🪐 Store First Object for Task 5




## 🎯 Descriptions:

### Task-3-test.py 🚀
This script tests the BaseModel class which defines all common attributes/methods for other classes. It ensures that:

- The BaseModel has the correct attributes such as `id`, `created_at`, and `updated_at`.
- The `__str__` method correctly prints the BaseModel in the format `[<class name>] (<self.id>) <self.__dict__>`.
- The `save` method updates the `updated_at` attribute.
- The `to_dict` method returns the dictionary representation of the BaseModel.
- **How to Run**: 
        ```bash
        ./Task-3-test.py
        ```


### Task 4: Create BaseModel from Dictionary 🌌

This script tests the recreation of a BaseModel from another one using its dictionary representation. The key methods involved here are `to_dict()` and the `__init__` method that accepts `*args` and `**kwargs`.
- **How to Run**: 
        ```
        ./Task-4-test.py
        ```

### Task 5: Store First Object 🪐

This script tests the persistence of the BaseModel objects. It checks the serialization of the objects into a JSON file and the subsequent deserialization back into BaseModel objects. The primary class handling this is the `FileStorage` class which manages the JSON file serialization and deserialization.
- **How to Run**: 
        ```
        ./Task-5-test.py
        ```


## 🛠 Usage:

To execute any script, navigate to the `Demos` directory and run the corresponding task. For example:

```
cd Demos/
./Task-3-test.py
