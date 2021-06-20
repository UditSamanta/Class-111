import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

dataframe = pd.read_csv('School3.csv')
data = dataframe['Math_score'].tolist()
pop_mean = statistics.mean(data)
pop_div = statistics.stdev(data)
print('pop_mean = '+str(pop_mean))
print('pop_div = '+str(pop_div))

def random_sets_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0, 1000):
    means = random_sets_mean(100)
    mean_list.append(means)
    
samplingStd = statistics.stdev(mean_list)
samplingMean = statistics.mean(mean_list)
print('samplingStd = '+str(samplingStd))
print('samplingMean = '+str(samplingMean))

first_std_deviation_start, first_std_deviation_end = samplingMean - samplingStd, samplingMean + samplingStd
second_std_deviation_start, second_std_deviation_end = samplingMean - (samplingStd*2), samplingMean + (samplingStd*2)
third_std_deviation_start, third_std_deviation_end = samplingMean - (samplingStd*3), samplingMean + (samplingStd*3)

#Finding the mean of the students who gave extra time of school1
dataframe = pd.read_csv('School_3_Sample.csv')
data = dataframe['Math_score'].tolist()
mean1 = statistics.mean(data)
figure = ff.create_distplot([mean_list], ['Student Marks'], show_hist = False)
figure.add_trace(go.Scatter(x = [samplingMean, samplingMean], y = [0, 0.17], mode = 'lines', name = 'mean'))
figure.add_trace(go.Scatter(x = [mean1, mean1], y = [0, 0.17], mode = 'lines', name = 'meanOfMathLabsStudents'))
figure.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0, 0.17], mode = 'lines', name = 'First Standard Deviation'))
figure.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0, 0.17], mode = 'lines', name = 'Second Standard Deviation'))
figure.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end], y = [0, 0.17], mode = 'lines', name = 'Third Standard Deviation'))
figure.show()

z_score = (mean1 - samplingMean)/samplingStd
print(z_score)





















