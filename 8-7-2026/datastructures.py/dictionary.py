student_record={"name":"manaswini","marks":78}
student_record["marks"]=83
student_record["grade"]="B"
print("Student record:",student_record);

person_details={"id":101,"name":"rahul","department":"It","salary":250000}
print("person_name:",person_details["name"]);
person_details["city"]="vijaywada";
person_details["salary"]=6000000;
print(person_details);



person_details.pop("name");
print(person_details);


person_details.popitem();
print(person_details);


