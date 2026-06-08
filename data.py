import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'
dif = pd.read_excel("/Users/supriyauppala/Desktop/myflask/Mydata.xlsx")
#fruits = dif.loc[dif['Food Group'] == 'Fruits']
df = dif.loc[dif['Food Group'] == 'Fruits']
#vegetables = dif.loc[dif['Food Group'] == 'Vegetables']
#df = pd.concat([fruits, vegetables], ignore_index=True)
# df=pd.concat([fruits_and_vegetables, beans_and_lentils], ignore_index=True)
df.drop(["ID", "Calcium (mg)","Iron, Fe (mg)","Potassium, K (mg)",
"Magnesium (mg)","Vitamin A, IU (IU)","Vitamin A, RAE (mcg)",
"Vitamin C (mg)","Vitamin B-12 (mcg)","Vitamin D (mcg)",
"Vitamin E (Alpha-Tocopherol) (mg)","Added Sugar (g)","Net-Carbs (g)",
"Omega 3s (mg)","Omega 6s (mg)","PRAL score","Trans Fatty Acids (g)",
"Soluble Fiber (g)","Insoluble Fiber (g)","Sucrose (g)","Glucose (Dextrose) (g)",
"Fructose (g)","Lactose (g)","Maltose (g)","Galactose (g)","Starch (g)",
"Total sugar alcohols (g)","Phosphorus, P (mg)","Sodium (mg)","Zinc, Zn (mg)",
"Copper, Cu (mg)","Manganese (mg)","Selenium, Se (mcg)","Fluoride, F (mcg)",
"Molybdenum (mcg)","Chlorine (mg)","Thiamin (B1) (mg)","Riboflavin (B2) (mg)",
"Niacin (B3) (mg)","Pantothenic acid (B5) (mg)","Vitamin B6 (mg)","Biotin (B7) (mcg)",
"Folate (B9) (mcg)","Folic acid (mcg)","Food Folate (mcg)","Folate DFE (mcg)",
"Choline (mg)","Betaine (mg)","Retinol (mcg)","Carotene, beta (mcg)",
"Carotene, alpha (mcg)","Lycopene (mcg)","Lutein + Zeaxanthin (mcg)",
"Vitamin D2 (ergocalciferol) (mcg)","Vitamin D3 (cholecalciferol) (mcg)",
"Vitamin D (IU) (IU)","Vitamin K (mcg)","Dihydrophylloquinone (mcg)",
"Menaquinone-4 (mcg)","Fatty acids, total monounsaturated (mg)",
"Fatty acids, total polyunsaturated (mg)","18:3 n-3 c,c,c (ALA) (mg)",
"20:5 n-3 (EPA) (mg)","22:5 n-3 (DPA) (mg)","22:6 n-3 (DHA) (mg)",
"Tryptophan (mg)","Threonine (mg)","Isoleucine (mg)","Leucine (mg)",
"Lysine (mg)","Methionine (mg)","Cystine (mg)","Phenylalanine (mg)",
"Tyrosine (mg)","Valine (mg)","Arginine (mg)","Histidine (mg)",
"Alanine (mg)","Aspartic acid (mg)","Glutamic acid (mg)","Glycine (mg)",
"Proline (mg)","Serine (mg)","Hydroxyproline (mg)","Alcohol (g)",
"Caffeine (mg)","Theobromine (mg)","Serving Weight 1 (g)",
"Serving Description 1 (g)",
"Serving Weight 2 (g)","Serving Description 2 (g)",
"Serving Weight 3 (g)","Serving Description 3 (g)",
"Serving Weight 4 (g)","Serving Description 4 (g)",
"Serving Weight 5 (g)","Serving Description 5 (g)",
"Serving Weight 6 (g)","Serving Description 6 (g)",
"Serving Weight 7 (g)","Serving Description 7 (g)",
"Serving Weight 8 (g)","Serving Description 8 (g)",
"Serving Weight 9 (g)","Serving Description 9 (g)",
"200 Calorie Weight (g)"
], axis = 1, inplace = True)

d2 = pd.DataFrame({'name':[], 'Food Group':[], 
'Calories':[],
 'Fat (g)':[], 
 'Protein (g)':[],
 'Carbohydrate (g)':[],
'Sugars (g)':[], 
  'Fiber (g)':[],
'Cholesterol (mg)':[],
 'Saturated Fats (g)':[], 'Water (g)':[]})
names = df['name'].tolist()
for i in range(len(names)):
    d2 = df[(df['name']==names[i])]
    d2 = d2.rename(columns={'Food Group':'category', 'Fat (g)':'fat', 
    'Protein (g)':'protein',
    'Carbohydrate (g)':'carbohydrate', 'Sugars (g)':'sugars', 
    'Fiber (g)':'fibers', 'Cholesterol (mg)':'cholesterol',
    'Saturated Fats (g)':'saturatedfats', 'Water (g)':'water'})
    d2["fat"] = d2["fat"].fillna(0)
    d2["protein"] = d2["protein"].fillna(0)
    d2["carbohydrate"] = d2["carbohydrate"].fillna(0)
    d2["sugars"] = d2["sugars"].fillna(0)
    d2["fibers"] = d2["fibers"].fillna(0)
    d2["cholesterol"] = d2["cholesterol"].fillna(0)
    d2["saturatedfats"] = d2["saturatedfats"].fillna(0)
    d2["water"] = d2["water"].fillna(0)
    my_list=[]
    for rows in d2.itertuples():
        my_list=[rows.name, rows.category, rows.Calories,
        rows.fat, rows.protein, rows.carbohydrate, rows.sugars , 
        rows.fibers , rows.cholesterol , rows.saturatedfats, rows.water]
    new_list=[]
    for j in range(3,len(my_list)):
        new_list.append(my_list[j])
    labels = ['Fats', 'Proteins', 'Carbohydrates', 'Sugars','Fibers',
    'Cholesterols','Saturated fats','Water']
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','mediumpurple','black','brown','orangered']
    matplotlib.pyplot.title(label=names[i])
    # Plot
    sizes=[]
    new_labels=[]
    new_colors=[]
    for ni in range(0,len(new_list)):
        if float(new_list[ni]) != 0.0:
            new_labels.append(labels[ni])
            new_colors.append(colors[ni])
            sizes.append(new_list[ni])
    patches, texts = plt.pie(sizes,colors=new_colors,startangle=140)
    plt.legend(patches, new_labels, loc="best")
    plt.axis('equal')
    string = '/'+str(names[i])+'.'
    for op in range(1,len(string)):
        if string[op] == '/':
            string = string[0:op]
            break
    plt.savefig('/Users/supriyauppala/Desktop/myflask/static/' +  string + 'png')
    print("Done making a copy of ",i+1)

quit()
