from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3211   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3211.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        '拜舍尔',                               # 9
        '艾德',                                 # 10
        '林',                                   # 11
        '莉西亚',                               # 12
        '希利尔',                               # 13
        '艾缇',                                 # 14
        '拉克',                                 # 15
        '希玛',                                 # 16
        '库安',                                 # 17
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
        'ED6_DT07/CH01040 ._CH',             # 00
        'ED6_DT07/CH01270 ._CH',             # 01
        'ED6_DT07/CH01030 ._CH',             # 02
        'ED6_DT07/CH01150 ._CH',             # 03
        'ED6_DT07/CH01120 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
        'ED6_DT07/CH01160 ._CH',             # 06
        'ED6_DT07/CH01020 ._CH',             # 07
        'ED6_DT07/CH01060 ._CH',             # 08
        'ED6_DT07/CH01153 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
        'ED6_DT07/CH01270P._CP',             # 01
        'ED6_DT07/CH01030P._CP',             # 02
        'ED6_DT07/CH01150P._CP',             # 03
        'ED6_DT07/CH01120P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
        'ED6_DT07/CH01160P._CP',             # 06
        'ED6_DT07/CH01020P._CP',             # 07
        'ED6_DT07/CH01060P._CP',             # 08
        'ED6_DT07/CH01153P._CP',             # 09
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
        TalkScenaIndex      = 3,
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
        TalkScenaIndex      = 4,
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
        TalkScenaIndex      = 5,
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
        TalkScenaIndex      = 7,
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
        TalkScenaIndex      = 8,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )


    ScpFunction(
        "Function_0_21A",          # 00, 0
        "Function_1_4AB",          # 01, 1
        "Function_2_4AC",          # 02, 2
        "Function_3_4C2",          # 03, 3
        "Function_4_4C9",          # 04, 4
        "Function_5_554",          # 05, 5
        "Function_6_CC7",          # 06, 6
        "Function_7_F13",          # 07, 7
        "Function_8_14AA",         # 08, 8
        "Function_9_16D9",         # 09, 9
        "Function_10_1865",        # 0A, 10
        "Function_11_186C",        # 0B, 11
    )


    def Function_0_21A(): pass

    label("Function_0_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_255")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 1960, 250, 8900, 0)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    Jump("loc_4AA")

    label("loc_255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_28B")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3430, 0, 4050, 11)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    Jump("loc_4AA")

    label("loc_28B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2C1")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -3460, 250, 8840, 350)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    Jump("loc_4AA")

    label("loc_2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_32A")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -1330, 250, 8540, 104)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 33700, 250, 7700, 171)
    TurnDirection(0xA, 0xB, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 1880, 250, 8350, 276)
    Jump("loc_4AA")

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_3A4")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3820, 0, 2790, 100)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 9)
    OP_44(0xB, 0x0)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, 29020, 250, 7120, 270)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 2530, 0, 4070, 6)
    Jump("loc_4AA")

    label("loc_3A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_3C4")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 29020, 250, 7010, 255)
    Jump("loc_4AA")

    label("loc_3C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_410")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3430, 0, 4050, 11)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 29020, 250, 7010, 255)
    Jump("loc_4AA")

    label("loc_410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_472")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 27220, 250, 6680, 96)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 29020, 250, 7010, 255)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3430, 0, 4050, 11)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    Jump("loc_4AA")

    label("loc_472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4AA")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -2080, 250, 6150, 195)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)

    label("loc_4AA")

    Return()

    # Function_0_21A end

    def Function_1_4AB(): pass

    label("Function_1_4AB")

    Return()

    # Function_1_4AB end

    def Function_2_4AC(): pass

    label("Function_2_4AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_4AC")

    label("loc_4C1")

    Return()

    # Function_2_4AC end

    def Function_3_4C2(): pass

    label("Function_3_4C2")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_3_4C2 end

    def Function_4_4C9(): pass

    label("Function_4_4C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_4D6")
    Jump("loc_550")

    label("loc_4D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_4E0")
    Jump("loc_550")

    label("loc_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4EA")
    Jump("loc_550")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4F4")
    Jump("loc_550")

    label("loc_4F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_4FE")
    Jump("loc_550")

    label("loc_4FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_508")
    Jump("loc_550")

    label("loc_508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_512")
    Jump("loc_550")

    label("loc_512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_549")

    ChrTalk(
        0xFE,
        "喂～～林。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "给我杯茶～～\x02",
    )

    CloseMessageWindow()
    Jump("loc_550")

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_550")

    label("loc_550")

    TalkEnd(0xFE)
    Return()

    # Function_4_4C9 end

    def Function_5_554(): pass

    label("Function_5_554")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_6B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_617")

    ChrTalk(
        0xFE,
        (
            "村子里这么安静\x01",
            "是因为今天没有观光的客人吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就是因为这样\x01",
            "我女儿一直睡到现在才起床。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……真是的，\x01",
            "要不要给她找点活干干呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B1")

    label("loc_617")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "是因为今天没有观光的客人吗。\x01",
            "村子里这么安静……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "希望在诞辰庆典之前\x01",
            "不要再发生什么事情就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B1")

    Jump("loc_CC3")

    label("loc_6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_850")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_777")

    ChrTalk(
        0xFE,
        (
            "对家庭主妇来说，\x01",
            "比起关心外面的事，\x01",
            "今晩要做的菜才更重要呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管外面发生什么，\x01",
            "女儿一到晚上\x01",
            "肚子都会饿。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84D")

    label("loc_777")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "马上就是女王的诞辰庆典了。\x01",
            "可是，最近到处都不太平啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……算了， \x01",
            "在意这种事也没用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还是想想\x01",
            "今天晚上做什么饭吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84D")

    Jump("loc_CC3")

    label("loc_850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_90C")

    ChrTalk(
        0xFE,
        (
            "蔡斯那边好像\x01",
            "发生了不得了的大事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近外边那么乱，\x01",
            "真是可怕啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还好这个村子\x01",
            "什么事都没发生……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC3")

    label("loc_90C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_972")

    ChrTalk(
        0xFE,
        (
            "我说，莉西亚。\x01",
            "你也稍微精神点呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我忍着睡意\x01",
            "给你做早饭呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC3")

    label("loc_972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_A49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9D4")

    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "真是散漫的女儿啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "简直和年轻时的丈夫一样，\x01",
            "真让人头疼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A46")

    label("loc_9D4")

    OP_A2(0x2)
    OP_8C(0xA, 0, 400)

    ChrTalk(
        0xFE,
        (
            "莉西亚！\x01",
            "别光喊肚子饿，\x01",
            "你也来帮帮忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要不然还要\x01",
            "等很久才能把饭做完。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 400)

    label("loc_A46")

    Jump("loc_CC3")

    label("loc_A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_A53")
    Jump("loc_CC3")

    label("loc_A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_ADD")

    ChrTalk(
        0xFE,
        (
            "为什么非要让\x01",
            "忙得不可开交的我来倒茶啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想要喝茶，\x01",
            "就不能自己去倒吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA8")

    label("loc_ADD")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "我还以为丈夫和女儿吃完了饭\x01",
            "就会没事了的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们吃完后谁也不收拾，\x01",
            "结果洗盘子的活儿还是由我来做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……总是这样，\x01",
            "就不能放过我一次吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA8")

    Jump("loc_CC3")

    label("loc_BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_CC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_C27")

    ChrTalk(
        0xFE,
        (
            "好了，\x01",
            "该开始准备中午饭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "调味料快要用完了。\x01",
            "一会儿去买点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC3")

    label("loc_C27")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "我的丈夫\x01",
            "是旅馆里的厨师哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他做的东方料理\x01",
            "在旅行者中很受欢迎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "连旅游指南里面\x01",
            "也有这方面的记载。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC3")

    TalkEnd(0xFE)
    Return()

    # Function_5_554 end

    def Function_6_CC7(): pass

    label("Function_6_CC7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_CD4")
    Jump("loc_F0F")

    label("loc_CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_CDE")
    Jump("loc_F0F")

    label("loc_CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_CE8")
    Jump("loc_F0F")

    label("loc_CE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_D9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D25")

    ChrTalk(
        0xFE,
        "呼啊啊啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "还是没有睡够呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D97")

    label("loc_D25")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "呼啊啊啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "爸爸从早上开始什么都不干，\x01",
            "也不起床。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D97")

    Jump("loc_F0F")

    label("loc_D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_E04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_DE2")

    ChrTalk(
        0xFE,
        "妈～妈，我肚子饿了～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我已经\x01",
            "快要饿死了啦～～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E01")

    label("loc_DE2")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "妈妈～～\x01",
            "饭还没做好吗～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E01")

    Jump("loc_F0F")

    label("loc_E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_EB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E4C")

    ChrTalk(
        0xFE,
        "呜，已经晚上啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊～讨厌～\x01",
            "天变黑了。\x01",
            "好可怕啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB1")

    label("loc_E4C")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "呜，好寂寞啊。\x01",
            "可是还要看家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，好饿啊。\x01",
            "妈妈快点回来吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB1")

    Jump("loc_F0F")

    label("loc_EB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_EBE")
    Jump("loc_F0F")

    label("loc_EBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_F08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_EE2")

    ChrTalk(
        0xFE,
        "啊，还有饭后点心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F05")

    label("loc_EE2")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "妈妈～\x01",
            "我也要喝茶。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F05")

    Jump("loc_F0F")

    label("loc_F08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_F0F")

    label("loc_F0F")

    TalkEnd(0xFE)
    Return()

    # Function_6_CC7 end

    def Function_7_F13(): pass

    label("Function_7_F13")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_FF1")

    ChrTalk(
        0xFE,
        (
            "今天真难得，\x01",
            "都没有客人啊。\x01",
            "我也可以休息了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过这样一来\x01",
            "『红叶亭』就更冷清了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "女王陛下的诞辰庆典\x01",
            "真是很吸引游客啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A6")

    label("loc_FF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_FFB")
    Jump("loc_14A6")

    label("loc_FFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_10E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_104E")

    ChrTalk(
        0xFE,
        (
            "好了，\x01",
            "我差不多该去工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，无论如何，\x01",
            "希望早日抓住那些犯人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E5")

    label("loc_104E")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "关于蔡斯的事件，\x01",
            "听说犯人好像还没抓到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "蔡斯市离军队的要塞很近，\x01",
            "本来以为那里会很安全的，可是……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E5")

    Jump("loc_14A6")

    label("loc_10E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1173")
    TurnDirection(0xFE, 0xE, 0)

    ChrTalk(
        0xFE,
        (
            "好了，拉克。\x01",
            "赶快吃早饭吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "再这么磨磨蹭蹭的话，\x01",
            "爸爸连你的那份也要吃了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A6")

    label("loc_1173")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_12ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_11C9")
    TurnDirection(0xFE, 0xE, 0)

    ChrTalk(
        0xFE,
        (
            "好，拉克。\x01",
            "那么面包就交给你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为接下来\x01",
            "爸爸要准备炖菜了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12EA")

    label("loc_11C9")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "我以前也在蔡斯住，\x01",
            "不过我还是\x01",
            "更喜欢这个村子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "生下这个孩子的时候，\x01",
            "我和妻子艾缇搬到这里住了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "蔡斯那边确实便利，\x01",
            "但是我觉得自己\x01",
            "还是适合这边的生活。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "每天能泡温泉\x01",
            "也是这里的一大魅力吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EA")

    Jump("loc_14A6")

    label("loc_12ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_12F7")
    Jump("loc_14A6")

    label("loc_12F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_1301")
    Jump("loc_14A6")

    label("loc_1301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_130B")
    Jump("loc_14A6")

    label("loc_130B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_14A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_13DA")

    ChrTalk(
        0xFE,
        (
            "其实我也是\x01",
            "『红叶亭』的客房工作人员……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那真是个很好的旅馆啊。\x01",
            "希望你们有机会一定来住住看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈，\x01",
            "这种话由我这个工作人员说出来，\x01",
            "听起来就像在打广告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A6")

    label("loc_13DA")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "你们是想找住宿的地方吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "『红叶亭』旅馆就在贮水池那边，\x01",
            "村子的另一头。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那真是个很好的旅馆啊。\x01",
            "希望你们有机会一定来住住看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A6")

    TalkEnd(0xFE)
    Return()

    # Function_7_F13 end

    def Function_8_14AA(): pass

    label("Function_8_14AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_14B7")
    Jump("loc_16D5")

    label("loc_14B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_15BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_150A")

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "要开始准备晚饭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊……这么说来， \x01",
            "今天做什么菜好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15BB")

    label("loc_150A")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "刚才在外边\x01",
            "看见拉克他们了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "小孩子就是有精神啊。\x01",
            "发生了那样的事件，\x01",
            "也还在外边活蹦乱跳的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我觉得\x01",
            "自己也被他们感染了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15BB")

    Jump("loc_16D5")

    label("loc_15BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_15C8")
    Jump("loc_16D5")

    label("loc_15C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_15D2")
    Jump("loc_16D5")

    label("loc_15D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_15DC")
    Jump("loc_16D5")

    label("loc_15DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_15E6")
    Jump("loc_16D5")

    label("loc_15E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1647")

    ChrTalk(
        0xFE,
        (
            "嗯嗯，\x01",
            "炖菜需要重新热一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "再多加一种蔬菜进去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16CB")

    label("loc_1647")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "午休的时候必须要预先准备晚饭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "因为我们家两个大人平时都要外出工作。\x02",
    )

    CloseMessageWindow()

    label("loc_16CB")

    Jump("loc_16D5")

    label("loc_16CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_16D5")

    label("loc_16D5")

    TalkEnd(0xFE)
    Return()

    # Function_8_14AA end

    def Function_9_16D9(): pass

    label("Function_9_16D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_16E6")
    Jump("loc_1861")

    label("loc_16E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_16F0")
    Jump("loc_1861")

    label("loc_16F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_16FA")
    Jump("loc_1861")

    label("loc_16FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1744")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1720")

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……呼唔唔。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1741")

    label("loc_1720")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "呼唔～……\x01",
            "还是很瞌睡啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1741")

    Jump("loc_1861")

    label("loc_1744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_183C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_17CE")

    ChrTalk(
        0xFE,
        (
            "爸爸很不擅长家务活。\x01",
            "做起来毛手毛脚的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样也能\x01",
            "在旅馆里工作吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1839")

    label("loc_17CE")

    OP_A2(0x6)
    TurnDirection(0xFE, 0xC, 0)

    ChrTalk(
        0xFE,
        (
            "喂，爸爸。\x01",
            "先把炖菜热一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "然后趁那段时间\x01",
            "做面包不就好了吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1839")

    Jump("loc_1861")

    label("loc_183C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_1846")
    Jump("loc_1861")

    label("loc_1846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_1850")
    Jump("loc_1861")

    label("loc_1850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_185A")
    Jump("loc_1861")

    label("loc_185A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1861")

    label("loc_1861")

    TalkEnd(0xFE)
    Return()

    # Function_9_16D9 end

    def Function_10_1865(): pass

    label("Function_10_1865")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_10_1865 end

    def Function_11_186C(): pass

    label("Function_11_186C")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_11_186C end

    SaveToFile()

Try(main)
