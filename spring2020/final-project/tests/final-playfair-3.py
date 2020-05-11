test = {
    "name": "Playfair Encryption-Decryption",       # name of the test
    "points": 12,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> callable( playfair )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> playfair( 'test' )
                    'UDTU'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> playfair( 'test', 'secret' )
                    'SCES'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> playfair( 'Hide the gold in the tree stump', 'playfair example')
                    'BMODZ BXDNA BEKUD MUIXM MOUVI F'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> playfair( 'BMODZ BXDNA BEKUD MUIXM MOUVI F', 'playfair example', False)
                    'hidethegoldinthetrexestump'
                    """,
                    "hidden": False,
                    "locked": False,
                },  
                {
                    "code": r"""
                    >>> playfair( 'FQVHD TAZQO EPEPS Y', 'decipher me', False)
                    'goodiobyoudiditx'
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