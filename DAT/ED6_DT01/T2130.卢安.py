from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2130   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2130.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2130   ._SN',
            'ED6_DT01/T2130_1 ._SN',
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
        '迪恩',                                 # 9
        '雷斯',                                 # 10
        '洛克',                                 # 11
        '巴克',                                 # 12
        '多姆斯',                               # 13
        '加布',                                 # 14
        '克拉姆',                               # 15
        '特蕾莎院长',                           # 16
        '阿加特',                               # 17
        '吉米',                                 # 18
        '照相机',                               # 19
        '迪奥德罗教区长',                       # 20
        '修女芙丽达',                           # 21
        '鲁特尔',                               # 22
        '兰达老人',                             # 23
        '米优',                                 # 24
        '西加罗',                               # 25
        '艾德尔',                               # 26
        '贝尔夫',                               # 27
        '布鲁托',                               # 28
        '巴克',                                 # 29
        '多姆斯',                               # 30
        '杰克',                                 # 31
        '皮卡罗',                               # 32
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
        'ED6_DT07/CH01390 ._CH',             # 00
        'ED6_DT07/CH02590 ._CH',             # 01
        'ED6_DT07/CH02570 ._CH',             # 02
        'ED6_DT07/CH00050 ._CH',             # 03
        'ED6_DT07/CH00370 ._CH',             # 04
        'ED6_DT07/CH00371 ._CH',             # 05
        'ED6_DT07/CH00373 ._CH',             # 06
        'ED6_DT07/CH00374 ._CH',             # 07
        'ED6_DT07/CH00100 ._CH',             # 08
        'ED6_DT07/CH00110 ._CH',             # 09
        'ED6_DT07/CH00140 ._CH',             # 0A
        'ED6_DT07/CH00101 ._CH',             # 0B
        'ED6_DT07/CH00111 ._CH',             # 0C
        'ED6_DT07/CH01040 ._CH',             # 0D
        'ED6_DT07/CH01670 ._CH',             # 0E
        'ED6_DT07/CH01410 ._CH',             # 0F
        'ED6_DT07/CH01023 ._CH',             # 10
        'ED6_DT07/CH01003 ._CH',             # 11
        'ED6_DT07/CH01053 ._CH',             # 12
        'ED6_DT07/CH01043 ._CH',             # 13
        'ED6_DT07/CH01213 ._CH',             # 14
        'ED6_DT07/CH02510 ._CH',             # 15
        'ED6_DT07/CH02520 ._CH',             # 16
        'ED6_DT07/CH02530 ._CH',             # 17
        'ED6_DT07/CH00450 ._CH',             # 18
        'ED6_DT07/CH00451 ._CH',             # 19
        'ED6_DT07/CH00453 ._CH',             # 1A
        'ED6_DT07/CH00454 ._CH',             # 1B
        'ED6_DT07/CH00460 ._CH',             # 1C
        'ED6_DT07/CH00461 ._CH',             # 1D
        'ED6_DT07/CH00463 ._CH',             # 1E
        'ED6_DT07/CH00464 ._CH',             # 1F
        'ED6_DT07/CH00470 ._CH',             # 20
        'ED6_DT07/CH00471 ._CH',             # 21
        'ED6_DT07/CH00473 ._CH',             # 22
        'ED6_DT07/CH00474 ._CH',             # 23
        'ED6_DT06/CH20058 ._CH',             # 24
        'ED6_DT07/CH00051 ._CH',             # 25
        'ED6_DT07/CH01393 ._CH',             # 26
    )

    AddCharChipPat(
        'ED6_DT07/CH01390P._CP',             # 00
        'ED6_DT07/CH02590P._CP',             # 01
        'ED6_DT07/CH02570P._CP',             # 02
        'ED6_DT07/CH00050P._CP',             # 03
        'ED6_DT07/CH00370P._CP',             # 04
        'ED6_DT07/CH00371P._CP',             # 05
        'ED6_DT07/CH00373P._CP',             # 06
        'ED6_DT07/CH00374P._CP',             # 07
        'ED6_DT07/CH00100P._CP',             # 08
        'ED6_DT07/CH00110P._CP',             # 09
        'ED6_DT07/CH00140P._CP',             # 0A
        'ED6_DT07/CH00101P._CP',             # 0B
        'ED6_DT07/CH00111P._CP',             # 0C
        'ED6_DT07/CH01040P._CP',             # 0D
        'ED6_DT07/CH01670P._CP',             # 0E
        'ED6_DT07/CH01410P._CP',             # 0F
        'ED6_DT07/CH01023P._CP',             # 10
        'ED6_DT07/CH01003P._CP',             # 11
        'ED6_DT07/CH01053P._CP',             # 12
        'ED6_DT07/CH01043P._CP',             # 13
        'ED6_DT07/CH01213P._CP',             # 14
        'ED6_DT07/CH02510P._CP',             # 15
        'ED6_DT07/CH02520P._CP',             # 16
        'ED6_DT07/CH02530P._CP',             # 17
        'ED6_DT07/CH00450P._CP',             # 18
        'ED6_DT07/CH00451P._CP',             # 19
        'ED6_DT07/CH00453P._CP',             # 1A
        'ED6_DT07/CH00454P._CP',             # 1B
        'ED6_DT07/CH00460P._CP',             # 1C
        'ED6_DT07/CH00461P._CP',             # 1D
        'ED6_DT07/CH00463P._CP',             # 1E
        'ED6_DT07/CH00464P._CP',             # 1F
        'ED6_DT07/CH00470P._CP',             # 20
        'ED6_DT07/CH00471P._CP',             # 21
        'ED6_DT07/CH00473P._CP',             # 22
        'ED6_DT07/CH00474P._CP',             # 23
        'ED6_DT06/CH20058P._CP',             # 24
        'ED6_DT07/CH00051P._CP',             # 25
        'ED6_DT07/CH01393P._CP',             # 26
    )

    DeclNpc(
        X                   = -4150,
        Z                   = 0,
        Y                   = 9070,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -4950,
        Z                   = 0,
        Y                   = 4460,
        Direction           = 120,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -2970,
        Z                   = 0,
        Y                   = 7390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -11930,
        Z                   = 0,
        Y                   = 4280,
        Direction           = 90,
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
        X                   = -11460,
        Z                   = 0,
        Y                   = 1930,
        Direction           = 90,
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
        X                   = -10100,
        Z                   = 0,
        Y                   = 2930,
        Direction           = 90,
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
        X                   = -6030,
        Z                   = 0,
        Y                   = 4040,
        Direction           = 270,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 33500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 33500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 53000,
        Z                   = 0,
        Y                   = 48100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 53000,
        Z                   = 0,
        Y                   = 33500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 58900,
        Z                   = 1000,
        Y                   = 52200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 54400,
        Z                   = 0,
        Y                   = 50000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 56580,
        Z                   = 0,
        Y                   = 42980,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 55130,
        Z                   = 0,
        Y                   = 45990,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 56110,
        Z                   = 0,
        Y                   = 45990,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 61600,
        Z                   = 0,
        Y                   = 45930,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 62560,
        Z                   = 0,
        Y                   = 45930,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -11800,
        Z                   = 250,
        Y                   = 4070,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -11600,
        Z                   = 250,
        Y                   = 1950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -10100,
        Z                   = 0,
        Y                   = 2930,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 350,
        Z                   = 0,
        Y                   = 1410,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -13330,
        Z                   = 600,
        Y                   = 6230,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -7720,
        Z                   = 0,
        Y                   = 10340,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )


    DeclActor(
        TriggerX            = 58980,
        TriggerZ            = 1000,
        TriggerY            = 50440,
        TriggerRange        = 400,
        ActorX              = 58900,
        ActorZ              = 2500,
        ActorY              = 52200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_506",          # 00, 0
        "Function_1_6DA",          # 01, 1
        "Function_2_705",          # 02, 2
        "Function_3_71B",          # 03, 3
        "Function_4_73F",          # 04, 4
        "Function_5_D5C",          # 05, 5
        "Function_6_10C8",         # 06, 6
        "Function_7_10E9",         # 07, 7
        "Function_8_110A",         # 08, 8
        "Function_9_1159",         # 09, 9
        "Function_10_11C3",        # 0A, 10
        "Function_11_1209",        # 0B, 11
        "Function_12_13C0",        # 0C, 12
        "Function_13_1569",        # 0D, 13
        "Function_14_1729",        # 0E, 14
        "Function_15_191A",        # 0F, 15
        "Function_16_1A8E",        # 10, 16
        "Function_17_1C60",        # 11, 17
        "Function_18_1E76",        # 12, 18
        "Function_19_1FE9",        # 13, 19
        "Function_20_214D",        # 14, 20
    )


    def Function_0_506(): pass

    label("Function_0_506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_521")
    SetChrPos(0x14, 62350, 0, 48350, 180)
    Jump("loc_67F")

    label("loc_521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_569")
    SetChrPos(0x14, 62350, 0, 48350, 180)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    Jump("loc_67F")

    label("loc_569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_584")
    SetChrPos(0x14, -17370, 0, 42870, 270)
    Jump("loc_67F")

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_59F")
    SetChrPos(0x14, 14600, 0, 44890, 270)
    Jump("loc_67F")

    label("loc_59F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_5E7")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrPos(0x14, 14600, 0, 44890, 270)
    Jump("loc_67F")

    label("loc_5E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_5F1")
    Jump("loc_67F")

    label("loc_5F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_614")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_67F")

    label("loc_614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_END)), "loc_61E")
    Jump("loc_67F")

    label("loc_61E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_67F")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8)

    label("loc_67F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A1")
    ClearChrFlags(0x11, 0x80)
    Jump("loc_6B7")

    label("loc_6A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B7")
    ClearChrFlags(0x11, 0x80)

    label("loc_6B7")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_6C3"),
        (SWITCH_DEFAULT, "loc_6D9"),
    )


    label("loc_6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D6")
    OP_A2(0x42C)
    Event(0, 20)

    label("loc_6D6")

    Jump("loc_6D9")

    label("loc_6D9")

    Return()

    # Function_0_506 end

    def Function_1_6DA(): pass

    label("Function_1_6DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6FB")
    OP_B1("t2130_y")
    Jump("loc_704")

    label("loc_6FB")

    OP_B1("t2130_n")

    label("loc_704")

    Return()

    # Function_1_6DA end

    def Function_2_705(): pass

    label("Function_2_705")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_71A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_705")

    label("loc_71A")

    Return()

    # Function_2_705 end

    def Function_3_71B(): pass

    label("Function_3_71B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_73E")
    OP_8D(0xFE, -8060, 7500, -1360, 2009, 1500)
    Jump("Function_3_71B")

    label("loc_73E")

    Return()

    # Function_3_71B end

    def Function_4_73F(): pass

    label("Function_4_73F")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_83F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DE")
    OP_A2(0x1)

    ChrTalk(
        0x13,
        (
            "市长被金钱蒙蔽了双眼，\x01",
            "做出了犯罪的行径。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "希望这片地区不要因此\x01",
            "陷入一片混乱才好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "空之女神啊……\x01",
            "请给予我们指引吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83C")

    label("loc_7DE")


    ChrTalk(
        0x13,
        (
            "市长被金钱蒙蔽了双眼，\x01",
            "做出了犯罪的行径。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "希望这片地区不要因此\x01",
            "陷入一片混乱才好……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83C")

    Jump("loc_D58")

    label("loc_83F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_881")

    ChrTalk(
        0x13,
        (
            "说起来，\x01",
            "这里的市长平时很忙，\x01",
            "很少来教会里看看呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D58")

    label("loc_881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_9A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93C")
    OP_A2(0x1)

    ChrTalk(
        0x13,
        "祈求所有人都能受到女神的祝福……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "……呼，一天终于结束了。\x01",
            "今天的观光客还是和往常一样多啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "可能市长会非常高兴吧，\x01",
            "不过他是不是忘了一件很重要的事情呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A3")

    label("loc_93C")


    ChrTalk(
        0x13,
        "今天的观光客还是和往常一样多啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "可能市长会非常高兴吧，\x01",
            "不过他是不是忘了一件很重要的事情呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A3")

    Jump("loc_D58")

    label("loc_9A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_AE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA3")
    OP_A2(0x1)

    ChrTalk(
        0x13,
        (
            "多亏了导力器，\x01",
            "很多事情做起来都变得很方便了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "不过自从飞艇被发明以来，\x01",
            "卢安的港口就变得非常冷清了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "七耀教会在如今的世界\x01",
            "也渐渐变成了一座被人们遗忘的雕像。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "我只希望卢安的市民至少不要\x01",
            "忘记对爱德丝女神的信仰……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADE")

    label("loc_AA3")


    ChrTalk(
        0x13,
        (
            "我只希望卢安的市民至少不要\x01",
            "忘记对爱德丝女神的信仰……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADE")

    Jump("loc_D58")

    label("loc_AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_BEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B7E")
    OP_A2(0x1)

    ChrTalk(
        0x13,
        (
            "如今来这里的人当中，\x01",
            "观光客人数要比本地居民多很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "其中也有没礼貌的家伙。\x01",
            "做弥撒的时候吵吵闹闹的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "让人头痛啊，真是的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE8")

    label("loc_B7E")


    ChrTalk(
        0x13,
        (
            "如今来这里的人当中，\x01",
            "观光客人数要比本地居民多很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "其中也有没礼貌的家伙。\x01",
            "让人头痛啊，真是的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE8")

    Jump("loc_D58")

    label("loc_BEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_C16")

    ChrTalk(
        0x13,
        (
            "呼，\x01",
            "早晨的弥撒好冷清啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D58")

    label("loc_C16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_C39")

    ChrTalk(
        0x13,
        (
            "各位，\x01",
            "请认真祈祷。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D58")

    label("loc_C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_D58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE1")
    OP_A2(0x1)

    ChrTalk(
        0x13,
        (
            "很久以前，\x01",
            "这里曾是海盗的盘踞之地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "不过最近经由杂志\x01",
            "以『海之教会』之名宣传了之后，\x01",
            "竟然变成了一个观光胜地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "世事真是变化莫测啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_D58")

    label("loc_CE1")


    ChrTalk(
        0x13,
        (
            "很久以前，\x01",
            "这里曾是海盗的盘踞之地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "不过最近经由杂志\x01",
            "以『海之教会』之名宣传了之后，\x01",
            "完全变成了一个观光胜地。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D58")

    TalkEnd(0x13)
    Return()

    # Function_4_73F end

    def Function_5_D5C(): pass

    label("Function_5_D5C")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_E44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF7")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "把幼小的孩子也牵连进去了……\x01",
            "真是让人痛心的事件啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "教区长曾经\x01",
            "去孤儿院探望过\x01",
            "那些可怜的孩子们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "下次我也要一起去。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E41")

    label("loc_DF7")


    ChrTalk(
        0xFE,
        (
            "教区长曾经\x01",
            "去孤儿院探望过\x01",
            "那些可怜的孩子们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "下次我也要一起去。\x02",
    )

    CloseMessageWindow()

    label("loc_E41")

    Jump("loc_10C4")

    label("loc_E44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_EAE")

    ChrTalk(
        0xFE,
        (
            "在卢安居住的居民\x01",
            "大多数都很繁忙的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从这一点可以看出\x01",
            "城里总有一股积极向上的势头。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C4")

    label("loc_EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_EFB")

    ChrTalk(
        0xFE,
        "今天傍晚的弥撒也很壮观。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "教区长看起来\x01",
            "好像有一些疲惫……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C4")

    label("loc_EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_F49")

    ChrTalk(
        0xFE,
        (
            "我们的教区长\x01",
            "平时看起来挺普通的，\x01",
            "其实他比其他人都要虔诚得多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C4")

    label("loc_F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_F97")

    ChrTalk(
        0xFE,
        "呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "教区长好像不太喜欢\x01",
            "别人把这个教会\x01",
            "当作观光胜地。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C4")

    label("loc_F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_FE0")

    ChrTalk(
        0xFE,
        "早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在正要开始早晨的弥撒。\x01",
            "一起来唱诵赞歌吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C4")

    label("loc_FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_104C")

    ChrTalk(
        0xFE,
        "现在正在举行傍晚的弥撒。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个时间有许多观光客\x01",
            "为了看夕阳照射下的彩色玻璃\x01",
            "而聚集到这里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C4")

    label("loc_104C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_10C4")

    ChrTalk(
        0xFE,
        (
            "这里一到傍晚，\x01",
            "海面上的夕阳照射在彩色玻璃上，\x01",
            "看起来非常漂亮。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "建筑物也非常漂亮，\x01",
            "特别受到女性的欢迎。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C4")

    TalkEnd(0x14)
    Return()

    # Function_5_D5C end

    def Function_6_10C8(): pass

    label("Function_6_10C8")

    TalkBegin(0x15)

    ChrTalk(
        0xFE,
        "哈哈，这个真漂亮……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x15)
    Return()

    # Function_6_10C8 end

    def Function_7_10E9(): pass

    label("Function_7_10E9")

    TalkBegin(0x16)

    ChrTalk(
        0xFE,
        "哦哦，这真是壮观啊！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x16)
    Return()

    # Function_7_10E9 end

    def Function_8_110A(): pass

    label("Function_8_110A")

    TalkBegin(0x17)

    ChrTalk(
        0xFE,
        (
            "哇～！\x01",
            "爷爷，快看快看！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好漂亮啊……\x01",
            "和观光导游书上说的一样。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x17)
    Return()

    # Function_8_110A end

    def Function_9_1159(): pass

    label("Function_9_1159")

    TalkBegin(0x18)

    ChrTalk(
        0xFE,
        "巡礼也平安无事地结束了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从出来旅游之后，\x01",
            "这还是我第一次和妻子就想去的地方达成一致。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x18)
    Return()

    # Function_9_1159 end

    def Function_10_11C3(): pass

    label("Function_10_11C3")

    TalkBegin(0x19)

    ChrTalk(
        0xFE,
        (
            "反射在水面上的夕阳\x01",
            "透过彩色玻璃照射进来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好漂亮……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x19)
    Return()

    # Function_10_11C3 end

    def Function_11_1209(): pass

    label("Function_11_1209")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_127E")

    ChrTalk(
        0xFE,
        (
            "我们好像被市长操纵，\x01",
            "做了许多十分霸道的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "偏偏被那个市长耍得团团转……\x01",
            "……我们真没面子呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13BC")

    label("loc_127E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_12ED")

    ChrTalk(
        0xFE,
        (
            "阿加特大哥，\x01",
            "不知道为什么突然紧急回到卢安了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没办法啊……\x01",
            "大哥在卢安的时候\x01",
            "我就老实点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13BC")

    label("loc_12ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1353")

    ChrTalk(
        0xFE,
        (
            "疼疼疼……\x01",
            "还是那么可怕的力量啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "阿加特大哥，\x01",
            "不知道为什么突然紧急回到卢安了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13BC")

    label("loc_1353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_138C")

    ChrTalk(
        0xFE,
        (
            "哼，\x01",
            "昨天我好像喝过头了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "头好晕啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_13BC")

    label("loc_138C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_13BC")

    ChrTalk(
        0xFE,
        (
            "干、干什么呀，\x01",
            "你们竟然会到这里来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13BC")

    TalkEnd(0x8)
    Return()

    # Function_11_1209 end

    def Function_12_13C0(): pass

    label("Function_12_13C0")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_143F")

    ChrTalk(
        0xFE,
        (
            "哼，\x01",
            "为什么非得生我的气不可啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天我还被军队里的\x01",
            "那个大姐狠狠地教训了一顿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我还真是命犯桃花啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1565")

    label("loc_143F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_14D2")

    ChrTalk(
        0xFE,
        (
            "好痛痛痛痛，可恶，\x01",
            "也不用这么用力打我吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个人成为游击士之后\x01",
            "是不是就越来越有蛮力了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样的话，\x01",
            "我还是暂时老实点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1565")

    label("loc_14D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_14FF")

    ChrTalk(
        0xFE,
        (
            "不行了，\x01",
            "还是敌不过那个人……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1565")

    label("loc_14FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1540")

    ChrTalk(
        0x9,
        (
            "啊～哈哈哈！\x01",
            "我喝不下了！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "啊～嗝……嗯……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1565")

    label("loc_1540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_1565")

    ChrTalk(
        0xFE,
        "……什么呀，不要看着我。\x02",
    )

    CloseMessageWindow()

    label("loc_1565")

    TalkEnd(0x9)
    Return()

    # Function_12_13C0 end

    def Function_13_1569(): pass

    label("Function_13_1569")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1607")

    ChrTalk(
        0xFE,
        (
            "我醒来的时候\x01",
            "已经被抓到军队的飞艇上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "穿蓝白相间军装的大姐\x01",
            "把我们所犯下的罪行\x01",
            "一条一条地陈列了出来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_1725")

    label("loc_1607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1679")

    ChrTalk(
        0xFE,
        (
            "啊哇哇，\x01",
            "没、没想到那个人竟然回来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……我还以为会被杀了呢。\x01",
            "他还是那样有惊人的威慑力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1725")

    label("loc_1679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_16C6")

    ChrTalk(
        0xFE,
        (
            "啊哇哇，\x01",
            "没、没想到那个人竟然回来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "从来没听说过啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1725")

    label("loc_16C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_16F3")

    ChrTalk(
        0xFE,
        (
            "怎么了，\x01",
            "想和我们比试比试吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1725")

    label("loc_16F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_1725")

    ChrTalk(
        0xFE,
        (
            "哼，各位游击士大人\x01",
            "来这里有何贵干呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1725")

    TalkEnd(0xA)
    Return()

    # Function_13_1569 end

    def Function_14_1729(): pass

    label("Function_14_1729")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1777")

    ChrTalk(
        0xFE,
        "疼呀………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个伤口看来是\x01",
            "阿加特大哥的剑留下的…………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1916")

    label("loc_1777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_17F7")

    ChrTalk(
        0xFE,
        (
            "虽然我以前听说过他，\x01",
            "但没有想到那就是阿加特大哥……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "果然是像迅雷一样的人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "迪恩他们\x01",
            "都变得唯唯诺诺了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1916")

    label("loc_17F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_183A")

    ChrTalk(
        0xFE,
        (
            "虽然我以前听说过他，\x01",
            "但没有想到那就是阿加特大哥……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1916")

    label("loc_183A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_18D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18B7")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        "我好想回家啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啰嗦的老爸老妈\x01",
            "是不是在家里等着我呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不……\x01",
            "已经不会有什么人在等我了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D1")

    label("loc_18B7")


    ChrTalk(
        0xFE,
        "呆在这里是最开心的。\x02",
    )

    CloseMessageWindow()

    label("loc_18D1")

    Jump("loc_1916")

    label("loc_18D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_1916")

    ChrTalk(
        0xFE,
        (
            "对于那些贪赃枉法的大人们所考虑的事情，\x01",
            "我已经厌烦了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1916")

    TalkEnd(0x1A)
    Return()

    # Function_14_1729 end

    def Function_15_191A(): pass

    label("Function_15_191A")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_196E")

    ChrTalk(
        0xFE,
        (
            "基尔巴特和我们\x01",
            "被带上了不同的飞艇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那家伙被带到哪里去了呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A8A")

    label("loc_196E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1A15")

    ChrTalk(
        0xFE,
        (
            "他还是和以前\x01",
            "一样的可怕啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "阿加特大哥\x01",
            "以前就对我们很严厉，\x01",
            "我和迪恩他们都非常尊敬他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "渡鸦帮变成现在这样，\x01",
            "是阿加特大哥\x01",
            "走了之后的事情了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8A")

    label("loc_1A15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1A42")

    ChrTalk(
        0xFE,
        (
            "他还是和以前\x01",
            "一样的可怕啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8A")

    label("loc_1A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1A6B")

    ChrTalk(
        0xFE,
        (
            "喂，\x01",
            "有什么好玩的事情吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8A")

    label("loc_1A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_1A8A")

    ChrTalk(
        0xFE,
        "……嗯～好无聊啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1A8A")

    TalkEnd(0x1B)
    Return()

    # Function_15_191A end

    def Function_16_1A8E(): pass

    label("Function_16_1A8E")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1B10")

    ChrTalk(
        0xFE,
        (
            "雷斯向军队里\x01",
            "那个短发的大姐挑战。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但没一会儿工夫\x01",
            "那家伙就被打败回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近的好多女人\x01",
            "都又强又可爱㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5C")

    label("loc_1B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1B6E")

    ChrTalk(
        0xFE,
        (
            "巧克力香烟吃吗？\x01",
            "我很喜欢这个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我也坏，\x01",
            "但是我敌不过阿加特大哥啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5C")

    label("loc_1B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1BA1")

    ChrTalk(
        0xFE,
        (
            "虽然我也坏，\x01",
            "但是我不过那个人啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5C")

    label("loc_1BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1C0E")

    ChrTalk(
        0xFE,
        (
            "昨天虽然有点害怕，\x01",
            "但是从渔船那里\x01",
            "抢来了一条沙丁鱼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿嘿，别看我这样，\x01",
            "其实我也很坏吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5C")

    label("loc_1C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_1C5C")

    ChrTalk(
        0xFE,
        (
            "今天在路边捡到的１米拉，\x01",
            "老子占为己有了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嘿嘿，我很邪恶吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1C5C")

    TalkEnd(0x1C)
    Return()

    # Function_16_1A8E end

    def Function_17_1C60(): pass

    label("Function_17_1C60")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1CCD")

    ChrTalk(
        0xFE,
        (
            "我只记得基尔巴特那家伙\x01",
            "来这里时的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对于我们所犯的罪行，\x01",
            "真的是一点也不记得了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E72")

    label("loc_1CCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1D5C")

    ChrTalk(
        0xFE,
        (
            "要是我知道\x01",
            "阿加特大哥会回来，\x01",
            "早就从仓库逃走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "他真是引人注目啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "头发的颜色和那把大剑，\x01",
            "站在城里马上就会被认出来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E72")

    label("loc_1D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1DC0")

    ChrTalk(
        0xFE,
        (
            "要是我知道\x01",
            "阿加特大哥会回来，\x01",
            "早就从仓库逃走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "做人就是要像他那样顶天立地啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E72")

    label("loc_1DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1E1B")

    ChrTalk(
        0xFE,
        (
            "因为没什么事情可以做，\x01",
            "所以就都聚集到这里来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我们真是在浪费青春啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E72")

    label("loc_1E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_1E72")

    ChrTalk(
        0xFE,
        (
            "我可不会干那些\x01",
            "惹祸上身的麻烦事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果发生什么事，\x01",
            "我马上就远走高飞。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E72")

    TalkEnd(0x1D)
    Return()

    # Function_17_1C60 end

    def Function_18_1E76(): pass

    label("Function_18_1E76")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1EA8")

    ChrTalk(
        0xFE,
        (
            "那个市长\x01",
            "比起我们来可坏得多了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FE5")

    label("loc_1EA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1EF9")

    ChrTalk(
        0xFE,
        (
            "那就是阿加特前辈吗。\x01",
            "真是吓我一跳啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那的确是他本人啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FE5")

    label("loc_1EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1F2F")

    ChrTalk(
        0xFE,
        "哇～他就是阿加特前辈啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真酷啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FE5")

    label("loc_1F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1F76")

    ChrTalk(
        0xFE,
        (
            "啊～啊，\x01",
            "哪里可以轻松地搞到钱啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "赌吧也关门了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FE5")

    label("loc_1F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_1FE5")

    ChrTalk(
        0xFE,
        "呼啊～啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我觉得工作\x01",
            "是一件很麻烦的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "被家人赶出来的确很迷惘，\x01",
            "不知不觉就到了这里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FE5")

    TalkEnd(0x1E)
    Return()

    # Function_18_1E76 end

    def Function_19_1FE9(): pass

    label("Function_19_1FE9")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2041")

    ChrTalk(
        0xFE,
        "……（发抖）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是这次的事被阿加特大哥知道的话，\x01",
            "肯定又要挨揍了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2149")

    label("loc_2041")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2084")

    ChrTalk(
        0xFE,
        "……（发抖）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我一点也没有想到\x01",
            "阿加特大哥会来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2149")

    label("loc_2084")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_20BF")

    ChrTalk(
        0xFE,
        "……（发抖）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "太可怕了，\x01",
            "我都站不稳了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2149")

    label("loc_20BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_20F6")

    ChrTalk(
        0xFE,
        (
            "唉，我一说要离开渡鸦帮，\x01",
            "他们就发怒了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2149")

    label("loc_20F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_2149")

    ChrTalk(
        0xFE,
        (
            "唉～\x01",
            "我可不是自己想呆在这里的。\x02\x03",
            "我是被大家硬拉过来的，\x01",
            "无法拒绝啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2149")

    TalkEnd(0x1F)
    Return()

    # Function_19_1FE9 end

    def Function_20_214D(): pass

    label("Function_20_214D")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    RemoveParty(0x35, 0xFF)
    AddParty(0x4, 0xFF)
    OP_31(0x4, 0x0, 0x11)
    OP_B5(0x4, 0x0)
    OP_B5(0x4, 0x5)
    OP_B5(0x4, 0x4)
    OP_B5(0x4, 0x3)
    OP_B5(0x4, 0x2)
    OP_B5(0x4, 0x1)
    OP_41(0x4, 0x79)
    OP_41(0x4, 0xF4)
    OP_41(0x4, 0x112)
    OP_41(0x4, 0x259, 0x0)
    OP_41(0x4, 0x262, 0x5)
    OP_41(0x4, 0x2C8, 0x4)
    OP_41(0x4, 0x265, 0x3)
    OP_41(0x4, 0x25B, 0x2)
    OP_41(0x4, 0x2D4, 0x1)
    OP_35(0x4, 0xBE)
    OP_36(0x4, 0xFA)
    FadeToDark(0, 0, -1)
    OP_20(0x9C4)
    OP_21()
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1D(0x56)
    SetChrPos(0x8, -10880, 0, 6920, 135)
    SetChrPos(0x9, -9460, 0, 7150, 270)
    SetChrPos(0xA, -10770, 0, 5350, 0)
    SetChrPos(0xB, -11290, 0, 4290, 90)
    SetChrPos(0xC, -10500, 0, 1550, 90)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)

    def lambda_2264():

        label("loc_2264")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_2264")

    QueueWorkItem2(0x8, 1, lambda_2264)

    def lambda_2275():

        label("loc_2275")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_2275")

    QueueWorkItem2(0x9, 1, lambda_2275)

    def lambda_2286():

        label("loc_2286")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_2286")

    QueueWorkItem2(0xA, 1, lambda_2286)

    def lambda_2297():

        label("loc_2297")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_2297")

    QueueWorkItem2(0xB, 1, lambda_2297)

    def lambda_22A8():

        label("loc_22A8")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_22A8")

    QueueWorkItem2(0xC, 1, lambda_22A8)

    def lambda_22B9():

        label("loc_22B9")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_22B9")

    QueueWorkItem2(0xD, 1, lambda_22B9)
    OP_6D(-9740, 0, 5080, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "#776F……别装蒜了！\x01",
            "是你们干的好事吧！？\x02\x03",
            "我饶不了你们！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "你这小鬼在说什么呀？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "喂喂，这里可不是\x01",
            "你这种小鬼头能来的地方哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "快点滚回家去，\x01",
            "乖乖地喝妈妈的奶吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "哈哈哈，说得对、说得对！\x02",
    )

    CloseMessageWindow()
    OP_92(0xE, 0x9, 0xED8, 0x7D0, 0x0)

    ChrTalk(
        0xE,
        "#776F呜呜呜呜呜……\x02",
    )

    OP_94(0x1, 0xE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x10E, 0x64, 0xBB8, 0x0)
    CloseMessageWindow()
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0xE,
        "#778F#3S哇啊啊啊啊啊啊啊啊……！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)

    def lambda_24AA():
        OP_6D(-12160, 0, 5450, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24AA)
    OP_94(0x1, 0xE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x10E, 0x64, 0xBB8, 0x0)
    CloseMessageWindow()
    OP_92(0xE, 0x9, 0x1F4, 0x1770, 0x0)

    def lambda_2585():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2585)
    OP_22(0x7D, 0x0, 0x64)
    OP_94(0x1, 0x9, 0xB4, 0x320, 0x1770, 0x0)
    Sleep(200)
    OP_92(0xE, 0xA, 0x320, 0x1770, 0x0)

    def lambda_25C2():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_25C2)
    OP_22(0x7D, 0x0, 0x64)
    OP_94(0x1, 0xA, 0xB4, 0x258, 0x1770, 0x0)

    ChrTalk(
        0x8,
        "搞、搞什么……？\x02",
    )

    OP_92(0xE, 0xA, 0x258, 0x1770, 0x0)

    def lambda_260F():
        OP_94(0x1, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_260F)
    OP_22(0x7D, 0x0, 0x64)
    OP_94(0x1, 0xA, 0xB4, 0x12C, 0x1770, 0x0)
    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这小鬼……\x01",
            "发什么癫呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#778F#2P别以为我没有妈妈\x01",
            "就随意看不起人家！\x02\x03",
            "#2P老师就是我的妈妈！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0xE, 0xA, 0x258, 0x1770, 0x0)

    def lambda_26B0():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_26B0)
    OP_22(0x7D, 0x0, 0x64)
    OP_94(0x1, 0xA, 0xB4, 0x12C, 0x1770, 0x0)

    ChrTalk(
        0xE,
        (
            "#776F#2P你们竟然把老师宝贵的家给……\x01",
            "竟然、竟然、竟然把……！\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0xE, 0xA, 0x258, 0x1770, 0x0)

    def lambda_272B():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_272B)
    OP_22(0x7D, 0x0, 0x64)
    OP_94(0x1, 0xA, 0xB4, 0x12C, 0x1770, 0x0)

    ChrTalk(
        0xA,
        "嘁……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xE, 0x40)
    OP_94(0x1, 0xE, 0xB4, 0x3E8, 0xBB8, 0x0)
    OP_92(0xE, 0xA, 0x320, 0x1770, 0x0)

    def lambda_2788():
        OP_94(0x0, 0xFE, 0x0, 0x12C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2788)
    OP_92(0xE, 0xA, 0x1F4, 0x1770, 0x0)
    OP_22(0x209, 0x0, 0x64)
    OP_96(0xE, 0xFFFFD594, 0x0, 0x145A, 0x1F4, 0x1388)
    OP_96(0xE, 0xFFFFD88C, 0x0, 0x1450, 0xC8, 0x1388)

    ChrTalk(
        0xE,
        "#778F#4P哇啊……\x02",
    )

    CloseMessageWindow()
    OP_92(0x8, 0xE, 0x2BC, 0x7D0, 0x0)
    OP_63(0xE)
    TurnDirection(0xE, 0x8, 400)
    Sleep(500)

    def lambda_2812():
        OP_94(0x1, 0xFE, 0x10E, 0xC8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2812)
    SetChrFlags(0xE, 0x4)
    ClearChrFlags(0xE, 0x400)
    OP_44(0x8, 0xFF)

    def lambda_2836():
        OP_99(0xFE, 0x0, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2836)

    def lambda_2846():
        OP_94(0x1, 0xFE, 0x0, 0x64, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2846)
    OP_94(0x1, 0xE, 0xB4, 0x64, 0x3E8, 0x0)
    OP_94(0x1, 0xE, 0x0, 0x64, 0x3E8, 0x0)

    def lambda_287A():
        OP_91(0xFE, 0x0, 0x190, 0x0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_287A)
    OP_9E(0xE, 0xF, 0x0, 0x12C, 0xBB8)

    ChrTalk(
        0x8,
        (
            "#2P我们懒得理你，\x01",
            "你这小鬼头就得意起来了啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0xA, 0xE, 0x3E8, 0x7D0, 0x0)

    ChrTalk(
        0xA,
        (
            "看来不给你\x01",
            "尝尝苦头也不行了。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x9, 0xE, 0x5DC, 0x7D0, 0x0)

    ChrTalk(
        0x9,
        (
            "不如就打一百下屁股吧？\x01",
            "哇～哈、哈、哈！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, -1130, 0, 4490, 0)
    SetChrPos(0x105, -1130, 0, 4490, 0)
    SetChrPos(0x102, -1130, 0, 4490, 0)

    ChrTalk(
        0x105,
        "#1P请你们住手！\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2A29():

        label("loc_2A29")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_2A29")

    QueueWorkItem2(0x9, 1, lambda_2A29)

    def lambda_2A3A():

        label("loc_2A3A")

        TurnDirection(0xFE, 0x105, 0)
        OP_48()
        Jump("loc_2A3A")

    QueueWorkItem2(0xA, 1, lambda_2A3A)

    def lambda_2A4B():

        label("loc_2A4B")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2A4B")

    QueueWorkItem2(0xB, 1, lambda_2A4B)

    def lambda_2A5C():

        label("loc_2A5C")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2A5C")

    QueueWorkItem2(0xC, 1, lambda_2A5C)

    def lambda_2A6D():

        label("loc_2A6D")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2A6D")

    QueueWorkItem2(0xD, 1, lambda_2A6D)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x101, 11)
    SetChrChipByIndex(0x102, 12)

    def lambda_2A92():
        OP_6D(-10300, 0, 5530, 1000)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2A92)

    def lambda_2AAA():
        OP_8E(0xFE, 0xFFFFE2FA, 0x0, 0x1338, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2AAA)
    Sleep(500)

    def lambda_2ACA():
        OP_8E(0xFE, 0xFFFFE606, 0x0, 0x16F8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2ACA)
    Sleep(300)

    def lambda_2AEA():
        OP_8E(0xFE, 0xFFFFE868, 0x0, 0xFC8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AEA)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x101, 8)
    SetChrSubChip(0x101, 6)
    WaitChrThread(0x102, 0x1)
    SetChrChipByIndex(0x102, 9)
    SetChrSubChip(0x102, 6)

    ChrTalk(
        0x8,
        "你、你们是……\x02",
    )

    CloseMessageWindow()
    OP_22(0x1FC, 0x0, 0x64)
    SetChrChipByIndex(0x9, 28)
    Sleep(100)
    SetChrChipByIndex(0xA, 32)
    Sleep(100)
    SetChrChipByIndex(0xB, 4)
    Sleep(100)
    SetChrChipByIndex(0xC, 4)
    Sleep(100)
    SetChrChipByIndex(0xD, 4)
    Sleep(100)
    SetChrFlags(0xE, 0x40)

    def lambda_2B73():
        OP_8C(0xFE, 270, 800)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2B73)
    OP_96(0xE, 0xFFFFD544, 0x0, 0x17E8, 0x1F4, 0x1388)
    ClearChrFlags(0xE, 0x20)
    SetChrFlags(0xE, 0x400)
    OP_96(0xE, 0xFFFFD1D4, 0x0, 0x19AA, 0xC8, 0x1388)
    ClearChrFlags(0xE, 0x4)
    SetChrChipByIndex(0x8, 24)
    OP_8C(0x8, 90, 400)

    ChrTalk(
        0xE,
        "#778F咳咳……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x105, 250)

    ChrTalk(
        0xE,
        "#775F科洛丝……姐姐？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0x1)

    ChrTalk(
        0x105,
        (
            "#049F竟然对一个\x01",
            "手无寸铁的小孩子使用暴力……\x02\x03",
            "太差劲了……\x01",
            "难道你们不觉得羞耻吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "你、你说什么～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "哟哟，小姑娘。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "本来觉得你那张小嘴蛮可爱的，\x01",
            "没想到还这么牙尖嘴利嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "就算有游击士在，\x01",
            "但跟这么多人动手，你以为自己能赢吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F科洛丝，你先退后！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F我们会争取时间。\x01",
            "你趁空隙把孩子救出去……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 90, 400)
    Sleep(200)

    ChrTalk(
        0x105,
        (
            "#042F#1P不……\x02\x03",
            "请让我也参加战斗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#047F#1P其实我本来\x01",
            "并不想用这个的……\x02\x03",
            "但是我曾经学过——\x01",
            "剑，应在保护他人之时才握于手中的。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x1F8, 0x0, 0x64)
    SetChrChipByIndex(0x105, 10)
    SetChrSubChip(0x105, 6)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x105,
        "#042F#1P现在，就是该出剑的时候了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F防身用的细剑？\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x105, 0x20)

    def lambda_2E66():
        OP_8C(0xFE, 270, 800)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2E66)
    WaitChrThread(0x105, 0x1)
    Sleep(500)
    ClearChrFlags(0x105, 0x20)

    ChrTalk(
        0x105,
        (
            "#046F请放了那孩子。\x02\x03",
            "否则……\x01",
            "我就只好强行救人了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "好、好酷呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "……真是惹人怜爱的小妹妹哦……\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x8,
        "#3S惹、惹人怜爱个屁！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "连这种小娘们儿都小看我们，\x01",
            "真是岂有此理！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "让他们好好尝尝\x01",
            "我们『渡鸦帮』的厉害！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#2P#1K喔！\x02",
    )


    ChrTalk(
        0xC,
        "#1P#1K喔！\x02",
    )


    ChrTalk(
        0xD,
        "#4P#1K喔！\x02",
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()
    SetChrChipByIndex(0x8, 25)
    SetChrChipByIndex(0x9, 29)
    SetChrChipByIndex(0xA, 33)
    SetChrChipByIndex(0xB, 5)
    SetChrChipByIndex(0xC, 5)
    SetChrChipByIndex(0xD, 5)

    def lambda_2FEA():
        OP_92(0xFE, 0x105, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2FEA)

    def lambda_2FFF():
        OP_92(0xFE, 0x102, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2FFF)

    def lambda_3014():
        OP_92(0xFE, 0x105, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3014)

    def lambda_3029():
        OP_92(0xFE, 0x101, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3029)

    def lambda_303E():
        OP_92(0xFE, 0x101, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_303E)

    def lambda_3053():
        OP_92(0xFE, 0x101, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3053)
    Sleep(300)
    Battle(0x397, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_3080"),
        (SWITCH_DEFAULT, "loc_3083"),
    )


    label("loc_3080")

    OP_B4(0x0)
    Return()

    label("loc_3083")

    EventBegin(0x0)
    SetChrPos(0xE, -11720, 0, 5630, 90)
    SetChrPos(0x105, -7070, 0, 5350, 270)
    SetChrPos(0x101, -6160, 0, 4019, 270)
    SetChrPos(0x102, -6120, 0, 5950, 270)
    SetChrChipByIndex(0x8, 24)
    SetChrChipByIndex(0x9, 28)
    SetChrChipByIndex(0xA, 32)
    SetChrChipByIndex(0xB, 7)
    SetChrChipByIndex(0xC, 7)
    SetChrChipByIndex(0xD, 7)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xB, -11300, 0, 10000, 135)
    SetChrPos(0xC, -14730, 0, 3670, 90)
    SetChrPos(0xD, -10480, 0, -290, 0)
    SetChrPos(0x8, -11270, 0, 6060, 90)
    SetChrPos(0x9, -9150, 0, 3860, 90)
    SetChrPos(0xA, -8760, 0, 7620, 90)
    TurnDirection(0x9, 0x105, 0)
    TurnDirection(0xA, 0x105, 0)
    OP_6D(-10660, 0, 5990, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x8,
        "这、这帮家伙是怪物吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "游击士也就算了，\x01",
            "连那个小丫头也不是泛泛之辈……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#774F好、好厉害啊姐姐！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F哇哦～！\x01",
            "科洛丝，你好厉害啊～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F如此超凡的剑法\x01",
            "应该也是师从名家的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#045F呵呵，我还差得远呢。\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x105, 65535)
    OP_0D()
    Sleep(500)
    OP_94(0x1, 0x105, 0x0, 0x3E8, 0x3E8, 0x0)

    ChrTalk(
        0x105,
        (
            "#043F那个，再战斗下去，\x01",
            "我想也已经没有意义了。\x02\x03",
            "求求你们……\x01",
            "请把那孩子放了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "这、这娘们儿……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "被、被你们耍成这样， \x01",
            "怎可能说句『哦，好』就了事啊！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x10, -990, 0, 1560, 315)
    SetChrPos(0xF, -2200, 0, 1380, 0)

    NpcTalk(
        0x10,
        "青年的声音",
        "#1P……给我到此为止吧。\x02",
    )

    CloseMessageWindow()

    def lambda_3417():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3417)

    def lambda_3425():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3425)

    def lambda_3433():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3433)

    def lambda_3441():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3441)

    def lambda_344F():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_344F)

    def lambda_345D():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_345D)

    ChrTalk(
        0x8,
        "是、是谁！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "新来的吗！？\x02",
    )

    CloseMessageWindow()

    def lambda_348F():

        label("loc_348F")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_348F")

    QueueWorkItem2(0x8, 1, lambda_348F)

    def lambda_34A0():

        label("loc_34A0")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_34A0")

    QueueWorkItem2(0x9, 1, lambda_34A0)

    def lambda_34B1():

        label("loc_34B1")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_34B1")

    QueueWorkItem2(0xA, 1, lambda_34B1)

    def lambda_34C2():

        label("loc_34C2")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_34C2")

    QueueWorkItem2(0x101, 1, lambda_34C2)

    def lambda_34D3():

        label("loc_34D3")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_34D3")

    QueueWorkItem2(0x102, 1, lambda_34D3)

    def lambda_34E4():

        label("loc_34E4")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_34E4")

    QueueWorkItem2(0x105, 1, lambda_34E4)

    def lambda_34F5():
        OP_6D(-9840, 0, 5810, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_34F5)
    ClearChrFlags(0x10, 0x80)
    OP_8E(0x10, 0xFFFFF042, 0x0, 0x114E, 0xBB8, 0x0)
    OP_8C(0x10, 270, 400)

    ChrTalk(
        0x10,
        (
            "#053F#1P哎呀哎呀，难得回来一趟，\x01",
            "居然连我的声音都不记得了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x8,
        "阿、阿加特大哥！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "你、你来了啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#050F#1P…………………………\x02",
    )

    CloseMessageWindow()

    def lambda_363E():
        OP_6D(-10660, 0, 5990, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_363E)

    def lambda_3656():
        OP_8E(0xFE, 0xFFFFDE36, 0x0, 0x14E6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3656)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    Sleep(600)
    OP_44(0x105, 0xFF)
    OP_8C(0x105, 45, 400)
    OP_90(0x105, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
    OP_8C(0x105, 180, 400)

    def lambda_36A6():

        label("loc_36A6")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_36A6")

    QueueWorkItem2(0x105, 1, lambda_36A6)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 270, 400)

    ChrTalk(
        0x101,
        (
            "#004F你、你怎么会……\x02\x03",
            "难道说，\x01",
            "你也认识这帮家伙！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#053F……雷斯……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "是、是，什么事？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x9, 400)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 36)
    SetChrSubChip(0x10, 0)
    OP_92(0x10, 0x9, 0x190, 0x1F40, 0x0)
    SetChrSubChip(0x10, 1)
    OP_22(0x1FB, 0x0, 0x64)

    def lambda_376D():
        OP_94(0x0, 0xFE, 0x0, 0x12C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_376D)
    SetChrChipByIndex(0x9, 30)
    SetChrFlags(0x9, 0x20)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_94(0x1, 0x9, 0xB4, 0x1F4, 0x1F40, 0x0)
    OP_22(0x209, 0x0, 0x64)

    def lambda_37AC():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_37AC)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 31)
    OP_99(0x9, 0x0, 0x3, 0x7D0)

    ChrTalk(
        0x9,
        "呜啊！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0)
    Sleep(80)
    SetChrChipByIndex(0x10, 3)
    ClearChrFlags(0x10, 0x20)
    Sleep(500)
    TurnDirection(0x10, 0xA, 400)
    OP_92(0x10, 0x9, 0xBB8, 0x1F40, 0x0)

    ChrTalk(
        0x10,
        (
            "#057F你们几个……都干了些什么？\x02\x03",
            "调戏妇女、虐待小孩……\x02\x03",
            "也太目无法纪了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "罗、啰嗦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "你这种已经离队的家伙\x01",
            "没有资格对我们指手画脚……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_38A5():
        OP_6D(-10660, 0, 7680, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_38A5)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x40)
    SetChrChipByIndex(0x10, 37)
    OP_92(0x10, 0xA, 0x3E8, 0x2710, 0x0)
    SetChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 36)
    SetChrSubChip(0x10, 0)
    OP_92(0x10, 0xA, 0x190, 0x2710, 0x0)
    SetChrSubChip(0x10, 1)
    OP_22(0x1FB, 0x0, 0x64)
    OP_22(0x209, 0x0, 0x64)

    def lambda_390B():
        OP_94(0x0, 0xFE, 0x0, 0x12C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_390B)
    SetChrChipByIndex(0xA, 34)
    SetChrFlags(0xA, 0x20)
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_94(0x1, 0xA, 0xB4, 0x1F4, 0x1F40, 0x0)

    def lambda_3945():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3945)
    WaitChrThread(0xA, 0x1)
    SetChrSubChip(0x10, 2)
    OP_8F(0xA, 0xFFFFDDAA, 0x7D0, 0x2CEC, 0x3A98, 0x0)
    PlayEffect(0x12, 0xFF, 0xA, 0, 0, -500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0xA,
        "呜哇！\x05\x02",
    )

    OP_22(0x8E, 0x0, 0x64)
    OP_6B(3070, 0)
    OP_6B(3000, 80)
    Sleep(500)
    OP_8F(0xA, 0xFFFFDDAA, 0x0, 0x2CEC, 0x7D0, 0x0)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0xA, 35)
    OP_99(0xA, 0x1, 0x3, 0x3E8)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x10, 0x20)
    Sleep(500)

    ChrTalk(
        0x10,
        "#050F……你刚刚说什么？\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x8,
        "大、大哥，饶了我们吧！\x02",
    )

    CloseMessageWindow()

    def lambda_3A5C():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3A5C)
    OP_44(0x8, 0xFF)
    SetChrChipByIndex(0x8, 21)
    OP_8E(0x8, 0xFFFFD1DE, 0x0, 0x18CE, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFFD01C, 0x0, 0x15E0, 0xBB8, 0x0)
    OP_8C(0x8, 90, 400)

    ChrTalk(
        0x8,
        "这小孩……你看，我这就放了他！\x02",
    )

    CloseMessageWindow()

    def lambda_3AC6():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3AC6)

    def lambda_3AD4():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AD4)

    def lambda_3AE2():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3AE2)

    ChrTalk(
        0xE,
        "#775F#1P科洛丝姐姐！\x02",
    )

    CloseMessageWindow()

    def lambda_3B0A():
        OP_6D(-9010, 0, 6820, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3B0A)

    def lambda_3B22():
        OP_8E(0xFE, 0xFFFFDD64, 0x0, 0x1496, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3B22)
    Sleep(300)
    OP_8E(0x105, 0xFFFFE03E, 0x0, 0x152C, 0x7D0, 0x0)
    OP_8C(0x105, 270, 400)

    ChrTalk(
        0x105,
        (
            "#048F太好了……\x01",
            "已经没事了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#053F哼，\x01",
            "早这么做不就得了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        (
            "#007F你还是那么粗暴啊……\x02\x03",
            "#009F还有，你为什么会在\x01",
            "这么恰到好处的时候出现？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0x10,
        (
            "#050F我只是听嘉恩那家伙说了。\x02\x03",
            "说洛连特来的两个小鬼\x01",
            "正在调查纵火事件什么的。\x02\x03",
            "#053F好了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xE, 400)
    Sleep(500)

    ChrTalk(
        0x10,
        "#050F#2P喂，小鬼头。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x10, 400)

    ChrTalk(
        0xE,
        "#775F什、什么事啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#051F#2P敢一个人闯进来，\x01",
            "还真是个有胆量的小子。\x02\x03",
            "不过这样有点太胡闹了吧。\x02\x03",
            "下次再让你妈妈操心的话，\x01",
            "可真的要打屁股哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#774F哎……？\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "女性的声音",
        "克拉姆……\x02",
    )

    CloseMessageWindow()

    def lambda_3D57():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3D57)

    def lambda_3D65():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D65)

    def lambda_3D73():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3D73)

    def lambda_3D81():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3D81)

    def lambda_3D8F():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3D8F)
    TurnDirection(0xE, 0xF, 400)
    Sleep(500)

    def lambda_3DA9():

        label("loc_3DA9")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_3DA9")

    QueueWorkItem2(0x101, 1, lambda_3DA9)

    def lambda_3DBA():

        label("loc_3DBA")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_3DBA")

    QueueWorkItem2(0x102, 1, lambda_3DBA)

    def lambda_3DCB():

        label("loc_3DCB")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_3DCB")

    QueueWorkItem2(0x105, 1, lambda_3DCB)
    ClearChrFlags(0xF, 0x80)

    def lambda_3DE1():
        OP_6D(-9140, 0, 5560, 1500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3DE1)
    OP_8E(0xF, 0xFFFFE642, 0x0, 0xAFA, 0x7D0, 0x0)
    TurnDirection(0xF, 0xE, 0)
    TurnDirection(0xE, 0xF, 0)

    ChrTalk(
        0xE,
        "#774F#1P老、老师！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#044F#2P您怎么来了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#754F我从协会得知你们来了这里，\x01",
            "然后我就拜托这位先生带我来的。\x02\x03",
            "#752F克拉姆，你这孩子真是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#772F#1P只、只有这次，\x01",
            "我是绝对不会道歉的！\x02\x03",
            "放火烧了我们房子的犯人\x01",
            "我绝对要亲手将他们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#755F#3S克拉姆！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(200)
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3F51():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x320, 0x1770)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_3F51)
    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F#2P特蕾莎老师……\x01",
            "不管怎样，请您不要责怪他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#754F不。\x01",
            "我不是要怪他。\x02\x03",
            "#757F克拉姆……\x01",
            "你的心情我很明白。\x02\x03",
            "那毕竟是大家一起生活过的地方。\x01",
            "对我们来说，那更加是无可替代的家园。\x02\x03",
            "但是呢……\x02\x03",
            "#756F就算你向犯人报复，\x01",
            "烧毁的家也不会再回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#775F#1P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#750F只要你们没事，\x01",
            "对老师来说就已经很满足了。\x02\x03",
            "这就是我唯一的希望……\x02\x03",
            "#758F所以呢，克拉姆……\x01",
            "你以后不要再做危险的事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#775F#1P老、老师……\x02\x03",
            "#777F……呜呜呜呜呜呜……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    ChrTalk(
        0xE,
        "#778F#1P#5S呜哇啊啊阿～～～！#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_92(0xE, 0xF, 0x258, 0x1388, 0x0)
    SetChrFlags(0xF, 0x20)
    OP_94(0x1, 0xF, 0xB4, 0x64, 0x5DC, 0x0)
    OP_94(0x1, 0xF, 0x0, 0x64, 0x5DC, 0x0)
    ClearChrFlags(0xF, 0x20)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#003F#2P呜……\x01",
            "这种场面真是太让人感动了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#049F#1P是啊……\x02\x03",
            "#049F能平安无事真是太好了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    def lambda_4240():
        OP_6D(-9840, 0, 6260, 1000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4240)
    WaitChrThread(0xC, 0x1)

    ChrTalk(
        0x10,
        (
            "#551F真是的……\x01",
            "所以就说女人和小孩麻烦嘛。\x02\x03",
            "#552F喂，黑发的小子。\x02\x03",
            "带着院长她们\x01",
            "快点离开这地方吧。\x02\x03",
            "我可不会应付这种场面。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    OP_8C(0x102, 270, 400)

    ChrTalk(
        0x102,
        (
            "#014F没问题，可是……\x01",
            "阿加特兄打算做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#057F这还用说……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x8, 400)

    def lambda_4338():
        OP_6D(-10420, 0, 6530, 1500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4338)
    OP_8E(0x10, 0xFFFFD58A, 0x0, 0x15E0, 0xBB8, 0x0)
    OP_8C(0x8, 90, 0)
    TurnDirection(0x10, 0x8, 400)

    ChrTalk(
        0x10,
        (
            "#054F#2P我要好好问个清楚，\x01",
            "看看这帮蠢货到底是不是犯人。\x02\x03",
            "给我洗好脖子等着吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_9E(0x8, 0x32, 0x0, 0x12C, 0x1770)
    Sleep(500)
    OP_44(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "哎～？\x01",
            "饶、饶了我们吧～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此……\x02\x03",
            "#019F既然这样的话，\x01",
            "那我们还是不打扰你们了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_28(0x3C, 0x1, 0x20)
    OP_A2(0x3FE)
    NewScene("ED6_DT01/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_214D end

    SaveToFile()

Try(main)
