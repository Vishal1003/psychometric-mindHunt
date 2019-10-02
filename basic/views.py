from django.shortcuts import render
from .forms import TestForm
import numpy as np
from sklearn.cluster import KMeans
import random
import matplotlib.pyplot as plt

def yon():
    a=random.choice([0,1])
    return a

X = np.array([[yon() for x in range(10)] for x in range(300)])
print(X)
kmeans = KMeans(n_clusters=5)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)   


def home(request):
    return render(request, 'basic/home.html')

def decision(num):
    base ="you belong to"
    if num ==1:
        return base+" leaders"
    elif num ==2:
        return base+" Emotionals"
    elif num ==3:
        return base+" Hard Workers"
    elif num ==4:
        return base+" Smart Workers"
    else:
        return base+" visionaries"

def test(request):

    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            Q1 = form.cleaned_data['Q1']
            Q2 = form.cleaned_data['Q2']
            Q3 = form.cleaned_data['Q3']
            Q4 = form.cleaned_data['Q4']
            Q5 = form.cleaned_data['Q5']
            Q6 = form.cleaned_data['Q6']
            Q7 = form.cleaned_data['Q7']
            Q8 = form.cleaned_data['Q8']
            Q9 = form.cleaned_data['Q9']
            Q10 = form.cleaned_data['Q10']

            tlist= (int(Q1),int(Q2),int(Q3),int(Q4),int(Q5),int(Q6),int(Q7),int(Q8),int(Q9),int(Q10))
            error =[]
            for cet in centroids:
                error.append(sum(np.square(np.subtract(cet,tlist)))) 
            result=error.index(min(error))
            print(result)
        return render(request,'basic/thankyou.html',{'result': decision(result)})
    



    form = TestForm()
    return render(request,'basic/form.html',{'form':form})

