# Barcoder
A program for generating barcodes to serialize gages and streamline documentation written in Python 3.10.11

### Barcoder 1.1
### Overview
Barcoder 1.1 is a Python script designed to generate barcodes and associated files for Gage equipment. The script creates a folder structure, generates a barcode in SVG format, and saves relevant information in text and CSV files. It also includes logging for error tracking.
Uses python-barcode. Source:https://github.com/WhyNotHugo/python-barcode

### Features
Generates barcodes in Code128 format.
Creates a structured folder for each Gage equipment.
Saves relevant Gage information in text and CSV files.
Logs errors for debugging and maintenance.

### Requirements
Python 3.x
python-barcode module
Installation
Clone the repository:
git clone https://github.com/yourusername/barcoder.git
cd barcoder

Install the required module:
pip install python-barcode

### Usage
Run the script:
python barcoder-1.1.py

Follow the prompts to enter the required information:
Part number
Operation number(s)
Gage creation date (mm-dd-yyyy)
Gage type
Gage version
Gage equipment number
Gage program
The script will generate a barcode and save the files in a structured folder within the Gage_Folders directory.

### Logging
Errors and important events are logged in the barcoder.log file located in the root directory. This helps in tracking the program’s execution and debugging any issues.

### Example
Enter the part number: 12345
Enter the operation number(s): 67890
Enter the Gage creation date (mm-dd-yyyy): 08-27-2024
Enter the Gage type: TypeA
Enter the Gage version: 1.0
Enter the Gage equipment number: GE123
Enter the Gage program: ProgramA

### License
MIT License

Copyright (c) 2024 Chad Tope

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


Author
Chad Tope
