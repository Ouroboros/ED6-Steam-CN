from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4310   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4310.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60089",
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
        '特务兵',                               # 9
        '特务兵',                               # 10
        '特务兵',                               # 11
        '特务兵',                               # 12
        '中队长',                               # 13
        '莉安妮',                               # 14
        '基库',                                 # 15
        '奈尔',                                 # 16
        '科洛蒂娅公主',                         # 17
        '尤莉亚中尉',                           # 18
        '雪拉扎德',                             # 19
        '奥利维尔',                             # 20
        '卡露娜',                               # 21
        '亚妮拉丝',                             # 22
        '库拉茨',                               # 23
        '克鲁茨',                               # 24
        '亲卫队员',                             # 25
        '亲卫队员',                             # 26
        '亲卫队员',                             # 27
        '亲卫队员',                             # 28
        '亲卫队员',                             # 29
        '亲卫队员',                             # 30
        '贵族老奶奶',                           # 31
        '贵族中年男子',                         # 32
        '贵族女孩',                             # 33
        '贵族青年',                             # 34
        '贵族中年女子',                         # 35
        '贵族老人',                             # 36
        '贵族小孩',                             # 37
        '男性学者２',                           # 38
        '管家',                                 # 39
        '青年市民',                             # 40
        ' ',                                    # 41
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
        'ED6_DT07/CH00100 ._CH',             # 00
        'ED6_DT07/CH00101 ._CH',             # 01
        'ED6_DT07/CH00110 ._CH',             # 02
        'ED6_DT07/CH00111 ._CH',             # 03
        'ED6_DT07/CH00170 ._CH',             # 04
        'ED6_DT07/CH00171 ._CH',             # 05
        'ED6_DT07/CH00340 ._CH',             # 06
        'ED6_DT07/CH00341 ._CH',             # 07
        'ED6_DT07/CH00510 ._CH',             # 08
        'ED6_DT07/CH01480 ._CH',             # 09
        'ED6_DT07/CH02320 ._CH',             # 0A
        'ED6_DT07/CH02060 ._CH',             # 0B
        'ED6_DT06/CH20143 ._CH',             # 0C
        'ED6_DT07/CH02090 ._CH',             # 0D
        'ED6_DT07/CH00020 ._CH',             # 0E
        'ED6_DT07/CH00030 ._CH',             # 0F
        'ED6_DT07/CH00122 ._CH',             # 10
        'ED6_DT07/CH00514 ._CH',             # 11
        'ED6_DT07/CH00513 ._CH',             # 12
        'ED6_DT07/CH01240 ._CH',             # 13
        'ED6_DT07/CH01630 ._CH',             # 14
        'ED6_DT07/CH01260 ._CH',             # 15
        'ED6_DT07/CH01620 ._CH',             # 16
        'ED6_DT07/CH01320 ._CH',             # 17
        'ED6_DT07/CH00040 ._CH',             # 18
        'ED6_DT06/CH20042 ._CH',             # 19
        'ED6_DT07/CH01180 ._CH',             # 1A
        'ED6_DT07/CH01200 ._CH',             # 1B
        'ED6_DT07/CH01210 ._CH',             # 1C
        'ED6_DT07/CH01220 ._CH',             # 1D
        'ED6_DT07/CH01230 ._CH',             # 1E
        'ED6_DT07/CH01490 ._CH',             # 1F
        'ED6_DT07/CH01470 ._CH',             # 20
        'ED6_DT07/CH01190 ._CH',             # 21
        'ED6_DT07/CH01560 ._CH',             # 22
        'ED6_DT07/CH01220 ._CH',             # 23
        'ED6_DT06/CH20113 ._CH',             # 24
        'ED6_DT07/CH00440 ._CH',             # 25
        'ED6_DT07/CH00441 ._CH',             # 26
        'ED6_DT07/CH01790 ._CH',             # 27
        'ED6_DT07/CH00500 ._CH',             # 28
        'ED6_DT07/CH00501 ._CH',             # 29
        'ED6_DT07/CH00444 ._CH',             # 2A
        'ED6_DT07/CH00443 ._CH',             # 2B
        'ED6_DT06/CH20114 ._CH',             # 2C
        'ED6_DT06/CH20115 ._CH',             # 2D
    )

    AddCharChipPat(
        'ED6_DT07/CH00100P._CP',             # 00
        'ED6_DT07/CH00101P._CP',             # 01
        'ED6_DT07/CH00110P._CP',             # 02
        'ED6_DT07/CH00111P._CP',             # 03
        'ED6_DT07/CH00170P._CP',             # 04
        'ED6_DT07/CH00171P._CP',             # 05
        'ED6_DT07/CH00340P._CP',             # 06
        'ED6_DT07/CH00341P._CP',             # 07
        'ED6_DT07/CH00510P._CP',             # 08
        'ED6_DT07/CH01480P._CP',             # 09
        'ED6_DT07/CH02320P._CP',             # 0A
        'ED6_DT07/CH02060P._CP',             # 0B
        'ED6_DT06/CH20143P._CP',             # 0C
        'ED6_DT07/CH02090P._CP',             # 0D
        'ED6_DT07/CH00020P._CP',             # 0E
        'ED6_DT07/CH00030P._CP',             # 0F
        'ED6_DT07/CH00122P._CP',             # 10
        'ED6_DT07/CH00514P._CP',             # 11
        'ED6_DT07/CH00513P._CP',             # 12
        'ED6_DT07/CH01240P._CP',             # 13
        'ED6_DT07/CH01630P._CP',             # 14
        'ED6_DT07/CH01260P._CP',             # 15
        'ED6_DT07/CH01620P._CP',             # 16
        'ED6_DT07/CH01320P._CP',             # 17
        'ED6_DT07/CH00040P._CP',             # 18
        'ED6_DT06/CH20042P._CP',             # 19
        'ED6_DT07/CH01180P._CP',             # 1A
        'ED6_DT07/CH01200P._CP',             # 1B
        'ED6_DT07/CH01210P._CP',             # 1C
        'ED6_DT07/CH01220P._CP',             # 1D
        'ED6_DT07/CH01230P._CP',             # 1E
        'ED6_DT07/CH01490P._CP',             # 1F
        'ED6_DT07/CH01470P._CP',             # 20
        'ED6_DT07/CH01190P._CP',             # 21
        'ED6_DT07/CH01560P._CP',             # 22
        'ED6_DT07/CH01220P._CP',             # 23
        'ED6_DT06/CH20113P._CP',             # 24
        'ED6_DT07/CH00440P._CP',             # 25
        'ED6_DT07/CH00441P._CP',             # 26
        'ED6_DT07/CH01790P._CP',             # 27
        'ED6_DT07/CH00500P._CP',             # 28
        'ED6_DT07/CH00501P._CP',             # 29
        'ED6_DT07/CH00444P._CP',             # 2A
        'ED6_DT07/CH00443P._CP',             # 2B
        'ED6_DT06/CH20114P._CP',             # 2C
        'ED6_DT06/CH20115P._CP',             # 2D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 37,
        ChipIndex           = 0x25,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 14,
        ChipIndex           = 0xF,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
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
        Unknown3            = 21,
        ChipIndex           = 0x15,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4420,
        Z                   = 250,
        Y                   = 72560,
        Direction           = 201,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5090,
        Z                   = 0,
        Y                   = 70990,
        Direction           = 254,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3560,
        Z                   = 250,
        Y                   = 71090,
        Direction           = 208,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -4630,
        Z                   = 250,
        Y                   = 72900,
        Direction           = 165,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3480,
        Z                   = 250,
        Y                   = 72300,
        Direction           = 150,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -4870,
        Z                   = 0,
        Y                   = 70280,
        Direction           = 162,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 6280,
        Z                   = 0,
        Y                   = 66790,
        Direction           = 237,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 6740,
        Z                   = 0,
        Y                   = 65120,
        Direction           = 257,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 8300,
        Z                   = 0,
        Y                   = 63060,
        Direction           = 241,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 6540,
        Z                   = 0,
        Y                   = 69410,
        Direction           = 239,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -57400,
        Y                   = 1000,
        Z                   = 2550,
        Range               = -43640,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0xFFFFFCCC,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )


    ScpFunction(
        "Function_0_65A",          # 00, 0
        "Function_1_70A",          # 01, 1
        "Function_2_718",          # 02, 2
        "Function_3_72E",          # 03, 3
        "Function_4_D67",          # 04, 4
        "Function_5_1203",         # 05, 5
        "Function_6_142A",         # 06, 6
        "Function_7_4438",         # 07, 7
        "Function_8_4460",         # 08, 8
        "Function_9_4C64",         # 09, 9
    )


    def Function_0_65A(): pass

    label("Function_0_65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_66D")
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    Event(0, 3)

    label("loc_66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_67B")
    OP_A3(0x3FB)
    Event(0, 8)

    label("loc_67B")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_687"),
        (SWITCH_DEFAULT, "loc_69D"),
    )


    label("loc_687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69A")
    OP_A2(0x659)
    Event(0, 6)

    label("loc_69A")

    Jump("loc_69D")

    label("loc_69D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 4)), scpexpr(EXPR_END)), "loc_6F8")
    SetChrSubChip(0x8, 0)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x8, -48300, 0, 18410, 90)
    SetChrPos(0x9, -48500, 0, 17000, 135)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
    SetChrChipByIndex(0x8, 25)
    SetChrChipByIndex(0x9, 25)

    label("loc_6F8")

    OP_51(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_65A end

    def Function_1_70A(): pass

    label("Function_1_70A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_717")
    OP_1B(0x0, 0x0, 0x9)

    label("loc_717")

    Return()

    # Function_1_70A end

    def Function_2_718(): pass

    label("Function_2_718")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_72D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_718")

    label("loc_72D")

    Return()

    # Function_2_718 end

    def Function_3_72E(): pass

    label("Function_3_72E")

    EventBegin(0x0)
    OP_6D(19290, 0, 360, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(5020, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x108, 190, 0, -7530, 0)
    SetChrPos(0x101, -1330, 0, -8480, 0)
    SetChrPos(0x102, 570, 0, -8760, 0)
    FadeToBright(1000, 0)
    OP_6D(640, 0, -4630, 4000)
    Fade(1000)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#004F这里就是『艾尔贝离宫』……\x02\x03",
            "唔～与城里相比，\x01",
            "也是同样那么的典雅豪华啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F啊，因为是王家的建筑嘛。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, 11820, 0, -6220, 250)
    SetChrPos(0x9, 12550, 0, -5100, 250)
    SetChrPos(0xB, 14020, 0, -5780, 250)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x108, 100, 400)

    ChrTalk(
        0x108,
        "#076F好的，冲进去！\x02",
    )

    CloseMessageWindow()

    def lambda_947():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_947)

    def lambda_955():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_955)

    def lambda_963():
        OP_6D(6340, 0, -6950, 1500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_963)

    def lambda_97B():
        OP_67(0, 4710, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_97B)

    def lambda_993():
        OP_6C(68000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_993)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x8,
        "你、你们是什么人！？\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFFFFFD44, 0x0, 0xFFFFE4F8, 0x1388, 0x0)
    OP_8E(0x101, 0x316, 0x0, 0xFFFFE82C, 0x1388, 0x0)
    OP_8C(0x101, 100, 0)

    ChrTalk(
        0x101,
        "#005F#5P你们这些坏人不配知道！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#5P不必多言，我们上！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A59():
        OP_6D(10400, 0, -6130, 700)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A59)

    def lambda_A71():
        OP_92(0xFE, 0x8, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A71)
    Sleep(50)

    def lambda_A8B():
        OP_92(0xFE, 0x8, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A8B)
    Sleep(50)

    def lambda_AA5():
        OP_92(0xFE, 0x8, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_AA5)
    SetChrChipByIndex(0x8, 7)
    SetChrFlags(0x8, 0x1000)

    def lambda_AC4():
        OP_92(0xFE, 0x108, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AC4)
    Sleep(50)
    SetChrChipByIndex(0x9, 38)
    SetChrFlags(0x9, 0x1000)

    def lambda_AE8():
        OP_92(0xFE, 0x108, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_AE8)
    Sleep(50)
    SetChrChipByIndex(0xB, 38)
    SetChrFlags(0xB, 0x1000)

    def lambda_B0C():
        OP_92(0xFE, 0x108, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B0C)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0x8, 0x1000)
    ClearChrFlags(0x9, 0x1000)
    ClearChrFlags(0xB, 0x1000)
    Battle(0x3AD, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_B6F"),
        (SWITCH_DEFAULT, "loc_B72"),
    )


    label("loc_B6F")

    OP_B4(0x0)
    Return()

    label("loc_B72")

    EventBegin(0x0)
    SetChrChipByIndex(0x8, 25)
    SetChrChipByIndex(0x9, 25)
    SetChrChipByIndex(0xB, 25)
    SetChrSubChip(0x8, 0)
    SetChrSubChip(0x9, 0)
    SetChrSubChip(0xB, 0)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
    SetChrFlags(0xB, 0x800)
    SetChrPos(0x8, 11700, 0, -9160, 176)
    SetChrPos(0x9, 12780, 0, -10830, 90)
    SetChrPos(0xB, 10700, 0, -11180, 296)
    OP_6D(10320, 0, -5900, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    SetChrPos(0x101, 7960, 0, -6540, 90)
    SetChrPos(0x108, 9450, 0, -5900, 270)
    SetChrPos(0x102, 8270, 0, -5050, 90)
    FadeToBright(1000, 0)
    OP_6D(8640, 0, -5700, 1500)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#002F嗯，公主殿下他们被关在哪里呢？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F肯定在这个巨大的建筑里面。\x02\x03",
            "我们要进行地毯式的调查才行。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072F如果再磨磨蹭蹭的话，\x01",
            "前庭的那些家伙就会赶来了。\x02\x03",
            "尽快行动。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_3_72E end

    def Function_4_D67(): pass

    label("Function_4_D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 4)), scpexpr(EXPR_END)), "loc_D6F")
    Return()

    label("loc_D6F")

    OP_A2(0x654)
    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, -52180, 0, 20500, 180)
    SetChrPos(0x9, -50170, 0, 20530, 180)
    SetChrChipByIndex(0x8, 39)
    SetChrChipByIndex(0x9, 39)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_DC7():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_DC7)

    def lambda_DD5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DD5)

    def lambda_DE3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DE3)
    OP_6D(-50570, 0, 17760, 2000)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x108, -50910, 0, 8080, 0)
    SetChrPos(0x102, -50140, 0, 6930, 0)
    SetChrPos(0x101, -52160, 0, 7020, 0)

    def lambda_E44():
        OP_8E(0xFE, 0xFFFF38C8, 0x0, 0x31EC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_E44)

    def lambda_E5F():
        OP_8E(0xFE, 0xFFFF34FE, 0x0, 0x2CF6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E5F)

    def lambda_E7A():
        OP_8E(0xFE, 0xFFFF3BDE, 0x0, 0x2E90, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E7A)

    ChrTalk(
        0x8,
        "#5P你们是什么人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P好像在哪儿见过……\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x9, 40)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#5P是他们！\x01",
            "武术大会取得优胜的……\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x8, 40)
    OP_0D()

    ChrTalk(
        0x8,
        "#5P游击士那些家伙！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F#2P啊，知道就好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P老老实实让我们过去的话，\x01",
            "或许还可以饶你们一命。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P不、不要小看了我们！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P我们的防守坚如铁壁，\x01",
            "能破的了就破来试试看！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1051():
        OP_6D(-50570, 0, 20000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1051)
    SetChrChipByIndex(0x8, 41)

    def lambda_106E():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_106E)
    Sleep(50)
    SetChrChipByIndex(0x8, 41)

    def lambda_108D():
        OP_92(0xFE, 0x102, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_108D)

    def lambda_10A2():
        OP_8E(0xFE, 0xFFFF3878, 0x0, 0x9A92, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_10A2)
    Sleep(50)

    def lambda_10C2():
        OP_92(0xFE, 0x8, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10C2)
    Sleep(50)

    def lambda_10DC():
        OP_92(0xFE, 0x9, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10DC)
    Sleep(300)
    OP_44(0x101, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    Battle(0x3AE, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_111D"),
        (SWITCH_DEFAULT, "loc_1120"),
    )


    label("loc_111D")

    OP_B4(0x0)
    Return()

    label("loc_1120")

    SetChrSubChip(0x8, 0)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x8, -48300, 0, 18410, 90)
    SetChrPos(0x9, -48500, 0, 17000, 135)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
    SetChrChipByIndex(0x8, 25)
    SetChrChipByIndex(0x9, 25)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    SetChrPos(0x101, -50450, 0, 17110, 0)
    SetChrPos(0x108, -50450, 0, 17110, 0)
    SetChrPos(0x102, -50450, 0, 17110, 0)
    OP_51(0x101, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x108, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x108, 0)
    OP_6D(-50450, 0, 17110, 0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_4_D67 end

    def Function_5_1203(): pass

    label("Function_5_1203")

    SetMapFlags(0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_139C")
    OP_A2(0x655)
    EventBegin(0x0)
    OP_8B(0x0, 0xFFFF38FA, 0x5604, 0x190)
    OP_8B(0x1, 0xFFFF38FA, 0x5604, 0x190)
    OP_8B(0x2, 0xFFFF38FA, 0x5604, 0x190)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上着锁，无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#000F唉～怎么会这样！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F真是相当坚固的锁呢……\x01",
            "得先找到钥匙才行呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_134E")

    ChrTalk(
        0x108,
        (
            "#070F唔，\x01",
            "那就只能暂时先到别的地方看看了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1397")

    label("loc_134E")


    ChrTalk(
        0x108,
        (
            "#070F唔，\x01",
            "去问问那个年轻的管家吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4C, 0x1, 0x8)

    label("loc_1397")

    EventEnd(0x1)
    Jump("loc_1424")

    label("loc_139C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_END)), "loc_13E9")
    OP_8B(0x0, 0xFFFF38FA, 0x5604, 0x190)
    OP_A2(0x658)
    OP_71(0x1, 0x10)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "使用了备用钥匙。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_64(0x0, 0x1)
    Jump("loc_1424")

    label("loc_13E9")

    OP_8B(0x0, 0xFFFF38FA, 0x5604, 0x190)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上着锁，无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1424")

    ClearMapFlags(0x80)
    Return()

    # Function_5_1203 end

    def Function_6_142A(): pass

    label("Function_6_142A")

    EventBegin(0x0)
    OP_6D(-20, 0, 54380, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(1760, 0)
    OP_6C(57000, 0)
    OP_6E(500, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x10, 50, 250, 68860, 180)
    SetChrPos(0xD, 6240, 0, 63940, 11)
    SetChrPos(0xF, 3070, 0, 58560, 0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x108, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -110, 0, 50960, 0)
    SetChrPos(0x102, -110, 0, 50960, 0)
    SetChrPos(0x108, -110, 0, 50960, 0)
    SetChrPos(0xE, -110, 0, 50960, 0)
    SetChrPos(0x13, -110, 0, 50960, 0)
    SetChrPos(0x11, -110, 0, 50960, 0)
    SetChrPos(0x12, -110, 0, 50960, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)

    def lambda_158A():

        label("loc_158A")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_158A")

    QueueWorkItem2(0xD, 1, lambda_158A)

    def lambda_159B():

        label("loc_159B")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_159B")

    QueueWorkItem2(0x1E, 1, lambda_159B)

    def lambda_15AC():

        label("loc_15AC")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_15AC")

    QueueWorkItem2(0x1F, 1, lambda_15AC)

    def lambda_15BD():

        label("loc_15BD")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_15BD")

    QueueWorkItem2(0x20, 1, lambda_15BD)

    def lambda_15CE():

        label("loc_15CE")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_15CE")

    QueueWorkItem2(0x21, 1, lambda_15CE)

    def lambda_15DF():

        label("loc_15DF")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_15DF")

    QueueWorkItem2(0x22, 1, lambda_15DF)

    def lambda_15F0():

        label("loc_15F0")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_15F0")

    QueueWorkItem2(0x23, 1, lambda_15F0)

    def lambda_1601():

        label("loc_1601")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1601")

    QueueWorkItem2(0x24, 1, lambda_1601)

    def lambda_1612():

        label("loc_1612")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1612")

    QueueWorkItem2(0x25, 1, lambda_1612)

    def lambda_1623():

        label("loc_1623")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1623")

    QueueWorkItem2(0x26, 1, lambda_1623)

    def lambda_1634():

        label("loc_1634")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1634")

    QueueWorkItem2(0x27, 1, lambda_1634)
    OP_1F(0x50, 0x12C)
    FadeToBright(1000, 0)

    def lambda_1654():
        OP_6D(750, 0, 56890, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1654)

    def lambda_166C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_166C)

    def lambda_167E():
        OP_8E(0xFE, 0xFFFFFFC4, 0x0, 0xDFFC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_167E)
    Sleep(500)

    def lambda_169E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_169E)

    def lambda_16B0():
        OP_8E(0xFE, 0x302, 0x0, 0xDBEC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16B0)
    Sleep(500)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_16E7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_16E7)

    def lambda_16F9():
        OP_8E(0xFE, 0xFFFFFC4A, 0x0, 0xDA34, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_16F9)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x101, 65535)

    def lambda_171E():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_171E)
    WaitChrThread(0x102, 0x1)
    SetChrChipByIndex(0x102, 65535)

    def lambda_1736():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1736)
    WaitChrThread(0x108, 0x1)
    SetChrChipByIndex(0x108, 65535)

    def lambda_174E():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_174E)
    WaitChrThread(0x101, 0x3)

    def lambda_1761():
        OP_6D(2460, 0, 58180, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1761)
    TurnDirection(0xF, 0x101, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0xF,
        "#143F你、你们……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F呀呵～我们来救你们了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F奈尔先生，\x01",
            "看起来您安然无恙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#144F来救我们的，真的！？\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "女孩的声音",
        "艾丝蒂尔、约修亚。\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "女孩的声音",
        "没想到能在这里相会……\x02",
    )

    CloseMessageWindow()

    def lambda_187A():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_187A)
    Sleep(100)

    def lambda_188D():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_188D)
    Sleep(100)
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        "#004F……咦？\x02",
    )

    CloseMessageWindow()

    def lambda_18BC():
        OP_6D(70, 250, 68760, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18BC)

    def lambda_18D4():
        OP_67(0, 4420, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_18D4)

    def lambda_18EC():
        OP_6C(21000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_18EC)
    Sleep(1500)

    def lambda_1901():
        OP_8E(0xFE, 0xFFFFFDE4, 0x0, 0x1041E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1901)
    Sleep(100)

    def lambda_1921():
        OP_8E(0xFE, 0x1EA, 0x0, 0x1041E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1921)
    Sleep(300)

    def lambda_1941():
        OP_8E(0xFE, 0xFFFFF6E6, 0x0, 0x10266, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1941)
    Sleep(100)

    def lambda_1961():
        OP_8E(0xFE, 0x8AC, 0x0, 0x10568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1961)

    def lambda_197C():

        label("loc_197C")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_197C")

    QueueWorkItem2(0x101, 0, lambda_197C)

    def lambda_198D():

        label("loc_198D")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_198D")

    QueueWorkItem2(0x102, 0, lambda_198D)

    def lambda_199E():

        label("loc_199E")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_199E")

    QueueWorkItem2(0x108, 1, lambda_199E)

    def lambda_19AF():

        label("loc_19AF")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_19AF")

    QueueWorkItem2(0xF, 1, lambda_19AF)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#501F您、您就是公主殿下吧。\x02\x03",
            "#001F初次见面。\x01",
            "我们是游击士协会的……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "身着礼服的女孩",
        (
            "#406F不是初次见面呢。\x02\x03",
            "#401F艾丝蒂尔、约修亚。\x01",
            "终于按照约定再会了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F咦……\x02\x03",
            "……………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F#3S啊啊，你不是科洛丝吗！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    NpcTalk(
        0x10,
        "科洛丝",
        (
            "#405F艾丝蒂尔你真是的。\x02\x03",
            "虽然没有立刻察觉，\x01",
            "但也不至于那么惊讶嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F话、话虽这么说，\x01",
            "可是身着礼服、长发披肩……\x02\x03",
            "#501F究竟是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F……对不起呢，科洛丝。\x02\x03",
            "艾丝蒂尔这个人思想比较单纯。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F我说！\x01",
            "你那是什～么意思！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "科洛丝",
        (
            "#466F呵呵……\x01",
            "我认为那是艾丝蒂尔的一个优点哦。\x02\x03",
            "#401F对了，约修亚。\x02\x03",
            "你还称呼我……那个名字啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，我觉得你也是这么希望的吧。\x01",
            "　\x02\x03",
            "如果你介意的话，我还是称呼本名吧？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "科洛丝",
        (
            "#408F怎么会呢……\x01",
            "谢谢呢，我真的好开心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F？？？\x02\x03",
            "话说回来……\x01",
            "为什么科洛丝会在这里呢？\x02\x03",
            "还有，公主殿下不是应该在这的吗？\x01",
            "为什么到处都没有看见呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#145F我说啊，不就在你的面前吗。\x02\x03",
            "这位就是女王陛下的孙女，\x01",
            "科洛蒂娅公主殿下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F…………哦。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_20(0x7D0)
    OP_44(0x101, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xD, 0x0)

    def lambda_1E52():
        OP_67(0, 6000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E52)
    OP_6C(45000, 1500)
    Sleep(500)
    OP_63(0x101)
    Sleep(400)

    ChrTalk(
        0x101,
        "#005F#5S#2P啊啊啊啊啊啊？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_6E(480, 0)
    OP_44(0x108, 0xFF)
    OP_44(0xF, 0xFF)
    CloseMessageWindow()
    OP_1D(0x11)

    NpcTalk(
        0x10,
        "科洛蒂娅公主",
        (
            "#466F对不起呢，我一直没说……\x02\x03",
            "#405F我本来打算和艾丝蒂尔你们\x01",
            "在王都再会的时候告诉你们的……\x01",
            "　\x02\x03",
            "结果被理查德上校掳走了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F可、可是，为什么？\x02\x03",
            "为什么公主殿下会隐藏身份\x01",
            "在王立学院念书呢……！？\x02\x03",
            "而、而且我们称呼你科洛丝，\x01",
            "这样可以吗……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "科洛蒂娅公主",
        (
            "#406F以后也请一如既往地叫我科洛丝。\x01",
            "　\x02\x03",
            "科洛蒂娅·冯·奥赛雷丝……\x02\x03",
            "#401F其实，我的全名的开始和末尾相结合\x01",
            "就是我的爱称了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F是这样的啊……\x02\x03",
            "嗯，那么头发呢？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "科洛蒂娅公主",
        (
            "#400F啊，这是假发。\x02\x03",
            "如果真的是这种发型，\x01",
            "在学院里面读书就不太方便了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#141F我也有够粗心的了……\x02\x03",
            "虽然以前看过您的照片，\x01",
            "但在市长官邸事件中见到您时\x01",
            "竟然完全没有注意到……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "科洛蒂娅公主",
        (
            "#466F呵呵，对不起。\x02\x03",
            "杜南王叔和戴尔蒙市长都没有察觉，\x01",
            "真是有些意外的效果呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F哦，说起来，\x01",
            "那个公爵还是你的亲戚呢。\x02\x03",
            "#004F嗯，对了。\x01",
            "最重要的事情反而忘记了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们把至今为止的事情经过一一道来，\x01",
            "也说明了接受女王的委托前来营救的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    NpcTalk(
        0x10,
        "科洛蒂娅公主",
        (
            "#404F是这样啊……\x02\x03",
            "#403F艾丝蒂尔、约修亚，\x01",
            "还有那位金先生……\x02\x03",
            "#406F你们能来营救我们，\x01",
            "我发自内心地感谢你们的恩德。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊哈哈，怎么又客气起来了呢。\x02\x03",
            "如果知道被掳走的是科洛丝的话，\x01",
            "就算不委托我们也会来的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "科洛蒂娅公主",
        "#405F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F的确如此呢。\x02\x03",
            "#010F不过，相比之下，\x01",
            "我觉得你要感谢的应该是陛下才对。\x02\x03",
            "她不顾自己所处的不利境况，\x01",
            "也要委托我们来营救你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#074F的确，公主殿下既然已经平安无事，\x01",
            "那么陛下就可以拒绝上校的要求了……\x02\x03",
            "#072F也许陛下已经视死如归了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x108, 400)

    NpcTalk(
        0x10,
        "科洛蒂娅公主",
        (
            "#403F是的……\x01",
            "祖母大人就是那样的。\x02\x03",
            "无论如何也不会妥协，\x01",
            "可是这样祖母大人她……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xD, -230, 0, 55310, 346)
    SetChrChipByIndex(0x8, 37)
    SetChrFlags(0x8, 0x1)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xC, 1020, 0, 56140, 0)
    SetChrPos(0x8, 50, 0, 54770, 0)
    OP_20(0x5DC)

    NpcTalk(
        0xC,
        "男人的声音",
        (
            "#1P所谓闹剧，\x01",
            "就是这个样子的吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_21()

    def lambda_2707():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2707)

    def lambda_2715():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2715)

    def lambda_2723():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2723)

    def lambda_2731():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2731)

    def lambda_273F():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_273F)

    def lambda_274D():
        OP_6D(680, 0, 60840, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_274D)

    def lambda_2765():
        OP_6E(500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2765)
    Sleep(500)
    OP_1D(0x56)
    Sleep(1500)

    ChrTalk(
        0xD,
        "#6P公、公主殿下～……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "科洛蒂娅公主",
        "#407F小莉安妮！？\x02",
    )

    CloseMessageWindow()

    def lambda_27BA():
        OP_6D(850, 0, 60760, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_27BA)

    def lambda_27D2():
        OP_6E(450, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_27D2)
    SetChrChipByIndex(0x101, 0)

    def lambda_27E7():
        OP_8E(0xFE, 0xFFFFFDEE, 0x0, 0xEF4C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27E7)
    Sleep(200)
    SetChrChipByIndex(0x102, 2)

    def lambda_280C():
        OP_8E(0xFE, 0x258, 0x0, 0xF19A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_280C)
    Sleep(100)
    SetChrChipByIndex(0x108, 4)

    def lambda_2831():
        OP_8E(0xFE, 0xFFFFF754, 0x0, 0xF1B8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2831)
    Sleep(200)

    def lambda_2851():
        OP_8E(0xFE, 0xA, 0x0, 0xF820, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2851)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        "#580F那、那个小女孩是谁！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x1)

    NpcTalk(
        0x10,
        "科洛蒂娅公主",
        (
            "#403F是摩尔根将军的孙女……\x02\x03",
            "为了威逼被软禁在哈肯大门的将军就范，\x01",
            "小莉安妮也被带到这里来了……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F为了要挟陛下而将公主殿下带到这里，\x01",
            "你们对付所有掌权者都是用同一种手段。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2P你说得完全没错……\x01",
            "不过，别以为这是单纯的威胁哦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2P我们情报部的队员，为了理想，\x01",
            "就算化成鬼、化成修罗也在所不惜！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F这、这种事还有脸自吹自擂！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "科洛蒂娅公主",
        (
            "#402F中队长，我想和你做个交易。\x02\x03",
            "请让我代替那个孩子，作为人质。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2P哦……\x01",
            "我才不会上当呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2P对于我们这些人而言，\x01",
            "是没有亲手杀死王族成员的勇气的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2P与之相比，\x01",
            "摩尔根将军的孙女就要好办得多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2P既有作为人质的价值，\x01",
            "要打伤她又不会很难下手。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "科洛蒂娅公主",
        "#407F……你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F……无耻～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#075F哎呀呀，无可救药的家伙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#2P哼，随便你们怎么胡说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2P到王都执勤的巡回部队\x01",
            "很快就要从空中庭园归来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2P到时候会把亲卫队还有游击士\x01",
            "在这儿一网打尽！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x12,
        "女性的声音",
        "#1P啊～那已经不可能了哦。\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x12,
        "女性的声音",
        (
            "#1P他们在来这里的途中\x01",
            "就已经被我们全部消灭了。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2DF8():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2DF8)

    def lambda_2E06():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2E06)

    def lambda_2E14():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2E14)

    def lambda_2E22():
        OP_6D(500, 0, 59390, 800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2E22)
    OP_6E(500, 800)

    def lambda_2E43():

        label("loc_2E43")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_2E43")

    QueueWorkItem2(0xC, 1, lambda_2E43)

    def lambda_2E54():

        label("loc_2E54")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_2E54")

    QueueWorkItem2(0x8, 1, lambda_2E54)

    def lambda_2E65():

        label("loc_2E65")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_2E65")

    QueueWorkItem2(0xD, 1, lambda_2E65)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0x12, 0x20)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x12, 16)
    ClearChrFlags(0x12, 0x80)
    OP_1D(0x2F)

    def lambda_2E9C():

        label("loc_2E9C")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2E9C")

    QueueWorkItem2(0x12, 1, lambda_2E9C)
    OP_96(0x12, 0xFFFFF7A4, 0x0, 0xD5C0, 0x3E8, 0x1F40)
    OP_22(0x1F6, 0x0, 0x64)
    OP_99(0x12, 0x2, 0x4, 0xBB8)
    PlayEffect(0x8, 0xFF, 0xFF, 50, 1000, 54770, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    TurnDirection(0x8, 0x12, 0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 43)

    def lambda_2F1E():
        OP_94(0x1, 0xFE, 0xB4, 0xBB8, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2F1E)
    OP_99(0x12, 0x4, 0x9, 0xBB8)
    OP_44(0xD, 0xFF)
    OP_44(0x8, 0xFF)

    ChrTalk(
        0x8,
        "#10A啊！\x05\x02",
    )

    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 42)
    OP_22(0x20C, 0x0, 0x64)

    def lambda_2F65():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2F65)
    Sleep(500)

    def lambda_2F7A():
        OP_8E(0xFE, 0xFFFFF4DE, 0x0, 0xD912, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2F7A)
    Sleep(100)
    OP_8F(0xC, 0x6CC, 0x0, 0xDACA, 0x1388, 0x0)
    WaitChrThread(0xD, 0x1)
    OP_96(0x12, 0xFFFFF858, 0x0, 0xDA16, 0x1F4, 0x1F40)
    TurnDirection(0xD, 0x12, 400)
    Sleep(200)

    ChrTalk(
        0xC,
        "#2P什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#3P呜……呜呜……\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0xD,
        "#3S#3P呜哇哇啊啊啊啊啊啊！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_3037():

        label("loc_3037")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_3037")

    QueueWorkItem2(0x101, 1, lambda_3037)

    def lambda_3048():

        label("loc_3048")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_3048")

    QueueWorkItem2(0x102, 1, lambda_3048)

    def lambda_3059():

        label("loc_3059")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_3059")

    QueueWorkItem2(0x108, 1, lambda_3059)

    def lambda_306A():

        label("loc_306A")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_306A")

    QueueWorkItem2(0xF, 1, lambda_306A)

    def lambda_307B():

        label("loc_307B")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_307B")

    QueueWorkItem2(0x10, 1, lambda_307B)

    ChrTalk(
        0x12,
        "#021F#5P乖～乖～已经没事了哦。\x02",
    )

    CloseMessageWindow()
    OP_44(0x12, 0xFF)
    OP_8C(0x12, 45, 400)

    ChrTalk(
        0x12,
        (
            "#020F艾丝蒂尔、约修亚。\x01",
            "真是好久不见了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F雪、雪拉姐！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F终于来了吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2P哪、哪里有这么\x01",
            "慢条斯理的打招呼的！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "青年的声音",
        "#1P哈·哈·哈。简直不解风情呢。\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp008_00.eff")
    SetChrPos(0x28, 1590, 1000, 54930, 0)
    PlayEffect(0x0, 0xFF, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x28, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x8, 0xFF, 0xFF, 1590, 1000, 54930, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 18)

    def lambda_3240():
        OP_96(0xFE, 0xBD6, 0x0, 0xDFFC, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3240)

    ChrTalk(
        0xC,
        "#10A呜哦……\x05\x02",
    )

    Sleep(400)

    def lambda_3273():

        label("loc_3273")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_3273")

    QueueWorkItem2(0x12, 1, lambda_3273)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x12, 90, 0)

    def lambda_3296():
        OP_96(0xFE, 0x442, 0x0, 0xDDCC, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3296)
    Sleep(200)
    OP_22(0x1F6, 0x0, 0x64)
    OP_99(0x12, 0x2, 0x4, 0xFA0)
    PlayEffect(0x8, 0xFF, 0xFF, 3180, 1500, 56940, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xC, 0x4)

    def lambda_3301():
        OP_6D(6320, 0, 57730, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3301)

    def lambda_3319():
        OP_8F(0xFE, 0x2508, 0x1F4, 0xDCE6, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3319)
    OP_99(0x12, 0x4, 0x9, 0x7D0)
    WaitChrThread(0xC, 0x1)
    OP_22(0x8E, 0x0, 0x64)
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 17)

    ChrTalk(
        0xC,
        "#10A呜啊！\x05\x02",
    )

    PlayEffect(0x12, 0xFF, 0xC, 0, 0, -500, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_6B(1800, 0)
    OP_6B(1760, 80)
    Sleep(500)
    OP_8F(0xC, 0x2512, 0x0, 0xDCE6, 0x3E8, 0x0)
    OP_22(0x20C, 0x0, 0x64)
    OP_99(0xC, 0x0, 0x3, 0x7D0)

    ChrTalk(
        0x12,
        "#027F#5P刚才那是附赠品哦。\x02",
    )

    CloseMessageWindow()
    OP_6D(280, 0, 59100, 2000)

    ChrTalk(
        0x101,
        (
            "#509F好、好狠啊～\x02\x03",
            "#004F咦，刚才发起攻击的是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F……奥利维尔吗？\x02",
    )

    CloseMessageWindow()
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x12, 14)
    TurnDirection(0x12, 0x13, 400)
    OP_22(0xA6, 0x0, 0x64)

    NpcTalk(
        0x13,
        "青年的声音",
        "#1PBingo⊙\x02",
    )

    CloseMessageWindow()

    def lambda_34B6():

        label("loc_34B6")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_34B6")

    QueueWorkItem2(0x12, 1, lambda_34B6)

    def lambda_34C7():

        label("loc_34C7")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_34C7")

    QueueWorkItem2(0xD, 1, lambda_34C7)

    def lambda_34D8():

        label("loc_34D8")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_34D8")

    QueueWorkItem2(0x101, 1, lambda_34D8)

    def lambda_34E9():

        label("loc_34E9")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_34E9")

    QueueWorkItem2(0x102, 1, lambda_34E9)

    def lambda_34FA():

        label("loc_34FA")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_34FA")

    QueueWorkItem2(0x108, 1, lambda_34FA)

    def lambda_350B():

        label("loc_350B")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_350B")

    QueueWorkItem2(0xF, 1, lambda_350B)

    def lambda_351C():

        label("loc_351C")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_351C")

    QueueWorkItem2(0x10, 1, lambda_351C)
    ClearChrFlags(0x13, 0x80)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_353D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_353D)

    def lambda_354F():
        OP_8E(0xFE, 0x1E, 0x0, 0xD7F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_354F)
    Sleep(100)
    OP_6D(550, 0, 58110, 2000)

    ChrTalk(
        0x13,
        (
            "#031F哎呀呀。主角华丽登场了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)

    def lambda_35FD():
        OP_8E(0xFE, 0xFFFFFC18, 0x0, 0xDF34, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_35FD)
    Sleep(200)
    SetChrChipByIndex(0x102, 65535)

    def lambda_3622():
        OP_8E(0xFE, 0xF0, 0x0, 0xE2C2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3622)
    Sleep(200)
    SetChrChipByIndex(0x108, 65535)

    def lambda_3647():
        OP_8E(0xFE, 0xFFFFF830, 0x0, 0xE25E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_3647)
    Sleep(300)

    def lambda_3667():
        OP_8E(0xFE, 0x78, 0x0, 0xE90C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3667)
    Sleep(200)

    def lambda_3687():
        OP_8E(0xFE, 0x9A6, 0x0, 0xE902, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_3687)
    OP_44(0x12, 0xFF)
    OP_20(0x5DC)
    OP_21()
    OP_1D(0x11)

    ChrTalk(
        0x108,
        (
            "#071F哈哈哈……\x01",
            "这不是那位怪腔怪调的兄弟吗。\x02\x03",
            "#070F对了，雪拉扎德，\x01",
            "真是好久不见了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 270, 400)

    ChrTalk(
        0x12,
        (
            "#021F#2P你好，久疏问候了。\x02\x03",
            "#020F没想到金先生你也到利贝尔来了呢。\x01",
            "　\x02\x03",
            "听说你和艾丝蒂尔他们在一起时，\x01",
            "我就没有那么担心了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哈哈，你真是太抬举我了。\x01",
            "　\x02\x03",
            "#071F不过我说你啊……\x01",
            "没见一段日子，越来越有魅力了呢。\x02\x03",
            "说实话，我都有些认不出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#520F#2P哎、哎呀，真的吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x12, 400)
    Sleep(200)
    TurnDirection(0x13, 0x108, 400)
    Sleep(200)
    TurnDirection(0x13, 0x12, 400)

    ChrTalk(
        0x13,
        (
            "#032F哼·哼·哼，我好生嫉妒。\x01",
            "　\x02\x03",
            "#034F在把我尽情地享用完之后，\x01",
            "又像垃圾一样抛弃了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x13, 400)

    ChrTalk(
        0x12,
        (
            "#027F#2P哎哟，我说奥利维尔，\x01",
            "你不是已经和爱娜她搭上了吗？\x02\x03",
            "还想一脚踏两只船啊？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x102, 400)

    ChrTalk(
        0x13,
        (
            "#034F哈·哈·哈，对不起～啦。\x01",
            "人家～开玩笑的～啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F还真是的……\x01",
            "大家都还是老样子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F可是雪拉姐姐怎么来到王都的呢？\x01",
            "　\x02\x03",
            "王国军不是把关所全部封锁了吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)

    def lambda_3AC0():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AC0)
    TurnDirection(0x12, 0x102, 400)

    ChrTalk(
        0x12,
        (
            "#021F#2P嗯，所以我们是乘着小船\x01",
            "从瓦雷利亚湖渡过来的。\x02\x03",
            "然后在王都的码头上岸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F原来如此，真是深思熟虑……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F可是可是，你为什么又会\x01",
            "和这个骗吃骗喝的大赖皮蛋在一起呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BBD():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3BBD)

    ChrTalk(
        0x12,
        (
            "#025F#2P我刚踏出王都的协会就撞见他了。\x01",
            "　\x02\x03",
            "他死皮赖脸地跟着我，甩都甩不掉，\x01",
            "没办法之下，我就只有带他来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#031F哈·哈·哈。\x02\x03",
            "如此有趣好玩的事情，\x01",
            "怎能缺少了我这位天才演奏家的参与呢。\x02\x03",
            "#030F对了，那位小姐是……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    OP_44(0x101, 0xFF)

    def lambda_3CFF():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3CFF)
    OP_8E(0x102, 0x3AC, 0x0, 0xE36C, 0x7D0, 0x0)
    TurnDirection(0x102, 0x10, 400)
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        (
            "#006F啊，我给大家介绍一下。\x02\x03",
            "她是女王陛下的孙女科洛蒂娅公主殿下。\x01",
            "　\x02\x03",
            "是我和约修亚的朋友。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3DB2():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DB2)

    def lambda_3DC0():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3DC0)
    OP_44(0x10, 0xFF)

    NpcTalk(
        0x10,
        "科洛蒂娅公主",
        (
            "#401F两位，初次见面。\x02\x03",
            "非常感谢你们两位刚才的协助。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#021F#2P别客气，这也是游击士的义务嘛。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#035F哈·哈·哈。\x01",
            "拯救美丽的公主是绅士的无上荣誉呢。\x02\x03",
            "#030F能见到公主您，是我的光荣。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x11, -110, 0, 50960, 0)
    SetChrPos(0xE, -110, 0, 50960, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(
        0x11,
        "女性的声音",
        "#1P科洛丝，你没事吧！\x02",
    )

    CloseMessageWindow()

    def lambda_3FA9():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3FA9)

    def lambda_3FB7():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FB7)

    def lambda_3FC5():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3FC5)

    def lambda_3FD3():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3FD3)

    def lambda_3FE1():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3FE1)

    def lambda_3FEF():
        OP_8F(0xFE, 0x4A6, 0x0, 0xD9EE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3FEF)

    def lambda_400A():
        OP_8F(0xFE, 0xFFFFF948, 0x0, 0xDEF8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_400A)
    Sleep(500)

    def lambda_402A():

        label("loc_402A")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_402A")

    QueueWorkItem2(0x101, 1, lambda_402A)

    def lambda_403B():

        label("loc_403B")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_403B")

    QueueWorkItem2(0x102, 1, lambda_403B)

    def lambda_404C():

        label("loc_404C")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_404C")

    QueueWorkItem2(0x108, 1, lambda_404C)

    def lambda_405D():

        label("loc_405D")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_405D")

    QueueWorkItem2(0x13, 1, lambda_405D)

    def lambda_406E():

        label("loc_406E")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_406E")

    QueueWorkItem2(0x12, 1, lambda_406E)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x1000)
    SetChrChipByIndex(0x11, 44)

    def lambda_408E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_408E)

    def lambda_40A0():
        OP_8E(0xFE, 0xFFFFFEA2, 0x0, 0xDF7A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_40A0)
    Sleep(500)
    OP_22(0x8C, 0x0, 0x64)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xE, 0x4)

    def lambda_40D4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_40D4)

    def lambda_40E6():
        OP_8E(0xFE, 0x33E, 0x0, 0xE8C6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_40E6)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 45)
    SetChrSubChip(0x11, 2)
    WaitChrThread(0xE, 0x1)
    OP_43(0xE, 0x1, 0x0, 0x7)
    OP_A2(0x0)

    NpcTalk(
        0x10,
        "科洛蒂娅公主",
        "#409F尤莉亚，基库！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "啾！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A5(0x0)
    OP_97(0xE, 0x82, 0xE8C6, 0xFFFEA070, 0x1388, 0x1)
    OP_97(0xE, 0x82, 0xE8C6, 0xFFFEA070, 0xBB8, 0x1)
    SetChrFlags(0xE, 0x20)

    def lambda_418E():

        label("loc_418E")

        OP_99(0xFE, 0x0, 0x7, 0x1388)
        OP_48()
        Jump("loc_418E")

    QueueWorkItem2(0xE, 2, lambda_418E)

    def lambda_41A1():
        OP_8F(0xFE, 0xFFFFFD26, 0x258, 0xE0C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_41A1)
    OP_8C(0xE, 45, 100)
    WaitChrThread(0xE, 0x1)

    def lambda_41C8():
        OP_8F(0xFE, 0xFFFFFD26, 0x0, 0xE0C4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_41C8)
    WaitChrThread(0xE, 0x1)
    OP_44(0xE, 0x2)
    Fade(500)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 36)
    SetChrSubChip(0x11, 1)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "#311F#5P啾啾！\x02\x03",
            "啾——啾！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "科洛蒂娅公主",
        (
            "#408F呵呵，太好了。\x01",
            "你们也平安无事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#171F#2P殿下，您平安无事就好……\x02\x03",
            "真的……真的太好了……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "科洛蒂娅公主",
        (
            "#401F尤莉亚你也是……\x01",
            "还是那么精神焕发呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，艾丝蒂尔他们带着科洛丝\x01",
            "和伪装行动的游击士还有亲卫队队员汇合了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "安顿好其他的人质之后，\x01",
            "众人决定一起商讨对策以确认当前的状况。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_1B(0x0, 0x0, 0xFFFF)
    OP_28(0x4B, 0x4, 0x10)
    OP_28(0x4C, 0x4, 0x10)
    OP_28(0x4C, 0x1, 0x40)
    OP_28(0x4C, 0x1, 0x80)
    OP_28(0x4C, 0x1, 0x100)
    OP_28(0x4D, 0x4, 0x2)
    OP_28(0x4D, 0x4, 0x4)
    OP_28(0x4D, 0x1, 0x1)
    OP_28(0x4D, 0x1, 0x2)
    OP_20(0x5DC)
    OP_21()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_142A end

    def Function_7_4438(): pass

    label("Function_7_4438")

    OP_A6(0x0)

    label("loc_443B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_445C")
    OP_97(0xFE, 0x82, 0xE8C6, 0xFFFA81C0, 0x1388, 0x1)
    OP_48()
    Jump("loc_443B")

    label("loc_445C")

    OP_A3(0x0)
    Return()

    # Function_7_4438 end

    def Function_8_4460(): pass

    label("Function_8_4460")

    EventBegin(0x0)
    OP_6D(1040, 130, 67720, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(44000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x11, -40, 250, 70880, 180)
    SetChrPos(0x102, -2410, 0, 67020, 45)
    SetChrPos(0x13, -3610, 0, 67070, 61)
    SetChrPos(0x108, -3890, 0, 68290, 80)
    SetChrPos(0x101, 2540, 0, 67490, 320)
    SetChrPos(0x10, 1280, 0, 67070, 2)
    SetChrPos(0x12, 2980, 0, 66110, 297)
    SetChrPos(0x14, -730, 0, 65269, 0)
    SetChrPos(0x16, 180, 0, 64510, 0)
    SetChrPos(0x15, -950, 0, 63940, 0)
    SetChrPos(0x17, -2170, 0, 64410, 0)
    SetChrPos(0x18, -1770, 0, 61620, 0)
    SetChrPos(0x18, 70, 0, 61620, 0)
    SetChrPos(0x18, 1840, 0, 61620, 0)
    SetChrPos(0x18, -1770, 0, 59790, 0)
    SetChrPos(0x18, 70, 0, 59790, 0)
    SetChrPos(0x18, 1840, 0, 59790, 0)
    SetChrChipByIndex(0x10, 24)

    ChrTalk(
        0x11,
        (
            "#170F现在我就对解放格兰赛尔城\x01",
            "和营救女王陛下的作战进行说明。\x02\x03",
            "首先，由约修亚君等\x01",
            "三人为一组从地下水路\x01",
            "攻入格兰赛尔城的地下。\x02\x03",
            "然后迅速赶往亲卫队值勤室\x01",
            "将城门的开关装置启动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F嗯，巨大的烟花\x01",
            "就要开始燃放了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#030F哼哼……不管怎样，\x01",
            "最后一幕终于开演了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#170F在城门打开的同时，\x01",
            "全体亲卫队员以及四名\x01",
            "游击士就从市街区冲进城内。\x02\x03",
            "尽量制造草木皆兵的效果，\x01",
            "将敌人全部引入城内集中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "好的，交给我们去办吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "太好了，我已经跃跃欲试了！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 400)

    ChrTalk(
        0x11,
        (
            "#170F最后还要说的是……\x02\x03",
            "……殿下，您真的\x01",
            "下决心要参战吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#040F抱歉……\x01",
            "我一定要救出祖母大人。\x02\x03",
            "而且，\x01",
            "我还会操纵飞行艇……\x02\x03",
            "没有不让我\x01",
            "参战的道理吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#170F唉……\x02\x03",
            "如果早知道会发生这样的事情，\x01",
            "当初就不会教你操纵飞艇的方法了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F不用担心啦，尤莉亚中尉。\x02\x03",
            "科洛丝就交给\x01",
            "我们来照顾吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#020F我以『银闪』之名作为赌注，\x01",
            "发誓一定会保护公主的安全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#170F我知道了……拜托你们了。\x02\x03",
            "在将敌人的兵力集中于城内之后，\x01",
            "艾丝蒂尔等三人为一组就乘坐\x01",
            "特务飞行艇在空中庭园强行着陆。\x02\x03",
            "然后就冲入女王宫\x01",
            "救出艾莉茜雅女王陛下。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)

    ChrTalk(
        0x11,
        (
            "#170F正午钟响的同时开始作战——\x01",
            "在此之前请在各自的地点等候。\x02\x03",
            "……全体听命，行动开始！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "明白！\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_A2(0x3FD)
    NewScene("ED6_DT01/T4300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_4460 end

    def Function_9_4C64(): pass

    label("Function_9_4C64")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CD0")

    ChrTalk(
        0x101,
        (
            "#002F还没有完成女王陛下的委托呢。\x01",
            "　\x02\x03",
            "快点把公主殿下找出来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DAB")

    label("loc_4CD0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D3B")

    ChrTalk(
        0x102,
        (
            "#012F等把人质都解放了，\x01",
            "再离开这里吧。\x02\x03",
            "总之要先把里面彻底调查一番。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DAB")

    label("loc_4D3B")


    ChrTalk(
        0x108,
        (
            "#072F还没有找到公主殿下和其他人质呢。\x01",
            "　\x02\x03",
            "先把那些坏家伙们\x01",
            "一个不留地干掉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DAB")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_9_4C64 end

    SaveToFile()

Try(main)
