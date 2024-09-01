from flask import Flask, request, jsonify, render_template
import pickle 
import numpy as np

class KNN:
    
    def __init__(self):
        self.distance = None
        self.vector_pata_hai = None
        self.vector_ke_result = None
        self.hamara_vector = None

    def fit(self, x_train, y_train):
        self.vector_pata_hai = np.array(x_train)
        self.vector_ke_result = np.array(y_train) 

    def predict(self, test):
        self.hamara_vector = np.array(test)
        distance_vector = self.vector_pata_hai - self.hamara_vector
        distance = np.sum(distance_vector**2, axis=1)
        self.distance = np.sqrt(distance)
        minimum = self.distance.min()

        output = []
        for index, dist in enumerate(self.distance):
            if dist == minimum:
                output.append(self.vector_ke_result[index])  # Index correctly

        return np.array(output)  # Convert output list to numpy array

model_path='knn_model.pkl'
with open(model_path,'rb') as file:
    model = pickle.load(file) 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('project.html')

@app.route('/predict',  methods=['POST'])
def predict():

    def vectorize(front_array):
        categories = ['AI/ML', 'Remote Sensing', 'IoT', 'Embedded Systems', 'Data Analysis', 'Data Science',
                  'Environmental Science', 'Blockchain', 'Security', 'Medical Imaging', 'Robotics', 'Game Development',
                  '3D Modeling', 'nan']
        init_vector = [0] * len(categories)

        for element in front_array:
         if element in categories:
            index = categories.index(element)
            init_vector[index] = 1

        return init_vector[0:13]
        
    selected_values = {
        'dropdown1': request.form.get('dropdown1'),
        'dropdown2': request.form.get('dropdown2'),
        'dropdown3': request.form.get('dropdown3'),
        'dropdown4': request.form.get('dropdown4')
    }

    options_map = {
        "option0": "none",
        "option1": "AI/ML",
        "option2": "Remote Sensing",
        "option3": "IoT",
        "option4": "Embedded Systems",
        "option5": "Data Analysis",
        "option6": "Data Science",
        "option7": "Environmental Science",
        "option8": "Blockchain",
        "option9": "Security",
        "option10": "Medical Imaging",
        "option11": "Robotics",
        "option12": "Game Development",
        "option13": "3D Modelling"
    }

    front_array = [options_map.get(value, "Unknown Tag") for value in selected_values]


    
    int_features = vectorize(front_array)
    final_features = [np.array(int_features)]

    prediction = model.predict(final_features)
    output = prediction[:] 

    return render_template('project.html', prediction_texts ='Prediction:{}'.format(output))

@app.route('/')
def home():
    array_length = len(output)
    return render_template('projects.html', items=items, array_length=array_length)

if __name__ == "_main__":
    app.run(debug=True)
