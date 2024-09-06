
import itertools
from roster import student_roster

class ClassroomOrganizer:
    def __init__(self):
        # Store the sorted names
        self.sorted_names = self._sort_alphabetically(student_roster)
        # Initialize the index for iteration
        self.index = 0

    def _sort_alphabetically(self, students):
        # Sort the student names alphabetically
        names = [student_info['name'] for student_info in students]
        return sorted(names)

    def get_students_with_subject(self, subject):
        # Return students who have the given subject as their favorite
        selected_students = [
            (student['name'], subject) 
            for student in student_roster 
            if student.get('favorite_subject') == subject
        ]
        return selected_students

    # Iterator protocol: __iter__ and __next__
    def __iter__(self):
        # Return the iterator object (self in this case)
        return self

    def __next__(self):
        # Check if we have iterated through all the students
        if self.index >= len(self.sorted_names):
            raise StopIteration  # End of iteration
        # Get the next student's name
        student_name = self.sorted_names[self.index]
        # Increment the index for the next call
        self.index += 1
        return student_name

    # defining a method that will retrieve a final list of all tuple combinations of 2 students that can be seated at each table
    def get_table_combinations(self):
      return list(itertools.combinations(self.sorted_names, 2))
    
    def get_combinations_of_students_for_subjects(self, subjects, combination_size=4):
        # Retrieve students for each subject and combine them
        students = []
        for subject in subjects:
            students.extend(self.get_students_with_subject(subject))
          # Generate all possible combinations of the specified size
        return list(itertools.combinations(students, combination_size))
      

# Example usage of ClassroomOrganizer
classroom = ClassroomOrganizer()

# Using a for loop to iterate over the ClassroomOrganizer object
print("Roll Call:")
for student in classroom:
    print(student)

# Alternatively, using next() calls
print("\nUsing next() calls:")
classroom = iter(ClassroomOrganizer())  # Reset the iterator

try:
    while True:
        print(next(classroom))
except StopIteration:
    print("Roll call complete!")
