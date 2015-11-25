from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2131   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2131   ._SN',
            'ED6_DT01/T2131_1 ._SN',
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
        '修比拉老板',                           # 9
        '照相机',                               # 10
        '加鲁诺',                               # 11
        '杜南公爵',                             # 12
        '管家菲利普',                           # 13
        '奈尔',                                 # 14
        '西蒙',                                 # 15
        '梅尔茨',                               # 16
        '普莱米奥',                             # 17
        '哈尔德',                               # 18
        '鲁特尔',                               # 19
        '兰达老人',                             # 20
        '米优',                                 # 21
        '西加罗',                               # 22
        '艾德尔',                               # 23
        '斯库阿洛',                             # 24
        '塞卡鲁特',                             # 25
        '贝斯卡',                               # 26
        '波尔',                                 # 27
        '吉米',                                 # 28
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
        'ED6_DT07/CH01270 ._CH',             # 00
        'ED6_DT07/CH01190 ._CH',             # 01
        'ED6_DT07/CH02140 ._CH',             # 02
        'ED6_DT07/CH02470 ._CH',             # 03
        'ED6_DT07/CH02060 ._CH',             # 04
        'ED6_DT07/CH01143 ._CH',             # 05
        'ED6_DT07/CH01760 ._CH',             # 06
        'ED6_DT07/CH01560 ._CH',             # 07
        'ED6_DT07/CH01570 ._CH',             # 08
        'ED6_DT07/CH01210 ._CH',             # 09
        'ED6_DT07/CH01023 ._CH',             # 0A
        'ED6_DT07/CH01123 ._CH',             # 0B
        'ED6_DT07/CH01020 ._CH',             # 0C
        'ED6_DT07/CH01000 ._CH',             # 0D
        'ED6_DT07/CH01050 ._CH',             # 0E
        'ED6_DT07/CH01043 ._CH',             # 0F
        'ED6_DT07/CH01213 ._CH',             # 10
        'ED6_DT07/CH01443 ._CH',             # 11
        'ED6_DT07/CH01460 ._CH',             # 12
        'ED6_DT07/CH01123 ._CH',             # 13
        'ED6_DT07/CH01023 ._CH',             # 14
        'ED6_DT07/CH01003 ._CH',             # 15
        'ED6_DT07/CH01053 ._CH',             # 16
    )

    AddCharChipPat(
        'ED6_DT07/CH01270P._CP',             # 00
        'ED6_DT07/CH01190P._CP',             # 01
        'ED6_DT07/CH02140P._CP',             # 02
        'ED6_DT07/CH02470P._CP',             # 03
        'ED6_DT07/CH02060P._CP',             # 04
        'ED6_DT07/CH01143P._CP',             # 05
        'ED6_DT07/CH01760P._CP',             # 06
        'ED6_DT07/CH01560P._CP',             # 07
        'ED6_DT07/CH01570P._CP',             # 08
        'ED6_DT07/CH01210P._CP',             # 09
        'ED6_DT07/CH01023P._CP',             # 0A
        'ED6_DT07/CH01123P._CP',             # 0B
        'ED6_DT07/CH01020P._CP',             # 0C
        'ED6_DT07/CH01000P._CP',             # 0D
        'ED6_DT07/CH01050P._CP',             # 0E
        'ED6_DT07/CH01043P._CP',             # 0F
        'ED6_DT07/CH01213P._CP',             # 10
        'ED6_DT07/CH01443P._CP',             # 11
        'ED6_DT07/CH01460P._CP',             # 12
        'ED6_DT07/CH01123P._CP',             # 13
        'ED6_DT07/CH01023P._CP',             # 14
        'ED6_DT07/CH01003P._CP',             # 15
        'ED6_DT07/CH01053P._CP',             # 16
    )

    DeclNpc(
        X                   = 24640,
        Z                   = 0,
        Y                   = 27000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
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
        X                   = 500,
        Z                   = 0,
        Y                   = 2200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 32400,
        Z                   = 0,
        Y                   = 28200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 31600,
        Z                   = 0,
        Y                   = 29700,
        Direction           = 145,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -3500,
        Z                   = 300,
        Y                   = 34200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 7000,
        Z                   = 300,
        Y                   = 29100,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -3490,
        Z                   = 250,
        Y                   = 32049,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -5500,
        Z                   = 300,
        Y                   = 33800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 2900,
        Z                   = 300,
        Y                   = 26900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 2900,
        Z                   = 300,
        Y                   = 29150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 29260,
        Z                   = 400,
        Y                   = 30200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 27050,
        Z                   = 400,
        Y                   = 30200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -6400,
        Z                   = 300,
        Y                   = 27200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -4000,
        Z                   = 300,
        Y                   = 27200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -2940,
        Z                   = 0,
        Y                   = 5590,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -21740,
        Z                   = 200,
        Y                   = 1670,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -1940,
        Z                   = 0,
        Y                   = 1220,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -17720,
        Z                   = 250,
        Y                   = -840,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 6870,
        Z                   = 250,
        Y                   = 29240,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )


    DeclActor(
        TriggerX            = 25600,
        TriggerZ            = 0,
        TriggerY            = 28000,
        TriggerRange        = 1400,
        ActorX              = 24920,
        ActorZ              = 1000,
        ActorY              = 28100,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4000,
        TriggerZ            = 250,
        TriggerY            = 33700,
        TriggerRange        = 400,
        ActorX              = -5500,
        ActorZ              = 1800,
        ActorY              = 33800,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -23760,
        TriggerZ            = 0,
        TriggerY            = 6340,
        TriggerRange        = 1400,
        ActorX              = -23760,
        ActorZ              = 1500,
        ActorY              = 6340,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 28730,
        TriggerZ            = 0,
        TriggerY            = 37220,
        TriggerRange        = 800,
        ActorX              = 28730,
        ActorZ              = 1800,
        ActorY              = 37220,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_472",          # 00, 0
        "Function_1_62E",          # 01, 1
        "Function_2_6CF",          # 02, 2
        "Function_3_6E5",          # 03, 3
        "Function_4_182D",         # 04, 4
        "Function_5_190D",         # 05, 5
        "Function_6_1F5C",         # 06, 6
        "Function_7_24B9",         # 07, 7
        "Function_8_2AE7",         # 08, 8
        "Function_9_2B7F",         # 09, 9
        "Function_10_2C4C",        # 0A, 10
        "Function_11_2DA1",        # 0B, 11
        "Function_12_2F69",        # 0C, 12
        "Function_13_31DC",        # 0D, 13
        "Function_14_3855",        # 0E, 14
        "Function_15_385A",        # 0F, 15
        "Function_16_4839",        # 10, 16
        "Function_17_51A5",        # 11, 17
        "Function_18_5458",        # 12, 18
        "Function_19_54F0",        # 13, 19
        "Function_20_5511",        # 14, 20
        "Function_21_5532",        # 15, 21
        "Function_22_559B",        # 16, 22
        "Function_23_564E",        # 17, 23
        "Function_24_5728",        # 18, 24
    )


    def Function_0_472(): pass

    label("Function_0_472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4B9")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    SetChrPos(0x8, 29470, 0, 32220, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A7")
    Jump("loc_4B6")

    label("loc_4A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4B6")
    ClearChrFlags(0x1B, 0x80)

    label("loc_4B6")

    Jump("loc_62D")

    label("loc_4B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_500")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    SetChrPos(0x8, 29470, 0, 32220, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EE")
    Jump("loc_4FD")

    label("loc_4EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4FD")
    ClearChrFlags(0x1B, 0x80)

    label("loc_4FD")

    Jump("loc_62D")

    label("loc_500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_54C")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    SetChrPos(0x8, 29470, 0, 32220, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53A")
    Jump("loc_549")

    label("loc_53A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_549")
    ClearChrFlags(0x1B, 0x80)

    label("loc_549")

    Jump("loc_62D")

    label("loc_54C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_574")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_571")
    ClearChrFlags(0x1B, 0x80)

    label("loc_571")

    Jump("loc_62D")

    label("loc_574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_5A3")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x8, 29470, 0, 32220, 180)
    Jump("loc_62D")

    label("loc_5A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_5CD")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    SetChrPos(0x8, 29470, 0, 32220, 180)
    Jump("loc_62D")

    label("loc_5CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_5FC")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x8, 29470, 0, 32220, 180)
    Jump("loc_62D")

    label("loc_5FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_610")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    Jump("loc_62D")

    label("loc_610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_62D")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x8, 29470, 0, 32220, 180)

    label("loc_62D")

    Return()

    # Function_0_472 end

    def Function_1_62E(): pass

    label("Function_1_62E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_64F")
    OP_B1("t2131_y")
    Jump("loc_658")

    label("loc_64F")

    OP_B1("t2131_n")

    label("loc_658")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x8)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_677")
    OP_64(0x0, 0x1)

    label("loc_677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_681")
    Jump("loc_6CE")

    label("loc_681")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_68B")
    Jump("loc_6CE")

    label("loc_68B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_695")
    Jump("loc_6CE")

    label("loc_695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_69F")
    Jump("loc_6CE")

    label("loc_69F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_6A9")
    Jump("loc_6CE")

    label("loc_6A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_6B3")
    Jump("loc_6CE")

    label("loc_6B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_6BD")
    Jump("loc_6CE")

    label("loc_6BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_6C7")
    Jump("loc_6CE")

    label("loc_6C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_6CE")

    label("loc_6CE")

    Return()

    # Function_1_62E end

    def Function_2_6CF(): pass

    label("Function_2_6CF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6CF")

    label("loc_6E4")

    Return()

    # Function_2_6CF end

    def Function_3_6E5(): pass

    label("Function_3_6E5")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x332)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B8")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                             # 0
            "买东西\x01",                           # 1
            "欢迎品尝「健康泡饭」500米拉\x01",      # 2
            "归还钓鱼竿\x01",                       # 3
            "离开\x01",                             # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_788")
    OP_0D()
    OP_A9(0x24)
    OP_56(0x0)
    TalkEnd(0x17)
    Return()

    label("loc_788")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_862")
    SubMira(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "尝了尝\x07\x02",
            "健康泡饭\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x2EE)
    OP_31(0x1, 0xFD, 0x2EE)
    OP_31(0x2, 0xFD, 0x2EE)
    OP_31(0x3, 0xFD, 0x2EE)
    OP_31(0x4, 0xFD, 0x2EE)
    OP_31(0x5, 0xFD, 0x2EE)
    OP_31(0x6, 0xFD, 0x2EE)
    OP_31(0x7, 0xFD, 0x2EE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_854")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x6)"), scpexpr(EXPR_END)), "loc_820")
    Jump("loc_854")

    label("loc_820")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "学会了\x07\x02",
            "健康泡饭\x07\x00",
            "的做法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_854")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_88A")

    label("loc_862")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_88A")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x17)
    Return()

    label("loc_89C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A4")
    OP_3F(0x332, 1)
    Sleep(400)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了\x07\x02",
            "钓鱼竿\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0xFE,
        (
            "哦，辛苦了。\x01",
            "钓鱼的成果怎么样啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果饿了就告诉我。\x01",
            "我给你们做最好的料理。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x17)
    Return()

    label("loc_9A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B5")
    TalkEnd(0x17)
    Return()

    label("loc_9B5")

    Jump("loc_DE4")

    label("loc_9B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x332)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C42")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                             # 0
            "买东西\x01",                           # 1
            "欢迎品尝「健康泡饭」500米拉\x01",      # 2
            "借钓鱼竿\x01",                         # 3
            "离开\x01",                             # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A62")
    OP_0D()
    OP_A9(0x24)
    OP_56(0x0)
    TalkEnd(0x17)
    Return()

    label("loc_A62")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B76")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B3C")
    SubMira(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "尝了尝\x07\x02",
            "健康泡饭\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x2EE)
    OP_31(0x1, 0xFD, 0x2EE)
    OP_31(0x2, 0xFD, 0x2EE)
    OP_31(0x3, 0xFD, 0x2EE)
    OP_31(0x4, 0xFD, 0x2EE)
    OP_31(0x5, 0xFD, 0x2EE)
    OP_31(0x6, 0xFD, 0x2EE)
    OP_31(0x7, 0xFD, 0x2EE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B2E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x6)"), scpexpr(EXPR_END)), "loc_AFA")
    Jump("loc_B2E")

    label("loc_AFA")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "学会了\x07\x02",
            "健康泡饭\x07\x00",
            "的做法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2E")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_B64")

    label("loc_B3C")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_B64")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x17)
    Return()

    label("loc_B76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2E")

    ChrTalk(
        0xFE,
        "哦，要去钓鱼吗？\x02",
    )

    CloseMessageWindow()
    OP_3E(0x332, 1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "借来了\x07\x02",
            "钓鱼竿\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0xFE,
        (
            "如果用完了，\x01",
            "记得把它还回来。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x17)
    Return()

    label("loc_C2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C3F")
    TalkEnd(0x17)
    Return()

    label("loc_C3F")

    Jump("loc_DE4")

    label("loc_C42")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "对话\x01",                             # 0
            "买东西\x01",                           # 1
            "欢迎品尝「健康泡饭」500米拉\x01",      # 2
            "离开\x01",                             # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBF")
    OP_0D()
    OP_A9(0x24)
    OP_56(0x0)
    TalkEnd(0x17)
    Return()

    label("loc_CBF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD3")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D99")
    SubMira(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "尝了尝\x07\x02",
            "健康泡饭\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x2EE)
    OP_31(0x1, 0xFD, 0x2EE)
    OP_31(0x2, 0xFD, 0x2EE)
    OP_31(0x3, 0xFD, 0x2EE)
    OP_31(0x4, 0xFD, 0x2EE)
    OP_31(0x5, 0xFD, 0x2EE)
    OP_31(0x6, 0xFD, 0x2EE)
    OP_31(0x7, 0xFD, 0x2EE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D8B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x6)"), scpexpr(EXPR_END)), "loc_D57")
    Jump("loc_D8B")

    label("loc_D57")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "学会了\x07\x02",
            "健康泡饭\x07\x00",
            "的做法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8B")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_DC1")

    label("loc_D99")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_DC1")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x17)
    Return()

    label("loc_DD3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DE4")
    TalkEnd(0x17)
    Return()

    label("loc_DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x1000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x800)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1050")
    OP_28(0x21, 0x1, 0x800)

    ChrTalk(
        0xFE,
        "您好，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F请问一下，\x01",
            "能把二楼的那个钓鱼竿借给我们吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哦，当然可以。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们只要说一声，\x01",
            "随时都可以借走的。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【借钓鱼竿】\x01",      # 0
            "【不借】\x01",          # 1
        )
    )

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FEC")
    OP_0D()
    OP_3E(0x332, 1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "借来了\x07\x02",
            "钓鱼竿\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0xFE,
        (
            "如果用完了，\x01",
            "记得把它还回来。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x17)
    Return()

    label("loc_FEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_104D")

    ChrTalk(
        0xFE,
        "如果需要，随时可以找我。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我会马上把钓鱼竿借给你们的。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x17)
    Return()

    label("loc_104D")

    Jump("loc_1829")

    label("loc_1050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_11DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_112C")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        "现任市长已经被罢免了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算是戴尔蒙家族的人，\x01",
            "做出这种伤天害理的事，\x01",
            "也肯定是要受到惩治的啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就连那些小混混也都被这件事吓一跳，\x01",
            "都说戴尔蒙做得太过分了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11D9")

    label("loc_112C")


    ChrTalk(
        0xFE,
        (
            "选下一届市长的话，\x01",
            "还是要选波尔多斯老大。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是他做市长的话，\x01",
            "我想一定能把卢安治理好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D9")

    Jump("loc_1829")

    label("loc_11DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1310")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_128E")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "市长曾经准备\x01",
            "停止提供对港湾设施的援助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果不是波尔多斯老大直接和他面谈的话，\x01",
            "还不知道会怎样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "卢安还是很需要一个港口的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_130D")

    label("loc_128E")


    ChrTalk(
        0xFE,
        (
            "市长曾经准备\x01",
            "停止提供对港湾设施的援助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果不是波尔多斯老大直接和他面谈的话，\x01",
            "还不知道会怎样呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_130D")

    Jump("loc_1829")

    label("loc_1310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_13DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A4")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "刚才有个红头发的游击士\x01",
            "来这里打听了一些事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯～\x01",
            "我好像在哪里见过他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13DA")

    label("loc_13A4")


    ChrTalk(
        0xFE,
        (
            "刚才那个红头发的游击士\x01",
            "我好像在哪里见过他……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13DA")

    Jump("loc_1829")

    label("loc_13DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1598")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1505")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "渡鸦帮的那些人\x01",
            "也经常来这家店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在的那些家伙\x01",
            "并不是粗野，\x01",
            "而只是没骨气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为对自己没有信心，\x01",
            "而将愤怒发泄在周围的人身上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过他们以前\x01",
            "可确实是坏到骨子里了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1595")

    label("loc_1505")


    ChrTalk(
        0xFE,
        (
            "现在渡鸦帮的那些人\x01",
            "并不是粗野，而只是没骨气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过他们以前\x01",
            "可确实是坏到骨子里了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1595")

    Jump("loc_1829")

    label("loc_1598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_174F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_168E")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        "我原来也是个渔夫。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这家店里所使用的材料，\x01",
            "都是我起早摸黑\x01",
            "出海捕获而来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我可不是在自夸，\x01",
            "这里的菜总是卢安最新鲜的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_174C")

    label("loc_168E")


    ChrTalk(
        0xFE,
        (
            "这家店里所使用的材料，\x01",
            "都是我起早摸黑\x01",
            "出海捕获而来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我可不是在自夸，\x01",
            "这里的菜总是卢安最新鲜的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_174C")

    Jump("loc_1829")

    label("loc_174F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_1829")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17FE")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "您好，欢迎光临！\x01",
            "这里是亚克罗萨船员酒吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里主要是\x01",
            "渔夫和船员集中的酒馆，\x01",
            "当然也欢迎一般的顾客啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1829")

    label("loc_17FE")


    ChrTalk(
        0xFE,
        (
            "欢迎光临！\x01",
            "这里是亚克罗萨船员酒吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1829")

    TalkEnd(0x17)
    Return()

    # Function_3_6E5 end

    def Function_4_182D(): pass

    label("Function_4_182D")

    TalkBegin(0xA)

    ChrTalk(
        0xFE,
        (
            "定期船停航了，\x01",
            "我只能从蔡斯步行而来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，真是的。\x01",
            "路上好危险呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀哎呀，\x01",
            "我再也不想这样了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_4_182D end

    def Function_5_190D(): pass

    label("Function_5_190D")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_19AE")

    ChrTalk(
        0xFE,
        (
            "马上就要出航了，\x01",
            "遇上选举的话我就不能投票了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，要是能选出一个\x01",
            "为港口事业着想的好市长，\x01",
            "那对我们来说就最好不过了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F58")

    label("loc_19AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1B4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AAD")
    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "下一次出海，\x01",
            "要向埃雷波尼亚帝国运送导力器制品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们的港口有很多军舰驻扎，\x01",
            "很有压迫感……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "即使现在想到入港的时候，\x01",
            "我还是会觉得很紧张。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B4A")

    label("loc_1AAD")


    ChrTalk(
        0xFE,
        (
            "下一次出海，\x01",
            "要向埃雷波尼亚帝国运送导力器制品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们的港口有很多军舰驻扎，\x01",
            "那种压迫感让我感到很紧张……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B4A")

    Jump("loc_1F58")

    label("loc_1B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1C90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1F")
    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "我在休假日\x01",
            "也要帮忙装载货物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "该让我多休息会儿才对。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……但是，\x01",
            "我可没有放弃当水手的打算。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还是很喜欢大海的，\x01",
            "而且这也是份值得骄傲的工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C8D")

    label("loc_1C1F")


    ChrTalk(
        0xFE,
        (
            "我在休假日\x01",
            "也要帮忙装载货物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……但是，\x01",
            "我可没有放弃当水手的打算。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C8D")

    Jump("loc_1F58")

    label("loc_1C90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1E00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D68")
    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "来这里的途中，\x01",
            "我看见有个孩子向着\x01",
            "仓库的方向飞奔过去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "奇怪了，\x01",
            "他要去那种地方做什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要不被仓库里的\x01",
            "那些家伙缠上就好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DFD")

    label("loc_1D68")


    ChrTalk(
        0xFE,
        (
            "来这里的途中，\x01",
            "我看见有个孩子向着\x01",
            "仓库的方向飞奔过去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要不被仓库里的\x01",
            "那些家伙缠上就好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DFD")

    Jump("loc_1F58")

    label("loc_1E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1EA3")

    ChrTalk(
        0xFE,
        "我是贸易商船的航海员。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然现在非常悠闲，\x01",
            "不过平时有好几个月要海上度过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F58")

    label("loc_1EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_1F58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F32")
    OP_A2(0xA)

    ChrTalk(
        0xFE,
        "嗝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我刚从卡尔瓦德共和国\x01",
            "返航回到这里来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好久没在陆地上了……嗝……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F58")

    label("loc_1F32")


    ChrTalk(
        0xFE,
        "老大～！！　再来一杯～！\x02",
    )

    CloseMessageWindow()

    label("loc_1F58")

    TalkEnd(0x18)
    Return()

    # Function_5_190D end

    def Function_6_1F5C(): pass

    label("Function_6_1F5C")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1FD5")

    ChrTalk(
        0xFE,
        "市长真的被捕了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然不很清楚情况，\x01",
            "不过好像发生了很不得了的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_1FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_206F")

    ChrTalk(
        0xFE,
        (
            "今天早上灯塔里的灯还是没有灭，\x01",
            "到底发生什么事情了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想那个弗科特大爷\x01",
            "不会像我们这种人一样\x01",
            "在偷懒打瞌睡吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_206F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_20DB")

    ChrTalk(
        0xFE,
        "呼，今天打渔大丰收。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "鱼总是集中在同一个地方，\x01",
            "这样打渔真是轻松啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_20DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2207")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_219F")
    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "仓库被那些家伙们占据着，\x01",
            "为什么市长一点表示都没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了，反正我是个渔夫，\x01",
            "这种麻烦的事情我可不想沾上什么边。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2204")

    label("loc_219F")


    ChrTalk(
        0xFE,
        (
            "仓库被那些家伙们占据着，\x01",
            "为什么市长一点表示都没有。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2204")

    Jump("loc_24B5")

    label("loc_2207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2347")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22BF")
    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "亚瑟利亚湾的海鲜\x01",
            "真的非常美味呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "对了，现在这个季节……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我向你们强烈推荐\x01",
            "菜单上的这个酒蒸鱼籽。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2344")

    label("loc_22BF")


    ChrTalk(
        0xFE,
        (
            "亚瑟利亚湾的海鲜\x01",
            "真的非常美味呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我向你们强烈推荐\x01",
            "菜单上的这个酒蒸鱼籽。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2344")

    Jump("loc_24B5")

    label("loc_2347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_24B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_242C")
    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "最近加入的同行\x01",
            "非常能干活呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我除了会捕鱼之外，\x01",
            "什么都不会了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之只要还有人吃鱼，\x01",
            "我就会继续做渔夫。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_242C")


    ChrTalk(
        0xFE,
        (
            "我除了会捕鱼之外，\x01",
            "什么都不会了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之只要还有人吃鱼，\x01",
            "我就会继续做渔夫。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24B5")

    TalkEnd(0x19)
    Return()

    # Function_6_1F5C end

    def Function_7_24B9(): pass

    label("Function_7_24B9")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2527")

    ChrTalk(
        0xFE,
        (
            "北街区那些家伙\x01",
            "应该是想选诺曼做市长吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们这边则是想选\x01",
            "波尔多斯来做市长。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AE3")

    label("loc_2527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_25B2")

    ChrTalk(
        0xFE,
        (
            "现在不同于以往，\x01",
            "港湾的设施建设都无法取得\x01",
            "计划中那么多预算。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然波尔多斯主任很辛苦，\x01",
            "但我还是希望作为负责人的他\x01",
            "能够更加努力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AE3")

    label("loc_25B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_26F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26AF")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "以前卢安是军事要地，\x01",
            "百日战役的时候这里可是激战连连。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之，如果这里被攻破，\x01",
            "到瓦雷利亚湖那一带就很容易被拿下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，在瓦雷利亚湖\x01",
            "还有一个坚不可摧的雷斯顿要塞。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26F3")

    label("loc_26AF")


    ChrTalk(
        0xFE,
        (
            "以前卢安是军事要地，\x01",
            "百日战役的时候这里可是激战连连。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26F3")

    Jump("loc_2AE3")

    label("loc_26F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_28C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2813")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "流经这个城市的卢比诺川\x01",
            "和位于利贝尔王国中央的\x01",
            "瓦雷利亚湖相连。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在港口装运的海外物资\x01",
            "都会经过这条运河\x01",
            "直接运送到位于湖畔的王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正因为这样，以前就有许多\x01",
            "从国外来的各式各样的商人聚集于此。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C2")

    label("loc_2813")


    ChrTalk(
        0xFE,
        (
            "流经这个城市的卢比诺川\x01",
            "和位于利贝尔王国中央的\x01",
            "瓦雷利亚湖相连。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在港口装运的海外物资\x01",
            "都会经过这条运河\x01",
            "直接运送到位于湖畔的王都。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28C2")

    Jump("loc_2AE3")

    label("loc_28C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2985")

    ChrTalk(
        0xFE,
        (
            "如果想赚钱的话，\x01",
            "比起做普通的船员，\x01",
            "还不如开展观光事业比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "在这里聚集的这些家伙们\x01",
            "可不是那么识时务……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AE3")

    label("loc_2985")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_2AE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A5D")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "出海之后喝的第一杯酒是非常特别的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……以前，\x01",
            "这里是船员和渔夫的城市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "现在出海的人数减少了很多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AE3")

    label("loc_2A5D")


    ChrTalk(
        0xFE,
        (
            "……以前，\x01",
            "这里是船员和渔夫的城市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "现在出海的人数减少了很多。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AE3")

    TalkEnd(0x1A)
    Return()

    # Function_7_24B9 end

    def Function_8_2AE7(): pass

    label("Function_8_2AE7")

    TalkBegin(0xB)

    ChrTalk(
        0xFE,
        (
            "#226F可恶，一个小小的女孩\x01",
            "竟敢羞辱我这个未来的国王……\x02\x03",
            "#224F嘿～一决胜负吧！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_8_2AE7 end

    def Function_9_2B7F(): pass

    label("Function_9_2B7F")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C03")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "#720F大人……大人……\x02\x03",
            "天色已经不早了，\x01",
            "我们还是回酒店去吧……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    Jump("loc_2C48")

    label("loc_2C03")


    ChrTalk(
        0xFE,
        (
            "#722F呼，\x01",
            "虽然我也知道和他说这些没什么用……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C48")

    TalkEnd(0xC)
    Return()

    # Function_9_2B7F end

    def Function_10_2C4C(): pass

    label("Function_10_2C4C")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_2D2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF7")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "#141F嘿嘿……\x01",
            "这样所有的消息都收集齐了。\x02\x03",
            "这可能是大家想象不到的独家新闻呢。\x01",
            "　\x02\x03",
            "#142F……接下来就是如何得到报道的确证了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D2A")

    label("loc_2CF7")


    ChrTalk(
        0xFE,
        (
            "#141F这可能是大家想象不到的独家新闻呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D2A")

    Jump("loc_2D9D")

    label("loc_2D2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2D9D")

    ChrTalk(
        0xFE,
        (
            "#141F哟，艾丝蒂尔、约修亚。\x02\x03",
            "如果有什么事件发生，\x01",
            "记得来给我提供资料啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D9D")

    TalkEnd(0xD)
    Return()

    # Function_10_2C4C end

    def Function_11_2DA1(): pass

    label("Function_11_2DA1")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2E67")

    ChrTalk(
        0xFE,
        (
            "赌博和做买卖\x01",
            "其实有几分相似。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "抱着玩玩儿的态度不会有什么压力，\x01",
            "但是比较容易上瘾。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F65")

    label("loc_2E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2F65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F15")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "呼，谈判结束了，\x01",
            "我终于能够休息一下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近，\x01",
            "米拉诺总是休假和出差连在一起。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F65")

    label("loc_2F15")


    ChrTalk(
        0xFE,
        (
            "呼，谈判结束了，\x01",
            "我终于能够休息一下了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F65")

    TalkEnd(0xE)
    Return()

    # Function_11_2DA1 end

    def Function_12_2F69(): pass

    label("Function_12_2F69")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_3018")

    ChrTalk(
        0xFE,
        (
            "阿加特前辈好厉害。\x01",
            "『重剑』的称号并非浪得虚名。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过在利贝尔\x01",
            "好像还有更加厉害的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D8")

    label("loc_3018")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_311D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B6")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "嘿哟、嘿哟……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "阿，阿嚏！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哆哆嗦嗦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "噗噜噗噜噗噜……\x01",
            "染上感冒后，\x01",
            "虽然很不舒服，\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_311A")

    label("loc_30B6")


    ChrTalk(
        0xFE,
        "不过我还是要吃很多饭！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "吃了之后才有体力，\x01",
            "随时准备出击是游击士的职责！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_311A")

    Jump("loc_31D8")

    label("loc_311D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_31D8")

    ChrTalk(
        0xFE,
        (
            "之前，我在沙滩那里\x01",
            "碰到一个非常敏捷的魔兽！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我本来想击退它的，\x01",
            "但是一攻击，那把非常硬的剑就断了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然那家伙很小，\x01",
            "但却绝不能小看它啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31D8")

    TalkEnd(0xF)
    Return()

    # Function_12_2F69 end

    def Function_13_31DC(): pass

    label("Function_13_31DC")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_32A4")

    ChrTalk(
        0xFE,
        "现役的市长被逮捕了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "根据利贝尔的法律，\x01",
            "要进行市长选举。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "谁会是候选人呢，\x01",
            "我对这一点\x01",
            "非常感兴趣啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3851")

    label("loc_32A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_337E")

    ChrTalk(
        0x8,
        (
            "市长对我们这样的观光设施\x01",
            "给予了很大的支持……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "而给港湾设施的预算\x01",
            "年年都在削减。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "许许多多不满的声音\x01",
            "也在日渐高涨。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3851")

    label("loc_337E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_33DC")

    ChrTalk(
        0x8,
        (
            "本店的改建\x01",
            "正在稳步进行中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "离新装修的店重新开张已经不远了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3851")

    label("loc_33DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_348A")

    ChrTalk(
        0x8,
        (
            "转旋转圆盘的手艺是\x01",
            "绝对不可以生疏下来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "为了让客人们得到消遣，\x01",
            "精彩的表演也是很重要的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3851")

    label("loc_348A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_350D")

    ChrTalk(
        0x8,
        (
            "为了配合重建，\x01",
            "也差不多该\x01",
            "购置个新轮盘了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我希望把这里装饰成\x01",
            "观光客们能够经常来的地方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3851")

    label("loc_350D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_36CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3624")
    OP_A2(0x6)

    ChrTalk(
        0x8,
        (
            "旺季的时候，\x01",
            "会有各地的游客过来玩两手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "一旦观光业繁荣起来，\x01",
            "客人会更加多吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "真希望这里快点装修完，\x01",
            "然后像以往那样再次热闹起来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36CA")

    label("loc_3624")


    ChrTalk(
        0x8,
        (
            "一旦观光业繁荣起来，\x01",
            "客人会更加多吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "真希望这里快点装修完，\x01",
            "然后像以往那样再次热闹起来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36CA")

    Jump("loc_3851")

    label("loc_36CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_3793")

    ChrTalk(
        0x8,
        (
            "人生啊，\x01",
            "就如同这个轮盘。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "即使今天非常顺手，\x01",
            "说不定明天可能全盘皆输。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "可以的话，就请珍惜现在，\x01",
            "好好享受不留遗憾。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3851")

    label("loc_3793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_3851")

    ChrTalk(
        0x8,
        (
            "拉旺塔尔赌吧\x01",
            "将于女王诞辰庆典举行的同时\x01",
            "重新向各位市民和游客开放。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "现在二楼的地板\x01",
            "正在全面重新装修中。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3851")

    TalkEnd(0x8)
    Return()

    # Function_13_31DC end

    def Function_14_3855(): pass

    label("Function_14_3855")

    Call(0, 15)
    Return()

    # Function_14_3855 end

    def Function_15_385A(): pass

    label("Function_15_385A")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4102")
    EventBegin(0x0)
    OP_4A(0x10, 255)

    ChrTalk(
        0x10,
        "您好，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "…………嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "喂，你们几个。\x01",
            "是要去巴伦诺灯塔吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3953")

    ChrTalk(
        0x101,
        (
            "#000F嗯，是的。\x02\x03",
            "我们要把这个维修工具箱\x01",
            "交给弗科特老人。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 0)
    Jump("loc_3A4E")

    label("loc_3953")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39CA")

    ChrTalk(
        0x102,
        (
            "#010F嗯，是啊。\x02\x03",
            "我们要把这个维修工具箱\x01",
            "交给弗科特老人。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 0)
    Jump("loc_3A4E")

    label("loc_39CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A4E")

    ChrTalk(
        0x105,
        (
            "#040F啊，是的。\x02\x03",
            "不过我只是\x01",
            "稍微帮一下忙……\x02\x03",
            "我们要把这个维修工具箱\x01",
            "交给看守灯塔的弗科特老人。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x105, 0)

    label("loc_3A4E")


    ChrTalk(
        0x10,
        (
            "果然是这样。\x01",
            "怪不得你们拿着个大箱子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "他老人家自从去了灯塔以后，\x01",
            "已经很久没来过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "希望他能够健康快乐啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F老爷爷他以前很喜欢到这个店里来吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0x10,
        (
            "他是一个老渔夫了，\x01",
            "对于酒和赌都很感兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "他老人家最喜欢的就是\x01",
            "用果实榨的汁所制成的、\x01",
            "名为『亚瑟利亚葡萄酒』的鸡尾酒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "这种鸡尾酒\x01",
            "和海鱼真是绝配。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "可是他去了灯塔之后\x01",
            "就再也没来品尝过了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "他的工作可是十分艰苦的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F嗯……\x01",
            "真的很可怜呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "哦，对了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "如果方便的话，\x01",
            "能带一瓶给他吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "反正你们要去灯塔，\x01",
            "所以我希望你们把鸡尾酒也带去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "这倒不是什么委托。\x01",
            "如果很忙的话，\x01",
            "你们不接受也没有关系的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F是给老爷爷捎去的对吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F我说，约修亚，\x01",
            "应该是可以的吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F嗯，我想没问题。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_3E94")
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#505F唔，又多了一个需要小心携带的东西呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#041F呵呵，是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3E94")


    ChrTalk(
        0x10,
        (
            "哦，\x01",
            "那么记得帮我向他老人家问好哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3EC3():
        TurnDirection(0x101, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3EC3)

    def lambda_3ED1():
        TurnDirection(0x102, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3ED1)

    def lambda_3EDF():
        TurnDirection(0x105, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3EDF)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x105, 0x1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "亚瑟利亚葡萄酒\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x1D, 0x1, 0x4)
    OP_3E(0x19A, 1)

    ChrTalk(
        0x10,
        (
            "如果有下酒菜就更好了，\x01",
            "不凑巧的是我这里的已经卖完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "这个季节用玛诺利亚村的特产\x01",
            "『辣鳀鱼』来下酒是最爽的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "……可惜没办法啊，\x01",
            "这次只有酒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "你们努力工作吧。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_407A")

    ChrTalk(
        0x101,
        "#000F嗯，再见了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F9")

    label("loc_407A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40BB")

    ChrTalk(
        0x102,
        "#010F嗯，再见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F再见了，大叔。\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F9")

    label("loc_40BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40F9")

    ChrTalk(
        0x105,
        "#040F那么我们告辞了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F再见了，大叔。\x02",
    )

    CloseMessageWindow()

    label("loc_40F9")

    EventEnd(0x1)
    OP_4B(0x10, 255)
    Jump("loc_4835")

    label("loc_4102")

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
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_415F")
    OP_0D()
    OP_A9(0x23)
    OP_56(0x0)
    TalkEnd(0x10)
    Return()

    label("loc_415F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4170")
    TalkEnd(0x10)
    Return()

    label("loc_4170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_42AD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_41F0")

    ChrTalk(
        0x10,
        (
            "老人家身体健康\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "特意帮忙送东西，真是谢谢你们。\x01",
            "那么，工作要加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42AA")

    label("loc_41F0")


    ChrTalk(
        0x10,
        (
            "这次的事情\x01",
            "你们可别往心里去哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "本来也是我\x01",
            "即兴拜托你们的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "反正慰问老人家的机会\x01",
            "以后还多的是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "到时候还要麻烦你们。\x02",
    )

    CloseMessageWindow()

    label("loc_42AA")

    Jump("loc_4835")

    label("loc_42AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_42BF")
    Call(0, 16)
    Jump("loc_4835")

    label("loc_42BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4545")
    OP_A2(0xD)
    OP_28(0x1D, 0x1, 0x2000)

    ChrTalk(
        0x10,
        (
            "哟，\x01",
            "送维修工具箱的工作完成了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        (
            "#003F嗯～抱歉。\x02\x03",
            "最后还是没办法把工具箱送过去呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F对不起。\x02\x03",
            "您还特地让我们送鸡尾酒的……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(
        0x10,
        "哦，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "你们不要介意。\x01",
            "本来也是我\x01",
            "即兴拜托你们的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "一开始我不是说了吗？\x01",
            "如果太忙的话，\x01",
            "不接受也没有关系的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F真是太过意不去了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0x10,
        (
            "慰问老人家的机会\x01",
            "以后还多的是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "到时候还要麻烦你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊，\x01",
            "以后也请多多关照。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(
        0x10,
        "哦，再见啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4835")

    label("loc_4545")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46DC")
    OP_28(0x1D, 0x1, 0x2000)
    OP_A2(0xD)

    ChrTalk(
        0x10,
        (
            "哟，送维修工具箱的\x01",
            "看起来工作已经完成了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "弗科特他老人家\x01",
            "身体还好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嗯，很健康呢。\x01",
            "还让我们向大家问好。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0x10,
        (
            "哦，是吗。\x01",
            "那真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "这么老了还坚持工作，\x01",
            "本来我一直很担心他的身体状况，\x01",
            "看来没什么事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "特意帮忙送东西，真是谢谢你们。\x01",
            "那么，工作要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，再见了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4835")

    label("loc_46DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4831")

    ChrTalk(
        0x10,
        "代我向老人家问好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "如果要是有下酒菜\x01",
            "就更好了…………\x01",
            "不凑巧的是我这里的已经卖完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "这个季节用玛诺利亚村的特产\x01",
            "『辣鳀鱼』来下酒是最爽的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "……可惜没办法啊，\x01",
            "这次只有酒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "好了，你们工作要努力哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4835")

    label("loc_4831")

    Call(0, 16)

    label("loc_4835")

    TalkEnd(0x10)
    Return()

    # Function_15_385A end

    def Function_16_4839(): pass

    label("Function_16_4839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_49CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4956")
    OP_A2(0x7)

    ChrTalk(
        0x10,
        (
            "渡鸦帮的家伙是被\x01",
            "施了催眠术一类的东西，\x01",
            "所以才做了市长的帮手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "不瞒你们，\x01",
            "我的弟弟也是其中的一员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "他们平常不做正经事，\x01",
            "是被社会摒弃的一群人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "真是不争气的家伙啊……\x01",
            "这就叫做自食其果。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49CC")

    label("loc_4956")


    ChrTalk(
        0x10,
        (
            "不瞒你们，\x01",
            "我的弟弟也是渡鸦帮的一员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "真是不争气的家伙啊……\x01",
            "这就叫做自食其果。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49CC")

    Jump("loc_51A1")

    label("loc_49CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_4ABE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A6D")
    OP_A2(0x7)

    ChrTalk(
        0x10,
        (
            "昨晚开始\x01",
            "我弟弟就一直没有回家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "他到底去哪里游手好闲了……\x01",
            "算了，反正他总会回来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ABB")

    label("loc_4A6D")


    ChrTalk(
        0x10,
        (
            "……唉，这个兔崽子，\x01",
            "从小时候开始就让我操心……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4ABB")

    Jump("loc_51A1")

    label("loc_4ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_4BA5")

    ChrTalk(
        0x10,
        (
            "二楼的改建到底\x01",
            "要到什么时候才能结束啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "平时会有许多旅客\x01",
            "慕名前来拉旺塔尔赌吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "不早点重新开业的话，\x01",
            "本店的招牌可要垮了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51A1")

    label("loc_4BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_4D58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C70")
    OP_A2(0x7)

    ChrTalk(
        0x10,
        (
            "哎呀哎呀，我弟弟这次\x01",
            "真是给游击士协会添了很大麻烦啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "我早就料到会有这一天的到来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "算了，这也是个让那群笨蛋\x01",
            "好好冷静一下的机会。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D55")

    label("loc_4C70")


    ChrTalk(
        0x10,
        "哎呀哎呀，弟弟那家伙……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "这次真是给游击士协会\x01",
            "添了很大的麻烦啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "算了，这也是个让那群笨蛋\x01",
            "好好冷静一下的机会。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D55")

    Jump("loc_51A1")

    label("loc_4D58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_4D92")

    ChrTalk(
        0x10,
        (
            "怎么了？\x01",
            "你们是来找什么人的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51A1")

    label("loc_4D92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_4ECF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E7D")
    OP_A2(0x7)

    ChrTalk(
        0x10,
        (
            "听说昨天弟弟\x01",
            "那帮家伙们缠上市长了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "反抗比自己地位高的人，\x01",
            "是想否定自己的自卑感吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "这样想来，他们还真是可悲啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4ECC")

    label("loc_4E7D")


    ChrTalk(
        0x10,
        (
            "好～\x01",
            "新的一天又开始了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "加油干吧。\x02",
    )

    CloseMessageWindow()

    label("loc_4ECC")

    Jump("loc_51A1")

    label("loc_4ECF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_5056")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FC3")
    OP_A2(0x7)

    ChrTalk(
        0x10,
        (
            "弟弟那家伙加入了\x01",
            "港口那边一个叫渡鸦帮的流氓集团。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "也不去找点工作做，\x01",
            "只会给别人惹麻烦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "真是一点也不知道羞耻，\x01",
            "怎么有脸去见老天爷啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5053")

    label("loc_4FC3")


    ChrTalk(
        0x10,
        (
            "弟弟那家伙加入了\x01",
            "港口那边一个叫渡鸦帮的流氓集团。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "真是一点也不知道羞耻，\x01",
            "怎么有脸去见老天爷啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5053")

    Jump("loc_51A1")

    label("loc_5056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_51A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_512A")
    OP_A2(0x7)

    ChrTalk(
        0x10,
        "第一次看到你们呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "你们是旅行者吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "如果是的话，\x01",
            "就不要靠近港口的仓库。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "那一带是\x01",
            "不良青年聚集的地方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51A1")

    label("loc_512A")


    ChrTalk(
        0x10,
        (
            "你们最好不要到\x01",
            "港口的仓库那边去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "那一带是\x01",
            "不良青年聚集的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51A1")

    TalkEnd(0x10)
    Return()

    # Function_16_4839 end

    def Function_17_51A5(): pass

    label("Function_17_51A5")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_52CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5259")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        "坐在那个座位上的人是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他不是米拉诺家的\x01",
            "西蒙那小子吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特里诺一家果然是\x01",
            "柏斯商人的憧憬啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52CA")

    label("loc_5259")


    ChrTalk(
        0xFE,
        (
            "米拉诺家的西蒙\x01",
            "来这里了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特里诺一家果然是\x01",
            "柏斯商人的憧憬啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52CA")

    Jump("loc_5454")

    label("loc_52CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_53D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5378")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "刚才在那边的牌桌上\x01",
            "和别人赌博……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果自己赢了，\x01",
            "当然很是高兴……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但如果被对手占了上风，\x01",
            "就会变得很不愉快了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53D1")

    label("loc_5378")


    ChrTalk(
        0xFE,
        (
            "如果自己赢了，\x01",
            "当然很是高兴……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但如果被对手占了上风，\x01",
            "就会变得很不愉快了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53D1")

    Jump("loc_5454")

    label("loc_53D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_5454")

    ChrTalk(
        0xFE,
        (
            "呼～因为定期船停航，\x01",
            "我本以为生意谈不成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "幸好我急急忙忙\x01",
            "从柏斯赶过来了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5454")

    TalkEnd(0x11)
    Return()

    # Function_17_51A5 end

    def Function_18_5458(): pass

    label("Function_18_5458")

    TalkBegin(0x12)
    OP_62(0x12, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "偶尔独自一人也不错啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "父亲和女儿在二楼玩。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_18_5458 end

    def Function_19_54F0(): pass

    label("Function_19_54F0")

    TalkBegin(0x13)

    ChrTalk(
        0xFE,
        "唔唔唔，再来一盘！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_19_54F0 end

    def Function_20_5511(): pass

    label("Function_20_5511")

    TalkBegin(0x14)

    ChrTalk(
        0xFE,
        (
            "好啊！！\x01",
            "又是我赢了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x14)
    Return()

    # Function_20_5511 end

    def Function_21_5532(): pass

    label("Function_21_5532")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_555E")

    ChrTalk(
        0xFE,
        "好，再来再来再来！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5597")

    label("loc_555E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_5597")

    ChrTalk(
        0xFE,
        (
            "虽然有点晚了，\x01",
            "不过我是来吃早饭的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5597")

    TalkEnd(0x15)
    Return()

    # Function_21_5532 end

    def Function_22_559B(): pass

    label("Function_22_559B")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_55C7")

    ChrTalk(
        0xFE,
        (
            "唔～一旦输了，\x01",
            "对胜负就会更加执着……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_564A")

    label("loc_55C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_564A")

    ChrTalk(
        0xFE,
        (
            "咦……\x01",
            "我以为赌吧的底楼应该会很吵的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这家店给人感觉非常清爽呢。\x02",
    )

    CloseMessageWindow()

    label("loc_564A")

    TalkEnd(0x16)
    Return()

    # Function_22_559B end

    def Function_23_564E(): pass

    label("Function_23_564E")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_56C9")

    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，\x01",
            "很快就可以解读这幅地图了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好～\x01",
            "这一次一定要找到海盗的财宝。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5724")

    label("loc_56C9")


    ChrTalk(
        0xFE,
        "唔唔～哦，原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，\x01",
            "这幅地图的大概含义我已经明白了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5724")

    TalkEnd(0x1B)
    Return()

    # Function_23_564E end

    def Function_24_5728(): pass

    label("Function_24_5728")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "拉旺塔尔赌吧\x01",
            "将于女王诞辰庆典举行的同时\x01",
            "重新向各位市民和游客开放！！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_5728 end

    SaveToFile()

Try(main)
