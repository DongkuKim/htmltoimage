import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image

# Create a function to render HTML and CSS to an image
def capture_webpage_image(html_content, output_image="webpage_image.png"):
    # Setup Chrome options for headless operation
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless Chrome (without UI)
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    chrome_options.add_argument("--window-size=1920x1080")  # Set window size for rendering

    # Setup the WebDriver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    
    # Create a temporary HTML page
    temp_html_path = "temp_page.html"
    
    # Write the HTML (with embedded CSS) to a temporary file
    with open(temp_html_path, "w") as file:
        file.write(html_content)

    # Load the HTML page in the browser
    driver.get(f"file:///{temp_html_path}")

    # Wait for the page to fully load
    time.sleep(2)

    # Capture a screenshot of the page
    screenshot_path = "screenshot.png"
    driver.save_screenshot(screenshot_path)

    # Close the browser
    driver.quit()

    # Open the screenshot image using Pillow for any processing (if needed)
    img = Image.open(screenshot_path)
    
    # Save the final image
    img.save(output_image)
    print(f"Screenshot saved as {output_image}")

# Example usage with both HTML and CSS in the same string
html_and_css = """
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

capture_webpage_image(html_and_css)
