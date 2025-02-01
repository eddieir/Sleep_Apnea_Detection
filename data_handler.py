import os
import pandas as pd
import requests
import zipfile

class DataHandler:
    def __init__(self, url, download_path, extracted_path):
        """
        :param url: The URL to download the dataset.
        :param download_path: The local file path to save the zip file.
        :param extracted_path: The folder to extract and store the dataset.
        """
        self.url = url
        self.download_path = download_path
        self.extracted_path = extracted_path

    def download_and_extract(self):
        """
        Download the dataset from the given URL, extract it, and save it to the specified folder.
        """
        print("Downloading dataset...")
        # Download the dataset
        response = requests.get(self.url, stream=True)
        if response.status_code == 200:
            with open(self.download_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            print(f"Dataset downloaded as {self.download_path}")
        else:
            raise Exception(f"Failed to download dataset. HTTP Status Code: {response.status_code}")

        # Extract the dataset
        print("Extracting dataset...")
        with zipfile.ZipFile(self.download_path, 'r') as zip_ref:
            zip_ref.extractall(self.extracted_path)
        print(f"Dataset extracted to {self.extracted_path}")

    def load_data(self, csv_file_name):
        """
        Load a specific CSV file from the extracted dataset folder.
        :param csv_file_name: The name of the CSV file to load.
        :return: A Pandas DataFrame containing the dataset.
        """
        csv_path = os.path.join(self.extracted_path, csv_file_name)
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"{csv_file_name} not found in extracted dataset.")
        print("Loading data from file...")
        data = pd.read_csv(csv_path)
        print("Data loaded successfully.")
        return data
