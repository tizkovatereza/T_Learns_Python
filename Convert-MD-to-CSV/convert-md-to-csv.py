import marko

def convert_md_to_html(file_path):
   with open(file_path, 'r') as f:
       text = f.read()
   html = marko.convert(text)
   return html

if __name__ == "__main__":
   file_path = "README.md" # replace with your file path
   html = convert_md_to_html(file_path)
   with open("output.html", 'w') as f:
       f.write(html)