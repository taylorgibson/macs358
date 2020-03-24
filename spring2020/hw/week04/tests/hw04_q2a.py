test = {
    "name": "Question 2, Part a",       # name of the test
    "points": 2,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> callable(character_count)
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> len( character_count( 'HELLO' ) )
                    26
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> character_count( 'HELLO' ) == character_count( 'Hello!123' )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },                
                {
                    "code": r"""
                    >>> character_count( 'HELLO' )
                    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> character_count( ciphertext )
                    [16, 9, 41, 50, 1, 8, 29, 31, 57, 60, 0, 12, 43, 43, 74, 19, 11, 14, 2, 21, 1, 72, 10, 19, 28, 73]
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