A simple script with a clear task: reading a large Excel file and organizing its data into a Python dictionary.
---

# How does it work?
* In the **ExcelData** module, the file is read and the dictionary is then populated using a loop that iterates through
each row, stores the data in variables, and automatically adds them to the **CountyData** dictionary within the loop.
The main function used is **`setdefault()`**.

* However, in the main program, it simply imports the **ExcelData** module, creates a new Python file named **census2010**,
opens it in **write (`w`) mode**, and populates it with the dictionary that was created earlier in the module.

* Finally, once the **the program** file is run, it is automatically populated with the data in a clear and well-organized
format in **census2010**.
The dictionary uses the `states` as its main keys, with each state containing a dictionary as its value.
Inside this dictionary, the keys represent the `counties`, and each county has another dictionary as its value
containing two keys: **`pop`**, which stands for population, and **`tracts`**, which represents the number of census tracts
in that county. Each key contains its corresponding value.
---
# How to Run the Program?
Place all the files in the same folder, then open the **`the program`** file in any text editor or IDE 
and simply click **Run**.
Make sure that the **`census2010`** file does not already exist in the folder so that it can be created automatically
by the code.

---
# Author
*This project is an application of what I learned from the book **Automate the Boring Stuff with Python***.

Sief Nasr





