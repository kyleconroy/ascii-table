import logging
import optparse
import math

ascii = [
    ("NUL", "null"),
    ("SOH", "start of heading"),
    ("STX", "start of text"),
    ("ETX", "end of text"),
    ("EOT", "end of transmission"),
    ("ENQ","enquiry"),
    ("ACK","acknowledge"),
    ("BEL","bell"),
    ("BS", "backspace"),
    ("TAB","horizontal tab"),
    ("LF","NL line feed"),
    ("VT", "vertical tab"),
    ("FF", "NP form feed"),
    ("CR","carriage return"),
    ("SO","shift out"),
    ("SI","shift in"),
    ("DLE","data link escape"),
    ("DC1","device control 1"),
    ("DC2","device control 2"),
    ("DC3","device control 3"),
    ("DC4","device control 4"),
    ("NAK","negative acknowledge"),
    ("SYN","synchronous idle"),
    ("ETB","end of trans. block"),
    ("CAN","cancel"),
    ("EM", "end of medium"),
    ("SUB","substitute"),
    ("ESC","escape"),
    ("FS","file seperator"),
    ("GS","group seperator"),
    ("RS","record seperator"),
    ("US","unit seperator"),
]

parser = optparse.OptionParser()
(options, args) = parser.parse_args()

if len(args) != 1:
    parser.error("Incorrect number of arguments")

COLUMNS = int(args[0])
ROWS = math.ceil(127.0 / COLUMNS)
TABLE_HEADER ="<th>Dec</th><th>Hx</th><th>Oct</th><th class=\"html\">Html</th><th class=\"char\">Char</th>"

# HTML
html =  "<!DOCTYPE><html><head><title>ASCII Table</title>"

# Style
f = open("style.css")
html += "<style>" + f.read() + "</style></head>"

# Table
html += "<body><table id=\"ascii-table\" cellspacing=0><thead>"

# Table Header
html += "<tr>"

for i in range(COLUMNS):
    html += TABLE_HEADER

html += "</tr>"

html += "</thead><tbody>"

def table_row(i):
    octal = "000" + str(oct(i))
    row =  "<td class=\"dec\">%d</td>" % i
    row += "<td class=\"hex\">%s</td>" % hex(i).upper()[2:]
    row += "<td class=\"oct\">%s</td>" % octal[-3:]
    if i < 32:
        row += "<td class=\"html\"></td>"
        row += "<td class=\"char\">%s</td>" % ascii[i][0]
    else:
        row += "<td class=\"html\">&amp;#%d;</td>" % i
        row += "<td class=\"char\">"
        if i == 32:
            row += "Space"
        elif i == 127:
            row += "DEL"
        else:
            row += "%s" % chr(i).upper()
            row += "</td>"
    return row

for i in range(ROWS):
    html += "<tr>"
    for p in range(COLUMNS):
        char = int(i + (ROWS * p))
        if char < 128:
            html += table_row(char)
    html += "</tr>"

html += "</tbody>"
html += "</table>"
html += "</body></html>"

print html
