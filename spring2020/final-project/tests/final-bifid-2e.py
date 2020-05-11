test = {
    "name": "Bifid, Part 2E",       # name of the test
    "points": 4,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> callable( bifid_horizontal_to_vertical )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> bifid_horizontal_to_vertical( [2, 1, 5, 3, 5, 4] )
                    [[2, 1, 5], [3, 5, 4]]
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> bifid_horizontal_to_vertical( [2, 3, 1, 5, 1, 4] )
                    [[2, 3, 1], [5, 1, 4]]
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> bifid_horizontal_to_vertical( [4, 2, 2, 4, 2, 4, 1, 3, 3, 3, 2, 3, 1, 4, 4, 1, 2, 1, 4, 3, 4, 3, 4, 3, 1, 1, 4, 3, 2, 2, 5, 3, 3, 1, 2, 5] )
                    [[4, 2, 2, 4, 2, 4, 1, 3, 3, 3, 2, 3, 1, 4, 4, 1, 2, 1], [4, 3, 4, 3, 4, 3, 1, 1, 4, 3, 2, 2, 5, 3, 3, 1, 2, 5]]
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