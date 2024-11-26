import json
from datetime import datetime

class Course:
    def __init__(self, code, name, teacher, email, credits, time, location):
        self.code = code
        self.name = name
        self.teacher = teacher
        self.email = email
        self.credits = credits
        self.time = time
        self.location = location
        self.notes = []
        self.deadlines = []

    def add_notes(self, note):
        self.notes.append(note)

    def add_deadline(self, description, due_date):
        self.deadlines.append({"description": description, "due_date": due_date})
        self.deadlines.sort(key=lambda x: datetime.strptime(x["due_date"], "%Y-%m-%d"))

    def display_info(self):
        print(f"Course Code: {self.code}")
        print(f"Name: {self.name}")
        print(f"Teacher: {self.teacher}")
        print(f"Email: {self.email}")
        print(f"Credits: {self.credits}")
        print(f"Time: {self.time}")
        print(f"Location: {self.location}")
        print(f"Notes: {', '.join(self.notes) if self.notes else 'No notes'}")
        if self.deadlines:
            print("Deadlines:")
            for deadline in self.deadlines:
                print(f"  - {deadline['description']} by {deadline['due_date']}")
        else:
            print("No deadlines.")

    def most_urgent_deadline(self):
        return self.deadlines[0] if self.deadlines else None


def save_courses_to_file(courses, filename="courses.json"):
    with open(filename, "w") as file:
        json.dump([course.__dict__ for course in courses], file)


def load_courses_from_file(filename="courses.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return [Course(**course) for course in data]
    except FileNotFoundError:
        return []


def main():
    courses = load_courses_from_file()

    while True:
        print("\nMenu:")
        print("1. Add Course")
        print("2. Modify Course")
        print("3. View Course Information")
        print("4. Add Notes to a Course")
        print("5. Add Deadlines to a Course")
        print("6. Show Most Urgent Deadline")
        print("7. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            code = input("Course Code: ")
            name = input("Name: ")
            teacher = input("Teacher: ")
            email = input("Email: ")
            credits = int(input("Credits: "))
            time = input("Lecture Time: ")
            location = input("Location: ")
            courses.append(Course(code, name, teacher, email, credits, time, location))

        elif choice == "2":
            code = input("Enter the course code to modify: ")
            course = next((c for c in courses if c.code == code), None)
            if course:
                course.name = input("New Name (or press Enter to keep): ") or course.name
                course.teacher = input("New Teacher (or press Enter to keep): ") or course.teacher
                course.email = input("New Email (or press Enter to keep): ") or course.email
                course.credits = int(input("New Credits (or press Enter to keep): ") or course.credits)
                course.time = input("New Lecture Time (or press Enter to keep): ") or course.time
                course.location = input("New Location (or press Enter to keep): ") or course.location
            else:
                print("Course not found!")

        elif choice == "3":
            code = input("Enter the course code to view: ")
            course = next((c for c in courses if c.code == code), None)
            if course:
                course.display_info()
            else:
                print("Course not found!")

        elif choice == "4":
            code = input("Enter the course code to add notes: ")
            course = next((c for c in courses if c.code == code), None)
            if course:
                note = input("Enter your note: ")
                course.add_notes(note)
            else:
                print("Course not found!")

        elif choice == "5":
            code = input("Enter the course code to add deadlines: ")
            course = next((c for c in courses if c.code == code), None)
            if course:
                description = input("Enter deadline description: ")
                due_date = input("Enter deadline date (YYYY-MM-DD): ")
                course.add_deadline(description, due_date)
            else:
                print("Course not found!")

        elif choice == "6":
            urgent_deadline = None
            for course in courses:
                deadline = course.most_urgent_deadline()
                if deadline:
                    if not urgent_deadline or datetime.strptime(deadline["due_date"], "%Y-%m-%d") < datetime.strptime(
                        urgent_deadline["due_date"], "%Y-%m-%d"
                    ):
                        urgent_deadline = deadline
            if urgent_deadline:
                print(f"Most Urgent Deadline: {urgent_deadline['description']} by {urgent_deadline['due_date']}")
            else:
                print("No deadlines found!")

        elif choice == "7":
            save_courses_to_file(courses)
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
