test = {
    "name": "Question 2b",       # name of the test
    "points": 4,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> callable( RSA )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> RSA( 5, (3,33) )
                    26
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> RSA( 26, (7,33) )
                    5
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> RSA( 234712, (65537, 6935347))
                    2678654
                    """,
                    "hidden": False,
                    "locked": False,
                },     
                {
                    "code": r"""
                    >>> RSA( 2678654, (5655233, 6935347))
                    234712
                    """,
                    "hidden": False,
                    "locked": False,
                },      
                {
                    "code": r"""
                    >>> RSA( 26786543243423, (5655233, 6935347))
                    'invalid'
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