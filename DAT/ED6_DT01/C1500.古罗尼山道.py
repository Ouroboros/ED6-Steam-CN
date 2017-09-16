from ED6ScenarioHelper import *

def main():
    # 古罗尼山道

    CreateScenaFile(
        FileName            = 'C1500   ._SN',
        MapName             = 'Bose',
        Location            = 'C1500.x',
        MapIndex            = 61,
        MapDefaultBGM       = "ed60022",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/C1500   ._SN',
            'ED6_DT01/C1500_1 ._SN',
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
        '魔兽',                                 # 10
        '魔兽',                                 # 11
        '魔兽',                                 # 12
        '魔兽',                                 # 13
        '魔兽',                                 # 14
        '魔兽',                                 # 15
        '魔兽',                                 # 16
        '照相机',                               # 17
        '艾丝蒂尔',                             # 18
        '约修亚',                               # 19
        '雪拉扎德',                             # 20
        '古罗尼山道·关所方向',                 # 21
        '西柏斯街道方向',                       # 22
    )

    DeclEntryPoint(
        Unknown_00              = -130600,
        Unknown_04              = -40,
        Unknown_08              = 178500,
        Unknown_0C              = 4,
        Unknown_0E              = 225,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 260,
        Unknown_32              = 240,
        Unknown_34              = 300,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 61,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10140 ._CH',             # 00
        'ED6_DT09/CH10141 ._CH',             # 01
        'ED6_DT07/CH00100 ._CH',             # 02
        'ED6_DT07/CH00110 ._CH',             # 03
        'ED6_DT07/CH00120 ._CH',             # 04
        'ED6_DT07/CH00101 ._CH',             # 05
        'ED6_DT07/CH00111 ._CH',             # 06
        'ED6_DT07/CH00121 ._CH',             # 07
        'ED6_DT07/CH00102 ._CH',             # 08
        'ED6_DT09/CH10200 ._CH',             # 09
        'ED6_DT09/CH10201 ._CH',             # 0A
        'ED6_DT09/CH10880 ._CH',             # 0B
        'ED6_DT09/CH10881 ._CH',             # 0C
        'ED6_DT09/CH11160 ._CH',             # 0D
        'ED6_DT09/CH11161 ._CH',             # 0E
        'ED6_DT09/CH10870 ._CH',             # 0F
        'ED6_DT09/CH10871 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT09/CH10140P._CP',             # 00
        'ED6_DT09/CH10141P._CP',             # 01
        'ED6_DT07/CH00100P._CP',             # 02
        'ED6_DT07/CH00110P._CP',             # 03
        'ED6_DT07/CH00120P._CP',             # 04
        'ED6_DT07/CH00101P._CP',             # 05
        'ED6_DT07/CH00111P._CP',             # 06
        'ED6_DT07/CH00121P._CP',             # 07
        'ED6_DT07/CH00102P._CP',             # 08
        'ED6_DT09/CH10200P._CP',             # 09
        'ED6_DT09/CH10201P._CP',             # 0A
        'ED6_DT09/CH10880P._CP',             # 0B
        'ED6_DT09/CH10881P._CP',             # 0C
        'ED6_DT09/CH11160P._CP',             # 0D
        'ED6_DT09/CH11161P._CP',             # 0E
        'ED6_DT09/CH10870P._CP',             # 0F
        'ED6_DT09/CH10871P._CP',             # 10
    )

    DeclNpc(
        X                   = -150000,
        Z                   = 7800,
        Y                   = 63100,
        Direction           = 0,
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
        X                   = -150000,
        Z                   = 7800,
        Y                   = 63100,
        Direction           = 0,
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
        X                   = -150000,
        Z                   = 7800,
        Y                   = 63100,
        Direction           = 0,
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
        X                   = -150000,
        Z                   = 7800,
        Y                   = 63100,
        Direction           = 0,
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
        X                   = -150300,
        Z                   = 6800,
        Y                   = 90200,
        Direction           = 0,
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
        X                   = -150300,
        Z                   = 6800,
        Y                   = 90200,
        Direction           = 0,
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
        X                   = -150300,
        Z                   = 6800,
        Y                   = 90200,
        Direction           = 0,
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
        X                   = -150300,
        Z                   = 6800,
        Y                   = 90200,
        Direction           = 0,
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
        X                   = 99000,
        Z                   = 0,
        Y                   = 99000,
        Direction           = 0,
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
        X                   = 99000,
        Z                   = 0,
        Y                   = 99000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 99000,
        Z                   = 0,
        Y                   = 99000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 99000,
        Z                   = 0,
        Y                   = 99000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -140810,
        Z                   = 6010,
        Y                   = -31010,
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
        X                   = -119390,
        Z                   = -60,
        Y                   = 180920,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -146390,
        Z                   = 2009,
        Y                   = 152190,
        Unknown_0C          = 0,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCA,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -148000,
        Z                   = 2090,
        Y                   = 136280,
        Unknown_0C          = 0,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -154200,
        Z                   = 1990,
        Y                   = 120790,
        Unknown_0C          = 0,
        Unknown_0E          = 13,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCC,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -154710,
        Z                   = 4070,
        Y                   = 99880,
        Unknown_0C          = 58,
        Unknown_0E          = 13,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCC,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -154180,
        Z                   = 4030,
        Y                   = 76310,
        Unknown_0C          = 117,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -162330,
        Z                   = 4019,
        Y                   = 46020,
        Unknown_0C          = 116,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -135360,
        Z                   = 3950,
        Y                   = 20570,
        Unknown_0C          = 99,
        Unknown_0E          = 13,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCC,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -131150,
        Z                   = 2040,
        Y                   = 55190,
        Unknown_0C          = 57,
        Unknown_0E          = 13,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCC,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -151910,
        Z                   = 5910,
        Y                   = -11960,
        Unknown_0C          = 0,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -143900,
        Y                   = 2800,
        Z                   = 74200,
        Range               = 2000,
        Unknown_10          = 0x4B0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x10040,
        Unknown_1C          = 0,
    )


    DeclActor(
        TriggerX            = -123590,
        TriggerZ            = 4010,
        TriggerY            = 89800,
        TriggerRange        = 1000,
        ActorX              = -122930,
        ActorZ              = 5010,
        ActorY              = 89680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -128169,
        TriggerZ            = 4130,
        TriggerY            = 22090,
        TriggerRange        = 1000,
        ActorX              = -127650,
        ActorZ              = 5630,
        ActorY              = 22150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_476",          # 00, 0
        "Function_1_477",          # 01, 1
        "Function_2_4D5",          # 02, 2
        "Function_3_4EB",          # 03, 3
        "Function_4_633",          # 04, 4
    )


    def Function_0_476(): pass

    label("Function_0_476")

    Return()

    # Function_0_476 end

    def Function_1_477(): pass

    label("Function_1_477")

    OP_16(0x2, 0xFA0, 0xFFFBED08, 0xFFFF2540, 0x3003E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49B")
    OP_6F(0x0, 0)
    Jump("loc_4A2")

    label("loc_49B")

    OP_6F(0x0, 60)

    label("loc_4A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B4")
    OP_6F(0x1, 0)
    Jump("loc_4BB")

    label("loc_4B4")

    OP_6F(0x1, 60)

    label("loc_4BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CD")
    OP_6F(0x0, 0)
    Jump("loc_4D4")

    label("loc_4CD")

    OP_6F(0x0, 60)

    label("loc_4D4")

    Return()

    # Function_1_477 end

    def Function_2_4D5(): pass

    label("Function_2_4D5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4EA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_4D5")

    label("loc_4EA")

    Return()

    # Function_2_4D5 end

    def Function_3_4EB(): pass

    label("Function_3_4EB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_561")
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
    OP_A2(0x372)
    Jump("loc_5D7")

    label("loc_561")

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

    label("loc_5D7")

    Jump("loc_625")

    label("loc_5DA")

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
    OP_83(0xF, 0x17)

    label("loc_625")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4EB end

    def Function_4_633(): pass

    label("Function_4_633")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_715")
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x16, -128169, 4130, 22090, 320)
    TurnDirection(0x16, 0x0, 0)

    def lambda_682():
        OP_8F(0xFE, 0xFFFE0B57, 0x1022, 0x564A, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_682)

    def lambda_69D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_69D)
    ClearChrFlags(0x16, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0xD0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x16, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_6F0"),
        (2, "loc_702"),
        (1, "loc_712"),
        (SWITCH_DEFAULT, "loc_715"),
    )


    label("loc_6F0")

    OP_A2(0x396)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_715")

    label("loc_702")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_712")

    OP_B4(0x0)
    Return()

    label("loc_715")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x133, 1)"), scpexpr(EXPR_END)), "loc_76F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "珍珠耳环\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x373)
    Jump("loc_7EB")

    label("loc_76F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "珍珠耳环\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "珍珠耳环\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_7EB")

    Jump("loc_832")

    label("loc_7EE")

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
    OP_83(0xF, 0x18)

    label("loc_832")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_633 end

    SaveToFile()

Try(main)
