from ED6ScenarioHelper import *

def main():
    # 神秘森林

    CreateScenaFile(
        FileName            = 'C0301   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0301.x',
        MapIndex            = 19,
        MapDefaultBGM       = "ed60021",
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
    )

    DeclEntryPoint(
        Unknown_00              = 35000,
        Unknown_04              = 0,
        Unknown_08              = 16000,
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
        Unknown_3A              = 19,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10010 ._CH',             # 00
        'ED6_DT09/CH10011 ._CH',             # 01
        'ED6_DT09/CH10280 ._CH',             # 02
        'ED6_DT09/CH10281 ._CH',             # 03
        'ED6_DT09/CH10230 ._CH',             # 04
        'ED6_DT09/CH10231 ._CH',             # 05
        'ED6_DT09/CH10240 ._CH',             # 06
        'ED6_DT09/CH10241 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10010P._CP',             # 00
        'ED6_DT09/CH10011P._CP',             # 01
        'ED6_DT09/CH10280P._CP',             # 02
        'ED6_DT09/CH10281P._CP',             # 03
        'ED6_DT09/CH10230P._CP',             # 04
        'ED6_DT09/CH10231P._CP',             # 05
        'ED6_DT09/CH10240P._CP',             # 06
        'ED6_DT09/CH10241P._CP',             # 07
    )

    DeclMonster(
        X                   = -5000,
        Z                   = 0,
        Y                   = -28000,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x48,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -13000,
        Z                   = -300,
        Y                   = -11000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x4E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 17000,
        Z                   = -300,
        Y                   = -5000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x43,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -23000,
        Z                   = 0,
        Y                   = 32000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x43,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7000,
        Z                   = -100,
        Y                   = -27000,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x4F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 2000,
        Z                   = 0,
        Y                   = -4000,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x46,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21000,
        Z                   = -300,
        Y                   = 11000,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x49,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -16000,
        Z                   = -300,
        Y                   = -3000,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x47,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5000,
        Z                   = 0,
        Y                   = 14000,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x4D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 1000,
        Z                   = 0,
        Y                   = 26000,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x46,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -7330,
        TriggerZ            = 0,
        TriggerY            = 800,
        TriggerRange        = 1500,
        ActorX              = -7330,
        ActorZ              = 1500,
        ActorY              = 800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 10760,
        TriggerZ            = 0,
        TriggerY            = 21620,
        TriggerRange        = 1500,
        ActorX              = 10760,
        ActorZ              = 1500,
        ActorY              = 21620,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_24A",          # 00, 0
        "Function_1_24B",          # 01, 1
        "Function_2_28C",          # 02, 2
        "Function_3_356",          # 03, 3
    )


    def Function_0_24A(): pass

    label("Function_0_24A")

    Return()

    # Function_0_24A end

    def Function_1_24B(): pass

    label("Function_1_24B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 4)), scpexpr(EXPR_END)), "loc_260")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_64(0x0, 0x1)

    label("loc_260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 5)), scpexpr(EXPR_END)), "loc_275")
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_64(0x1, 0x1)

    label("loc_275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 5)), scpexpr(EXPR_END)), "loc_285")
    OP_10(0x1, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_28B")

    label("loc_285")

    OP_10(0x1, 0x1)
    OP_10(0x3, 0x0)

    label("loc_28B")

    Return()

    # Function_1_24B end

    def Function_2_28C(): pass

    label("Function_2_28C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x386, 1)"), scpexpr(EXPR_END)), "loc_2FD")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "熊刺草\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_64(0x0, 0x1)
    OP_A2(0x284)
    Jump("loc_34D")

    label("loc_2FD")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "熊刺草\x07\x00",
            "发现了，\x01\x07\x00",
            "不过现有的数量太多，不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_34D")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_28C end

    def Function_3_356(): pass

    label("Function_3_356")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_417")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x386, 1)"), scpexpr(EXPR_END)), "loc_3C7")
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "熊刺草\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_64(0x1, 0x1)
    OP_A2(0x285)
    Jump("loc_417")

    label("loc_3C7")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "熊刺草\x07\x00",
            "发现了，\x01\x07\x00",
            "不过现有的数量太多，不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_417")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_356 end

    SaveToFile()

Try(main)
