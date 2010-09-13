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

f = open("style.css")

print """<!DOCTYPE>
<html>
<head>
  <title>ASCII Table</title>
  <style>"""
print f.read()
print """
  </style>
</head>
<body>
<table id="ascii-table" cellspacing=0>
  <thead>
    <tr>
      <th>Dec</th>
      <th>Hx</th>
      <th>Oct</th>
      <th>Char</th>
      <th></th>
      <th>Dec</th>
      <th>Hx</th>
      <th>Oct</th>
      <th>Html</th>
      <th>Chr</th>
      <th>Dec</th>
      <th>Hx</th>
      <th>Oct</th>
      <th>Html</th>
      <th>Chr</th>
      <th>Dec</th>
      <th>Hx</th>
      <th>Oct</th>
      <th>Html</th>
      <th>Chr</th>
    </tr>
  </thead>
  <tbody>"""

for i in range(32):
    print "    <tr>"

    octal = "000" + str(oct(i))
    print "      <td>%d</td>" % i
    print "      <td>%s</td>" % hex(i).upper()[2:]
    print "      <td>%s</td>" % octal[-3:]
    print "      <td class=\"char\">%s</td>" % ascii[i][0]
    print "      <td>(%s)</td>" % ascii[i][1]

    for char in [i+32, i+64, i+96]:
        octal = "000" + str(oct(char))
        print "      <td class=\"dec\">%d</td>" % char
        print "      <td>%s</td>" % hex(char).upper()[2:]
        print "      <td>%s</td>" % octal[-3:]
        print "      <td>&amp;#%d;</td>" % char
        print "      <td class=\"char\">",
        if char == 32:
            print "Space",
        elif char == 127:
            print "DEL",
        else:
            print "%s" % chr(char).upper(),
            print "</td>"

    print "    </tr>"

print "  </tbody>"
print "</table>"
print "</body></html>"
