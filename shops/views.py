from django.http.response import JsonResponse
import matplotlib.pyplot as plt
from io import BytesIO
from django.shortcuts import render
import base64
from .dataset import allages, allprods, vesages, vesprods, pizages, pizprods
from collections import Counter
from scipy.stats import beta
import numpy as np
import matplotlib
matplotlib.use('Agg')
# Create your views here.
def shop(request):
    if request.method == "POST":
        p1l = int(request.POST.get('p1likes'))
        p1d = int(request.POST.get('p1dislikes'))
        p1o = int(request.POST.get('p1orders'))
        p2l = int(request.POST.get('p2likes'))
        p2d = int(request.POST.get('p2dislikes'))
        p2o = int(request.POST.get('p2orders'))
        p3l = int(request.POST.get('p3likes'))
        p3d = int(request.POST.get('p3dislikes'))
        p3o = int(request.POST.get('p3orders'))
        p4l = int(request.POST.get('p4likes'))
        p4d = int(request.POST.get('p4dislikes'))
        p4o = int(request.POST.get('p4orders'))
        def shop_recommend(shop):
            """Recommends what has to be Sold."""
            products = {
                    'MYSHOP': {'Product 1':[p1l,p1d,p1o], 'Product 2':[p2l,p2d,p2o],
                    'Product 3':[p3l,p3d,p3o], 'Product 4':[p4l,p4d,p4o]},
                    
                }
            def Beta(alpha, abeta):
                """ Finds the p-value of the product."""
                from scipy.stats import beta
                mean, var, skew, kurt = beta.stats(alpha, abeta, moments='mvsk')
                return mean

            def sortdict(dicname):
                """ Sorts a dictionary in Descending Order. """
                return dict(sorted(dicname.items(), key=lambda b: b[-1], reverse=True))

            data    = products[shop]
            pdict   = dict()
            orders  = dict()
            for key,val in data.items():
                pdict[key]  = Beta(val[0],val[1])
                orders[key] = val[2]

            recommend = dict()
            for prod in sortdict(pdict).keys():
                recommend[prod] = list(sortdict(orders).keys()).index(prod) + 1


            flag = dict()
            for pro,pos in recommend.items():
                if pos == 1:
                    """First 2 Leading to be bought and most preffered."""
                    flag[pro] = 0

            """ Among best four preffered. """
            for bb in sortdict(pdict).keys():
                    if bb not in flag.keys():
                        flag[bb] = 1
            return flag
        recoms = shop_recommend('MYSHOP')

        x = np.linspace(0, 1.0, 100)
        p1 = beta.pdf(x, p1l, p1d)
        p2 = beta.pdf(x, p2l, p2d)
        p3 = beta.pdf(x, p3l, p3d)
        p4 = beta.pdf(x, p4l, p4d)
        plt.plot(x, p1, "b-", x, p2, f"r-*", x, p3, "g*",x, p4,'m+')
        plt.xlabel('Probability', fontsize='15')
        plt.ylabel('Density', fontsize='15')
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        graphic = base64.b64encode(image_png)
        graphic = graphic.decode('utf-8')
        plt.close()
        
        context = {'graphic': graphic, 'results':True, 'data': recoms, 'title':'Shop Recommendation.'}
    else:
        context = {'title':'Shop Recommendation.'}
    
    template = 'shops.html'
    return render(request, template, context)


def customer(request):
    shops = ['Vespa Farms','Pizza Hut']
    if request.method == 'POST':
        age = int(request.POST.get('age'))
        shopie = request.POST.get('myshop')
        if str(shopie) == 'Pizza Hut':
            ages = pizages
            products = pizprods
        else:
            ages = vesages
            products = vesprods
        age15bel = []; age1620  = []; age2125  = []
        age2630  = []; age3135  = []; age3640  = []
        age4145  = []; age46abo = []
        for i in range(0, len(ages)):
            if ages[i] <= 15:
                age15bel.append(products[i])
            elif 16 <= ages[i] <= 20:
                age1620.append(products[i])
            elif 21 <= ages[i] <= 25:
                age2125.append(products[i])
            elif 26 <= ages[i] <= 30:
                age2630.append(products[i])
            elif 31 <= ages[i] <= 35:
                age3135.append(products[i])
            elif 36 <= ages[i] <= 40:
                age3640.append(products[i])
            elif 41 <= ages[i] <= 45:
                age4145.append(products[i])
            else:
                age46abo.append(products[i])
        
        if age <= 15:
            label = '0-15'
            group = age15bel
        elif 16 <= age <= 20:
            label = '16-20'
            group = age1620
        elif 21 <= age <= 25:
            label = '21-25'
            group  = age2125
        elif 26 <= age <= 30:
            label = '26-30'
            group = age2630
        elif 31 <= age <= 35:
            label = '31-35'
            group = age3135
        elif 36 <= age <= 40:
            label = '36-40'
            group = age3640
        elif 41 <= age <= 45:
            label = '41-45'
            group = age4145
        else:
            label = '46+'
            group = age46abo

        prodhists = dict(Counter(group))
        bidhaa    = list(prodhists.keys())
        orders    = list(prodhists.values())
        fig, ax   = plt.subplots()
        ax.bar(bidhaa, orders, 0.8, color='#17B897')
        ax.set_ylabel('Orders')
        ax.set_title(f'Products Vs Orders {label}')
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        graphic = base64.b64encode(image_png)
        graphic = graphic.decode('utf-8')
        plt.close()
        #plt.clf()


        """ Customer Recommendations."""
        context = {'shops': shops, 'results': True,'graphic': graphic}
    else:
        context = {'shops': shops, 'results': False}
    template = 'customers.html'
    return render(request, template, context)

def vespa(request):
    template = 'vespa.html'
    context = {'Shopps': 'Vespas', 'choices' :['Shops','Customers']}
    return render(request, template, context)



import keras
from keras.preprocessing import image
from keras.applications import imagenet_utils
import tensorflow
import os.path
from model_project.settings import  MEDIA_ROOT
img_path = MEDIA_ROOT + '\\images\\'
from django.conf import settings
from .models import Detection, Categorise
def object_predict(request):
    detects = Detection.objects.all()
    if request.method == 'POST':
        imname = str(request.POST.get('mydet'))
        imageurl = str(Detection.objects.filter(name=imname).first().image.url)[13:]
        mobile = tensorflow.keras.applications.mobilenet.MobileNet()
        def prepare_image(file):
            img_path = MEDIA_ROOT + '\\images\\'
            img = image.load_img(img_path + file, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array_expanded_dims = np.expand_dims(img_array, axis=0)
            return keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)
    
        preprocessed_image = prepare_image(f'{imageurl}')
        predictions = mobile.predict(preprocessed_image)
        results = imagenet_utils.decode_predictions(predictions)

        def modify(line):
            import re
            line = re.sub('[_]', ' ', line)
            return line.title()
        analysis = {}
        for i in range(0, len(results[0])):
            analysis[modify(results[0][i][1])] = results[0][i][2]
        confidence = str(int(round(float(list(analysis.values())[0]), 2)*100))
        detected = list(analysis.keys())[0]

        if Categorise.objects.filter(name=detected).exists():
            flag =  'Reject'
        else:
            flag = 'Allow'
        context = {'data': analysis, 'detects':detects, 'results':True ,'detected':detected, 'confidence': confidence}
    else:
        context = {'detects':detects, 'results': False}
    template = 'predict.html'
    return render(request, template, context)


from django.shortcuts import render, redirect
from .forms import *
def upload_image(request):
    if request.method == 'POST':
        form = DetectionForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('predict')
    else:
        form = DetectionForm()
    return render(request, 'input.html', {'form' : form})