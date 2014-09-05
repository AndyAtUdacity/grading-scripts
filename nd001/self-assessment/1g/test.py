from StringIO import StringIO
import sys
import traceback as tb

student_code_file = 'studentMain.py'
ns = {}

def test(code_file):
	try:
		code = open(code_file)
		code_string = code.read()
		exec(code_string, ns)
	except Exception as e:
		comment = "The code raised an exception"
		return "NO" + comment
	try:
		if not addOdds(6,10) == 16:
			comment = "The code didn't behave as expected."
			return "NO" + comment
		else:
			return "OK" + comment
	except Exception as e:
		comment = "The code raised an exception"
		return "NO" + comment

try:
    output = StringIO()
    suppressed_stdout = sys.stdout
    sys.stdout = output
    result = test(student_code_file)
    sys.stdout = suppressed_stdout
    print result
except Exception as e:
    sys.stdout = suppressed_stdout
    exc_type, exc_value, exc_traceback = sys.exc_info()
    comment = 'Your code raised an exception:\n'
    comment += ''.join(tb.format_tb(exc_traceback))
    comment += ''.join(tb.format_exc())
    comment += '\nThis might be an error with the grading code on our end, so please'
    comment += '\nsend support@udacity.com an email to let us know what happened!'
    print 'NO'+comment


