test = {
    "name": "Question 1",       # name of the test
    "points": 6,        # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> def uses_loop(function):
                    ...     import ast
                    ...     import inspect
                    ...     loop_statements = ast.For, ast.While, ast.AsyncFor
                    ...     nodes = ast.walk(ast.parse(inspect.getsource(function)))
                    ...     return any(isinstance(node, loop_statements) for node in nodes)
                    >>> uses_loop( triangular_number )
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
                    >>> has_return_statement( triangular_number )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },                
                {                       
                    "code": r"""
                    >>> triangular_number(1)
                    1
                    """,
                    "hidden": False,    # ignored by otter
                    "locked": False,    # ignored by otter
                }, 
                {
                    "code": r"""
                    >>> triangular_number(3)
                    6
                    """,
                    "hidden": False,
                    "locked": False,
                }, 
                {
                    "code": r"""
                    >>> triangular_number(10)
                    55
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> isinstance( triangular_number(1), int )
                    True
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