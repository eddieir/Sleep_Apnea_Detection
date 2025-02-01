from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

class Preprocessor:
    def __init__(self, data):
        self.data = data

    def preprocess(self):
        print("Preprocessing data...")
        # Drop irrelevant columns and handle missing values
        self.data = self.data.dropna()
        
        # Assuming the dataset has relevant columns: 'OxygenLevels', 'HeartRate', 'RespiratoryRate', 'MovementIndex', 'Apnea'
        features = ['OxygenLevels', 'HeartRate', 'RespiratoryRate', 'MovementIndex']
        target = 'Apnea'

        X = self.data[features]
        y = self.data[target]

        # Standardize features
        scaler = StandardScaler()
        X = scaler.fit_transform(X)

        # Reshape data for LSTM input (samples, timesteps, features)
        X = X.reshape((X.shape[0], 1, X.shape[1]))

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test
