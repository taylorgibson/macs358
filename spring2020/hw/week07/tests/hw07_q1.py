test = {
    "name": "Question 1",       # name of the test
    "points": 2,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> callable( index_of_coincidence )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> index_of_coincidence('Hello', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                    0.1
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> round(index_of_coincidence('THISISASENTENCETHATISNTVERYLONGBUTIHOPETHATITSCORESLIKEAMONOALPHABETICCIPHER'), 8)
                    0.06666667
                    """,
                    "hidden": False,
                    "locked": False,
                },
                                {
                    "code": r"""
                    >>> round( index_of_coincidence( ciphertext_1 ), 8 )
                    0.04374254
                    """,
                    "hidden": False,
                    "locked": False,
                },
                                {
                    "code": r"""
                    >>> round( index_of_coincidence( ciphertext_2 ), 8 )
                    0.04110226
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
