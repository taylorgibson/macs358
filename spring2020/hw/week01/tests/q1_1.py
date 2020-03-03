test = {
  'name': 'q1_1',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(q1_name, str)
          True
          """,
          'hidden': False,
          'locked': False
        }, 
        {
          'code': r"""
          >>> q1_name.find(' ') == -1
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> q1_name == q1_name.title()
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}