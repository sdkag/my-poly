
### way 1
```yml
circle:
  cohort, ta_id

circle_student (joins):
  circle_id, ta_id
```
### way 2
```yml
circle:
  cohort, ta_id

circle_student (joins):
  circle_id, ta_id
```

Questions
  author_id
	goal
	failing description of bug
	error_message
	body
	category
	notes. array of notes.
	time_question_opened
	time_question_answered
	time_question_closed

Resolution
	question_id
	body


resolution_tags or question_tags and or both.



attachments
	file type (image, md, txt)
	link



in the gui, pull up yesterdays things
after standup pool together

Tags/Topics/Keywords
  category (ex. react, redux, destructuring, etc...)

standup
  day (enum)
	student_id
	yesterday
	today
	roadblocks

tracking sheet (pretty much just google sheet)
  planning docs
	milestones

students
	name, github, heroku link, scorecard

tas
  name

cohort_student (joins)
	cohort_id
	student_id


circle_student (joins):
  circle_id, ta_id