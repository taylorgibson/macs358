test = {
    "name": "Question 1",       # name of the test
    "points": 10,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> multiplicative( 'NEPTUNE', 5 )
                    'NUXRW NU'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> multiplicative( 'Jupiter', 17 )
                    'XCVGL QD'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> multiplicative( 'Pluto, sadly not a planet!', 9, True, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' )
                    'FVYPW GABVI NWPAF VANKP'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> multiplicative( 'NUXRW NU', 5, False )
                    'neptune'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> multiplicative( 'Venus', 2 )
                    'Invalid Key'
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