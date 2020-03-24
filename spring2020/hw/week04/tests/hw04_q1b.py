test = {
    "name": "Question 1, Part b",       # name of the test
    "points": 2,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> isinstance( values, list )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> [round(i,7) for i in values]
                    [0.0215054, 0.0120968, 0.0551075, 0.0672043, 0.0013441, 0.0107527, 0.0389785, 0.0416667, 0.0766129, 0.0806452, 0.016129, 0.0, 0.0577957, 0.0577957, 0.0994624, 0.0255376, 0.0147849, 0.0188172, 0.0026882, 0.0282258, 0.0013441, 0.0967742, 0.0134409, 0.0255376, 0.0376344, 0.0981183]
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> callable(barplot)
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