try:
    grade_result['correct'] = (executor_result['stdout'][0:2] == 'OK')
    grade_result['comment'] = executor_result['stdout'][2:]
    grade_result['feedback'] = 'See feedback below.'
except:
    grade_result['correct'] = False
    grade_result['comment'] = 'The grading code broke :('
    grade_result['feedback'] = 'The grading code broke :('