from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'C2115   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2115.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        'ED6_DT09/CH10560 ._CH',             # 00
        'ED6_DT09/CH10561 ._CH',             # 01
        'ED6_DT09/CH10570 ._CH',             # 02
        'ED6_DT09/CH10571 ._CH',             # 03
        'ED6_DT09/CH10580 ._CH',             # 04
        'ED6_DT09/CH10581 ._CH',             # 05
        'ED6_DT09/CH10590 ._CH',             # 06
        'ED6_DT09/CH10591 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10560P._CP',             # 00
        'ED6_DT09/CH10561P._CP',             # 01
        'ED6_DT09/CH10570P._CP',             # 02
        'ED6_DT09/CH10571P._CP',             # 03
        'ED6_DT09/CH10580P._CP',             # 04
        'ED6_DT09/CH10581P._CP',             # 05
        'ED6_DT09/CH10590P._CP',             # 06
        'ED6_DT09/CH10591P._CP',             # 07
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 3970,
        Z                   = 0,
        Y                   = 3770,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1BC,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -8230,
        TriggerZ            = 0,
        TriggerY            = 8330,
        TriggerRange        = 1000,
        ActorX              = -8730,
        ActorZ              = 0,
        ActorY              = 8830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9350,
        TriggerZ            = 0,
        TriggerY            = 9330,
        TriggerRange        = 1000,
        ActorX              = 8850,
        ActorZ              = 0,
        ActorY              = 8830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 12530,
        TriggerZ            = 0,
        TriggerY            = -660,
        TriggerRange        = 1000,
        ActorX              = 12530,
        ActorZ              = 0,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -12430,
        TriggerZ            = 0,
        TriggerY            = -640,
        TriggerRange        = 1000,
        ActorX              = -12430,
        ActorZ              = 0,
        ActorY              = 110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4470,
        TriggerZ            = 0,
        TriggerY            = 22500,
        TriggerRange        = 1000,
        ActorX              = 4690,
        ActorZ              = 0,
        ActorY              = 23200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_23A",          # 00, 0
        "Function_1_23B",          # 01, 1
        "Function_2_2D5",          # 02, 2
        "Function_3_2EB",          # 03, 3
        "Function_4_4FA",          # 04, 4
        "Function_5_6D9",          # 05, 5
        "Function_6_8E3",          # 06, 6
        "Function_7_AE3",          # 07, 7
    )


    def Function_0_23A(): pass

    label("Function_0_23A")

    Return()

    # Function_0_23A end

    def Function_1_23B(): pass

    label("Function_1_23B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D")
    OP_6F(0x0, 0)
    Jump("loc_254")

    label("loc_24D")

    OP_6F(0x0, 60)

    label("loc_254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_266")
    OP_6F(0x1, 0)
    Jump("loc_26D")

    label("loc_266")

    OP_6F(0x1, 60)

    label("loc_26D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F")
    OP_6F(0x2, 0)
    Jump("loc_286")

    label("loc_27F")

    OP_6F(0x2, 60)

    label("loc_286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_298")
    OP_6F(0x3, 0)
    Jump("loc_29F")

    label("loc_298")

    OP_6F(0x3, 60)

    label("loc_29F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B1")
    OP_6F(0x4, 0)
    Jump("loc_2B8")

    label("loc_2B1")

    OP_6F(0x4, 60)

    label("loc_2B8")

    SoundDistance(0x1CB, 0xFFFFFFA6, 0x0, 0x96, 0x7D0, 0x61A8, 0x64, 0x0)
    Return()

    # Function_1_23B end

    def Function_2_2D5(): pass

    label("Function_2_2D5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2EA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2D5")

    label("loc_2EA")

    Return()

    # Function_2_2D5 end

    def Function_3_2EB(): pass

    label("Function_3_2EB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, -8730, 3000, 8830, 320)
    TurnDirection(0x8, 0x0, 0)

    def lambda_33A():
        OP_8F(0xFE, 0xFFFFDDE6, 0x5DC, 0x227E, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_33A)

    def lambda_355():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_355)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x1BD, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_3A8"),
        (2, "loc_3BA"),
        (1, "loc_3CA"),
        (SWITCH_DEFAULT, "loc_3CD"),
    )


    label("loc_3A8")

    OP_A2(0x4AF)
    OP_6F(0x0, 60)
    Sleep(500)
    Jump("loc_3CD")

    label("loc_3BA")

    OP_6F(0x0, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_3CA")

    OP_B4(0x0)
    Return()

    label("loc_3CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x7B, 1)"), scpexpr(EXPR_END)), "loc_423")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "水纹剑\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4AE)
    Jump("loc_497")

    label("loc_423")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "水纹剑\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "水纹剑\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_497")

    Jump("loc_4EC")

    label("loc_49A")

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
    OP_83(0xF, 0x20)

    label("loc_4EC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2EB end

    def Function_4_4FA(): pass

    label("Function_4_4FA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DC")
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 8850, 3000, 8830, 320)
    TurnDirection(0x9, 0x0, 0)

    def lambda_549():
        OP_8F(0xFE, 0x2292, 0x5DC, 0x227E, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_549)

    def lambda_564():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_564)
    ClearChrFlags(0x9, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x1BD, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_5B7"),
        (2, "loc_5C9"),
        (1, "loc_5D9"),
        (SWITCH_DEFAULT, "loc_5DC"),
    )


    label("loc_5B7")

    OP_A2(0x4B1)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_5DC")

    label("loc_5C9")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_5D9")

    OP_B4(0x0)
    Return()

    label("loc_5DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D0, 1)"), scpexpr(EXPR_END)), "loc_62E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "美臭\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4B0)
    Jump("loc_69A")

    label("loc_62E")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "美臭\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "美臭\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_69A")

    Jump("loc_6CB")

    label("loc_69D")

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
    OP_83(0xF, 0x21)

    label("loc_6CB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_4FA end

    def Function_5_6D9(): pass

    label("Function_5_6D9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BB")
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, 12530, 3000, 0, 320)
    TurnDirection(0xA, 0x0, 0)

    def lambda_728():
        OP_8F(0xFE, 0x30F2, 0x5DC, 0x0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_728)

    def lambda_743():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_743)
    ClearChrFlags(0xA, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x1BD, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_796"),
        (2, "loc_7A8"),
        (1, "loc_7B8"),
        (SWITCH_DEFAULT, "loc_7BB"),
    )


    label("loc_796")

    OP_A2(0x4B3)
    OP_6F(0x2, 60)
    Sleep(500)
    Jump("loc_7BB")

    label("loc_7A8")

    OP_6F(0x2, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_7B8")

    OP_B4(0x0)
    Return()

    label("loc_7BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xF9, 1)"), scpexpr(EXPR_END)), "loc_813")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "战斗服\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4B2)
    Jump("loc_88B")

    label("loc_813")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "战斗服\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "战斗服\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_88B")

    Jump("loc_8D5")

    label("loc_88E")

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
    OP_83(0xF, 0x22)

    label("loc_8D5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_6D9 end

    def Function_6_8E3(): pass

    label("Function_6_8E3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A95")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C5")
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, -12430, 3000, 110, 320)
    TurnDirection(0xB, 0x0, 0)

    def lambda_932():
        OP_8F(0xFE, 0xFFFFCF72, 0x5DC, 0x6E, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_932)

    def lambda_94D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_94D)
    ClearChrFlags(0xB, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x1BD, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_9A0"),
        (2, "loc_9B2"),
        (1, "loc_9C2"),
        (SWITCH_DEFAULT, "loc_9C5"),
    )


    label("loc_9A0")

    OP_A2(0x4B5)
    OP_6F(0x3, 60)
    Sleep(500)
    Jump("loc_9C5")

    label("loc_9B2")

    OP_6F(0x3, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_9C2")

    OP_B4(0x0)
    Return()

    label("loc_9C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x117, 1)"), scpexpr(EXPR_END)), "loc_A1C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "军用靴\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4B4)
    Jump("loc_A92")

    label("loc_A1C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "军用靴\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "军用靴\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_A92")

    Jump("loc_AD5")

    label("loc_A95")

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
    OP_83(0xF, 0x23)

    label("loc_AD5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_8E3 end

    def Function_7_AE3(): pass

    label("Function_7_AE3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_B59")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4B6)
    Jump("loc_BCF")

    label("loc_B59")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_BCF")

    Jump("loc_C22")

    label("loc_BD2")

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
    OP_83(0xF, 0x24)

    label("loc_C22")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_AE3 end

    SaveToFile()

Try(main)
