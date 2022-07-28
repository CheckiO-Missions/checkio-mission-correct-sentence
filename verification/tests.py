"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["greetings, friends"],
            "answer": "Greetings, friends."
        },
        {
            "input": ["Greetings, friends"],
            "answer": "Greetings, friends."
        },
        {
            "input": ["Greetings, friends."],
            "answer": "Greetings, friends."
        },
        {
            "input": ["greetings, friends."],
            "answer": "Greetings, friends."
        }
    ],
    "Extra": [
        {
            "input": ["hi"],
            "answer": "Hi."
        },
        {
            "input": ["welcome to New York"],
            "answer": "Welcome to New York."
        }
    ]
}
