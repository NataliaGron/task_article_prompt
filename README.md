# Article-to-HTML Converter

This application, built using Python, connects to the OpenAI API to process text files efficiently. It reads a provided article from a text file and sends its content, along with a specified prompt, to OpenAI for content generation. The resulting HTML code from OpenAI is then saved as artykul.html for easy access and use.

**Main features**:
- **Integration with OpenAI API**: The application connects to the OpenAI API to send article content and receive generated HTML code.
- **Text File Processing**: Automatically reads the article content from a text file and sends it to OpenAI for processing.
- **HTML File Generation**: Saves the generated HTML code in an artykul.html file, ready for use.

&nbsp;

## Installation

The project uses Python, along with the OpenAI API for text processing and HTML code generation.
- Install Python.
- Run `pip install openai` in the terminal to install the OpenAI library.
- Sign up at OpenAI and obtain your API key.
- In the code, replace `<API_KEY>` in the following line:
`client = OpenAI(api_key='<API_KEY>')` with your actual API key.
- Create an article.txt file in the same directory as the script and paste the article content you want to process into it.
- In the terminal, navigate to the folder containing the script and run it with the following command: `python main.py`
- The generated artykul.html file will appear in the same folder, ready to be used or further edited.

&nbsp;

## Additional Files

In addition to the article-to-HTML converter functionality, this project includes two additional HTML files to help you preview and visualize the generated article:
- `szablon.html`: This is a template file that provides the basic structure for displaying the article. It includes a placeholder `<body>` section where the article content will be inserted. You can use this template to format and style the generated article in any way you prefer. Simply copy and paste the generated HTML content from `artykul.html` into the `<body>` of this template.
- `podglad.html`: This file allows you to preview the article directly in the browser. It contains the same template as `szablon.html`, and the generated article content from the `artykul.html` file is already pasted into the `<body>` section.