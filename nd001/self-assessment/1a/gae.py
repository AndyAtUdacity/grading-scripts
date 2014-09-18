grade_result["correct"] = None
grade_result["completed"] = True
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

		# coding_proficiency is between 0 and 9.
		htmlSkill = responses['HTML']
		cssSkill  = responses['CSS']
		jsSkill   = responses['JavaScript']
		coding_proficiency = htmlSkill + \
							 cssSkill + \
							 jsSkill

		if coding_proficiency == 9: # student is fluent in all 3 languages.
			comment += ("""You're already fluent in all the languages we will be
				covering in this nanodegree! While this doesn't make you a web
				developer, it may mean that you can find a shortened path through
				this nanodegree. When you talk to your coach, make sure you discuss
				your existing expertise and how it may influence your path through
				the nanodegree.\n\n""")

		elif (coding_proficiency >= 6) and (min(htmlSkill, cssSkill, jsSkill) >= 2):
			comment += ("""Congratulations! Since you already have a strong foundation
				in the languages we will be covering, you will be able to focus
				your energy on learning the skills that take you from someone who knows
				the languages to someone who is an expert web developer. Talk to your
				coach about how your existing skills may influence your path through the
				nanodegree.\n\n""")

		elif (coding_proficiency >= 6):
			comment += ("""Congratulations! Your expertise in some of the languages of
				web development will be extremely helpful as you go through this nanodegree.\n\n""")

		elif (coding_proficiency >= 4) and (jsSkill < htmlSkill) and (jsSkill < cssSkill):
			comment += ("""It looks like you are a strong developer of static web pages.
				As you probably know, becoming a professional web developer involves making dynamic pages
				which requires a mastery of JavaScript. This nanodegree is a perfect fit
				for you: you will build a deep understanding of the web and how HTML, CSS,
				and JS combine to make rich interactive web pages.\n\n""")

		elif (coding_proficiency >= 3) and (((jsSkill > htmlSkill) and (jsSkill >= cssSkill)) or ((jsSkill >= htmlSkill) and (jsSkill > cssSkill))):
			comment += ("""JavaScript is often one of the most difficult things for new web
				developers to learn. Your experience with it will be especially helpful as you start
				piecing together HTML, CSS, and JS to create rich interactive web pages.
				Your background makes you a great fit for this nanodegree.\n\n""")

		elif coding_proficiency == 0:
			comment += ("""Unfortunately, this nanodegree is not for you. You will need to have
				at least some experience in one of the three languages of web development to
				be successful. Take Udacity's Intro to HTML and CSS and then come back and enroll
				in the nanodegree.\n\n""")

		elif coding_proficiency <= 1:
			comment += ("""Since you are so new to the languages of web development, this
				nanodegree will be very challenging. You can still become a web developer,
				but you may want to consider doing more independent learning before committing
				to this nanodegree. If you decide to continue make sure you discuss your
				background with your coach.\n\n""")

		else:
			comment += ("""You are a perfect candidate for this nanodegree. You've got some
				experience but are not yet a master in the languages of web development.\n\n""")

		grade_result["comment"] = comment

getComment(responses)
