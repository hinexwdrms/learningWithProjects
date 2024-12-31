from flask import Flask, render_template, request
import unit_values

app = Flask(__name__)

#conversion logic
def convert_length(length, from_unit, to_unit):
    try:
        # Perform conversion using the dictionary
        return length * unit_values.length_dict[from_unit][to_unit]
    except KeyError:
        # Handle unsupported units
        return "Unsupported unit conversion."

@app.route('/convert_length',methods=['POST','GET']) #route that maps the URL to the function.

def length():   #function to convert length units
    converted_value = None

    if request.method == 'POST':  #getting the input values from the form
        length = float(request.form['length'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']

        #return result
        converted_value = convert_length(length, from_unit, to_unit)

        return render_template('length.html', converted_value=converted_value)
if __name__ == '__main__':
    app.run(debug=True)
