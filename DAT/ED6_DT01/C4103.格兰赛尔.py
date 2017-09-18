from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4103   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4103.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60021",
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
        'ED6_DT07/CH00344 ._CH',             # 0C
        'ED6_DT07/CH01450 ._CH',             # 0D
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
        'ED6_DT07/CH00344P._CP',             # 0C
        'ED6_DT07/CH01450P._CP',             # 0D
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )


    DeclEvent(
        X                   = 23240,
        Y                   = -1000,
        Z                   = 7400,
        Range               = 17390,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFE0D4,
        Unknown_18          = 0x0,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = 44270,
        Y                   = 1000,
        Z                   = 940,
        Range               = 48410,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0x0,
        Unknown_18          = 0x0,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = 45450,
        Y                   = 1000,
        Z                   = 6140,
        Range               = 47430,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0x1144,
        Unknown_18          = 0x0,
        Unknown_1C          = 24,
    )


    ScpFunction(
        "Function_0_57A",          # 00, 0
        "Function_1_5AE",          # 01, 1
        "Function_2_5DB",          # 02, 2
        "Function_3_5F1",          # 03, 3
        "Function_4_92E",          # 04, 4
        "Function_5_12A5",         # 05, 5
        "Function_6_12EB",         # 06, 6
        "Function_7_1331",         # 07, 7
        "Function_8_1377",         # 08, 8
        "Function_9_13BD",         # 09, 9
        "Function_10_13EF",        # 0A, 10
        "Function_11_1421",        # 0B, 11
        "Function_12_1454",        # 0C, 12
        "Function_13_1487",        # 0D, 13
        "Function_14_14BA",        # 0E, 14
        "Function_15_14D9",        # 0F, 15
        "Function_16_150C",        # 10, 16
        "Function_17_153F",        # 11, 17
        "Function_18_1572",        # 12, 18
        "Function_19_15A5",        # 13, 19
        "Function_20_15D8",        # 14, 20
        "Function_21_160B",        # 15, 21
        "Function_22_1EA7",        # 16, 22
        "Function_23_2002",        # 17, 23
        "Function_24_218E",        # 18, 24
        "Function_25_249A",        # 19, 25
    )


    def Function_0_57A(): pass

    label("Function_0_57A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_588")
    OP_A3(0x3FA)
    Event(0, 3)

    label("loc_588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_596")
    OP_A3(0x3FB)
    Event(0, 4)

    label("loc_596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_5AD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FC)
    Event(0, 21)

    label("loc_5AD")

    Return()

    # Function_0_57A end

    def Function_1_5AE(): pass

    label("Function_1_5AE")

    OP_16(0x2, 0xFA0, 0xFFFEA070, 0xFFFE4698, 0x30066)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 6)), scpexpr(EXPR_END)), "loc_5D5")
    OP_71(0x0, 0x4)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D5")

    OP_22(0x1CC, 0x1, 0x64)
    Return()

    # Function_1_5AE end

    def Function_2_5DB(): pass

    label("Function_2_5DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_5DB")

    label("loc_5F0")

    Return()

    # Function_2_5DB end

    def Function_3_5F1(): pass

    label("Function_3_5F1")

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

    def lambda_66B():
        OP_6C(45000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_66B)
    Sleep(2000)

    def lambda_680():
        OP_6E(228, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_680)
    OP_6D(26290, 0, 960, 5000)

    ChrTalk(
        0x8,
        (
            "哈啊……\x01",
            "肚子好饿啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x18,
        "还没到换班时间吗？\x02",
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
            "反正在逃中的人\x01",
            "连１０个都不到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那些家伙，上校只要想的话，\x01",
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

    ChrTalk(
        0xE,
        (
            "……只要你们办得到\x01",
            "就尽管来试试看。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_89C():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_89C)

    def lambda_8AA():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8AA)

    def lambda_8B8():
        OP_6E(262, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8B8)

    def lambda_8C8():
        OP_6D(20430, 0, 1370, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8C8)

    def lambda_8E0():
        OP_6C(315000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8E0)
    Sleep(1500)

    ChrTalk(
        0x8,
        "呀……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "亲卫队中队长，\x01",
            "尤莉亚·舒华兹！？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_5F1 end

    def Function_4_92E(): pass

    label("Function_4_92E")

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

    ChrTalk(
        0xE,
        (
            "#170F总算收拾掉了……\x02\x03",
            "哦……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BF2():
        TurnDirection(0xFE, 0x17, 800)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_BF2)

    def lambda_C00():
        TurnDirection(0xFE, 0x17, 800)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_C00)

    def lambda_C0E():
        TurnDirection(0xFE, 0x17, 800)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_C0E)

    def lambda_C1C():
        TurnDirection(0xFE, 0x17, 800)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_C1C)

    def lambda_C2A():
        TurnDirection(0xFE, 0x17, 800)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C2A)
    Sleep(100)

    def lambda_C3D():
        OP_6D(19050, 0, 1190, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C3D)

    def lambda_C55():
        OP_6C(315000, 2300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C55)
    Sleep(400)
    OP_43(0x22, 0x1, 0x0, 0x6)
    OP_43(0x23, 0x1, 0x0, 0x7)
    OP_43(0x24, 0x1, 0x0, 0x8)
    OP_43(0x17, 0x1, 0x0, 0x5)
    OP_43(0x18, 0x1, 0x0, 0xB)
    OP_43(0x1D, 0x1, 0x0, 0x10)
    Sleep(600)

    def lambda_C99():
        OP_6D(25500, 0, 390, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C99)

    def lambda_CB1():
        OP_67(0, 6710, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_CB1)
    OP_43(0x19, 0x1, 0x0, 0xC)
    OP_43(0x1E, 0x1, 0x0, 0x11)
    Sleep(400)
    OP_43(0x1A, 0x1, 0x0, 0xD)
    OP_43(0x1F, 0x1, 0x0, 0x12)
    Sleep(400)
    OP_43(0x1B, 0x1, 0x0, 0xE)
    OP_43(0x20, 0x1, 0x0, 0x13)
    Sleep(400)
    OP_43(0x1C, 0x1, 0x0, 0xF)
    OP_43(0x21, 0x1, 0x0, 0x14)
    Sleep(400)
    OP_43(0x25, 0x1, 0x0, 0x9)
    OP_43(0x26, 0x1, 0x0, 0xA)
    Sleep(2500)

    ChrTalk(
        0x17,
        "愚蠢的家伙……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "飞行艇是严密封锁了的，\x01",
            "不会那么容易被你们抢走的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#170F…………………………\x02",
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
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xA, 13660, 0, -70, 90)
    SetChrPos(0xB, 12560, 0, -2110, 75)
    SetChrPos(0xC, 13730, 0, -1250, 68)
    SetChrPos(0xD, 12340, 0, 1110, 97)

    def lambda_E91():
        OP_6D(28050, 0, 980, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E91)
    SetChrChipByIndex(0x22, 11)
    SetChrChipByIndex(0x23, 11)
    SetChrChipByIndex(0x24, 11)

    def lambda_EB8():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_EB8)

    def lambda_ED3():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_ED3)

    def lambda_EEE():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_EEE)
    Sleep(100)
    SetChrChipByIndex(0x18, 9)
    SetChrChipByIndex(0x1C, 9)

    def lambda_F18():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_F18)

    def lambda_F33():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_F33)
    Sleep(100)
    SetChrChipByIndex(0x19, 9)
    SetChrChipByIndex(0x1D, 9)

    def lambda_F5D():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_F5D)

    def lambda_F78():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_F78)
    Sleep(100)
    PlayEffect(0x8, 0xFF, 0xFF, 21350, 3000, 30, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_44(0x1B, 0xFF)
    PlayEffect(0x8, 0xFF, 0xFF, 17730, 1000, -580, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x1B, 12)
    OP_8C(0x1B, 244, 0)

    def lambda_1017():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1017)
    Sleep(100)
    OP_44(0x22, 0xFF)
    OP_44(0x23, 0xFF)
    OP_44(0x24, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1D, 0xFF)
    OP_44(0x1E, 0xFF)
    SetChrChipByIndex(0x17, 8)
    SetChrChipByIndex(0x18, 8)
    SetChrChipByIndex(0x19, 8)
    SetChrChipByIndex(0x1A, 8)
    SetChrChipByIndex(0x1C, 8)
    SetChrChipByIndex(0x1D, 8)
    SetChrChipByIndex(0x1E, 8)
    SetChrChipByIndex(0x1F, 8)
    SetChrChipByIndex(0x20, 8)
    SetChrChipByIndex(0x21, 8)
    SetChrChipByIndex(0x22, 10)
    SetChrChipByIndex(0x23, 10)
    SetChrChipByIndex(0x24, 10)
    SetChrChipByIndex(0x25, 10)
    SetChrChipByIndex(0x26, 10)

    def lambda_1097():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1097)

    def lambda_10A5():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_10A5)

    def lambda_10B3():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_10B3)

    def lambda_10C1():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_10C1)

    def lambda_10CF():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_10CF)

    def lambda_10DD():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_10DD)

    def lambda_10EB():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_10EB)

    def lambda_10F9():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_10F9)

    def lambda_1107():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1107)

    def lambda_1115():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_1115)

    def lambda_1123():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_1123)

    def lambda_1131():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_1131)

    def lambda_113F():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_113F)

    def lambda_114D():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_114D)

    def lambda_115B():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_115B)

    def lambda_1169():
        OP_67(0, 4650, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1169)

    def lambda_1181():
        OP_6C(291000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1181)
    OP_6D(18070, 0, 1210, 1500)

    ChrTalk(
        0x17,
        "呀……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "游、游击士！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "你们打算\x01",
            "与军队为敌吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "很抱歉……\x01",
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
    NewScene("ED6_DT01/C4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_92E end

    def Function_5_12A5(): pass

    label("Function_5_12A5")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x44E8, 0x0, 0xFFFFFE98, 0x1770, 0x0)
    OP_8E(0xFE, 0x5438, 0x0, 0x0, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)

    def lambda_12DD():

        label("loc_12DD")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_12DD")

    QueueWorkItem2(0xFE, 0, lambda_12DD)
    Return()

    # Function_5_12A5 end

    def Function_6_12EB(): pass

    label("Function_6_12EB")

    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x47FE, 0xA, 0xFFFFF718, 0x1770, 0x0)
    OP_8E(0xFE, 0x5794, 0x0, 0xFFFFF754, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_1323():

        label("loc_1323")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1323")

    QueueWorkItem2(0xFE, 0, lambda_1323)
    Return()

    # Function_6_12EB end

    def Function_7_1331(): pass

    label("Function_7_1331")

    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x4C0E, 0x0, 0xFFFFFF92, 0x1770, 0x0)
    OP_8E(0xFE, 0x5AC8, 0x0, 0xFFFFFFCE, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_1369():

        label("loc_1369")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1369")

    QueueWorkItem2(0xFE, 0, lambda_1369)
    Return()

    # Function_7_1331 end

    def Function_8_1377(): pass

    label("Function_8_1377")

    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x4574, 0x0, 0x41A, 0x1770, 0x0)
    OP_8E(0xFE, 0x5744, 0x0, 0x780, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_13AF():

        label("loc_13AF")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_13AF")

    QueueWorkItem2(0xFE, 0, lambda_13AF)
    Return()

    # Function_8_1377 end

    def Function_9_13BD(): pass

    label("Function_9_13BD")

    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x4466, 0x0, 0xFFFFF7D6, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_13E1():

        label("loc_13E1")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_13E1")

    QueueWorkItem2(0xFE, 0, lambda_13E1)
    Return()

    # Function_9_13BD end

    def Function_10_13EF(): pass

    label("Function_10_13EF")

    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x434E, 0x0, 0x938, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_1413():

        label("loc_1413")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1413")

    QueueWorkItem2(0xFE, 0, lambda_1413)
    Return()

    # Function_10_13EF end

    def Function_11_1421(): pass

    label("Function_11_1421")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x4128, 0x0, 0xFFFFFA38, 0x1770, 0x0)
    OP_8E(0xFE, 0x55B4, 0x64, 0xFFFFF2D6, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_11_1421 end

    def Function_12_1454(): pass

    label("Function_12_1454")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x4128, 0x0, 0xFFFFFA38, 0x1770, 0x0)
    OP_8E(0xFE, 0x4F92, 0x14, 0xFFFFF718, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_12_1454 end

    def Function_13_1487(): pass

    label("Function_13_1487")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x4128, 0x0, 0xFFFFFA38, 0x1770, 0x0)
    OP_8E(0xFE, 0x4FEC, 0x0, 0xFFFFFD12, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_13_1487 end

    def Function_14_14BA(): pass

    label("Function_14_14BA")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x4826, 0x0, 0xFFFFFD4E, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_14_14BA end

    def Function_15_14D9(): pass

    label("Function_15_14D9")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x4128, 0x0, 0xFFFFFA38, 0x1770, 0x0)
    OP_8E(0xFE, 0x4B00, 0x1E, 0xFFFFF3EE, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_15_14D9 end

    def Function_16_150C(): pass

    label("Function_16_150C")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x3F7A, 0x0, 0x29E, 0x1770, 0x0)
    OP_8E(0xFE, 0x54A6, 0x0, 0xC26, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_16_150C end

    def Function_17_153F(): pass

    label("Function_17_153F")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x3F7A, 0x0, 0x29E, 0x1770, 0x0)
    OP_8E(0xFE, 0x4FBA, 0x0, 0x712, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_17_153F end

    def Function_18_1572(): pass

    label("Function_18_1572")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x3F7A, 0x0, 0x29E, 0x1770, 0x0)
    OP_8E(0xFE, 0x4CFE, 0x0, 0x21C, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_18_1572 end

    def Function_19_15A5(): pass

    label("Function_19_15A5")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x3F7A, 0x0, 0x29E, 0x1770, 0x0)
    OP_8E(0xFE, 0x472C, 0x0, 0x5F0, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_19_15A5 end

    def Function_20_15D8(): pass

    label("Function_20_15D8")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x3F7A, 0x0, 0x29E, 0x1770, 0x0)
    OP_8E(0xFE, 0x4C54, 0x0, 0xDF2, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_20_15D8 end

    def Function_21_160B(): pass

    label("Function_21_160B")

    ClearMapFlags(0x2000000)
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
    AddParty(0x4, 0xFF)
    AddParty(0x2, 0xFF)
    OP_31(0x2, 0x0, 0x22)
    OP_B5(0x2, 0x0)
    OP_B5(0x2, 0x1)
    OP_B5(0x2, 0x5)
    OP_B5(0x2, 0x4)
    OP_B5(0x2, 0x3)
    OP_B5(0x2, 0x2)
    OP_41(0x2, 0x40)
    OP_41(0x2, 0xF6)
    OP_41(0x2, 0x114)
    OP_41(0x2, 0x26F, 0x0)
    OP_41(0x2, 0x26C, 0x1)
    OP_41(0x2, 0x260, 0x5)
    OP_41(0x2, 0x269, 0x4)
    OP_41(0x2, 0x271, 0x3)
    OP_41(0x2, 0x280, 0x2)
    OP_35(0x2, 0xAA)
    OP_35(0x2, 0xAB)
    OP_35(0x2, 0xAC)
    OP_36(0x2, 0xF0)
    OP_31(0x4, 0x0, 0x20)
    OP_B5(0x4, 0x0)
    OP_B5(0x4, 0x5)
    OP_B5(0x4, 0x4)
    OP_B5(0x4, 0x3)
    OP_B5(0x4, 0x2)
    OP_B5(0x4, 0x1)
    OP_41(0x4, 0x7C)
    OP_41(0x4, 0xF6)
    OP_41(0x4, 0x114)
    OP_41(0x4, 0x25A, 0x0)
    OP_41(0x4, 0x262, 0x5)
    OP_41(0x4, 0x2C9, 0x4)
    OP_41(0x4, 0x265, 0x3)
    OP_41(0x4, 0x25D, 0x2)
    OP_41(0x4, 0x2D4, 0x1)
    OP_35(0x4, 0xBE)
    OP_35(0x4, 0xBF)
    OP_36(0x4, 0xFA)
    SetChrPos(0x101, 46320, -10, -1800, 0)
    SetChrPos(0x103, 47360, 0, -2280, 0)
    SetChrPos(0x105, 45230, 0, -2280, 0)

    def lambda_1744():
        OP_6D(46300, -40, -1440, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1744)

    def lambda_175C():
        OP_6E(262, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_175C)
    Sleep(5000)

    ChrTalk(
        0x101,
        (
            "#002F情报部的特务飞艇……\x01",
            "没想到会是在这种情况下乘坐啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F怎么说好呢……\x01",
            "真是造型随便、低俗的飞艇啊。\x02\x03",
            "#027F和空贼飞艇真是棋逢对手呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F不过话说回来，\x01",
            "拥有很强大的性能这一点是没错的。\x02\x03",
            "这样的一艘飞艇，\x01",
            "情报部是怎么得到的呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯，说到这个。\x02\x03",
            "#007F那个叫『福音』的导力器\x01",
            "也隐藏了不少秘密呢……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x27, 46370, 200, 6000, 180)
    ClearChrFlags(0x27, 0x80)
    OP_4A(0x27, 255)

    NpcTalk(
        0x27,
        "青年的声音",
        (
            "#4P呀，是公主殿下啊。\x01",
            "让您久等了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1981():
        OP_6D(46270, 200, 430, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1981)

    def lambda_1999():
        OP_8E(0xFE, 0xB522, 0xC8, 0x442, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1999)
    WaitChrThread(0x27, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x105,
        (
            "#041F是佩顿师傅啊。\x01",
            "你好，真是好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F咦……这个人是?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F他是佩顿师傅，\x01",
            "『埃尔赛尤号』巡洋舰的维修员。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#5P我是由中央工房\x01",
            "外派的技术人员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#5P因为『埃尔赛尤号』处于试飞阶段，\x01",
            "所以需要测试并处理各种数据。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎～是这样啊。\x02\x03",
            "可是，在卢安看到那飞艇的时候，\x01",
            "还是飞得好好的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "#5P一般的飞行当然是可以了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#5P因为新型的导力引擎开发进度推迟，\x01",
            "所以暂时只能用旧型的引擎，\x01",
            "这样就不能发挥其应有的性能了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#5P而且现在飞艇又被情报部给夺走了，\x01",
            "试飞只有无限延期了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#5P我在王都走投无路的时候，\x01",
            "尤莉亚中尉就让我到这里来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F原来是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F呵呵……\x01",
            "请多多指教哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "#5P好、好的，交给我吧！\x02",
    )

    CloseMessageWindow()

    def lambda_1D34():

        label("loc_1D34")

        TurnDirection(0xFE, 0x27, 400)
        OP_48()
        Jump("loc_1D34")

    QueueWorkItem2(0x101, 1, lambda_1D34)

    def lambda_1D45():

        label("loc_1D45")

        TurnDirection(0xFE, 0x27, 400)
        OP_48()
        Jump("loc_1D45")

    QueueWorkItem2(0x105, 1, lambda_1D45)

    def lambda_1D56():

        label("loc_1D56")

        TurnDirection(0xFE, 0x27, 400)
        OP_48()
        Jump("loc_1D56")

    QueueWorkItem2(0x103, 1, lambda_1D56)
    OP_8E(0x27, 0xBB9E, 0xC8, 0x2DA, 0x7D0, 0x0)
    TurnDirection(0x27, 0x105, 400)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x103, 0xFF)

    ChrTalk(
        0x27,
        (
            "#5P只要解开锁定，\x01",
            "就可以开动飞艇了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#5P因为飞艇的机动性很高，\x01",
            "所以驾驶时要小心才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#042F#6P我明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F那么，\x01",
            "我们赶快上飞艇去吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x27, 270, 0)
    OP_4B(0x27, 255)
    EventEnd(0x0)
    Return()

    # Function_21_160B end

    def Function_22_1EA7(): pass

    label("Function_22_1EA7")

    TalkBegin(0x27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F4C")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",            # 0
            "改造·换钱\x01",      # 1
            "购买道具\x01",        # 2
            "离开\x01",            # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F22")
    OP_0D()
    OP_A9(0x6C)
    OP_56(0x0)
    TalkEnd(0x27)
    Return()

    label("loc_1F22")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F3B")
    OP_0D()
    OP_A9(0x6D)
    OP_56(0x0)
    TalkEnd(0x27)
    Return()

    label("loc_1F3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F4C")
    TalkEnd(0x27)
    Return()

    label("loc_1F4C")


    ChrTalk(
        0x27,
        (
            "我带了一些可以调整大家的\x01",
            "导力器的工具。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "还有，我也准备了一些装备和道具，\x01",
            "虽然种类不算很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "有需要的话请说一声。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x27)
    Return()

    # Function_22_1EA7 end

    def Function_23_2002(): pass

    label("Function_23_2002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 7)), scpexpr(EXPR_END)), "loc_200A")
    Return()

    label("loc_200A")

    EventBegin(0x0)
    OP_4A(0x27, 255)
    OP_8C(0x27, 225, 400)

    ChrTalk(
        0x27,
        "……哦，对了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x27, 0)
    TurnDirection(0x105, 0x27, 0)
    TurnDirection(0x103, 0x27, 0)

    ChrTalk(
        0x27,
        (
            "我带了一些可以调整大家的\x01",
            "导力器的工具。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "还有，我也准备了一些装备和道具，\x01",
            "虽然种类不算很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F啊，真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#027F哎呀，还是挺会办事的嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#041F您真是帮了我们大忙了，\x01",
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
    OP_8C(0x27, 270, 0)
    OP_4B(0x27, 255)
    EventEnd(0x1)
    Return()

    # Function_23_2002 end

    def Function_24_218E(): pass

    label("Function_24_218E")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x105, 46310, 200, 4320, 176)
    SetChrPos(0x103, 46840, 200, 3150, 0)
    SetChrPos(0x101, 45710, 200, 3160, 0)
    OP_6D(46390, 250, 4580, 0)
    OP_0D()

    ChrTalk(
        0x105,
        (
            "#042F#5P距离正午已经没有多少时间了。\x01",
            "　\x02\x03",
            "这就乘坐飞艇并启动引擎吗？\x01",
            "　\x02",
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
            "【乘坐飞艇】\x01",      # 0
            "【整理装备】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_228A"),
        (1, "loc_22A8"),
        (SWITCH_DEFAULT, "loc_2319"),
    )


    label("loc_228A")


    ChrTalk(
        0x105,
        "#047F#5P好的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2319")

    label("loc_22A8")


    ChrTalk(
        0x105,
        "#040F#5P好的。\x02",
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

    label("loc_2319")

    OP_28(0x4D, 0x1, 0x20)
    OP_4A(0x27, 255)
    TurnDirection(0x27, 0x105, 400)
    OP_6D(47340, 250, 3680, 1000)

    ChrTalk(
        0x105,
        (
            "#040F#5P……佩顿师傅，请你在后面协助我。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "#2P遵命！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#2P引擎的调整就交给我吧，\x01",
            "殿下专心驾驶飞艇就行了！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        "#002F#6P雪拉姐，终于要开始了……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#026F#2P是啊……\x02\x03",
            "#020F任务虽然很艰巨，不过原则是相通的。\x01",
            "　\x02\x03",
            "迅速果敢……以及沉着冷静。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x3F0)
    NewScene("ED6_DT01/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_218E end

    def Function_25_249A(): pass

    label("Function_25_249A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2634")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2531")
    TurnDirection(0x105, 0x0, 400)

    ChrTalk(
        0x105,
        (
            "#043F嗯，\x01",
            "距离正午已经没有多少时间了。\x02\x03",
            "准备好了的话，\x01",
            "我们就上飞艇吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#006F嗯，知道了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2619")

    label("loc_2531")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25BE")
    TurnDirection(0x103, 0x1, 400)

    ChrTalk(
        0x103,
        (
            "#022F距离作战开始已经没有多少时间了。\x01",
            "　\x02\x03",
            "确认完装备就赶快上飞艇去吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2619")

    label("loc_25BE")

    TurnDirection(0x105, 0x1, 400)

    ChrTalk(
        0x105,
        (
            "#042F距离正午已经没有多少时间了。\x01",
            "　\x02\x03",
            "准备好了的话，\x01",
            "我们就上飞艇吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2619")

    OP_90(0x0, 0x7D0, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_2634")

    Return()

    # Function_25_249A end

    SaveToFile()

Try(main)
