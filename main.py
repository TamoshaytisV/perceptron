from data import data as dataset


learning_rate = 0.000001
threshold = learning_rate / 0.1


def predict(input_val, weight):
    return input_val * weight


def reverse_predict(input_val, weight):
    return input_val / weight


def train(data):
    epohs = 0
    weight = 0
    errors = []

    while not errors or max(errors) > threshold:
        errors = []
        for row in data:
            expected = row[-1]
            input_val = row[0]
            result = predict(input_val, weight)
            error = round(result - expected, 40) ** 2
            errors.append(error)
            weight = weight + learning_rate * error
        epohs += 1
    return weight, epohs


weight, __ = train(dataset)

print('1 km = ', predict(1, weight))
print('5.5 km = ', predict(5.5, weight))
print('10 km = ', predict(10, weight))

print('1 mile = ', reverse_predict(1, weight))
print('5.5 miles = ', reverse_predict(5.5, weight))
print('10 miles = ', reverse_predict(10, weight))
