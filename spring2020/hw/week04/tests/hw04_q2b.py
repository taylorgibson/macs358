test = {
    "name": "Question 2, Part b",       # name of the test
    "points": 2,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> callable(expected_count)
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> len( expected_count( 'HELLO' ) )
                    26
                    """,
                    "hidden": False,
                    "locked": False,
                },                
                {
                    "code": r"""
                    >>> expected_count( 'HELLO' )
                    [0.40835000000000005, 0.0746, 0.1101, 0.21265, 0.6351, 0.1114, 0.10075, 0.3047, 0.3483, 0.00765, 0.06459999999999999, 0.20125, 0.1203, 0.33744999999999997, 0.37534999999999996, 0.09645000000000001, 0.00475, 0.29935, 0.31635, 0.4678, 0.1379, 0.0489, 0.128, 0.0075, 0.0997, 0.0038499999999999997]
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> expected_count( 'HELLO' ) == expected_count( 'Hello!123' )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },                
                {
                    "code": r"""
                    >>> expected_count( ciphertext )
                    [60.762480000000004, 11.10048, 16.38288, 31.642319999999998, 94.50287999999999, 16.576320000000003, 14.991600000000002, 45.33936, 51.82704, 1.13832, 9.61248, 29.946, 17.900640000000003, 50.212559999999996, 55.85208, 14.35176, 0.7068, 44.54328, 47.072880000000005, 69.60864000000001, 20.51952, 7.27632, 19.046400000000002, 1.116, 14.83536, 0.57288]
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