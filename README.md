# Document_Search_Reader by Rohith Vishnu Kumar

**This is a Tool which takes documents of (.pdf, .docx, .xlsx, .jpg, .jpeg, .png) formats. It scans the documents (even there are images inside the documents) and extracts the text and allows the user to serach for Keywords (Multiple keywords seperated by commas) at a single time. It no only searches for exact word but also searches for Synonyms related to that keyword. It also have an advanced Search Capability where user can extensively search inside the document with prompt and even ask questions related to the document all in real time. It also have a summarise option where it gives a concise summary of the document and the summarised document is made available for download.**

Features:
1. Multi-format Document Support: <br>
PDF: Extracts text from PDFs, including those with embedded images.
DOCX: Reads and processes text from Word documents.
XLSX: Extracts text from Excel sheets.
Image Files: Utilizes OCR (Optical Character Recognition) to extract text from images in JPG, JPEG, and PNG formats.

2. Text Extraction and Search:<br>
Keyword Search: Allows users to search for multiple keywords at once.
Synonym Search: Searches for synonyms of the provided keywords to enhance search results.
Advanced Search: Enables extensive search within documents using prompts and real-time questions.

3. Summarization:<br>
Document Summarization: Provides a concise summary of the document.
Downloadable Summary: Summarized content is available for download in a user-friendly format.

# Installation

To get started with Document_Search_Reader, follow these steps:

1. Clone the repository and cd to Current Directory:
    ```
    git clone https://github.com/Rohithvishnukumar/Document_Search_Reader.git
    cd Doc_Reader
    ```

2. Install Dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a .env file and add this variables:
   ```
   API_KEY =           # Google gemini 1.5 flash api key
   secret_key = ""     # session secrete key

   MYSQL_HOST = ""
   MYSQL_USER = ""
   MYSQL_PASSWORD = ""
   MYSQL_DB = ""


   MAIL_USERNAME = ""  # your mail id
   MAIL_PASSWORD = ""  # you application password (google)

   # also add the gemini api in advancedsearch.js
   ```

4. Run the application:
   ```
   python app.py
   ```

5. If you are going for Deployment in live Server Use gunicorn

# Contact
# For questions, suggestions, or feedback, please open an issue on GitHub or contact us at rohithvishnuk@gmail.com

