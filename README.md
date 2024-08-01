# Google Website Query Search

This repository contains a Python script to automate Google searches for specified queries on specified websites. The script reads queries and websites from a CSV file, constructs Google search URLs, and opens them in new browser tabs.

## Features

- **Automate Google Searches**: Open Google search results for specified queries on specified websites.
- **CSV Input**: Read queries and websites from a CSV file (`queries_websites.csv`).
- **Browser Automation**: Automatically open search URLs in new browser tabs.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python Latest Version installed
- Required Python library: `pandas`

You can install the required library using pip:

```bash
pip install pandas
```

## Installation

1. Download the repository files to your local computer.
   - Go to the repository on GitHub.
   - Click on the "Code" button and select "Download ZIP".
   - Extract the ZIP file to your desired location.

2. Ensure the necessary Python library is installed.

## Usage

1. Prepare a CSV file (`queries_websites.csv`) with your queries and websites. The file should have the following format:

   ```csv
   query,website
   example query 1,example.com
   example query 2,anotherexample.com
   example query 3,yetanotherexample.com
   ```

2. Open the Command Prompt (cmd) and navigate to the directory where the script is located.

3. Run the Python script with the path to your CSV file:

   ```bash
   python "Google Website Query Search.py"
   ```

## Example CSV

Here's an example of how your `queries_websites.csv` file should look:

```csv
query,website
best laptops 2024,techradar.com
top 10 programming languages 2024,stackoverflow.com
how to start a blog,bloggingbasics101.com
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

If you have any questions or suggestions, feel free to reach out to:

- Name: Haseeb Ur Rehman Mughal
- Email: Haseebmughal546@gmail.com
