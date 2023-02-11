from flask import Flask, render_template 

app = Flask(__name__)


Bestsellers = {
    1 : {
        'name' : 'Book #1',
        'description' : 'some description',
        'price' : '$56',
        'image' : 'book1.jpeg',        
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1225,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
                
    },
    2 : {
        'name' : 'Book #2',
        'description' : 'some description',
        'price' : '$23',
        'image' : 'book2.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1226,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
        
    },
    3 : {
        'name' : 'Book #3',
        'description' : 'some description',
        'price' : '$33',
        'image' : 'book3.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1227,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
        
    },
    4 : {
        'name' : 'Book #4',
        'description' : 'some description',
        'price' : '$55',
        'image' : 'book4.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1228,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
        
    },
    5 : {
        'name' : 'Book #5',
        'description' : 'some description',
        'price' : '$12',
        'image' : 'book5.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1229,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
        
    },
    6 : {
        'name' : 'Book #6',
        'description' : 'some description',
        'price' : '$23',
        'image' : 'book6.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1230,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
    },
}    
recommended_items1 = {  
    
    1 : {
        'name' : 'Book #7',
        'description' : 'some description',
        'price' : '$77',
        'image' : 'book7.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1231,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
        
    },
    2 : {
        'name' : 'Book #8',
        'description' : 'some description',
        'price' : '$74',
        'image' : 'book8.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1232,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
        
    },
    3 : {
        'name' : 'Book #9',
        'description' : 'some description',
        'price' : '$27',
        'image' : 'book9.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1233,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
    },
} 
recommended_items2 = {        
    
    1 : {
        'name' : 'Book #10',
        'description' : 'some description',
        'price' : '$53',
        'image' : 'book10.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1234,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
        
    },
    2 : {
        'name' : 'Book #11',
        'description' : 'some description',
        'price' : '$75',
        'image' : 'book11.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1235,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
        
    },
    3 : {
        'name' : 'Book #12',
        'description' : 'some description',
        'price' : '$16',
        'image' : 'book12.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1236,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
        
    },
}



CATEGORY = ['3D Kitab','Akademik','Bədii','Bizness','Detektiv']




FEATURES_ITEMS = {
    1 : {
        'name' : 'Book #1',
        'description' : 'some description',
        'price' : '$56',
        'image' : 'book1.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1225,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
        
    },
    2 : {
        'name' : 'Book #2',
        'description' : 'some description',
        'price' : '$23',
        'image' : 'book2.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1226,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
        
    },
    3 : {
        'name' : 'Book #3',
        'description' : 'some description',
        'price' : '$33',
        'image' : 'book3.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1227,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
        
    },
    4 : {
        'name' : 'Book #4',
        'description' : 'some description',
        'price' : '$55',
        'image' : 'book4.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1228,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
        
    },
    5 : {
        'name' : 'Book #5',
        'description' : 'some description',
        'price' : '$12',
        'image' : 'book5.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1229,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
        
    },
    6 : {
        'name' : 'Book #6',
        'description' : 'some description',
        'price' : '$23',
        'image' : 'book6.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1230,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
    },
    7 : {
        'name' : 'Book #7',
        'description' : 'some description',
        'price' : '$77',
        'image' : 'book7.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1231,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
        
    },
    8 : {
        'name' : 'Book #8',
        'description' : 'some description',
        'price' : '$74',
        'image' : 'book8.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1232,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
        
    },
    9 : {
        'name' : 'Book #9',
        'description' : 'some description',
        'price' : '$27',
        'image' : 'book9.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1233,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
    },
    10 : {
        'name' : 'Book #10',
        'description' : 'some description',
        'price' : '$53',
        'image' : 'book10.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1234,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
        
    },
    11 : {
        'name' : 'Book #11',
        'description' : 'some description',
        'price' : '$75',
        'image' : 'book11.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1235,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
        
    },
    12 : {
        'name' : 'Book #12',
        'description' : 'some description',
        'price' : '$16',
        'image' : 'book12.jpeg',
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Web_ID': 1236,
        'Review' : 'My Review',
        'Brand' : 'E-SHOPPER'
        
    },
}




@app.route("/home")
def index():
    return render_template('index.html', Books = Bestsellers , recommended_items1  = recommended_items1, recommended_items2  = recommended_items2 , CATEGORY = CATEGORY)

@app.route("/home/<int:id>")
def index_detail(id):
    return render_template('book.html', CATEGORY = CATEGORY, FEATURES_ITEMS = Bestsellers[id], recommended_items1 = recommended_items1, recommended_items2 = recommended_items2)

@app.route("/reco1/<int:id>")
def reco1_detail(id):
    return render_template('book.html', CATEGORY = CATEGORY,  FEATURES_ITEMS = recommended_items1[id], recommended_items1 = recommended_items1, recommended_items2 = recommended_items2)

@app.route("/reco2/<int:id>")
def reco2_detail(id):
    return render_template('book.html', CATEGORY = CATEGORY,  FEATURES_ITEMS = recommended_items2[id], recommended_items1 = recommended_items1, recommended_items2 = recommended_items2)


@app.route("/product")
def product():
    return render_template('product.html', FEATURES_ITEMS = FEATURES_ITEMS , CATEGORY = CATEGORY)


@app.route("/product/<int:id>")
def product_detail(id):
    return render_template('book.html', CATEGORY = CATEGORY, FEATURES_ITEMS = FEATURES_ITEMS[id], recommended_items1 = recommended_items1, recommended_items2 = recommended_items2)

