test = {
    "name": "Question 2, Part A",       # name of the test
    "points": 4,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> callable( text_split )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> text_split('Hello', 5)
                    ['H', 'E', 'L', 'L', 'O']
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> text_split('Cryptography is Awesome', 6)
                    ['CGIO', 'RRSM', 'YAAE', 'PPW', 'THE', 'OYS']
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> text_split( ciphertext_1, 15 )
                    ['CRUAHAMPKFIWZZSUGMVZLQITKLZBBTWOQMTUAKELWAKPKLUDVLFSBSSZGWVBAVMVTPKTB', 'SISZVUURZWIEBVMZDPPKZHJEUGRYLIJICPILWHJPNCSKIPMLBQEVZYJWOGMGWIGWPASRV', 'MAHWUOLLXAUWYCAWEONLWVACAAIIUQHJIAVGYGVSLYJXKUPWEBVHIBPZELVSKCZKXDUVU', 'USZVSKAVWMVKIXXYKIHGIUPPGVBFIKVLJLOJIKPALHLQXVBUDXWCMVBLVROEEIQASELII', 'LYMLHSYBYLVUWLZAJJWOGWVVBGTHPATEFSMVCSUMPKVOJMVBSGSAGHWZUSIRMRKPUKILT', 'ELLVOFIYEOUMZVGRWVKSSVTXTBSMSKPRZAFYYKINBPLEPVRYGMUMKVPDMYJILKCVLQAVA', 'RBAGEVJIRIVLIHVXEEOLZBNEUJUKCAQWVVRLXACLFBONWHCIKQRLSVCMMIHLSUUJWCASL', 'WMQUNSHDWUVHGPBKWEMKWTLFFCLPSLZPQFQVZWYGZFILTPATSKMHFLZPISEVMKOKSJXIW', 'DIEBPFHVTRMVMAVVKQTIYAEHGIGMDHIVCVKNLWMUGGKEBDYHQWKVHWLKTFRZAOILTXFJO', 'LTKYVJHSLQIUIJWRKKSPGKKMDQMJPPTXYFWKZSKWYEWFBZJFRYEUTYWXIKMRWPJPAKTZM', 'KFDIXMLCEWTASMZKIUWQJEBKSMEAZVFZOPQLRNOZEBJRRMHTEHPXZNKZIAUAWBHVYUFXU', 'AXFDRFMOVMZJSNWZJHSCPYZFJKRJXBPPSHCGFFILXVLFXVTPOMKJGVIHXAACMYVHFXVJK', 'UALHQVGMPUEHQMIWPSHKGIVKAWMLGIVVISIDDLCBAJSLVQSBHKPLGITBVAGAVGRNHAAVG', 'VYWRAVIIVALXRVGJVZXILVSYPAFRYAVXTSJEPFPYMLMVOGYRBAGRZVVJZAGGHWGKBTFP', 'ZMYCLDFWXCPAXOQLXEVZTOHEKBNKELVWVQFQXLDSILNWIKVGTKVZXMQLVPHZRYTIVMHW']
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