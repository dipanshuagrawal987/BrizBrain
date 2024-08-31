class KNN:
    
    def __init__(self):
        self.distance = None
        self.vector_pata_hai = None
        self.vector_ke_result = None
        self.hamara_vector = None

    def fit(self, x_train, y_train):
        # Store training vectors and corresponding results
        self.vector_pata_hai = np.array(x_train)
        self.vector_ke_result = np.array(y_train)  # Corrected to match the shape of x_train

    def predict(self, test):
        # Convert the test vector to a numpy array
        self.hamara_vector = np.array(test)

        # Calculate the difference vectors
        distance_vector = self.vector_pata_hai - self.hamara_vector

        # Calculate squared distances manually
        distance = np.sum(distance_vector**2, axis=1)

        # Compute Euclidean distances
        self.distance = np.sqrt(distance)

        # Find the minimum distance value
        minimum = self.distance.min()

        # Collect results corresponding to the minimum distance
        output = []
        for index, dist in enumerate(self.distance):
            if dist == minimum:
                output.append(self.vector_ke_result[index])  # Index correctly

        return np.array(output)  # Convert output list to numpy array
