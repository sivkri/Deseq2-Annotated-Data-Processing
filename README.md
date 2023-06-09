# filter-based-on-FC-and-FDR
Filter DE genes based on log2Folchange, FDR value or both

# Deseq2_Annotated_Data_Processing

This repository contains a Python script for processing and filtering annotated data generated by the DESeq2 differential expression analysis tool. The script takes a DESeq2 annotated file as input, applies filtering criteria based on log2 fold change and adjusted p-values, and generates a modified output file.

## Prerequisites
- Python 3.x

## Usage
1. Clone the repository to your local machine or download the script file directly.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Execute the script using the following command:
   ```
   python filter_FDR_FC.py [input_file]
   ```
   Replace `[input_file]` with the path to the DESeq2 annotated file you want to process.
5. The processed output file will be generated in the same directory as the input file with a modified name.


The provided Python script (filter_FDR_FC.py) processes a DESeq2 annotated file by filtering the data based on log2 fold change and adjusted p-values. Here's a breakdown of the code:

1. The script imports the `sys` module to retrieve command-line arguments.
2. The input file path is obtained from the command-line arguments and opened for reading (`f1`).
3. The output file path is generated by replacing the input file name with "1.5_FC_New" (`output`). A new file is opened for writing (`out`).
4. The header line from the input file is read and written to the output file.
5. For each line in the input file:
    - The line is stored in a variable `l` for writing to the output file later.
    - The line is stripped of leading/trailing whitespaces and split into a list based on tab separators.
    - The gene ID, log2 fold change, and adjusted p-value are extracted from the line.
    - If the adjusted p-value is less than 0.05 and the log2 fold change is greater than 1 or less than -1, the line is written to the output file.
6. Once all lines have been processed, the script finishes execution, and the output file is closed.

## License
This project is licensed under the [MIT License](LICENSE). Feel free to modify and use the code according to your needs.
