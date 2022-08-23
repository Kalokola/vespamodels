<samp>

# [Vespa Stores](http://vespas.herokuapp.com/shop/)

[![Made in Tanzania](https://img.shields.io/badge/made%20in-tanzania-008751.svg?style=flat-square)](https://github.com/Tanzania-Developers-Community/made-in-tanzania)

This deployment is a part of the dlab bootcamp project, we explored recommendation systems in ecommerce stores and built a web store. Features supported are the Recommendar Sytems for Customer Side and Shop Side.

## NB
The neural net part isn't included the app since heroku  supports a slug size less than 500MiBs, including the neural net part peaks up to 1023MiBs.

## Ho to use locally.
```bash
$ git clone https://github.com/kalokola/vespamodels.git
$ cd vespamodels
$ pip3 install -r requiremnets.txt
$ python3 manage.py runserver
```
You can now view the local project on your device at [127.0.0.1:8000](http://127.0.0.1:8000/)


# Customer Side
This part shows how algorithms recommend product to users basing on their age at their first login. **Age Group Visualisations** are shown on the graphs. 



# Shop Side.
- A beta distribution was used to sort and suggest products on the home feed line basing on popularity of products and user generated data like number of likes and dislikes per product.

- Also, used content based approach to filter the comments on a given post to extract useful informations for recommendation like age group, seasons, locality, positivity of feedacks.

- This part had a Product Image Fraud Detection where we fine tunned a Keras lightweight deep learning model called MobileNet 72MB trained on 17M objects. This helped suspend accounts in our e-commerce store incase they upload products that they havent subscribed to post in te store for instance if a grocery store uploads a gun. They are suspended.

## Access: [vespas](http://vespas.herokuapp.com/shop/)


## Credits
1. [kalokola](https://github.com/kalokola)
2. Ashura, Elizabeth, Dorothy, Kalokola
3. DLAB Staff and Inspired Ideas
</samp>
