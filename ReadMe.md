# Cermati Assignment
---
This is a Python script that scrapes job postings from Cermati website and saves them as a JSON file.

Installation
To run this script, you need to have Python 3 and the following libraries installed:

requests

You can install them using pip:

```Python
pip install requests
```
Usage
To use this script, you need to clone this repository or download the main.py file. Then, you can run the script from the command line:

```Python
python main.py
```
The script will create two files in the same directory: index.html and data.json. The index.html file contains the HTML source code of the Cermati website. The data.json file contains the scraped job postings organized by department.

The data.json file has the following structure as asked in assignement:
```pyhon
{
    "department": [
        {
            "title": "job title",
            "location": "job location",
            "description": "job description",
            "qualification": "job qualification",
            "posted by": "job poster"
        },
        ...
    ],
    ...
}
```



#Contact
If you have any questions or feedback, please contact me You have my details.