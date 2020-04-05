test = {
    "name": "Question 2, Part b",       # name of the test
    "points": 4,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> callable( vigenere )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> vigenere('onaplaneaplaneisdue', 'hospital')
                    'VBSET TNPHD DPVXI DKIW'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> vigenere('DAGAZ MTLZT GRTIC SVBCS EO', 'vigenere', False)
                    'isawmichelangeloatwork'
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