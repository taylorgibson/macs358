test = {
    "name": "Question 1",       # name of the test
    "points": 0,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> isinstance( my_replacements, dict )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> for test in [('1', 'ONE'), ('2', 'TWO'), ('3', 'THREE'), ('4', 'FOUR'), ('5', 'FIVE'), ('6', 'SIX'), ('7', 'SEVEN'), ('8', 'EIGHT'), ('9', 'NINE'), ('0', 'ZERO'), ('.', 'PERIOD'), (',', 'COMMA'), ('!', 'EXCLAMATIONPOINT'), ('?', 'QUESTIONMARK')]:
                    ...     test in my_replacements.items()
                    True
                    True
                    True
                    True
                    True
                    True
                    True
                    True
                    True
                    True
                    True
                    True
                    True
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },

            ],
            "scored": False,            # ignored by otter
            "setup": "",                # ignored by otter
            "teardown": "",             # ignored by otter
            "type": "doctest"           # the type of test; only "doctest" allowed
        },
    ]
}