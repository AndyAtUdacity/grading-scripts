grade_result["correct"] = None
grade_result["completed"] = True
grade_result["comment"] = ''

for k, v in widget_inputs.items():
	grade_result["comment"] += "%s = %s\n\n" % (k, v)

if not widget_inputs['numeric1'] or not widget_inputs['numeric2']:
	grade_result["correct"] = False
	grade_result["completed"] = False
	grade_result["comment"] = """Enter a number into both boxes"""

elif int(widget_inputs['numeric1']) != 40 or int(widget_inputs['numeric2']) != 117:
	grade_result["comment"] = """That's incorrect. In this nanodegree we assume that you have a basic comfort with quantitative and logical thinking. Take Udacity's Introductory Algebra Review to work on your quantitative reasoning skills before continuing with this nanodegree."""

else:
	grade_result["comment"] = """Correct! In this nanodegree we assume that you have a basic comfort with quantitative and logical thinking. Your ability to solve problems likes these suggests that you have these skills.  Next you will explain *how* you solved this problem."""

