
from flask import Flask, render_template
from condom_structures import total_gi_responses
from markupsafe import escape
from flask import request
from answer_converter import answer_converter
import sys


app = Flask(__name__)

name = total_gi_responses

def add_5(x):
    if type(x) == int or type(x) == float:

        return x + 5
    
    else:
        return x

form_data = dict()


@app.route("/")

def form():
    return render_template('apphtml.html')


@app.route('/data/', methods = ['POST', 'GET'])

def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        result = answer_converter(request.form["OR"], request.form["AND"], request.form["Question you want to see results of"])
        return render_template('data.html', 
        dependent = result[4], 
        independent_ors = result[2],
        independent_ands = result[3],
        total_number = result[1],
        x1 = result[0][0],
        x2 = result[0][1],
        x3 = result[0][2],
        x4 = result[0][3],
        x5 = result[0][4],
        x6 = result[0][5],
        x7 = result[0][6],
        x8 = result[0][7],
        x9 = result[0][8],
        x10 = result[0][9],
        x11 = result[0][10],
        x12 = result[0][11],
        x13 = result[0][12],
        x14 = result[0][13],
        x15 = result[0][14],
        x16 = result[0][15],
        x17 = result[0][16],
        x18 = result[0][17],
        x19 = result[0][18],
        x20 = result[0][19],
        x21 = result[0][20],
        x22 = result[0][21],
        x23 = result[0][22],
        x24 = result[0][23],
        x25 = result[0][24],
        x26 = result[0][25],
        x27 = result[0][26],
        x28 = result[0][27],
        x29 = result[0][28],
        x30 = result[0][29],
        x31 = result[0][30],
        x32 = result[0][31],
        x33 = result[0][32],
        x34 = result[0][33],
        x35 = result[0][34],
        x36 = result[0][35],
        x37 = result[0][36],
        x38 = result[0][37],
        x39 = result[0][38],
        x40 = result[0][39],
        x41 = result[0][40],
        x42 = result[0][41],
        x43 = result[0][42],
        x44 = result[0][43],
        x45 = result[0][44],
        x46 = result[0][45],
        x47 = result[0][46],
        x48 = result[0][47],
        x49 = result[0][48],
        x50 = result[0][49],
        x51 = result[0][50],
        x52 = result[0][51],
        x53 = result[0][52],
        x54 = result[0][53],
        x55 = result[0][54],
        x56 = result[0][55],
        x57 = result[0][56],
        x58 = result[0][57],
        x59 = result[0][58],
        x60 = result[0][59],
        x61 = result[0][60],
        x62 = result[0][61],
        x63 = result[0][62],
        x64 = result[0][63],
        x65 = result[0][64],
        x66 = result[0][65],
        x67 = result[0][66],
        x68 = result[0][67],
        x69 = result[0][68],
        x70 = result[0][69],
        x71 = result[0][70],
        x72 = result[0][71],
        x73 = result[0][72],
        x74 = result[0][73],
        x75 = result[0][74],
        x76 = result[0][75],
        x77 = result[0][76],
        x78 = result[0][77],
        x79 = result[0][78],
        x80 = result[0][79],
        x81 = result[0][80],
        x82 = result[0][81],
        x83 = result[0][82],
        x84 = result[0][83],
        x85 = result[0][84],
        x86 = result[0][85],
        x87 = result[0][86],
        x88 = result[0][87],
        x89 = result[0][88],
        x90 = result[0][89],
        x91 = result[0][90],
        x92 = result[0][91],
        x93 = result[0][92],
        x94 = result[0][93],
        x95 = result[0][94],
        x96 = result[0][95],
        x97 = result[0][96],
        x98 = result[0][97],
        x99 = result[0][98],
        x100 = result[0][99]
        )


@app.route('/reference')

def reference():
    return render_template('reference.html')












def hello_world():
    var = total_gi_responses
    string = "Hello " + f"{escape(total_gi_responses)}" + "\n" + "test"

    with app.test_request_context('/hello', method='POST'):
        assert request.path == '/hello'
        assert request.method == 'POST'

    return string


def try_again():
    return "hello"



