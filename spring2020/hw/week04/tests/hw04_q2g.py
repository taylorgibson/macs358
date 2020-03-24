test = {
    "name": "Question 2, Part g",       # name of the test
    "points": 2,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> caesar( ciphertext, key_used, False )
                    'havinghadsometimeatmydisposalwheninlondonihadvisitedthebritishmuseumandmadesearchamongthebooksandmapsinthelibraryregardingtransylvaniaithadstruckmethatsomeforeknowledgeofthecountrycouldhardlyfailtohavesomeimportanceindealingwithanoblemanofthatcountryifindthatthedistricthenamedisintheextremeeastofthecountryjustonthebordersofthreestatestransylvaniamoldaviaandbukovinainthemidstofthecarpathianmountainsoneofthewildestandleastknownportionsofeuropeiwasnotabletolightonanymaporworkgivingtheexactlocalityofthecastledraculaastherearenomapsofthiscountryasyettocomparewithourownordnancesurveymapsbutifoundthatbistritztheposttownnamedbycountdraculaisafairlywellknownplaceishallenterheresomeofmynotesastheymayrefreshmymemorywhenitalkovermytravelswithmina'
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