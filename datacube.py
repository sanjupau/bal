import csv

def main():
    outdata = open("data_cube_sample.csv", "w")
    arr = []
    a = int(input("Enter the size of the semester dimensions: "))
    b = int(input("Enter the size of the student dimensions: "))
    c = int(input("Enter the size of the attribute dimensions: "))
    column_val = ["S.No", "Age", "Sleeping habit"]
    for i in range(a):
        temp1 = []
        for j in range(b):
            temp2 = []
            for k in range(c):
                print(f"Enter the {column_val[k]} of student: {j+1} in sem: {i+1}")
                print(f"location {i} {j} {k}")
                temp2.append(int(input()))
            temp1.append(temp2)
        arr.append(temp1)
    print("\nvalue extractions from data cube ****************")
    entered_S_No = int(input("Enter the student Serial Number: "))
    entered_semester = int(input("Enter the semester: "))
    print("Enter the attribute you want to fetch")
    print("1. S.No\n2. Age\n3. Sleeping habit")
    choosen_attribute = int(input())
    outdata.write("required attribute\n")
    if choosen_attribute < 1 or choosen_attribute > 3:
        print("Enter a valid attribute")
    else:
        print("\n")
        print(arr[entered_semester-1][entered_S_No-1][choosen_attribute-1])
        outdata.write(str(arr[entered_semester-1][entered_S_No-1][choosen_attribute-1]) + "\n")
    outdata.close()

if __name__ == "__main__":
    main()






output:
Enter the size of the semester dimensions: 2
Enter the size of the student dimensions: 2
Enter the size of the attribute dimensions: 3
Enter the S.No of student: 1 in sem: 1
location 0 0 0
1
Enter the Age of student: 1 in sem: 1
location 0 0 1
20
Enter the Sleeping habit of student: 1 in sem: 1
location 0 0 2
8
Enter the S.No of student: 2 in sem: 1
location 0 1 0
2
Enter the Age of student: 2 in sem: 1
location 0 1 1
19
Enter the Sleeping habit of student: 2 in sem: 1
location 0 1 2
6
Enter the S.No of student: 1 in sem: 2
location 1 0 0
1
Enter the Age of student: 1 in sem: 2
location 1 0 1
21
Enter the Sleeping habit of student: 1 in sem: 2
location 1 0 2
7
Enter the S.No of student: 2 in sem: 2
location 1 1 0
2
Enter the Age of student: 2 in sem: 2
location 1 1 1
20
Enter the Sleeping habit of student: 2 in sem: 2
location 1 1 2
8
Enter the student Serial Number: 2
Enter the semester: 1
Enter the attribute you want to fetch
1.
