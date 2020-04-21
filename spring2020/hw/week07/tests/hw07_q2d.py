test = {
    "name": "Question 2, Part D",       # name of the test
    "points": 4,       # number of points for the entire suite
    "hidden": False,    # whether the test is hidden on Gradescope
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases, each case is a dict
                {
                    "code": r"""
                    >>> callable( crack_vigenere )
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> crack_vigenere(ciphertext_1)
                    'alicewasbeginningtogetverytiredofsittingbyhersisteronthebankandofhavingnothingtodoonceortwiceshehadpeepedintothebookhersisterwasreadingbutithadnopicturesorconversationsinitandwhatistheuseofabookthoughtalicewithoutpicturesorconversationssoshewasconsideringinherownmindaswellasshecouldforthehotdaymadeherfeelverysleepyandstupidwhetherthepleasureofmakingadaisychainwouldbeworththetroubleofgettingupandpickingthedaisieswhensuddenlyawhiterabbitwithpinkeyesranclosebyhertherewasnothingsoveryremarkableinthatnordidalicethinkitsoverymuchoutofthewaytoheartherabbitsaytoitselfohdearohdearishallbelatewhenshethoughtitoverafterwardsitoccurredtoherthatsheoughttohavewonderedatthisbutatthetimeitallseemedquitenaturalbutwhentherabbitactuallytookawatchoutofitswaistcoatpocketandlookedatitandthenhurriedonalicestartedtoherfeetforitflashedacrosshermindthatshehadneverbeforeseenarabbitwitheitherawaistcoatpocketorawatchtotakeoutofitandburningwithcuriositysheranacrossthefieldafteritandfortunatelywasjustintimetoseeitpopdownalargerabbitholeunderthehedge'
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> crack_vigenere(ciphertext_2, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                    'margarettheeldestofthefourwassixteenandveryprettybeingplumpandfairwithlargeeyesplentyofsoftbrownhairasweetmouthandwhitehandsofwhichshewasrathervainfifteenyearoldjowasverytallthinandbrownandremindedoneofacoltforsheneverseemedtoknowwhattodowithherlonglimbswhichwereverymuchinherwayshehadadecidedmouthacomicalnoseandsharpgrayeyeswhichappearedtoseeeverythingandwerebyturnsfiercefunnyorthoughtfulherlongthickhairwasheronebeautybutitwasusuallybundledintoanettobeoutofherwayroundshouldershadjobighandsandfeetaflyawaylooktoherclothesandtheuncomfortableappearanceofagirlwhowasrapidlyshootingupintoawomananddidntlikeitelizabethorbethaseveryonecalledherwasarosysmoothhairedbrighteyedgirlofthirteenwithashymanneratimidvoiceandapeacefulexpressionwhichwasseldomdisturbedherfathercalledherlittlemisstranquilityandthenamesuitedherexcellentlyforsheseemedtoliveinahappyworldofherownonlyventuringouttomeetthefewwhomshetrustedandlovedamythoughtheyoungestwasamostimportantpersoninherownopinionatleastaregularsnowmaidenwithblueeyesandyellowhaircurlingonhershoulderspaleandslenderandalwayscarryingherselflikeayoungladymindfulofhermannerswhatthecharactersofthefoursisterswerewewillleavetobefoundout'
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