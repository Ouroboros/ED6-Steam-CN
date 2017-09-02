from ED6ScenarioHelper import *

def main():
    # 亚班特酒馆

    CreateScenaFile(
        FileName            = 'T0131   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0131.x',
        MapIndex            = 7,
        MapDefaultBGM       = "ed60010",
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
        '德瑟鲁',                               # 9
        '托露塔',                               # 10
        '伊莉莎',                               # 11
        '福克纳',                               # 12
        '提恩特',                               # 13
        '米拉诺',                               # 14
        '西蒙',                                 # 15
        '拉欧老人',                             # 16
        '奈尔',                                 # 17
        '潘杜爷爷',                             # 18
        '利吉',                                 # 19
        '目标用摄像机',                         # 20
    )

    DeclEntryPoint(
        Unknown_00              = 42000,
        Unknown_04              = 0,
        Unknown_08              = 70000,
        Unknown_0C              = 270,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 7,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 40000,
        Unknown_04              = 0,
        Unknown_08              = 64000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 7,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 45000,
        Unknown_04              = 0,
        Unknown_08              = 70000,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 7,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01280 ._CH',             # 00
        'ED6_DT07/CH01130 ._CH',             # 01
        'ED6_DT07/CH02490 ._CH',             # 02
        'ED6_DT07/CH01270 ._CH',             # 03
        'ED6_DT07/CH01503 ._CH',             # 04
        'ED6_DT07/CH01233 ._CH',             # 05
        'ED6_DT07/CH01140 ._CH',             # 06
        'ED6_DT07/CH01003 ._CH',             # 07
        'ED6_DT07/CH01120 ._CH',             # 08
        'ED6_DT07/CH01250 ._CH',             # 09
        'ED6_DT07/CH01760 ._CH',             # 0A
        'ED6_DT07/CH02060 ._CH',             # 0B
        'ED6_DT06/CH20015 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH01280P._CP',             # 00
        'ED6_DT07/CH01130P._CP',             # 01
        'ED6_DT07/CH02490P._CP',             # 02
        'ED6_DT07/CH01270P._CP',             # 03
        'ED6_DT07/CH01503P._CP',             # 04
        'ED6_DT07/CH01233P._CP',             # 05
        'ED6_DT07/CH01140P._CP',             # 06
        'ED6_DT07/CH01003P._CP',             # 07
        'ED6_DT07/CH01120P._CP',             # 08
        'ED6_DT07/CH01250P._CP',             # 09
        'ED6_DT07/CH01760P._CP',             # 0A
        'ED6_DT07/CH02060P._CP',             # 0B
        'ED6_DT06/CH20015P._CP',             # 0C
    )

    DeclNpc(
        X                   = 36450,
        Z                   = 0,
        Y                   = 126300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 82238,
        Z                   = 0,
        Y                   = 79895,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 40200,
        Z                   = 1500,
        Y                   = 78700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 34500,
        Z                   = 0,
        Y                   = 75200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 39320,
        Z                   = 220,
        Y                   = 70940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 39570,
        Z                   = 0,
        Y                   = 66410,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 41450,
        Z                   = 0,
        Y                   = 67420,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 39480,
        Z                   = 1650,
        Y                   = 76950,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 36600,
        Z                   = 0,
        Y                   = 75170,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 36500,
        Z                   = 0,
        Y                   = 72960,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 36500,
        Z                   = 0,
        Y                   = 72960,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 35580,
        TriggerZ            = 0,
        TriggerY            = 74990,
        TriggerRange        = 800,
        ActorX              = 34500,
        ActorZ              = 1500,
        ActorY              = 75200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_33E",          # 00, 0
        "Function_1_435",          # 01, 1
        "Function_2_457",          # 02, 2
        "Function_3_46D",          # 03, 3
        "Function_4_61D",          # 04, 4
        "Function_5_718",          # 05, 5
        "Function_6_188C",         # 06, 6
        "Function_7_24B8",         # 07, 7
        "Function_8_2E24",         # 08, 8
        "Function_9_4856",         # 09, 9
        "Function_10_485B",        # 0A, 10
        "Function_11_5A16",        # 0B, 11
        "Function_12_5EFE",        # 0C, 12
        "Function_13_68AF",        # 0D, 13
        "Function_14_6C8D",        # 0E, 14
        "Function_15_6EFE",        # 0F, 15
        "Function_16_7220",        # 10, 16
    )


    def Function_0_33E(): pass

    label("Function_0_33E")

    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_357")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_36D")

    label("loc_357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_361")
    Jump("loc_36D")

    label("loc_361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_36D")
    ClearChrFlags(0xF, 0x80)

    label("loc_36D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_383")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8)

    label("loc_383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AA")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8)
    SetChrPos(0x10, 37320, 0, 75500, 0)

    label("loc_3AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C0")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)

    label("loc_3C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_3DB")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)

    label("loc_3DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_3EF")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x8)
    Jump("loc_405")

    label("loc_3EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_405")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x8)

    label("loc_405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41E")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x8)
    Jump("loc_434")

    label("loc_41E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_434")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x8)

    label("loc_434")

    Return()

    # Function_0_33E end

    def Function_1_435(): pass

    label("Function_1_435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44D")
    OP_B1("t0131_y")
    Jump("loc_456")

    label("loc_44D")

    OP_B1("t0131_n")

    label("loc_456")

    Return()

    # Function_1_435 end

    def Function_2_457(): pass

    label("Function_2_457")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_457")

    label("loc_46C")

    Return()

    # Function_2_457 end

    def Function_3_46D(): pass

    label("Function_3_46D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61C")
    Sleep(3000)
    OP_8E(0xFE, 0xA85C, 0x5DC, 0x13434, 0x9C4, 0x0)
    OP_8B(0xFE, 0x186A0, 0x13434, 0x1F4)
    Sleep(3000)
    OP_8E(0xFE, 0xA7B7, 0x5DC, 0x12CC8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA79B, 0x5DC, 0x129A8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA795, 0x0, 0x12296, 0x3E8, 0x0)
    OP_8E(0xFE, 0xA0F0, 0x0, 0x11940, 0x9C4, 0x0)
    OP_8B(0xFE, 0x0, 0x11940, 0x1F4)
    Sleep(3000)
    OP_8E(0xFE, 0xA730, 0x0, 0xFFDC, 0x7D0, 0x0)
    OP_8B(0xFE, 0x186A0, 0xFFDC, 0x1F4)
    Sleep(3000)
    OP_8E(0xFE, 0x8854, 0x0, 0xF974, 0x9C4, 0x0)
    OP_8B(0xFE, 0x0, 0xF938, 0x1F4)
    Sleep(3000)
    OP_8B(0xFE, 0x186A0, 0xF938, 0x1F4)
    OP_8E(0xFE, 0x90EC, 0x0, 0xFBF4, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9344, 0x0, 0x10680, 0x9C4, 0x0)
    OP_8B(0xFE, 0x186A0, 0x10680, 0x1F4)
    Sleep(3000)
    OP_8E(0xFE, 0x81B0, 0x0, 0x10D88, 0x7D0, 0x0)
    OP_8E(0xFE, 0x81B0, 0x0, 0x121D8, 0x9C4, 0x0)
    OP_8B(0xFE, 0x0, 0x121D8, 0x1F4)
    Sleep(3000)
    OP_8E(0xFE, 0x8930, 0x0, 0x1320E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8E30, 0x0, 0x133DA, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9D08, 0x5DC, 0x1336C, 0x9C4, 0x0)
    OP_8B(0xFE, 0x9D08, 0x0, 0x1F4)
    Jump("Function_3_46D")

    label("loc_61C")

    Return()

    # Function_3_46D end

    def Function_4_61D(): pass

    label("Function_4_61D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_717")
    Sleep(3000)
    OP_8E(0xFE, 0x8E62, 0x0, 0x1E26C, 0x7D0, 0x0)
    OP_8B(0xFE, 0x0, 0x1E26C, 0x1F4)
    Sleep(3000)
    OP_8E(0xFE, 0x9308, 0x0, 0x1DA9C, 0x7D0, 0x0)
    OP_8B(0xFE, 0x9308, 0x0, 0x1F4)
    Sleep(3000)
    OP_8B(0xFE, 0x0, 0x1DA9C, 0x1F4)
    OP_8E(0xFE, 0x8F34, 0x0, 0x1E26C, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8F34, 0x0, 0x1ED5C, 0x9C4, 0x0)
    OP_8E(0xFE, 0x9470, 0x0, 0x1F144, 0x9C4, 0x0)
    OP_8E(0xFE, 0x9AB0, 0x0, 0x1F2D4, 0x9C4, 0x0)
    OP_8B(0xFE, 0x9AB0, 0x30D40, 0x1F4)
    Sleep(3000)
    OP_8B(0xFE, 0x0, 0x1F2D4, 0x1F4)
    OP_8E(0xFE, 0x8E62, 0x0, 0x1ED5C, 0x7D0, 0x0)
    OP_8B(0xFE, 0x0, 0x1ED5C, 0x1F4)
    Jump("Function_4_61D")

    label("loc_717")

    Return()

    # Function_4_61D end

    def Function_5_718(): pass

    label("Function_5_718")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 1)), scpexpr(EXPR_END)), "loc_1858")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 36520, 0, 73960, 0)
    SetChrPos(0x102, 37840, 0, 73590, 315)
    OP_8C(0x10, 180, 0)
    ClearMapFlags(0x1)
    OP_51(0x13, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x13, 0x3E8)
    OP_A2(0x252)
    OP_28(0x19, 0x1, 0x8)
    OP_28(0x19, 0x1, 0x10)
    OP_28(0x19, 0x1, 0x20)
    OP_28(0x8, 0x4, 0x40)
    OP_28(0xB, 0x4, 0x40)
    OP_4F(0x17, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x40)

    NpcTalk(
        0x10,
        "满脸胡渣的男人",
        "#142F喂，你们是什么人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F你是不是……\x01",
            "《利贝尔通讯》的记者啊？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "满脸胡渣的男人",
        (
            "#142F没错……\x01",
            "你怎么会知道？\x02\x03",
            "#142F虽然我喜欢采访别人，\x01",
            "不过可不喜欢别人对我刨根问底。\x02\x03",
            "#142F到底有什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4P我们是游击士协会派来的。\x01",
            "请问您是不是委托了护卫的工作？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "满脸胡渣的男人",
        (
            "#147F哦哦，终于来了啊！\x01",
            "我都等得不耐烦了。\x02\x03",
            "#141F那么……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 45, 400)
    OP_8C(0x10, 180, 400)
    TurnDirection(0x10, 0x101, 400)

    NpcTalk(
        0x10,
        "满脸胡渣的男人",
        "#143F卡西乌斯·布莱特在哪里？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F那个嘛……\x01",
            "他本人要负责其他的工作。\x02\x03",
            "#007F而且已经离开了洛连特……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "满脸胡渣的男人",
        (
            "#142F你、你说什么！？\x02\x03",
            "#142F好不容易来这一趟，\x01",
            "还以为可以顺便采访这位传说中的游击士……\x02\x03",
            "#145F可恶……\x01",
            "这下子我的专访计划全都落空了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F虽然不知道是怎么回事……\x01",
            "不过，也不用那么悲观嘛。\x02\x03",
            "#001F因为有我们在，\x01",
            "一定会好好替他完成任务的⊙\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "满脸胡渣的男人",
        (
            "#145F嘁，没办法……\x01",
            "这次也只能这么办了……\x02\x03",
            "#145F…………………………\x02\x03",
            "#142F……刚才你说什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#501F『也不用那么悲观嘛』？\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "满脸胡渣的男人",
        (
            "#144F不是那句！\x01",
            "是『替他完成任务』！\x02\x03",
            "#144F那是怎么回事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F你还不明白吗？\x01",
            "我们是代替他工作的游击士啊。\x02\x03",
            "#000F看看，这封是介绍信。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "游击士协会的介绍信\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x324, 1)

    NpcTalk(
        0x10,
        "满脸胡渣的男人",
        (
            "#142F喂喂，玩笑开过头了吧……\x02\x03",
            "#142F像你们这样的小鬼，\x01",
            "也敢说自己是游击士？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#009F小、小鬼？\x01",
            "你怎么能对妙龄少女说这种话呢！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "满脸胡渣的男人",
        (
            "#141F什～么少女呀。\x01",
            "一身毫无品味的打扮。\x02\x03",
            "#141F不甘心的话，\x01",
            "就换回裙子做一个像样的女孩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F这是棒术用的服装！\x01",
            "没看到我穿的就是裙子吗！\x02\x03",
            "#005F真是的，没礼貌的大叔……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(
        0x10,
        "满脸胡渣的男人",
        (
            "#144F我，我才二十几岁！\x01",
            "别叫我大叔！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F#4P……总之，记者先生。\x02\x03",
            "#017F我们确实是游击士，\x01",
            "是协会派来协助你取材的。\x02\x03",
            "#010F换成其他人也不是不行。\x01",
            "但是最近人手紧缺，不知要等到何时。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    NpcTalk(
        0x10,
        "满脸胡渣的男人",
        (
            "#145F唔，那也是……\x01",
            "截稿时间也不能再拖了……\x02\x03",
            "#145F没办法，实在是走投无路了。\x02\x03",
            "#141F就当我拜托你们了，这样总可以了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F自以为是的大叔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4P好了好了。\x02\x03",
            "#010F……我叫约修亚。\x01",
            "这个女孩叫艾丝蒂尔。\x02\x03",
            "#010F能告诉我们您的名字吗？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "满脸胡渣的男人",
        (
            "#141F奈尔·班兹。\x01",
            "《利贝尔通讯》最能干的记者。\x02\x03",
            "#141F虽说不会相处很久，不过还是多关照啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F哼哼，这句话是我说才对。\x02\x03",
            "#007F对了……你要我们带你去哪里呢？\x02\x03",
            "#007F我记得是要去危险的地方取材，\x01",
            "需要有身手不凡的向导对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#140F是被称做『翡翠之塔』的遗迹。\x01",
            "你们至少也应该听过这名字吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F什～么呀。\x02\x03",
            "#006F何止听说过，\x01",
            "之前还进去过执行任务呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#141F哦，那不是正好嘛。\x02\x03",
            "#141F具体来说，\x01",
            "只要护送我们到塔顶就可以了。\x02\x03",
            "#141F我们要拍一些登在杂志上的照片。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯～听起来好像很有趣嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4P你说『我们』……\x01",
            "难道还有其他人一起去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#140F还有和我搭档的摄影师。\x02\x03",
            "#140F因为照相机出了点问题，\x01",
            "刚才去了工房那里……\x02\x03",
            "#142F真是的，怎么这么慢啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F要是你着急的话，\x01",
            "我们就去工房接你的搭档吧？\x02\x03",
            "#000F反正等一下也要一起出去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#140F这样说也对……\x02\x03",
            "#140F好，去工房叫上那家伙，\x01",
            "然后直接出城去塔那边吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x10, 0x0, 0x0, 0xBB8, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8)
    OP_92(0x1, 0x0, 0x0, 0xBB8, 0x0)
    AddParty(0xE, 0xFF)
    EventEnd(0x0)
    SetMapFlags(0x1)
    Jump("loc_1888")

    label("loc_1858")


    NpcTalk(
        0x10,
        "满脸胡渣的男人",
        "#145F啊～肚子饿死了，肚子。\x02",
    )

    CloseMessageWindow()

    label("loc_1888")

    TalkEnd(0x10)
    Return()

    # Function_5_718 end

    def Function_6_188C(): pass

    label("Function_6_188C")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1A13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1977")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "新的菜式\x01",
            "受到了广泛的好评。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特别是伊莉莎想出的\x01",
            "那个菜式最受大家欢迎啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不如别叫她当服务生了，\x01",
            "来帮我打理厨房可能更合适。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A10")

    label("loc_1977")


    ChrTalk(
        0xFE,
        (
            "特别是伊莉莎想出的\x01",
            "那个菜式最受大家欢迎啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不如别叫她当服务生了，\x01",
            "来帮我打理厨房可能更合适。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A10")

    Jump("loc_24B4")

    label("loc_1A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1BB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B40")
    OP_A2(0x0)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "哟，雪拉扎德！\x01",
            "你又来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我进了几瓶\x01",
            "你最喜欢喝的酒哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一定要来喝啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F哎呀，真开心。\x01",
            "等工作告一段落了我就过来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAF")

    label("loc_1B40")

    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "我进了雪拉扎德你\x01",
            "最喜欢喝的酒哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一定要来喝啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1BAF")

    Jump("loc_24B4")

    label("loc_1BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1CDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C85")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "差不多该考虑\x01",
            "换换新的菜式了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以往遇到这种情况，\x01",
            "都是由全体员工一起\x01",
            "出主意定制新菜单的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……让伊莉莎也帮忙想想吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CD8")

    label("loc_1C85")


    ChrTalk(
        0xFE,
        (
            "以往遇到这种情况，\x01",
            "都是由全体员工一起\x01",
            "出主意定制新菜单的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CD8")

    Jump("loc_24B4")

    label("loc_1CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1F6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA6")
    OP_A2(0x0)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "说起来，艾丝蒂尔会做饭吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊哈哈，\x01",
            "我家做饭是轮班制的……\x02\x03",
            "#007F……所以嘛，好歹算是会一点吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是水平不行的话\x01",
            "就从简单的东西做起好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要备齐了材料和炊具，\x01",
            "剩下的就只要放手一试就行了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "学会做饭的话\x01",
            "真的百利而无一害啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F68")

    label("loc_1EA6")


    ChrTalk(
        0xFE,
        (
            "只要备齐了材料和炊具，\x01",
            "剩下的就只要放手一试就行了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "学会做饭的话\x01",
            "真的百利而无一害啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F68")

    Jump("loc_24B4")

    label("loc_1F6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_20B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2051")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "刚才帕赛尔农场\x01",
            "发来联络通知我们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说是再过一小阵\x01",
            "就能恢复蔬菜供应了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在虽然从其它地方进着货，\x01",
            "但毕竟还是帕赛尔农场的东西最好啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20B3")

    label("loc_2051")


    ChrTalk(
        0xFE,
        (
            "现在虽然从其它地方进着货，\x01",
            "毕竟还是帕赛尔农场的蔬菜最好啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20B3")

    Jump("loc_24B4")

    label("loc_20B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_2131")

    ChrTalk(
        0xFE,
        (
            "帕赛尔农场\x01",
            "没有按预定送来蔬菜呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是不是出什么事了呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B4")

    label("loc_2131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_21D5")

    ChrTalk(
        0x8,
        (
            "呼，忙死了。\x01",
            "现在正是最忙的时候啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "储备的食材已经用完了，\x01",
            "明天还得去采购一些才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B4")

    label("loc_21D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_2349")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D7")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "在我看来，\x01",
            "料理有两大乐趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那就是吃的乐趣\x01",
            "以及做菜的乐趣！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "呵呵，\x01",
            "我做每一款料理时\x01",
            "都燃烧着无穷的热情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "当然，\x01",
            "吃美味的料理时也很开心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2346")

    label("loc_22D7")


    ChrTalk(
        0x8,
        "吃是乐趣做也是乐趣……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "呵呵，\x01",
            "我做每一款料理时\x01",
            "都燃烧着无穷的热情啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2346")

    Jump("loc_24B4")

    label("loc_2349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_246E")
    OP_A2(0x2AA)

    ChrTalk(
        0x8,
        (
            "哟，艾丝蒂尔和约修亚啊，\x01",
            "今天怎么这么早呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F早上好，\x01",
            "德瑟鲁厨师。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "要想满足食客们的要求，\x01",
            "就得从早餐做起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "今日的主打菜式是一口气薏粉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "嗯，非常的可口啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B4")

    label("loc_246E")


    ChrTalk(
        0x8,
        "今日的主打菜式是一口气薏粉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "嗯，非常的可口啊。\x02",
    )

    CloseMessageWindow()

    label("loc_24B4")

    TalkEnd(0x8)
    Return()

    # Function_6_188C end

    def Function_7_24B8(): pass

    label("Function_7_24B8")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_2571")

    ChrTalk(
        0xFE,
        (
            "新菜单受到好评，\x01",
            "材料都已经用完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是供不应求呢。\x01",
            "看来要进多一点的货才行……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E20")

    label("loc_2571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_25C2")
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "哎呀，雪拉小姐。\x01",
            "欢迎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请随便坐。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E20")

    label("loc_25C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_2771")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C2")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "我们店是在我和老公\x01",
            "结婚之前开张的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以寄托了\x01",
            "我们很多的思念哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看见女儿伊莉莎\x01",
            "在店里帮忙，\x01",
            "真是有点感慨万千啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_276E")

    label("loc_26C2")


    ChrTalk(
        0xFE,
        (
            "我们店是在我和老公\x01",
            "结婚之前开张的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看见女儿伊莉莎\x01",
            "在店里帮忙，\x01",
            "真是有点感慨万千啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_276E")

    Jump("loc_2E20")

    label("loc_2771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_2898")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2844")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "最近有一对十分活跃的\x01",
            "新人游击士拍档……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难不成\x01",
            "就是指艾丝蒂尔你们吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大名鼎鼎的游击士居然是我女儿的朋友，\x01",
            "我可以在朋友面前吹嘘一番了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2895")

    label("loc_2844")


    ChrTalk(
        0xFE,
        (
            "大名鼎鼎的游击士居然是我女儿的朋友，\x01",
            "我可以在朋友面前吹嘘一番了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2895")

    Jump("loc_2E20")

    label("loc_2898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_293C")

    ChrTalk(
        0xFE,
        (
            "听说帕赛尔农场\x01",
            "很快就能恢复供货了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像是田里\x01",
            "出现了一些魔兽，\x01",
            "后来请了游击士摆平了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E20")

    label("loc_293C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_2AB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A44")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "帕赛尔农场\x01",
            "通知我们说暂时不能给\x01",
            "我们供应足够的蔬菜了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "出什么事了呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "得尽快去其它农场那里想办法啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AB1")

    label("loc_2A44")


    ChrTalk(
        0xFE,
        (
            "帕赛尔农场\x01",
            "通知我们说暂时不能给\x01",
            "我们供应足够的蔬菜了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AB1")

    Jump("loc_2E20")

    label("loc_2AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_2B41")

    ChrTalk(
        0x9,
        (
            "好，\x01",
            "先把经理的工作放在一边……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "该着手进行\x01",
            "做饭的准备了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E20")

    label("loc_2B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_2D01")
    TurnDirection(0x9, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C89")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "哎呀，艾丝蒂尔，\x01",
            "好久没有看到你了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "自从你们从\x01",
            "主日学校毕业之后，\x01",
            "不知不觉已经过去了很久呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "你是来找伊莉莎的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "就在刚才，\x01",
            "她还在店里帮忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "需要的话我把她叫出来。\x01",
            "她也肯定想见你呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CFE")

    label("loc_2C89")


    ChrTalk(
        0x9,
        (
            "艾丝蒂尔，\x01",
            "你是来找伊莉莎的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "她在店里帮忙呢，\x01",
            "需要的话我把她叫出来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CFE")

    Jump("loc_2E20")

    label("loc_2D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DB4")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        "唔，昨天的销售额有所增长……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嗯，\x01",
            "客人对于早餐的评价十分高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我们偶尔也要想想这些\x01",
            "令人有干劲的事情呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E20")

    label("loc_2DB4")


    ChrTalk(
        0x9,
        "唔，昨天的销售额有所增长……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嗯，\x01",
            "客人对于早餐的评价十分高。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E20")

    TalkEnd(0x9)
    Return()

    # Function_7_24B8 end

    def Function_8_2E24(): pass

    label("Function_8_2E24")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_3035")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FBF")
    OP_A2(0x3)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "这不是艾丝蒂尔和约修亚嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎么了～？\x01",
            "拿着旅行包。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F唔，其实呢……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔告诉伊莉莎她和约修亚将要去柏斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xFE,
        "这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我有点担心呢。\x01",
            "不过你们还是早点出发比较好哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这里等着的确\x01",
            "不像是艾丝蒂尔的作风。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊哈哈……\x01",
            "嗯，那我们出发了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3032")

    label("loc_2FBF")


    ChrTalk(
        0xFE,
        (
            "这可是非同一般的\x01",
            "旅行冒险啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(
        0xFE,
        (
            "约修亚、艾丝蒂尔，\x01",
            "我一定会在这里支持你们的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3032")

    Jump("loc_4852")

    label("loc_3035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_31AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3167")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "啊，艾丝蒂尔和约修亚啊。\x01",
            "欢迎光临……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F你好，小伊莉莎。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(
        0xFE,
        (
            "呀，连雪拉扎德姐姐也来了啊……\x01",
            "今天也是来喝酒的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是不是又来\x01",
            "欺负福克纳先生了啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F哎呀，\x01",
            "我才没有欺负他呢。\x02\x03",
            "#027F我那是疼他㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31AB")

    label("loc_3167")

    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "雪拉扎德姐姐，\x01",
            "是不是又来\x01",
            "欺负福克纳先生了啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31AB")

    Jump("loc_4852")

    label("loc_31AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_3364")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_330C")
    OP_A2(0x3)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "艾丝蒂尔，听我说听我说～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "前一阵里农的妈妈\x01",
            "忽然来我家， \x01",
            "问我要不要嫁到他们家去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "吓了我一跳呢～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过， \x01",
            "我还是想自己挑老公。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3361")

    label("loc_330C")


    ChrTalk(
        0xFE,
        (
            "里农先生年纪也不小了。\x01",
            "也难怪她妈妈会担心～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3361")

    Jump("loc_4852")

    label("loc_3364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_3495")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_341B")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "之前雪拉扎德姐姐\x01",
            "来店里喝酒了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就像艾丝蒂尔说的那样，\x01",
            "真是不得了呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "简直难以言表。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3492")

    label("loc_341B")


    ChrTalk(
        0xFE,
        (
            "之前雪拉扎德姐姐\x01",
            "来店里喝酒了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "总之真是不得了呢～\x02",
    )

    CloseMessageWindow()

    label("loc_3492")

    Jump("loc_4852")

    label("loc_3495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_3514")

    ChrTalk(
        0xFE,
        (
            "艾丝蒂尔、约修亚。\x01",
            "怎么样？工作还顺利吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "偶尔也来我们这里休息休息啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4852")

    label("loc_3514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_3715")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36AE")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "你们俩也终于踏出了\x01",
            "成为游击士的第一步了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "客人之间已经\x01",
            "在议论纷纷了呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F是、是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "洛连特虽说是乡下地方，\x01",
            "但也有卡西乌斯先生和雪拉姐姐\x01",
            "这样了不起的人物在啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大家都说你们也会\x01",
            "加入他们的行列呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F唔唔，伊莉莎，\x01",
            "别给我太大压力嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3712")

    label("loc_36AE")


    ChrTalk(
        0xFE,
        (
            "你们俩也终于踏出了\x01",
            "成为游击士的第一步了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "加油哦★\x02",
    )

    CloseMessageWindow()

    label("loc_3712")

    Jump("loc_4852")

    label("loc_3715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_3C49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3809")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37D2")
    OP_A2(0x3)

    ChrTalk(
        0xA,
        "啊，欢迎光临～★\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "难得你们俩\x01",
            "到这里来吃饭呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "爸爸和妈妈\x01",
            "要我好好款待你们哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3806")

    label("loc_37D2")


    ChrTalk(
        0xA,
        (
            "叫全家人都来\x01",
            "好好吃一顿如何呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3806")

    Jump("loc_3C46")

    label("loc_3809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C10")
    OP_A2(0x2A9)

    ChrTalk(
        0xA,
        "欢迎光临～☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "哦？艾丝蒂尔和约修亚？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F好久不见了，伊莉莎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "你们今天在一起做什么呢？\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "啊～难道说你们是在约会～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F哈哈哈……\x01",
            "这当然不是啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "说起来，你们俩正在\x01",
            "为当上游击士而努力着吧～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "做得怎么样呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，其实我们呢……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        "艾丝蒂尔将胸前的徽章拿给伊莉莎看。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xA,
        (
            "哇～合格了吗～？\x01",
            "恭喜啊！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "这可是艾丝蒂尔\x01",
            "从小就向往的职业呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哈哈，是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "对了，为了庆祝你们俩，\x01",
            "今天就到我家吃饭好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "爸爸和妈妈\x01",
            "要我好好款待你们哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F啊，真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F不行呢，艾丝蒂尔。\x01",
            "父亲还在家里等着我们回去呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F啊，对啊。\x02\x03",
            "#501F不好意思呢，伊莉莎……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "啊，唔。\x01",
            "没关系呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不过你们下次\x01",
            "一定要来我家吃饭哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C46")

    label("loc_3C10")


    ChrTalk(
        0xA,
        (
            "艾丝蒂尔，你们下次\x01",
            "一定要来我家吃饭哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C46")

    Jump("loc_4852")

    label("loc_3C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_446D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_4011")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F91")
    OP_A2(0x2A8)

    ChrTalk(
        0xA,
        (
            "咦，\x01",
            "研修已经结束了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F是啊！\x01",
            "太好了，伊莉莎！\x02\x03",
            "#001F告诉你，\x01",
            "我终于成为游击士了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "真的啊？\x01",
            "恭喜恭喜～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "这可是艾丝蒂尔\x01",
            "从小就向往的职业呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不过作为游击士，\x01",
            "危险的工作也会不少的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F这个，可能会吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "约修亚，你要看着艾丝蒂尔，\x01",
            "不要让她蛮横乱来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "因为艾丝蒂尔\x01",
            "就像一只小野猪一样，\x01",
            "今后鲁莽的时候肯定不少呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我很明白这一点，伊莉莎。\x02\x03",
            "#015F不过如果她本人不太明白的话，\x01",
            "还是一件比较麻烦的事情呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F哼，你们两个说的\x01",
            "怎么全部都是我的坏话呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我和约修亚只是为你\x01",
            "感到有些不放心呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "总之如果不小心的话，\x01",
            "就很有可能会受伤的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F呼，知道了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_400E")

    label("loc_3F91")


    ChrTalk(
        0xA,
        (
            "约修亚，你要看着艾丝蒂尔，\x01",
            "不要让她蛮横乱来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "艾丝蒂尔\x01",
            "就像一只小野猪一样，\x01",
            "今后鲁莽的时候肯定不少呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_400E")

    Jump("loc_446A")

    label("loc_4011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43ED")
    OP_A2(0x3)
    OP_A2(0x211)

    ChrTalk(
        0xA,
        "欢迎光临～☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "哦？艾丝蒂尔和约修亚？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F好久不见了，伊莉莎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "你们今天在一起做什么呢？\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "啊～难道说你们是在约会～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F不是啦。\x01",
            "听我说，伊莉莎！\x02\x03",
            "#001F告诉你，\x01",
            "我终于成为游击士了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "真的啊？\x01",
            "恭喜恭喜～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "这可是艾丝蒂尔\x01",
            "从小就向往的职业呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不过作为游击士，\x01",
            "危险的工作也会不少的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F这个，可能会吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "约修亚，你要看着艾丝蒂尔，\x01",
            "不要让她蛮横乱来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "艾丝蒂尔\x01",
            "就像一只小野猪一样，\x01",
            "今后鲁莽的时候肯定不少呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我很明白这一点，伊莉莎。\x02\x03",
            "#015F不过如果她本人不太明白的话，\x01",
            "还是一件比较麻烦的事情呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F哼，你们两个说的\x01",
            "怎么全部都是我的坏话呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我和约修亚只是为你\x01",
            "感到有些不放心呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "总之如果不小心的话，\x01",
            "就很有可能会受伤的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F呼，知道了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_446A")

    label("loc_43ED")


    ChrTalk(
        0xA,
        (
            "约修亚，你要看着艾丝蒂尔，\x01",
            "不要让她蛮横乱来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "艾丝蒂尔\x01",
            "就像一只小野猪一样，\x01",
            "今后鲁莽的时候肯定不少呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_446A")

    Jump("loc_4852")

    label("loc_446D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47C3")
    OP_A2(0x2A7)
    OP_A2(0x210)

    ChrTalk(
        0xA,
        "欢迎光临～☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "哦？艾丝蒂尔和约修亚？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F好久不见了，伊莉莎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "你们今天在一起做什么呢？\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "啊～难道说你们是在约会～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F不是啦。\x01",
            "今天就要进行游击士训练了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "这样啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "当年在主日学校\x01",
            "上课的同学们都沿着\x01",
            "各自的理想拼命努力了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "……不愧是艾丝蒂尔，\x01",
            "选择走这样一条路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F什么呀～这样不好吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "嗯，没有啦，我反倒觉得\x01",
            "这样才符合艾丝蒂尔你的风格哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "哦，对啦。\x01",
            "缇欧已经在帮家里做农活了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "上次还叫大家\x01",
            "一起去她家玩呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F咦……是缇欧啊。\x01",
            "有这样的事啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4852")

    label("loc_47C3")


    ChrTalk(
        0xA,
        (
            "当年在主日学校\x01",
            "上课的同学们都沿着\x01",
            "各自的理想拼命努力了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "艾丝蒂尔也要好好加油哦。\x02",
    )

    CloseMessageWindow()

    label("loc_4852")

    TalkEnd(0xA)
    Return()

    # Function_8_2E24 end

    def Function_9_4856(): pass

    label("Function_9_4856")

    Call(0, 10)
    Return()

    # Function_9_4856 end

    def Function_10_485B(): pass

    label("Function_10_485B")

    TalkBegin(0xB)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                               # 0
            "买东西\x01",                             # 1
            "欢迎品尝「一口气薏粉」100米拉\x01",      # 2
            "离开\x01",                               # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48E4")
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_48D9")
    OP_A9(0x75)
    Jump("loc_48DB")

    label("loc_48D9")

    OP_A9(0x5)

    label("loc_48DB")

    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_48E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49F2")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_49B8")
    SubMira(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "尝了尝\x07\x02",
            "一口气薏粉\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0xB4)
    OP_31(0x1, 0xFD, 0xB4)
    OP_31(0x2, 0xFD, 0xB4)
    OP_31(0x3, 0xFD, 0xB4)
    OP_31(0x4, 0xFD, 0xB4)
    OP_31(0x5, 0xFD, 0xB4)
    OP_31(0x6, 0xFD, 0xB4)
    OP_31(0x7, 0xFD, 0xB4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49AA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x3)"), scpexpr(EXPR_END)), "loc_4979")
    Jump("loc_49AA")

    label("loc_4979")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "学会了\x07\x02",
            "一口气薏粉\x07\x00",
            "的做法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49AA")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_49E0")

    label("loc_49B8")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_49E0")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xB)
    Return()

    label("loc_49F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A0C")
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_4A0C")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_4B6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ADF")
    OP_A2(0x2)

    ChrTalk(
        0xB,
        (
            "说起来之前市长官邸\x01",
            "好像被强盗洗劫了一番哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "偏偏是选择市长官邸下手，\x01",
            "看来犯人也挺猖狂的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "啊啊，总之没有人受伤\x01",
            "就已经让人安心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B6B")

    label("loc_4ADF")


    ChrTalk(
        0xB,
        (
            "说起来之前市长官邸\x01",
            "好像被强盗洗劫了一番哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "偏偏是选择市长官邸下手，\x01",
            "看来犯人也挺猖狂的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B6B")

    Jump("loc_5A12")

    label("loc_4B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_4DEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DAA")
    OP_A2(0x2)

    ChrTalk(
        0x103,
        "#020F你好啊，福克纳㈱\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x103, 400)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        "啊，雪、雪拉扎德小姐！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "欢、欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F什么嘛，你慌什么呀。\x01",
            "不用担心，我现在在工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "那、那太好了。\x01",
            "不不，您辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F呵呵，工作结束之后\x01",
            "我会再来这里喝一杯的。\x02\x03",
            "#027F到时还请多关照啊㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "哈、哈哈……恭候光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F（唉，被吓到了。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F（还被吓得不轻呢。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DEC")

    label("loc_4DAA")


    ChrTalk(
        0xB,
        "……我今天要不要早退呢。\x02",
    )

    CloseMessageWindow()

    label("loc_4DEC")

    Jump("loc_5A12")

    label("loc_4DEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_5138")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50AC")
    OP_A2(0x2)

    ChrTalk(
        0xB,
        (
            "游击士协会的人\x01",
            "酒量都很好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "雪拉扎德小姐就不用说了，\x01",
            "卡西乌斯先生也挺能喝的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "不过，爱娜小姐真是叫人意外。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们听雪拉姐姐说过，\x01",
            "爱娜小姐的酒量也是挺厉害的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "是啊，她可是\x01",
            "和雪拉扎德小姐同一个级别的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "而且喝完之后脸色都一点没变，\x01",
            "一直都那么悠悠然的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F哈哈，只要不像雪拉姐那样\x01",
            "胡搅蛮缠就已经很好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "看起来，\x01",
            "游击士协会真是恐怖的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "……啊，\x01",
            "只有利吉先生倒是不大能喝呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5135")

    label("loc_50AC")


    ChrTalk(
        0xB,
        (
            "竟然有人能和\x01",
            "雪拉扎德小姐是一个级别的，\x01",
            "真是叫人吃惊了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "而这个人居然是爱娜小姐，\x01",
            "这就更叫人惊上加惊了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5135")

    Jump("loc_5A12")

    label("loc_5138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_5396")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5325")
    OP_A2(0x2)

    ChrTalk(
        0xB,
        (
            "之前雪拉扎德小姐\x01",
            "来光顾我们店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我一直陪她到打烊，\x01",
            "真是惨不堪言呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "她连喝了五瓶\x01",
            "我们这里最烈的酒，\x01",
            "而且还一点醉意都没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F是啊，\x01",
            "雪拉姐喝醉这种事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F闻所未闻见所未见呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "伊莉莎自己躲起来了，\x01",
            "厨师长也先回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "结果第二天我整个人软绵绵的，\x01",
            "根本都没法工作呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5393")

    label("loc_5325")


    ChrTalk(
        0xB,
        (
            "之前雪拉扎德小姐\x01",
            "来光顾我们店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我一直陪她到打烊，\x01",
            "真是惨不堪言呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5393")

    Jump("loc_5A12")

    label("loc_5396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_55E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_553F")
    OP_A2(0x2)

    ChrTalk(
        0xB,
        (
            "洛连特支部里有个\x01",
            "叫雪拉扎德的\x01",
            "外国游击士对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "长得又漂亮，\x01",
            "又经常光顾本店，\x01",
            "我们是很欢迎她来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "不过喝了酒之后可真是不得了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "要说怎么个不得了法嘛……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F哈哈，这我知道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F深有体会。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "唉，平时倒真是个\x01",
            "爽朗又漂亮的大姐姐啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55E3")

    label("loc_553F")


    ChrTalk(
        0xB,
        (
            "之前雪拉扎德小姐\x01",
            "一个人来的时候实在是有点恐怖。\x01",
            "因为要陪她喝酒的那个人是我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "平时倒真是个\x01",
            "爽朗又漂亮的大姐姐啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55E3")

    Jump("loc_5A12")

    label("loc_55E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_5654")

    ChrTalk(
        0xB,
        (
            "厨师长忽然要我们\x01",
            "改换进货商……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "是不是出什么事了呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A12")

    label("loc_5654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_57B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5721")
    OP_A2(0x2)

    ChrTalk(
        0xB,
        (
            "我们这儿的厨师可以\x01",
            "灵活地运用食材让乡村的\x01",
            "风味得以完全地展现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "洛连特周围有很多农场。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我向你们极力推荐那道\x01",
            "用野菜制成的主打菜品。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57B2")

    label("loc_5721")


    ChrTalk(
        0xB,
        (
            "我们这儿的厨师可以\x01",
            "灵活地运用食材让乡村的\x01",
            "风味得以完全地展现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我向你们极力推荐那道\x01",
            "用野菜制成的主打菜品。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57B2")

    Jump("loc_5A12")

    label("loc_57B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_5954")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58C9")
    OP_A2(0x2)

    ChrTalk(
        0xB,
        (
            "在那边坐的那位女商人\x01",
            "好像是从柏斯来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "头脑又聪明，\x01",
            "人又长得漂亮。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "像我这种人\x01",
            "根本就配不上她啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "……可是，她说话的口音\x01",
            "总让人感觉有些怪怪的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5951")

    label("loc_58C9")


    ChrTalk(
        0xB,
        (
            "在那边的那位女商人\x01",
            "头脑又聪明，\x01",
            "人又长得漂亮。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "……可是，她说话的口音\x01",
            "总让人感觉有些怪怪的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5951")

    Jump("loc_5A12")

    label("loc_5954")


    ChrTalk(
        0xB,
        (
            "酒吧刚开的时候，\x01",
            "我是作为一个\x01",
            "服务生来这里工作的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "自从店里开始\x01",
            "提供早餐和午餐，\x01",
            "我就成为了一个酒保了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A12")

    TalkEnd(0xB)
    Return()

    # Function_10_485B end

    def Function_11_5A16(): pass

    label("Function_11_5A16")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_5B35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B00")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "香香香香……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不错不错不错不错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好吃好吃好吃好吃……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…………打嗝。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "刚才好像在街上看到了老大。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "反正小心不要让他发现\x01",
            "我翘班来这里吃东西就行了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B32")

    label("loc_5B00")


    ChrTalk(
        0xFE,
        (
            "香香香香……\x01",
            "不错不错好吃好吃……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…………打嗝。\x02",
    )

    CloseMessageWindow()

    label("loc_5B32")

    Jump("loc_5EFA")

    label("loc_5B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5C40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C1C")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "香香香香……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不错不错不错不错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好吃好吃好吃好吃……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…………打嗝。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "玛鲁加矿山的魔兽事件\x01",
            "也总算平静下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总算可以\x01",
            "悠悠闲闲地吃饭了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C3D")

    label("loc_5C1C")


    ChrTalk(
        0xFE,
        (
            "香香香香……\x01",
            "不错不错好吃好吃……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C3D")

    Jump("loc_5EFA")

    label("loc_5C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_5D38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D03")
    OP_A2(0x4)

    ChrTalk(
        0xC,
        "香香香香……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "不错不错不错不错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "好吃好吃好吃好吃……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "…………打嗝。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "再来一杯，\x01",
            "再来一杯我就回去工作了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D35")

    label("loc_5D03")


    ChrTalk(
        0xC,
        (
            "香香香香……\x01",
            "不错不错好吃好吃……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "…………打嗝。\x02",
    )

    CloseMessageWindow()

    label("loc_5D35")

    Jump("loc_5EFA")

    label("loc_5D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_5E31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DFC")
    OP_A2(0x4)

    ChrTalk(
        0xC,
        "香香香香……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "不错不错不错不错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "好吃好吃好吃好吃……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "…………打嗝。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "如果不快点吃完回矿山的话，\x01",
            "我旷工的事情就会被老大发现的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E2E")

    label("loc_5DFC")


    ChrTalk(
        0xC,
        (
            "香香香香……\x01",
            "不错不错好吃好吃……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "…………打嗝。\x02",
    )

    CloseMessageWindow()

    label("loc_5E2E")

    Jump("loc_5EFA")

    label("loc_5E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EC8")
    OP_A2(0x4)

    ChrTalk(
        0xC,
        "香香香香……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "不错不错不错不错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "好吃好吃好吃好吃……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "…………打嗝。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "因为在矿山工作的缘故，\x01",
            "很容易变得饿起来～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EFA")

    label("loc_5EC8")


    ChrTalk(
        0xC,
        (
            "香香香香……\x01",
            "不错不错好吃好吃……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "…………打嗝。\x02",
    )

    CloseMessageWindow()

    label("loc_5EFA")

    TalkEnd(0xC)
    Return()

    # Function_11_5A16 end

    def Function_12_5EFE(): pass

    label("Function_12_5EFE")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_600C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FB1")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "啊啊，玛鲁加矿山\x01",
            "开采出来的那颗翠耀石，\x01",
            "我真想以个人的身份买下来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "到底是什么人\x01",
            "抢在我之前买走了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6009")

    label("loc_5FB1")


    ChrTalk(
        0xFE,
        (
            "啊啊，玛鲁加矿山\x01",
            "开采出来的那颗翠耀石，\x01",
            "我真想以个人的身份买下来啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6009")

    Jump("loc_68AB")

    label("loc_600C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_624A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_617B")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "我听说洛连特的\x01",
            "游击士中有很多\x01",
            "很厉害的人物在哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听说最近还新加入两个\x01",
            "很有前途的年轻人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个城镇不仅资源丰富，\x01",
            "人才也很多呀……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是能网罗到有前途的新人，\x01",
            "小姐也会开心的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6247")

    label("loc_617B")


    ChrTalk(
        0xFE,
        (
            "这个城镇不仅资源丰富，\x01",
            "人才也很多呀……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是能网罗到有前途的新人，\x01",
            "小姐也会开心的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6247")

    Jump("loc_68AB")

    label("loc_624A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_63BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6354")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "这次可真走运。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想不到正在谈判的时候\x01",
            "矿山竟然发现了新矿脉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听到这种消息，\x01",
            "比看在父亲的份上去听\x01",
            "帝国商人啰里啰嗦要好得多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "对吧，西蒙？\x02",
    )

    CloseMessageWindow()
    Jump("loc_63B8")

    label("loc_6354")


    ChrTalk(
        0xFE,
        (
            "虽然很多人认为\x01",
            "洛连特是乡下地方，\x01",
            "但其实却是个资源的宝库啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63B8")

    Jump("loc_68AB")

    label("loc_63BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_653C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64B2")
    OP_A2(0x5)

    ChrTalk(
        0xD,
        "呵呵，西蒙！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "这次我特意来做这笔生意，\x01",
            "真是来对了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "预订的七耀石\x01",
            "已经全部收购完毕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "过不了多久这些东西\x01",
            "就会产生更多的价值了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6539")

    label("loc_64B2")


    ChrTalk(
        0xD,
        (
            "预订的七耀石\x01",
            "已经全部收购完毕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "过不了多久这些东西\x01",
            "就会产生更多的价值了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6539")

    Jump("loc_68AB")

    label("loc_653C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_66D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6635")
    OP_A2(0x5)

    ChrTalk(
        0xD,
        (
            "木材方面\x01",
            "无论如何都要确保足够的购入量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "我说西蒙，\x01",
            "七耀石的收购没问题吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "我特地来到洛连特做这笔交易，\x01",
            "怎么能让它失败呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66D5")

    label("loc_6635")


    ChrTalk(
        0xD,
        (
            "我说西蒙，\x01",
            "七耀石的收购没问题吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "我特地来到洛连特做这笔交易，\x01",
            "怎么能让它失败呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66D5")

    Jump("loc_68AB")

    label("loc_66D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67A8")
    OP_A2(0x5)

    ChrTalk(
        0xD,
        "西蒙，你听好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "现在是应该收购洛连特的\x01",
            "木材和七耀石的时候了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "无论风险有多大，\x01",
            "只要预算允许就尽量多购入一些。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68AB")

    label("loc_67A8")


    ChrTalk(
        0xD,
        (
            "目标就是女王诞辰庆典，\x01",
            "到了那个时候价格就会上扬了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "趁现在还是便宜的时候买入，\x01",
            "到了那个时候就可以好好赚一笔了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68AB")

    TalkEnd(0xD)
    Return()

    # Function_12_5EFE end

    def Function_13_68AF(): pass

    label("Function_13_68AF")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_6952")

    ChrTalk(
        0xFE,
        (
            "米拉诺小姐，下次的谈判就要开始了，\x01",
            "差不多该回柏斯去了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "小姐也一定对这次的报告\x01",
            "迫不及待了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C89")

    label("loc_6952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_69BF")

    ChrTalk(
        0xFE,
        "米拉诺小姐，那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我、我想我们实在是\x01",
            "没什么时间去招募人才了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C89")

    label("loc_69BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_6A6A")

    ChrTalk(
        0xFE,
        (
            "米拉诺小姐伶牙俐齿，\x01",
            "真是说不过她啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唉唉……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C89")

    label("loc_6A6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_6AEE")

    ChrTalk(
        0xE,
        (
            "说起来最近在玛鲁加矿山\x01",
            "好像发现了新的矿脉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "或许很值得期待哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C89")

    label("loc_6AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_6BA7")

    ChrTalk(
        0xE,
        (
            "嗯，这个嘛，\x01",
            "我已经和玛鲁加矿山的人取得了联系，\x01",
            "商谈也正在进行中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "再耐心等待一下吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C89")

    label("loc_6BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C23")
    OP_A2(0x6)

    ChrTalk(
        0xE,
        (
            "好、好的，木材方面\x01",
            "事情都已经安排好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "七耀石那边也开始着手进行了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C89")

    label("loc_6C23")


    ChrTalk(
        0xE,
        (
            "木材方面\x01",
            "事情都已经安排好了。\x01",
            "七耀石那边也开始着手进行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C89")

    TalkEnd(0xE)
    Return()

    # Function_13_68AF end

    def Function_14_6C8D(): pass

    label("Function_14_6C8D")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_6DE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D87")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "我也是个男人。\x01",
            "所以我下定决心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "绝对信任女儿选择的男人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那家伙一定能\x01",
            "成为独当一面的人，\x01",
            "给我的女儿带来幸福。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也要尽我所能，\x01",
            "在工作上好好协助他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DE5")

    label("loc_6D87")


    ChrTalk(
        0xFE,
        (
            "我也是个男人。\x01",
            "所以我下定决心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "绝对信任女儿选择的男人。\x02",
    )

    CloseMessageWindow()

    label("loc_6DE5")

    Jump("loc_6EFA")

    label("loc_6DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EA3")
    OP_A2(0x7)

    ChrTalk(
        0xF,
        "哼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "太嫩了，\x01",
            "那家伙也不过是个半吊子而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "想在两三年内\x01",
            "在林业上做出好成绩来，\x01",
            "这种想法也太天真了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EFA")

    label("loc_6EA3")


    ChrTalk(
        0xF,
        "哼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "太嫩了，\x01",
            "那家伙也不过是个半吊子而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EFA")

    TalkEnd(0xF)
    Return()

    # Function_14_6C8D end

    def Function_15_6EFE(): pass

    label("Function_15_6EFE")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_705C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FD8")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "昨天，我看到南面\x01",
            "好像有什么东西在空中盘旋着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果是鸟的话也太大了吧。\x01",
            "究竟是什么东西呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "年纪老了眼睛也不中用了，\x01",
            "看什么东西都不清楚了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7059")

    label("loc_6FD8")


    ChrTalk(
        0xFE,
        (
            "昨天，我看到南面\x01",
            "好像有什么东西在空中盘旋着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果是鸟的话也太大了吧。\x01",
            "究竟是什么东西呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7059")

    Jump("loc_721C")

    label("loc_705C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71A0")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "１０年前，突破了国境线的帝国军\x01",
            "曾经将洛连特重重包围。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "然后为了迫使市民投降\x01",
            "竟然炮轰了那座钟楼……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔……对不起。\x01",
            "又让你想起那件事了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F不不，没事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_721C")

    label("loc_71A0")


    ChrTalk(
        0xFE,
        (
            "如今城市和钟楼\x01",
            "都已经恢复如初了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但还是留下了许多\x01",
            "看不见的伤痕啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_721C")

    TalkEnd(0x11)
    Return()

    # Function_15_6EFE end

    def Function_16_7220(): pass

    label("Function_16_7220")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_73B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_731D")
    OP_A2(0x9)

    ChrTalk(
        0x12,
        "呀，是艾丝蒂尔和约修亚啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "前一阵我在米尔西街道见到了一种\x01",
            "四处乱蹿异常敏捷的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "闪着光冲过来，\x01",
            "一眨眼功夫就又逃走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "到底是什么东西呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_73AF")

    label("loc_731D")


    ChrTalk(
        0x12,
        (
            "前一阵我在米尔西街道见到了一种\x01",
            "四处乱蹿异常敏捷的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "闪着光冲过来，\x01",
            "一眨眼功夫就又逃走了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73AF")

    Jump("loc_74F3")

    label("loc_73B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_74F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7473")
    OP_A2(0x9)

    ChrTalk(
        0x12,
        "呀，是艾丝蒂尔和约修亚啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F利吉哥哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "你们第一天当上游击士\x01",
            "就发生了大事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "听说连卡西乌斯先生\x01",
            "都出动来帮你们了，\x01",
            "应该没事吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74F3")

    label("loc_7473")


    ChrTalk(
        0x12,
        (
            "你们第一天当上游击士\x01",
            "就发生了大事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "听说连卡西乌斯先生\x01",
            "都出动来帮你们了，\x01",
            "应该没事吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74F3")

    TalkEnd(0x12)
    Return()

    # Function_16_7220 end

    SaveToFile()

Try(main)
