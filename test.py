from spire.doc import *
from spire.doc.common import *
import os

# HTML content as a string
html_content = """
<html>
<head>
    <title>Sample Webpage</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
        }

        h1 {
            font-size: 2em;
            color: blue;
        }

        p {
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a simple webpage generated in Python.</p>
</body>
</html>
"""

# Write the HTML content to a file
input_dir = 'input'
if not os.path.exists(input_dir):
    os.makedirs(input_dir)

# Define the file path for the HTML file inside the 'input' directory
html_file_path = os.path.join(input_dir, "test.html")

html_file_path = "input/test.html"  # Make sure the path is correct
with open(html_file_path, "w") as html_file:
    html_file.write(html_content)

# Create a Document object
document = Document()

# Load the HTML file
document.LoadFromFile(html_file_path, FileFormat.Html)

# Get the first section
section = document.Sections[0]

# Set the page margins (in inches)
section.PageSetup.Margins.All = 2  # You can adjust this value

# Convert the document to a list of image streams
imageStreams = document.SaveImageToStreams(ImageType.Bitmap)

# Create the output directory if it doesn't exist

output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate through the image streams and save them as PNG files
for index, stream in enumerate(imageStreams):
    # Construct the file path for the PNG file
    image_file_path = os.path.join(output_dir, f'image_{index}.png')
    
    # Save each image stream as a PNG file
    with open(image_file_path, 'wb') as imageFile:
        imageFile.write(stream.ToArray())

# Dispose resources to free up memory
document.Dispose()

print(f"Images saved to '{output_dir}'")
