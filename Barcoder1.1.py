# Chad Tope
# 8/27/2024
# barcoder-1.1.py

import barcode
from datetime import datetime
import os
import logging

# Setup logging
logging.basicConfig(filename='barcoder.log', level=logging.ERROR, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def get_shared_folder_path():
    shared_folder_name = "Gage_Folders"
    root_dir = os.getcwd()
    shared_folder_path = os.path.join(root_dir, shared_folder_name)
    
    if not os.path.exists(shared_folder_path):
        os.makedirs(shared_folder_path)
        print(f"Shared folder '{shared_folder_name}' created at {shared_folder_path}")
    else:
        print(f"Using existing shared folder at {shared_folder_path}")
    
    return shared_folder_path

def generate_barcode_and_files(Gage_equipment_number, part_number, operation_numbers, Gage_version, Gage_creation_date, Gage_program):
    try:
        Gage_file_update = datetime.now().strftime("%m-%d-%Y")
        shared_folder_path = get_shared_folder_path()
        folder_name = os.path.join(shared_folder_path, f"{Gage_equipment_number}_{Gage_file_update}")
        existing_folders = [folder for folder in os.listdir(shared_folder_path) if folder.startswith(Gage_equipment_number)]
        if existing_folders:
            print(f"A folder with Gage equipment number '{Gage_equipment_number}' already exists.")
            return False

        os.makedirs(folder_name)
        barcode_filename = f"{Gage_equipment_number}_{Gage_file_update}.svg"
        barcode_filepath = os.path.join(folder_name, barcode_filename)
        barcode_class = barcode.get_barcode_class('code128')
        barcode_object = barcode_class(Gage_equipment_number)
        
        with open(barcode_filepath, "wb") as f:
            barcode_object.write(f, options={'write_text': False})
        print(f"Barcode saved as {barcode_filepath}")

        text_filename = f"{Gage_equipment_number}_{Gage_file_update}.txt"
        text_filepath = os.path.join(folder_name, text_filename)
        with open(text_filepath, "w") as text_file:
            text_file.write(f"Gage Creation Date: {Gage_creation_date}\n\n")
            text_file.write(f"Gage Type: {Gage_type}\n")
            text_file.write(f"Gage Version: {Gage_version}\n\n")
            text_file.write(f"Gage Equipment Number: {Gage_equipment_number}\n")
            text_file.write(f"Gage Program(s): {Gage_program}\n")
            text_file.write(f"Part Number(s): {part_number}\n")
            text_file.write(f"Operation Number(s): {operation_numbers}\n\n")
            text_file.write(f"Last Updated: {Gage_file_update}\n")
        print(f"Text file saved as {text_filepath}")

        submission_log = os.path.join(folder_name, f"{Gage_equipment_number}_submission_log.csv")
        with open(submission_log, "w") as csvfile:
            csvfile.write("Gage Creation Date,Gage Type,Gage Version,Gage Equipment Number,Gage Program(s),Part Number(s),Operation Number(s),Last Updated\n")
            csvfile.write(f"{Gage_creation_date},{Gage_type},{Gage_version},{Gage_equipment_number},{Gage_program},{part_number},{operation_numbers},{Gage_file_update}\n")
        print(f"Submission log saved as {submission_log}")

        return True

    except Exception as e:
        logging.error(f"Failed during barcode and file generation: {e}")
        print("An error occurred. Please check the logs for details.")
        return False

if __name__ == "__main__":
    while True:
        part_number = input("Enter the part number: ")
        operation_numbers = input("Enter the operation number(s): ")
        Gage_creation_date = input("Enter the Gage creation date (mm-dd-yyyy): ")
        Gage_type = input("Enter the Gage type: ")
        Gage_version = input("Enter the Gage version: ")
        Gage_equipment_number = input("Enter the Gage equipment number: ")
        Gage_program = input("Enter the Gage program: ")

        try:
            datetime.strptime(Gage_creation_date, "%m-%d-%Y")
            
            if generate_barcode_and_files(Gage_equipment_number, part_number, operation_numbers, Gage_version, Gage_creation_date, Gage_program):
                run_again = input("Do you want to create another barcode and files? (yes/no): ").strip().lower()
                if run_again != 'yes' and run_again != 'y':
                    print("Exiting the program.")
                    break
            else:
                print("Please enter a different Gage equipment number.")
        except ValueError:
            print("Invalid date format. Please enter the Gage creation date in mm-dd-yyyy format.")
