grade_result["correct"] = None
grade_result["completed"] = True
grade_result["comment"] = ''
CORRECT = True

shouldBeChecked   = map(str,[6,7,8,9,13,15])
shouldBeUnchecked = map(str,[1,2,3,4,5,10,11,12,14])

numChecked = 0
numSelected = 0
for k, v in widget_inputs.items():
	if k[:5] == 'check':
		checkNum = k[5:]
		if v:
			numChecked += 1
			if checkNum not in shouldBeChecked:
				CORRECT = False
		else:
			if checkNum not in shouldBeUnchecked:
				CORRECT = False
	elif k[:5] == 'radio':
		if v == True:
			numSelected += 1
		if k[5:] == '1' and v == False:
			CORRECT = False

if numChecked == 0:
	grade_result["correct"] = False
	grade_result["completed"] = False
	grade_result["comment"] = """There are checkboxes between the two code samples. Go through and check the box next to each line of code that contains a difference."""
elif numSelected == 0:
	grade_result["correct"] = False
	grade_result["completed"] = False
	grade_result["comment"] = """Select one of the two buttons below the code samples to indicate which sample will run."""
elif CORRECT:
	grade_result["comment"] = """You correctly identified all the differences!\n\nSuccessful programmers need to have patience and attention to detail to thoroughly inspect code."""
else:
	grade_result["comment"] = """You did not correctly identify all the differing lines. Patience and attention to detail are essential to your success in this nanodegree. You should build fluency in code inspection by taking Udacity's Intro to Computer Science before taking this nanodegree."""
