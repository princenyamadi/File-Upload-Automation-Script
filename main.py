import os
import requests
from requests.exceptions import RequestException
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()


# DECLARATIONS
PROD_BASE_URL=os.getenv('PROD_BASE_URL')
DEV_BASE_URL=os.getenv('DEV_BASE_URL')
BASE_URL=DEV_BASE_URL
LOGIN_URL = BASE_URL + '/v1/auth/login'
UPLOAD_URL = BASE_URL + '/v1/images/upload'
IMAGE_FOLDER = './images'
CHUNK_SIZE = 5


def get_token():
    login_payload = {
        "email":os.getenv("EMAIL"),
        "password": os.getenv('PASSWORD')
    }
    
    try:
        response = requests.post(LOGIN_URL,json=login_payload)
        response.raise_for_status()
        token = response.json().get('token')
        if not token: 
            raise ValueError("Token not found in response!")
        print("Login succcessful, token retrieved")
        return token
    except RequestException as e:
        print(f"Error during login: {e}")
        raise
    except ValueError as e:
        print(e)
        raise
    
# *------
def upload_files(token, description, tags, event_id):
    headers = {"Authorization" : f"Bearer {token}"}
    
    try:
        files = [os.path.join(IMAGE_FOLDER, f) for f in os.listdir(IMAGE_FOLDER) if os.path.isfile(os.path.join(IMAGE_FOLDER, f))]
    except FileNotFoundError:
        print(f"The folder {IMAGE_FOLDER} does not exist!")
        return
    
    if not files:
        print("No files found in the specified folder.")
        return
    
    for i in range(0, len(files),CHUNK_SIZE):
        chunk = files[i:i + CHUNK_SIZE]
        files_data = [("images", (os.path.basename(file_path), open(file_path, 'rb'))) for file_path in chunk]

        try:
            # Prepare the multipart form-data payload
            payload = {
                "description": description,
                "tags": tags,
                "eventId": event_id
            }
            print(f"Uploading {len(chunk)} files...")
            response = requests.post(UPLOAD_URL, headers=headers, data=payload, files=files_data)
            response.raise_for_status()
            print(f"Uploaded {len(chunk)} files successfully.")
        except RequestException as e:
            print(f"Error uploading files in this chunk: {e}")
        finally:
            # Close file objects to avoid resource leaks
            for _, (_, file) in files_data:
                file.close()
                         
# execute
if __name__ == "__main__":
    try:
        token = get_token()
        
        description = "Coastal Expedition 2024",
        tags = "event,tour,photography,album,costal,capecoast,ghana"
        event_id =""
        
        # Upload files
        upload_files(token=token,description=description,event_id=event_id,tags=tags)
        
        print("File upload process completed")
    except Exception as e:
        print(f"Script terminated with error: {e}")
