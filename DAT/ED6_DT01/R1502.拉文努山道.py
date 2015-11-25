from ED6ScenarioHelper import *

def main():
    # 拉文努山道

    CreateScenaFile(
        FileName            = 'R1502   ._SN',
        MapName             = 'Bose',
        Location            = 'R1502.x',
        MapIndex            = 59,
        MapDefaultBGM       = "ed60022",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/R1502   ._SN',
            'ED6_DT01/R1502_1 ._SN',
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
        '魔兽',                                 # 9
        '拉文努村方向',                         # 10
        '拉文努村废坑方向',                     # 11
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
        Unknown_3A              = 59,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10860 ._CH',             # 00
        'ED6_DT09/CH10861 ._CH',             # 01
        'ED6_DT09/CH10862 ._CH',             # 02
        'ED6_DT07/CH00100 ._CH',             # 03
        'ED6_DT07/CH00110 ._CH',             # 04
        'ED6_DT07/CH00120 ._CH',             # 05
        'ED6_DT09/CH10030 ._CH',             # 06
        'ED6_DT09/CH10031 ._CH',             # 07
        'ED6_DT09/CH10330 ._CH',             # 08
        'ED6_DT09/CH10331 ._CH',             # 09
        'ED6_DT09/CH10310 ._CH',             # 0A
        'ED6_DT09/CH10311 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT09/CH10860P._CP',             # 00
        'ED6_DT09/CH10861P._CP',             # 01
        'ED6_DT09/CH10862P._CP',             # 02
        'ED6_DT07/CH00100P._CP',             # 03
        'ED6_DT07/CH00110P._CP',             # 04
        'ED6_DT07/CH00120P._CP',             # 05
        'ED6_DT09/CH10030P._CP',             # 06
        'ED6_DT09/CH10031P._CP',             # 07
        'ED6_DT09/CH10330P._CP',             # 08
        'ED6_DT09/CH10331P._CP',             # 09
        'ED6_DT09/CH10310P._CP',             # 0A
        'ED6_DT09/CH10311P._CP',             # 0B
    )

    DeclNpc(
        X                   = -73840,
        Z                   = -50,
        Y                   = -1150,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -4760,
        Z                   = 10,
        Y                   = -38310,
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
        X                   = -62970,
        Z                   = -30,
        Y                   = 86680,
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
        X                   = -31260,
        Z                   = -20,
        Y                   = -41320,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -40880,
        Z                   = 20,
        Y                   = -10170,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x132,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35910,
        Z                   = -40,
        Y                   = 12760,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -16540,
        Z                   = -20,
        Y                   = 5850,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -88970,
        Z                   = -90,
        Y                   = -16370,
        Unknown_0C          = 0,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x131,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -70020,
        Z                   = -20,
        Y                   = 24980,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -81390,
        Z                   = -70,
        Y                   = 41540,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -73200,
        Y                   = -1000,
        Z                   = 430,
        Range               = -70000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFE3AE,
        Unknown_18          = 0x10000,
        Unknown_1C          = 0,
    )


    DeclActor(
        TriggerX            = -98600,
        TriggerZ            = -90,
        TriggerY            = 21830,
        TriggerRange        = 1000,
        ActorX              = -98170,
        ActorZ              = 1490,
        ActorY              = 22340,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_272",          # 00, 0
        "Function_1_273",          # 01, 1
        "Function_2_2B5",          # 02, 2
        "Function_3_2CB",          # 03, 3
    )


    def Function_0_272(): pass

    label("Function_0_272")

    Return()

    # Function_0_272 end

    def Function_1_273(): pass

    label("Function_1_273")

    OP_16(0x2, 0xFA0, 0xFFFD40E0, 0xFFFE4698, 0x30021)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_295")
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_29B")

    label("loc_295")

    OP_10(0x1, 0x1)
    OP_10(0x2, 0x0)

    label("loc_29B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AD")
    OP_6F(0x0, 0)
    Jump("loc_2B4")

    label("loc_2AD")

    OP_6F(0x0, 60)

    label("loc_2B4")

    Return()

    # Function_1_273 end

    def Function_2_2B5(): pass

    label("Function_2_2B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2B5")

    label("loc_2CA")

    Return()

    # Function_2_2B5 end

    def Function_3_2CB(): pass

    label("Function_3_2CB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_341")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x37B)
    Jump("loc_3B7")

    label("loc_341")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "回复药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "回复药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_3B7")

    Jump("loc_3E4")

    label("loc_3BA")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x81)

    label("loc_3E4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2CB end

    SaveToFile()

Try(main)
