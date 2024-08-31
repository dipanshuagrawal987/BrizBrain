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
