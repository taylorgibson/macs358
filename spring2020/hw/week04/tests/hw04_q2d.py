test = {
    "name": "Question 2, Part d",       # name of the test
    "points": 2,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> callable(caesar_scorer)
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> caesar_scorer( ciphertext ) == caesar_scorer( ciphertext.lower() + '_?7' )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },                
                {
                    "code": r"""
                    >>> caesar_scorer( 'HELLO' )
                    [22.419528323566897, 74.53412783887602, 544.2707817635634, 26.45577759442753, 30.78208525260472, 434.2671993736693, 57.23574687938866, 140.3854503628539, 291.3116696400298, 70.8103572412429, 190.8019230876682, 19.47134711613135, 1066.6777446386084, 59.14048967531066, 743.4692944294621, 299.54248188851915, 92.85753260911373, 370.85267757674177, 30.0668809854318, 35.750345119003754, 34.080294714310476, 978.2975350287999, 47.4964534569183, 27.78218443228838, 358.0475362924121, 50.489122994055684]
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> caesar_scorer( ciphertext )
                    [13615.47519299308, 2317.657832625157, 5582.638314540754, 6116.345526578418, 7350.217416328631, 13823.33393262407, 3356.3322622792252, 2890.819636259512, 3922.7969992693743, 14358.916438577256, 8336.845982449739, 4217.199653336609, 10576.450179439122, 8103.256883574919, 4382.858003998274, 12694.478772777033, 8587.099287903793, 6988.617876548996, 6059.744462727922, 8114.360237475129, 4236.744583544989, 30.65097328110476, 12372.66678503298, 4526.252115419933, 14533.322951377879, 5475.118911902521]
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