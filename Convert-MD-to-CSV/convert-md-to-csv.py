import marko
import pandas as pd
import re
from bs4 import BeautifulSoup

def convert_md_to_html(file_path):
   with open(file_path, 'r') as f:
       text = f.read()
   html = marko.convert(text)
   return html

def populate_csv(html_path, csv_path):
    # Parse the HTML file
    with open(html_path, 'r') as f:
        contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    rows = []
    details = soup.find_all('details')
    for detail in details:  
        oss_category = detail.find_previous('h1').text
        agent_name = detail.find_previous('h2').text
        tagline = detail.find_previous('p').text
        
        # Dict that represents a single row
        agent_row = { 'Category': oss_category, 'Name': agent_name, 'Tagline': tagline}

        logo_url = detail.find('img')
        if logo_url is not None:
            logo_url = logo_url['src']            
            agent_row["Image"] = logo_url
        else:
            agent_row["Image"] = ""

        agent_use_case_category = detail.find('h3', string='Category')
        if agent_use_case_category is not None:
            agent_use_case_category_paragrahp = agent_use_case_category.find_next('p')
            agent_row["Use-cases"] = agent_use_case_category_paragrahp.text
        else:
            agent_row["Use-cases"] = ""

        description_el = detail.find('h3', string='Description')
        if description_el is not None:                        
            description = description_el.find_next('ul')
            agent_row["Description"] = description
        else:
            agent_row["Description"] = ""           

        # TODO: Improve parsing links
        links_el = detail.find('h3', string='Links')
        if links_el is not None:           
            links = links_el.find_next('ul')
            agent_row["Links"] = links
        else:
            agent_row["Links"] = ""
        
        rows.append(agent_row)
    
    df = pd.DataFrame.from_dict(rows, orient='columns')              
    df.to_csv(csv_path, header=True, index=False)    
    

if __name__ == "__main__":
    md_file_path = "/Users/terezatizkova/Developer/awesome-ai-agents/README.md" # replace with your file path
    html = convert_md_to_html(md_file_path)

    # Save HTML output
    with open("output.html", 'w') as f:
        f.write(html)

    # CSV file path
    csv_file_path = "converted_output.csv"

    # Populate the CSV file
    populate_csv("output.html", csv_file_path)