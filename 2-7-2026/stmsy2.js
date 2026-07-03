// Student Class
class Student {
    constructor(id, name, marks) {
        this.id = id;
        this.name = name;
        this.marks = marks;
    }

    // Grade Calculation
    getGrade() {
        if (this.marks >= 90) {
            return "Grade A";
        } else if (this.marks >= 75) {
            return "Grade B";
        } else if (this.marks >= 60) {
            return "Grade C";
        } else {
            return "Fail";
        }
    }
}

// Array to Store Students
let students = [];

// Add Student Records
students.push(new Student(101, "Rahul", 95));
students.push(new Student(102, "Priya", 82));
students.push(new Student(103, "Kiran", 67));
students.push(new Student(104, "Suresh", 45));
students.push(new Student(105, "Anitha", 91));

// Display Student Report
console.log("----------- STUDENT REPORT -----------");

students.forEach(student => {
    console.log(
        "ID:", student.id,
        "| Name:", student.name,
        "| Marks:", student.marks,
        "| Grade:", student.getGrade()
    );
});

// Find Topper
let topper = students.reduce((a, b) => {
    return a.marks > b.marks ? a : b;
});

console.log("\nTopper:", topper.name + " (" + topper.marks + ")");

// Display Passed Students
console.log("\nPassed Students:");
students
    .filter(student => student.marks >= 60)
    .forEach(student => {
        console.log(student.name);
    });

// Display Failed Students
console.log("\nFailed Students:");
students
    .filter(student => student.marks < 60)
    .forEach(student => {
        console.log(student.name);
    });

// Calculate Average Marks
let totalMarks = students.reduce((sum, student) => {
    return sum + student.marks;
}, 0);

let average = totalMarks / students.length;

console.log("\nAverage Marks:", average);

// Count Passed Students
let totalPassed = students.filter(student => student.marks >= 60).length;

console.log("Total Passed:", totalPassed);

// Count Failed Students
let totalFailed = students.filter(student => student.marks < 60).length;

console.log("Total Failed:", totalFailed);

// Search Student by ID
let searchID = 103;

let studentByID = students.find(student => student.id === searchID);

console.log("\nSearch by Student ID:");
console.log(studentByID);

// Search Student by Name
let searchName = "Priya";

let studentByName = students.find(student => student.name === searchName);

console.log("\nSearch by Student Name:");
console.log(studentByName);

// Sort Students by Marks (Descending)
students.sort((a, b) => {
    return b.marks - a.marks;
});

console.log("\nStudents Sorted by Marks (Descending):");

students.forEach(student => {
    console.log(student.name + " - " + student.marks);
});

// Display Top 3 Students
console.log("\nTop 3 Students:");

students.slice(0, 3).forEach(student => {
    console.log(student.name + " - " + student.marks);
});