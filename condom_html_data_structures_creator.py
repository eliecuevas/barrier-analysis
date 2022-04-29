import datetime
import operator

from condom_structures import so_num, so_pct, so_options, total_so_responses
from condom_structures import confidence_num, confidence_pct, total_confidence_responses







so_table = '''

    <table id = "t01" class = "inlineTable" style = "width: 50%; float: left;">

    <caption style = "color: powderblue;"> Sexual Orientation Breakdown </caption>

    <colgroup>
    <col span = "1" style = "width: 70%;">
    <col span = "1" style = "width: 15%;">
    <col span = "1" style = "width: 15%;">
    </colgroup>

    <tr>
    <th> Sexual Orientation </th>
    <th> # </th>
    <th> pct </th>
    </tr>

'''


for orientation in so_num.keys():
    so_table += "\n" + "<tr>" + "\n" 
    so_table += "<td>" + orientation + "</td>" + "\n" 
    so_table += "<td style = 'text-align: center;'>" + str(so_num[orientation]) + "</td>" + "\n" 
    so_table += "<td style = 'text-align: center;'>" + str((so_pct[orientation]*100))[:4] + "</td>" + "\n" 
    so_table += "</tr>" + "\n" 

so_table += "</table>" + "\n"


confidence_table = '''

    <table id = "t01" class = "inlineTable" style = "width: 50%; float: left;">

    <caption style = "color: powderblue;"> Condom Confidence: "I feel confident I can use a condom correctly" </caption>

    <colgroup>
    <col span = "1" style = "width: 70%;">
    <col span = "1" style = "width: 15%;">
    <col span = "1" style = "width: 15%;">
    </colgroup>

    <tr>
    <th> Response </th>
    <th> # </th>
    <th> pct </th>
    </tr>

'''

for response in confidence_num.keys():
    confidence_table += "\n" + "<tr>" + "\n" 
    confidence_table += "<td>" + response + "</td>" + "\n" 
    confidence_table += "<td style = 'text-align: center;'>" + str(confidence_num[response]) + "</td>" + "\n" 
    confidence_table += "<td style = 'text-align: center;'>" + str((confidence_pct[response]*100))[:4] + "</td>" + "\n" 
    confidence_table += "</tr>" + "\n" 

confidence_table += "</table>" + "\n"








class Variables_needed:
    timestamp = str(datetime.datetime.now())[:-7] #timestamp, in format "yyyy-mm-dd hh-mm-ss"
    so_table = so_table
    confidence_table = confidence_table

if __name__ == '__main__': 




    HTML_file_0 = open('quick_glance_draft.html', 'r')
    html_new = HTML_file_0.read().format(p = Variables_needed())

    HTML_file_1 = open('html_dashboard.html', 'w')
    HTML_file_1.write("")
    HTML_file_1.write(html_new)

    HTML_file_0.close
    HTML_file_1.close

    pass


