grade_result["correct"] = True
grade_result["comment"] = ''

responses = {}
for k, v in widget_inputs.items():
	radioNumber = int(k[5:]) - 1
	isChecked = v
	if isChecked:
		if radioNumber < 4:
			language = "HTML"
			fluency  = radioNumber
		elif radioNumber < 8:
			language = "CSS"
			fluency  = radioNumber - 4
		elif radioNumber < 12:
			language = "JavaScript"
			fluency  = radioNumber - 8
		else:
			language = "English"
			fluency  = radioNumber - 12
		responses[language] = fluency

def fluencyNumberToString(fluencyNumber):
	if fluencyNumber == 0:
		return "not proficient"
	elif fluencyNumber == 1:
		return "somewhat proficient"
	elif fluencyNumber == 2:
		return "fairly proficient"
	elif fluencyNumber == 3:
		return "fluent"

def getComment(responses):
	comment = ''
	if len(responses) < 4:
		comment += 'Make sure you select a proficiency for each of the 4 languages.'
		grade_result["correct"] = False
		grade_result["comment"] = comment
		return
	else:
		if responses['English'] == 0:
			comment += ("""Unfortunately at this time Udacity's classes are
				all taught in English. Without some understanding of English
				it will be impossible to complete this nanodegree.
				\n\nIf you want to learn English, check out
				<a href="www.duolingo.com">Duolingo</a>. It's a great way to
				learn a foreign language for free.""")
			grade_result["comment"] = comment
			return

		elif responses['English'] == 1:
			comment += ("""For now, Udacity's classes are taught exclusively
				in English. Though our videos have subtitles, it will still
				be very difficult to earn a nanodegree without a strong
				understanding of English.
				\n\nWe recommend you use another resource to learn web development.
				<a href="http://www.codecademy.com/learn">Codecademy</a> is a
				great resource for learning to code and it uses only written
				English (which is easier than video to consume at your own pace).
				\n\nIf you're interested in improving your English, we recommend you
				check out <a href="www.duolingo.com">Duolingo</a>. It's a great
				way to learn a foreign language for free.""")
			grade_result["comment"] = comment
			return

getComment(responses)
