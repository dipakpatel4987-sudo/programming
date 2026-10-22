#include <iostream>
using namespace std;


class Person {
protected:
    string name;
    int age;

public:
    void setPerson(string n, int a) {
        name = n;
        age = a;
    }

    void displayPerson() {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
    }
};


class Student : public Person {
private:
    int rollNo;

public:
    void setStudent(int r) {
        rollNo = r;
    }

    void displayStudent() {
        displayPerson();
        cout << "Roll Number: " << rollNo << endl;
    }
};


class Teacher : public Person {
private:
    string subject;

public:
    void setTeacher(string s) {
        subject = s;
    }

    void displayTeacher() {
        displayPerson();
        cout << "Subject: " << subject << endl;
    }
};

int main() {
    Student s;
    Teacher t;

    
    s.setPerson("Dipak", 20);
    s.setStudent(101);

    cout << "Student Details" << endl;
    s.displayStudent();

    cout << endl;

    
    t.setPerson("Ramesh", 40);
    t.setTeacher("Mathematics");

    cout << "Teacher Details" << endl;
    t.displayTeacher();

    return 0;
}
