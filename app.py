from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

debug = DebugToolbarExtension(app)

RESPONSES = 'responses' # As people answer questions, store their answers in this list.
#  For example, at the end of the survey: ['Yes', 'No', 'Less than $10,000', 'Yes']

@app.route('/')
def show_start():
    """ Render a page that shows the user the title of the survey, the instructions, and a button to start the survey. """
    title = survey.title
    instructions = survey.instructions
    questions = survey.questions
    return render_template('start.html', title=title, instructions=instructions, questions=questions)

# modify your start page so that clicking on the button fires off a POST request to a new route that will set session[“responses”] to an empty list
@app.route("/begin", methods=["POST"])
def start_survey():
    """ Reset survey and redirect to the start of the survey. """

    session[RESPONSES] = [] # set session[“responses”] to an empty list

    return redirect("/questions/0")

@app.route('/questions/<int:index>')
def show_question(index):
    """ Show a form asking the current question, and listing the choices as radio buttons. """ 
    responses = session.get(RESPONSES)

    if (responses is None):
        # No answers have been appended to RESPONSES, trying to access question page before Start the Survey button has been clicked
        return redirect("/")

    if (len(responses) == len(survey.questions)):
        # All answers have been appended to RESPONSES so they've answered all the questions - redirect to completion page
        return redirect("/complete")

    if (len(responses) != index):
        # Trying to access questions out of order so redirect them to the last unanswered question and flash a message telling them they’re trying to access an invalid question
        flash(f"Invalid question id: {index}.")
        return redirect(f"/questions/{len(responses)}")
    
    q = survey.questions[index] # Access survey question through index since it's a list of instances inside the class
    choices = survey.questions[index].choices 
    return render_template('question.html', question=q, choices=choices)

@app.route('/answer', methods=["POST"])
def show_answer():
    """ When the user submits an answer, append this answer to responses list, and then redirect them to the next question. """
    choice = request.form['answer'] # get answer choice from form
    responses = session[RESPONSES]
    responses.append(choice)
    session[RESPONSES] = responses

    if (len(responses) == len(survey.questions)):
        # Once all answers have been appended to RESPONSES, the length should equal length of survey, meaning they completed
        return redirect("/complete")

    else: 
        # If length of RESPONSES doesn't equal length of survey, they are not done and will be redirected to the remaining questions
        return redirect(f"/questions/{len(responses)}")
    
@app.route('/complete')
def complete():
    """ Survey complete. Show a simple “Thank You!” page. """
    return render_template('completed.html')
