# PDF Table Extractor (Flask Web App) (Project #1)

A lightweight web application built with Python and Flask that allows users to upload PDF documents, automatically extracts tabular data from them, cleans up complex/messy headers, and displays the tables on the web while generating a downloadable Excel (`.xlsx`) file.
## Features
**File Uploading:** Securely handles PDF uploads using Flask.
**Data Extraction:** Uses `pdfplumber` to scrape tables from multiple PDF pages.
**Data Cleaning:** Uses `pandas` to merge multi-line headers and remove blank `NaN` artifacts from the PDF extraction process.
**Export to Excel:** Automatically generates an Excel file with each table on a separate sheet using `openpyxl`.
**Responsive Frontend:** Simple, clean UI built with Bootstrap 5.

# Words and Paragraphs Counter (Project #2)
A simple, fast, and responsive web application built with **Python** and **Flask** that counts the exact number of characters, words, and paragraphs in a given text.
## Features
* **Word & Character Count:** Accurately calculates the total words and characters.
* **Paragraph Count:** Intelligently counts paragraphs while ignoring empty lines.
* **Live Clock & Date:** Displays today's date and a real-time updating clock using JavaScript.
* **Modern UI:** Clean and responsive interface styled with **Bootstrap 5**.
