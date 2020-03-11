test = {
    "name": "Question 3",       # name of the test
    "points": 8,        # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases each case is a dict
                {
                    "code": r"""
                    >>> def uses_loop(function):
                    ...     import ast
                    ...     import inspect
                    ...     loop_statements = ast.For, ast.While, ast.AsyncFor
                    ...     nodes = ast.walk(ast.parse(inspect.getsource(function)))
                    ...     return any(isinstance(node, loop_statements) for node in nodes)
                    >>> uses_loop( calculate_mkey )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },                
                {
                    "code": r"""
                    >>> def has_return_statement(function):
                    ...     import ast
                    ...     import inspect
                    ...     conditional_statements = ast.Return
                    ...     nodes = ast.walk(ast.parse(inspect.getsource(function)))
                    ...     return any(isinstance(node, conditional_statements) for node in nodes)
                    >>> has_return_statement( calculate_mkey )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },                
                {                       
                    "code": r"""
                    >>> calculate_mkey(5)
                    21
                    """,
                    "hidden": False,    # ignored by otter
                    "locked": False,    # ignored by otter
                }, 
                {
                    "code": r"""
                    >>> calculate_mkey(7, 13)
                    2
                    """,
                    "hidden": False,
                    "locked": False,
                }, 
                {
                    "code": r"""
                    >>> calculate_mkey(6, 26)
                    -1
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> calculate_mkey.__doc__ is None
                    False
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