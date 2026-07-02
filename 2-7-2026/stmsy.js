// Array to store student names
let students = [];

// Function to add a student
function addStudent() {

    let name = document.getElementById("studentName").value;

    if (name === "") {
        alert("Please enter a student name");
        return;
    }

    // Add name to array
    students.push(name);

    // Display updated list
    displayStudents();

    // Clear input box
    document.getElementById("studentName").value = "";
}

// Function to display students
function displayStudents() {

    let output = "";

    for (let i = 0; i < students.length; i++) {

        output += "<li>" +
                  students[i] +
                  " <button onclick='deleteStudent(" + i + ")'>Delete</button>" +
                  "</li>";
    }

    document.getElementById("studentList").innerHTML = output;
}

// Function to delete a student
function deleteStudent(index) {

    // Remove one student from the array
    students.splice(index, 1);

    // Refresh the list
    displayStudents();
}