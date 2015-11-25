from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3116   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3116.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        '拉赛尔博士',                           # 9
        '提妲',                                 # 10
        '玛多克工房长',                         # 11
        '加鲁诺',                               # 12
        '普罗梅笛',                             # 13
        '安东尼',                               # 14
        '导力器',                               # 15
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
        'ED6_DT07/CH02020 ._CH',             # 00
        'ED6_DT07/CH00060 ._CH',             # 01
        'ED6_DT07/CH02620 ._CH',             # 02
        'ED6_DT07/CH01190 ._CH',             # 03
        'ED6_DT07/CH01100 ._CH',             # 04
        'ED6_DT07/CH01700 ._CH',             # 05
        'ED6_DT06/CH20021 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02020P._CP',             # 00
        'ED6_DT07/CH00060P._CP',             # 01
        'ED6_DT07/CH02620P._CP',             # 02
        'ED6_DT07/CH01190P._CP',             # 03
        'ED6_DT07/CH01100P._CP',             # 04
        'ED6_DT07/CH01700P._CP',             # 05
        'ED6_DT06/CH20021P._CP',             # 06
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 20,
        Z                   = 700,
        Y                   = 39430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 917510,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1C2",          # 00, 0
        "Function_1_3E3",          # 01, 1
        "Function_2_497",          # 02, 2
        "Function_3_4AD",          # 03, 3
        "Function_4_4D1",          # 04, 4
        "Function_5_4F1",          # 05, 5
        "Function_6_633",          # 06, 6
        "Function_7_188E",         # 07, 7
        "Function_8_1974",         # 08, 8
        "Function_9_1A47",         # 09, 9
        "Function_10_1B10",        # 0A, 10
        "Function_11_2E1E",        # 0B, 11
        "Function_12_41CA",        # 0C, 12
        "Function_13_4218",        # 0D, 13
        "Function_14_4243",        # 0E, 14
        "Function_15_426E",        # 0F, 15
        "Function_16_42AD",        # 10, 16
        "Function_17_4BD0",        # 11, 17
    )


    def Function_0_1C2(): pass

    label("Function_0_1C2")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1CE"),
        (SWITCH_DEFAULT, "loc_210"),
    )


    label("loc_1CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E1")
    OP_A2(0x513)
    Event(0, 10)

    label("loc_1E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FA")
    SetMapFlags(0x10000000)
    Event(0, 11)

    label("loc_1FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20D")
    OP_A2(0x531)
    Event(0, 16)

    label("loc_20D")

    Jump("loc_210")

    label("loc_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_230")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -4500, 0, 6620, 99)
    Jump("loc_3E2")

    label("loc_230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_250")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -4500, 0, 6620, 99)
    Jump("loc_3E2")

    label("loc_250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_270")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -4500, 0, 6620, 99)
    Jump("loc_3E2")

    label("loc_270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2A6")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -4500, 0, 6620, 99)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -90, 0, 9830, 355)
    Jump("loc_3E2")

    label("loc_2A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_2CD")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 670, 0, 8480, 6)
    OP_43(0xD, 0x0, 0x0, 0x3)
    Jump("loc_3E2")

    label("loc_2CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2D7")
    Jump("loc_3E2")

    label("loc_2D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_332")
    SetChrPos(0xE, 40, 800, 11550, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0x8, 140, 0, 12690, 175)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32F")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -130, 0, 10450, 0)

    label("loc_32F")

    Jump("loc_3E2")

    label("loc_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_37E")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -100, 0, 12700, 180)
    SetChrPos(0x8, -2310, 0, 14200, 0)
    SetChrPos(0xE, 40, 800, 11550, 0)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_3E2")

    label("loc_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3A5")
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0x8, 140, 0, 12690, 175)
    Jump("loc_3E2")

    label("loc_3A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3C5")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -4500, 0, 6620, 99)
    Jump("loc_3E2")

    label("loc_3C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3E2")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -4500, 0, 6620, 99)

    label("loc_3E2")

    Return()

    # Function_0_1C2 end

    def Function_1_3E3(): pass

    label("Function_1_3E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_428")

    label("loc_3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_413")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_428")

    label("loc_413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_428")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48A")
    LoadEffect(0x1, "map\\\\mpfog.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_48A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_496")
    OP_72(0x0, 0x4)

    label("loc_496")

    Return()

    # Function_1_3E3 end

    def Function_2_497(): pass

    label("Function_2_497")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_497")

    label("loc_4AC")

    Return()

    # Function_2_497 end

    def Function_3_4AD(): pass

    label("Function_3_4AD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D0")
    OP_8D(0xFE, -1710, 9770, 3200, 6310, 3000)
    Jump("Function_3_4AD")

    label("loc_4D0")

    Return()

    # Function_3_4AD end

    def Function_4_4D1(): pass

    label("Function_4_4D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_4ED")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xFE,
        "喵～……\x02",
    )

    CloseMessageWindow()

    label("loc_4ED")

    TalkEnd(0xFE)
    Return()

    # Function_4_4D1 end

    def Function_5_4F1(): pass

    label("Function_5_4F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_62F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_59D")

    ChrTalk(
        0xFE,
        (
            "拉赛尔博士\x01",
            "好像已经回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我本来还想请他\x01",
            "给我们多提一些建议的，\x01",
            "这次还是算了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "只能以后有机会再说了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_62F")

    label("loc_59D")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "哦？\x01",
            "拉赛尔博士好像已经回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次这么早就\x01",
            "结束了研究工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀～\x01",
            "真的是难得一见呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62F")

    TalkEnd(0xFE)
    Return()

    # Function_5_4F1 end

    def Function_6_633(): pass

    label("Function_6_633")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_7B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6BD")

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "拉赛尔博士到底去了哪里呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我倒是希望他能够\x01",
            "好好地收拾一下试验用具。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B3")

    label("loc_6BD")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "现在我正在重新\x01",
            "对导力枪进行设计……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过还是有些不舍得\x01",
            "对已经成熟的设计\x01",
            "做大幅度的改动啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼……这下子\x01",
            "说不定会比从图纸开始\x01",
            "重新设计还要麻烦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B3")

    Jump("loc_188A")

    label("loc_7B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_8C2")

    ChrTalk(
        0xFE,
        (
            "现在处于研究阶段的导力枪的\x01",
            "平衡性出了一些问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，如果能够做得更加易用，\x01",
            "说不定会成为十分畅销的商品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "到底是注重性能，\x01",
            "还是注重易用性呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个抉择太难了，\x01",
            "还是先考虑二者兼顾吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188A")

    label("loc_8C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_B49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A01")

    ChrTalk(
        0xFE,
        (
            "为了下一次的研究，\x01",
            "我已经开始整理相关资料了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次应该会以易用性\x01",
            "作为追求的目标吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其实老实说，\x01",
            "到底应该注重哪一方面的设计\x01",
            "连我自己也不是很清楚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正因如此，对我们技术人员来说，\x01",
            "这一难题才有挑战的价值。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B46")

    label("loc_A01")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "哟，早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从昨天开始，\x01",
            "我就在整理关于下一次研究主题的资料了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次应该会以易用性\x01",
            "作为追求的目标吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其实老实说，\x01",
            "到底应该注重哪一方面的设计\x01",
            "连我自己也不是很清楚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正因如此，对我们技术人员来说，\x01",
            "这一难题才有挑战的价值。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B46")

    Jump("loc_188A")

    label("loc_B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_E6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CAF")

    ChrTalk(
        0xFE,
        (
            "今天，有位客人在维修柜台\x01",
            "打听易用的照相机，\x01",
            "我就向其介绍了相关的商品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，易用这一特性\x01",
            "用数字是表现不出来的。\x01",
            "结果我还是没有办法说清楚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然武器店的老板\x01",
            "叮嘱我说要基于\x01",
            "能让更多人使用这一点来考虑……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过我还是不能理解\x01",
            "他这句话的含义。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6B")

    label("loc_CAF")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "……唉，真难办啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天，我在维修柜台\x01",
            "向一位客人介绍了相关的商品……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是我不管怎么介绍商品的高性能，\x01",
            "也不能使客人满意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像那位客人想要的是\x01",
            "使用起来非常方便的照相机……\x01",
            "不过易用性用数字是表现不出来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然武器店的老板\x01",
            "叮嘱我说要基于\x01",
            "能让更多人使用这一点来考虑……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过我还是不能理解\x01",
            "他这句话的含义。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6B")

    Jump("loc_188A")

    label("loc_E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1404")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1310")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 5)), scpexpr(EXPR_END)), "loc_F8D")

    ChrTalk(
        0xFE,
        (
            "导力枪的研究\x01",
            "我觉得还算是比较顺利吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一些细节部分\x01",
            "看来还需要些时间来完善，\x01",
            "但是不管怎么说大体已经成形了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "照这个势头研发的话，\x01",
            "会比我预计的更早出现在商店货架上哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且发售的时候\x01",
            "商品也会包装得更可爱一点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_130D")

    label("loc_F8D")

    OP_A2(0x585)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD2")

    ChrTalk(
        0xFE,
        (
            "啊，提妲。\x01",
            "哎，还有这几位……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "哎呀，你们是……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FE6")

    label("loc_FD2")


    ChrTalk(
        0xFE,
        "哎呀，你们就是……\x02",
    )

    CloseMessageWindow()

    label("loc_FE6")


    ChrTalk(
        0x101,
        "#501F嗯？怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F说起来……\x02\x03",
            "我们好像\x01",
            "在卢安见过面吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "啊，果然是你们呀。\x01",
            "那时候真是给你们添麻烦了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "来，要不要看看\x01",
            "我做的导力枪的试验品啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊，我也想起来了。\x01",
            "你就是那时候的学者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F对了，\x01",
            "加鲁诺先生，您好像说过。\x02\x03",
            "在去卢安的途中\x01",
            "把导力枪试制品丢掉了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(
        0xFE,
        (
            "哎呀～\x01",
            "那一次可真是被逼到绝路了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真的是得救了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F在那之后\x01",
            "你的研究进行得如何了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "我觉得还算是比较顺利吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一些细节部分\x01",
            "看来还需要些时间来完善，\x01",
            "但是不管怎么说大体已经成形了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "照这个势头研发的话，\x01",
            "会比我预计的更早出现在商店货架上哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且发售的时候\x01",
            "商品也会包装得更可爱一点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_130D")

    Jump("loc_1401")

    label("loc_1310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1371")

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "现在可不是发呆的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要赶快把改良方案\x01",
            "确定下来才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1401")

    label("loc_1371")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "呼～……\x01",
            "露依赛重新把试制品做了出来，\x01",
            "真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没有样品的话，\x01",
            "研究就没办法进行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1401")

    Jump("loc_188A")

    label("loc_1404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_188A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1799")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 5)), scpexpr(EXPR_END)), "loc_1523")

    ChrTalk(
        0xFE,
        (
            "导力枪的研究\x01",
            "我觉得还算是比较顺利吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一些细节部分\x01",
            "看来还需要些时间来完善，\x01",
            "但是不管怎么说大体已经成形了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "照这个势头研发的话，\x01",
            "会比我预计的更早出现在商店货架上哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且发售的时候\x01",
            "商品也会包装得更可爱一点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1796")

    label("loc_1523")

    OP_A2(0x585)

    ChrTalk(
        0xFE,
        "哎呀，你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F嗯？怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F说起来……\x02\x03",
            "我们好像\x01",
            "在卢安见过面吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "啊，我记起来了。\x01",
            "那时候真是给你们添麻烦了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "来，要不要看看我做的\x01",
            "导力枪的试验品啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊，我也想起来了。\x01",
            "你就是那时候的学者。\x02\x03",
            "#000F在那之后\x01",
            "你的研究进行得如何了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "我觉得还算是比较顺利吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一些细节部分\x01",
            "看来还需要些时间来完善，\x01",
            "但是不管怎么说大体已经成形了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "照这个势头研发的话，\x01",
            "会比我预计的更早出现在商店货架上哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且发售的时候\x01",
            "商品也会包装得更可爱一点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1796")

    Jump("loc_188A")

    label("loc_1799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_17FA")

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "现在可不是发呆的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要赶快把改良方案\x01",
            "确定下来才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188A")

    label("loc_17FA")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "呼～……\x01",
            "露依赛重新把试制品做了出来，\x01",
            "真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没有样品的话，\x01",
            "研究就没办法进行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_188A")

    TalkEnd(0xFE)
    Return()

    # Function_6_633 end

    def Function_7_188E(): pass

    label("Function_7_188E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1970")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1902")

    ChrTalk(
        0xA,
        (
            "#800F提妲就拜托你们照顾了。\x01",
            "　\x02\x03",
            "提妲，\x01",
            "去的时候要当心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1970")

    label("loc_1902")


    ChrTalk(
        0xA,
        (
            "#800F咦，怎么了？\x02\x03",
            "去亚尔摩村的话，\x01",
            "要从西南方的门口出城啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1970")

    TalkEnd(0xFE)
    Return()

    # Function_7_188E end

    def Function_8_1974(): pass

    label("Function_8_1974")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_19E3")

    ChrTalk(
        0x8,
        (
            "#100F抱歉，亚尔摩村水泵修理的工作\x01",
            "就麻烦你们了。\x02\x03",
            "只要把提妲送到那里，\x01",
            "后面的工作交给她就行了。\x02\x03",
            "那么，就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A43")

    label("loc_19E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A43")

    ChrTalk(
        0x8,
        (
            "#100F嗯？在干什么呢？\x02\x03",
            "还不快点去把\x01",
            "内燃引擎设备和汽油拿到这里来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A43")

    TalkEnd(0xFE)
    Return()

    # Function_8_1974 end

    def Function_9_1A47(): pass

    label("Function_9_1A47")

    TalkBegin(0xFE)

    ChrTalk(
        0x9,
        (
            "#060F内燃引擎设备和汽油的保管地方，\x01",
            "去五楼的演算室问问就知道了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_END)), "loc_1ACA")

    ChrTalk(
        0x101,
        (
            "#000F嗯，保管地点已经知道了，\x01",
            "我们马上去拿过来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B0C")

    label("loc_1ACA")


    ChrTalk(
        0x101,
        (
            "#505F五楼的演算室吗。\x02\x03",
            "#000F那我们先去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B0C")

    TalkEnd(0xFE)
    Return()

    # Function_9_1A47 end

    def Function_10_1B10(): pass

    label("Function_10_1B10")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-770, 0, 1240, 0)
    RemoveParty(0x6, 0xFF)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_4A(0x9, 255)
    OP_4A(0x8, 255)
    SetChrPos(0x8, -100, 0, 12700, 180)
    SetChrPos(0x9, -1030, 0, 1690, 0)
    SetChrPos(0x101, -600, 0, 510, 0)
    SetChrPos(0x102, -1950, 0, 750, 0)
    SetChrPos(0xE, 40, 800, 11550, 0)
    ClearChrFlags(0xE, 0x80)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "唉！又失败了吗！\x02",
    )

    CloseMessageWindow()

    def lambda_1BC5():
        OP_6D(1050, 0, 11840, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BC5)

    def lambda_1BDD():
        OP_8E(0xFE, 0x55A, 0x0, 0x26D4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1BDD)
    Sleep(300)

    def lambda_1BFD():
        OP_8E(0xFE, 0xFFFFFCE0, 0x0, 0x2710, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1BFD)
    Sleep(200)

    def lambda_1C1D():
        OP_8E(0xFE, 0x82, 0x0, 0x263E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C1D)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0x8, 0)

    ChrTalk(
        0x9,
        (
            "#560F爷爷。\x01",
            "我们来帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#103F哦哦，提妲。\x02\x03",
            "哦……\x01",
            "你们也都来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嘿嘿～\x01",
            "我们也很在意嘛。\x02\x03",
            "#006F对了，现在到底在干什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#104F如你们所见，\x01",
            "我正在尝试用工作机器把\x01",
            "『黑色导力器』的外壳切开……\x02\x03",
            "看来也并不顺利啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#102F百闻不如一见，你们亲眼看看吧。\x02\x03",
            "……按下按钮。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x9C, 0x0, 0x64)
    Sleep(400)
    OP_22(0xE0, 0x0, 0x64)
    OP_71(0x1, 0x20)
    OP_71(0x2, 0x20)
    OP_70(0x1, 0x3)
    OP_70(0x2, 0x3)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x101,
        "#004F哇……这是什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#062F工作用的圆盘锯。\x02\x03",
            "由特殊合金制成的，\x01",
            "能切断绝大多数种类的材料……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F哦，用这个的话……\x02",
    )

    CloseMessageWindow()
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_6F(0x1, 3)
    OP_6F(0x2, 3)
    OP_70(0x1, 0x25)
    OP_70(0x2, 0x25)
    OP_73(0x1)
    OP_71(0x1, 0x20)
    OP_71(0x2, 0x20)
    OP_6F(0x1, 34)
    OP_6F(0x2, 34)
    OP_70(0x1, 0x25)
    OP_70(0x2, 0x25)
    OP_22(0xC7, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\mp007_00.eff")
    PlayEffect(0x0, 0x0, 0xE, 0, 300, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_23(0xE0)
    OP_23(0xC7)
    OP_22(0x9A, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_73(0x1)
    Sleep(500)
    OP_82(0x0, 0x2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#004F停、停下来了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#561F果然……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F虽然规模较小，不过是和昨天一样的现象。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#102F看来，这个黑色的东西能让\x01",
            "打算对其进行干涉的导力器的机能\x01",
            "完全停止下来。\x02\x03",
            "不仅仅是熄灭照明设备，\x01",
            "其他的导力器也会被停止下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F是、是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#064F但是，爷爷。\x02\x03",
            "为什么没有像昨天那样\x01",
            "影响到其他的范围呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#101F嗯，你发现得好。\x02\x03",
            "这个停止现象\x01",
            "似乎会在周围运作的导力器中\x01",
            "产生连锁反应而扩大。\x02\x03",
            "#100F有效范围大概为５亚矩。\x02\x03",
            "反过来说，\x01",
            "如果范围内没有运作中的导力器，\x01",
            "此现象就不能再继续扩大了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F原来如此……\x01",
            "还有这样的定律啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#104F但是，就算知道了这一点，\x01",
            "关键的机器不能运转，\x01",
            "还是无法调查导力器的内部呀……\x02\x03",
            "这才是真正的麻烦所在呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F不能想办法\x01",
            "用人力切开这个东西吗？\x02\x03",
            "比如说靠气势或毅力之类的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F你还真敢说啊，艾丝蒂尔。\x02\x03",
            "用特殊合金制的小刀划过\x01",
            "不是也没有伤痕吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F啊，也是……\x02\x03",
            "#006F嗯～那么用火呢？\x02\x03",
            "放进熔铁炉里熔掉怎么样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#065F那、那种做法，\x01",
            "内部的零件也会坏掉的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F果然不行吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#103F…………………………\x02\x03",
            "不，也许行得通。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F用高温熔化的方法吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#102F不，不是的。\x02\x03",
            "问题在于导力——\x01",
            "我们太依赖靠导力来运作的机器了。\x02\x03",
            "用导力以外的能量\x01",
            "来运作工作机器就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F用导力以外的能量\x01",
            "来运作……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F有这样的方法吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#104F所谓的『内燃引擎』……\x02\x03",
            "是利用火燃烧\x01",
            "所产生的能量来运作的装置。\x02\x03",
            "这项发明的历史比导力器更为悠久，\x01",
            "但效率也比导力引擎要低。\x02\x03",
            "#100F不过，简单地使工作机器运作，\x01",
            "这种程度还是可以做得到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F还有那样的东西啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F原来如此，\x01",
            "这就是用『火』吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#064F但是，爷爷。\x02\x03",
            "内燃引擎这个设备，\x01",
            "我看都没看过呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#100F记得在中央工房某个地方\x01",
            "保存有研究用的设备。\x02\x03",
            "#103F对了，\x01",
            "还必须找到燃料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F燃料……是油吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#100F那还远远不够，\x01",
            "必须要用『汽油』那样燃烧力更强的东西。\x02\x03",
            "以前这东西曾经作为溶剂使用过，\x01",
            "说不定还有剩余下来的。\x02\x03",
            "唔……\x01",
            "好像行得通。\x02\x03",
            "#101F就这样定了！\x01",
            "赶快开始改造工作机器吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#560F啊，我也来帮忙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F那个那个，\x01",
            "有我们能帮上忙的地方吗？\x02\x03",
            "虽然做不到\x01",
            "像提妲那样专业的工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#100F这样的话，\x01",
            "你们就去把那个内燃引擎和汽油取来吧。\x02\x03",
            "可能有点重，但以游击士的能力，\x01",
            "我想你们应该能找到办法运过来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FＯＫ，交给我们吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F内燃引擎和汽油对吧。\x02\x03",
            "是放在哪里的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#103F嗯？\x02\x03",
            "…………………………\x02\x03",
            "…………哎呀…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F博士您该不会是\x01",
            "忘了放在哪里了吧……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#104F嗯，忘了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F还回答得这么轻描淡写～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        (
            "#560F#2P那、那个，艾丝蒂尔姐姐。\x02\x03",
            "去演算室的话，\x01",
            "我想应该能查到放在哪儿。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x101,
        "#505F演算室？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#060F#2P五楼有个房间里\x01",
            "放着一台导力演算器。\x02\x03",
            "有关中央工房的资料\x01",
            "全部都记录在那机器里面，\x01",
            "我想应该也有各种设备的保管场所吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F好厉害。\x01",
            "竟然有这样的东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#101F就是这样，拜托你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F真是的……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F算了，\x01",
            "总之先到五楼的演算室去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    OP_28(0x3F, 0x1, 0x80)
    OP_28(0x3F, 0x1, 0x100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, -410, 0, 8910, 180)
    SetChrPos(0x102, -410, 0, 8910, 180)
    SetChrPos(0x9, -100, 0, 12700, 180)
    SetChrPos(0x8, -2310, 0, 14200, 0)
    OP_4B(0x8, 255)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_69(0x101, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_10_1B10 end

    def Function_11_2E1E(): pass

    label("Function_11_2E1E")

    AddParty(0x6, 0xFF)
    EventBegin(0x0)
    OP_6D(600, 0, 11100, 0)
    ClearChrFlags(0x8, 0x80)
    OP_4A(0x8, 255)
    OP_4A(0xA, 255)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, 400, 0, 10200, 270)
    SetChrPos(0x107, -630, 0, 10390, 90)
    SetChrPos(0x101, 640, 0, 800, 0)
    SetChrPos(0x102, -430, 0, 800, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#1P呼，我们回来了～\x02",
    )

    CloseMessageWindow()

    def lambda_2EAD():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2EAD)

    def lambda_2EBB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2EBB)

    def lambda_2EC9():
        OP_8E(0xFE, 0x280, 0x0, 0x230A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2EC9)
    Sleep(500)
    OP_8E(0x102, 0xFFFFFE52, 0x0, 0x2224, 0xBB8, 0x0)

    ChrTalk(
        0x102,
        (
            "#010F博士，\x01",
            "需要的东西都带来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#103F#5P哦哦，回来啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#560F#1P辛苦你们了～\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "内燃引擎设备\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "汽油罐\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x367, 1)
    OP_3F(0x368, 1)

    ChrTalk(
        0x101,
        (
            "#007F呼～\x01",
            "的确是有点重啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#101F#5P哦哦，真是辛苦啦。\x02\x03",
            "#100F哈哈，告诉你们，\x01",
            "工作机器也刚好改造完毕了。\x02\x03",
            "之后只要装上内燃引擎，\x01",
            "再灌入汽油就好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(
        0x8,
        (
            "#100F#5P提妲，\x01",
            "我们快点完成它吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(
        0x107,
        "#061F#1P好～\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_6D(-1390, 0, 11640, 0)
    SetChrPos(0x101, -2690, 0, 9810, 0)
    SetChrPos(0x102, -1580, 0, 9760, 0)
    SetChrPos(0x107, -3220, 0, 11360, 90)
    SetChrPos(0x8, -2350, 0, 13080, 180)
    OP_72(0x0, 0x4)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#101F好了，完成啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F呜哇～\x01",
            "这东西真特别啊。\x02\x03",
            "这就是利用内燃引擎的引擎吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F嗯，是的。\x02\x03",
            "引擎里面燃烧着汽油，\x01",
            "所释放的能量就能使工作机器运作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这样一来，即使不依靠导力，\x01",
            "也能运行工作机器了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#104F没错。\x01",
            "那么赶快打开开关吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x8, 0x1, 0x0, 0xC)
    OP_43(0x102, 0x1, 0x0, 0xD)
    OP_43(0x101, 0x1, 0x0, 0xE)
    OP_43(0x107, 0x1, 0x0, 0xF)
    OP_6D(1050, 0, 11840, 2000)
    WaitChrThread(0x107, 0x1)

    ChrTalk(
        0x8,
        "#102F……按下按钮。\x02",
    )

    CloseMessageWindow()
    OP_22(0x9C, 0x0, 0x64)
    Sleep(400)
    OP_22(0x9F, 0x1, 0x64)

    def lambda_3374():

        label("loc_3374")

        OP_7C(0x0, 0xA, 0xBB8, 0x64)
        OP_48()
        Jump("loc_3374")

    QueueWorkItem2(0x101, 3, lambda_3374)
    OP_71(0x1, 0x20)
    OP_71(0x2, 0x20)
    OP_70(0x1, 0x3)
    OP_70(0x2, 0x3)
    Sleep(500)
    OP_8C(0x8, 180, 400)
    Sleep(500)

    ChrTalk(
        0x101,
        "#004F哇，动了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F和导力引擎相比，\x01",
            "噪音和振动都要大很多啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#102F嗯，这是它的缺点之一。\x02\x03",
            "但和预想的一样，\x01",
            "应该不用担心会发生昨天的事情。\x02\x03",
            "那么，就这样开始解体吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F……（吞口水）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#560F……（紧张紧张）\x02",
    )

    CloseMessageWindow()
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_6F(0x1, 3)
    OP_6F(0x2, 3)
    OP_70(0x1, 0x2D)
    OP_70(0x2, 0x2D)
    OP_73(0x1)
    OP_71(0x1, 0x20)
    OP_71(0x2, 0x20)
    OP_6F(0x1, 42)
    OP_6F(0x2, 42)
    OP_70(0x1, 0x2D)
    OP_70(0x2, 0x2D)
    OP_22(0xC7, 0x1, 0x64)
    LoadEffect(0x0, "map\\\\mp010_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -100, 1200, 11450, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x101,
        "#004F哇哇……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F好厉害的火花……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#102F好，先停一下。\x02\x03",
            "首先要确认一下\x01",
            "这东西外壳的削损程度。\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_82(0x0, 0x2)
    OP_23(0xC7)
    OP_44(0x101, 0x3)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x9F)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_6F(0x1, 362)
    OP_6F(0x2, 362)
    OP_70(0x1, 0x16D)
    OP_70(0x2, 0x16D)
    OP_73(0x1)
    Sleep(1000)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们往黑色导力器外壳的表面上看去。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "外壳上只是留下了小小的伤口。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#505F只、只削了这么一点？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F真不敢相信……\x01",
            "这可是特殊合金制的圆盘锯呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F真是极为坚硬的材质啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#101F其实只要保持耐心继续下去，\x01",
            "应该能完全切开的。\x02\x03",
            "哈哈……\x01",
            "只可惜圆盘锯有必要多换几个了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F这么说……\x01",
            "从现在开始就是耐力的考验了吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -800, 0, 800, 0)

    ChrTalk(
        0xA,
        "#1P博士，你有空吗？\x02",
    )

    CloseMessageWindow()

    def lambda_38B6():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_38B6)

    def lambda_38C4():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_38C4)

    def lambda_38D2():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38D2)

    def lambda_38E0():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_38E0)
    OP_8E(0xA, 0xFFFFFF6A, 0x0, 0x1F40, 0xBB8, 0x0)

    ChrTalk(
        0xA,
        (
            "#801F哦哦……\x01",
            "已经顺利改造完毕了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#104F当然了，\x01",
            "你以为我是谁呀。\x02\x03",
            "#100F怎么了，\x01",
            "又有什么麻烦吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#800F刚才亚尔摩旅馆\x01",
            "给博士发了一条的联络过来。\x02\x03",
            "他们说旅馆那个抽取温泉的导力泵\x01",
            "好像出了故障。\x02\x03",
            "这样下去的话就不能营业了，\x01",
            "所以想请博士马上过去修理一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#102F啊～怎么搞的！？\x02\x03",
            "哎呀呀！\x01",
            "如此忙的时候还来麻烦的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#805F这样的话……\x01",
            "要不要我派其他技师代替你去呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#100F不……\x01",
            "那是４０多年前的破铜烂铁了。\x02\x03",
            "只熟悉最新型机械的年轻人\x01",
            "是没办法应付那东西的。\x02\x03",
            "#104F唔，真是伤脑筋。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x107)
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(
        0x107,
        (
            "#560F那个，爷爷……\x02\x03",
            "我有个建议……\x01",
            "这次让我替您去修理好吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C63():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C63)

    def lambda_3C71():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C71)
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(
        0x8,
        "#103F什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#802F提妲？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F以前您带我去的时候，\x01",
            "我也帮忙维修过那东西哦。\x02\x03",
            "所以我想没问题的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#100F唔……的确。\x01",
            "技术方面交给你应该没问题……\x02\x03",
            "不过我担心别的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#803F是啊，\x01",
            "街道上有那么多魔兽出没……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#063F可是可是……\x01",
            "麻绪婆婆有麻烦，我不能置之不理啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3DD8():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3DD8)
    TurnDirection(0x101, 0x102, 400)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    OP_63(0x102)

    def lambda_3E1C():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E1C)
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(
        0x101,
        (
            "#006F#2P……那样的话，\x01",
            "交给我们两个不就行了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x107,
        "#064F咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P艾丝蒂尔说的没错。\x01",
            "确保道路安全也是游击士的义务。\x02\x03",
            "这次就让我们两个做护卫吧。\x01",
            "我们一定会将提妲安全护送到那里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#801F哦哦，你们一起去的话，\x01",
            "那就没什么好担心的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#100F唔……\x01",
            "难得你们费心，那就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F那个那个……\x01",
            "这样麻烦你们可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#2P哎呀～小孩子就不要担心太多啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F#2P一起去的话起码多个照应。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F谢、谢谢你们。\x01",
            "艾丝蒂尔姐姐、约修亚哥哥。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x8, 400)
    Sleep(200)
    TurnDirection(0x107, 0xA, 400)
    Sleep(500)

    ChrTalk(
        0x107,
        (
            "#560F爷爷、工房长叔叔。\x02\x03",
            "那我们走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#101F哦哦，拜托你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#801F路上要小心点哦。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-100, 0, 6770, 0)
    SetChrPos(0x101, -100, 0, 6770, 180)
    SetChrPos(0x102, -100, 0, 6770, 180)
    SetChrPos(0x107, -100, 0, 6770, 180)
    SetChrPos(0x8, 0, 0, 12740, 180)
    SetChrPos(0xA, -130, 0, 10450, 0)
    OP_4B(0x8, 255)
    OP_4B(0xA, 255)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    ClearMapFlags(0x10000000)
    OP_A2(0x51A)
    OP_28(0x3F, 0x4, 0x10)
    OP_28(0x3F, 0x4, 0x20)
    OP_28(0x40, 0x4, 0x2)
    OP_28(0x40, 0x4, 0x4)
    EventEnd(0x0)
    Return()

    # Function_11_2E1E end

    def Function_12_41CA(): pass

    label("Function_12_41CA")

    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFF876, 0x0, 0x348A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFEF2, 0x0, 0x3674, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF9C, 0x0, 0x319C, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_12_41CA end

    def Function_13_4218(): pass

    label("Function_13_4218")

    Sleep(400)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x474, 0x0, 0x2774, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_13_4218 end

    def Function_14_4243(): pass

    label("Function_14_4243")

    Sleep(800)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x78, 0x0, 0x26DE, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_14_4243 end

    def Function_15_426E(): pass

    label("Function_15_426E")

    Sleep(1200)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFF448, 0x0, 0x268E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFD1C, 0x0, 0x27E2, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_15_426E end

    def Function_16_42AD(): pass

    label("Function_16_42AD")

    EventBegin(0x0)
    OP_6D(-180, 0, 2620, 0)
    SetMapFlags(0x40000000)
    AddParty(0x5, 0xFF)
    OP_31(0x5, 0x0, 0x1A)
    OP_B5(0x5, 0x0)
    OP_B5(0x5, 0x1)
    OP_B5(0x5, 0x2)
    OP_B5(0x5, 0x3)
    OP_41(0x5, 0x9B)
    OP_41(0x5, 0xF5)
    OP_41(0x5, 0x113)
    OP_41(0x5, 0x25F, 0x0)
    OP_41(0x5, 0x259, 0x1)
    OP_41(0x5, 0x262, 0x2)
    OP_35(0x5, 0xC8)
    OP_35(0x5, 0xC9)
    OP_35(0x5, 0xCA)
    OP_36(0x5, 0xFF)
    OP_36(0x5, 0x100)
    SetChrFlags(0x106, 0x80)
    SetChrPos(0x107, -850, 0, 2040, 0)
    SetChrPos(0x101, -1590, 0, 900, 0)
    SetChrPos(0x102, -260, 0, 1060, 0)
    OP_22(0x9F, 0x1, 0x64)

    def lambda_434F():

        label("loc_434F")

        OP_7C(0x0, 0xA, 0xBB8, 0x64)
        OP_48()
        Jump("loc_434F")

    QueueWorkItem2(0x101, 3, lambda_434F)
    OP_71(0x1, 0x20)
    OP_71(0x2, 0x20)
    OP_6F(0x1, 42)
    OP_6F(0x2, 42)
    OP_70(0x1, 0x2D)
    OP_70(0x2, 0x2D)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x107,
        (
            "#062F爷爷，不好了啦！\x02\x03",
            "#064F……啊……………\x02",
        )
    )

    CloseMessageWindow()
    OP_6D(1770, 0, 12830, 2000)

    def lambda_43DC():
        OP_8E(0xFE, 0x140, 0x0, 0x259E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_43DC)

    def lambda_43F7():
        OP_8E(0xFE, 0xFFFFFCAE, 0x0, 0x21F2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43F7)

    def lambda_4412():
        OP_8E(0xFE, 0x3B6, 0x0, 0x2170, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4412)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#004F奇怪了……\x02\x03",
            "既然博士不在的话，\x01",
            "为什么工作机器自己会在动？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F是、是啊……\x01",
            "总之先把工作机器停下来……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4499():

        label("loc_4499")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_4499")

    QueueWorkItem2(0x101, 1, lambda_4499)

    def lambda_44AA():

        label("loc_44AA")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_44AA")

    QueueWorkItem2(0x102, 1, lambda_44AA)
    SetChrFlags(0x107, 0x4)
    OP_8E(0x107, 0x97E, 0x0, 0x271A, 0xFA0, 0x0)
    OP_8E(0x107, 0xA3C, 0x0, 0x326E, 0xFA0, 0x0)
    OP_8E(0x107, 0x50, 0x0, 0x350C, 0xFA0, 0x0)
    OP_8E(0x107, 0x8C, 0x0, 0x3200, 0xFA0, 0x0)
    OP_8C(0x107, 90, 400)
    Sleep(500)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_23(0x9F)
    OP_44(0x101, 0x3)
    OP_22(0x9A, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_6F(0x1, 362)
    OP_6F(0x2, 362)
    OP_70(0x1, 0x16D)
    OP_70(0x2, 0x16D)
    OP_73(0x1)
    Sleep(1500)

    ChrTalk(
        0x107,
        (
            "#561F呼……\x02\x03",
            "#063F爷爷他……\x01",
            "现在到底在哪儿呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F不止是博士……\x01",
            "『黑色导力器』也不见了。\x02\x03",
            "难道说这是……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x106, -790, 0, 2500, 0)
    ClearChrFlags(0x106, 0x80)

    ChrTalk(
        0x106,
        "#1P哼，你们在这里啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_465D():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_465D)

    def lambda_466B():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_466B)

    def lambda_4679():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4679)
    OP_6D(990, 0, 7840, 1000)

    ChrTalk(
        0x101,
        "#004F阿、阿加特！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F您怎么会在这里……\x02",
    )

    CloseMessageWindow()

    def lambda_46CD():

        label("loc_46CD")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_46CD")

    QueueWorkItem2(0x101, 1, lambda_46CD)

    def lambda_46DE():

        label("loc_46DE")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_46DE")

    QueueWorkItem2(0x102, 1, lambda_46DE)
    OP_8E(0x106, 0xFFFFFF2E, 0x0, 0x1B1C, 0xBB8, 0x0)
    OP_43(0x107, 0x2, 0x0, 0x11)

    ChrTalk(
        0x106,
        (
            "#552F哼，这句话是我问你们才对。\x02\x03",
            "我听到这里发生骚乱就赶了过来，\x01",
            "不过没想到又被你们两个抢先一步。\x02\x03",
            "真是不知天高地厚的小鬼，\x01",
            "明明本事就不多，还到处乱出风头。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F你、你这个刀子嘴～……\x01",
            "没见一段时间还是那么惹人厌啊。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x2)
    TurnDirection(0x107, 0x106, 400)

    ChrTalk(
        0x107,
        (
            "#064F那个……\x01",
            "艾丝蒂尔姐姐你们认识他吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F他叫阿加特。\x01",
            "是我们在游击士协会的前辈。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x106, 0x107, 400)

    ChrTalk(
        0x106,
        (
            "#052F喂，我问你们两个……\x02\x03",
            "#057F既然全体人员已经疏散了，\x01",
            "为什么还会有小鬼在这种地方？\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x106, 0x55A, 0x0, 0x1D38, 0xBB8, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "阿加特紧紧盯着提妲。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x107,
        "#065F……呜……\x02",
    )

    OP_9E(0x107, 0xF, 0x0, 0x3E8, 0xBB8)
    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_8E(0x101, 0x186, 0x0, 0x1DF6, 0xBB8, 0x0)
    TurnDirection(0x101, 0x106, 0)

    ChrTalk(
        0x101,
        (
            "#009F等、等一下，\x01",
            "你怎么吓唬人家女孩子啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F…………………………\x02\x03",
            "#552F嘁……\x02\x03",
            "虽然想说的话堆积如山，\x01",
            "但还是以后再说吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(
        0x106,
        "#050F话说回来，这到底是怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F嗯，其实……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们向阿加特说明了拉赛尔博士不见的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x106,
        (
            "#053F唔，发烟筒吗……\x01",
            "我有很不好的预感。\x02\x03",
            "#054F时间紧迫……\x01",
            "赶快把博士找出来吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F知道了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F明白。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#063F……爷爷……\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_28(0x41, 0x1, 0x4)
    EventEnd(0x0)
    Return()

    # Function_16_42AD end

    def Function_17_4BD0(): pass

    label("Function_17_4BD0")

    OP_8E(0x107, 0x50, 0x0, 0x350C, 0xBB8, 0x0)
    OP_8E(0x107, 0x33E, 0x0, 0x3692, 0xBB8, 0x0)
    OP_8E(0x107, 0xA3C, 0x0, 0x326E, 0xBB8, 0x0)
    OP_8E(0x107, 0x8D4, 0x0, 0x1E14, 0xBB8, 0x0)
    TurnDirection(0x107, 0x101, 400)
    Return()

    # Function_17_4BD0 end

    SaveToFile()

Try(main)
