#include <iostream>
#include <cstdlib>
#include <string>

struct Student {
  std::string studentId;
  std::string name;
  int age;
};

struct StudentNode {
  struct StudentNode *next;
  Student student;
};

static StudentNode *s_listHead = NULL;

void addStudentToSystem(const Student *student) {
  StudentNode *nodeToAdd = (StudentNode*)malloc(sizeof(StudentNode));
  // assert(nodeToAdd != NULL);

  nodeToAdd->student = *student;

  // Add entry to the front of the list
  nodeToAdd->next = s_listHead;
  s_listHead = nodeToAdd;
}

// Code to populate the list with fake student data

static void generateFakeStudent(Student *student) {
  student->studentId = "S" + std::to_string(rand() % 1000);
  student->name = "StudentName" + std::to_string(rand() % 100);
  student->age = 18 + rand() % 5; // Random age between 18 and 22
}

static void generateFakeStudentList(void) {
  for (int i = 0; i < 10; i++) {
    Student student;
    generateFakeStudent(&student);
    addStudentToSystem(&student);
  }
}

// Function to display student information
static void displayStudentInfo(const StudentNode *node) {
  std::cout << "Student ID: " << node->student.studentId << std::endl;
  std::cout << "Name: " << node->student.name << std::endl;
  std::cout << "Age: " << node->student.age << std::endl;
  std::cout << "------------------------" << std::endl;
}

int main(void) {
  generateFakeStudentList();

  // Displaying student information
  StudentNode *currentNode = s_listHead;
  while (currentNode != NULL) {
    displayStudentInfo(currentNode);
    currentNode = currentNode->next;
  }

  // Let's just spin loop so we can break at any point and dump the list
  while (1) { }
  return 0;
}
