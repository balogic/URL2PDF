import pdfkit
print "Enter the URL to be converted:"
my_url = raw_input()
pdfkit.from_url(my_url,"output.pdf")
print "Completed"
