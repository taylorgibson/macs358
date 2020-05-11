test = {
    "name": "Bifid, Part 3",       # name of the test
    "points": 4,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> callable( bifid )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> bifid( 'Hey' )
                    'FXY'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> bifid( 'This is a long message', key='ABCDEFGHIKLMNOPQRSTUVWXYZ')
                    'RIICN HDQFS SSASG XLK'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> bifid( 'FINRK SIQIO AN', 'macs', False )
                    'finalproiect'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> bifid( 'MKCTB SIY', key='durham', encipher=False )
                    'bullcity'
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