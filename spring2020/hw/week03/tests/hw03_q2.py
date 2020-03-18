test = {
    "name": "Question 2",       # name of the test
    "points": 10,        # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> affine( 'MERCURY', 7, 23 )
                    'DZMLH MJ'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> affine( 'Europa', 3, 10 )
                    'WSJAD K'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> affine( 'Ganymede Station?', 25, 8, True, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' )
                    'CIVKW EFEQP IPAUV'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> affine( 'DZMLH MJ', 7, 23, False )
                    'mercury'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> affine( 'Callisto', 4, 8 )
                    'Invalid key'
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