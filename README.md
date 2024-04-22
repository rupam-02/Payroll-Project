# Payroll-Project
This Python program utilizes the mysql.connector library to manage a payroll system. It allows adding, displaying, searching, modifying, and deleting employee records in a MySQL database. Additionally, it calculates the final income based on specific parameters such as working days, allowances, and provident fund percentage.

Note : Before running the python program, we need to create the database payroll and the table payroll in MySQL and then run the program.

Here's a detailed description of its functionality:
1. Database Connection: The program establishes a connection to a MySQL database using the mysql.connector library, providing credentials such as host, user, password, and database name.
2. Menu Driven Interface: It offers a menu-driven interface for user interaction. The menu includes options to add a record, display records, search for a record, modify a record, delete a record, calculate final income, and exit the program.
3. Adding Records: The program allows users to add new employee records to the database. It prompts the user to enter details such as Employee ID, Employee Name, Department, and Monthly Salary. Additional default values for parameters like Working Days Per Year, HRA (House Rent Allowance), DA (Dearness Allowance), Medical Allowance, and Provident Fund can be modified later.
4. Displaying Records: Users can view all records stored in the payroll database. The program retrieves data from the database and displays it in a structured format, including Employee ID, Employee Name, Department, Monthly Salary, Working Days Per Year, HRA, DA, Medical Allowance, and Provident Fund.
5. Searching Records: Users can search for specific employee records by entering the Employee ID. The program queries the database to find and display the corresponding record if it exists.
6. Modifying Records: This feature allows users to update existing employee records. Users can choose which aspect of the record to modify, such as Employee ID, Employee Name, Department, Monthly Salary, Working Days Per Year, HRA, DA, Medical Allowance, or Provident Fund.
7. Deleting Records: Users can delete employee records from the database by entering the Employee ID corresponding to the record they wish to delete.
8. Calculating Final Income: The program calculates the final income for each employee based on the provided parameters. It considers factors such as Monthly Salary, Working Days Per Year, HRA, DA, Medical Allowance, and Provident Fund percentage to compute the final salary.
9. Menu Loop and Exit: The program runs in a continuous loop until the user chooses to exit. It provides a structured and interactive way to manage payroll-related tasks efficiently.

Overall, this program streamlines payroll management by offering functionalities for data manipulation, calculation, and database interaction, making it a valuable tool for HR and payroll departments.
