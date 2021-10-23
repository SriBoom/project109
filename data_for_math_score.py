import csv
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
math_data=df["math score"].tolist()

mean=statistics.mean(math_data)
median=statistics.median(math_data)
mode=statistics.mode(math_data)
std_deviation=statistics.stdev(math_data)

print("mean,median,mode, and standard deviation of height is {}, {}, {}, {}".format(mean,median,mode,std_deviation))

first_std_dev_start,first_std_dev_end = mean-std_deviation,mean+std_deviation
second_std_dev_start,second_std_dev_end = mean-(2*std_deviation),mean+(2*std_deviation)
third_std_dev_start,third_std_dev_end = mean-(3*std_deviation),mean+(3*std_deviation)

fig=ff.create_distplot([math_data], ["Math Scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_dev_start, first_std_dev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_dev_start, second_std_dev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()


list_of_data_within_1_std_deviation = [result for result in math_data if result > first_std_dev_start and result < first_std_dev_end]
list_of_data_within_2_std_deviation = [result for result in math_data if result > second_std_dev_start and result < second_std_dev_end]
list_of_data_within_3_std_deviation = [result for result in math_data if result > third_std_dev_start and result < third_std_dev_end]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(math_data)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(math_data)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(math_data)))
