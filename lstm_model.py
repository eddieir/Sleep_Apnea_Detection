from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

class LSTMModel:
    def __init__(self, input_shape):
        self.input_shape = input_shape
        self.model = self.build_model()

    def build_model(self):
        print("Building LSTM model...")
        model = Sequential([
            LSTM(128, input_shape=self.input_shape, return_sequences=True, activation='relu'),
            Dropout(0.3),
            LSTM(64, activation='relu'),
            Dropout(0.3),
            Dense(32, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        
        model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])
        print(model.summary())
        return model

    def train(self, X_train, y_train, X_val, y_val, epochs=50, batch_size=32):
        print("Training model...")
        history = self.model.fit(
            X_train, y_train,
            validation_data=(X_val, y_val),
            epochs=epochs,
            batch_size=batch_size,
            verbose=1
        )
        return history

    def evaluate(self, X_test, y_test):
        print("Evaluating model...")
        y_pred = (self.model.predict(X_test) > 0.5).astype(int)
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))
        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

    def save_model(self, filepath):
        self.model.save(filepath)
        print(f"Model saved as '{filepath}'.")
