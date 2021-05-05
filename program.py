import statistics
import random
import pandas as  pd
import plotly_express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go


file1 = pd.read_csv('data.csv')
data = df['reading_time'].tolist()

dataset = []
def randomdata():
    for i in range(0,100):
        index = random.randint(0,(len(data) - 1))
        value = data[index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def showgraph(meanlist):
    datframe = meanlist
    mean = statistics.mean(dataframe)
    graph = ff.create_distplot([dataframe], ['Result'], show_hist = False)
    graph.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = 'lines', name = 'Mean'))
    graph.show()

def setup():
    meanlist = []
    for i in range(0,1000):
        setofmeans = randomdata()
        meanlist.append(setofmeans)
    showfig(meanlist)
    mean = statistics.mean(meanlist)
    print('mean of sampling distribution' ,mean)
    sd = statistics.stdev(data)
    print(sd)

setup()

