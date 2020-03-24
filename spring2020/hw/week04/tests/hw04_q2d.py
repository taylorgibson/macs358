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
                    [64.46325657001422, 32.490399592428695, 544.2707817635634, 36.966709656039356, 20.271153190992887, 434.2671993736693, 57.23574687938866, 140.3854503628539, 291.3116696400298, 70.8103572412429, 190.8019230876682, 19.47134711613135, 1066.6777446386084, 59.14048967531066, 743.4692944294621, 299.54248188851915, 92.85753260911373, 370.85267757674177, 30.0668809854318, 46.261277180615586, 23.569362652698633, 978.2975350287999, 58.007385518530135, 17.27125237067654, 358.0475362924121, 50.489122994055684]
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> caesar_scorer( ciphertext )
                    [13605.303323256037, 2448.2674655681694, 5582.638314540754, 6372.549495580206, 6988.904126710724, 13806.380816395666, 3361.630111100602, 2877.2571432767872, 3953.665798401931, 14327.835725491845, 8702.962654999028, 3858.076141231538, 10594.886693337514, 8133.136750927484, 4703.907642573717, 12336.132278499097, 8574.737640653913, 7101.638651405036, 6117.596971857358, 7937.83591474685, 4241.194776554946, 85.53668707056978, 12381.143343147181, 4687.871823464072, 14558.116883861923, 5230.994038213473]
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