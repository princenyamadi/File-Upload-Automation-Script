---

# File Upload Automation Script

## **Project Overview**

This Python script automates the process of uploading image files from a local directory to a remote server. The script authenticates the user via an API endpoint, retrieves a JWT token, and then uploads files in chunks using the multipart/form-data format. The image upload endpoint is secured by a Bearer token to ensure the authentication of each request.

## **Features**

- **User Authentication**: The script interacts with an authentication API to retrieve a JWT token for secure communication.
- **File Upload**: Uploads image files from a specified local directory to a remote server in chunks.
- **Multipart/form-data**: Utilizes multipart/form-data for file uploads, including metadata such as descriptions, tags, and event IDs.
- **Environment Configuration**: All sensitive credentials, including API keys and authentication tokens, are stored securely in an `.env` file for easy configuration.
- **Robust Error Handling**: Implements comprehensive error handling for issues such as expired tokens, failed file uploads, and network errors.
- **Logging**: Tracks the progress of uploads and logs any issues for easier debugging.

## **Technologies Used**

- **Python**: Core scripting language.
- **Requests**: HTTP library used for making API calls.
- **python-dotenv**: For managing environment variables.
- **Multipart/form-data**: Standard used for file upload via HTTP.
- **JWT Authentication**: For secure API requests.

## **Installation**

1. **Clone the repository**:

   ```bash
   git clone https://github.com/princenyamadi/File-Upload-Automation-Script.git

   cd File-Upload-Automation-Script
   ```

2. **Set up a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   .\venv\Scripts\activate   # On Windows
   ```

3. **Install required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file**:

   In the root of your project, create a `.env` file to store your credentials and other configuration details:

   ```ini
    EMAIL=<value>
    PASSWORD=<value>
    PROD_BASE_URL=<value>
    DEV_BASE_URL=<value>
   ```

5. **Run the script**:

   ```bash
   python upload_script.py
   ```

## **Usage**

- The script will authenticate the user and retrieve a token from the provided authentication API endpoint.
- It will then upload all image files found in the specified local directory to the remote server, using a multipart/form-data format.
- Each image file will be uploaded in chunks, and the script will handle the submission of metadata such as descriptions, tags, and event IDs along with the images.

## **Contributing**

Contributions are welcome! Please fork the repository and create a pull request for any improvements or fixes.

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
