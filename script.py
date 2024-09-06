import itertools
from roster import student_roster
from classroom_organizer import ClassroomOrganizer

# Example of using student_iterable (optional, for testing)
student_iterable = iter(student_roster)
print(next(student_iterable))
print(next(student_iterable))
print(next(student_iterable))
print(next(student_iterable))
print(next(student_iterable))
print(next(student_iterable))
print(next(student_iterable))
print(next(student_iterable))
print(next(student_iterable))
print(next(student_iterable))

def main():
    # Create an instance of ClassroomOrganizer
    classroom = ClassroomOrganizer()
    
    # Get the table combinations
    combinations = classroom.get_table_combinations()
    
    # Define subjects for the afterschool program
    subjects = ['Math', 'Science']
    
    # Get 4-student combinations for the specified subjects
    subject_combinations = classroom.get_combinations_of_students_for_subjects(subjects)

    # Print the combinations of all students for each table
    print("Possible combinations of students for each table:")
    for combo in combinations:
        print(combo)

    # Print the combinations of 4 students whose favorite subjects are Math and Science
    print("Possible combinations of 4 students with favorite subjects Math and Science:")
    for combo in subject_combinations:
        print(combo)

if __name__ == "__main__":
    main()
