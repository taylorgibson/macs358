test = {
    "name": "Question 2, Part c",       # name of the test
    "points": 4,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> callable(chi_squared_score)
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> chi_squared_score( ciphertext ) == chi_squared_score( ciphertext.lower() + '123.!' )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },                
                {
                    "code": r"""
                    >>> chi_squared_score( ciphertext )
                    13605.303323256037
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