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
       
        fname = request.POST['fname']
        number = int(request.POST['number'])
        age = int(request.POST['age'])
        Q1 = int(request.POST['Q1'])
        Q2 = int(request.POST['Q2'])
        Q3 =int(request.POST['Q3'])
        Q4 = int(request.POST['Q4'])
        Q5 = int(request.POST['Q5'])
        Q6 = int(request.POST['Q6'])
        Q7 = int(request.POST['Q7'])
        Q8 = int(request.POST['Q8'])
        Q9 = int(request.POST['Q9'])
        Q10 = int(request.POST['Q10'])

        tlist= (int(Q1),int(Q2),int(Q3),int(Q4),int(Q5),int(Q6),int(Q7),int(Q8),int(Q9),int(Q10))
        error =[]
        for cet in centroids:
            error.append(sum(np.square(np.subtract(cet,tlist)))) 
        result=error.index(min(error))
        print(result)
        return render(request,'basic/thankyou.html',{'result': decision(result),'name':fname, 'number':number, 'age': age})
    



    form = TestForm()
    return render(request,'basic/form2.html',{'form':form})

# on changing the form2 to form we will get original.