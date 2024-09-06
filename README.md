# Classroom Organizer

## Overview

The Classroom Organizer project is a Python application designed to help manage classroom seating arrangements and organize students based on their favorite subjects. This tool includes functionality for generating student combinations for seating at tables and finding groups of students whose favorite subjects align with specific criteria.

## Features

- **Sort Students Alphabetically**: Retrieve a list of students sorted by their first names.
- **Retrieve Subject-Specific Students**: Get a list of students whose favorite subject matches a given subject.
- **Generate Seating Combinations**: Create all possible combinations of students for seating at tables.
- **Organize After-School Program**: Find combinations of students whose favorite subjects are Math and Science.

## Requirements

- Python 3.x
- `itertools` module (standard library, no additional installation required)
- A `roster.py` file containing student data in the format expected by the `ClassroomOrganizer` class.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/classroom-organizer.git
    ```

2. Navigate to the project directory:
    ```bash
    cd classroom-organizer
    ```

3. Ensure you have Python 3.x installed.

## Usage

1. **Define Student Roster**:
   Ensure you have a `roster.py` file with the following structure:
    ```python
    student_roster = [
        {'name': 'Alice', 'favorite_subject': 'Math'},
        {'name': 'Bob', 'favorite_subject': 'Science'},
        # Add more student records here
    ]
    ```

2. **Run the Script**:
    Execute the `script.py` file to see the output:
    ```bash
    python script.py
    ```

## Methods

### `ClassroomOrganizer`

- **`__init__()`**: Initializes the organizer and sorts the student names alphabetically.
- **`_sort_alphabetically(students)`**: Helper method to sort students by name.
- **`get_students_with_subject(subject)`**: Returns a list of students whose favorite subject matches the given subject.
- **`get_table_combinations()`**: Returns all possible combinations of 2 students for seating at tables.
- **`get_combinations_of_students_for_subjects(subjects, combination_size=4)`**: Retrieves and combines students whose favorite subjects match the provided list, and returns all possible combinations of the specified size.

## Example Output

### Possible Combinations of Students for Each Table
```
Possible combinations of students for each table:
('Alice', 'Bob')
('Alice', 'Charlie')
...
```

### Possible Combinations of 4 Students with Favorite Subjects Math and Science
```
Possible combinations of 4 students with favorite subjects Math and Science:
('Alice', 'Bob', 'Charlie', 'Diana')
...
```

## What I Learned

1. **Understanding Iterators**:
   - Implementing the iterator protocol in Python to create custom iterators and manage iteration over a list of student names.

2. **Using `itertools` for Combinations**:
   - How to use the `itertools` module to generate combinations and permutations, specifically to find all possible pairs and groups of students.

3. **Class Design and Methods**:
   - Designing a class with methods that manage different functionalities, such as sorting data, filtering based on criteria, and generating combinations.

4. **Debugging and Testing**:
   - Debugging common issues related to method arguments and ensuring that functions are correctly called with the required parameters.

5. **Documentation Best Practices**:
   - Writing clear and concise documentation to describe project functionality, usage instructions, and lessons learned, making the project accessible and understandable to others.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

