from ED6ScenarioHelper import *

def main():
    # 东柏斯街道

    CreateScenaFile(
        FileName            = 'R1101   ._SN',
        MapName             = 'Bose',
        Location            = 'R1101.x',
        MapIndex            = 55,
        MapDefaultBGM       = "ed60020",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Mechanic',                             # 9
        'Haulage Vehicle',                      # 10
        'Grant',                                # 11
        'Verte Bridge - Checkpoint',            # 12
        'Bose',                                 # 13
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 55,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT06/CH20078 ._CH',             # 00
        'ED6_DT07/CH01260 ._CH',             # 01
        'ED6_DT09/CH10290 ._CH',             # 02
        'ED6_DT09/CH10291 ._CH',             # 03
        'ED6_DT09/CH10320 ._CH',             # 04
        'ED6_DT09/CH10321 ._CH',             # 05
        'ED6_DT09/CH10350 ._CH',             # 06
        'ED6_DT09/CH10351 ._CH',             # 07
        'ED6_DT09/CH10870 ._CH',             # 08
        'ED6_DT09/CH10871 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT06/CH20078P._CP',             # 00
        'ED6_DT07/CH01260P._CP',             # 01
        'ED6_DT09/CH10290P._CP',             # 02
        'ED6_DT09/CH10291P._CP',             # 03
        'ED6_DT09/CH10320P._CP',             # 04
        'ED6_DT09/CH10321P._CP',             # 05
        'ED6_DT09/CH10350P._CP',             # 06
        'ED6_DT09/CH10351P._CP',             # 07
        'ED6_DT09/CH10870P._CP',             # 08
        'ED6_DT09/CH10871P._CP',             # 09
    )

    DeclNpc(
        X                   = -64160,
        Z                   = 0,
        Y                   = 28100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -64160,
        Z                   = 0,
        Y                   = 28100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -65150,
        Z                   = 0,
        Y                   = 26800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -10250,
        Z                   = 0,
        Y                   = -8450,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -106260,
        Z                   = 0,
        Y                   = -32340,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -46450,
        Z                   = 30,
        Y                   = 2310,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -72920,
        Z                   = -30,
        Y                   = 51450,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -97850,
        Z                   = -30,
        Y                   = 45380,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -90070,
        Z                   = 1040,
        Y                   = 27970,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -114180,
        Z                   = 80,
        Y                   = -40,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -71266,
        Y                   = -2000,
        Z                   = 12121,
        Range               = -55060,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x3E8F,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    ScpFunction(
        "Function_0_246",          # 00, 0
        "Function_1_247",          # 01, 1
        "Function_2_25F",          # 02, 2
        "Function_3_275",          # 03, 3
        "Function_4_AE5",          # 04, 4
        "Function_5_B29",          # 05, 5
    )


    def Function_0_246(): pass

    label("Function_0_246")

    Return()

    # Function_0_246 end

    def Function_1_247(): pass

    label("Function_1_247")

    OP_16(0x2, 0xFA0, 0xFFFCE708, 0xFFFE4698, 0x30016)
    OP_71(0x0, 0x4)
    Return()

    # Function_1_247 end

    def Function_2_25F(): pass

    label("Function_2_25F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_274")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_25F")

    label("loc_274")

    Return()

    # Function_2_25F end

    def Function_3_275(): pass

    label("Function_3_275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE4")
    OP_A2(0x305)
    OP_28(0x7, 0x4, 0x40)
    OP_28(0xC, 0x4, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x329)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_298")
    OP_28(0xD, 0x4, 0x40)

    label("loc_298")

    EventBegin(0x0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x0, 0xA, 400)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x1, 0xA, 400)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x2, 0xA, 400)
    Sleep(500)

    def lambda_2FF():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FF)

    def lambda_30D():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_30D)

    def lambda_31B():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_31B)

    ChrTalk(
        0x101,
        "#004FWhat's that headed this way...?\x02",
    )

    CloseMessageWindow()
    OP_72(0x0, 0x4)
    OP_71(0x0, 0x20)
    SetChrPos(0x9, -64060, 0, 32450, 180)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    OP_A1(0x9, 0x0)
    OP_71(0x0, 0x40)
    SetChrPos(0xA, -65360, 0, 30700, 180)
    OP_22(0xCF, 0x1, 0x64)
    OP_43(0x9, 0x2, 0x0, 0x4)

    def lambda_39F():
        OP_8F(0xFE, 0xFFFF054C, 0x0, 0x4BA0, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_39F)

    def lambda_3BA():
        OP_8E(0xFE, 0xFFFEFF7A, 0x0, 0x45F6, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3BA)
    LoadEffect(0x0, "map\\\\mp024_00.eff")
    PlayEffect(0x0, 0x0, 0x9, 0, 200, -7000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x9, 0, 200, -4000, 0, 0, 0, 1000, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)

    def lambda_471():
        OP_6C(335000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_471)
    OP_48()
    SetChrBattleFlags(0x8, 0x20)
    OP_89(0x8, -63900, 1600, 32000, 180)
    OP_6D(-63960, 0, 26270, 3000)
    SetChrPos(0x101, -66870, 0, 15150, 358)
    SetChrPos(0x102, -68360, 310, 16180, 55)
    SetChrPos(0x103, -67000, 10, 16650, 326)

    def lambda_4DC():

        label("loc_4DC")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4DC")

    QueueWorkItem2(0x101, 1, lambda_4DC)

    def lambda_4ED():

        label("loc_4ED")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4ED")

    QueueWorkItem2(0x102, 1, lambda_4ED)

    def lambda_4FE():

        label("loc_4FE")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4FE")

    QueueWorkItem2(0x103, 1, lambda_4FE)
    OP_6D(-65780, 0, 17980, 5000)
    WaitChrThread(0x9, 0x1)
    OP_24(0xCF, 0x50)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    WaitChrThread(0xA, 0x1)

    ChrTalk(
        0xA,
        (
            "#821F#4PWell, if it isn't Scherazard!\x01",
            "How have you been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#023FFine. I haven't seen you in a while,\x01",
            "either.\x02\x03",
            "What are you up to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#820F#4PAs you can see, I'm doing an\x01",
            "escort job.\x02\x03",
            "I'm sure that you've heard about all the\x01",
            "airliners being grounded after the Linde\x01",
            "incident, right?\x02\x03",
            "Because of that we have to move\x01",
            "all this cargo to the Royal City\x01",
            "by ground transport.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FI see. Well, your efforts are\x01",
            "appreciated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#820F#4PSo, how about yourself? What are\x01",
            "you doing with these youngsters?\x02\x03",
            "Don't tell me you're looking into\x01",
            "the incident...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#023FThat was the plan. Why? Do you know\x01",
            "something we should be aware of?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#823F#4PWell...\x02\x03",
            "#820FI think it would be best if you\x01",
            "spoke with Lugran about it at\x01",
            "the Bose branch.\x02\x03",
            "Anyway, I've got to get going.\x01",
            "Catch you later.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_851():
        OP_8E(0xFE, 0xFFFF0D58, 0x0, 0xFFFF649C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_851)
    Sleep(300)

    def lambda_871():
        OP_8F(0xFE, 0xFFFF0D58, 0x0, 0xFFFF649C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_871)
    OP_24(0xCF, 0x64)
    PlayEffect(0x0, 0x0, 0x9, 0, 200, -7000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x9, 0, 200, -4000, 0, 0, 0, 1000, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_6D(-67630, 60, 16050, 5000)
    OP_43(0x9, 0x2, 0x0, 0x5)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)

    ChrTalk(
        0x101,
        (
            "#505FChief Warrant Officer Ashton and now him...\x01",
            "Everyone keeps hinting at something, but no one will\x01",
            "just come out and say it. I wonder what's up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FWell, there must be a good reason for it,\x01",
            "and we'll probably find our answers at the\x01",
            "Bose branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026FAgreed. If we do as he suggests and ask\x01",
            "Lugran about it, we may just get a clue\x01",
            "as to what's going on.\x02\x03",
            "#020FAnyway, let's get moving.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_71(0x0, 0x4)
    EventEnd(0x0)

    label("loc_AE4")

    Return()

    # Function_3_275 end

    def Function_4_AE5(): pass

    label("Function_4_AE5")

    OP_24(0xCF, 0x41)
    Sleep(100)
    OP_24(0xCF, 0x46)
    Sleep(100)
    OP_24(0xCF, 0x4B)
    Sleep(100)
    OP_24(0xCF, 0x50)
    Sleep(100)
    OP_24(0xCF, 0x55)
    Sleep(100)
    OP_24(0xCF, 0x5A)
    Sleep(100)
    OP_24(0xCF, 0x5F)
    Sleep(100)
    OP_24(0xCF, 0x64)
    Return()

    # Function_4_AE5 end

    def Function_5_B29(): pass

    label("Function_5_B29")

    Sleep(1000)
    OP_24(0xCF, 0x5F)
    Sleep(100)
    OP_24(0xCF, 0x5A)
    Sleep(100)
    OP_24(0xCF, 0x55)
    Sleep(100)
    OP_24(0xCF, 0x50)
    Sleep(100)
    OP_24(0xCF, 0x4B)
    Sleep(100)
    OP_24(0xCF, 0x46)
    Sleep(100)
    OP_24(0xCF, 0x41)
    Sleep(100)
    OP_23(0xCF)
    Return()

    # Function_5_B29 end

    SaveToFile()

Try(main)
