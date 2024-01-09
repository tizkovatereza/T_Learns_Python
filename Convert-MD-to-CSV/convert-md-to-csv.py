import marko
import pandas as pd
from bs4 import BeautifulSoup

def convert_md_to_html(file_path):
   with open(file_path, 'r') as f:
       text = f.read()
   html = marko.convert(text)
   return html

def create_empty_csv(file_path, columns):
   # Create an empty DataFrame with specified columns
   df = pd.DataFrame(columns=columns)
   # Save the DataFrame to a CSV file
   df.to_csv(file_path, index=False)

def populate_csv(html_path, csv_path):
 # Parse the HTML file
 with open(html_path, 'r') as f:
     contents = f.read()

 soup = BeautifulSoup(contents, 'lxml')

 # Initialize name and category
 name = ""
 category = ""

 # Iterate over the h1 and h2 tags
 for tag in soup.find_all(['h1', 'h2']):
     # Update the category if the tag is a h1 tag
     if tag.name == 'h1':
         category = 'Open source' if 'open_hands: Open-source projects' in str(tag) else 'Closed source'
     # Update the name if the tag is a h2 tag and the category is not empty
     elif tag.name == 'h2' and category:
         name = tag.text
         # Append the name and category to the CSV file
         df = pd.DataFrame({'Category': [category], 'Name': [name]})
         df.to_csv(csv_path, mode='a', header=False, index=False)


if __name__ == "__main__":
   md_file_path = "README.md" # replace with your file path
   html = convert_md_to_html(md_file_path)

   # Save HTML output
   with open("output.html", 'w') as f:
       f.write(html)

   # CSV file path
   csv_file_path = "converted_output.csv"
   # Columns for the CSV file
   columns = ["Category", "Name", "Tagline", "Description", "Links"]
   # Create and save the empty CSV file
   create_empty_csv(csv_file_path, columns)

   # Populate the CSV file
   populate_csv("output.html", csv_file_path)