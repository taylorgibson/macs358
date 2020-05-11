test = {
    "name": "Polybius 1a",       # name of the test
    "points": 4,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> callable( polybius_square_gen )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> polybius_square_gen()
                    [['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H', 'I', 'K'], ['L', 'M', 'N', 'O', 'P'], ['Q', 'R', 'S', 'T', 'U'], ['V', 'W', 'X', 'Y', 'Z']]
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> polybius_square_gen( 'Polybius Cipher' )
                    [['P', 'O', 'L', 'Y', 'B'], ['I', 'U', 'S', 'C', 'H'], ['E', 'R', 'A', 'D', 'F'], ['G', 'K', 'M', 'N', 'Q'], ['T', 'V', 'W', 'X', 'Z']]
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> polybius_square_gen( key = 'Long Jump' )
                    [['L', 'O', 'N', 'G', 'I'], ['U', 'M', 'P', 'A', 'B'], ['C', 'D', 'E', 'F', 'H'], ['K', 'Q', 'R', 'S', 'T'], ['V', 'W', 'X', 'Y', 'Z']]
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