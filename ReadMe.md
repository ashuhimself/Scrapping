# Cermati Assignment
---
This is a Python script that scrapes job postings from Cermati website and saves them as a JSON file.

Installation
To run this script, you need to have Python 3 and libraries installed:



You can install them using pip:

```Python
pip install -r requirements.txt
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

===

[]:Used requests.Session() to maintain a persistent connection with the website and minimize the number of HTTP requests sent.

[]:Used re.compile() to compile the regex pattern for extracting job URLs, which is more efficient than compiling the pattern every time it is used.

[]:Used a copy() method to copy dictionaries in the group-by loop to avoid modifying the original dictionaries and causing unintended side effects.

[]:Added a timer to measure the runtime of the program and a counter timer to show the execution progress of the program in seconds.

===

#Contact
If you have any questions or feedback, please contact me You have my details.