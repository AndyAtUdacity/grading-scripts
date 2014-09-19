grade_result["correct"] = None
grade_result["completed"] = True
grade_result["comment"] = ''

for k, v in widget_inputs.items():
	grade_result["comment"] += "%s = %s\n\n" % (k, v)

wi = widget_inputs

if not wi['radio1'] and not wi['radio2'] and not wi['radio3']:
	grade_result["comment"] = """Select 'yes', 'no', or 'not sure'."""
elif not wi['radio1']:
	grade_result["comment"] = """Unfortunately, you cannot take this nanodegree if you are unable to commit 10 hours per week. We suggest you browse the Udacity course catalog and begin with a single course and come back to this nanodegree when you have the time to commit."""
else:
	grade_result["comment"] = """If you spend 10 hours per week we expect it will take about 6 months to complete this nanodegree."""

