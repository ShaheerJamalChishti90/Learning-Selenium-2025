# Selenium-MasterProject

This repository demonstrates how to scrape the Audible website using Selenium with pagination and a custom bot. Follow the steps below to set up and run the project smoothly on both Windows and macOS. Instructions are provided for both `.ipynb` and `.py` file users.

---

## Prerequisites

1. **Python Installation**  
   Ensure Python 3.7 or above is installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Google Chrome Installation**  
   Install the latest version of Google Chrome from [google.com/chrome](https://www.google.com/chrome/).

3. **ChromeDriver Installation**

   - Download the ChromeDriver version compatible with your Chrome browser from [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads).
   - **Windows**: Extract the `chromedriver.exe` file and place it in a known directory (e.g., `C:\chromedriver\chromedriver.exe`).
   - **macOS**: Extract the `chromedriver` file and move it to `/usr/local/bin/` or another directory in your PATH.

4. **Install Required Libraries**  
   Install the necessary Python libraries using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

---

## Project Setup

1. **Clone the Repository**  
   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/MuhammadUzair1/Selenium-MasterProject
   cd Selenium-MasterProject
   ```

2. **Update the ChromeDriver Path**  
   Update the `path` variable in the script to point to your ChromeDriver location:

   ```python
   path = '/path/to/chromedriver'  # Replace with your actual path
   ```

3. **Run the Script**
   - **For `.py` Users**:  
     Run the script using the command:
     ```bash
     python script.py
     ```
   - **For `.ipynb` Users**:  
     Open the Jupyter Notebook and run the cells sequentially:
     ```bash
     jupyter notebook script.ipynb
     ```

---

## Audible Website to Scrape

The script scrapes data from the following Audible page:

- [Audible Best Sellers](https://www.audible.com/adblbestsellers)

---

## Output

The script extracts the following data:

- Book Title
- Book Author
- Book Length

The data is saved in a CSV file named `books_pagination.csv` in the project directory.

---

## Notes

- Ensure your ChromeDriver version matches your Chrome browser version.
- If you encounter issues with Selenium, verify that the `chromedriver` executable is in your PATH or update the `path` variable in the script.
- The script uses Selenium 3.141.0. If you wish to use a newer version, update the code accordingly.

---

## Troubleshooting

- **Common Errors**:
  - `WebDriverException`: Ensure the ChromeDriver path is correct.
  - `NoSuchElementException`: Verify that the website's structure has not changed.
- **Debugging**:
  - Use `time.sleep()` to allow pages to load fully.
  - Check the website's HTML structure using browser developer tools.

---

Enjoy scraping Audible with this project!
