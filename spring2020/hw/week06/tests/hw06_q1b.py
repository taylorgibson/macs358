test = {
    "name": "Question 1, Part b",       # name of the test
    "points": 4,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> callable( vigenere_keygen )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> vigenere_keygen('Hello World', 'test')
                    'TESTTESTTE'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> vigenere_keygen('ERFEW WEFES JX', 'jupyter')
                    'JUPYTERJUPYT'
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