# Anti-Plagiarism

## Setup

- Copy the www folder into wampserver folder
- Type `localhost` into your web browser
- Upload the dummy file `1.pdf` present in the folder. 
  P.S. Other files other than `1.pdf` won't work since code is hard coded during development stage.
- The `upload.php` script runs on clicking `submit` and the file gets uploaded to folder `upload` in `www` folder.


## Expected Outcome

- The file gets uploaded and `new-pdf.py` is triggered.

## Observed/Current Outcome

- The file gets uploaded and `new-pdf.py` is not triggered.

## Enhancement

- Make a way such that the `new-pdf.py` gets triggered.
- You can run the batch file `run.bat` and see the script working. You can also run batch file using PHP to execute the Python Script.
  Anything else will do, just run the file `new-pdf.py`
  
  
## Installation

- Anaconda installation required

  Libraries that need to be installed before proceeding
  
  - PyPDF2
  - Flask
  - Jinja2
  
