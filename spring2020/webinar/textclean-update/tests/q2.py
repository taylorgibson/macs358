test = {
    "name": "Question 2",       # name of the test
    "points": 0,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> callable( text_clean )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> text_clean( 'Meet me at 9 oclock', LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', special = my_replacements )
                    'MEETMEATNINEOCLOCK'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> text_clean( 'Testing Testing 123. Is this thing on?', LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', special = my_replacements )
                    'TESTINGTESTINGONETWOTHREEPERIODISTHISTHINGONQUESTIONMARK'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> text_clean( 'Frankly my dear, I dont give a hoot!', LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', special = my_replacements )
                    'FRANKLYMYDEARCOMMAIDONTGIVEAHOOTEXCLAMATIONPOINT'
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