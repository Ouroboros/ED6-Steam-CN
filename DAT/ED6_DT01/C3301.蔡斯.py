from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3301   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3301.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60032",
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
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10630 ._CH',             # 00
        'ED6_DT09/CH10631 ._CH',             # 01
        'ED6_DT09/CH10640 ._CH',             # 02
        'ED6_DT09/CH10641 ._CH',             # 03
        'ED6_DT09/CH10650 ._CH',             # 04
        'ED6_DT09/CH10651 ._CH',             # 05
        'ED6_DT09/CH10660 ._CH',             # 06
        'ED6_DT09/CH10661 ._CH',             # 07
        'ED6_DT09/CH10670 ._CH',             # 08
        'ED6_DT09/CH10671 ._CH',             # 09
        'ED6_DT09/CH10680 ._CH',             # 0A
        'ED6_DT09/CH10681 ._CH',             # 0B
        'ED6_DT09/CH10690 ._CH',             # 0C
        'ED6_DT09/CH10691 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT09/CH10630P._CP',             # 00
        'ED6_DT09/CH10631P._CP',             # 01
        'ED6_DT09/CH10640P._CP',             # 02
        'ED6_DT09/CH10641P._CP',             # 03
        'ED6_DT09/CH10650P._CP',             # 04
        'ED6_DT09/CH10651P._CP',             # 05
        'ED6_DT09/CH10660P._CP',             # 06
        'ED6_DT09/CH10661P._CP',             # 07
        'ED6_DT09/CH10670P._CP',             # 08
        'ED6_DT09/CH10671P._CP',             # 09
        'ED6_DT09/CH10680P._CP',             # 0A
        'ED6_DT09/CH10681P._CP',             # 0B
        'ED6_DT09/CH10690P._CP',             # 0C
        'ED6_DT09/CH10691P._CP',             # 0D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 151480,
        Z                   = 10,
        Y                   = -36090,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 173520,
        Z                   = -30,
        Y                   = -9860,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1EB,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 145980,
        Z                   = 0,
        Y                   = -16110,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1ED,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 133740,
        Z                   = -10,
        Y                   = -17360,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1EF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 100000,
        Z                   = 40,
        Y                   = -11970,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 103250,
        Z                   = 60,
        Y                   = -23320,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 86210,
        Z                   = -10,
        Y                   = -27450,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 68170,
        Z                   = 20,
        Y                   = -25410,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1EA,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 158010,
        TriggerZ            = 30,
        TriggerY            = -64629,
        TriggerRange        = 1000,
        ActorX              = 157660,
        ActorZ              = 1530,
        ActorY              = -65230,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 140470,
        TriggerZ            = -30,
        TriggerY            = -11410,
        TriggerRange        = 1000,
        ActorX              = 140500,
        ActorZ              = 1470,
        ActorY              = -10700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 90610,
        TriggerZ            = 50,
        TriggerY            = -19930,
        TriggerRange        = 1000,
        ActorX              = 91210,
        ActorZ              = 1550,
        ActorY              = -19850,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 97500,
        TriggerZ            = -20,
        TriggerY            = -18130,
        TriggerRange        = 1000,
        ActorX              = 96830,
        ActorZ              = 1480,
        ActorY              = -18060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2CA",          # 00, 0
        "Function_1_2CB",          # 01, 1
        "Function_2_335",          # 02, 2
        "Function_3_403",          # 03, 3
        "Function_4_576",          # 04, 4
        "Function_5_75D",          # 05, 5
        "Function_6_97A",          # 06, 6
    )


    def Function_0_2CA(): pass

    label("Function_0_2CA")

    Return()

    # Function_0_2CA end

    def Function_1_2CB(): pass

    label("Function_1_2CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DD")
    OP_6F(0x0, 0)
    Jump("loc_2E4")

    label("loc_2DD")

    OP_6F(0x0, 60)

    label("loc_2E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F6")
    OP_6F(0x1, 0)
    Jump("loc_2FD")

    label("loc_2F6")

    OP_6F(0x1, 60)

    label("loc_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30F")
    OP_6F(0x2, 0)
    Jump("loc_316")

    label("loc_30F")

    OP_6F(0x2, 60)

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328")
    OP_6F(0x3, 0)
    Jump("loc_32F")

    label("loc_328")

    OP_6F(0x3, 60)

    label("loc_32F")

    OP_22(0x1CD, 0x1, 0x64)
    Return()

    # Function_1_2CB end

    def Function_2_335(): pass

    label("Function_2_335")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35A")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3ED")

    label("loc_35A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_373")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3ED")

    label("loc_373")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38C")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3ED")

    label("loc_38C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A5")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3ED")

    label("loc_3A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BE")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3ED")

    label("loc_3BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D7")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3ED")

    label("loc_3D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ED")
    OP_99(0xFE, 0x6, 0x7, 0x546)

    label("loc_3ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_402")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3ED")

    label("loc_402")

    Return()

    # Function_2_335 end

    def Function_3_403(): pass

    label("Function_3_403")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_47A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "大回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x5C1)
    Jump("loc_4F2")

    label("loc_47A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "大回复药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "大回复药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_4F2")

    Jump("loc_568")

    label("loc_4F5")

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
    OP_83(0xF, 0x26)

    label("loc_568")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_403 end

    def Function_4_576(): pass

    label("Function_4_576")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_716")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_658")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 140500, 2970, -10700, 320)
    TurnDirection(0x8, 0x0, 0)

    def lambda_5C5():
        OP_8F(0xFE, 0x224D4, 0x5BE, 0xFFFFD634, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5C5)

    def lambda_5E0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5E0)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x1F2, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_633"),
        (2, "loc_645"),
        (1, "loc_655"),
        (SWITCH_DEFAULT, "loc_658"),
    )


    label("loc_633")

    OP_A2(0x5C7)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_658")

    label("loc_645")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_655")

    OP_B4(0x0)
    Return()

    label("loc_658")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x25D, 1)"), scpexpr(EXPR_END)), "loc_6A9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "ＥＰ３\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x5C2)
    Jump("loc_713")

    label("loc_6A9")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "ＥＰ３\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "ＥＰ３\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_713")

    Jump("loc_74F")

    label("loc_716")

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
    OP_83(0xF, 0x27)

    label("loc_74F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_576 end

    def Function_5_75D(): pass

    label("Function_5_75D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_909")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83F")
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 91210, 3050, -19850, 320)
    TurnDirection(0x9, 0x0, 0)

    def lambda_7AC():
        OP_8F(0xFE, 0x1644A, 0x60E, 0xFFFFB276, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7AC)

    def lambda_7C7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7C7)
    ClearChrFlags(0x9, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x1F2, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_81A"),
        (2, "loc_82C"),
        (1, "loc_83C"),
        (SWITCH_DEFAULT, "loc_83F"),
    )


    label("loc_81A")

    OP_A2(0x5C8)
    OP_6F(0x2, 60)
    Sleep(500)
    Jump("loc_83F")

    label("loc_82C")

    OP_6F(0x2, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_83C")

    OP_B4(0x0)
    Return()

    label("loc_83F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xB9, 1)"), scpexpr(EXPR_END)), "loc_894")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "Ｇ－冲击炮\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x5C3)
    Jump("loc_906")

    label("loc_894")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "Ｇ－冲击炮\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "Ｇ－冲击炮\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_906")

    Jump("loc_96C")

    label("loc_909")

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
    OP_83(0xF, 0x28)

    label("loc_96C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_75D end

    def Function_6_97A(): pass

    label("Function_6_97A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_9F1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "大回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x5C4)
    Jump("loc_A69")

    label("loc_9F1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "大回复药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "大回复药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_A69")

    Jump("loc_AA7")

    label("loc_A6C")

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
    OP_83(0xF, 0x29)

    label("loc_AA7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_97A end

    SaveToFile()

Try(main)
