"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": "greetings, friends",
            "answer": "Greetings, friends."
        },
        {
            "input": "Greetings, friends",
            "answer": "Greetings, friends."
        },
        {
            "input": "Greetings, friends.",
            "answer": "Greetings, friends."
        }
    ],
    "Extra": [
        {
            "input": "hi",
            "answer": "Hi."
        }
    ]
}
