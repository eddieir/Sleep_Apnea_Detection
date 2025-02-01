from data_handler import DataHandler
from preprocess import Preprocessor
from lstm_model import LSTMModel
from visualizer import Visualizer

class SleepApneaDetectionPipeline:
    def __init__(self, url, download_path, extracted_path, csv_file_name):
        """
        :param url: The URL to download the dataset.
        :param download_path: The local file path to save the zip file.
        :param extracted_path: The folder to extract and store the dataset.
        :param csv_file_name: The name of the CSV file to load after extraction.
        """
        self.url = url
        self.download_path = download_path
        self.extracted_path = extracted_path
        self.csv_file_name = csv_file_name

    def run(self):
        # Step 1: Download and load data
        data_handler = DataHandler(self.url, self.download_path, self.extracted_path)
        data_handler.download_and_extract()
        data = data_handler.load_data(self.csv_file_name)

        # Step 2: Preprocess data
        preprocessor = Preprocessor(data)
        X_train, X_test, y_train, y_test = preprocessor.preprocess()

        # Step 3: Build the model
        lstm_model = LSTMModel(input_shape=(X_train.shape[1], X_train.shape[2]))

        # Step 4: Train the model
        history = lstm_model.train(X_train, y_train, X_test, y_test, epochs=50, batch_size=32)

        # Step 5: Evaluate the model
        lstm_model.evaluate(X_test, y_test)

        # Step 6: Visualize results
        Visualizer.plot_training_history(history)

        # Step 7: Save the model
        lstm_model.save_model('sleep_apnea_lstm_model.h5')
