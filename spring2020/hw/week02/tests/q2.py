test = {
    "name": "Question 2",       # name of the test
    "points": 6,        # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases each case is a dict
                {                       
                    "code": r"""
                    >>> def uses_conditional_branches(function):
                    ...     import ast
                    ...     import inspect
                    ...     conditional_statements = ast.If
                    ...     nodes = ast.walk(ast.parse(inspect.getsource(function)))
                    ...     return any(isinstance(node, conditional_statements) for node in nodes)
                    >>> uses_conditional_branches( integer_compare )
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
                    >>> has_return_statement( integer_compare )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },                
                {                       
                    "code": r"""
                    >>> integer_compare(3, 7)
                    'y is larger than x'
                    """,
                    "hidden": False,    # ignored by otter
                    "locked": False,    # ignored by otter
                }, 
                {
                    "code": r"""
                    >>> integer_compare(5, 1)
                    'x is larger than y'
                    """,
                    "hidden": False,
                    "locked": False,
                }, 
                {
                    "code": r"""
                    >>> integer_compare(4, 4)
                    'x and y are equal'
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