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

   # Find the h1 tag that comes after the specific h1 tag
   h1_tags = soup.find_all('h1')
   for tag in h1_tags:
       if 'open_hands: Open-source projects' in str(tag):
           next_h1 = tag.find_next('h2')
           while next_h1 is not None:
               name = next_h1.text
               # Append the name to the CSV file
               df = pd.DataFrame({'Name': [name]})
               df.to_csv(csv_path, mode='a', header=False, index=False)
               next_h1 = next_h1.find_next('h2')

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