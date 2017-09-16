from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2710   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2710.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2710   ._SN',
            'ED6_DT01/T2710_1 ._SN',
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
        '哈恩队长',                             # 9
        '基恩茨副长',                           # 10
        '士兵库隆',                             # 11
        '梅尔凯斯',                             # 12
        '琳塞',                                 # 13
        '巴拉特',                               # 14
        '约修亚',                               # 15
        '目标用摄像机',                         # 16
        '杜南公爵',                             # 17
        '管家菲利普',                           # 18
        '塞萨尔',                               # 19
        '加雷利',                               # 20
        '蒂雅',                                 # 21
        '士兵奥塔',                             # 22
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
        'ED6_DT07/CH01310 ._CH',             # 00
        'ED6_DT07/CH01300 ._CH',             # 01
        'ED6_DT07/CH01220 ._CH',             # 02
        'ED6_DT07/CH01050 ._CH',             # 03
        'ED6_DT07/CH01140 ._CH',             # 04
        'ED6_DT07/CH00010 ._CH',             # 05
        'ED6_DT07/CH02140 ._CH',             # 06
        'ED6_DT07/CH02470 ._CH',             # 07
        'ED6_DT07/CH01270 ._CH',             # 08
        'ED6_DT07/CH00100 ._CH',             # 09
        'ED6_DT07/CH00101 ._CH',             # 0A
        'ED6_DT07/CH02490 ._CH',             # 0B
        'ED6_DT07/CH01040 ._CH',             # 0C
        'ED6_DT07/CH01043 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH01310P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
        'ED6_DT07/CH01220P._CP',             # 02
        'ED6_DT07/CH01050P._CP',             # 03
        'ED6_DT07/CH01140P._CP',             # 04
        'ED6_DT07/CH00010P._CP',             # 05
        'ED6_DT07/CH02140P._CP',             # 06
        'ED6_DT07/CH02470P._CP',             # 07
        'ED6_DT07/CH01270P._CP',             # 08
        'ED6_DT07/CH00100P._CP',             # 09
        'ED6_DT07/CH00101P._CP',             # 0A
        'ED6_DT07/CH02490P._CP',             # 0B
        'ED6_DT07/CH01040P._CP',             # 0C
        'ED6_DT07/CH01043P._CP',             # 0D
    )

    DeclNpc(
        X                   = 4750,
        Z                   = 0,
        Y                   = 90620,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -2750,
        Z                   = 0,
        Y                   = 11470,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -4800,
        Z                   = 0,
        Y                   = 7900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -770,
        Z                   = 0,
        Y                   = 21500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -770,
        Z                   = 0,
        Y                   = 22500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -770,
        Z                   = 0,
        Y                   = 23500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 52155,
        Z                   = -3000,
        Y                   = 17688,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 20000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4500,
        Z                   = 5000,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 95300,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -3800,
        Z                   = 0,
        Y                   = 24700,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 400,
        Z                   = 0,
        Y                   = 19200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 93480,
        Z                   = 0,
        Y                   = 85530,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )


    DeclEvent(
        X                   = -6779,
        Y                   = -1000,
        Z                   = 1610,
        Range               = -5847,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x189C,
        Unknown_18          = 0x10000,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = -3939,
        Y                   = -1000,
        Z                   = 1820,
        Range               = 2122,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x0,
        Unknown_1C          = 17,
    )


    DeclActor(
        TriggerX            = -2990,
        TriggerZ            = 0,
        TriggerY            = 7710,
        TriggerRange        = 1000,
        ActorX              = -4800,
        ActorZ              = 1500,
        ActorY              = 7900,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 95800,
        TriggerZ            = 0,
        TriggerY            = 13660,
        TriggerRange        = 1000,
        ActorX              = 95300,
        ActorZ              = 1500,
        ActorY              = 16000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 93600,
        TriggerZ            = 0,
        TriggerY            = 87450,
        TriggerRange        = 1000,
        ActorX              = 93480,
        ActorZ              = 1500,
        ActorY              = 85530,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_386",          # 00, 0
        "Function_1_82A",          # 01, 1
        "Function_2_899",          # 02, 2
        "Function_3_967",          # 03, 3
        "Function_4_B3A",          # 04, 4
        "Function_5_D35",          # 05, 5
        "Function_6_FA9",          # 06, 6
        "Function_7_211F",         # 07, 7
        "Function_8_2168",         # 08, 8
        "Function_9_3052",         # 09, 9
        "Function_10_3057",        # 0A, 10
        "Function_11_3873",        # 0B, 11
        "Function_12_3878",        # 0C, 12
        "Function_13_478A",        # 0D, 13
        "Function_14_49D2",        # 0E, 14
        "Function_15_4B29",        # 0F, 15
        "Function_16_4B2E",        # 10, 16
        "Function_17_558B",        # 11, 17
        "Function_18_56B3",        # 12, 18
    )


    def Function_0_386(): pass

    label("Function_0_386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3A9")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_6FE")

    label("loc_3A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3CC")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_6FE")

    label("loc_3CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3EF")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_6FE")

    label("loc_3EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_412")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_6FE")

    label("loc_412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_435")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_6FE")

    label("loc_435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_48B")
    SetChrPos(0x8, 4750, 0, 90620, 0)
    SetChrPos(0xA, -4800, 0, 7900, 90)
    SetChrPos(0x9, 2900, 0, 95100, 90)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_6FE")

    label("loc_48B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_680")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_518")
    SetChrPos(0x8, -2810, 0, 92600, 270)
    SetChrPos(0x9, 96840, 0, 14020, 339)
    SetChrPos(0xB, -3090, 0, 18660, 270)
    SetChrPos(0xC, -3860, 0, 19770, 270)
    SetChrPos(0xD, -2570, 0, 23890, 315)
    OP_44(0x13, 0xFF)
    SetChrChipByIndex(0x13, 13)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x10)
    SetChrPos(0x13, 95610, 200, 7550, 180)
    Jump("loc_67D")

    label("loc_518")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_5F2")
    SetChrPos(0x8, 0, 0, 5250, 0)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0xA, 92510, 0, 9380, 69)
    SetChrPos(0x9, 92630, 0, 12500, 90)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -680, 0, 5220, 0)
    SetChrPos(0x13, 320, 0, 23610, 176)
    SetChrPos(0x14, -3790, 0, 19850, 141)
    SetChrPos(0xB, 0, 0, 6230, 270)
    SetChrPos(0xC, 670, 0, 5960, 270)
    SetChrPos(0xD, -800, 0, 5880, 315)
    OP_43(0xB, 0x1, 0x1, 0x8)
    OP_43(0xC, 0x1, 0x1, 0x9)
    OP_43(0xD, 0x1, 0x1, 0xA)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x8, 0x10)
    Jump("loc_67D")

    label("loc_5F2")

    SetChrPos(0xB, 1596, 0, 12441, 90)
    SetChrPos(0xC, 1513, 0, 13617, 90)
    SetChrPos(0xD, 909, 0, 13169, 90)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    SetChrPos(0x13, 320, 0, 23610, 176)
    SetChrPos(0x14, -3790, 0, 19850, 141)
    SetChrPos(0xA, 92510, 0, 9380, 69)
    SetChrPos(0x9, 92630, 0, 12500, 90)
    SetChrFlags(0x8, 0x80)

    label("loc_67D")

    Jump("loc_6FE")

    label("loc_680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_6FE")
    SetChrPos(0x8, 1970, 0, 94650, 270)
    SetChrPos(0xA, -50, 0, 94650, 90)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xC, -3860, 0, 19770, 270)
    SetChrPos(0xD, -2570, 0, 23890, 315)
    OP_44(0x13, 0xFF)
    SetChrChipByIndex(0x13, 13)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x10)
    SetChrPos(0x13, 95610, 200, 7550, 180)

    label("loc_6FE")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_716"),
        (101, "loc_787"),
        (102, "loc_7A8"),
        (103, "loc_7FC"),
        (SWITCH_DEFAULT, "loc_829"),
    )


    label("loc_716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_784")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_746")
    OP_28(0x23, 0x1, 0x8000)
    Event(1, 0)
    Jump("loc_784")

    label("loc_746")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_784")
    SetChrPos(0xB, 1596, 0, 12441, 90)
    SetChrPos(0xC, 1513, 0, 13617, 90)
    SetChrPos(0xD, 909, 0, 13169, 90)

    label("loc_784")

    Jump("loc_829")

    label("loc_787")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A5")
    Event(1, 1)

    label("loc_7A5")

    Jump("loc_829")

    label("loc_7A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D2")
    AddParty(0x1, 0xFF)
    OP_28(0x23, 0x4, 0x10)
    Event(1, 23)
    Jump("loc_7F9")

    label("loc_7D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F9")
    AddParty(0x1, 0xFF)
    OP_28(0x23, 0x4, 0x10)
    Event(1, 24)

    label("loc_7F9")

    Jump("loc_829")

    label("loc_7FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_826")
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    Event(1, 11)

    label("loc_826")

    Jump("loc_829")

    label("loc_829")

    Return()

    # Function_0_386 end

    def Function_1_82A(): pass

    label("Function_1_82A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_834")
    Jump("loc_86C")

    label("loc_834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_861")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_848")
    Jump("loc_85E")

    label("loc_848")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_85A")
    OP_64(0x0, 0x1)
    Jump("loc_85E")

    label("loc_85A")

    OP_64(0x0, 0x1)

    label("loc_85E")

    Jump("loc_86C")

    label("loc_861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_86C")
    OP_64(0x0, 0x1)

    label("loc_86C")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_888"),
        (101, "loc_888"),
        (102, "loc_888"),
        (104, "loc_888"),
        (106, "loc_888"),
        (SWITCH_DEFAULT, "loc_890"),
    )


    label("loc_888")

    OP_22(0x1C6, 0x1, 0x64)
    Jump("loc_893")

    label("loc_890")

    OP_23(0x1C6)

    label("loc_893")

    OP_1C(0x3, 0x0, 0x12)
    Return()

    # Function_1_82A end

    def Function_2_899(): pass

    label("Function_2_899")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BE")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_951")

    label("loc_8BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D7")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_951")

    label("loc_8D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F0")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_951")

    label("loc_8F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_909")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_951")

    label("loc_909")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_922")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_951")

    label("loc_922")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93B")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_951")

    label("loc_93B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_951")
    OP_99(0xFE, 0x6, 0x7, 0x546)

    label("loc_951")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_966")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_951")

    label("loc_966")

    Return()

    # Function_2_899 end

    def Function_3_967(): pass

    label("Function_3_967")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_974")
    Jump("loc_B36")

    label("loc_974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_97E")
    Jump("loc_B36")

    label("loc_97E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_988")
    Jump("loc_B36")

    label("loc_988")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_992")
    Jump("loc_B36")

    label("loc_992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_9A3")
    Jump("loc_9A3")

    label("loc_9A3")

    Jump("loc_B36")

    label("loc_9A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_9B0")
    Jump("loc_B36")

    label("loc_9B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_AE4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A68")

    ChrTalk(
        0xFE,
        (
            "我是为了静思一些事情\x01",
            "才来到这里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "都是那个公爵，\x01",
            "害我把刚才想的事情\x01",
            "都忘得一干二净了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE1")

    label("loc_A68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_AB2")
    OP_4A(0xFE, 255)

    ChrTalk(
        0xFE,
        (
            "你是这里的士兵吧！\x01",
            "快点想想办法啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xFE, 255)
    Jump("loc_AE1")

    label("loc_AB2")


    ChrTalk(
        0xFE,
        (
            "……从钥匙孔\x01",
            "不知道能不能看到里面。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE1")

    Jump("loc_B36")

    label("loc_AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_B36")

    ChrTalk(
        0xFE,
        (
            "在遗迹这样的地方还会有瀑布，\x01",
            "真是罕见啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B36")

    TalkEnd(0xB)
    Return()

    # Function_3_967 end

    def Function_4_B3A(): pass

    label("Function_4_B3A")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_B47")
    Jump("loc_D31")

    label("loc_B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_B51")
    Jump("loc_D31")

    label("loc_B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_B5B")
    Jump("loc_D31")

    label("loc_B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_B65")
    Jump("loc_D31")

    label("loc_B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_B76")
    Jump("loc_B76")

    label("loc_B76")

    Jump("loc_D31")

    label("loc_B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_B83")
    Jump("loc_D31")

    label("loc_B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_CC7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C00")

    ChrTalk(
        0xFE,
        (
            "难得的出游，\x01",
            "心情都被那个臭公爵破坏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我要上诉！\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC4")

    label("loc_C00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_C89")
    OP_4A(0xFE, 255)

    ChrTalk(
        0xC,
        "王国军不是市民的朋友吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "好歹也要做些什么吧！\x02",
    )

    CloseMessageWindow()
    OP_4B(0xFE, 255)
    Jump("loc_CC4")

    label("loc_C89")


    ChrTalk(
        0xFE,
        "真是，要想点办法呀。\x02",
    )

    CloseMessageWindow()

    label("loc_CC4")

    Jump("loc_D31")

    label("loc_CC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_D31")

    ChrTalk(
        0xFE,
        (
            "你们也觉得\x01",
            "这里的景色非常美丽吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不愧是\x01",
            "『利贝尔十六景』之一啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D31")

    TalkEnd(0xC)
    Return()

    # Function_4_B3A end

    def Function_5_D35(): pass

    label("Function_5_D35")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_D42")
    Jump("loc_FA5")

    label("loc_D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_D4C")
    Jump("loc_FA5")

    label("loc_D4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_D56")
    Jump("loc_FA5")

    label("loc_D56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_D60")
    Jump("loc_FA5")

    label("loc_D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_D74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_D71")
    Jump("loc_D71")

    label("loc_D71")

    Jump("loc_FA5")

    label("loc_D74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_D7E")
    Jump("loc_FA5")

    label("loc_D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_EFA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E36")

    ChrTalk(
        0xFE,
        "游击士好像把问题解决了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不知道面对那样我行我素的人\x01",
            "是怎么把问题解决的，\x01",
            "不过游击士果然很靠得住啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF7")

    label("loc_E36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_E91")
    OP_4A(0xFE, 255)

    ChrTalk(
        0xD,
        "就这样任他无理取闹吗！\x02",
    )

    CloseMessageWindow()
    OP_4B(0xFE, 255)
    Jump("loc_EF7")

    label("loc_E91")


    ChrTalk(
        0xFE,
        (
            "如果连游击士面对\x01",
            "大人物也处于弱势的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "前景真是一片黑暗啊……\x02",
    )

    CloseMessageWindow()

    label("loc_EF7")

    Jump("loc_FA5")

    label("loc_EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_FA5")

    ChrTalk(
        0xFE,
        (
            "充满田园风光的玛诺利亚，\x01",
            "观光旅游的港口城市卢安，\x01",
            "以及这个艾尔·雷登……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个地区的\x01",
            "风景名胜还真多啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA5")

    TalkEnd(0xD)
    Return()

    # Function_5_D35 end

    def Function_6_FA9(): pass

    label("Function_6_FA9")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_10B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1023")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "新的通知又下来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "上级部门对于\x01",
            "逮捕犯人的事情\x01",
            "还没有放弃。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B1")

    label("loc_1023")


    ChrTalk(
        0xFE,
        (
            "可是这次的通知\x01",
            "却给我们出了个难题啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我得准确无误地\x01",
            "向部下传达才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B1")

    Jump("loc_211B")

    label("loc_10B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1222")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A5")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "解除盘查的命令\x01",
            "是确凿的事实。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对于这个命令，\x01",
            "我个人的确还是有些疑问。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，军令如山。\x01",
            "是不容我们自作主张的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "除了服从上级的命令之外\x01",
            "别无选择。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_121F")

    label("loc_11A5")


    ChrTalk(
        0xFE,
        (
            "就算是这样，\x01",
            "现在要解除盘查……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……是有什么内幕吗？\x02",
    )

    CloseMessageWindow()

    label("loc_121F")

    Jump("loc_211B")

    label("loc_1222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_14FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_146B")
    OP_A2(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_136D")

    ChrTalk(
        0xFE,
        "哦，是游击士们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "中央工房被袭击的事件\x01",
            "我们已经收到了相关报告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个关所和各地的关所一起\x01",
            "开始实行严格的盘查制度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样一来\x01",
            "犯人就无处可逃了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "放心吧。\x01",
            "我想很快就可以抓到了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1468")

    label("loc_136D")


    ChrTalk(
        0xFE,
        "哟，你们是旅行者吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "非常抱歉，\x01",
            "因为发生了中央工房的事件，\x01",
            "所以关所这里要进行盘查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "除非有紧急情况，\x01",
            "不然是不能给你们发通行证的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且最近一段时间之内\x01",
            "这种状况都要持续下去。\x01",
            "如果是要去旅行的话，以后还会有机会的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1468")

    Jump("loc_14F9")

    label("loc_146B")


    ChrTalk(
        0xFE,
        (
            "王国军也在全力协助\x01",
            "搜捕袭击工房的犯人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我相信犯人一定会\x01",
            "很快被逮捕的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14F9")

    Jump("loc_211B")

    label("loc_14FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_164F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B7")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "对昨夜在蔡斯发生的事件，\x01",
            "王国军也非常关注。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "情报部的那些人\x01",
            "现在肯定在拼命调查吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164C")

    label("loc_15B7")


    ChrTalk(
        0xFE,
        (
            "算了，\x01",
            "反正很快一切又会恢复原状的，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "蔡斯的中央工房\x01",
            "是王国最重要的财产啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_164C")

    Jump("loc_211B")

    label("loc_164F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_1B97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 7)), scpexpr(EXPR_END)), "loc_17E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1718")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "呼，接下来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "文件已经整理好了，\x01",
            "去看看部下的情况吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果总是呆在房间里不出去，\x01",
            "就不能给他们起好带头作用了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17E3")

    label("loc_1718")


    ChrTalk(
        0xFE,
        (
            "自从公爵阁下那次事件以来，\x01",
            "感觉自己好像得不到\x01",
            "部下的信赖了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈，你们可能认为我太神经质了，\x01",
            "不过这也是我作为队长的分内工作啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17E3")

    Jump("loc_1B94")

    label("loc_17E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_19E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1959")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "哎呀，是你们几位。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "公爵阁下来的时候\x01",
            "你们真是帮了大忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "多亏你们才没给\x01",
            "其他的旅客添更多的麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我们之间存在许多问题，\x01",
            "但我想今后还是和\x01",
            "游击士协会共同合作好一些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果再有什么事的话，\x01",
            "可能就要再次拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19DF")

    label("loc_1959")


    ChrTalk(
        0xFE,
        (
            "我想今后还是和\x01",
            "游击士协会共同合作好一些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果再有什么事的话，\x01",
            "可能就要再次拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19DF")

    Jump("loc_1B94")

    label("loc_19E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B02")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "呼，前些日子\x01",
            "遇到了一件很麻烦的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一位和王室有关系的大人物\x01",
            "到这个关所来视察了……\x01",
            "那可是个蛮不讲理的人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "给那些普通的旅客们\x01",
            "带来了不少的麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看到那样的人，\x01",
            "我对利贝尔王室的印象\x01",
            "也变得比较差了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B94")

    label("loc_1B02")


    ChrTalk(
        0xFE,
        (
            "好不容易\x01",
            "就快到女王的诞辰庆典了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看到那样的人，\x01",
            "我对利贝尔王室的印象\x01",
            "也变得比较差了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B94")

    Jump("loc_211B")

    label("loc_1B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_1F52")
    OP_A2(0x58F)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1D9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D14")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "哎呀，是你们几位。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "公爵阁下来的时候\x01",
            "你们真是帮了大忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "多亏你们才没给\x01",
            "其他的旅客添更多的麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我们之间存在许多问题，\x01",
            "但我想今后还是和\x01",
            "游击士协会共同合作好一些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果再有什么事的话，\x01",
            "可能就要再次拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D9A")

    label("loc_1D14")


    ChrTalk(
        0xFE,
        (
            "我想今后还是和\x01",
            "游击士协会共同合作好一些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果再有什么事的话，\x01",
            "可能就要再次拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D9A")

    Jump("loc_1F4F")

    label("loc_1D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EBD")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "呼，前些日子\x01",
            "遇到了一件很麻烦的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一位和王室有关系的大人物\x01",
            "到这个关所来视察了……\x01",
            "那可是个蛮不讲理的人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "给那些普通的旅客们\x01",
            "带来了不少的麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看到那样的人，\x01",
            "我对利贝尔王室的印象\x01",
            "也变得比较差了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F4F")

    label("loc_1EBD")


    ChrTalk(
        0xFE,
        (
            "好不容易\x01",
            "就快到女王的诞辰庆典了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看到那样的人，\x01",
            "我对利贝尔王室的印象\x01",
            "也变得比较差了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F4F")

    Jump("loc_211B")

    label("loc_1F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1FF8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1FC5")

    ChrTalk(
        0xFE,
        "各位，这次辛苦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀呀…………\x01",
            "多灾多难的一天终于过去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FF5")

    label("loc_1FC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_1FF5")

    ChrTalk(
        0xFE,
        (
            "各、各位\x01",
            "请冷静一点！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FF5")

    label("loc_1FF5")

    Jump("loc_211B")

    label("loc_1FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_211B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2100")
    OP_A2(0x0)
    OP_A2(0x2)
    OP_4A(0xA, 255)

    ChrTalk(
        0xFE,
        (
            "听说公爵要到\x01",
            "卢安市去进行访问，\x01",
            "不过没听说过会到这里来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "唉，好像是根据他本人的意愿\x01",
            "而突然改变预定计划的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呼，这就没办法了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "视察的相关事项\x01",
            "本来已经准备好了的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "是！\x02",
    )

    CloseMessageWindow()
    OP_4B(0xA, 255)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_211B")

    label("loc_2100")


    ChrTalk(
        0xFE,
        "唉，真是件麻烦事啊。\x02",
    )

    CloseMessageWindow()

    label("loc_211B")

    TalkEnd(0x8)
    Return()

    # Function_6_FA9 end

    def Function_7_211F(): pass

    label("Function_7_211F")

    TalkBegin(0xE)

    ChrTalk(
        0xE,
        (
            "#010F这里由我们来想办法……\x01",
            "　\x02\x03",
            "艾丝蒂尔你们赶快去食堂看看状况。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    # Function_7_211F end

    def Function_8_2168(): pass

    label("Function_8_2168")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2211")

    ChrTalk(
        0xFE,
        (
            "……所以说嘛，\x01",
            "新的通知到现在才来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "早知道一开始\x01",
            "就解除盘查了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304E")

    label("loc_2211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_241F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2334")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "队长虽然看起来很普通，\x01",
            "但是属于那种刚直不阿的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他认为这次的命令\x01",
            "无法让人接受。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过实际上，\x01",
            "我也觉得无法接受呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊啊～可恶！\x01",
            "真让人恼火。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241C")

    label("loc_2334")


    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "一个不明不白的公爵事件就够呛了，\x01",
            "这回又来了个不知所谓的命令……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个国家的领导者\x01",
            "怎么会变得这么奇怪呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说实话，\x01",
            "实在不想再碰上这样的事情了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_241C")

    Jump("loc_304E")

    label("loc_241F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_24B6")

    ChrTalk(
        0xFE,
        (
            "抱歉啊。\x01",
            "现在关所正处于戒严状态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我不能和你们\x01",
            "说太多闲话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "而且部下还在旁边呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_304E")

    label("loc_24B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_25C4")

    ChrTalk(
        0xFE,
        (
            "听说了吗，蔡斯的事情。\x01",
            "好像引起了很大的骚乱啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为那里是利贝尔王国中\x01",
            "导力化程度最高的城市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果那里一旦停止运转，\x01",
            "想必一定会带来很多不便吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304E")

    label("loc_25C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2A2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 0)), scpexpr(EXPR_END)), "loc_2696")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2657")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "不能再偷懒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "队长很快\x01",
            "就要来巡视了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2693")

    label("loc_2657")


    ChrTalk(
        0xFE,
        (
            "没办法啊，\x01",
            "这份工作太累人了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2693")

    Jump("loc_2A29")

    label("loc_2696")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_283B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27A5")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "噢，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，之前公爵阁下来的时候\x01",
            "真是多亏你们帮了大忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "游击士和王国军之间\x01",
            "经常会有各种纠纷………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过在表面上\x01",
            "还是会经常互相协助的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2838")

    label("loc_27A5")


    ChrTalk(
        0xFE,
        (
            "也是啊，台面上的话语\x01",
            "还是交给那些所谓的伟人们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要在事件现场\x01",
            "能够处理得当就可以了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2838")

    Jump("loc_2A29")

    label("loc_283B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_295D")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "前不久王室的那个什么公爵\x01",
            "到这个关所来视察了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，那是个胡说八道、\x01",
            "蛮不讲理的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "一想到要为那样的家伙忙个不停……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就会觉得\x01",
            "要是没来参军就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A29")

    label("loc_295D")


    ChrTalk(
        0xFE,
        (
            "一想到那个公爵\x01",
            "也算是王室的一员……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就会觉得\x01",
            "要是没来参军就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，以我现在的立场，\x01",
            "这样的事情还是少说为妙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A29")

    Jump("loc_304E")

    label("loc_2A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_2DE7")
    OP_A2(0x590)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2BDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B46")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "噢，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，之前公爵阁下来的时候\x01",
            "真是多亏你们帮了大忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "游击士和王国军之间\x01",
            "经常会有各种纠纷………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过在表面上\x01",
            "还是会经常互相协助的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BD9")

    label("loc_2B46")


    ChrTalk(
        0xFE,
        (
            "也是啊，台面上的话语\x01",
            "还是交给那些所谓的伟人们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要在事件现场\x01",
            "能够处理得当就可以了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BD9")

    Jump("loc_2DE4")

    label("loc_2BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CFE")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "前不久王室的那个什么公爵\x01",
            "到这个关所来视察了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，那是个胡说八道、\x01",
            "蛮不讲理的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "一想到要为那样的家伙忙个不停……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就会觉得\x01",
            "要是没来参军就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DE4")

    label("loc_2CFE")


    ChrTalk(
        0xFE,
        (
            "一想到那个公爵\x01",
            "也算是王室的一员……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就会觉得\x01",
            "要是没来参军就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，以我现在的立场，\x01",
            "这样的事情还是少说为妙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DE4")

    Jump("loc_304E")

    label("loc_2DE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2FB6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2FA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F12")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "哇哈哈哈，\x01",
            "小姑娘还真是干净利落！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "游击士里\x01",
            "也有些很有趣的人嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "为什么那种人\x01",
            "会出生在王家呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说他是下任国王，\x01",
            "我只是希望他的发型能正经点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FA3")

    label("loc_2F12")


    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "为什么那种人\x01",
            "会出生在王家呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说他是下任国王，\x01",
            "我只是希望他的发型能正经点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FA3")

    Jump("loc_2FB3")

    label("loc_2FA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_2FB3")
    Jump("loc_2FB3")

    label("loc_2FB3")

    Jump("loc_304E")

    label("loc_2FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_304E")

    ChrTalk(
        0xFE,
        (
            "库隆那家伙\x01",
            "和队长说了些什么啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "总觉得有不好的预感……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那家伙总是会带来\x01",
            "一些不好的消息。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_304E")

    TalkEnd(0x9)
    Return()

    # Function_8_2168 end

    def Function_9_3052(): pass

    label("Function_9_3052")

    Call(0, 10)
    Return()

    # Function_9_3052 end

    def Function_10_3057(): pass

    label("Function_10_3057")

    TalkBegin(0x12)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30B7")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x34)
    OP_56(0x0)
    TalkEnd(0x12)
    Return()

    label("loc_30B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30D1")
    FadeToBright(300, 0)
    TalkEnd(0x12)
    Return()

    label("loc_30D1")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_31CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_318C")
    OP_A2(0x3)

    ChrTalk(
        0x12,
        "你们好，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "看啊，现在这个样子。\x01",
            "基本上没什么人来光顾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "诞辰庆典也带走了很多旅客。\x01",
            "唉～人气这个东西真是变幻莫测啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31C8")

    label("loc_318C")


    ChrTalk(
        0x12,
        (
            "好吧，\x01",
            "既然你们特地来到这里，\x01",
            "我就给你们露一手吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "来吧，\x01",
            "你们想点什么都可以！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31C8")

    Jump("loc_386F")

    label("loc_31CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_32F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_326C")
    OP_A2(0x3)

    ChrTalk(
        0x12,
        "你们好，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "如你所见，\x01",
            "现在盘查已经解除了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "不过这样好吗？\x01",
            "这么快就解除盘查。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32EF")

    label("loc_326C")


    ChrTalk(
        0x12,
        (
            "哼，\x01",
            "反正肯定还没抓到犯人吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "王国军真是没什么用啊。\x01",
            "接下来就看游击士的了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32EF")

    Jump("loc_386F")

    label("loc_32F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_33B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3386")
    OP_A2(0x3)

    ChrTalk(
        0x12,
        (
            "呼，\x01",
            "最近烦人的消息接二连三……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "就算是我，\x01",
            "今天也没有什么心情说话。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33B5")

    label("loc_3386")


    ChrTalk(
        0x12,
        (
            "呼，真是的。\x01",
            "烦人的消息太多了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33B5")

    Jump("loc_386F")

    label("loc_33B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3463")

    ChrTalk(
        0x12,
        (
            "听说了吗？\x01",
            "蔡斯的事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "所有导力器\x01",
            "都停止运转了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "真是令人惊讶的\x01",
            "神奇事件啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_386F")

    label("loc_3463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_34E5")

    ChrTalk(
        0x12,
        "噢，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "这里唯一的优点就是景色不错，\x01",
            "你们还是可以好好享受一下的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_386F")

    label("loc_34E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_3628")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_358C")

    ChrTalk(
        0x12,
        "哟，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "之前真是多谢了。\x01",
            "对了，今天来也是因为工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "如果有空的话，\x01",
            "要记得经常来玩呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3625")

    label("loc_358C")


    ChrTalk(
        0x12,
        "哟，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "欣赏了瀑布的风景之后，\x01",
            "再来品尝一些美味的食物如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "总之，\x01",
            "请在这里好好放松一下哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3625")

    Jump("loc_386F")

    label("loc_3628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_36C4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_36B4")

    ChrTalk(
        0x12,
        (
            "唉……\x01",
            "真是个令人头痛的大叔啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "完全搞不清\x01",
            "什么是公共场合。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C1")

    label("loc_36B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_36C1")
    Jump("loc_36C1")

    label("loc_36C1")

    Jump("loc_386F")

    label("loc_36C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_386F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37DB")
    OP_A2(0x3)

    ChrTalk(
        0x12,
        "哟，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "在欣赏美景时如果没有佳肴做伴，\x01",
            "那可就有些遗憾了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "这里的盐锅烤小鱼\x01",
            "可是十分好吃的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "从头到尾都可以吃，\x01",
            "是本店超级推荐的料理！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_386F")

    label("loc_37DB")


    ChrTalk(
        0x12,
        (
            "在欣赏美景时如果没有佳肴做伴，\x01",
            "那可就有些遗憾了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "这里的盐锅烤小鱼\x01",
            "可是十分好吃的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_386F")

    TalkEnd(0x12)
    Return()

    # Function_10_3057 end

    def Function_11_3873(): pass

    label("Function_11_3873")

    Call(0, 12)
    Return()

    # Function_11_3873 end

    def Function_12_3878(): pass

    label("Function_12_3878")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3A0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3955")
    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "总部那边\x01",
            "又下达了新的命令。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "大概又是\x01",
            "与通行许可相关的通知吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "呼～\x01",
            "差不多都可以猜出来是什么内容了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A0B")

    label("loc_3955")


    ChrTalk(
        0xA,
        (
            "好像又有一个\x01",
            "新的命令下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "唔～\x01",
            "上级部门怎么忽左忽右的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "感觉好像\x01",
            "总是抓不住要点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A0B")

    Jump("loc_4786")

    label("loc_3A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3BB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AE8")
    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "上级部门\x01",
            "又下达新指示了，\x01",
            "说要解除盘查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "可还没有听说犯人\x01",
            "被逮捕了的消息啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "就这样恢复以往的通行状态，\x01",
            "不会有问题吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BAF")

    label("loc_3AE8")


    ChrTalk(
        0xA,
        (
            "虽说是上级部门的命令，\x01",
            "但总感觉难以理解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "犯人都还没有捉到，\x01",
            "就把盘查给解除了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "难道说其他的关所\x01",
            "也接到了相同的命令吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BAF")

    Jump("loc_4786")

    label("loc_3BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3D0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C85")
    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "很抱歉，\x01",
            "现在除非有紧急情况，\x01",
            "否则不能签发通行许可证。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "在袭击蔡斯的犯人\x01",
            "被逮捕之前的这段时间内\x01",
            "都会保持现在的状况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D0C")

    label("loc_3C85")


    ChrTalk(
        0xA,
        (
            "现在除非有紧急情况，\x01",
            "否则不能签发通行许可证。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "如果能早些\x01",
            "逮捕犯人就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D0C")

    Jump("loc_4786")

    label("loc_3D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3E44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DC4")
    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "昨天晚上，\x01",
            "蔡斯发生了奇怪的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "导力竟然都停止了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "唔～\x01",
            "那种事情真的会发生吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E41")

    label("loc_3DC4")


    ChrTalk(
        0xA,
        (
            "据说昨晚蔡斯的\x01",
            "导力发生了停止现象……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "有点难以置信呢。\x01",
            "导力器竟然会停止工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E41")

    Jump("loc_4786")

    label("loc_3E44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_44A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43A4")
    EventBegin(0x0)
    Fade(1000)
    OP_8C(0xA, 90, 0)
    SetChrPos(0x101, -2800, 0, 6800, 270)
    SetChrPos(0x102, -2800, 0, 8000, 270)
    SetChrPos(0x105, -1800, 0, 7200, 270)
    OP_6D(-3900, 0, 7800, 1000)

    ChrTalk(
        0xA,
        (
            "你们好。\x01",
            "请问有什么事呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们想进入蔡斯地区，\x01",
            "请问能帮我们办理通行手续吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "啊，是这样啊。\x01",
            "那就请到这边的柜台。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "通行手续办好之后，\x01",
            "你们就无法再返回卢安地区了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "这样可以吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【办理通行手续】\x01",      # 0
            "【还是算了】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4069"),
        (1, "loc_4361"),
        (SWITCH_DEFAULT, "loc_439F"),
    )


    label("loc_4069")

    OP_A2(0x502)

    ChrTalk(
        0x101,
        (
            "#006F嗯，\x01",
            "就麻烦您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "那么，\x01",
            "请在这些文件上签字吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔和约修亚\x01",
            "在通行手续的文件上签了字。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0xA,
        "好的，这样就ＯＫ了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "请问那位小姐\x01",
            "也要办理通行手续吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F啊……\x01",
            "我只是来为他们送行的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "哦，这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "那么你可以一直送到\x01",
            "卡鲁迪亚隧道的入口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#041F真是太感谢了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#501F卡鲁迪亚隧道？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "嗯，没错。\x01",
            "是一直连接到蔡斯市的地下通道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "那可是一条贯穿整个\x01",
            "卡鲁迪亚丘陵的超长隧道哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎～是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F地下的隧道吗……\x01",
            "还是第一次走这种地方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_439F")

    label("loc_4361")


    ChrTalk(
        0xA,
        (
            "那么，\x01",
            "准备好了之后再来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_439F")

    label("loc_439F")

    EventEnd(0x0)
    Jump("loc_44A6")

    label("loc_43A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 3)), scpexpr(EXPR_END)), "loc_4425")

    ChrTalk(
        0xA,
        "哦，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "既然已经办好通行手续，\x01",
            "就不能再从这个关所回去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44A6")

    label("loc_4425")


    ChrTalk(
        0xA,
        (
            "送行的人可以送到\x01",
            "卡鲁迪亚隧道入口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "那么各位，\x01",
            "路上请务必小心行走。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44A6")

    Jump("loc_4786")

    label("loc_44A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_4658")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4627")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4591")
    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "没想到他竟然是\x01",
            "艾莉茜雅女王的侄子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "这次也是由于我传达的命令不当\x01",
            "而引发了这个事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "哎呀呀，\x01",
            "吃饭的时候又要被副长挖苦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4624")

    label("loc_4591")


    ChrTalk(
        0xA,
        (
            "这次也是由于我传达的命令不当\x01",
            "而引发了这个事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "哎呀呀，\x01",
            "吃饭的时候又要被副长挖苦了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4624")

    Jump("loc_4655")

    label("loc_4627")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_4634")
    Jump("loc_4655")

    label("loc_4634")


    ChrTalk(
        0xA,
        "副长他没事吧……\x02",
    )

    CloseMessageWindow()

    label("loc_4655")

    Jump("loc_4786")

    label("loc_4658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_4786")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4761")
    OP_4A(0x8, 255)
    OP_A2(0x0)
    OP_A2(0x2)

    ChrTalk(
        0x8,
        (
            "听说公爵要到\x01",
            "卢安市去进行访问，\x01",
            "不过没听说过会到这里来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "唉，\x01",
            "好像是根据他本人的意愿\x01",
            "而突然改变预定计划的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "呼，这就没办法了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "视察的相关事项\x01",
            "本来已经准备好了的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "是！\x02",
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_4786")

    label("loc_4761")


    ChrTalk(
        0xA,
        (
            "好像有一个大人物\x01",
            "突然要来这里访问。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4786")

    TalkEnd(0xA)
    Return()

    # Function_12_3878 end

    def Function_13_478A(): pass

    label("Function_13_478A")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_4797")
    Jump("loc_49CE")

    label("loc_4797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_47A1")
    Jump("loc_49CE")

    label("loc_47A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_47AB")
    Jump("loc_49CE")

    label("loc_47AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_47B5")
    Jump("loc_49CE")

    label("loc_47B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_47C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_47C6")
    Jump("loc_47C6")

    label("loc_47C6")

    Jump("loc_49CE")

    label("loc_47C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_47D3")
    Jump("loc_49CE")

    label("loc_47D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_493C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_485D")

    ChrTalk(
        0xFE,
        "他居然是王家的人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我可不想让其他国家的人知道\x01",
            "我们王国有如此蛮横的家伙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4939")

    label("loc_485D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_48FD")

    ChrTalk(
        0xFE,
        (
            "嗯，士兵碰上这种事\x01",
            "也是没有办法的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "他们的心情我能理解。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4939")

    label("loc_48FD")


    ChrTalk(
        0xFE,
        (
            "嗯嗯，\x01",
            "那种我行我素的人到处都有。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4939")

    Jump("loc_49CE")

    label("loc_493C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_49CE")

    ChrTalk(
        0xFE,
        "哇啊～这里真美。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "住宿又便宜，\x01",
            "想在这里住多久都行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49CE")

    TalkEnd(0x13)
    Return()

    # Function_13_478A end

    def Function_14_49D2(): pass

    label("Function_14_49D2")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_49DF")
    Jump("loc_4B25")

    label("loc_49DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_49E9")
    Jump("loc_4B25")

    label("loc_49E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_49F3")
    Jump("loc_4B25")

    label("loc_49F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_49FD")
    Jump("loc_4B25")

    label("loc_49FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4A11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_4A0E")
    Jump("loc_4A0E")

    label("loc_4A0E")

    Jump("loc_4B25")

    label("loc_4A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_4A1B")
    Jump("loc_4B25")

    label("loc_4A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_4ADC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4A96")

    ChrTalk(
        0xFE,
        (
            "你们几个\x01",
            "就是解决事件的人吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不愧是游击士啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4AD9")

    label("loc_4A96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_4ABE")

    ChrTalk(
        0xFE,
        "真伤脑筋……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4AD9")

    label("loc_4ABE")


    ChrTalk(
        0xFE,
        "真伤脑筋……\x02",
    )

    CloseMessageWindow()

    label("loc_4AD9")

    Jump("loc_4B25")

    label("loc_4ADC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_4B25")

    ChrTalk(
        0xFE,
        (
            "虽说瀑布的水声很大，\x01",
            "可是心里却感觉很平静呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B25")

    TalkEnd(0x14)
    Return()

    # Function_14_49D2 end

    def Function_15_4B29(): pass

    label("Function_15_4B29")

    Call(0, 16)
    Return()

    # Function_15_4B29 end

    def Function_16_4B2E(): pass

    label("Function_16_4B2E")

    TalkBegin(0x15)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "离开\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B8E")
    OP_0D()
    OP_A9(0x35)
    OP_56(0x0)
    TalkEnd(0x15)
    Return()

    label("loc_4B8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B9F")
    TalkEnd(0x15)
    Return()

    label("loc_4B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_4DC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D4B")
    OP_A2(0x4)

    ChrTalk(
        0x15,
        (
            "留宿的人忘了带走的东西\x01",
            "可真不少呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "虽然我们都暂时代为保管了，\x01",
            "但很少有人回来取。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "这本书也是\x01",
            "无人认领的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "……啊，想要这本书吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "唔～………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "你们能替我向队长保密吗？\x01",
            "因为这是违反规定的呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5D1)
    OP_3E(0x219, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "红耀石　第８卷\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_4DC2")

    label("loc_4D4B")


    ChrTalk(
        0x15,
        "你们是旅行者吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "这个时候为了诞辰庆典，\x01",
            "大家都赶往王都了，很少有人到这里来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DC2")

    Jump("loc_5587")

    label("loc_4DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_4F55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EB6")
    OP_A2(0x4)

    ChrTalk(
        0x15,
        (
            "刚才基恩茨副长来了，\x01",
            "很粗暴地对我们大声吼叫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "太、太可怕了，\x01",
            "好像一下就变得勃然大怒了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "是发生了什么\x01",
            "难以忍受的事情吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F52")

    label("loc_4EB6")


    ChrTalk(
        0x15,
        (
            "呼，我们的副长\x01",
            "平常是个乐呵呵的人……\x01",
            "可一旦发怒就会变得极为恐怖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "这种事情\x01",
            "无论谁听了\x01",
            "都会发怒啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F52")

    Jump("loc_5587")

    label("loc_4F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_507C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FF8")
    OP_A2(0x4)

    ChrTalk(
        0x15,
        (
            "总、总觉得\x01",
            "好像出大事了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "我们这个关所\x01",
            "也进入了前所未有的\x01",
            "警戒状态了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5079")

    label("loc_4FF8")


    ChrTalk(
        0x15,
        (
            "唉，\x01",
            "光是听说袭击事件什么的\x01",
            "就让人毛骨悚然了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "好希望早日能够将\x01",
            "犯人绳之以法啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5079")

    Jump("loc_5587")

    label("loc_507C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_519F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5119")
    OP_A2(0x4)

    ChrTalk(
        0x15,
        "哟，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "蔡斯那里\x01",
            "好像出事了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "导力器竟然都停止运转了。\x01",
            "这世界上还有这等奇妙的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_519C")

    label("loc_5119")


    ChrTalk(
        0x15,
        (
            "据说是由于中央工房的\x01",
            "实验而导致的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "可是不管是怎样的实验，\x01",
            "也不至于把导力都给停止了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_519C")

    Jump("loc_5587")

    label("loc_519F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_5370")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_531E")
    OP_A2(0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51E2")

    ChrTalk(
        0x15,
        "哟，欢迎来到艾尔·雷登。\x02",
    )

    CloseMessageWindow()
    Jump("loc_531B")

    label("loc_51E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5245")

    ChrTalk(
        0x15,
        "哦，你们是兄妹结伴旅行吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "从这里可以近距离看到瀑布，\x01",
            "是个最佳的住宿地点哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_531B")

    label("loc_5245")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52BB")

    ChrTalk(
        0x15,
        "哦，你们是兄妹结伴旅行吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "从这里可以近距离看到瀑布，\x01",
            "是个最佳的住宿地点哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_531B")

    label("loc_52BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_531B")

    ChrTalk(
        0x15,
        (
            "哟，\x01",
            "相当年轻的旅客啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "是和哥哥姐姐一起来旅行的吗？\x02",
    )

    CloseMessageWindow()

    label("loc_531B")

    Jump("loc_536D")

    label("loc_531E")


    ChrTalk(
        0x15,
        (
            "如果有什么事情，\x01",
            "和我说一声就是了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "那么，旅途愉快。\x02",
    )

    CloseMessageWindow()

    label("loc_536D")

    Jump("loc_5587")

    label("loc_5370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_53F0")

    ChrTalk(
        0x15,
        (
            "哟，欢迎光临。\x01",
            "这里是旅行者的住宿设施。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "想要休息的时候\x01",
            "就请告诉我一声。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5587")

    label("loc_53F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_5516")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5478")

    ChrTalk(
        0x15,
        (
            "这么长时间\x01",
            "一直在吵吵闹闹的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "过会儿向副长问一下\x01",
            "发生了什么事吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5513")

    label("loc_5478")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_54CC")

    ChrTalk(
        0x15,
        "外面真吵啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "有什么人在挑起纷争吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5513")

    label("loc_54CC")


    ChrTalk(
        0x15,
        "外面真吵啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "有什么人在挑起纷争吗？\x02",
    )

    CloseMessageWindow()

    label("loc_5513")

    Jump("loc_5587")

    label("loc_5516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_5587")

    ChrTalk(
        0x15,
        (
            "今天希望在这里留宿的客人\x01",
            "好像很多呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "得早点去\x01",
            "把房间打扫干净才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5587")

    TalkEnd(0x15)
    Return()

    # Function_16_4B2E end

    def Function_17_558B(): pass

    label("Function_17_558B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5629")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55AA")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_55B1")

    label("loc_55AA")

    TurnDirection(0x102, 0x0, 400)

    label("loc_55B1")


    ChrTalk(
        0x102,
        (
            "#010F这边是卢安地区啊。\x02\x03",
            "我们没有拿到通行证，\x01",
            "是不能从这边出去的。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_56B2")

    label("loc_5629")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56B2")
    EventBegin(0x1)
    OP_4A(0xE, 255)
    TurnDirection(0xE, 0x101, 0)

    ChrTalk(
        0xE,
        (
            "#012F艾丝蒂尔，\x01",
            "赶快去食堂看看情况吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    OP_8C(0xE, 0, 0)
    OP_4B(0xE, 255)
    Sleep(50)
    EventEnd(0x4)

    label("loc_56B2")

    Return()

    # Function_17_558B end

    def Function_18_56B3(): pass

    label("Function_18_56B3")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_18_56B3 end

    SaveToFile()

Try(main)
