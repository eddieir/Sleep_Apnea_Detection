from pipeline import SleepApneaDetectionPipeline

if __name__ == "__main__":
    # URL of the dataset (replace with the actual download link from PhysioNet)
    DATA_URL = "https://physionet.org/static/published-projects/sleep-edf/sleep-edf-database-1.0.0.zip"
    # Local paths for downloading and extracting
    DOWNLOAD_PATH = "sleep_edf_dataset.zip"
    EXTRACTED_PATH = "sleep_edf_data"
    CSV_FILE_NAME = "sleep_data.csv"  # Replace with the actual CSV file name inside the extracted folder

    # Run the pipeline
    pipeline = SleepApneaDetectionPipeline(DATA_URL, DOWNLOAD_PATH, EXTRACTED_PATH, CSV_FILE_NAME)
    pipeline.run()
