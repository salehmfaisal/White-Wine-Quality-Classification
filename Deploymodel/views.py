# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import pickle


def home(request):
    return render(request, "home.html")

def result(request):
    model= pickle.load(open('random_forest_classifier_model.pkl', 'rb'))
    
    
    lis=[]
    
    lis.append(request.GET['fixed acidity'])
    lis.append(request.GET['volatile acidity'])
    lis.append(request.GET['citric acid'])
    lis.append(request.GET['residual sugar'])
    lis.append(request.GET['chlorides'])
    lis.append(request.GET['total sulfur dioxide'])
    lis.append(request.GET['density'])
    lis.append(request.GET['sulphates'])
    lis.append(request.GET['alcohol'])
    
    
    
    
    ans=model.predict([lis])
    
    return render(request, "result.html", {'ans': ans, 'lis': lis})