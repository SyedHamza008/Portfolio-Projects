# PDF Table Extractor (Flask Web App)

A lightweight web application built with Python and Flask that allows users to upload PDF documents, automatically extracts tabular data from them, cleans up complex/messy headers, and displays the tables on the web while generating a downloadable Excel (`.xlsx`) file.
## Features
**File Uploading:** Securely handles PDF uploads using Flask.
**Data Extraction:** Uses `pdfplumber` to scrape tables from multiple PDF pages.
**Data Cleaning:** Uses `pandas` to merge multi-line headers and remove blank `NaN` artifacts from the PDF extraction process.
**Export to Excel:** Automatically generates an Excel file with each table on a separate sheet using `openpyxl`.
**Responsive Frontend:** Simple, clean UI built with Bootstrap 5.
