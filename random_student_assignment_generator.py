import random
import csv

# Lists of sample first names and last names to generate random student names
first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah"]
last_names = ["Doe", "Smith", "Johnson", "Lee", "Brown", "Williams", "Davis", "Miller", "Wilson", "Moore"]

# Generate 100 unique student numbers starting from 1001
def generate_student_number(index):
    return 1001 + index

# Create a class to represent each student
class Student:
    def __init__(self, first_name, last_name, student_number):
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number
        self.reviews = []  # List to store the 3 assigned reviews

# Generate a list of 100 students
def generate_students(num_students=100):
    students = []
    for i in range(num_students):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        student_number = generate_student_number(i)
        students.append(Student(first_name, last_name, student_number))
    return students

# Assign 3 random peer reviews to each student
def assign_peer_reviews(students):
    student_numbers = [student.student_number for student in students]
    for student in students:
        available_numbers = [num for num in student_numbers if num != student.student_number]  # Exclude own student number
        student.reviews = random.sample(available_numbers, 3)  # Randomly select 3 peer assignments

# Write the peer review assignments to a CSV file
def generate_peer_review_csv(students, filename="peer_reviews.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['First Name', 'Last Name', 'Student Number', 'Review 1', 'Review 2', 'Review 3', 'Grade 1', 'Grade 2', 'Grade 3'])
        
        # Write each student's data and peer reviews
        for student in students:
            row = [student.first_name, student.last_name, student.student_number] + student.reviews + ['', '', '']
            writer.writerow(row)

# Main execution
if __name__ == "__main__":
    # Generate 100 random students
    students = generate_students(100)
    
    # Assign peer reviews to each student
    assign_peer_reviews(students)
    
    # Generate the CSV file with the peer reviews and empty grade columns
    generate_peer_review_csv(students)
    
    print("Peer review assignments saved to 'peer_reviews.csv'.")

#Arkia Ebrahimi 20235443