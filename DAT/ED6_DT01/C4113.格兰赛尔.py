from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4113   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4113.x',
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
        '卡露娜',                               # 11
        '亚妮拉丝',                             # 12
        '库拉茨',                               # 13
        '克鲁茨',                               # 14
        '尤莉亚中尉',                           # 15
        '亲卫队员',                             # 16
        '亲卫队员',                             # 17
        '亲卫队员',                             # 18
        '亲卫队员',                             # 19
        '亲卫队员',                             # 20
        '亲卫队员',                             # 21
        '亲卫队员',                             # 22
        '亲卫队员',                             # 23
        '中队长',                               # 24
        '特务兵',                               # 25
        '特务兵',                               # 26
        '特务兵',                               # 27
        '特务兵',                               # 28
        '特务兵',                               # 29
        '特务兵',                               # 30
        '特务兵',                               # 31
        '特务兵',                               # 32
        '特务兵',                               # 33
        '特务兵',                               # 34
        '军用犬',                               # 35
        '军用犬',                               # 36
        '军用犬',                               # 37
        '军用犬',                               # 38
        '军用犬',                               # 39
        '修理员佩顿',                           # 40
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
        'ED6_DT07/CH01610 ._CH',             # 00
        'ED6_DT07/CH00400 ._CH',             # 01
        'ED6_DT07/CH00420 ._CH',             # 02
        'ED6_DT07/CH00390 ._CH',             # 03
        'ED6_DT07/CH00410 ._CH',             # 04
        'ED6_DT07/CH02090 ._CH',             # 05
        'ED6_DT07/CH01320 ._CH',             # 06
        'ED6_DT07/CH01610 ._CH',             # 07
        'ED6_DT07/CH00340 ._CH',             # 08
        'ED6_DT07/CH00341 ._CH',             # 09
        'ED6_DT09/CH10060 ._CH',             # 0A
        'ED6_DT09/CH10061 ._CH',             # 0B
        'ED6_DT06/CH20042 ._CH',             # 0C
        'ED6_DT07/CH01450 ._CH',             # 0D
        'ED6_DT06/CH20114 ._CH',             # 0E
        'ED6_DT06/CH20115 ._CH',             # 0F
        'ED6_DT06/CH20116 ._CH',             # 10
        'ED6_DT06/CH20117 ._CH',             # 11
        'ED6_DT07/CH00344 ._CH',             # 12
        'ED6_DT07/CH00440 ._CH',             # 13
        'ED6_DT07/CH00441 ._CH',             # 14
        'ED6_DT07/CH01790 ._CH',             # 15
        'ED6_DT07/CH00502 ._CH',             # 16
        'ED6_DT07/CH00510 ._CH',             # 17
        'ED6_DT07/CH00511 ._CH',             # 18
        'ED6_DT07/CH00442 ._CH',             # 19
    )

    AddCharChipPat(
        'ED6_DT07/CH01610P._CP',             # 00
        'ED6_DT07/CH00400P._CP',             # 01
        'ED6_DT07/CH00420P._CP',             # 02
        'ED6_DT07/CH00390P._CP',             # 03
        'ED6_DT07/CH00410P._CP',             # 04
        'ED6_DT07/CH02090P._CP',             # 05
        'ED6_DT07/CH01320P._CP',             # 06
        'ED6_DT07/CH01610P._CP',             # 07
        'ED6_DT07/CH00340P._CP',             # 08
        'ED6_DT07/CH00341P._CP',             # 09
        'ED6_DT09/CH10060P._CP',             # 0A
        'ED6_DT09/CH10061P._CP',             # 0B
        'ED6_DT06/CH20042P._CP',             # 0C
        'ED6_DT07/CH01450P._CP',             # 0D
        'ED6_DT06/CH20114P._CP',             # 0E
        'ED6_DT06/CH20115P._CP',             # 0F
        'ED6_DT06/CH20116P._CP',             # 10
        'ED6_DT06/CH20117P._CP',             # 11
        'ED6_DT07/CH00344P._CP',             # 12
        'ED6_DT07/CH00440P._CP',             # 13
        'ED6_DT07/CH00441P._CP',             # 14
        'ED6_DT07/CH01790P._CP',             # 15
        'ED6_DT07/CH00502P._CP',             # 16
        'ED6_DT07/CH00510P._CP',             # 17
        'ED6_DT07/CH00511P._CP',             # 18
        'ED6_DT07/CH00442P._CP',             # 19
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
        Y                   = 0,
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
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 131087,
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
        Unknown3            = 131089,
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
        Unknown3            = 131089,
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
        Unknown3            = 131089,
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
        Unknown3            = 131089,
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
        Unknown3            = 131089,
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
        Unknown3            = 131089,
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
        Unknown3            = 131089,
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
        Unknown3            = 131089,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
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
        X                   = 14350,
        Y                   = -1000,
        Z                   = -8640,
        Range               = 11930,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x19F0,
        Unknown_18          = 0x0,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = 44270,
        Y                   = 1000,
        Z                   = 940,
        Range               = 48410,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0xFFFFFF10,
        Unknown_18          = 0x0,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = 45450,
        Y                   = 1000,
        Z                   = 6140,
        Range               = 47430,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0x1144,
        Unknown_18          = 0x0,
        Unknown_1C          = 22,
    )


    ScpFunction(
        "Function_0_5FA",          # 00, 0
        "Function_1_62E",          # 01, 1
        "Function_2_646",          # 02, 2
        "Function_3_B08",          # 03, 3
        "Function_4_174F",         # 04, 4
        "Function_5_1782",         # 05, 5
        "Function_6_17C8",         # 06, 6
        "Function_7_180E",         # 07, 7
        "Function_8_1854",         # 08, 8
        "Function_9_1886",         # 09, 9
        "Function_10_18B8",        # 0A, 10
        "Function_11_18EB",        # 0B, 11
        "Function_12_191E",        # 0C, 12
        "Function_13_1951",        # 0D, 13
        "Function_14_1970",        # 0E, 14
        "Function_15_19A3",        # 0F, 15
        "Function_16_19D6",        # 10, 16
        "Function_17_1A09",        # 11, 17
        "Function_18_1A3C",        # 12, 18
        "Function_19_1A6F",        # 13, 19
        "Function_20_1AA2",        # 14, 20
        "Function_21_2297",        # 15, 21
        "Function_22_23FD",        # 16, 22
        "Function_23_26CF",        # 17, 23
    )


    def Function_0_5FA(): pass

    label("Function_0_5FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_611")
    OP_A3(0x3FA)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_61F")
    OP_A3(0x3FB)
    Event(0, 3)

    label("loc_61F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_62D")
    OP_A3(0x3FC)
    Event(0, 20)

    label("loc_62D")

    Return()

    # Function_0_5FA end

    def Function_1_62E(): pass

    label("Function_1_62E")

    OP_16(0x2, 0xFA0, 0xFFFEA070, 0xFFFE4698, 0x30066)
    OP_22(0x1CC, 0x1, 0x64)
    Return()

    # Function_1_62E end

    def Function_2_646(): pass

    label("Function_2_646")

    ClearMapFlags(0x2000000)
    EventBegin(0x0)
    OP_6D(45860, 0, 7990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(69000, 0)
    OP_6E(325, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 26320, 0, 2029, 270)
    SetChrPos(0x9, 26350, 0, -100, 270)
    FadeToBright(2000, 0)

    def lambda_6C5():
        OP_6C(45000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6C5)
    Sleep(2000)

    def lambda_6DA():
        OP_6E(228, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6DA)
    OP_6D(26290, 0, 960, 5000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x9, 0x20)

    ChrTalk(
        0x8,
        (
            "#5P哈啊……\x01",
            "肚子好饿啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x8,
        "#5P还没到换班时间吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        "喂喂，可别松懈。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "潜伏中的亲卫队\x01",
            "随时都有可能出现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P反正在逃中的人\x01",
            "连十个都不到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P那些家伙，上校只要想的话，\x01",
            "绝对一下就把他们给捉了。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0xE, 16180, 0, 1410, 90)
    SetChrPos(0xF, 15420, 0, 630, 90)
    SetChrPos(0x10, 15520, 0, 2230, 90)
    SetChrPos(0x11, 14270, 0, 550, 90)
    SetChrPos(0x12, 14270, 0, 2230, 90)
    SetChrSubChip(0xE, 1)
    SetChrSubChip(0xF, 2)
    SetChrSubChip(0x10, 2)
    SetChrSubChip(0x11, 2)
    SetChrSubChip(0x12, 2)
    OP_20(0x5DC)

    ChrTalk(
        0xE,
        (
            "#2P……如果你们能办得到的话，\x01",
            "就尽管来试试看。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_960():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_960)

    def lambda_96E():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_96E)

    def lambda_97C():
        OP_6E(262, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_97C)

    def lambda_98C():
        OP_6D(20430, 0, 1370, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_98C)

    def lambda_9A4():
        OP_6C(315000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9A4)
    Sleep(500)
    OP_1D(0x59)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x8,
        "#2P什……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P亲卫队中队长……\x01",
            "尤莉亚·舒华兹！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 25)
    SetChrChipByIndex(0x9, 25)
    SetChrSubChip(0x8, 0)
    SetChrSubChip(0x9, 0)
    SetChrFlags(0xE, 0x1000)
    SetChrFlags(0xF, 0x1000)
    SetChrFlags(0x10, 0x1000)
    SetChrFlags(0x11, 0x1000)
    SetChrFlags(0x12, 0x1000)
    SetChrChipByIndex(0xE, 14)

    def lambda_A4C():
        OP_94(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A4C)

    def lambda_A62():
        OP_6D(24930, 0, 1380, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A62)
    Sleep(200)
    SetChrChipByIndex(0xF, 16)
    SetChrChipByIndex(0x10, 16)
    SetChrChipByIndex(0x11, 16)
    SetChrChipByIndex(0x12, 16)

    def lambda_A93():
        OP_92(0xFE, 0x9, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A93)
    Sleep(50)

    def lambda_AAD():
        OP_92(0xFE, 0x8, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_AAD)
    Sleep(50)

    def lambda_AC7():
        OP_92(0xFE, 0x9, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_AC7)
    Sleep(50)

    def lambda_AE1():
        OP_92(0xFE, 0x8, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_AE1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_646 end

    def Function_3_B08(): pass

    label("Function_3_B08")

    EventBegin(0x0)
    OP_6D(30000, 0, 630, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(233000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x108, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0xE, 28310, 0, 210, 90)
    SetChrPos(0xF, 29950, 0, -1020, 47)
    SetChrPos(0x10, 29140, 0, 2290, 127)
    SetChrPos(0x11, 31010, 0, 1560, 131)
    SetChrPos(0x12, 31530, 0, -1200, 11)
    SetChrChipByIndex(0x8, 12)
    SetChrChipByIndex(0x9, 12)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 33200, 0, 2800, 26)
    SetChrPos(0x9, 32790, 0, 420, 142)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x1D, 0x40)
    SetChrFlags(0x1E, 0x40)
    SetChrFlags(0x1F, 0x40)
    SetChrFlags(0x20, 0x40)
    SetChrFlags(0x21, 0x40)
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
    SetChrPos(0x17, 11630, 0, -2640, 90)
    SetChrPos(0x18, 9800, 0, -3930, 90)
    SetChrPos(0x19, 9800, 0, -3930, 90)
    SetChrPos(0x1A, 9800, 0, -3930, 90)
    SetChrPos(0x1B, 9800, 0, -3930, 90)
    SetChrPos(0x1C, 9800, 0, -3930, 90)
    SetChrPos(0x1D, 9890, 0, -2180, 90)
    SetChrPos(0x1E, 9890, 0, -2180, 90)
    SetChrPos(0x1F, 9890, 0, -2180, 90)
    SetChrPos(0x20, 9890, 0, -2180, 90)
    SetChrPos(0x21, 9890, 0, -2180, 90)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x22, 0x40)
    SetChrFlags(0x23, 0x40)
    SetChrFlags(0x24, 0x40)
    SetChrFlags(0x25, 0x40)
    SetChrFlags(0x26, 0x40)
    SetChrPos(0x22, 12030, 0, -4240, 90)
    SetChrPos(0x23, 13140, 0, -2490, 72)
    SetChrPos(0x24, 11810, 0, -930, 90)
    SetChrPos(0x25, 8510, 0, -4850, 90)
    SetChrPos(0x26, 8510, 0, -1080, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "#176F#5P总算收拾掉了……\x02\x03",
            "#173F哦……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 1)
    SetChrSubChip(0xF, 1)
    SetChrSubChip(0x10, 1)
    SetChrSubChip(0x11, 1)
    SetChrSubChip(0x12, 1)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x12, 0x20)

    def lambda_E24():
        TurnDirection(0xFE, 0x17, 800)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E24)

    def lambda_E32():
        TurnDirection(0xFE, 0x17, 800)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E32)

    def lambda_E40():
        TurnDirection(0xFE, 0x17, 800)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E40)

    def lambda_E4E():
        TurnDirection(0xFE, 0x17, 800)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E4E)

    def lambda_E5C():
        TurnDirection(0xFE, 0x17, 800)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_E5C)
    Sleep(100)

    def lambda_E6F():
        OP_6D(19050, 0, 1190, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E6F)

    def lambda_E87():
        OP_6C(315000, 2300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E87)
    Sleep(400)
    OP_43(0x22, 0x1, 0x0, 0x5)
    OP_43(0x23, 0x1, 0x0, 0x6)
    OP_43(0x24, 0x1, 0x0, 0x7)
    OP_43(0x17, 0x1, 0x0, 0x4)
    OP_43(0x18, 0x1, 0x0, 0xA)
    OP_43(0x1D, 0x1, 0x0, 0xF)
    Sleep(600)

    def lambda_ECB():
        OP_6D(25500, 0, 390, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ECB)

    def lambda_EE3():
        OP_67(0, 6710, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_EE3)
    OP_43(0x19, 0x1, 0x0, 0xB)
    OP_43(0x1E, 0x1, 0x0, 0x10)
    Sleep(400)
    OP_43(0x1A, 0x1, 0x0, 0xC)
    OP_43(0x1F, 0x1, 0x0, 0x11)
    Sleep(400)
    OP_43(0x1B, 0x1, 0x0, 0xD)
    OP_43(0x20, 0x1, 0x0, 0x12)
    Sleep(400)
    OP_43(0x1C, 0x1, 0x0, 0xE)
    OP_43(0x21, 0x1, 0x0, 0x13)
    Sleep(400)
    OP_43(0x25, 0x1, 0x0, 0x8)
    OP_43(0x26, 0x1, 0x0, 0x9)
    Sleep(2500)

    ChrTalk(
        0x17,
        "愚蠢的家伙……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "飞艇是上了锁的，\x01",
            "不会那么容易被你们抢走的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#178F#2P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "如果不乖乖服从上校，\x01",
            "那么就只有用你们的性命……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "顽固不化的家伙们，\x01",
            "受死吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "进攻！\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xA, 12560, 0, -2110, 70)
    SetChrPos(0xD, 13660, 0, -70, 90)
    SetChrPos(0xC, 13730, 0, -1250, 75)
    SetChrPos(0xB, 12340, 0, 1110, 95)

    def lambda_10B2():
        OP_6D(28050, 0, 980, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_10B2)
    LoadEffect(0x2, "map\\\\mp019_00.eff")
    LoadEffect(0x0, "craft\\\\cr201_02.eff")
    SetChrPos(0x28, 19080, 0, 510, 0)
    PlayEffect(0x2, 0xFF, 0xC, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x28, 0, 0, 0, 0)
    Sleep(200)
    SetChrChipByIndex(0x22, 11)
    SetChrChipByIndex(0x23, 11)
    SetChrChipByIndex(0x24, 11)

    def lambda_114E():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_114E)

    def lambda_1169():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_1169)

    def lambda_1184():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1184)
    Sleep(100)
    SetChrChipByIndex(0x18, 20)
    SetChrChipByIndex(0x1C, 9)

    def lambda_11AE():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_11AE)

    def lambda_11C9():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_11C9)
    Sleep(100)
    SetChrChipByIndex(0x19, 9)
    SetChrChipByIndex(0x1D, 9)

    def lambda_11F3():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_11F3)

    def lambda_120E():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_120E)
    OP_22(0x1FA, 0x0, 0x64)
    Sleep(100)
    Sleep(200)
    OP_44(0x1B, 0xFF)
    OP_44(0x1F, 0xFF)
    OP_44(0x20, 0xFF)
    Sleep(100)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_44(0x22, 0xFF)
    OP_44(0x23, 0xFF)
    OP_44(0x24, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1D, 0xFF)
    OP_44(0x1E, 0xFF)
    SetChrChipByIndex(0x17, 23)
    SetChrChipByIndex(0x18, 19)
    SetChrChipByIndex(0x19, 8)
    SetChrChipByIndex(0x1A, 19)
    SetChrChipByIndex(0x1C, 19)
    SetChrChipByIndex(0x1D, 8)
    SetChrChipByIndex(0x1E, 19)
    SetChrChipByIndex(0x1F, 8)
    SetChrChipByIndex(0x20, 19)
    SetChrChipByIndex(0x21, 8)
    SetChrChipByIndex(0x22, 10)
    SetChrChipByIndex(0x23, 10)
    SetChrChipByIndex(0x24, 10)
    SetChrChipByIndex(0x25, 10)
    SetChrChipByIndex(0x26, 10)

    def lambda_12C8():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_12C8)

    def lambda_12D6():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_12D6)

    def lambda_12E4():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_12E4)

    def lambda_12F2():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_12F2)

    def lambda_1300():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1300)

    def lambda_130E():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_130E)

    def lambda_131C():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_131C)

    def lambda_132A():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_132A)

    def lambda_1338():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1338)

    def lambda_1346():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1346)

    def lambda_1354():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_1354)

    def lambda_1362():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_1362)

    def lambda_1370():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_1370)

    def lambda_137E():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_137E)

    def lambda_138C():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_138C)

    def lambda_139A():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_139A)

    def lambda_13A8():

        label("loc_13A8")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_13A8")

    QueueWorkItem2(0x22, 0, lambda_13A8)

    def lambda_13BB():

        label("loc_13BB")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_13BB")

    QueueWorkItem2(0x23, 0, lambda_13BB)

    def lambda_13CE():

        label("loc_13CE")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_13CE")

    QueueWorkItem2(0x24, 0, lambda_13CE)

    def lambda_13E1():
        OP_67(0, 4650, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_13E1)

    def lambda_13F9():
        OP_6C(291000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13F9)

    def lambda_1409():
        OP_6D(16070, 0, 1210, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1409)
    Sleep(350)
    PlayEffect(0x0, 0xFF, 0x1B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x20, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_44(0x1B, 0xFF)
    OP_44(0x1F, 0xFF)
    OP_44(0x20, 0xFF)

    def lambda_14D1():
        OP_8F(0x1B, 0x4BB4, 0x0, 0xFFFFF880, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_14D1)

    def lambda_14EC():
        OP_8F(0x1F, 0x50D2, 0x0, 0x46A, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_14EC)

    def lambda_1507():
        OP_8F(0x20, 0x4934, 0x0, 0xA28, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_1507)
    TurnDirection(0x1B, 0x28, 0)
    TurnDirection(0x1F, 0x28, 0)
    TurnDirection(0x20, 0x28, 0)
    SetChrChipByIndex(0x1B, 18)
    SetChrChipByIndex(0x1F, 18)
    SetChrChipByIndex(0x20, 18)
    SetChrFlags(0x1B, 0x20)
    SetChrFlags(0x1F, 0x20)
    SetChrFlags(0x20, 0x20)

    def lambda_1555():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1555)

    def lambda_1565():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1565)

    def lambda_1575():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1575)
    Sleep(30)

    def lambda_158A():
        OP_8F(0x1B, 0x4BB4, 0x0, 0xFFFFF880, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_158A)

    def lambda_15A5():
        OP_8F(0x1F, 0x50D2, 0x0, 0x46A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_15A5)

    def lambda_15C0():
        OP_8F(0x20, 0x4934, 0x0, 0xA28, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_15C0)
    Sleep(30)

    def lambda_15E0():
        OP_8F(0x1B, 0x4BB4, 0x0, 0xFFFFF880, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_15E0)

    def lambda_15FB():
        OP_8F(0x1F, 0x50D2, 0x0, 0x46A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_15FB)

    def lambda_1616():
        OP_8F(0x20, 0x4934, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_1616)
    Sleep(30)
    OP_44(0x1B, 0x2)
    OP_44(0x1F, 0x2)
    OP_44(0x20, 0x2)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x17,
        "#2P游、游击士！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#2P你们打算与军队为敌吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P很抱歉……\x01",
            "你们的所作所为是违法的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "奉陛下的口谕，\x01",
            "前来消灭你们！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/C4111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_B08 end

    def Function_4_174F(): pass

    label("Function_4_174F")

    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0x44E8, 0x0, 0xFFFFFE98, 0x1770, 0x0)
    OP_8E(0xFE, 0x5438, 0x0, 0x0, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 23)
    Return()

    # Function_4_174F end

    def Function_5_1782(): pass

    label("Function_5_1782")

    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x47FE, 0xA, 0xFFFFF718, 0x1770, 0x0)
    OP_8E(0xFE, 0x5794, 0x0, 0xFFFFF754, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_17BA():

        label("loc_17BA")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_17BA")

    QueueWorkItem2(0xFE, 0, lambda_17BA)
    Return()

    # Function_5_1782 end

    def Function_6_17C8(): pass

    label("Function_6_17C8")

    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x4C0E, 0x0, 0xFFFFFF92, 0x1770, 0x0)
    OP_8E(0xFE, 0x5AC8, 0x0, 0xFFFFFFCE, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_1800():

        label("loc_1800")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1800")

    QueueWorkItem2(0xFE, 0, lambda_1800)
    Return()

    # Function_6_17C8 end

    def Function_7_180E(): pass

    label("Function_7_180E")

    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x4574, 0x0, 0x41A, 0x1770, 0x0)
    OP_8E(0xFE, 0x5744, 0x0, 0x780, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_1846():

        label("loc_1846")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1846")

    QueueWorkItem2(0xFE, 0, lambda_1846)
    Return()

    # Function_7_180E end

    def Function_8_1854(): pass

    label("Function_8_1854")

    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x4466, 0x0, 0xFFFFF7D6, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_1878():

        label("loc_1878")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1878")

    QueueWorkItem2(0xFE, 0, lambda_1878)
    Return()

    # Function_8_1854 end

    def Function_9_1886(): pass

    label("Function_9_1886")

    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x434E, 0x0, 0x938, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_18AA():

        label("loc_18AA")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_18AA")

    QueueWorkItem2(0xFE, 0, lambda_18AA)
    Return()

    # Function_9_1886 end

    def Function_10_18B8(): pass

    label("Function_10_18B8")

    SetChrChipByIndex(0xFE, 20)
    OP_8E(0xFE, 0x4128, 0x0, 0xFFFFFA38, 0x1770, 0x0)
    OP_8E(0xFE, 0x55B4, 0x64, 0xFFFFF2D6, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 19)
    Return()

    # Function_10_18B8 end

    def Function_11_18EB(): pass

    label("Function_11_18EB")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x4128, 0x0, 0xFFFFFA38, 0x1770, 0x0)
    OP_8E(0xFE, 0x4F92, 0x14, 0xFFFFF718, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_11_18EB end

    def Function_12_191E(): pass

    label("Function_12_191E")

    SetChrChipByIndex(0xFE, 20)
    OP_8E(0xFE, 0x4128, 0x0, 0xFFFFFA38, 0x1770, 0x0)
    OP_8E(0xFE, 0x4FEC, 0x0, 0xFFFFFD12, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 19)
    Return()

    # Function_12_191E end

    def Function_13_1951(): pass

    label("Function_13_1951")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x4826, 0x0, 0xFFFFFD4E, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_13_1951 end

    def Function_14_1970(): pass

    label("Function_14_1970")

    SetChrChipByIndex(0xFE, 20)
    OP_8E(0xFE, 0x4128, 0x0, 0xFFFFFA38, 0x1770, 0x0)
    OP_8E(0xFE, 0x4B00, 0x1E, 0xFFFFF3EE, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 19)
    Return()

    # Function_14_1970 end

    def Function_15_19A3(): pass

    label("Function_15_19A3")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x3F7A, 0x0, 0x29E, 0x1770, 0x0)
    OP_8E(0xFE, 0x54A6, 0x0, 0xC26, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_15_19A3 end

    def Function_16_19D6(): pass

    label("Function_16_19D6")

    SetChrChipByIndex(0xFE, 20)
    OP_8E(0xFE, 0x3F7A, 0x0, 0x29E, 0x1770, 0x0)
    OP_8E(0xFE, 0x4FBA, 0x0, 0x712, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 19)
    Return()

    # Function_16_19D6 end

    def Function_17_1A09(): pass

    label("Function_17_1A09")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x3F7A, 0x0, 0x29E, 0x1770, 0x0)
    OP_8E(0xFE, 0x4CFE, 0x0, 0x21C, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_17_1A09 end

    def Function_18_1A3C(): pass

    label("Function_18_1A3C")

    SetChrChipByIndex(0xFE, 20)
    OP_8E(0xFE, 0x3F7A, 0x0, 0x29E, 0x1770, 0x0)
    OP_8E(0xFE, 0x472C, 0x0, 0x5F0, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 19)
    Return()

    # Function_18_1A3C end

    def Function_19_1A6F(): pass

    label("Function_19_1A6F")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x3F7A, 0x0, 0x29E, 0x1770, 0x0)
    OP_8E(0xFE, 0x4C54, 0x0, 0xDF2, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_19_1A6F end

    def Function_20_1AA2(): pass

    label("Function_20_1AA2")

    EventBegin(0x0)
    OP_6D(46220, -50, 11920, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(366, 0)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x7, 0xFF)
    AddParty(0x0, 0xFF)
    AddParty(0x2, 0xFF)
    AddParty(0x4, 0xFF)
    OP_B5(0x2, 0x0)
    OP_B5(0x2, 0x1)
    OP_B5(0x2, 0x2)
    OP_B5(0x2, 0x3)
    OP_B5(0x2, 0x4)
    OP_B5(0x2, 0x5)
    OP_41(0x2, 0x40)
    OP_41(0x2, 0xF5)
    OP_41(0x2, 0x113)
    OP_41(0x2, 0x26E, 0x0)
    OP_41(0x2, 0x26B, 0x1)
    OP_41(0x2, 0x25F, 0x2)
    OP_41(0x2, 0x262, 0x3)
    OP_41(0x2, 0x268, 0x4)
    OP_41(0x2, 0x271, 0x5)
    OP_35(0x2, 0xAA)
    OP_35(0x2, 0xAB)
    OP_36(0x2, 0xF0)
    OP_B5(0x4, 0x0)
    OP_B5(0x4, 0x5)
    OP_B5(0x4, 0x4)
    OP_B5(0x4, 0x3)
    OP_B5(0x4, 0x2)
    OP_B5(0x4, 0x1)
    OP_41(0x4, 0x7C)
    OP_41(0x4, 0xF5)
    OP_41(0x4, 0x113)
    OP_41(0x4, 0x259, 0x0)
    OP_41(0x4, 0x261, 0x5)
    OP_41(0x4, 0x2C8, 0x4)
    OP_41(0x4, 0x264, 0x3)
    OP_41(0x4, 0x25F, 0x2)
    OP_41(0x4, 0x27E, 0x1)
    OP_35(0x4, 0xBE)
    OP_35(0x4, 0xBF)
    OP_36(0x4, 0xFA)
    SetChrPos(0x101, 46320, -10, -1800, 0)
    SetChrPos(0x103, 47360, 0, -2280, 0)
    SetChrPos(0x105, 45230, 0, -2280, 0)

    def lambda_1BC8():
        OP_6D(46300, -40, -1440, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BC8)

    def lambda_1BE0():
        OP_6E(262, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BE0)
    Sleep(7000)

    ChrTalk(
        0x101,
        (
            "#000F情报部的特务艇……\x01",
            "没想到要在这种情况下乘坐啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F怎么说好呢……\x01",
            "真是造型随便、低俗的飞艇啊。\x02\x03",
            "和空贼艇真是棋逢对手呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F不过，拥有很强大的性能\x01",
            "这一点是没错的。\x02\x03",
            "这样的一艘飞船，\x01",
            "情报部是怎么得到的呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F确实有很多谜团呢。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x27, 46370, 200, 5440, 180)
    ClearChrFlags(0x27, 0x80)

    def lambda_1D9C():
        OP_8E(0xFE, 0xB522, 0xC8, 0x442, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1D9C)
    Sleep(500)

    def lambda_1DBC():
        OP_6D(46270, 200, 430, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DBC)
    WaitChrThread(0x27, 0x1)

    ChrTalk(
        0x27,
        (
            "呀，是殿下啊。\x01",
            "让您久等了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F佩顿师傅。。\x01",
            "你好，好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F咦……这个人是?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F他是佩顿师傅，\x01",
            "『埃尔赛尤号』飞船\x01",
            "的维修人员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "我是由中央工房\x01",
            "外派的技术人员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "『埃尔赛尤号』\x01",
            "现在还处于测试阶段，\x01",
            "不能用于实战。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哎～是这样啊。\x02\x03",
            "在卢安看到它的时候\x01",
            "可是飞的好好的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "一般的飞行当然是可以的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "因为新型的导力引擎开发进度\x01",
            "推迟而搭载了旧型的引擎，\x01",
            "这样就不能发挥其应有的性能了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "而且现在『埃尔赛尤号』又被\x01",
            "情报部给夺走了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "我在王都走投无路的时候，\x01",
            "尤莉亚中尉就让我到这里来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F原来是这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F呵呵……\x01",
            "请多多指教哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "好、好的，交给我吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "只要解开锁定，\x01",
            "就可以启动了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x27, 0xADFC, 0xC8, 0x3FC, 0x7D0, 0x0)
    TurnDirection(0x27, 0x105, 400)

    def lambda_21D0():

        label("loc_21D0")

        TurnDirection(0xFE, 0x105, 0)
        OP_48()
        Jump("loc_21D0")

    QueueWorkItem2(0x27, 3, lambda_21D0)

    ChrTalk(
        0x27,
        (
            "因为飞艇的机动性很高，\x01",
            "所以驾驶时要小心才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F我明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F那么，\x01",
            " \x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_20_1AA2 end

    def Function_21_2297(): pass

    label("Function_21_2297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_22A4")
    Return()

    label("loc_22A4")

    EventBegin(0x0)

    ChrTalk(
        0x27,
        "……哦，对了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "我带了一些可以调整\x01",
            "大家的导力器的工具。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "还有，虽然种类不多，\x01",
            " \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F哎呀，还是挺会办事的嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F真是帮了我们大忙了。\x01",
            "真是非常感谢啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "东、东西不多，希望能派上用场。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "有需要的话请说一声。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x65F)
    EventEnd(0x1)
    Return()

    # Function_21_2297 end

    def Function_22_23FD(): pass

    label("Function_22_23FD")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x105, 46310, 200, 4320, 176)
    SetChrPos(0x103, 46840, 200, 3150, 0)
    SetChrPos(0x101, 45710, 200, 3160, 0)
    TurnDirection(0x27, 0x105, 0)
    OP_6D(46390, 250, 4580, 1000)

    ChrTalk(
        0x105,
        (
            "#040F距离正午已经\x01",
            "没有多少时间了。\x02\x03",
            "要乘坐飞艇\x01",
            "并启动引擎吗？\x02",
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
            "乘坐飞艇\x01",      # 0
            " \x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_24FC"),
        (1, "loc_2517"),
        (SWITCH_DEFAULT, "loc_2585"),
    )


    label("loc_24FC")


    ChrTalk(
        0x105,
        "#040F我明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2585")

    label("loc_2517")


    ChrTalk(
        0x105,
        "#040F我明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F如果想整理装备的话\x01",
            "就和修理员师傅说一声吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_2585")

    OP_A2(0x660)
    OP_28(0x4D, 0x1, 0x20)
    TurnDirection(0x105, 0x27, 400)

    ChrTalk(
        0x105,
        (
            "#040F……佩顿师傅，\x01",
            "请您在后面协助我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "明白了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "引擎的调整就交给我吧，\x01",
            "请殿下专心的驾驶飞艇！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        "#000F雪拉姐，终于要开始了……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#020F是啊……\x02\x03",
            "任务虽然很艰巨，\x01",
            "不过原则是相通的。\x02\x03",
            "迅速果敢……以及沉着冷静。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3F0)
    NewScene("ED6_DT01/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_22_23FD end

    def Function_23_26CF(): pass

    label("Function_23_26CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_286E")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2766")
    TurnDirection(0x105, 0x0, 400)

    ChrTalk(
        0x105,
        (
            "#042F嗯，距离正午已经\x01",
            "没有多少时间了。\x02\x03",
            "准备好了的话，\x01",
            "我们就上飞艇吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#002F嗯，知道了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2853")

    label("loc_2766")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27F8")
    TurnDirection(0x103, 0x1, 400)

    ChrTalk(
        0x103,
        (
            "#026F距离作战开始\x01",
            "已经没有多少时间了。\x02\x03",
            "#027F确认完装备\x01",
            "就赶快上飞艇去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2853")

    label("loc_27F8")

    TurnDirection(0x105, 0x1, 400)

    ChrTalk(
        0x105,
        (
            "#042F距离正午已经\x01",
            "没有多少时间了。\x02\x03",
            "准备好了的话，\x01",
            "我们就上飞艇吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2853")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_286E")

    Return()

    # Function_23_26CF end

    SaveToFile()

Try(main)
