test = {
    "name": "Question 1, Part a",       # name of the test
    "points": 4,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> callable( trithemius_keygen )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> trithemius_keygen('HELLO', 3, 2)
                    'DFHJL'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> trithemius_keygen('FHERS XS', 24, 25)
                    'YXWVUTS'
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