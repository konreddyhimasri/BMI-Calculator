# BMI-Calculator

**⚖️ BMI Calculator** – Project Overview

The BMI Calculator is a Python-based GUI application built using Tkinter that allows users to calculate and track their Body Mass Index (BMI). It takes user inputs for weight (kg) and height (cm), computes the BMI, classifies the result into categories such as Underweight, Normal Weight, Overweight, or Obesity, and stores the data for future reference. Additionally, the application provides a BMI history viewer and a graph plotting feature to visualize trends over time.

**🌟 Features**

BMI Calculation – Computes BMI using the formula:

![Image](https://github.com/user-attachments/assets/afce3c09-0ec9-44a0-a4aa-9e836e4247f7)
​
**BMI Classification – Categorizes BMI into four groups:**

Underweight: BMI < 18.5

Normal Weight: BMI between 18.5 and 24.9

Overweight: BMI between 25 and 29.9

Obesity: BMI ≥ 30

**Data Storage**– Saves BMI records in a CSV file for historical tracking.

View BMI History – Displays past BMI records for different users.

Plot BMI Trends – Uses Matplotlib to generate a graph showing BMI changes over time.

Error Handling – Detects and alerts users when invalid inputs are provided.

User-Friendly GUI – Designed with a light blue theme for easy readability.

**🛠️ Technologies Used**

Python – The core programming language.

Tkinter – Used to build the graphical user interface (GUI).

CSV Module – Saves BMI records in a structured format.

Matplotlib & NumPy – Used to plot historical BMI data trends.

OS Module – Checks if previous BMI records exist before accessing them.

**🚀 How It Works?**

**1️⃣ User Inputs Details**

The user enters their name, weight (in kg), and height (in cm) into the respective input fields.

Clicking the "Calculate BMI" button triggers the calculation.

**2️⃣ BMI Calculation & Classification**

The entered height is converted from centimeters to meters.

The BMI is computed using the standard formula.

The BMI value is classified into one of the four categories.

The result is displayed on the screen.

**3️⃣ Saving Data for Future Reference**

Each BMI calculation is saved in a CSV file (bmi_data.csv) with the following details:

Username, Weight (kg), Height (cm), BMI Value, Category

If the CSV file doesn’t exist, it is automatically created.

**4️⃣ Viewing BMI History**

Clicking the "Show History" button opens a new window displaying all previous BMI records for different users.

The history is retrieved from the CSV file and organized by username.

**5️⃣ Plotting BMI Trends**

Clicking the "Plot Data" button generates a line graph using Matplotlib.

Each user’s BMI records are plotted over time with different colors.

The graph helps track BMI fluctuations and trends.

**6️⃣ Error Handling**

If a user enters non-numeric values for weight or height, an error message is displayed.

If any field is left empty, the application prompts the user to complete all fields.

If the history file (bmi_data.csv) doesn’t exist, an alert notifies the user.

**🖥️ User Interface Design**

The BMI Calculator UI is designed to be simple and intuitive with a light blue theme for better readability.

**Main Interface**

Title Section – Displays "BMI Calculator" in bold text at the top.

Input Fields – Three fields allow users to enter their name, weight, and height.

Calculate Button – Clicking this button computes and displays the BMI.

Result Display – The computed BMI and its category appear below the button.

**Additional Features**

Show History Button – Opens a new window displaying all saved BMI records.

Plot Data Button – Generates a graph showing BMI trends over multiple entries.

**📌 Future Enhancements**

✅ Health Advice Feature – Provide dietary and fitness recommendations based on BMI.

✅ Multi-User Support – Allow multiple users to log in and track their BMI separately.

✅ Export Data Option – Enable users to download their BMI history as a PDF or Excel file.

✅ Mobile-Friendly Version – Convert the application into a mobile app using Kivy.

✅ Real-Time BMI Trends – Display an interactive dashboard with graphical updates.


![Image](https://github.com/user-attachments/assets/934cb529-0f9a-438b-b7fe-b6f47d3097e5)
![Image](https://github.com/user-attachments/assets/a3453bd7-cb68-4049-9e10-a0e06667b759)
![Image](https://github.com/user-attachments/assets/17a774eb-b9c6-42e6-b92c-cb3d32c0bb8c)

**VIDEO REFERENCE:**

https://github.com/user-attachments/assets/a4bcf15a-a022-4599-be9a-0a1a0d0f27cd
