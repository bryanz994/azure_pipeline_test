# Python program to bulk upload json files as blobs to azure storage
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContentSettings, ContainerClient
 
# IMPORTANT: Replace connection string with your storage account connection string
# Usually starts with DefaultEndpointsProtocol=https;...
MY_CONNECTION_STRING = "CHANGEME"
 
# Replace with blob container. This should be already created in azure storage.
MY_EVENTS_CONTAINER = "default/events"
 
# Replace with the local folder which contains the json files for upload
LOCAL_EVENTS_PATH = "./"
 
class AzureBlobFileUploader:
  def __init__(self):
    print("Intializing AzureBlobFileUploader")
 
    # Initialize the connection to Azure storage account
    self.blob_service_client =  BlobServiceClient.from_connection_string(MY_CONNECTION_STRING)
 
  def upload_all_json_in_folder(self):
    # Get all files with json extension and exclude directories
    all_file_names = [f for f in os.listdir(LOCAL_EVENTS_PATH)
                    if os.path.isfile(os.path.join(LOCAL_EVENTS_PATH, f)) and ".json" in f]
 
    # Upload each file
    for file_name in all_file_names:
      self.upload_json(file_name)
 
  def upload_json(self,file_name):
    # Create blob with same name as local file name
    blob_client = self.blob_service_client.get_blob_client(container=MY_EVENTS_CONTAINER,
                                                          blob=file_name)
    # Get full path to the file
    upload_file_path = os.path.join(LOCAL_EVENTS_PATH, file_name)
 
    # Create blob on storage
    # Overwrite if it already exists!
    json_content_setting = ContentSettings(content_type='text/json')
    print(f"uploading file - {file_name}")
    with open(upload_file_path, "rb") as data:
      blob_client.upload_blob(data,overwrite=True,content_settings=json_content_setting)
 
 
# Initialize class and upload files
azure_blob_file_uploader = AzureBlobFileUploader()
azure_blob_file_uploader.upload_all_json_in_folder()
