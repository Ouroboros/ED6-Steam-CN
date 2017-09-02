from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4230   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4230.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '艾莉茜雅女王',                         # 9
        '杜南公爵',                             # 10
        '管家菲利普',                           # 11
        '特务兵',                               # 12
        '特务兵',                               # 13
        '特务兵',                               # 14
        '特务兵',                               # 15
        '茜亚',                                 # 16
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
        'ED6_DT07/CH02460 ._CH',             # 00
        'ED6_DT07/CH02230 ._CH',             # 01
        'ED6_DT07/CH02240 ._CH',             # 02
        'ED6_DT07/CH00000 ._CH',             # 03
        'ED6_DT07/CH00010 ._CH',             # 04
        'ED6_DT07/CH02010 ._CH',             # 05
        'ED6_DT07/CH02140 ._CH',             # 06
        'ED6_DT07/CH02470 ._CH',             # 07
        'ED6_DT07/CH01330 ._CH',             # 08
        'ED6_DT07/CH00100 ._CH',             # 09
        'ED6_DT07/CH00101 ._CH',             # 0A
        'ED6_DT07/CH00120 ._CH',             # 0B
        'ED6_DT07/CH00121 ._CH',             # 0C
        'ED6_DT07/CH00140 ._CH',             # 0D
        'ED6_DT07/CH00141 ._CH',             # 0E
        'ED6_DT07/CH02540 ._CH',             # 0F
        'ED6_DT07/CH00440 ._CH',             # 10
        'ED6_DT07/CH00441 ._CH',             # 11
        'ED6_DT07/CH00500 ._CH',             # 12
        'ED6_DT07/CH00501 ._CH',             # 13
        'ED6_DT06/CH20042 ._CH',             # 14
        'ED6_DT06/CH20089 ._CH',             # 15
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02230P._CP',             # 01
        'ED6_DT07/CH02240P._CP',             # 02
        'ED6_DT07/CH00000P._CP',             # 03
        'ED6_DT07/CH00010P._CP',             # 04
        'ED6_DT07/CH02010P._CP',             # 05
        'ED6_DT07/CH02140P._CP',             # 06
        'ED6_DT07/CH02470P._CP',             # 07
        'ED6_DT07/CH01330P._CP',             # 08
        'ED6_DT07/CH00100P._CP',             # 09
        'ED6_DT07/CH00101P._CP',             # 0A
        'ED6_DT07/CH00120P._CP',             # 0B
        'ED6_DT07/CH00121P._CP',             # 0C
        'ED6_DT07/CH00140P._CP',             # 0D
        'ED6_DT07/CH00141P._CP',             # 0E
        'ED6_DT07/CH02540P._CP',             # 0F
        'ED6_DT07/CH00440P._CP',             # 10
        'ED6_DT07/CH00441P._CP',             # 11
        'ED6_DT07/CH00500P._CP',             # 12
        'ED6_DT07/CH00501P._CP',             # 13
        'ED6_DT06/CH20042P._CP',             # 14
        'ED6_DT06/CH20089P._CP',             # 15
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
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    DeclEvent(
        X                   = 1980,
        Y                   = -1000,
        Z                   = -1550,
        Range               = -2230,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFF056,
        Unknown_18          = 0x0,
        Unknown_1C          = 11,
    )


    ScpFunction(
        "Function_0_27A",          # 00, 0
        "Function_1_471",          # 01, 1
        "Function_2_4A6",          # 02, 2
        "Function_3_4BC",          # 03, 3
        "Function_4_503",          # 04, 4
        "Function_5_5A2",          # 05, 5
        "Function_6_75F",          # 06, 6
        "Function_7_CB4",          # 07, 7
        "Function_8_449F",         # 08, 8
        "Function_9_5EEE",         # 09, 9
        "Function_10_5FF6",        # 0A, 10
        "Function_11_6001",        # 0B, 11
    )


    def Function_0_27A(): pass

    label("Function_0_27A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_288")
    OP_A3(0x3FA)
    Event(0, 6)

    label("loc_288")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_294"),
        (SWITCH_DEFAULT, "loc_2B5"),
    )


    label("loc_294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 8)

    label("loc_2B2")

    Jump("loc_2B5")

    label("loc_2B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_2DA")
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 1)
    SetChrChipByIndex(0x138, 2)
    Jump("loc_2E9")

    label("loc_2DA")

    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 3)
    SetChrChipByIndex(0x138, 4)

    label("loc_2E9")

    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_2F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_302")
    Jump("loc_34E")

    label("loc_302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_329")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -53080, 0, 12340, 3)
    OP_43(0xF, 0x0, 0x0, 0x2)
    Jump("loc_34E")

    label("loc_329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_333")
    Jump("loc_34E")

    label("loc_333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_33D")
    Jump("loc_34E")

    label("loc_33D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_347")
    Jump("loc_34E")

    label("loc_347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_34E")

    label("loc_34E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_358")
    Jump("loc_470")

    label("loc_358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_419")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, -52830, 0, 7650, 179)
    SetChrPos(0xA, -53810, 0, 7520, 79)
    SetChrPos(0xB, -5180, 0, 11510, 90)
    SetChrPos(0xD, -3130, 0, 13730, 262)
    SetChrPos(0xE, -5030, 0, 13030, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 5)), scpexpr(EXPR_END)), "loc_416")
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xE, 0x1)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xD, 0x800)
    SetChrFlags(0xE, 0x800)
    SetChrChipByIndex(0xB, 20)
    SetChrChipByIndex(0xD, 20)
    SetChrChipByIndex(0xE, 20)
    SetChrFlags(0x9, 0x20)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 21)

    label("loc_416")

    Jump("loc_470")

    label("loc_419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_423")
    Jump("loc_470")

    label("loc_423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_42D")
    Jump("loc_470")

    label("loc_42D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_437")
    Jump("loc_470")

    label("loc_437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_441")
    Jump("loc_470")

    label("loc_441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_44B")
    Jump("loc_470")

    label("loc_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_455")
    Jump("loc_470")

    label("loc_455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_45F")
    Jump("loc_470")

    label("loc_45F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_469")
    Jump("loc_470")

    label("loc_469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_470")

    label("loc_470")

    Return()

    # Function_0_27A end

    def Function_1_471(): pass

    label("Function_1_471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_486")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_497")
    OP_1B(0x2, 0x0, 0x7)

    label("loc_497")

    OP_1B(0x5, 0x0, 0xA)
    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_471 end

    def Function_2_4A6(): pass

    label("Function_2_4A6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4BB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_4A6")

    label("loc_4BB")

    Return()

    # Function_2_4A6 end

    def Function_3_4BC(): pass

    label("Function_3_4BC")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "杜南公爵晕过去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFE)
    Return()

    # Function_3_4BC end

    def Function_4_503(): pass

    label("Function_4_503")

    TalkBegin(0xFE)

    ChrTalk(
        0xA,
        (
            "#720F公主殿下，还有各位，\x01",
            "十分感谢你们的宽宏大量。\x02\x03",
            "我代表殿下向你们谢罪，\x01",
            "对于此恩此德，没齿难忘。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_503 end

    def Function_5_5A2(): pass

    label("Function_5_5A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_5AF")
    Jump("loc_75B")

    label("loc_5AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_736")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_63C")

    ChrTalk(
        0xFE,
        (
            "公主殿下她\x01",
            "刚才悄悄地到街上去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "据说是因为\x01",
            "她的同学也到王都来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_733")

    label("loc_63C")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "因为公主殿下回来了，\x01",
            "我要把这个房间打扫一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "公主殿下她\x01",
            "刚才悄悄地到街上去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "据说是因为\x01",
            "她的同学也到王都来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_733")

    Jump("loc_75B")

    label("loc_736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_740")
    Jump("loc_75B")

    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_74A")
    Jump("loc_75B")

    label("loc_74A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_754")
    Jump("loc_75B")

    label("loc_754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_75B")

    label("loc_75B")

    TalkEnd(0xFE)
    Return()

    # Function_5_5A2 end

    def Function_6_75F(): pass

    label("Function_6_75F")

    EventBegin(0x0)
    OP_6D(-460, 0, 2620, 0)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x138, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x138, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 10, 0, -5370, 225)
    SetChrPos(0x102, 10, 0, -5370, 225)
    SetChrPos(0x138, 10, 0, -5370, 225)

    def lambda_7DB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_7DB)

    def lambda_7ED():
        OP_8E(0xFE, 0xFFFFFFA6, 0x0, 0x564, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_7ED)
    Sleep(500)

    def lambda_80D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_80D)

    def lambda_81F():
        OP_8E(0xFE, 0xFFFFFBF0, 0x0, 0xFFFFFE5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81F)
    Sleep(500)

    def lambda_83F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_83F)

    def lambda_851():
        OP_8E(0xFE, 0x2EE, 0x0, 0xFFFFFE5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_851)
    WaitChrThread(0x138, 0x1)
    OP_8C(0x138, 180, 400)

    ChrTalk(
        0x101,
        (
            "#000F呼～刚才好紧张。\x02\x03",
            "谢谢您，希尔丹夫人，\x01",
            "多亏您的及时相助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F很高明的手腕呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#710F多谢你们的夸奖。\x02\x03",
            "那么……怎么样，\x01",
            "在和陛下见面之前先换衣服吧？\x02\x03",
            "不用特别在意的，\x01",
            "我先带你们去换吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F其实我们只要到了这里就可以……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请务必要带我们去换衣服。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(-52690, 0, 7170, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrPos(0x101, -51850, 0, 7470, 270)
    SetChrPos(0x102, -53280, 0, 7850, 180)
    SetChrPos(0x138, -52990, 0, 5970, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#000F你还真是的，\x01",
            "那么害羞干嘛。\x02\x03",
            "刚才那样不就很好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这可关系到我的信誉啊，\x01",
            "刚才那样是绝对不行的呢。\x02\x03",
            "对了，希尔丹夫人，\x01",
            "这个房间莫非是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#710F嗯……\x01",
            "就是科洛蒂亚公主的房间。\x02\x03",
            "不过她一般不在\x01",
            "王城里面居住，\x01",
            "所以就没有怎么用过……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x138, 400)

    ChrTalk(
        0x101,
        (
            "#000F咦～是这样的啊。\x02\x03",
            "可是，不是说公主殿下\x01",
            "在照顾着陛下的吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#710F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那果然也是假消息。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#710F详细情况你们\x01",
            "就直接询问陛下吧。\x02\x03",
            "在女王宫二楼的就是\x01",
            "艾莉茜雅女王的房间。\x02\x03",
            "我们这就去吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 3)
    SetChrChipByIndex(0x138, 4)
    Return()

    # Function_6_75F end

    def Function_7_CB4(): pass

    label("Function_7_CB4")

    EventBegin(0x0)
    Fade(1000)
    OP_A2(0x644)
    OP_28(0x4A, 0x1, 0x100)
    OP_28(0x4A, 0x1, 0x200)
    SetChrChipByIndex(0x138, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrPos(0x138, -950, 8000, 35250, 0)
    SetChrPos(0x101, -2110, 8000, 34000, 0)
    SetChrPos(0x102, -270, 8000, 34020, 0)
    SetChrPos(0x8, -980, 8000, 38840, 0)
    OP_6D(-570, 8000, 34880, 2000)

    ChrTalk(
        0x138,
        (
            "#710F陛下，打扰了。\x02\x03",
            "我照之前所说的把\x01",
            "艾丝蒂尔和约修亚\x01",
            "带来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "……辛苦你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "请进来吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#710F我明白了。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x138, 0xFFFFF786, 0x1F40, 0x89B2, 0x7D0, 0x0)
    OP_8C(0x138, 180, 400)

    ChrTalk(
        0x138,
        (
            "#710F我就在这里等着。\x02\x03",
            "那么你们俩就进去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F好、好的……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F打扰了……\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(-100970, 0, 4310, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -100980, 0, 20410, 0)
    SetChrPos(0x101, -101650, 0, 3570, 0)
    SetChrPos(0x102, -100450, 0, 3560, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#000F啊……\x02",
    )

    CloseMessageWindow()

    def lambda_ED7():
        OP_6D(-100940, 0, 19690, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_ED7)

    def lambda_EEF():
        OP_6C(12000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_EEF)

    def lambda_EFF():
        OP_67(0, 4200, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_EFF)

    def lambda_F17():
        OP_6E(317, 8000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_F17)
    Sleep(6000)

    def lambda_F2C():
        OP_8E(0xFE, 0xFFFE733E, 0x0, 0x39BC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F2C)

    def lambda_F47():
        OP_8E(0xFE, 0xFFFE797E, 0x0, 0x3AC0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F47)
    Sleep(2000)

    ChrTalk(
        0x8,
        "#090F…………………………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    OP_8C(0x8, 180, 300)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#090F呵呵……\x01",
            "欢迎你们的到来。\x02\x03",
            "我的名字叫做\x01",
            "艾莉茜雅·冯·奥赛雷丝。\x02\x03",
            "利贝尔王国，第２６代国王。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F我、我是……\x01",
            "我是艾丝蒂尔·布莱特。\x02\x03",
            "游击士协会的准游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F同样是准游击士\x01",
            "名叫约修亚·布莱特。\x02\x03",
            "初次见面，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F艾丝蒂尔和约修亚呢。\x02\x03",
            "能和你们两位见面，\x01",
            "我真的很高兴。\x02\x03",
            "没有什么好东西款待你们，\x01",
            "一些茶水微表敬意。\x02\x03",
            "你们就收下，\x01",
            "我们到那边去慢慢谈。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(-106830, 640, 12020, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(240, 0)
    SetChrPos(0x8, -106730, 0, 13420, 180)
    SetChrPos(0x101, -107390, 0, 10600, 0)
    SetChrPos(0x102, -106200, 0, 10610, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#090F这样啊……\x01",
            "拉赛尔博士竟会卷入这样的事。\x02\x03",
            "将一切导力现象停止的\x01",
            "漆黑导力器……\x02\x03",
            "那样的物品竟然\x01",
            "落入了上校手中……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F博士说女王陛下\x01",
            "也许可以知道理查德上校\x01",
            "拿它来做什么。\x02\x03",
            "请问……有什么线索吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F……………………………………\x02\x03",
            "只有一个线索。\x02\x03",
            "不过，我想上校\x01",
            "应该不会知道那一点。\x02\x03",
            "我是不是有些过于担心\x01",
            "了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F那个……\x01",
            "那个线索是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F……对你们说\x01",
            "这些话是没有关系的。\x02\x03",
            "数十年前，在这个王都的地下\x01",
            "检测出了巨大的导力反应。\x02\x03",
            "当时做这项调查的\x01",
            "就是中央工房的拉赛尔博士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F巨大的导力反应……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F所谓王都的地下，\x01",
            "就是地下水路周边吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F不是的，是从比地下水路还要\x01",
            "深很多的地方检测出来的。\x02\x03",
            "博士认为那是至今还没有\x01",
            "失去机能的古代文明遗物\x01",
            "的埋藏之地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F古代文明的遗物……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F就是被称为『古代遗物』\x01",
            "的古代导力器。\x02\x03",
            "其中大部分都如塔顶的装置\x01",
            "那样失去了机能……\x02\x03",
            "另一部分稀少的，就像戴尔蒙市长的\x01",
            "传家宝那样，还继续保持着机能。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F那样的东西在王都地下……\x02\x03",
            "啊，这么说\x01",
            "那个『黑色导力器』就是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F作为将埋藏的遗物的机能\x01",
            "停止来使用的……\x02\x03",
            "这种可能性是有的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F是啊……\x02\x03",
            "可是，那个遗物究竟是什么，\x01",
            "为何会埋藏在那里，\x01",
            "这些都还不清楚。\x02\x03",
            "拉赛尔博士的调查本身\x01",
            "也还在非正式的进行当中……\x02\x03",
            "如果说上校从某个地方得知了其存在，\x01",
            "我认为这也并不是不可能的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是吗……\x02\x03",
            "不管怎样，不好的事情\x01",
            "有可能会因此而导致。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F真是的，稍微想开一点，\x01",
            "不要把事情想的那么严峻嘛……\x02\x03",
            "而且只要人们陷入了困境，\x01",
            "游击士就自然会出现的！\x02\x03",
            "无论如何也会阻止上校的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F呵呵……\x02\x03",
            "不愧是……\x01",
            "卡西乌斯阁下的孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F陛下和父亲\x01",
            "以前曾经认识吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F他是我去世的孩子的朋友，\x01",
            "也是拯救王国的英雄呢。\x02\x03",
            "他辞退了军衔作为游击士时，\x01",
            "还时常帮我办事，承蒙他的关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F是、是这样吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F这我们以前并不知道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F呵呵，以他的性格来看，\x01",
            "你们不知道也是比较正常的。\x02\x03",
            "如果１０年前的战争\x01",
            "没有他的奋力拼搏……\x02\x03",
            "这个地方还会存在吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯……\x01",
            "详细的情况我还是不太清楚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F其实，这就是我的\x01",
            "目的所在……\x02\x03",
            "艾丝蒂尔、约修亚。\x02\x03",
            "你们愿意稍微听一听我这个\x01",
            "上了年纪的人讲过去的故事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊……好的，那是当然！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F洗耳恭听。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#090F这是１０年前的事情……\x02\x03",
            "埃雷波尼亚帝国的南部\x01",
            "发生了一起沉痛的事件，\x01",
            "有一个小村落被全灭。\x02\x03",
            "不是自然灾害或是魔兽的侵害，\x01",
            "而是人为的屠杀。\x02\x03",
            "然后，因为领土紧邻，\x01",
            "帝国政府断定是王国军所为，\x01",
            "于是向利贝尔宣战。\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x4001B, 0x0, 0x0, 0x64)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#090F帝国军在宣战的同时，\x01",
            "集中大量兵力攻破了哈肯大门……\x02\x03",
            "利贝尔除了王都以外的地方\x01",
            "转瞬之间全都被占领了。\x02\x03",
            "而且入侵的兵力是\x01",
            "王国军的３倍以上。\x02\x03",
            "因为王国有屠杀农民的嫌疑，\x01",
            "大陆诸国都采取了旁观的态度……\x02\x03",
            "王都要被占领也\x01",
            "只是时间的问题。\x02",
        )
    )

    CloseMessageWindow()
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x4001C, 0x0, 0x0, 0x64)

    ChrTalk(
        0x8,
        (
            "#090F可是开战的两个月之后……\x02\x03",
            "谁都无法想象的状况\x01",
            "使战局产生了巨大改变。\x02\x03",
            "当时才开发完毕的警备飞艇\x01",
            "将连接各地的关所一一夺回，\x01",
            "切断了帝国军的联络。\x02\x03",
            "接着，从雷斯顿要塞开始，\x01",
            "王国军总兵力乘坐水上艇出击，\x01",
            "将各个地方夺了回来。\x02\x03",
            "蔡斯、卢安、柏斯、洛连特……\x02\x03",
            "切断了占领各地的帝国军师团\x01",
            "的补给来源后，将其各个击破。\x02",
        )
    )

    CloseMessageWindow()
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x4001D, 0x0, 0x0, 0x64)

    ChrTalk(
        0x8,
        (
            "#090F制定这次反攻作战计划的就是\x01",
            "卡西乌斯·布莱特上校——\x02\x03",
            "摩尔根将军的得力助手，\x01",
            "理查德上校的顶头上司，\x01",
            "也就是你们的父亲。\x02\x03",
            "此后不久，在游击士协会\x01",
            "以及七耀教会的仲裁下，\x01",
            "战争终于迎来的结束。\x02\x03",
            "可是就在那时，卡西乌斯阁下\x01",
            "失去了对于他来说最重要的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x4001E, 0x0, 0x0, 0x64)

    ChrTalk(
        0x8,
        (
            "#090F那就是莱娜·布莱特女士……\x01",
            "艾丝蒂尔的母亲。\x02\x03",
            "洛连特的钟楼，在反攻作战时\x01",
            "被走投无路的帝国军师团\x01",
            "恶意报复而破坏了。\x02\x03",
            "而那时……\x01",
            "后面的你们都知道了……\x02\x03",
            "卡西乌斯阁下，甚至连\x01",
            "夫人最后的一眼都没有见到……\x02",
        )
    )

    CloseMessageWindow()
    OP_AE(0x1F4)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#000F……怎么会……………\x02\x03",
            "怎么会这样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F……自己确立的作战计划，\x01",
            "结果却导致了夫人的死去。\x02\x03",
            "因此而深深自责的卡西乌斯阁下\x01",
            "辞去了军衔，走上了游击士的道路。\x02\x03",
            "守护在幸存下来的你的身边……\x02\x03",
            "这样做是为了用自己的双手\x01",
            "来保护心爱的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F笨蛋……爸爸……\x02\x03",
            "因为爸爸的过失而导致\x01",
            "妈妈的离去……\x02\x03",
            "不是这样的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F嗯，是啊……\x02\x03",
            "这一切都是没有实力来\x01",
            "保护自己子民的女王的责任。\x02\x03",
            "对不起，艾丝蒂尔。\x01",
            "我没有保护好你的妈妈……\x02\x03",
            "对于此事……\x01",
            "请接受我深深的歉意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F没、没有必要道歉的！\x02\x03",
            "女王陛下一直守护着\x01",
            "这来之不易的和平……\x02\x03",
            "爸爸他们拼死守护着\x01",
            "这个国家……\x02\x03",
            "妈妈换来的生命\x01",
            "由我来守护……\x02\x03",
            "这样就可以了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F艾丝蒂尔……\x01",
            "谢谢，你是个优秀的孩子……\x02\x03",
            "能够见到你们\x01",
            "真是太好了……\x02\x03",
            "我发自心底的这么认为。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F女王陛下……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F不过，正因为如此……\x02\x03",
            "正因为如此，我不希望\x01",
            "你们遇到任何危险。\x02\x03",
            "在卡西乌斯阁下外出的时候，\x01",
            "你们俩万一出了什么事情，\x01",
            "让我怎么交待……\x02\x03",
            "因此，请你们回到洛连特的家中\x01",
            "等待你们的父亲回来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F可、可是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F可是，女王陛下……\x02\x03",
            "由父亲卡西乌斯取回的、\x01",
            "陛下您一直守护着的和平\x01",
            "现在即将开始动摇了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#090F约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F因为『黑色导力器』所带来的事件……\x02\x03",
            "就这样下去，上校一旦达成\x01",
            "让公爵大人成为国王的目的时，\x01",
            "现在的和平会变成什么样的呢？\x02\x03",
            "请您务必要考虑一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#090F…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F对、对不起，女王陛下……\x02\x03",
            "我们两个自从成为游击士以来，\x01",
            "就作为爸爸的代理完成任务。\x02\x03",
            "从那时开始，空贼事件，\x01",
            "传递信件，打开奇怪的小包裹，\x01",
            "就这样在各地游历……\x02\x03",
            "感觉就好像是被爸爸背着\x01",
            "来到这里的一样。\x02\x03",
            "所以……我也想要守护着。\x02\x03",
            "这和平的、幸福的每一天……\x02\x03",
            "以及这一路上所认识的，\x01",
            "关心我、喜欢我的人们……\x02\x03",
            "女王殿下也好，像我的妈妈那样的人\x01",
            "也好，我会用自己的方法来守护着的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F艾丝蒂尔……\x02\x03",
            "…………………………\x02\x03",
            "的确……\x01",
            "和那个孩子所说的一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F我也终于明白了。\x02\x03",
            "我想通过艾丝蒂尔你们\x01",
            "向游击士协会委托\x01",
            "一些需要解决的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F女王陛下……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F陛下……\x01",
            "请您尽管吩咐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F委托的内容就是：将被情报部\x01",
            "囚禁的人们救出来。\x02\x03",
            "其中还包含我的孙女\x01",
            "科洛蒂娅公主。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，公主殿下果然\x01",
            "被抓到某个地方去了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F是啊……\x02\x03",
            "回想起来，这次的政变是\x01",
            "因为我要推选那个孩子\x01",
            "作为新一代国王而开始的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F不是杜南公爵对吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F嗯，虽说他是我的\x01",
            "外甥，但杜南公爵\x01",
            "是个问题多多的人物。\x02\x03",
            "相比之下，虽说不算很成熟，\x01",
            " \x02\x03",
            "在考虑了王国的未来之后……\x01",
            "我做出的决定就是\x01",
            "选择科洛蒂娅公主。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，公主的事情\x01",
            "我不是很了解……\x02\x03",
            "不过不管怎么说，做出\x01",
            "这样的决定应该是正确的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F呵呵，可是无论何时，这个世界\x01",
            "总是倾向于对女性当权\x01",
            "持反对的态度。\x02\x03",
            "何况，对于被大国侵略\x01",
            "的过去还记忆犹新的今天……\x02\x03",
            "连续２代都由女王来统治，\x01",
            "结果只会导致国力的衰弱……\x02\x03",
            "抱有这种想法的人物会出现，\x01",
            "也没有什么不可思议的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此……\x01",
            "那样的人物就是理查德上校吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F是的。\x02\x03",
            "我想推选科洛蒂娅\x01",
            "作为新一代国王的想法\x01",
            "不知何时被他得知了。\x02\x03",
            "于是他就把这件事告诉了公爵，\x01",
            "然后发动了这次政变。\x02\x03",
            "实际上是为了暗中操纵公爵，\x01",
            "把利贝尔变成不弱于周边大国\x01",
            "的强大军事国家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此……\x02\x03",
            "终于明白这次\x01",
            "事件的全貌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F变成强大的军事国家……\x01",
            "具体是要怎么做呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F会有各种各样的做法。\x02\x03",
            "提高税率，\x01",
            "增大军费开支……\x02\x03",
            "开发大量的以破坏为目的\x01",
            "的导力兵器……\x02\x03",
            "采取大规模的征兵制……\x02\x03",
            "转变成可以和利贝尔不予以认可的\x01",
            "猎兵团签订合法契约……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F怎、怎么会……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F的确，与之类似的要求\x01",
            "上校也向我提出过。\x02\x03",
            "虽说这也是出自纯粹的爱国心\x01",
            "的一番话……\x02\x03",
            "但是我无论如何\x01",
            "也不认为那是正确的。\x02\x03",
            "要守护国家，\x01",
            "仅靠军事力量是不行的。\x02\x03",
            "和他国协调好关系，\x01",
            "在外交上努力一点……\x02\x03",
            "加强技术交流、经济交流，\x01",
            "可以让全国各地更加繁荣，\x01",
            "也就可以牢固的守卫国家了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F……陛下所说的\x01",
            "的确才是有道理的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯嗯！\x01",
            "不谋而合！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F但是，上校一口断定这是\x01",
            "带有妇人之见的理想论。\x02\x03",
            "而且还以科洛蒂娅的安全\x01",
            "来要挟我退位。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F大部分掌权者的亲人都被\x01",
            "作为了人质，所以不敢违抗上校。\x02\x03",
            "可我是女王。\x01",
            "不能因为骨肉之情而\x01",
            "出卖国家的未来。\x02\x03",
            "话虽然这么说，但那个孩子\x01",
            "是我唯一的一个孙女……\x02\x03",
            "我不能见死不救啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F女王陛下……\x01",
            "请您放心吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F您委托的旨意，我们已经清楚的知道了。\x02\x03",
            "一定会将包括公主殿下在内的\x01",
            "所有人质救出来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F非常感谢……\x01",
            "艾丝蒂尔、约修亚。\x02\x03",
            "这样一来，上校的要挟\x01",
            "始终都不会让我屈服的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F请、请问，\x01",
            " \x02\x03",
            "还有『黑色导力器』那件事……\x02\x03",
            "如果现在要帮助女王陛下您逃离这里，\x01",
            "我认为也不是不可能的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F谢谢你，艾丝蒂尔。\x02\x03",
            "不过，我如果逃离了，\x01",
            "也并不能改变局势。\x02\x03",
            "而且这件事究竟与『黑色导力器』有着\x01",
            "怎样的联系，对此我很在意。\x02\x03",
            "我要向上校问清楚\x01",
            "他的真实意图所在。\x02\x03",
            "请理解我的心意。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(-52350, 0, 6280, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x138, 0)
    SetChrPos(0x101, -53470, 0, 6160, 90)
    SetChrPos(0x102, -51450, 0, 6000, 270)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#000F哈～真是一位\x01",
            "充满魅力的女性啊～\x02\x03",
            "和蔼可亲而又内心坚强，\x01",
            "相当的坚毅啊……\x02\x03",
            "等我到了那个年纪时\x01",
            "也要成为那样\x01",
            "优雅的老奶奶呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F优雅……\x02\x03",
            "不过的确是很有一国之主\x01",
            "风范的一位女性呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯……\x02\x03",
            "真想这就阻止政变，\x01",
            "救出女王陛下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F其实这并不属于游击士\x01",
            "的管辖范围的呢……\x02\x03",
            "不过无论如何，也让我们\x01",
            "尽力去完成吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯……没错。\x02\x03",
            "还有就是从女王那里\x01",
            "听说的父亲所做的事，\x01",
            "简直就像是在做梦一样……\x02\x03",
            "还会有我不知道的事情\x01",
            "冒出来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F……说不定呢。\x02",
    )

    CloseMessageWindow()
    OP_9F(0x138, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x138, -51030, 0, 420, 225)

    ChrTalk(
        0x138,
        (
            "料理还在准备中，\x02\x03",
            "你们准备完毕了吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_42D5():
        TurnDirection(0xFE, 0x138, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42D5)
    TurnDirection(0x101, 0x138, 400)

    ChrTalk(
        0x101,
        "#000F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    def lambda_42FE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_42FE)

    def lambda_4310():
        OP_8E(0xFE, 0xFFFF34A4, 0x0, 0xF96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_4310)

    def lambda_432B():

        label("loc_432B")

        TurnDirection(0xFE, 0x138, 0)
        OP_48()
        Jump("loc_432B")

    QueueWorkItem2(0x101, 1, lambda_432B)

    def lambda_433C():

        label("loc_433C")

        TurnDirection(0xFE, 0x138, 0)
        OP_48()
        Jump("loc_433C")

    QueueWorkItem2(0x102, 1, lambda_433C)
    Sleep(300)
    OP_6D(-52330, 0, 5310, 1000)
    WaitChrThread(0x138, 0x1)

    ChrTalk(
        0x138,
        (
            "#710F那我们就立刻\x01",
            "回休息室去吧。\x02\x03",
            "已经１１点过了……\x01",
            "再过一会就是新的一天了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哇啊，已经这么晚了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F过了很长的时间呢，\x01",
            "当我们在和陛下聊天时。\x02\x03",
            "如果在这么待下去，\x01",
            "看守就会觉得可疑了。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    EventEnd(0x0)
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 1)
    SetChrChipByIndex(0x138, 2)
    OP_1B(0x2, 0x0, 0xFFFF)
    Return()

    # Function_7_CB4 end

    def Function_8_449F(): pass

    label("Function_8_449F")

    ClearMapFlags(0x10000000)
    OP_28(0x4E, 0x1, 0x4)
    EventBegin(0x0)
    OP_6D(1080, 0, 3170, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(2190, 0)
    OP_6C(44000, 0)
    OP_6E(426, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, 0, 0, 9760, 180)
    SetChrPos(0xB, -1480, 0, 9280, 180)
    SetChrPos(0xD, 0, 0, 8350, 180)
    SetChrPos(0xE, 1400, 0, 9310, 180)
    SetChrPos(0x101, -90, 0, 920, 0)
    SetChrPos(0x105, -1330, 0, 430, 0)
    SetChrPos(0x103, 930, 0, 430, 0)
    SetChrChipByIndex(0x101, 9)
    SetChrChipByIndex(0x103, 11)
    SetChrChipByIndex(0x105, 13)
    FadeToBright(1000, 0)
    OP_6D(1130, 0, 6000, 1000)

    ChrTalk(
        0x9,
        (
            "#224F叛、叛逆者！\x01",
            "居然恬不知耻地跑到这里来了！？\x02\x03",
            "明知我是将要继承王位的人，\x01",
            "你们还要动粗吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F#2P别说笑了，你那发型已经够搞笑了。\x02\x03",
            "你现在已经再也不可能成为国王了，\x01",
            "真正的下任国王在我们身旁。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#226F什、什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F#2P您是杜南公爵吧。\x01",
            "我们是游击士协会派来的人。\x02\x03",
            "科洛蒂娅殿下委托我们来救出女王陛下。\x01",
            "　\x02\x03",
            "#021F如果您能通融一下，\x01",
            "那我们也不会为难您的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#222F科、科洛蒂娅！？\x02\x03",
            "那个小姑娘……\x01",
            "简直就是碍手碍脚的家伙！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F#2P杜南王叔……\x01",
            "请您不要再执迷不悟了好吗？\x02\x03",
            "王叔，\x01",
            "您已经被理查德上校给利用了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#223F你、你是谁啊……\x02\x03",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#222F你、你、你……\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x9,
        "#224F#3S你不是科洛蒂娅吗！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x9,
        "#226F那样的发型和装扮，像个什么样子！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#2P终于发觉了啊……\x02\x03",
            "反应这么慢……\x01",
            "怪不得你在卢安没能注意到啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F#2P虽然我对您不是很了解，\x01",
            "不过的确是个很迟钝的人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#542F#2P对不起，一直瞒着您这件事，\x01",
            "都是我的不好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#226F根、根本就是把我当傻瓜来耍！\x01",
            "　\x02\x03",
            "这就是为何女人这种生物\x01",
            "不可信任的原因啊！\x02\x03",
            "狡猾、小气、为一些不值得的\x01",
            "小事情故意找碴儿……\x02\x03",
            "怎能把王冠交给这样无聊的家伙呢！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#2P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#024F#2P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#043F#2P…………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#223F……嗯……不过………\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0xB,
        (
            "#5P殿、殿下……\x01",
            "情况不妙啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5P还、还是投降吧……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101)
    OP_63(0x105)
    OP_63(0x103)

    ChrTalk(
        0x101,
        "#001F#2P哈哈……真是没用的手下啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F#2P哎呀呀，看来我得对你另眼相看了。\x02\x03",
            "在这样的时代里，\x01",
            "竟然还会有人敢做出如此臆断的发言。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#542F#2P对、对不起了王叔。\x02\x03",
            "#045F这回有点儿……\x01",
            "我也没办法帮您求情了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4D11():
        OP_6D(420, 0, 10250, 700)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D11)

    def lambda_4D29():
        OP_8E(0xFE, 0x122, 0x0, 0x59A6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D29)
    Sleep(50)

    def lambda_4D49():
        OP_8E(0xFE, 0x122, 0x0, 0x59A6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4D49)
    Sleep(50)

    def lambda_4D69():
        OP_8E(0xFE, 0x122, 0x0, 0x59A6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4D69)
    Sleep(500)
    OP_44(0x101, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x105, 0xFF)
    Battle(0x3AA, 0x0, 0x0, 0x2, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_4DA8"),
        (SWITCH_DEFAULT, "loc_4DAB"),
    )


    label("loc_4DA8")

    OP_B4(0x0)
    Return()

    label("loc_4DAB")

    EventBegin(0x0)
    OP_6D(-2360, 0, 10280, 0)
    OP_67(0, 5270, -10000, 0)
    OP_6B(3260, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0xB, -5180, 0, 11510, 90)
    SetChrPos(0xD, -3130, 0, 13730, 262)
    SetChrPos(0xE, -5030, 0, 13030, 135)
    SetChrChipByIndex(0xB, 20)
    SetChrChipByIndex(0xD, 20)
    SetChrChipByIndex(0xE, 20)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xE, 0x1)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xD, 0x800)
    SetChrFlags(0xE, 0x800)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E6A")
    SetChrPos(0x9, -4810, 0, 7920, 90)
    Jump("loc_4E90")

    label("loc_4E6A")

    SetChrPos(0x9, -6370, 0, 7980, 90)
    SetChrFlags(0x9, 0x20)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 21)

    label("loc_4E90")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_4E9C"),
        (SWITCH_DEFAULT, "loc_57F9"),
    )


    label("loc_4E9C")

    SetChrPos(0x101, -2120, 0, 8860, 0)
    SetChrPos(0x105, -850, 0, 8130, 0)
    SetChrPos(0x103, -2400, 0, 7180, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_2B(0x4D, 0x2)

    ChrTalk(
        0x101,
        (
            "#502F#2P好的，解决了！\x02\x03",
            "#006F接下来，该轮到公爵您了吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F4C():
        OP_6D(-5080, 0, 8690, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4F4C)

    def lambda_4F64():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F64)
    Sleep(50)

    def lambda_4F77():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4F77)
    Sleep(50)

    def lambda_4F8A():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4F8A)
    OP_8F(0x9, 0xFFFFEA34, 0x0, 0x1F18, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x103,
        (
            "#027F#2P由女人手中挥出的鞭子，\x01",
            "想不想品尝一下是什么滋味呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0x9, 0xFFFFE6E2, 0x0, 0x1EB4, 0x7D0, 0x0)

    ChrTalk(
        0x9,
        (
            "#226F哇、哇呀呀呀呀呀……\x02\x03",
            "不要过来、不要靠近我呀啊啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F对不起……\x01",
            "请您原谅我们吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#222F可恶，这样的话，\x01",
            "我就只好拿陛下当盾牌……\x02\x03",
            "#224F……嘿～哈～喝！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_50F3():
        OP_8C(0xFE, 270, 800)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_50F3)
    OP_8F(0x9, 0xFFFFDFC6, 0x0, 0x1EDC, 0x1770, 0x0)
    OP_22(0x7D, 0x0, 0x64)

    ChrTalk(
        0x9,
        "#228F#10A呜……\x05\x02",
    )


    def lambda_5144():
        OP_8C(0xFE, 800, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5144)
    OP_96(0x9, 0xFFFFE462, 0x0, 0x1F2C, 0x320, 0x1F40)

    def lambda_5169():
        OP_8C(0xFE, 800, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5169)
    OP_96(0x9, 0xFFFFE71E, 0x0, 0x1F2C, 0x190, 0x1F40)
    OP_22(0x30, 0x0, 0x64)
    OP_62(0x9, 0x12C, 1600, 0x30, 0x32, 0x96, 0x0)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x20)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 21)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x105, 65535)

    def lambda_521D():
        OP_6D(-5790, 0, 8440, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_521D)

    def lambda_5235():
        OP_8E(0xFE, 0xFFFFE94E, 0x0, 0x245E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5235)
    Sleep(200)

    def lambda_5255():
        OP_8E(0xFE, 0xFFFFECD2, 0x0, 0x1C84, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5255)
    Sleep(200)

    def lambda_5275():
        OP_8E(0xFE, 0xFFFFEE30, 0x0, 0x22A6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5275)

    def lambda_5290():

        label("loc_5290")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_5290")

    QueueWorkItem2(0x101, 1, lambda_5290)

    def lambda_52A1():

        label("loc_52A1")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_52A1")

    QueueWorkItem2(0x103, 1, lambda_52A1)

    def lambda_52B2():

        label("loc_52B2")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_52B2")

    QueueWorkItem2(0x105, 1, lambda_52B2)
    WaitChrThread(0x101, 0x2)
    OP_63(0x9)

    ChrTalk(
        0x101,
        (
            "#007F哎呀……\x01",
            "这家伙好像受惊过度了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F不过他确实阻碍我们了，\x01",
            "这不是个很有意思的教训吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#047F嗯……\x01",
            "真是不幸的事件啊。\x02\x03",
            "#049F可是……难道……\x01",
            "就让王叔昏迷在这里行吗……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -490, 0, -530, 270)
    OP_4A(0xA, 255)

    NpcTalk(
        0xA,
        "男性的声音",
        "#1P……公、公爵大人！？　　　\x02",
    )

    CloseMessageWindow()

    def lambda_5435():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5435)

    def lambda_5443():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5443)

    def lambda_5451():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5451)

    def lambda_545F():
        OP_8E(0xA, 0xFFFFE73C, 0x0, 0x1C7A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_545F)
    OP_6D(-2009, 0, 6520, 1000)
    Sleep(200)

    def lambda_5490():

        label("loc_5490")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_5490")

    QueueWorkItem2(0x101, 1, lambda_5490)

    def lambda_54A1():

        label("loc_54A1")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_54A1")

    QueueWorkItem2(0x103, 1, lambda_54A1)

    def lambda_54B2():

        label("loc_54B2")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_54B2")

    QueueWorkItem2(0x105, 1, lambda_54B2)

    def lambda_54C3():
        OP_6D(-5850, 0, 8290, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_54C3)
    WaitChrThread(0xA, 0x1)
    TurnDirection(0xA, 0x9, 800)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x101,
        "#004F啊，是菲利普先生！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x105, 400)

    ChrTalk(
        0xA,
        (
            "#722F艾丝蒂尔小姐……\x01",
            "还有科洛蒂娅公主……\x02\x03",
            "对于这次我家主人的执迷不悟，\x01",
            "我感到非常的抱歉！\x02\x03",
            "这一切都是因为我没有\x01",
            "好好教导大人而导致的……\x02\x03",
            "#723F因此，如果你们要惩罚的话，\x01",
            "就请惩罚在下吧！　　\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "菲利普向艾丝蒂尔等人深深地低下了头。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#004F等、等一下！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#048F菲利普先生……\x01",
            "请您先抬起头来吧。\x02\x03",
            "我们一行人，是为了救祖母……\x01",
            "是为了营救女王陛下而赶来的。\x02\x03",
            "原本就和王叔是没有任何牵连的。\x01",
            "　\x02\x03",
            "因此，菲利普先生……\x01",
            "请把王叔送到我的房间养伤吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#721F公、公主殿下……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F事实上他没有受到什么伤害哦。\x02\x03",
            "就只是因为突然受惊而昏厥，\x01",
            "过一会儿就没事的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#722F大、大家……\x01",
            "真是太感谢了。\x02\x03",
            "你们的大恩大德，我决对不会忘记的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E33")

    label("loc_57F9")

    SetChrPos(0x101, -5810, 0, 9310, 315)
    SetChrPos(0x105, -4910, 0, 7300, 336)
    SetChrPos(0x103, -4560, 0, 8870, 296)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x105, 65535)
    OP_6D(-5790, 0, 8440, 0)

    def lambda_5852():

        label("loc_5852")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_5852")

    QueueWorkItem2(0x101, 1, lambda_5852)

    def lambda_5863():

        label("loc_5863")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_5863")

    QueueWorkItem2(0x103, 1, lambda_5863)

    def lambda_5874():

        label("loc_5874")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_5874")

    QueueWorkItem2(0x105, 1, lambda_5874)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#007F呼～～\x01",
            "想不到连公爵也一起打晕了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F如果可以办到的话，\x01",
            "倒是只需要打倒特务兵就行了……\x02\x03",
            "#021F不过他确实阻碍我们了，\x01",
            "这不是个很有意思的教训吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#047F嗯……\x01",
            "真是不幸的事件啊。\x02\x03",
            "#049F可是……难道……\x01",
            "就让王叔昏迷在这里行吗……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -490, 0, -530, 270)
    OP_4A(0xA, 255)

    NpcTalk(
        0xA,
        "男性的声音",
        "#1P……公、公爵大人！？　　　\x02",
    )

    CloseMessageWindow()

    def lambda_5A47():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A47)

    def lambda_5A55():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A55)

    def lambda_5A63():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5A63)

    def lambda_5A71():
        OP_8E(0xA, 0xFFFFE73C, 0x0, 0x1C7A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5A71)
    OP_6D(-2009, 0, 6520, 1000)
    Sleep(200)

    def lambda_5AA2():

        label("loc_5AA2")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_5AA2")

    QueueWorkItem2(0x101, 1, lambda_5AA2)

    def lambda_5AB3():

        label("loc_5AB3")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_5AB3")

    QueueWorkItem2(0x103, 1, lambda_5AB3)

    def lambda_5AC4():

        label("loc_5AC4")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_5AC4")

    QueueWorkItem2(0x105, 1, lambda_5AC4)

    def lambda_5AD5():
        OP_6D(-5850, 0, 8290, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5AD5)
    WaitChrThread(0xA, 0x1)
    TurnDirection(0xA, 0x9, 800)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x101,
        "#004F啊，是菲利普先生！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x105, 400)

    ChrTalk(
        0xA,
        (
            "#722F艾丝蒂尔小姐……\x01",
            "还有科洛蒂娅公主……\x02\x03",
            "对于这次我家主人的执迷不悟，\x01",
            "我感到非常的抱歉！\x02\x03",
            "这一切都是因为我没有\x01",
            "好好教导大人而导致的……\x02\x03",
            "#723F因此，如果你们要惩罚的话，\x01",
            "就请惩罚在下吧！　　\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "菲利普向艾丝蒂尔等人深深地低下了头。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#004F等、等一下！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#048F菲利普先生……\x01",
            "请您先抬起头来吧。\x02\x03",
            "我们一行人，是为了救祖母……\x01",
            "是为了营救女王陛下而赶来的。\x02\x03",
            "原本就和王叔是没有任何牵连的。\x01",
            "　\x02\x03",
            "因此，菲利普先生……\x01",
            "请把王叔送到我的房间养伤吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#721F公、公主殿下……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F事实上他没有受什么重伤哦。\x02\x03",
            "只是因为受了点打击昏过去了，\x01",
            "过一会儿就没事的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#722F大、大家……\x01",
            "真是太感谢了。\x02\x03",
            "你们的大恩大德，我决对不会忘记的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E33")

    label("loc_5E33")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x9, -52830, 0, 7650, 179)
    SetChrPos(0xA, -53810, 0, 7520, 79)
    OP_63(0x9)
    OP_6D(-5920, 0, 8680, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    SetChrPos(0x101, -5920, 0, 8680, 0)
    SetChrPos(0x105, -5920, 0, 8680, 0)
    SetChrPos(0x103, -5920, 0, 8680, 0)
    FadeToBright(1000, 0)
    OP_A2(0x665)
    EventEnd(0x0)
    Return()

    # Function_8_449F end

    def Function_9_5EEE(): pass

    label("Function_9_5EEE")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 9)
    SetChrChipByIndex(0x103, 11)
    SetChrChipByIndex(0x105, 13)
    OP_6D(-100980, 0, 8360, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -101110, 0, 3990, 0)
    SetChrPos(0x103, -102060, 0, 2930, 0)
    SetChrPos(0x105, -100330, 0, 2930, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#000F一个人也没有？！（※仮）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F肯定是在里面的阳台！（※仮）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x680)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x105, 65535)
    EventEnd(0x0)
    Return()

    # Function_9_5EEE end

    def Function_10_5FF6(): pass

    label("Function_10_5FF6")

    ClearMapFlags(0x2000000)
    OP_1B(0x5, 0x0, 0xFFFF)
    Return()

    # Function_10_5FF6 end

    def Function_11_6001(): pass

    label("Function_11_6001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6088")
    EventBegin(0x1)
    TurnDirection(0x138, 0x101, 400)

    NpcTalk(
        0x0,
        "希尔丹夫人",
        (
            "#710F女王陛下的房间\x01",
            "就在这个女王宫的二楼。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_6088")

    Return()

    # Function_11_6001 end

    SaveToFile()

Try(main)
