# School-Management-System

This is a project I made in my School.

# System Requirements

- Any OS will work
- MySQL installed
- Python installed along with `mysql.connector` package

## Steps to get the code running

- Start MySQL
- Create database name school with the following commmand
  `create database school`
- Then use the database
  `use school`
- Create table school with the following command

  ```
   create table school(Name VARCHAR(50),
   Class VARCHAR(20), Section VARCHAR(10), Scholar_No INT, Fees_Paid INT,
   Fees_Due INT, Caution_Fee INT, Items_Broken
   VARCHAR(100));

  ```

- Update the Python code with your MySQL password. No other changes are required

# Possible errors and their solutions

## General reminder

Install all the python packages using `pip3` for _Linux and Mac_ users and uninstall ones installed with pip

## Module not found error

To fix this you might try installing _mysql-connector-python-rf_ by running
`pip install mysql-connector-python-rf` for Windows users or `pip3 install mysql-connector-python-rf` for Linux/ Mac users.

You might also check for the _pyvenv.cfg_ file. If not, run the following command in terminal open in your project.

```
python3 -m venv .venv

```

**for Mac and Linux**

or

````

python -m venv .venv

```for Windows users.
Under that file, set `include-system-site-packages = true`
````
