import csv
import main


def check_consecutive_numbers_csv(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            numbers = []
            for row in csvreader:
                numbers.extend([int(num) for num in row])

            for i in range(len(numbers) - 2):
                if numbers[i] > 30 and numbers[i+1] > 30 and numbers[i+2] > 30:
                    print("starting song")
                    main.start_song()
                    return True

            return False
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return False
    except ValueError:
        print(
            "Invalid data in the file. Please ensure the file contains only numeric values.")
        return False


# Example usage:
file_path = "data.csv"  # Replace with the path to your CSV file
if check_consecutive_numbers_csv(file_path):
    print("There are three consecutive numbers over 30 in the CSV file.")
else:
    print("No three consecutive numbers over 30 found in the CSV file.")
