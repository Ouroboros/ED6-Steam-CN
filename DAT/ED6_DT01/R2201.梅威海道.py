from ED6ScenarioHelper import *

def main():
    # 梅威海道

    CreateScenaFile(
        FileName            = 'R2201   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2201.x',
        MapIndex            = 101,
        MapDefaultBGM       = "ed60020",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/R2201   ._SN',
            'ED6_DT01/R2201_1 ._SN',
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
        '吉米',                                 # 9
        '魔兽',                                 # 10
        '魔兽',                                 # 11
        '魔兽',                                 # 12
        '照相机',                               # 13
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
        Unknown_3A              = 101,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01040 ._CH',             # 00
        'ED6_DT09/CH10230 ._CH',             # 01
        'ED6_DT07/CH00100 ._CH',             # 02
        'ED6_DT07/CH00101 ._CH',             # 03
        'ED6_DT07/CH00110 ._CH',             # 04
        'ED6_DT07/CH00111 ._CH',             # 05
        'ED6_DT09/CH10460 ._CH',             # 06
        'ED6_DT09/CH10461 ._CH',             # 07
        'ED6_DT09/CH10160 ._CH',             # 08
        'ED6_DT09/CH10161 ._CH',             # 09
        'ED6_DT09/CH10450 ._CH',             # 0A
        'ED6_DT09/CH10451 ._CH',             # 0B
        'ED6_DT09/CH10220 ._CH',             # 0C
        'ED6_DT09/CH10221 ._CH',             # 0D
        'ED6_DT09/CH10480 ._CH',             # 0E
        'ED6_DT09/CH10481 ._CH',             # 0F
        'ED6_DT09/CH10470 ._CH',             # 10
        'ED6_DT09/CH10471 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
        'ED6_DT09/CH10230P._CP',             # 01
        'ED6_DT07/CH00100P._CP',             # 02
        'ED6_DT07/CH00101P._CP',             # 03
        'ED6_DT07/CH00110P._CP',             # 04
        'ED6_DT07/CH00111P._CP',             # 05
        'ED6_DT09/CH10460P._CP',             # 06
        'ED6_DT09/CH10461P._CP',             # 07
        'ED6_DT09/CH10160P._CP',             # 08
        'ED6_DT09/CH10161P._CP',             # 09
        'ED6_DT09/CH10450P._CP',             # 0A
        'ED6_DT09/CH10451P._CP',             # 0B
        'ED6_DT09/CH10220P._CP',             # 0C
        'ED6_DT09/CH10221P._CP',             # 0D
        'ED6_DT09/CH10480P._CP',             # 0E
        'ED6_DT09/CH10481P._CP',             # 0F
        'ED6_DT09/CH10470P._CP',             # 10
        'ED6_DT09/CH10471P._CP',             # 11
    )

    DeclNpc(
        X                   = 72800,
        Z                   = -6000,
        Y                   = 3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 76800,
        Z                   = -6000,
        Y                   = -2800,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 72800,
        Z                   = -6000,
        Y                   = -3800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 67200,
        Z                   = -6000,
        Y                   = -2000,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 67200,
        Z                   = -6000,
        Y                   = -2000,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -5600,
        Z                   = -2000,
        Y                   = 30080,
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
        X                   = 117910,
        Z                   = -2020,
        Y                   = -87790,
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
        X                   = 36840,
        Z                   = -2000,
        Y                   = 16600,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x183,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 41480,
        Z                   = -6090,
        Y                   = 11430,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x189,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 83840,
        Z                   = -2000,
        Y                   = -19430,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x182,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 103150,
        Z                   = -6030,
        Y                   = -53480,
        Unknown_0C          = 180,
        Unknown_0E          = 16,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 73280,
        Z                   = -5940,
        Y                   = -40040,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 36840,
        Z                   = -2000,
        Y                   = 16600,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x327,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 41480,
        Z                   = -6090,
        Y                   = 11430,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x32D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 83840,
        Z                   = -2000,
        Y                   = -19430,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x326,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 103150,
        Z                   = -6030,
        Y                   = -53480,
        Unknown_0C          = 180,
        Unknown_0E          = 16,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x331,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 73280,
        Z                   = -5940,
        Y                   = -40040,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x32E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 72000,
        Y                   = -6000,
        Z                   = -12900,
        Range               = 2000,
        Unknown_10          = 0x578,
        Unknown_14          = 0x0,
        Unknown_18          = 0x10040,
        Unknown_1C          = 0,
    )


    DeclActor(
        TriggerX            = 79840,
        TriggerZ            = -6030,
        TriggerY            = -14200,
        TriggerRange        = 1000,
        ActorX              = 80360,
        ActorZ              = -6040,
        ActorY              = -13800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 112050,
        TriggerZ            = -6010,
        TriggerY            = -68270,
        TriggerRange        = 1000,
        ActorX              = 112550,
        ActorZ              = -5940,
        ActorY              = -68770,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 66590,
        TriggerZ            = -6050,
        TriggerY            = -4800,
        TriggerRange        = 1000,
        ActorX              = 65960,
        ActorZ              = -5100,
        ActorY              = -4960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3DE",          # 00, 0
        "Function_1_3DF",          # 01, 1
        "Function_2_4AE",          # 02, 2
        "Function_3_4C4",          # 03, 3
        "Function_4_5F5",          # 04, 4
        "Function_5_733",          # 05, 5
    )


    def Function_0_3DE(): pass

    label("Function_0_3DE")

    Return()

    # Function_0_3DE end

    def Function_1_3DF(): pass

    label("Function_1_3DF")

    OP_16(0x2, 0xFA0, 0xFFFEFA48, 0xFFFDA288, 0x30027)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_409")
    OP_B1("R2201_y")
    Jump("loc_412")

    label("loc_409")

    OP_B1("R2201_n")

    label("loc_412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43A")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_453")

    label("loc_43A")

    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)

    label("loc_453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x97, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_465")
    OP_6F(0x0, 0)
    Jump("loc_46C")

    label("loc_465")

    OP_6F(0x0, 60)

    label("loc_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x97, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47E")
    OP_6F(0x1, 0)
    Jump("loc_485")

    label("loc_47E")

    OP_6F(0x1, 60)

    label("loc_485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x97, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_497")
    OP_6F(0x2, 0)
    Jump("loc_49E")

    label("loc_497")

    OP_6F(0x2, 60)

    label("loc_49E")

    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x186A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x1C8, 0x1, 0x64)
    Return()

    # Function_1_3DF end

    def Function_2_4AE(): pass

    label("Function_2_4AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C3")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_4AE")

    label("loc_4C3")

    Return()

    # Function_2_4AE end

    def Function_3_4C4(): pass

    label("Function_3_4C4")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x97, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_53B")
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
    OP_A2(0x4BB)
    Jump("loc_5B3")

    label("loc_53B")

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

    label("loc_5B3")

    Jump("loc_5E7")

    label("loc_5B6")

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
    OP_83(0xF, 0x85)

    label("loc_5E7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4C4 end

    def Function_4_5F5(): pass

    label("Function_4_5F5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x97, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_66B")
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
    OP_A2(0x4BC)
    Jump("loc_6E1")

    label("loc_66B")

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
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_6E1")

    Jump("loc_725")

    label("loc_6E4")

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
    OP_83(0xF, 0x86)

    label("loc_725")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5F5 end

    def Function_5_733(): pass

    label("Function_5_733")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x97, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x97, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_831")
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xD, 65960, -3500, -4960, 320)
    TurnDirection(0xD, 0x0, 0)

    def lambda_782():
        OP_8F(0xFE, 0x101A8, 0xFFFFEC78, 0xFFFFECA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_782)

    def lambda_79D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_79D)
    ClearChrFlags(0xD, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E6")
    Battle(0x32C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_7F3")

    label("loc_7E6")

    Battle(0x188, 0x0, 0x0, 0x0, 0xFF)

    label("loc_7F3")

    SetChrFlags(0xD, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_80C"),
        (2, "loc_81E"),
        (1, "loc_82E"),
        (SWITCH_DEFAULT, "loc_831"),
    )


    label("loc_80C")

    OP_A2(0x4BE)
    OP_6F(0x2, 60)
    Sleep(500)
    Jump("loc_831")

    label("loc_81E")

    OP_6F(0x2, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_82E")

    OP_B4(0x0)
    Return()

    label("loc_831")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x143, 1)"), scpexpr(EXPR_END)), "loc_88B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "红耀石护符\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4BD)
    Jump("loc_907")

    label("loc_88B")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "红耀石护符\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "红耀石护符\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_907")

    Jump("loc_958")

    label("loc_90A")

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
    OP_83(0xF, 0x87)

    label("loc_958")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_733 end

    SaveToFile()

Try(main)
