# Vacations Management System 🌍✈️

A Python-based application for managing vacation data. This system allows you to add, update, view, and delete vacation packages stored in a MySQL database. It supports the CRUD (Create, Read, Update, Delete) operations, and connects to a remote MySQL database for persistent storage.

## Features 🔥

- **Add New Vacation**: Add new vacation details including title, description, start date, end date, price, and destination country.
- **Update Vacation**: Update vacation details such as title, description, dates, price, and country.
- **Delete Vacation**: Remove vacation records from the database.
- **View Vacations**: View all vacations available in the database.

## Installation 🛠️

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/beydonce/Vacations-project.git
   cd vacations-management
Install Dependencies:

Install the required Python packages using pip.

bash
Copy
Edit
pip install -r requirements.txt
Setup MySQL Database:

Make sure you have a MySQL database running. Create a database with the name vacations and configure it with the following schema:

sql
Copy
Edit
CREATE DATABASE vacations;
Configuration:

Update the DAL class in the src/utils/dal.py file to point to your MySQL server's host:

host="your_main_computer_ip_or_hostname"
Ensure that your MySQL server is accessible and configured to accept remote connections (if applicable).

Usage 📖
Running the Application:

To run the application, execute the following command:
python src/utils/main.py

Available Options:

Add a new vacation
Update vacation details
Delete vacation
View all vacations
Follow the on-screen prompts to interact with the system.

Example
Here’s a sample interaction with the program:


=== Manage Vacations ===
1. Add New Vacation 🏖️
2. Update Vacation Details 📝
3. Delete Vacation 🗑️
4. View Vacations 🏖️
0. Back to Main Menu 🔙
Choose an option: 1

--- Add New Vacation ---
Enter vacation title: Summer in Paris
Enter vacation description: A wonderful vacation in Paris with a lot of sightseeing.
Enter start date (YYYY-MM-DD): 2025-06-01
Enter end date (YYYY-MM-DD): 2025-06-15
Enter price: 2500
Enter country ID: 1

Contributing 🤝
We welcome contributions! If you would like to contribute, please fork the repository and submit a pull request with your proposed changes.

Steps to contribute:
Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes and commit them (git commit -am 'Add new feature').
Push to the branch (git push origin feature/your-feature).
Open a pull request.
License 📝
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements 🙏
Thank you Uri the GOAT for teaching us!!
🚀 Happy coding!



### Explanation:
- **Introduction**: A quick description of what the project does.
- **Features**: A list of features that the application supports.
- **Installation**: Detailed steps to clone the repository, install dependencies, and set up the MySQL database.
- **Usage**: Instructions on how to run the program and interact with it.
- **Example**: A small sample interaction showing how the user would use the application.
- **Contributing**: Guidelines for contributing to the project.
- **License**: MIT license section (you can change the license based on your preferences).
- **Acknowledgements**: Credits to any third-party software or libraries used in the project.




