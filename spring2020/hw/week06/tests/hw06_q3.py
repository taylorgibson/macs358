test = {
    "name": "Question 3",       # name of the test
    "points": 4,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> callable( autokey )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> autokey('acceptthegreaterchallenge', 'UNICORN')
                    'UPKGD KGHGI VTTML VIYEL EIEIL'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> autokey('UPKGD KGHGI VTTML VIYEL EIEIL', 'unicorn', False)
                    'acceptthegreaterchallenge'
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