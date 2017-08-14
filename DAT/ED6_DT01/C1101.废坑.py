from ED6ScenarioHelper import *

def main():
    # 废坑

    CreateScenaFile(
        FileName            = 'C1101   ._SN',
        MapName             = 'Bose',
        Location            = 'C1101.x',
        MapIndex            = 49,
        MapDefaultBGM       = "ed60030",
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
        '吉尔',                                 # 9
        '空贼',                                 # 10
        '空贼',                                 # 11
        '空贼',                                 # 12
        '空贼',                                 # 13
        '空贼艇',                               # 14
        '空贼艇（影）',                         # 15
        '摩尔根将军',                           # 16
        '王国军军官',                           # 17
        '王国军士兵',                           # 18
        '王国军士兵',                           # 19
        '王国军士兵',                           # 20
        '王国军士兵',                           # 21
        '王国军士兵',                           # 22
        '王国军士兵',                           # 23
        '王国军士兵',                           # 24
        '王国军士兵',                           # 25
        '王国军士兵',                           # 26
        '王国军士兵',                           # 27
        '王国军士兵',                           # 28
        '王国军士兵',                           # 29
        '王国军士兵',                           # 30
        '王国军士兵',                           # 31
        '王国军士兵',                           # 32
        '王国军士兵',                           # 33
        '王国军士兵',                           # 34
        '王国军士兵',                           # 35
        ' ',                                    # 36
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
        Unknown_3A              = 49,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02120 ._CH',             # 00
        'ED6_DT07/CH00300 ._CH',             # 01
        'ED6_DT07/CH00304 ._CH',             # 02
        'ED6_DT07/CH00305 ._CH',             # 03
        'ED6_DT07/CH00306 ._CH',             # 04
        'ED6_DT07/CH01380 ._CH',             # 05
        'ED6_DT07/CH00360 ._CH',             # 06
        'ED6_DT07/CH00364 ._CH',             # 07
        'ED6_DT07/CH00100 ._CH',             # 08
        'ED6_DT07/CH00101 ._CH',             # 09
        'ED6_DT07/CH00110 ._CH',             # 0A
        'ED6_DT07/CH00111 ._CH',             # 0B
        'ED6_DT07/CH00120 ._CH',             # 0C
        'ED6_DT07/CH00121 ._CH',             # 0D
        'ED6_DT07/CH00122 ._CH',             # 0E
        'ED6_DT07/CH00301 ._CH',             # 0F
        'ED6_DT07/CH02080 ._CH',             # 10
        'ED6_DT07/CH01650 ._CH',             # 11
        'ED6_DT07/CH01600 ._CH',             # 12
        'ED6_DT07/CH00361 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH02120P._CP',             # 00
        'ED6_DT07/CH00300P._CP',             # 01
        'ED6_DT07/CH00304P._CP',             # 02
        'ED6_DT07/CH00305P._CP',             # 03
        'ED6_DT07/CH00306P._CP',             # 04
        'ED6_DT07/CH01380P._CP',             # 05
        'ED6_DT07/CH00360P._CP',             # 06
        'ED6_DT07/CH00364P._CP',             # 07
        'ED6_DT07/CH00100P._CP',             # 08
        'ED6_DT07/CH00101P._CP',             # 09
        'ED6_DT07/CH00110P._CP',             # 0A
        'ED6_DT07/CH00111P._CP',             # 0B
        'ED6_DT07/CH00120P._CP',             # 0C
        'ED6_DT07/CH00121P._CP',             # 0D
        'ED6_DT07/CH00122P._CP',             # 0E
        'ED6_DT07/CH00301P._CP',             # 0F
        'ED6_DT07/CH02080P._CP',             # 10
        'ED6_DT07/CH01650P._CP',             # 11
        'ED6_DT07/CH01600P._CP',             # 12
        'ED6_DT07/CH00361P._CP',             # 13
    )

    DeclNpc(
        X                   = -1550,
        Z                   = 0,
        Y                   = 400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -31320,
        Y                   = -1000,
        Z                   = -13400,
        Range               = -30300,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFFFFBF28,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = 9230,
        Y                   = -1000,
        Z                   = 28440,
        Range               = 6690,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x6B6C,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )


    ScpFunction(
        "Function_0_50A",          # 00, 0
        "Function_1_56D",          # 01, 1
        "Function_2_5A8",          # 02, 2
        "Function_3_5BE",          # 03, 3
        "Function_4_5D4",          # 04, 4
        "Function_5_1F8C",         # 05, 5
        "Function_6_21B9",         # 06, 6
        "Function_7_23E6",         # 07, 7
        "Function_8_246C",         # 08, 8
        "Function_9_340E",         # 09, 9
        "Function_10_3EF1",        # 0A, 10
        "Function_11_3FCE",        # 0B, 11
        "Function_12_40AB",        # 0C, 12
        "Function_13_4188",        # 0D, 13
    )


    def Function_0_50A(): pass

    label("Function_0_50A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_526"),
        (108, "loc_538"),
        (109, "loc_54E"),
        (110, "loc_54E"),
        (111, "loc_54E"),
        (SWITCH_DEFAULT, "loc_56C"),
    )


    label("loc_526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_535")
    OP_A2(0x320)
    Event(0, 4)

    label("loc_535")

    Jump("loc_56C")

    label("loc_538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54B")
    OP_A2(0x329)
    Event(0, 9)

    label("loc_54B")

    Jump("loc_56C")

    label("loc_54E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_569")
    OP_A2(0x328)
    Event(0, 8)

    label("loc_569")

    Jump("loc_56C")

    label("loc_56C")

    Return()

    # Function_0_50A end

    def Function_1_56D(): pass

    label("Function_1_56D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_592")
    OP_1B(0x0, 0x0, 0xA)
    OP_1B(0x1, 0x0, 0xB)
    OP_1B(0x2, 0x0, 0xC)
    OP_1B(0x3, 0x0, 0xC)
    OP_1B(0x5, 0x0, 0xD)

    label("loc_592")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x387), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A7")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A7")

    Return()

    # Function_1_56D end

    def Function_2_5A8(): pass

    label("Function_2_5A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_5A8")

    label("loc_5BD")

    Return()

    # Function_2_5A8 end

    def Function_3_5BE(): pass

    label("Function_3_5BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D3")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_3_5BE")

    label("loc_5D3")

    Return()

    # Function_3_5BE end

    def Function_4_5D4(): pass

    label("Function_4_5D4")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-13820, 0, -21910, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6C(315000, 0)
    SetChrPos(0x101, -14020, 0, -25740, 0)
    SetChrPos(0x102, -13880, 0, -27430, 0)
    SetChrPos(0x103, -12570, 0, -26210, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, -2330, 0, 540, 270)
    SetChrPos(0x9, -5040, 0, 1610, 120)
    SetChrPos(0xA, -6710, 0, 660, 132)
    SetChrPos(0xB, -5140, 0, -1420, 66)
    SetChrPos(0xC, -6480, 0, -1100, 68)
    OP_72(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_A1(0xD, 0x0)
    SetChrPos(0xD, 9990, 0, -2360, 341)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#003F#5P真耀眼……\x02\x03",
            "#505F唔，那是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F#5P（别出声，艾丝蒂尔……）\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)

    ChrTalk(
        0x103,
        "#022F#5P（这次还真是中了大奖……）\x02",
    )

    CloseMessageWindow()

    def lambda_779():
        OP_6D(-7840, 0, 13100, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_779)

    def lambda_791():
        OP_67(0, 5220, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_791)

    def lambda_7A9():
        OP_6B(9500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7A9)

    def lambda_7B9():
        OP_6C(25000, 10000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7B9)
    OP_21()
    OP_1D(0x57)
    Sleep(6000)

    def lambda_7D1():
        OP_6D(-4300, 3000, -10, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D1)

    def lambda_7E9():
        OP_6E(138, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7E9)
    Sleep(4000)

    ChrTalk(
        0x8,
        (
            "#201F#2P先把重型物资放在一边，\x01",
            "食品和贵重物品要优先处理。\x02\x03",
            "尽量快一点。\x01",
            "再磨磨蹭蹭的敌人可就来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2P#1K收到！吉尔大哥。\x02",
    )


    ChrTalk(
        0xA,
        "#1P#1K收到！吉尔大哥。\x02",
    )


    ChrTalk(
        0xB,
        "#4P#1K收到！吉尔大哥。\x02",
    )


    ChrTalk(
        0xC,
        "#3P#1K收到！吉尔大哥。\x02",
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()
    Sleep(100)
    Fade(1000)
    OP_6D(-13820, 0, -21910, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(332, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#580F（定期船在这种地方……）\x02\x03",
            "（那个孩子所说的\x01",
            "　果然不是梦啊……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F（这里是……\x01",
            "　露天挖掘用的峡谷吗……）\x02\x03",
            "（果然是个绝妙的隐蔽场所。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F（不会轻易被发现呢。）\x02\x03",
            "（那些空贼搬运的\x01",
            "　是定期船装载的货物吧？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F（这些以后再说吧！）\x02\x03",
            "（在他们还没逃跑之前，\x01",
            "　一定要把他们全部逮住！）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-4110, 0, 490, 0)
    OP_67(0, 5220, -10000, 0)
    OP_6B(5070, 0)
    OP_6C(69000, 0)
    OP_6E(213, 0)
    SetChrChipByIndex(0x101, 8)
    SetChrChipByIndex(0x102, 10)
    SetChrChipByIndex(0x103, 12)
    SetChrPos(0x101, -10010, 0, -10600, 26)
    SetChrPos(0x102, -9790, 0, -12210, 25)
    SetChrPos(0x103, -8430, 0, -11060, 23)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#203F哈，这是第三个来回了……\x02\x03",
            "真是的，大哥一来\x01",
            "就拼命地使唤我这个做弟弟的。\x02\x03",
            "#200F不过算了，这次运完之后，\x01",
            "就可以不慌不忙地要求赎金了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1P到此为止了！\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_D13():
        TurnDirection(0xFE, 0x101, 800)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D13)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_D38():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D38)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_D62():
        TurnDirection(0xFE, 0x101, 800)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D62)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_D87():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D87)
    Sleep(50)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "#201F#5P什么！？\x02",
    )

    CloseMessageWindow()

    def lambda_DBE():
        OP_6D(-4960, 0, -4910, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DBE)

    def lambda_DD6():
        OP_6C(69000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DD6)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#502F只要世上仍存一丝罪恶之源，\x01",
            "燃烧的真实与正义之火就不会消失……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x101,
        "#508F#3S代表爱与正义的游击士，堂堂登场！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x102)
    OP_63(0x103)
    OP_63(0x8)
    OP_63(0x9)
    OP_63(0xA)
    OP_63(0xB)
    OP_63(0xC)

    ChrTalk(
        0x101,
        "#505F咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F爱与正义……好像有点那个了吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F真是的。\x01",
            "马上就开始得意忘形了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x101,
        (
            "#503F怎、怎么了……\x01",
            "我这叫做开门见山嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 6)
    SetChrChipByIndex(0xC, 6)
    SetChrChipByIndex(0xA, 6)
    SetChrChipByIndex(0xB, 6)
    SetChrChipByIndex(0x8, 1)
    SetChrChipByIndex(0x8, 15)
    OP_8E(0x8, 0xFFFFEFFC, 0x0, 0xFFFFF84E, 0x1388, 0x0)
    SetChrChipByIndex(0x8, 1)

    ChrTalk(
        0x8,
        (
            "#201F你们是……\x01",
            "和乔丝特交过手的那些人！？\x02\x03",
            "消、消息有误！\x01",
            "似乎来得太早了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F#2P消息有误？来得太早了？\x02\x03",
            "听不明白你在说什么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F#2P基于游击士协会的规定， \x01",
            "你们涉嫌抢劫定期船以及挟持乘客，\x01",
            "现以协会的名义将你们逮捕归案。\x02\x03",
            "给我束手就擒吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#201F等、等一下。\x02\x03",
            "难道说你们……\x01",
            "靠三个人就想逮捕我们？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F#2P什么呀，一看就知道了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#204F嗯，原来如此。\x01",
            "和那些家伙没关系啊。\x02\x03",
            "#201F要是这样就早点说嘛……\x01",
            "就让你们先暂时睡一会儿吧！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 15)

    def lambda_136B():
        OP_92(0xFE, 0x103, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_136B)
    Sleep(50)
    SetChrChipByIndex(0xC, 19)

    def lambda_138A():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_138A)
    Sleep(50)
    SetChrChipByIndex(0xB, 19)

    def lambda_13A9():
        OP_92(0xFE, 0x102, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_13A9)
    Sleep(50)
    SetChrChipByIndex(0x9, 19)

    def lambda_13C8():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_13C8)
    Sleep(50)
    SetChrChipByIndex(0xA, 19)

    def lambda_13E7():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_13E7)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x103, 13)

    def lambda_1410():
        OP_6D(-3960, 0, -3910, 800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1410)

    def lambda_1428():
        OP_92(0xFE, 0x8, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1428)
    Sleep(50)
    SetChrChipByIndex(0x101, 9)

    def lambda_1447():
        OP_92(0xFE, 0xC, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1447)
    Sleep(50)
    SetChrChipByIndex(0x102, 11)

    def lambda_1466():
        OP_92(0xFE, 0xB, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1466)
    Sleep(300)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    ClearChrFlags(0x103, 0x1000)
    Battle(0x387, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_14C4"),
        (SWITCH_DEFAULT, "loc_14C9"),
    )


    label("loc_14C4")

    OP_B4(0x0)
    Jump("loc_14C9")

    label("loc_14C9")

    OP_6D(-5750, 0, -5350, 0)
    OP_67(0, 5220, -10000, 0)
    OP_6B(5070, 0)
    OP_6C(69000, 0)
    OP_6E(212, 0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 2)
    SetChrChipByIndex(0x9, 7)
    SetChrChipByIndex(0xA, 7)
    SetChrChipByIndex(0xB, 7)
    SetChrChipByIndex(0xC, 7)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 8)
    SetChrChipByIndex(0x102, 10)
    SetChrChipByIndex(0x103, 12)
    SetChrPos(0x8, -5830, 0, -4580, 216)
    SetChrPos(0x9, -4000, 0, -5410, 258)
    SetChrPos(0xA, -4760, 0, -2930, 184)
    SetChrPos(0xB, -8260, 0, -3290, 156)
    SetChrPos(0xC, -2270, 0, -3270, 232)
    SetChrPos(0x101, -9950, 0, -7740, 49)
    SetChrPos(0x102, -9710, 0, -9600, 31)
    SetChrPos(0x103, -7170, 0, -8440, 358)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#203F疼疼疼……\x01",
            "还挺厉害的嘛。\x02\x03",
            "#200F不愧是打败过乔丝特的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F奉承我们也没有用。\x02\x03",
            "#005F你们还是乖乖地投降吧。\x01",
            "还有，把乘客们都放出来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#202F哈哈哈！\x01",
            "看起来你们真的什么都不知道。\x02\x03",
            "真是一群多管闲事的傻瓜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#016F……小心！\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp004_00.eff")
    OP_99(0x8, 0x3, 0x0, 0x3E8)
    SetChrChipByIndex(0x8, 1)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 3)

    def lambda_1810():
        OP_6C(50000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1810)
    OP_99(0x8, 0x0, 0x3, 0x3E8)
    OP_99(0x8, 0x0, 0x3, 0x3E8)
    WaitChrThread(0x101, 0x2)
    SetChrChipByIndex(0x8, 4)
    SoundLoad(127)
    SetChrPos(0x23, -7460, -3000, -6780, 339)
    PlayEffect(0x0, 0xFF, 0x8, 250, 900, 330, 0, 0, 0, 1000, 1000, 1000, 0x23, 0, 0, 0, 0)
    OP_99(0x8, 0x0, 0x1, 0x3E8)
    Sleep(1300)
    OP_22(0x7F, 0x0, 0x64)
    OP_11(0xFF, 0xFF, 0xFF, 0xA410, 0x17318, 0x0)
    SetMapFlags(0x10)
    StopSound(0x2C24, 0xE09C, 0x7D0)
    Sleep(2000)

    ChrTalk(
        0x101,
        "#580F这、这是什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#024F糟了，是烟雾弹！？\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_22(0x79, 0x0, 0x64)
    OP_22(0xCC, 0x0, 0x64)
    OP_22(0xCD, 0x0, 0x64)
    SetChrPos(0x8, 2280, 0, -8280, 117)

    ChrTalk(
        0x8,
        (
            "#202F啊～哈哈哈哈哈！\x02\x03",
            "虽然货物没搬光有点不甘心，\x01",
            "但是我就先忍了！\x02\x03",
            "再见啦，各位游击士！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xD, 6450, 100, -820, 341)
    SetChrPos(0xE, 6450, 100, -820, 341)
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    PlayEffect(0x1, 0x2, 0xE, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_72(0x0, 0x4)
    OP_71(0x1, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x40)
    OP_A1(0xD, 0x0)
    OP_A1(0xE, 0x1)

    def lambda_1A5D():

        label("loc_1A5D")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_1A5D")

    QueueWorkItem2(0x101, 1, lambda_1A5D)

    def lambda_1A6E():

        label("loc_1A6E")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_1A6E")

    QueueWorkItem2(0x103, 1, lambda_1A6E)

    def lambda_1A7F():

        label("loc_1A7F")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_1A7F")

    QueueWorkItem2(0x102, 1, lambda_1A7F)
    OP_43(0xD, 0x1, 0x0, 0x5)
    OP_43(0xE, 0x1, 0x0, 0x6)

    def lambda_1A9E():
        OP_6C(26000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A9E)
    Sleep(1000)

    def lambda_1AB3():
        OP_6B(6000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1AB3)
    StopSound(0xA794, 0x1BD50, 0x2710)
    Sleep(1000)

    def lambda_1AD5():
        OP_6D(-8130, 0, -15090, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1AD5)
    OP_43(0x103, 0x3, 0x0, 0x7)
    Sleep(5000)

    def lambda_1AF9():
        OP_6D(-9300, 0, -10850, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1AF9)
    OP_6B(5170, 2000)
    OP_20(0x5DC)
    Fade(1000)
    ClearMapFlags(0x10)
    OP_0D()
    OP_21()
    OP_1D(0x1E)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#007F咳，咳咳……\x02\x03",
            "好像进到眼睛里了～……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F别担心，没有毒……\x01",
            "好像只是普通的发烟筒而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x103, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x103, 65535)
    OP_8E(0x103, 0xFFFFDFD0, 0x0, 0xFFFFD364, 0x7D0, 0x0)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x103)

    ChrTalk(
        0x103,
        (
            "#022F……已经看不到他们了。\x02\x03",
            "#025F哎呀呀，跟上次一样，\x01",
            "这次也被他们逃掉了。\x02\x03",
            "这下可好了，\x01",
            "就算给我降级的处分我也无话可说。\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x103, 400)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        (
            "#009F真是的，雪拉姐……\x02\x03",
            "老是这样，\x01",
            "不要把过错都揽到自己一个人身上嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F我们也应该承担\x01",
            "被他们逃掉的责任。\x02\x03",
            "与其在这里后悔，\x01",
            "倒不如想想现在能做些什么……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#026F#4P呼，真是的……\x01",
            "我们的立场好像颠倒了呢。\x02\x03",
            "#020F不过幸好把定期船夺回来了。\x01",
            "我们赶快进去调查看看吧。\x02\x03",
            "也许里面还有乘客。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F……嗯！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, -12570, 0, -19040, 0)
    SetChrPos(0x102, -12570, 0, -19040, 0)
    SetChrPos(0x103, -12570, 0, -19040, 0)
    OP_6D(-12570, 0, -19040, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)
    OP_28(0x36, 0x1, 0x200)
    OP_28(0x36, 0x1, 0x400)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_4_5D4 end

    def Function_5_1F8C(): pass

    label("Function_5_1F8C")


    def lambda_1F92():
        OP_8F(0xFE, 0xFFFF029A, 0xFA0, 0xFFFF1E2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1F92)

    def lambda_1FAD():
        OP_8C(0xFE, 200, 30)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1FAD)
    Sleep(1000)

    def lambda_1FC0():
        OP_8F(0xFE, 0xFFFF9AF2, 0x4A38, 0xFFFEF71E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1FC0)
    Sleep(500)

    def lambda_1FE0():
        OP_8F(0xFE, 0xFFFF9AF2, 0x4A38, 0xFFFEF71E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1FE0)
    Sleep(500)
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 160)
    OP_70(0x0, 0xC8)

    def lambda_2012():
        OP_8C(0xFE, 200, 30)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2012)
    Sleep(200)

    def lambda_2025():
        OP_8C(0xFE, 200, 28)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2025)
    Sleep(200)

    def lambda_2038():
        OP_8C(0xFE, 200, 26)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2038)
    Sleep(200)

    def lambda_204B():
        OP_8C(0xFE, 200, 24)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_204B)
    Sleep(200)

    def lambda_205E():
        OP_8C(0xFE, 200, 22)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_205E)
    Sleep(200)

    def lambda_2071():
        OP_8C(0xFE, 200, 20)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2071)
    Sleep(200)

    def lambda_2084():
        OP_8C(0xFE, 200, 18)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2084)
    Sleep(200)

    def lambda_2097():
        OP_8C(0xFE, 200, 16)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2097)
    Sleep(200)

    def lambda_20AA():
        OP_8C(0xFE, 200, 15)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_20AA)
    OP_6F(0x0, 200)
    OP_70(0x0, 0xF0)

    def lambda_20C6():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3A98, 0xFFFEF71E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_20C6)
    Sleep(500)

    def lambda_20E6():
        OP_8C(0xFE, 200, 20)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_20E6)

    def lambda_20F4():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3A98, 0xFFFEF71E, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_20F4)
    Sleep(500)

    def lambda_2114():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3A98, 0xFFFEF71E, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2114)
    Sleep(500)

    def lambda_2134():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3A98, 0xFFFEF71E, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2134)
    Sleep(500)

    def lambda_2154():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3A98, 0xFFFEF71E, 0x6590, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2154)
    Sleep(500)

    def lambda_2174():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3A98, 0xFFFEF71E, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2174)
    Sleep(500)

    def lambda_2194():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3A98, 0xFFFEF71E, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2194)
    Sleep(500)
    WaitChrThread(0xFE, 0x2)
    OP_71(0x0, 0x4)
    Return()

    # Function_5_1F8C end

    def Function_6_21B9(): pass

    label("Function_6_21B9")


    def lambda_21BF():
        OP_8F(0xFE, 0xFFFF029A, 0x3E8, 0xFFFF1E2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_21BF)

    def lambda_21DA():
        OP_8C(0xFE, 200, 30)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_21DA)
    Sleep(1000)

    def lambda_21ED():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3E8, 0xFFFEF71E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_21ED)
    Sleep(500)

    def lambda_220D():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3E8, 0xFFFEF71E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_220D)
    Sleep(500)
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 160)
    OP_70(0x0, 0xC8)

    def lambda_223F():
        OP_8C(0xFE, 200, 30)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_223F)
    Sleep(200)

    def lambda_2252():
        OP_8C(0xFE, 200, 28)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2252)
    Sleep(200)

    def lambda_2265():
        OP_8C(0xFE, 200, 26)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2265)
    Sleep(200)

    def lambda_2278():
        OP_8C(0xFE, 200, 24)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2278)
    Sleep(200)

    def lambda_228B():
        OP_8C(0xFE, 200, 22)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_228B)
    Sleep(200)

    def lambda_229E():
        OP_8C(0xFE, 200, 20)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_229E)
    Sleep(200)

    def lambda_22B1():
        OP_8C(0xFE, 200, 18)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_22B1)
    Sleep(200)

    def lambda_22C4():
        OP_8C(0xFE, 200, 16)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_22C4)
    Sleep(200)

    def lambda_22D7():
        OP_8C(0xFE, 200, 15)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_22D7)
    OP_6F(0x0, 200)
    OP_70(0x0, 0xF0)

    def lambda_22F3():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3E8, 0xFFFEF71E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_22F3)
    Sleep(500)

    def lambda_2313():
        OP_8C(0xFE, 200, 20)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2313)

    def lambda_2321():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3E8, 0xFFFEF71E, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2321)
    Sleep(500)

    def lambda_2341():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3E8, 0xFFFEF71E, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2341)
    Sleep(500)

    def lambda_2361():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3E8, 0xFFFEF71E, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2361)
    Sleep(500)

    def lambda_2381():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3E8, 0xFFFEF71E, 0x6590, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2381)
    Sleep(500)

    def lambda_23A1():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3E8, 0xFFFEF71E, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_23A1)
    Sleep(500)

    def lambda_23C1():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3E8, 0xFFFEF71E, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_23C1)
    Sleep(500)
    WaitChrThread(0xFE, 0x2)
    OP_71(0x0, 0x4)
    Return()

    # Function_6_21B9 end

    def Function_7_23E6(): pass

    label("Function_7_23E6")

    Sleep(2000)
    OP_24(0x79, 0x5F)
    OP_24(0xCC, 0x5F)
    OP_24(0xCD, 0x5F)
    Sleep(200)
    OP_24(0x79, 0x5A)
    OP_24(0xCC, 0x5A)
    OP_24(0xCD, 0x5A)
    Sleep(200)
    OP_24(0x79, 0x55)
    OP_24(0xCC, 0x55)
    OP_24(0xCD, 0x55)
    Sleep(200)
    OP_24(0x79, 0x50)
    OP_24(0xCC, 0x50)
    OP_24(0xCD, 0x50)
    Sleep(200)
    OP_24(0x79, 0x46)
    OP_24(0xCC, 0x46)
    OP_24(0xCD, 0x46)
    Sleep(200)
    OP_24(0x79, 0x3C)
    OP_24(0xCC, 0x3C)
    OP_24(0xCD, 0x3C)
    Sleep(200)
    OP_24(0x79, 0x32)
    OP_24(0xCC, 0x32)
    OP_24(0xCD, 0x32)
    Sleep(200)
    OP_23(0x79)
    OP_23(0xCC)
    OP_23(0xCD)
    Return()

    # Function_7_23E6 end

    def Function_8_246C(): pass

    label("Function_8_246C")

    EventBegin(0x0)
    OP_6D(-11700, 7200, 16590, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -5960, 7200, 16680, 90)
    SetChrPos(0x102, -4940, 7200, 15330, 51)
    SetChrPos(0x103, -4230, 7200, 16900, 244)
    FadeToBright(1000, 0)
    OP_6D(-5220, 7200, 16540, 3000)

    ChrTalk(
        0x101,
        (
            "#007F#5P虽然已经调查了一遍，\x01",
            "可是一个人也没有发现……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F看样子乘客被空贼\x01",
            "用空贼飞艇带走的可能性很高。\x02\x03",
            "#012F……大概，是到他们的据点去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F#5P唔……\x02\x03",
            "好不容易\x01",
            "才找到的线索就这样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F好了好了。\x01",
            "不要这么愁眉苦脸的。\x02\x03",
            "现在并不是\x01",
            "一点线索都没有哦。\x02\x03",
            "#027F你们想想，为什么那帮家伙\x01",
            "会把定期船藏在这种地方呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#5P哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026F正如刚才所见，\x01",
            "定期船内的导力完全停止了……\x02\x03",
            "这也就意味着，\x01",
            "导力引擎被他们拿走了。\x02\x03",
            "众所周知，导力器中的导力\x01",
            "在经过一段时间后会自动回复。\x02\x03",
            "#022F而那些家伙多次\x01",
            "来回运送大量的货物。\x02\x03",
            "考虑这样做所花费的时间和带来的风险，\x01",
            "用定期船把货物运往自己的据点\x01",
            "效率反倒应该高得多吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#5P啊，确实……\x02\x03",
            "那么，空贼把定期船\x01",
            "藏在这个地方的原因就是……\x02\x03",
            "#505F嗯，仔细考虑一下的话……\x02",
        )
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
            "【为了挑选货物】\x01",                    # 0
            "【为了把人质转移到空贼飞艇上】\x01",      # 1
            "【为了抢夺导力引擎】\x01",                # 2
            "【为了逃避王国军的搜捕】\x01",            # 3
            "【因为据点在特殊的地方】\x01",            # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A9E"),
        (1, "loc_2B68"),
        (2, "loc_2C28"),
        (3, "loc_2CEE"),
        (4, "loc_2DF0"),
        (SWITCH_DEFAULT, "loc_2E1D"),
    )


    label("loc_2A9E")


    ChrTalk(
        0x103,
        (
            "#026F确实，这里比较宽阔，\x01",
            "挑选货物时也许很方便。\x02\x03",
            "#027F但是，这却无法构成\x01",
            "空贼把定期船藏在这个地方的理由。\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x35, 0x1)
    Jump("loc_2E1D")

    label("loc_2B68")


    ChrTalk(
        0x103,
        (
            "#026F确实，在把人质转移到空贼飞艇上的过程中，\x01",
            "定期船必须要着陆。\x02\x03",
            "#027F但是，这却无法构成\x01",
            "空贼把定期船藏在这个地方的理由。\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x35, 0x1)
    Jump("loc_2E1D")

    label("loc_2C28")


    ChrTalk(
        0x103,
        (
            "#026F确实，要把引擎拔除的话，\x01",
            "定期船必须要着陆。\x02\x03",
            "#027F但是，这却无法构成\x01",
            "空贼把定期船藏在这个地方的理由。\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x35, 0x1)
    Jump("loc_2E1D")

    label("loc_2CEE")


    ChrTalk(
        0x103,
        (
            "#026F确实，定期船很大，\x01",
            "很容易会被王国军发现……\x02\x03",
            "#027F所以把它藏在\x01",
            "据点以外的场所的可能性很高。\x02\x03",
            "但是，这个解释\x01",
            "也不能说是决定性的理由。\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x35, 0x2)
    Jump("loc_2E1D")

    label("loc_2DF0")


    ChrTalk(
        0x103,
        "#021F对，就是因为这个。\x02",
    )

    CloseMessageWindow()
    OP_2B(0x35, 0x3)
    Jump("loc_2E1D")

    label("loc_2E1D")

    Sleep(400)

    ChrTalk(
        0x103,
        (
            "#020F根据我的推测，\x01",
            "他们的据点应该是个地形特殊的地方。\x02\x03",
            "１０～１５亚矩……\x02\x03",
            "也就是说只能让空贼飞艇\x01",
            "这种小型艇降落的特殊场所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F#5P原、原来是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F像山峦、峡谷这样\x01",
            "高低差很大的复杂地形……\x02\x03",
            "#012F应该是最值得怀疑的地方吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F对，我也这么想。\x02\x03",
            "#522F如果真是那样的话……\x01",
            "那真是超出我们能力范围了。\x02\x03",
            "他们的据点很有可能\x01",
            "是在步行所涉足不到的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#5P那、那怎么办呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F是啊……\x02\x03",
            "虽然让人失望，但现在唯有\x01",
            "向军队说明情况并请求他们协助了。\x02\x03",
            "毕竟他们拥有军用飞艇啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#5P哎～……\x01",
            "搞了半天还是要依靠军队啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这艘定期船的事情\x01",
            "最后肯定要报告给军队的。\x02\x03",
            "不管他们的态度怎么样，\x01",
            "我认为现在还是合作比较好。\x02\x03",
            "这也是为了早点解放人质啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#5P嗯，是啊……\x02\x03",
            "现在不是任性的时候啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F总之，我们先回游击士协会\x01",
            "向卢格兰爷爷汇报一下吧。\x02\x03",
            "使用协会的导力通信器，\x01",
            "就可以和哈肯大门联络了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x36, 0x1, 0x800)
    OP_28(0x36, 0x1, 0x1000)
    EventEnd(0x0)
    Return()

    # Function_8_246C end

    def Function_9_340E(): pass

    label("Function_9_340E")

    EventBegin(0x0)
    OP_6D(-9690, 2130, 10650, 0)
    OP_67(0, 7660, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(293, 0)
    SetChrPos(0x101, -10200, 1630, 9500, 180)
    SetChrPos(0x103, -9190, 1620, 9480, 180)
    SetChrPos(0x102, -9720, 2020, 10410, 180)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x10, -9650, 0, 2260, 0)
    SetChrPos(0x11, -11190, 0, 2770, 24)
    SetChrPos(0x12, -12650, 0, 3420, 24)
    SetChrPos(0x13, -14120, 0, 4070, 24)
    SetChrPos(0x14, -15860, 0, 4850, 24)
    SetChrPos(0x15, -16590, 0, 3200, 24)
    SetChrPos(0x16, -14940, 0, 2470, 24)
    SetChrPos(0x17, -13390, 0, 1780, 24)
    SetChrPos(0x18, -11940, 0, 1130, 24)
    SetChrPos(0x19, -10330, 0, 610, 24)
    SetChrPos(0x1A, -8189, 0, 2810, 336)
    SetChrPos(0x1B, -6820, 0, 3430, 336)
    SetChrPos(0x1C, -5550, 0, 4000, 336)
    SetChrPos(0x1D, -4190, 0, 4600, 336)
    SetChrPos(0x1E, -8870, 0, 510, 336)
    SetChrPos(0x1F, -7450, 0, 1150, 336)
    SetChrPos(0x20, -6170, 0, 1720, 336)
    SetChrPos(0x21, -4870, 0, 2300, 336)
    SetChrPos(0x22, -3390, 0, 2960, 336)
    OP_72(0x5, 0x4)
    OP_72(0x6, 0x4)
    FadeToBright(1000, 0)
    OP_20(0x5DC)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#580F#5P哎、哎哎～～！？\x02\x03",
            "这、这是怎么回事啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F#5P哈……\x01",
            "这真是意料之外的来者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F#5P唔，看来这次\x01",
            "连联络的功夫也省了……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x65)
    Fade(2000)
    OP_6D(9600, 0, -2009, 0)
    OP_67(0, 13000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(280000, 0)
    OP_6E(483, 0)

    def lambda_37AB():
        OP_67(0, 6570, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_37AB)
    Sleep(2500)

    def lambda_37C8():
        OP_6C(39000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_37C8)

    def lambda_37D8():
        OP_6E(350, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_37D8)
    OP_6D(-10180, 340, 6490, 6000)

    ChrTalk(
        0x10,
        (
            "#2P发现一干\x01",
            "手持武器的嫌疑犯！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#2P你们！\x01",
            "老实举起手来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5P真是世态炎凉啊，\x01",
            "连小女孩也做起空贼来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F谁、谁是空贼啊！？\x02\x03",
            "没看到我身上的徽章吗！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xF, -9410, 0, -4900, 0)
    ClearChrFlags(0xF, 0x80)

    NpcTalk(
        0xF,
        "老人的声音",
        "#1P哼，游击士的徽章吗……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "老人的声音",
        (
            "#1P凭这种东西\x01",
            "就能证明自身的清白？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A00():
        OP_8E(0xFE, 0xFFFFDA58, 0x0, 0x11D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3A00)
    Sleep(500)

    def lambda_3A20():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3A20)

    def lambda_3A2E():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_3A2E)
    WaitChrThread(0x19, 0x1)

    def lambda_3A41():
        OP_8F(0xFE, 0xFFFFD59E, 0x0, 0x30C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3A41)

    def lambda_3A5C():
        OP_8F(0xFE, 0xFFFFDF62, 0x0, 0x226, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_3A5C)

    def lambda_3A77():

        label("loc_3A77")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_3A77")

    QueueWorkItem2(0x19, 1, lambda_3A77)

    def lambda_3A88():

        label("loc_3A88")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_3A88")

    QueueWorkItem2(0x1E, 1, lambda_3A88)

    def lambda_3A99():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3A99)
    WaitChrThread(0x10, 0x1)

    def lambda_3AAC():
        OP_8F(0xFE, 0xFFFFDD6E, 0x0, 0x76C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3AAC)

    def lambda_3AC7():

        label("loc_3AC7")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_3AC7")

    QueueWorkItem2(0x10, 1, lambda_3AC7)

    def lambda_3AD8():
        OP_6D(-9140, 1050, 8950, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3AD8)

    def lambda_3AF0():
        OP_6E(306, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3AF0)
    WaitChrThread(0xF, 0x1)

    ChrTalk(
        0x101,
        "#004F摩、摩尔根将军！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F为什么会在这里……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#163F根据各部队的报告，\x01",
            "这里尚未进行细致的搜查。\x01",
            "我们来这里也是理所当然的事情……\x02\x03",
            "#160F但是，万万没想到\x01",
            "你们竟然和空贼勾结。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F在没有真凭实据之前，\x01",
            "请不要这样随意下结论。\x02\x03",
            "我们只是先你们一步\x01",
            "到这里做现场调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#161F那么空贼在哪里？\x02\x03",
            "船内的乘客又在哪里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F只差一步就能抓住那些空贼了，\x01",
            "这是我们的疏忽。\x02\x03",
            "作为人质的乘客也不在定期船里面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#163F哼，真是不打自招……\x02\x03",
            "原来在我们到来之前，\x01",
            "你们已经向空贼通风报信了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F等、等一下！\x01",
            "你这样说实在是太过分了！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0xF,
        "#162F#5S这是我该讲的台词！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0xF,
        (
            "#162F#3S来人！\x01",
            "把这三个嫌疑犯抓起来！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_28(0x36, 0x1, 0x2000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1401   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_340E end

    def Function_10_3EF1(): pass

    label("Function_10_3EF1")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F09")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_3F10")

    label("loc_3F09")

    TurnDirection(0x103, 0x0, 400)

    label("loc_3F10")


    def lambda_3F16():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F16)

    def lambda_3F24():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F24)

    ChrTalk(
        0x103,
        (
            "#020F没有去别的地方的时间了。\x01",
            "　\x02\x03",
            "现在最重要的是调查定期船。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x7D0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_10_3EF1 end

    def Function_11_3FCE(): pass

    label("Function_11_3FCE")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FE6")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_3FED")

    label("loc_3FE6")

    TurnDirection(0x103, 0x0, 400)

    label("loc_3FED")


    def lambda_3FF3():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FF3)

    def lambda_4001():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4001)

    ChrTalk(
        0x103,
        (
            "#020F没有去别的地方的时间了。\x01",
            "　\x02\x03",
            "现在最重要的是调查定期船。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0xFFFFF830, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_11_3FCE end

    def Function_12_40AB(): pass

    label("Function_12_40AB")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40C3")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_40CA")

    label("loc_40C3")

    TurnDirection(0x103, 0x0, 400)

    label("loc_40CA")


    def lambda_40D0():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40D0)

    def lambda_40DE():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_40DE)

    ChrTalk(
        0x103,
        (
            "#020F没有去别的地方的时间了。\x01",
            "　\x02\x03",
            "现在最重要的是调查定期船。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x7D0, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_12_40AB end

    def Function_13_4188(): pass

    label("Function_13_4188")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41A0")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_41A7")

    label("loc_41A0")

    TurnDirection(0x103, 0x0, 400)

    label("loc_41A7")


    def lambda_41AD():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41AD)

    def lambda_41BB():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_41BB)

    ChrTalk(
        0x103,
        (
            "#020F没有去别的地方的时间了。\x01",
            "　\x02\x03",
            "现在最重要的是调查定期船。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFF830, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_13_4188 end

    SaveToFile()

Try(main)
