test = {
    "name": "Question 2, Part a",       # name of the test
    "points": 4,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> callable( trithemius )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> trithemius('donotpressthisbutton', 2, 4)
                    'FUXCL LRIAE JBGUH EHLKN'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> trithemius('NWTSV PPAMK JVUCJ AXVOL', 10, 24, False)
                    'donotpressthisbutton'
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