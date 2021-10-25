class Question:
    """Question on a questionnaire."""
    """A single question on a survey, with a question, a list of choices, and whether or not that question should allow for comments"""

    def __init__(self, question, choices=None, allow_text=False):
        """Create question (assume Yes/No for choices."""

        if not choices:
            choices = ["Yes", "No"]

        self.question = question
        self.choices = choices
        self.allow_text = allow_text


class Survey:
    """Questionnaire."""
    """A survey, which has a title, instructions, and a list of Question objects"""

    def __init__(self, title, instructions, questions):
        """Create questionnaire."""

        self.title = title
        self.instructions = instructions
        self.questions = questions

# ex: satisfaction_survey.questions[1].question to get question "Did someone else shop with you today?"

satisfaction_survey = Survey( # does not include any questions that allow comments
    "Customer Satisfaction Survey", # title
    "Please fill out a survey about your experience with us.", # instructions
    [ # questions (list of instances of the Question class)
        Question("Have you shopped here before?"),
        Question("Did someone else shop with you today?"),
        Question("On average, how much do you spend a month on frisbees?",
                 ["Less than $10,000", "$10,000 or more"]),
        Question("Are you likely to shop here again?"),
    ])

personality_quiz = Survey( # Ignore
    "Rithm Personality Test",
    "Learn more about yourself with our personality quiz!",
    [
        Question("Do you ever dream about code?"),
        Question("Do you ever have nightmares about code?"),
        Question("Do you prefer porcupines or hedgehogs?",
                 ["Porcupines", "Hedgehogs"]),
        Question("Which is the worst function name, and why?",
                 ["do_stuff()", "run_me()", "wtf()"],
                 allow_text=True),
    ]
)

surveys = { # Ignore
    "satisfaction": satisfaction_survey,
    "personality": personality_quiz,
}