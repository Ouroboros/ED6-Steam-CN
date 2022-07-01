from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3210   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        'ED6_DT07/CH01273 ._CH',             # 09
        'ED6_DT07/CH01153 ._CH',             # 0A
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
        'ED6_DT07/CH01273P._CP',             # 09
        'ED6_DT07/CH01153P._CP',             # 0A
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
        "Function_0_222",          # 00, 0
        "Function_1_4C1",          # 01, 1
        "Function_2_4E3",          # 02, 2
        "Function_3_4F9",          # 03, 3
        "Function_4_500",          # 04, 4
        "Function_5_58B",          # 05, 5
        "Function_6_D6F",          # 06, 6
        "Function_7_FE7",          # 07, 7
        "Function_8_157E",         # 08, 8
        "Function_9_17AD",         # 09, 9
        "Function_10_1939",        # 0A, 10
        "Function_11_1940",        # 0B, 11
    )


    def Function_0_222(): pass

    label("Function_0_222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_258")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 1750, 250, 8900, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    Jump("loc_4C0")

    label("loc_258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_28E")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3430, 0, 4050, 11)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    Jump("loc_4C0")

    label("loc_28E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2C4")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -3460, 250, 8840, 350)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    Jump("loc_4C0")

    label("loc_2C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_32D")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -1330, 250, 8540, 104)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 33700, 250, 7700, 171)
    TurnDirection(0xA, 0xB, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 1880, 250, 8350, 276)
    Jump("loc_4C0")

    label("loc_32D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_394")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3820, 0, 2790, 100)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 29020, 250, 7010, 255)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 2530, 0, 4070, 6)
    Jump("loc_4C0")

    label("loc_394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_3B4")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 28000, 250, 5350, 0)
    Jump("loc_4C0")

    label("loc_3B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_413")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3430, 0, 4050, 11)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 10)
    OP_44(0xB, 0x0)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, 29020, 250, 7120, 270)
    Jump("loc_4C0")

    label("loc_413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_48D")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0x9, 28090, 0, 8600, 180)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 10)
    OP_44(0xB, 0x0)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, 29020, 250, 7120, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3430, 0, 4050, 11)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    Jump("loc_4C0")

    label("loc_48D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4C0")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -3600, 250, 8850, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)

    label("loc_4C0")

    Return()

    # Function_0_222 end

    def Function_1_4C1(): pass

    label("Function_1_4C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D9")
    OP_B1("t3210_y")
    Jump("loc_4E2")

    label("loc_4D9")

    OP_B1("t3210_n")

    label("loc_4E2")

    Return()

    # Function_1_4C1 end

    def Function_2_4E3(): pass

    label("Function_2_4E3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F8")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_4E3")

    label("loc_4F8")

    Return()

    # Function_2_4E3 end

    def Function_3_4F9(): pass

    label("Function_3_4F9")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_3_4F9 end

    def Function_4_500(): pass

    label("Function_4_500")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_50D")
    Jump("loc_587")

    label("loc_50D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_517")
    Jump("loc_587")

    label("loc_517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_521")
    Jump("loc_587")

    label("loc_521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_52B")
    Jump("loc_587")

    label("loc_52B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_535")
    Jump("loc_587")

    label("loc_535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_53F")
    Jump("loc_587")

    label("loc_53F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_549")
    Jump("loc_587")

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_580")

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
    Jump("loc_587")

    label("loc_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_587")

    label("loc_587")

    TalkEnd(0xFE)
    Return()

    # Function_4_500 end

    def Function_5_58B(): pass

    label("Function_5_58B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_6EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_64E")

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
    Jump("loc_6E8")

    label("loc_64E")

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

    label("loc_6E8")

    Jump("loc_D6B")

    label("loc_6EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_887")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7AE")

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
    Jump("loc_884")

    label("loc_7AE")

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

    label("loc_884")

    Jump("loc_D6B")

    label("loc_887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_943")

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
    Jump("loc_D6B")

    label("loc_943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_9B0")
    TurnDirection(0xFE, 0xB, 0)

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
    Jump("loc_D6B")

    label("loc_9B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_A79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_A12")

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
    Jump("loc_A76")

    label("loc_A12")

    OP_A2(0x2)

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

    label("loc_A76")

    Jump("loc_D6B")

    label("loc_A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_A83")
    Jump("loc_D6B")

    label("loc_A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_ADF")

    ChrTalk(
        0xFE,
        (
            "真希望丈夫\x01",
            "吃完饭能把盘子收拾一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D6B")

    label("loc_ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_B69")

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
    Jump("loc_C50")

    label("loc_B69")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
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
    OP_62(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "……干脆我就放着不收拾算了，\x01",
            "看他们父女俩怎么办。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C50")

    Jump("loc_D6B")

    label("loc_C53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_D6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_CCF")

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
    Jump("loc_D6B")

    label("loc_CCF")

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

    label("loc_D6B")

    TalkEnd(0xFE)
    Return()

    # Function_5_58B end

    def Function_6_D6F(): pass

    label("Function_6_D6F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_D7C")
    Jump("loc_FE3")

    label("loc_D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_D86")
    Jump("loc_FE3")

    label("loc_D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_D90")
    Jump("loc_FE3")

    label("loc_D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_E42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_DCD")

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
    Jump("loc_E3F")

    label("loc_DCD")

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

    label("loc_E3F")

    Jump("loc_FE3")

    label("loc_E42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_EAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E8A")

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
    Jump("loc_EA9")

    label("loc_E8A")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "妈妈～～\x01",
            "饭还没做好吗～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA9")

    Jump("loc_FE3")

    label("loc_EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_F5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_EF4")

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
    Jump("loc_F59")

    label("loc_EF4")

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

    label("loc_F59")

    Jump("loc_FE3")

    label("loc_F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_F92")

    ChrTalk(
        0xFE,
        "那～么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "现在要玩点什么呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_FE3")

    label("loc_F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_FDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_FB6")

    ChrTalk(
        0xFE,
        "啊，还有饭后点心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_FD9")

    label("loc_FB6")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "妈妈～\x01",
            "我也要喝茶。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD9")

    Jump("loc_FE3")

    label("loc_FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_FE3")

    label("loc_FE3")

    TalkEnd(0xFE)
    Return()

    # Function_6_D6F end

    def Function_7_FE7(): pass

    label("Function_7_FE7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_10C5")

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
    Jump("loc_157A")

    label("loc_10C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_10CF")
    Jump("loc_157A")

    label("loc_10CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_11BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1122")

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
    Jump("loc_11B9")

    label("loc_1122")

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

    label("loc_11B9")

    Jump("loc_157A")

    label("loc_11BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1247")
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
    Jump("loc_157A")

    label("loc_1247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_13C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_129D")
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
    Jump("loc_13BE")

    label("loc_129D")

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

    label("loc_13BE")

    Jump("loc_157A")

    label("loc_13C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_13CB")
    Jump("loc_157A")

    label("loc_13CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_13D5")
    Jump("loc_157A")

    label("loc_13D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_13DF")
    Jump("loc_157A")

    label("loc_13DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_157A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_14AE")

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
            "哈哈，这种话由我这个工作人员说出来，\x01",
            "听起来就像在打广告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_157A")

    label("loc_14AE")

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

    label("loc_157A")

    TalkEnd(0xFE)
    Return()

    # Function_7_FE7 end

    def Function_8_157E(): pass

    label("Function_8_157E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_158B")
    Jump("loc_17A9")

    label("loc_158B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1692")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_15DE")

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
    Jump("loc_168F")

    label("loc_15DE")

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

    label("loc_168F")

    Jump("loc_17A9")

    label("loc_1692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_169C")
    Jump("loc_17A9")

    label("loc_169C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_16A6")
    Jump("loc_17A9")

    label("loc_16A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_16B0")
    Jump("loc_17A9")

    label("loc_16B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_16BA")
    Jump("loc_17A9")

    label("loc_16BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_171B")

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
    Jump("loc_179F")

    label("loc_171B")

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

    label("loc_179F")

    Jump("loc_17A9")

    label("loc_17A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_17A9")

    label("loc_17A9")

    TalkEnd(0xFE)
    Return()

    # Function_8_157E end

    def Function_9_17AD(): pass

    label("Function_9_17AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_17BA")
    Jump("loc_1935")

    label("loc_17BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_17C4")
    Jump("loc_1935")

    label("loc_17C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_17CE")
    Jump("loc_1935")

    label("loc_17CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1818")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_17F4")

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
    Jump("loc_1815")

    label("loc_17F4")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "呼唔～……\x01",
            "还是很瞌睡啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1815")

    Jump("loc_1935")

    label("loc_1818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1910")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_18A2")

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
    Jump("loc_190D")

    label("loc_18A2")

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

    label("loc_190D")

    Jump("loc_1935")

    label("loc_1910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_191A")
    Jump("loc_1935")

    label("loc_191A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_1924")
    Jump("loc_1935")

    label("loc_1924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_192E")
    Jump("loc_1935")

    label("loc_192E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1935")

    label("loc_1935")

    TalkEnd(0xFE)
    Return()

    # Function_9_17AD end

    def Function_10_1939(): pass

    label("Function_10_1939")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_10_1939 end

    def Function_11_1940(): pass

    label("Function_11_1940")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_11_1940 end

    SaveToFile()

Try(main)
