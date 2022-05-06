# Excel Compare

This is a utility I created for use in my current job where I was having to compare many datasets which were either in Excel or CSV format.
Whilst there are ways of doing this in Excel with formulas etc., this soon became tedious due to the number of datasets I had to compare, and so I developed this script to help.

The script outputs an Excel file containing the following sheets.
- Overview: Lists the input files, and an indication of whether the headings in the Excel file matched.
- File 1: The first file.
- File 2: The second file.
- Comparison: A colour-coded true/false matrix of all cells, indicating whether the value matches across the two files.
- Differences: The same as the Comparison tab, however only including rows where there is a difference.
- Difference Detail: Shows the actual values of differences between the two files.

## Usage

```bash
usage: python3 excel_compare.py [-h] [-s SORT_KEY] [-o OUTPUT_FILE] file1 file2

positional arguments:
  file1           File1
  file2           File2

optional arguments:
  -h, --help      show this help message and exit
  -s SORT_KEY     Column name to sort files by
  -o OUTPUT_FILE  Output filename
```

