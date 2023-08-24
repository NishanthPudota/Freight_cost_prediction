from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open(r"rf_model.pickle", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Line_item_quantity
        Line_Item_Quantity = request.form["Line_Item_Quantity"]
        Line_Item_Quantity = int(Line_Item_Quantity)

        # Line_Item_Value
        Line_Item_Value = request.form["Line_Item_Value"]
        Line_Item_Value = float(Line_Item_Value)

        # Weight
        Weight = request.form['Weight']
        Weight = float(Weight)

        # Country
        Country=request.form['Country']
        if(Country=='Congo'):
            Congo = 1
            Cote = 0
            Ethiopia = 0
            Guyana = 0
            Haiti = 0
            Mozambique = 0
            Nigeria = 0
            Rwanda = 0
            Tanzania = 0
            Uganda = 0
            Zambia = 0 
            Zimbabwe = 0
            Other_Country=0

        elif (Country=='Cote'):
            Congo = 0
            Cote = 1
            Ethiopia = 0
            Guyana = 0
            Haiti = 0
            Mozambique = 0
            Nigeria = 0
            Rwanda = 0
            Tanzania = 0
            Uganda = 0
            Zambia = 0 
            Zimbabwe = 0
            Other_Country=0

        elif (Country=='Ethiopia'):
            Congo = 0
            Cote = 0
            Ethiopia = 1
            Guyana = 0
            Haiti = 0
            Mozambique = 0
            Nigeria = 0
            Rwanda = 0
            Tanzania = 0
            Uganda = 0
            Zambia = 0 
            Zimbabwe =0
            Other_Country=0
            
        elif (Country=='Guyana'):
            Congo = 0
            Cote = 0
            Ethiopia = 0
            Guyana = 1
            Haiti = 0
            Mozambique = 0
            Nigeria = 0
            Rwanda = 0
            Tanzania = 0
            Uganda = 0
            Zambia = 0 
            Zimbabwe =0
            Other_Country=0
            
        elif (Country=='Haiti'):
            Congo = 0
            Cote = 0
            Ethiopia = 0
            Guyana = 0
            Haiti = 1
            Mozambique = 0
            Nigeria = 0
            Rwanda = 0
            Tanzania = 0
            Uganda = 0
            Zambia = 0 
            Zimbabwe =0
            Other_Country=0
            
        elif (Country=='Mozambique'):
            Congo = 0
            Cote = 0
            Ethiopia = 0
            Guyana = 0
            Haiti = 0
            Mozambique = 1
            Nigeria = 0
            Rwanda = 0
            Tanzania = 0
            Uganda = 0
            Zambia = 0 
            Zimbabwe =0
            Other_Country=0

        elif (Country=='Nigeria'):
            Congo = 0
            Cote = 0
            Ethiopia = 0
            Guyana = 0
            Haiti = 0
            Mozambique = 0
            Nigeria = 1
            Rwanda = 0
            Tanzania = 0
            Uganda = 0
            Zambia = 0 
            Zimbabwe =0
            Other_Country=0

        elif (Country=='Rwanda'):
            Congo = 0
            Cote = 0
            Ethiopia = 0
            Guyana = 0
            Haiti = 0
            Mozambique = 0
            Nigeria = 0
            Rwanda = 1
            Tanzania = 0
            Uganda = 0
            Zambia = 0 
            Zimbabwe =0
            Other_Country=0

        elif (Country=='Tanzania'):
            Congo = 0
            Cote = 0
            Ethiopia = 0
            Guyana = 0
            Haiti = 0
            Mozambique = 0
            Nigeria = 0
            Rwanda = 0
            Tanzania = 1
            Uganda = 0
            Zambia = 0 
            Zimbabwe =0
            Other_Country=0

        elif (Country=='Uganda'):
            Congo = 0
            Cote = 0
            Ethiopia = 0
            Guyana = 0
            Haiti = 0
            Mozambique = 0
            Nigeria = 0
            Rwanda = 0
            Tanzania = 0
            Uganda = 1
            Zambia = 0 
            Zimbabwe =0
            Other_Country=0

            
        elif (Country=='Zambia'):
            Congo = 0
            Cote = 0
            Ethiopia = 0
            Guyana = 0
            Haiti = 0
            Mozambique = 0
            Nigeria = 0
            Rwanda = 0
            Tanzania = 0
            Uganda = 0
            Zambia = 1 
            Zimbabwe =0
            Other_Country=0

        elif (Country=='Zimbabwe'):
            Congo = 0
            Cote = 0
            Ethiopia = 0
            Guyana = 0
            Haiti = 0
            Mozambique = 0
            Nigeria = 0
            Rwanda = 0
            Tanzania = 0
            Uganda = 0
            Zambia = 0 
            Zimbabwe = 1
            Other_Country=0

        else:
            Congo = 0
            Cote = 0
            Ethiopia = 0
            Guyana = 0
            Haiti = 0
            Mozambique = 0
            Nigeria = 0
            Rwanda = 0
            Tanzania = 0
            Uganda = 0
            Zambia = 0 
            Zimbabwe = 0
            Other_Country=1

        # Shipment Mode
        Shipment_Mode = request.form["Shipment_Mode"]
        if (Shipment_Mode == 'Air'):
            Air = 1
            Air_Charter = 0
            Ocean = 0
            Truck = 0

        elif (Shipment_Mode == 'Air_Charter'):
            Air = 0
            Air_Charter = 1
            Ocean = 0
            Truck = 0

        elif (Shipment_Mode == 'Ocean'):
            Air = 0
            Air_Charter = 0
            Ocean = 1
            Truck = 0

        else:
            Air = 0
            Air_Charter = 0
            Ocean = 0
            Truck = 1

        # Dosage Form
        Dosage_Form = request.form["Dosage_Form"]
        if (Dosage_Form == 'Capsule'):
            Capsule = 1
            Oral_Solution = 0
            Oral_Suspention = 0
            Tablet = 0
            Tablet_FDC = 0
            Other_Dosage_Form = 0
        
        elif (Dosage_Form == 'Oral_Solution'):
            Capsule = 0
            Oral_Solution = 1
            Oral_Suspention = 0
            Tablet = 0
            Tablet_FDC = 0
            Other_Dosage_Form = 0

        elif (Dosage_Form == 'Oral_Suspention'):
            Capsule = 0
            Oral_Solution = 0
            Oral_Suspention = 1
            Tablet = 0
            Tablet_FDC = 0
            Other_Dosage_Form = 0

        elif (Dosage_Form == 'Tablet'):
            Capsule = 0
            Oral_Solution = 0
            Oral_Suspention = 0
            Tablet = 1
            Tablet_FDC = 0
            Other_Dosage_Form = 0

        elif (Dosage_Form=='Tablet_FDC'):
            Capsule = 0
            Oral_Solution = 0
            Oral_Suspention = 0
            Tablet = 0
            Tablet_FDC = 1
            Other_Dosage_Form = 0

        else:
            Capsule = 0
            Oral_Solution = 0
            Oral_Suspention = 0
            Tablet = 0
            Tablet_FDC = 0
            Other_Dosage_Form = 1

        
        
        prediction=model.predict([[
            Line_Item_Quantity,
            Line_Item_Value,
            Weight,
            Congo,
            Cote,
            Ethiopia,
            Guyana,
            Haiti,
            Mozambique,
            Nigeria,
            Other_Country,
            Rwanda,
            Tanzania,
            Uganda,
            Zambia,
            Zimbabwe,
            Air,
            Air_Charter,
            Ocean,
            Truck,
            Capsule,
            Oral_Solution,
            Oral_Suspention,
            Other_Dosage_Form,
            Tablet,
            Tablet_FDC]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="The Freight cost is Rs. {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)