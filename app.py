from flask import Flask, render_template, url_for, request, redirect
import shutil
import os

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html', data='')


@app.route('/enterit',methods = ['POST', 'GET'])
def enterit():
   if request.method == 'POST':
      fn = request.form['nm']
      if len(str(fn)) == 0:
        return render_template('index.html', data="Enter any fruit name!")
      else:
        return redirect(url_for('fruit',name = fn))
   else:
      fn = request.args.get('nm')
      return redirect(url_for('fruit',name = fn))

@app.route('/fruit/<name>')
def fruit(name):
    lst = ['Lemons', 'Lemon Juice Raw', 'Lemon Juice From Concentrate Canned Or Bottled', 
    'Lemon Peel Raw', 'Prickly Pears', 'Plums Dried (Prunes) Stewed Without Added Sugar', 
    'Plums Dried (Prunes) Stewed With Added Sugar', 'Shredded Coconut Meat (Sweetened)', 
    'Pummelo', 'Raspberries', 'Raspberries Canned Red Heavy Syrup Pack Solids And Liquids',
     'Raspberries Frozen Red Sweetened', 'Rhubarb', 'Sapodilla', 'Mamey Sapote', 'Soursop', 
     'Strawberries', 'Tamarinds',
      'Fruit Salad (Pineapple And Papaya And Banana And Guava) Tropical Canned Heavy Syrup Solids And Liquids',
       'Watermelon', 'Maraschino Cherries (Canned)', 'Pineapple Canned Juice Pack Drained', 
       'Apricots Canned Heavy Syrup Drained', 'Cherries Sour Canned Water Pack Drained',
        'Cherries Sweet Canned Pitted Heavy Syrup Drained',
         'Apple Juice Canned Or Bottled Unsweetened With Added Ascorbic Acid',
         'Applesauce Canned Unsweetened With Added Ascorbic Acid',
          'Applesauce Canned Sweetened With Salt', 
          'Pink Grapefruit Juice',
           'Apple Juice Frozen Concentrate Unsweetened Diluted With 3 Volume Water With Added Ascorbic Acid',
            'Bartlett Pears', 'Red Anjou Pears', 'Bosc Pear', 'Green Anjou Pear', 'Prune Puree',
             'Candied Fruit', 'Abiyuch', 'Rowal', 'Guava Nectar Canned With Added Ascorbic Acid', 
             'Mango Nectar Canned', 'Tamarind Nectar Canned', 'Pomegranate Juice Bottled', 
             'Nance Canned Syrup Drained', 'Nance Frozen Unsweetened', 'Naranjilla (Lulo) Pulp Frozen Unsweetened', 
             'Horned Melon (Kiwano)', 'Orange Pineapple Juice Blend', 'Fuji Apples', 
             'Orange Juice Chilled Includes From Concentrate With Added Calcium And Vitamins A D E',
              'Fruit Juice Smoothie Naked Juice Mighty Mango', 'Fruit Juice Smoothie Naked Juice Green Machine', 
              'Fruit Juice Smoothie Bolthouse Farms Berry Boost', 'Fruit Juice Smoothie Bolthouse Farms Green Goodness', 
              'Fruit Juice Smoothie Bolthouse Farms Strawberry Banana', 
              'Apple Juice Canned Or Bottled Unsweetened With Added Ascorbic Acid Calcium And Potassium', 
              'Lemon Juice From Concentrate Bottled Concord',
               'Lemon Juice From Concentrate Bottled Real Lemon', 'Cranberry Sauce Whole Canned Ocean Spray',
                'Cranberry Sauce Jellied Canned Ocean Spray', 
                'Ruby Red Grapefruit Juice Blend (Grapefruit Grape Apple) Ocean Spray Bottled With Added Vitamin C',
                 'Cranberry Juice Unsweetened', 'Java Plum', 'Jujube', 'Dried Jujube', 
                 'Kiwifruit', 'Kumquats', 'Limes', 'Lime Juice', 'Lime Juice Canned Or Bottled Unsweetened', 'Dried Blueberries (Sweetened)', 
                 'Prunes Canned Heavy Syrup Pack Solids And Liquids', 'Prunes (Low-Moisture)', 
                 'Prunes Dehydrated (Low-Moisture) Stewed', 'Prunes (Dried Plums)', 'Quinces', 
                 'Golden Seedless Raisins', 'Raisins', 'Raisins Seeded', 'Rambutan Canned Syrup Pack', 
                 'Rhubarb Frozen Uncooked', 'Rhubarb Frozen Cooked With Sugar', 'Roselle', 'Rose Apples', 
                 'Strawberries Canned Heavy Syrup Pack Solids And Liquids', 'Frozen Strawberries',
                  'Strawberries Frozen Sweetened Sliced', 'Sugar Apples', 'Feijoa', 'Asian Pears', 
                  'Fruit Cocktail Canned Heavy Syrup Drained', 'Blueberries Canned Light Syrup Drained',
                   'Blueberries Wild Canned Heavy Syrup Drained', 'Peaches Canned Heavy Syrup Drained',
                    'Pears Canned Heavy Syrup Drained', 'Plums Canned Heavy Syrup Drained',
                     'Tangerines (Mandarin Oranges) Canned Juice Pack Drained', 'Peach Nectar Canned With Added Ascorbic Acid',
                      'Pear Nectar Canned With Added Ascorbic Acid', 'Pineapple Juice Canned Or Bottled Unsweetened With Added Ascorbic Acid',
                       'Apple Juice Frozen Concentrate Unsweetened Undiluted With Added Ascorbic Acid',
                        'Grapefruit Juice White Bottled Unsweetened Ocean Spray', 'Jackfruit Canned Syrup Pack',
                         'Medjool Dates', 'Durian', 'Pineapple (Traditional)', 'Pineapple Raw Extra Sweet Variety', 
                         'Clementines', 'Guanabana Nectar Canned', 'Juice Apple And Grape Blend With Added Ascorbic Acid',
                          'Juice Apple Grape And Pear Blend With Added Ascorbic Acid And Calcium', 'Plantains Green Fried', 
                          'Fried Yellow Plantains', 'Red Delicious Apples', 'Golden Delicious Apples', 'Granny Smith Apples',
                           'Gala Apples', 'Pineapple Juice Canned Not From Concentrate Unsweetened With Added Vitamins A C And E', 
                           'Fortified Fruit Juice Smoothie', 'Grape Juice Canned Or Bottled Unsweetened With Added Ascorbic Acid And Calcium',
                            'Fruit Juice Smoothie Odwalla Original Superfood', 'Frozen Raspberries', 'Guava Nectar With Sucralose Canned', 
                            'Kiwifruit Zespri Sungold Raw', 'Cranberry Juice Blend 100% Juice Bottled With Added Vitamin C And Calcium',
                             'Fruit Juice Smoothie Odwalla Strawberry Banana', 'Fruit Juice Smoothie Naked Juice Strawberry Banana',
                              'Litchis', 'Dried Litchis', 'Loganberries (Frozen)', 'Longans', 'Mangosteen Canned Syrup Pack', 
                              'Dried Sweetened Mango', 'Cantaloupe Melons', 'Casaba Melon', 'Olives', 'Jumbo Olives', 'Green Olives', 'Oranges',
                               'Orange Juice', 'Canned Orange Juice', 'Orange Juice From Concentrate', 'Orange Juice With Added Calcium And Vitamin D',
                                'Orange Juice Frozen Concentrate Unsweetened Diluted With 3 Volume Water', 'Orange Peel Raw', 
                                'Orange-Grapefruit Juice Canned Or Bottled Unsweetened', 'Tangerines', 'Tangerines (Mandarin Oranges) Canned Juice Pack',
                                 'Papaya Nectar Canned', 'Passion Fruit (Granadilla)', 'Purple Passion Fruit Juice', 'Yellow Passion Fruit Juice', 
                                 'Peaches Canned Light Syrup Pack Solids And Liquids', 'Peaches Canned Heavy Syrup Pack Solids And Liquids',
                                  'Peaches Canned Extra Heavy Syrup Pack Solids And Liquids', 'Peaches Spiced Canned Heavy Syrup Pack Solids And Liquids',
                                   'Peaches Dried Sulfured Stewed With Added Sugar', 'Peaches Frozen Sliced Sweetened', 'Peach Nectar Canned Without Added Ascorbic Acid',
                                    'Pears', 'Pears Canned Water Pack Solids And Liquids', 'Pears Canned In Syrup', 'Dried Pears', 
                                    'Pears Dried Sulfured Stewed Without Added Sugar', 'Pears Dried Sulfured Stewed With Added Sugar', 'Pineapple',
                                     'Pineapple Canned Water Pack Solids And Liquids', 'Pineapple Canned Juice Pack Solids And Liquids', 
                                     'Pineapple Canned Light Syrup Pack Solids And Liquids', 'Pineapple Juice Frozen Concentrate Unsweetened Diluted With 3 Volume Water',
                                      'Pitanga', 'Plantains', 'Plantains Cooked', 'Plums Canned Purple Heavy Syrup Pack Solids And Liquids',
                                       'Plums Canned Purple Extra Heavy Syrup Pack Solids And Liquids', 'Pomegranates', 'Dried Longans', 'Loquats',
                                        'Mammy Apple', 'Mangos', 'Honeydew Melon', 'Melon Balls', 'Mulberries', 'Nectarines', 'Oheloberries',
                                         'California Valencia Oranges', 'Navel Oranges', 'Florida Oranges', 'Oranges Raw With Peel', 'Orange Juice With Added Calcium', 
                                         'Orange Juice Frozen Concentrate Unsweetened Diluted With 3 Volume Water With Added Calcium',
                                          'Orange Juice Frozen Concentrate Unsweetened Undiluted With Added Calcium', 'Orange Juice Frozen Concentrate Unsweetened Undiluted', 
                                          'Tangerines (Mandarin Oranges) Canned Light Syrup Pack', 'Tangerine Juice', 'Papaya', 'Papaya Canned Heavy Syrup Drained', 'Yellow Peaches', 
                                          'Peaches Canned Water Pack Solids And Liquids', 'Peaches Canned Juice Pack Solids And Liquids', 'Peaches Canned Extra Light Syrup Solids And Liquids', 'Dried Peaches (Low-Moisture)',
                                           'Peaches Dehydrated (Low-Moisture) Sulfured Stewed', 'Dried Peaches', 'Peaches Dried Sulfured Stewed Without Added Sugar', 'Pears Canned Juice Pack Solids And Liquids',
                                            'Pears Canned Extra Light Syrup Pack Solids And Liquids', 'Pears Canned Light Syrup Pack Solids And Liquids',
                                             'Pears Canned Heavy Syrup Pack Solids And Liquids', 'Pear Nectar Canned Without Added Ascorbic Acid', 'Fuyu Persimmon', 
                                             'Persimmons Japanese Dried', 'Persimmons Native Raw', 'Pineapple Canned Heavy Syrup Pack Solids And Liquids', 'Pineapple Canned Extra Heavy Syrup Pack Solids And Liquids', 
                                             'Pineapple Frozen Chunks Sweetened', 'Pineapple Juice Canned Or Bottled Unsweetened Without Added Ascorbic Acid', 
                                             'Pineapple Juice Frozen Concentrate Unsweetened Undiluted', 'Plums', 'Plums Canned Purple Water Pack Solids And Liquids',
                                              'Plums Canned Purple Juice Pack Solids And Liquids', 'Plums Canned Purple Light Syrup Pack Solids And Liquids', 'Acerola Cherries (West Indian Cherry)', 
                                              'Acerola Juice Raw', 'Apples', 'Apples (Without Skin)', 'Apples Dehydrated (Low Moisture) Sulfured Stewed',
                                               'Dried Apples', 'Apples Dried Sulfured Stewed Without Added Sugar', 'Apples Dried Sulfured Stewed With Added Sugar', 
                                               'Apples Frozen Unsweetened Unheated', 'Applesauce Canned Unsweetened Without Added Ascorbic Acid (Includes USDA Commodity)',
                                                'Applesauce Canned Sweetened Without Salt (Includes USDA Commodity)', 'Apricots', 'Apricots Canned Water Pack With Skin Solids And Liquids',
                                                 'Apricots Canned Heavy Syrup Pack With Skin Solids And Liquids',
                                                  'Apricots Canned Heavy Syrup Pack Without Skin Solids And Liquids',
                                                   'Apricots Canned Extra Heavy Syrup Pack Without Skin Solids And Liquids', 'Low-Moisture Dried Apricots', 
                                                   'Apricots Frozen Sweetened', 'Apricot Nectar Canned Without Added Ascorbic Acid', 'Avocados', 'California Avocados', 'Florida Avocados', 
                                                   'Cherries Tart Dried Sweetened', 'Blackberries Canned Heavy Syrup Solids And Liquids',
                                                    'Blackberries Frozen Unsweetened', 'Blueberries', 'Boysenberries Canned Heavy Syrup',
                                                     'Boysenberries (Frozen)', 'Breadfruit', 'Starfruit (Carambola)', 'Cherries Sour Red Canned Heavy Syrup Pack Solids And Liquids',
                                                      'Cherries Sour Red Canned Extra Heavy Syrup Pack Solids And Liquids',
                                                       'Sour Red Cherries (Frozen)', 'Cherries (Sweet)', 'Cherries Sweet Canned Extra Heavy Syrup Pack Solids And Liquids',
                                                        'Crabapples', 'Cranberries', 'Dried Cranberries (Sweetened)', 'Zante Currants', 'Custard-Apple', 'Dates (Deglet Noor)',
                                                         'Elderberries', 'Figs', 'Figs Canned Water Pack Solids And Liquids', 'Figs Canned Light Syrup Pack Solids And Liquids', 
                                                         'Figs Canned Heavy Syrup Pack Solids And Liquids', 'Figs Canned Extra Heavy Syrup Pack Solids And Liquids', 
                                                         'Fruit Cocktail (Peach And Pineapple And Pear And Grape And Cherry) Canned Extra Light Syrup Solids And Liquids', 
                                                         'Fruit Cocktail (Peach And Pineapple And Pear And Grape And Cherry) Canned Light Syrup Solids And Liquids',
                                                          'Fruit Cocktail (Peach And Pineapple And Pear And Grape And Cherry) Canned Heavy Syrup Solids And Liquids', 
                                                          'Fruit Cocktail (Peach And Pineapple And Pear And Grape And Cherry) Canned Extra Heavy Syrup Solids And Liquids',
                                                           'Gooseberries', 'Gooseberries Canned Light Syrup Pack Solids And Liquids', 
                                                           'Goji Berries Dried', 'Grapefruit', 'White Florida Grapefruit', 'Grapefruit Sections Canned Water Pack Solids And Liquids',
                                                            'Grapefruit Sections Canned Juice Pack Solids And Liquids', 'Grapefruit Sections Canned Light Syrup Pack Solids And Liquids', 'Grapefruit Juice', 'White Grapefruit Juice', 
                                                            'Muscadine Grapes', 'Grape Juice (With Added Vitamin C)', 'Grape Juice', 'Groundcherries', 'Guavas', 'Strawberry Guavas',
                                                             'Apples Raw Without Skin Cooked Boiled', 'Apples Raw Without Skin Cooked Microwave', 
                                                             'Apples Canned Sweetened Sliced Drained Heated', 'Apples Dehydrated (Low Moisture) Sulfured Uncooked',
                                                              'Apples Frozen Unsweetened Heated', 'Apple Juice', 'Apple Juice Frozen Concentrate Unsweetened Undiluted Without Added Ascorbic Acid', 
                                                              'Apple Juice Frozen Concentrate Unsweetened Diluted With 3 Volume Water Without Added Ascorbic Acid',
                                                               'Apricots Canned Water Pack Without Skin Solids And Liquids', 'Apricots Canned Juice Pack With Skin Solids And Liquids',
                                                                'Apricots Canned Extra Light Syrup Pack With Skin Solids And Liquids',
                                                                 'Apricots Canned Light Syrup Pack With Skin Solids And Liquids', 'Apricots Dehydrated (Low-Moisture) Sulfured Stewed',
                                                                  'Dried Apricots', 'Apricots Dried Sulfured Stewed Without Added Sugar',
                                                                   'Apricots Dried Sulfured Stewed With Added Sugar', 'Bananas', 'Dried Bananas', 'Blackberries', 'Blackberry Juice Canned', 'Blueberries Canned Heavy Syrup Solids And Liquids',
                                                                    'Wild Blueberries (Frozen)', 'Blueberries (Frozen)', 'Blueberries Frozen Sweetened', 'Carissa', 'Cherimoya', 'Sour Red Cherries',
                                                                     'Cherries Sour Red Canned Water Pack Solids And Liquids (Includes USDA Commodity Red Tart Cherries Canned)',
                                                                      'Cherries Sour Red Canned Light Syrup Pack Solids And Liquids', 
                                                                      'Cherries Sweet Canned Water Pack Solids And Liquids', 'Cherries Sweet Canned Juice Pack Solids And Liquids',
                                                                       'Cherries Sweet Canned Light Syrup Pack Solids And Liquids',
                                                                        'Cherries Sweet Canned Pitted Heavy Syrup Pack Solids And Liquids',
                                                                         'Cranberry Sauce Canned Sweetened',
                                                                          'Cranberry-Orange Relish Canned',
                                                                           'European Black Currants', 
                                                                           'Red And White Currants', 
                                                                           'Dried Figs', 'Figs Dried Stewed', 
                                                                           'Fruit Cocktail (Peach And Pineapple And Pear And Grape And Cherry) Canned Water Pack Solids And Liquids', 
                                                                           'Fruit Cocktail (Peach And Pineapple And Pear And Grape And Cherry) Canned Juice Pack Solids And Liquids', 
                                                                           'Fruit Salad (Peach And Pear And Apricot And Pineapple And Cherry) Canned Water Pack Solids And Liquids',
                                                                            'Fruit Salad (Peach And Pear And Apricot And Pineapple And Cherry) Canned Juice Pack Solids And Liquids',
                                                                             'Fruit Salad (Peach And Pear And Apricot And Pineapple And Cherry) Canned Light Syrup Solids And Liquids',
                                                                              'Fruit Salad (Peach And Pear And Apricot And Pineapple And Cherry) Canned Extra Heavy Syrup Solids And Liquids',
                                                                              'Pink Grapefruit', 'California Grapefruit', 'Florida Grapefruit', 'White Grapefruit', 'White California Grapefruit', 
                                                                              'Grapefruit Juice White Canned Or Bottled Unsweetened', 'Grapefruit Juice White Canned Sweetened',
                                                                               'Grapefruit Juice White Frozen Concentrate Unsweetened Undiluted', 'Grapefruit Juice White Frozen Concentrate Unsweetened Diluted With 3 Volume Water',
                                                                                'Grapes', 'Red Or Green Grapes (European)', 'Grapes Canned Thompson Seedless Water Pack Solids And Liquids',
                                                                                 'Grapes Canned Thompson Seedless Heavy Syrup Pack Solids And Liquids', 'Guava Sauce Cooked', 'Jackfruit', 
                                                                                 'Grapefruit And Orange Sections Raw', 'Grapefruit And Orange Sections Cooked Canned Or Frozen Ns As To Added Sweetener', 
                                                                                 'Grapefruit And Orange Sections Cooked Canned Or Frozen Unsweetened Water Pack', 'Grapefruit And Orange Sections Cooked Canned Or Frozen In Light Syrup',
                                                                                  'Kumquat Cooked Or Canned In Syrup', 'Orange Sections Canned Juice Pack', 'Grapefruit Juice 100% Ns As To Form',
                                                                                   'Grapefruit Juice 100% Canned Bottled Or In A Carton', 'Grapefruit Juice 100% With Calcium Added', 

                                                                                   'Orange Juice 100% With Calcium Added Frozen Reconstituted', 'Apple Dried Cooked Ns As To Sweetened Or Unsweetened; Sweetened Ns As To Type Of Sweetener',
                                                                                    'Apple Dried Cooked With Sugar', 'Apple Chips', 'Apricot Dried Cooked Ns As To Sweetened Or Unsweetened; Sweetened Ns As To Type Of Sweetener', 'Apricot Dried Cooked With Sugar', 'Fig Dried Cooked Ns As To Sweetened Or Unsweetened; Sweetened Ns As To Type Of Sweetener', 'Fig Dried Cooked With Sugar', 'Papaya Dried', 'Peach Dried Cooked Ns As To Sweetened Or Unsweetened; Sweetened Ns As To Type Of Sweetener', 'Peach Dried Cooked With Sugar', 'Pear Dried Cooked Ns As To Sweetened Or Unsweetened; Sweetened Ns As To Type Of Sweetener', 'Pear Dried Cooked With Sugar', 'Pineapple Dried', 'Prune Dried Cooked Ns As To Sweetened Or Unsweetened; Sweetened Ns As To Type Of Sweetener', 'Prune Dried Cooked With Sugar', 'Raisins Cooked', 'Fruit Ns As To Type', 'Apple Baked Ns As To Added Sweetener', 'Apple Baked Unsweetened', 'Apple Baked With Sugar', 'Apple Rings Fried', 'Apple Pickled', 'Apple Fried', 'Banana Red Fried', 'Banana Baked', 'Banana Ripe Fried', 'Banana Batter-Dipped Fried', 'Starfruit Cooked With Sugar', 'Guava Shell Canned In Heavy Syrup', 'Lychee Cooked Or Canned In Sugar Or Syrup', 'Mango Pickled', 'Mango Cooked', 'Nectarine Cooked', 'Papaya Green Cooked', 'Papaya Cooked Or Canned In Sugar Or Syrup', 'Peach Pickled', 'Plum Pickled', 'Rhubarb Cooked Or Canned Unsweetened', 'Rhubarb Cooked Or Canned In Light Syrup', 'Rhubarb Cooked Or Canned Drained Solids', 'Blackberries Frozen Sweetened Ns As To Type Of Sweetener', 'Blueberries Cooked Or Canned Unsweetened Water Pack', 'Raspberries Cooked Or Canned Unsweetened Water Pack', 'Raspberries Frozen Unsweetened', 'Strawberries Raw With Sugar', 'Strawberries Cooked Or Canned Unsweetened Water Pack', 'Ambrosia', 'Cranberry-Orange Relish Uncooked', 'Cranberry-Raspberry Sauce', 'Fruit Salad Fresh Or Raw  Excluding Citrus Fruits No Dressing', 'Fruit Salad Fresh Or Raw Including Citrus Fruits No Dressing', 'Fruit Cocktail Or Mix Frozen', 'Fruit Salad Puerto Rican Style', 'Apple Salad With Dressing', 'Apple Candied', 'Banana Whip', 'Prune Whip', 'Fried Dwarf Banana Puerto Rican Style', 'Fried Dwarf Banana With Cheese Puerto Rican Style', 'Fruit Salad Excluding Citrus Fruits With Salad Dressing Or Mayonnaise', 'Fruit Salad Excluding Citrus Fruits With Whipped Cream', 'Fruit Salad Excluding Citrus Fruits With Nondairy Whipped Topping', 'Fruit Salad Excluding Citrus Fruits With Marshmallows', 'Fruit Salad Including Citrus Fruits With Pudding', 'Fruit Salad Excluding Citrus Fruits With Pudding', 'Fruit Salad Including Citrus Fruits With Salad Dressing Or Mayonnaise', 'Fruit Salad Including Citrus Fruit With Whipped Cream', 'Fruit Salad Including Citrus Fruits With Nondairy Whipped Topping', 'Fruit Salad Including Citrus Fruits With Marshmallows', 'Fruit Dessert With Cream And/or Pudding And Nuts', 'Cranberry Salad Congealed', 'Pineapple Salad With Dressing', 'Pickled Green Bananas Puerto Rican Style', 'Tomato Green Pickled', 'Sauerkraut Cooked Ns As To Fat Added In Cooking', 'Sauerkraut Cooked Fat Added In Cooking', 'Beans String Green Pickled', 'Celery Pickled', 'Corn Relish', 'Cauliflower Pickled', 'Cabbage Red Pickled', 'Mushrooms Pickled', 'Okra Pickled', 'Olives Nfs', 'Olives Black', 'Olives Green Stuffed', 'Peppers Pickled', 'Seaweed Pickled', 'Vegetables Pickled Hawaiian Style', 'Vegetable Relish', 'Vegetables Pickled', 'Turnip Pickled', 'Tsukemono Japanese Pickles', 'Zucchini Pickled', 'Chinese Preserved Sweet Vegetable']
    temp = False
    source = ""
    for i in range(len(lst)):
        print(i)
        print(name)
        print(lst[i])
        if lst[i] == name:
            str1 = "../static/"
            str2 = str(lst[i])
            str3 = ".png"
            source = str1+str2+str3
            # print(source)
            # destination = "/Users/supriyauppala/Desktop/myflask/static/mango.png"
            # print(destination)
            # dest = shutil.copy(source, destination)
            temp = True
            break
    if temp == True:
        return render_template('index.html', data=source)
    else:
        return render_template('index.html', data="Not Found")
            
if __name__ == "__main__":
    app.run(debug=True)



