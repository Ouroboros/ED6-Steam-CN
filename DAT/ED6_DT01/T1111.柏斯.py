from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1111   ._SN',
        MapName             = 'Bose',
        Location            = 'T1111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        '梅贝尔市长',                           # 9
        '莉拉',                                 # 10
        '管家门特斯',                           # 11
        '萨拉',                                 # 12
        '米拉诺',                               # 13
    )

    DeclEntryPoint(
        Unknown_00              = 48000,
        Unknown_04              = -3000,
        Unknown_08              = 27000,
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
        'ED6_DT07/CH02360 ._CH',             # 00
        'ED6_DT07/CH01350 ._CH',             # 01
        'ED6_DT07/CH01560 ._CH',             # 02
        'ED6_DT07/CH01230 ._CH',             # 03
        'ED6_DT07/CH02370 ._CH',             # 04
        'ED6_DT07/CH00003 ._CH',             # 05
        'ED6_DT07/CH00013 ._CH',             # 06
        'ED6_DT07/CH00023 ._CH',             # 07
        'ED6_DT07/CH00033 ._CH',             # 08
        'ED6_DT07/CH02363 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH02360P._CP',             # 00
        'ED6_DT07/CH01350P._CP',             # 01
        'ED6_DT07/CH01560P._CP',             # 02
        'ED6_DT07/CH01230P._CP',             # 03
        'ED6_DT07/CH02370P._CP',             # 04
        'ED6_DT07/CH00003P._CP',             # 05
        'ED6_DT07/CH00013P._CP',             # 06
        'ED6_DT07/CH00023P._CP',             # 07
        'ED6_DT07/CH00033P._CP',             # 08
        'ED6_DT07/CH02363P._CP',             # 09
    )

    DeclNpc(
        X                   = -120760,
        Z                   = 200,
        Y                   = 68570,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -3220,
        Z                   = -4000,
        Y                   = 68110,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 500,
        Y                   = -870,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -33400,
        Z                   = -3000,
        Y                   = 35100,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -120820,
        Z                   = 0,
        Y                   = 66250,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_2F6",          # 01, 1
        "Function_2_2F7",          # 02, 2
        "Function_3_30D",          # 03, 3
        "Function_4_331",          # 04, 4
        "Function_5_393",          # 05, 5
        "Function_6_1300",         # 06, 6
        "Function_7_1BA6",         # 07, 7
        "Function_8_2ACC",         # 08, 8
        "Function_9_2C6A",         # 09, 9
        "Function_10_328B",        # 0A, 10
        "Function_11_3BA2",        # 0B, 11
        "Function_12_4AC7",        # 0C, 12
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1CB")
    SetChrPos(0xB, -64150, -3000, 66390, 0)
    SetChrPos(0x9, -123500, 0, 66690, 275)
    SetChrChipByIndex(0x8, 9)
    Jump("loc_27E")

    label("loc_1CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1FA")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrPos(0xB, -64150, -3000, 66390, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x8, 9)
    Jump("loc_27E")

    label("loc_1FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_213")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    SetChrChipByIndex(0x8, 9)
    Jump("loc_27E")

    label("loc_213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_23D")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrPos(0xB, -64150, -3000, 66390, 0)
    SetChrChipByIndex(0x8, 9)
    Jump("loc_27E")

    label("loc_23D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_256")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    SetChrChipByIndex(0x8, 9)
    Jump("loc_27E")

    label("loc_256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_276")
    SetChrPos(0xB, -65000, -3000, 64650, 270)
    SetChrChipByIndex(0x8, 9)
    Jump("loc_27E")

    label("loc_276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27E")

    label("loc_27E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0xB, -6030, 4500, 2470, 275)

    label("loc_2AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_2B9")
    OP_A3(0x3FA)
    Event(0, 12)

    label("loc_2B9")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2C9"),
        (110, "loc_2DF"),
        (SWITCH_DEFAULT, "loc_2F5"),
    )


    label("loc_2C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DC")
    OP_A2(0x309)
    Event(0, 10)

    label("loc_2DC")

    Jump("loc_2F5")

    label("loc_2DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F2")
    OP_A2(0x317)
    Event(0, 11)

    label("loc_2F2")

    Jump("loc_2F5")

    label("loc_2F5")

    Return()

    # Function_0_19A end

    def Function_1_2F6(): pass

    label("Function_1_2F6")

    Return()

    # Function_1_2F6 end

    def Function_2_2F7(): pass

    label("Function_2_2F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2F7")

    label("loc_30C")

    Return()

    # Function_2_2F7 end

    def Function_3_30D(): pass

    label("Function_3_30D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_330")
    OP_8D(0xFE, -37400, -6200, -27800, -1300, 2000)
    Jump("Function_3_30D")

    label("loc_330")

    Return()

    # Function_3_30D end

    def Function_4_331(): pass

    label("Function_4_331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_350")

    label("loc_338")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_338")

    label("loc_34D")

    Jump("loc_392")

    label("loc_350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_37D")

    label("loc_357")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37A")
    OP_8D(0xFE, -34800, 34500, -31600, 36300, 2000)
    Jump("loc_357")

    label("loc_37A")

    Jump("loc_392")

    label("loc_37D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_392")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_37D")

    label("loc_392")

    Return()

    # Function_4_331 end

    def Function_5_393(): pass

    label("Function_5_393")

    TalkBegin(0x8)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B8")
    SetChrSubChip(0xFE, 1)
    Jump("loc_3D3")

    label("loc_3B8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3CE")
    SetChrSubChip(0xFE, 0)
    Jump("loc_3D3")

    label("loc_3CE")

    SetChrSubChip(0xFE, 2)

    label("loc_3D3")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_7A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_778")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#613F啊呀，是艾丝蒂尔……\x01",
            "难道你们现在要出发了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F感谢最近一段时间\x01",
            "您对我们的诸多照顾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#610F呵呵，\x01",
            "受照顾的应该是我们才对。\x02\x03",
            "如果像你们这样的游击士\x01",
            "能一直呆在柏斯的话，\x01",
            "大家一定会很高兴的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F市长姐姐这么说，\x01",
            "我们会觉得非常不好意思的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#610F你们用不着谦虚。\x02\x03",
            "让我再次\x01",
            "代表柏斯市民向你们致谢。\x02\x03",
            "真的是\x01",
            "太谢谢你们两位了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F市长姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#610F那么， \x01",
            "我也不能留你们太久。\x02\x03",
            "艾丝蒂尔、约修亚。\x01",
            "路上小心哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嗯，市长姐姐也要保重身体。\x01",
            "不要让工作累坏了身子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#617F呵呵，刚才已经被莉拉\x01",
            "狠狠地说了一顿了。\x02\x03",
            "我会注意的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么我们就告辞了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A4")

    label("loc_778")


    ChrTalk(
        0x8,
        (
            "#610F艾丝蒂尔、约修亚。\x01",
            "后会有期。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A4")

    Jump("loc_12F7")

    label("loc_7A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_B31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAE")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#610F我刚从米拉诺那里\x01",
            "知道了柏斯超市现在的经营状况。\x01",
            "　\x02\x03",
            "#612F定期船失踪事件还是\x01",
            "造成了非常大的影响啊。\x02\x03",
            "#610F各位……\x01",
            "如果掌握了什么线索，\x01",
            "记得来我这里通知一声哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嘿嘿，知道吗？\x02\x03",
            "虽然还不太确定，\x01",
            "不过也算是得到了一点点线索。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们会在这段时间内，\x01",
            "把收集到的情报呈上给您的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F不过，也可能会是空欢喜一场。\x02\x03",
            "现在唯有请你们等上一段时间了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#610F好的，\x01",
            "那我就期待你们的好消息了。\x02\x03",
            "务必要注意安全。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2E")

    label("loc_AAE")


    ChrTalk(
        0xFE,
        (
            "#612F真是的……\x02\x03",
            "本来就是非常忙的时候，\x01",
            "竟然还接连发生这么多的事件。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2E")

    Jump("loc_12F7")

    label("loc_B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_D87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD0")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#615F在我的朋友里\x01",
            "有一位叫米拉诺的女性……\x02\x03",
            "她的父亲也在\x01",
            "失踪的『林德号』乘客名册上。\x02\x03",
            "#612F像她父亲那样还没有回到家，\x01",
            "让家人十分担心的人也一定还有很多吧。\x01",
            "　\x02\x03",
            "这次强盗案与劫机案\x01",
            "是同一伙人干的可能性非常高。\x02\x03",
            "你们哪怕能查到一丝线索也好……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D84")

    label("loc_CD0")


    ChrTalk(
        0xFE,
        (
            "#612F这次，强盗案与劫机案\x01",
            "是同一伙人干的可能性非常高。\x02\x03",
            "你们哪怕能查到一丝线索也好……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D84")

    Jump("loc_12F7")

    label("loc_D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_10D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1012")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#610F啊，是你们。\x02\x03",
            "事件的调查有没有进展呢？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯～老实说，\x01",
            "情报太少了，还是有点难办。\x02\x03",
            "不过也算是发现了一些线索。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F虽说是线索，\x01",
            "不过也不是什么可靠的情报……\x02\x03",
            "不管怎么说，\x01",
            "我们打算先去拉文努村看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#610F拉文努村……是吗？\x01",
            "我记得军队那边已经调查过了……\x02\x03",
            "不过现在没有别的线索，\x01",
            "我们确实有再次调查的必要。\x02\x03",
            "我明白了，\x01",
            "那就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D6")

    label("loc_1012")


    ChrTalk(
        0xFE,
        (
            "#610F拉文努村……是吗？\x01",
            "我记得军队那边已经调查过了……\x02\x03",
            "不过现在没有别的线索，\x01",
            "我们确实有再次调查的必要。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D6")

    Jump("loc_12F7")

    label("loc_10D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1212")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B7")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#612F嗯～对劫机事件的处理\x01",
            "要放在最优先的地位。\x02\x03",
            "其他资料的整理就以后再做吧。\x01",
            "　\x02\x03",
            "#611F呵呵……\x01",
            "要忙起来了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_120F")

    label("loc_11B7")


    ChrTalk(
        0xFE,
        (
            "#611F呵呵……\x01",
            "要忙起来了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_120F")

    Jump("loc_12F7")

    label("loc_1212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_12F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12AF")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#610F各位游击士，\x01",
            "我期待你们的好消息。\x02\x03",
            "如果能见到摩尔根将军，\x01",
            "请代我向他问好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12F7")

    label("loc_12AF")


    ChrTalk(
        0xFE,
        (
            "#610F如果能见到摩尔根将军，\x01",
            "请代我向他问好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F7")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0x8)
    Return()

    # Function_5_393 end

    def Function_6_1300(): pass

    label("Function_6_1300")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_13B9")

    ChrTalk(
        0xFE,
        (
            "#621F这下小姐终于可以高枕无忧了。\x01",
            "　\x02\x03",
            "真的多亏了大家……\x01",
            "多谢你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA2")

    label("loc_13B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1489")

    ChrTalk(
        0xFE,
        (
            "小姐连续好几天\x01",
            "彻夜不眠地加班加点，\x01",
            "来想办法如何处理强盗事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果我无法好好照顾\x01",
            "小姐的身体状况的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA2")

    label("loc_1489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_16EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1667")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "#620F各位，这真是一场灾难。\x02\x03",
            "游击士协会那边\x01",
            "已经与小姐联系过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F嗯……\x01",
            "虽说拿他们没办法，\x01",
            "但我总觉得很没面子啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F算了，这次的事情是不可抗力造成的。\x01",
            "不能全都怪在王国军头上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F哼哼～\x02\x03",
            "空贼啊空贼～我们走着瞧吧。\x01",
            "下次我一定会抓住你们的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16E8")

    label("loc_1667")


    ChrTalk(
        0xFE,
        (
            "#620F各位，这真是一场灾难。\x02\x03",
            "游击士协会那边\x01",
            "已经与小姐联系过了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E8")

    Jump("loc_1BA2")

    label("loc_16EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_17EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A0")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "小姐就是那种自己越忙\x01",
            "就越有干劲的类型。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这可能是继承了前市长……\x01",
            "她父亲血统的原因吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17E8")

    label("loc_17A0")


    ChrTalk(
        0xFE,
        (
            "可是，\x01",
            "我却非常担心小姐的身体状况……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17E8")

    Jump("loc_1BA2")

    label("loc_17EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_19BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_191E")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "#620F摩尔根将军\x01",
            "来过我们这里很多次了。\x02\x03",
            "不管怎么看，\x01",
            "他都是一位非常出色的军人。\x02\x03",
            "#623F不管是好还是坏，\x01",
            "我觉得他都是一位拥有军人气质的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19BA")

    label("loc_191E")


    ChrTalk(
        0xFE,
        (
            "#620F摩尔根将军\x01",
            "是一位非常出色的军人。\x02\x03",
            "#623F不管是好还是坏，\x01",
            "我觉得他都是一位拥有军人气质的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19BA")

    Jump("loc_1BA2")

    label("loc_19BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_1BA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B0E")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "#620F这次的事情\x01",
            "真的让小姐很头疼。\x02\x03",
            "本来就有一大堆强盗案件\x01",
            "等着小姐去应付……\x02\x03",
            "#621F各位游击士，\x01",
            "请一定要帮小姐的忙……\x02\x03",
            "作为她的随从，\x01",
            "我也会很衷心地拜托你们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA2")

    label("loc_1B0E")


    ChrTalk(
        0xFE,
        (
            "#621F各位游击士，\x01",
            "请一定要帮小姐的忙……\x02\x03",
            "作为她的随从，\x01",
            "我也会很衷心地拜托你们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA2")

    TalkEnd(0x9)
    Return()

    # Function_6_1300 end

    def Function_7_1BA6(): pass

    label("Function_7_1BA6")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1DC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE4")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "真是要好好感谢一下各位才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "小姐如果能\x01",
            "趁此机会休息一下就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她只要一放松，\x01",
            "一些杂事就会找上门来，\x01",
            "这就是她的性格，我真替她担心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DC5")

    label("loc_1CE4")


    ChrTalk(
        0xFE,
        (
            "小姐如果能\x01",
            "趁此机会休息一下就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她只要一放松，\x01",
            "一些杂事就会找上门来，\x01",
            "这就是她的性格，我真替她担心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC5")

    Jump("loc_2AC8")

    label("loc_1DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_210B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FFD")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "在１０年前的战争中，\x01",
            "帝国军破坏了柏斯的街道，\x01",
            "并占据了整个柏斯地区。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "但是，小姐的父亲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也就是前一任市长，以他为先驱，\x01",
            "尽全力复兴这座属于商人的城市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "平时都是各自为政\x01",
            "做自己买卖的大大小小的商人，\x01",
            "就在那个紧要关头团结起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "小姐决定继承父亲的\x01",
            "这个伟大志向也是从那时开始的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2108")

    label("loc_1FFD")


    ChrTalk(
        0xFE,
        (
            "战争结束以后，\x01",
            "小姐的父亲作为先驱，\x01",
            "尽全力复兴这座属于商人的城市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "小姐决定继承父亲的\x01",
            "这个伟大志向也是从那时开始的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2108")

    Jump("loc_2AC8")

    label("loc_210B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2315")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2273")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "虽然我劝过小姐，\x01",
            "请她稍微休息一下的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过她说当务之急是要\x01",
            "消除市民的不安，\x01",
            "让街上恢复平静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我对她能有\x01",
            "如此大的长进感到十分欣慰，\x01",
            "但是我也希望她能够为自己多着想一点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2312")

    label("loc_2273")


    ChrTalk(
        0xFE,
        (
            "小姐能有如此大的长进\x01",
            "让我感到十分地欣慰……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "我也希望她能够为自己多着想一点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2312")

    Jump("loc_2AC8")

    label("loc_2315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2520")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A8")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "小姐当选柏斯市长的时候\x01",
            "因为过于年轻，\x01",
            "反对的声音一直不绝于耳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过当大家看到小姐制定的种种商业政策\x01",
            "让城市迅速发展起来之后，\x01",
            "支持者就陆续出现了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有势商人特里诺家的米拉诺小姐\x01",
            "就是其中的代表。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251D")

    label("loc_24A8")


    ChrTalk(
        0xFE,
        (
            "米拉诺小姐也很年轻，\x01",
            "不过作为商人却十分有才华……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "小姐对她的评价也很高。\x02",
    )

    CloseMessageWindow()

    label("loc_251D")

    Jump("loc_2AC8")

    label("loc_2520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_END)), "loc_25B1")

    ChrTalk(
        0xFE,
        (
            "各位辛苦了。\x01",
            "看起来调查似乎有所进展呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "小姐她也非常努力，\x01",
            "现在正干劲十足呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AC8")

    label("loc_25B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_261C")

    ChrTalk(
        0xFE,
        "各位，欢迎回来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "小姐正在\x01",
            "急切等待各位的报告。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AC8")

    label("loc_261C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_27C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_271D")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "哦，各位……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们是来找小姐……\x01",
            "……市长的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "无论有什么事情，\x01",
            "我们都欢迎你们随时过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "小姐吩咐过，无论什么时候，\x01",
            "我们都十分欢迎你们的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27C1")

    label("loc_271D")


    ChrTalk(
        0xFE,
        (
            "有什么事情的话，\x01",
            "欢迎随时过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "小姐吩咐过，无论什么时候，\x01",
            "我们都十分欢迎你们的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27C1")

    Jump("loc_2AC8")

    label("loc_27C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_END)), "loc_2986")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2886")

    ChrTalk(
        0xFE,
        (
            "你们可能已经知道了，\x01",
            "超市就在北街区的中央。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从我们官邸正门出去，\x01",
            "对面就是了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2983")

    label("loc_2886")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "哦，各位……\x01",
            "你们已经找到莉拉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "市长呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#621F还在超市。\x01",
            "我们正要去接她……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈，不愧是小姐啊，\x01",
            "对工作如此热心……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2983")

    Jump("loc_2AC8")

    label("loc_2986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2A27")

    ChrTalk(
        0xFE,
        (
            "市长刚刚去\x01",
            "七耀教会做礼拜了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有一个女佣与市长同行，\x01",
            "你们就记住这个特征吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AC8")

    label("loc_2A27")


    ChrTalk(
        0xFE,
        (
            "真是非常抱歉，\x01",
            "市长现在不在官邸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果各位有什么事情的话，\x01",
            "麻烦稍后再来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AC8")

    TalkEnd(0xA)
    Return()

    # Function_7_1BA6 end

    def Function_8_2ACC(): pass

    label("Function_8_2ACC")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BED")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "根据梅贝尔小姐所说的来看，\x01",
            "定期船失踪很有可能是空贼团做的好事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以赎金的数量来看，\x01",
            "父亲多半还活着吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样母亲也总算\x01",
            "能够暂时安心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C66")

    label("loc_2BED")


    ChrTalk(
        0xFE,
        (
            "你们是来调查\x01",
            "这个事件的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "拜托你们了！\x02",
    )

    CloseMessageWindow()

    label("loc_2C66")

    TalkEnd(0xC)
    Return()

    # Function_8_2ACC end

    def Function_9_2C6A(): pass

    label("Function_9_2C6A")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2DCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D45")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "最近都是由\x01",
            "莉拉来决定每天的食谱的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "蔬菜不太够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "等会儿去超市买点回来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DC8")

    label("loc_2D45")


    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "蔬菜不太够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "等会儿去超市买点回来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DC8")

    Jump("loc_3287")

    label("loc_2DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2EAA")

    ChrTalk(
        0xFE,
        (
            "大小姐真的非常繁忙……\x01",
            "如果能尽早将事件解决就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果能够恢复平静，\x01",
            "我就要约莉拉\x01",
            "一起去外面购物。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3287")

    label("loc_2EAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2F25")

    ChrTalk(
        0xFE,
        "快要到下午茶的时间了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我虽然很笨，\x01",
            "不过在泡茶技术这点上\x01",
            "是不会输给莉拉的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3287")

    label("loc_2F25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2FCA")

    ChrTalk(
        0xFE,
        (
            "小姐不仅是个美人，\x01",
            "还头脑聪明待人可亲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊～简直就是我梦寐以求的类型㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_3287")

    label("loc_2FCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_END)), "loc_3203")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_305E")
    TurnDirection(0xFE, 0x134, 0)

    ChrTalk(
        0xFE,
        (
            "莉、莉拉……\x01",
            "扫除马上就能做完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我可没有\x01",
            "偷懒去吃冰淇淋哦……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3200")

    label("loc_305E")

    OP_A2(0x4)
    TurnDirection(0xFE, 0x134, 0)

    ChrTalk(
        0xFE,
        "啊、哎……莉拉！？\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(700)

    ChrTalk(
        0xFE,
        "这、这么早就回来了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#620F……事情还没有办完呢。\x01",
            "我们正准备去超市接市长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是、是这样啊。\x01",
            "扫除马上就能做完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我、我可没有\x01",
            "偷懒去吃冰淇淋哦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F（莉拉小姐这么可怕吗？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（不知道……\x01",
            "　不过应该是有着独特魄力的人吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3200")

    Jump("loc_3287")

    label("loc_3203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_3287")

    ChrTalk(
        0xFE,
        (
            "如果不趁现在\x01",
            "赶快打扫完毕的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(700)

    ChrTalk(
        0xFE,
        "又会被莉拉骂的。\x02",
    )

    CloseMessageWindow()

    label("loc_3287")

    TalkEnd(0xB)
    Return()

    # Function_9_2C6A end

    def Function_10_328B(): pass

    label("Function_10_328B")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, 4000, 0, -5860, 0)
    SetChrPos(0x102, 3280, 0, -7224, 0)
    SetChrPos(0x103, 4570, 0, -6990, 0)
    SetChrPos(0xA, -1454, 500, 3536, 135)

    def lambda_32DC():
        OP_6D(840, 500, 1500, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_32DC)
    Sleep(2500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#004F哇啊啊～好豪华的房子啊……\x02\x03",
            "#001F快看快看，那个大吊灯！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#017F不要兴奋过头了，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    def lambda_338E():
        OP_6D(2860, 500, -380, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_338E)

    def lambda_33A6():
        OP_8E(0x101, 0x12B6, 0x0, 0xFFFFF27C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_33A6)
    Sleep(200)

    def lambda_33C6():
        OP_8E(0x102, 0xC9E, 0x0, 0xFFFFF060, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_33C6)
    Sleep(500)
    OP_8E(0x103, 0x10E0, 0x0, 0xFFFFEF02, 0xBB8, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x103,
        (
            "#020F看起来，\x01",
            "这里就是柏斯市长的官邸了。\x02\x03",
            "不知道市长在不在呢？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8)
    OP_4A(0xA, 0)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_6F(0x0, 30)
    Sleep(500)

    def lambda_3483():

        label("loc_3483")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_3483")

    QueueWorkItem2(0x101, 1, lambda_3483)

    def lambda_3494():

        label("loc_3494")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_3494")

    QueueWorkItem2(0x102, 1, lambda_3494)

    def lambda_34A5():

        label("loc_34A5")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_34A5")

    QueueWorkItem2(0x103, 1, lambda_34A5)
    OP_8E(0xA, 0xFFFFFD9E, 0x1F4, 0x474, 0x7D0, 0x0)
    TurnDirection(0xA, 0x103, 400)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_72(0x0, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x0, 0x0)
    Sleep(500)
    OP_71(0x0, 0x800)

    ChrTalk(
        0xA,
        "哎呀，是客人吗？\x02",
    )

    CloseMessageWindow()

    def lambda_3521():
        OP_6D(3750, 250, -2570, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3521)
    OP_8E(0xA, 0xCE4, 0x1F4, 0xFFFFFCAE, 0xBB8, 0x0)
    OP_8C(0xA, 180, 400)

    ChrTalk(
        0xA,
        (
            "欢迎光临。\x01",
            "这里是柏斯市长官邸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "请问各位客人有何贵干呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F我们是游击士协会的人。\x02\x03",
            "这次来访是想\x01",
            "详细了解一下市长委托的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "原来如此，我明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "可是，真的很不凑巧，\x01",
            "市长刚好出去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "应该是在礼拜堂做礼拜吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请问大概什么时候会回来呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "这个我也说不准……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "实际上，就算市长\x01",
            "现在突然回来也完全不奇怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊，是这样啊。\x02\x03",
            "那么我们到教会\x01",
            "去找找市长怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "可、可是……\x01",
            "要劳驾客人你们实在是不好意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F别介意。\x01",
            "这样对我们来说也省事了。\x02\x03",
            "说起来……\x01",
            "市长是什么样子的呢？\x02\x03",
            "肯定是一幅有钱人的样子吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "说到外貌啊……唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "无论是言行还是气质，\x01",
            "都越来越优秀、越来越优雅了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "要是能找到合适的另一半，\x01",
            "我就可以放心地隐退了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "啊！……失礼了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "啊啊，对了，\x01",
            "和市长同行的还有一位女佣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "这样找的话会比较方便些。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F带着女佣的人……\x01",
            "这样就很容易分辨了。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#006F我们赶快去教会吧。\x02",
    )

    CloseMessageWindow()
    OP_28(0x35, 0x1, 0x8)
    OP_4B(0xA, 0)
    EventEnd(0x0)
    Return()

    # Function_10_328B end

    def Function_11_3BA2(): pass

    label("Function_11_3BA2")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-120000, 0, 67000, 0)
    SetChrPos(0x8, -120760, 200, 68570, 180)
    SetChrPos(0x101, -118370, 0, 64050, 0)
    SetChrPos(0x102, -117260, 0, 64450, 315)
    SetChrPos(0x103, -117990, 0, 62790, 0)
    OP_67(0, 6030, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(314000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#612F市民的不满和意见的处理……\x02\x03",
            "由于柏斯上空飞行管制\x01",
            "造成的市场商品进货推迟……\x02\x03",
            "#615F下水道设备的修理……\x02\x03",
            "给女王陛下的礼品的选定……\x02\x03",
            "安塞尔新街的魔兽作乱……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#616F不行了～什么时候\x01",
            "才能把这些文书处理完啊～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F请问……\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x8, 1)
    OP_6D(-120700, 0, 68200, 1000)

    ChrTalk(
        0x8,
        (
            "#613F哎、哎呀……？\x02\x03",
            "#617F呵呵，各位。\x01",
            "原来你们已经回来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F看来您正在忙于公务……\x01",
            "不过我们可以占用一些时间吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#615F咳咳，当然可以。\x02\x03",
            "#611F是从摩尔根将军那得到的消息吗？\x01",
            "请赶快告诉我吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-120570, 1000, 67100, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(314000, 0)
    OP_6E(280, 0)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x101, -120910, 0, 66260, 0)
    SetChrPos(0x102, -119750, 0, 66130, 0)
    SetChrPos(0x103, -120500, 0, 65129, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#615F……真是辛苦你们了。\x01",
            "大概的情况我已经了解了。\x02\x03",
            "空贼团劫机，\x01",
            "然后要求赎金对吧……\x02\x03",
            "#612F事态比我想象的要严重啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F如果能隐瞒住游击士的身份，\x01",
            "也许还能探听出其它的情报……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#610F哪里，得到的并非坠机事故的消息，\x01",
            "这就已经帮了我们很大的忙了。\x02\x03",
            "接下来就是以柏斯市的立场\x01",
            "来制定解决对策了。\x02\x03",
            "要赶快向市民发表公告还有\x01",
            "考虑应对乘客家属的措施才行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F真是繁忙啊……\x01",
            "每天都要处理这么多的事务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#611F呵呵，那是市长的职责所在啊……\x02\x03",
            "#612F话说回来，\x01",
            "既然知道了犯人的真实身份……\x02\x03",
            "能不能拜托你们\x01",
            "继续调查并解决这个事件呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F当然，我们也正有这个打算。\x02\x03",
            "况且我们和那个空贼团\x01",
            "还有笔没算完的帐呢。\x02\x03",
            "我以游击士协会的荣誉担保，\x01",
            "必定在王国军之前把这个事件解决！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，说得对啊！\x02\x03",
            "还有老爸的事情，\x01",
            "这次也一并解决掉！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F…………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F#1P嗯，怎么了？\x01",
            "一脸严肃的样子……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#013F#4P唔……\x01",
            "尽管考虑了各种各样的情况。\x02\x03",
            "但不管怎么想，还是觉得不可思议。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#1P不可思议？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#4P有父亲在，\x01",
            "竟然也会被空贼得手。\x02\x03",
            "以在洛连特出现的\x01",
            "那伙人的实力来判断的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F确实如你所说。\x02\x03",
            "如果是对付那种程度的集团，\x01",
            "以老师的实力还是游刃有余的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)

    ChrTalk(
        0x101,
        (
            "#007F#1P哎呀，真是的……\x01",
            "约修亚和雪拉姐都把老爸想得太厉害了。\x02\x03",
            "他的身手的确很棒，可是要和整个集团对抗，\x01",
            "我觉得还是很够呛的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#613F………………………\x02\x03",
            "那个，稍稍打断一下可以吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_474C():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_474C)

    def lambda_475A():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_475A)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x8,
        (
            "#612F艾丝蒂尔你们的父亲\x01",
            "也搭乘了那艘定期船吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊，这个还没跟您说……\x02\x03",
            "说起来真让人觉得不好意思。\x01",
            "其实他也是一名游击士呢。\x02\x03",
            "他的名字叫卡西乌斯·布莱特。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#614F卡西乌斯·布莱特……\x01",
            "刚才你说的就是他！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎……嗯？？\x02\x03",
            "难道您认识我老爸？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#612F虽然没有和他见过面，\x01",
            "但是，他的大名我耳闻已久。\x02\x03",
            "原来……原来如此啊……\x02\x03",
            "这样的话，\x01",
            "说不定可以借此和军队进行交涉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F市长姐姐？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#615F……刚才真不好意思。\x01",
            "各位的心情我可以理解。\x02\x03",
            "#610F只要能解决这个事件，\x01",
            "无论要提供什么样的协助，我都在所不惜。\x02\x03",
            "有需要的时候，请各位不必\x01",
            "多虑，尽管提出来。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x400000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_3BA2 end

    def Function_12_4AC7(): pass

    label("Function_12_4AC7")

    OP_A2(0x32B)
    OP_28(0x37, 0x4, 0x2)
    OP_28(0x37, 0x4, 0x4)
    OP_28(0xF, 0x4, 0x40)
    OP_28(0x10, 0x4, 0x40)
    OP_28(0x12, 0x4, 0x40)
    OP_28(0x17, 0x4, 0x40)
    EventBegin(0x0)
    OP_6D(-63360, 0, -3290, 0)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x8, -64900, 200, -3990, 90)
    SetChrPos(0x101, -62760, 200, -5590, 0)
    SetChrPos(0x102, -60990, 200, -5640, 0)
    SetChrPos(0x103, -60990, 200, -2330, 180)
    SetChrPos(0x104, -62760, 200, -2330, 180)
    SetChrChipByIndex(0x8, 9)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x103, 7)
    SetChrChipByIndex(0x104, 8)
    SetChrSubChip(0x102, 1)
    SetChrSubChip(0x103, 2)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#007F没想到这家伙\x01",
            "真的被释放出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#027F好运来了挡也挡不住啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F哈·哈·哈。\x01",
            "你们就别这么夸奖人家嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 2)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#030F可是，白白喝了那瓶酒，\x01",
            "想起来还真的非常内疚啊。\x02\x03",
            "按照之前的约定，\x01",
            "我会为餐厅弹奏钢琴以作补偿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#610F呵呵，这就不用麻烦你了。\x02\x03",
            "因为那件事引起了不少的骚动，\x01",
            "大家再见面也会很尴尬吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F（唔，这家伙也真是的，\x01",
            "　一点都不知道自己的过错……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F（的确是脸皮超级厚啊……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#610F算了，其实这件事\x01",
            "也不能完全算作不幸的事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#033F可是……\x01",
            "我真的感到有点内疚啊。\x02\x03",
            "嗯，对了……\x02\x03",
            "#030F你们不是正在\x01",
            "调查一桩什么案件吗？\x02\x03",
            "作为那瓶酒的谢礼，\x01",
            "我愿意协助你们的调查工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#611F这样啊，听起来挺有趣的。\x02\x03",
            "可是会不会麻烦你呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#030F没问题，就包在我身上吧。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#031F就这样定了。\x01",
            "你们以后要多多关照哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F先等一下……\x01",
            "谁叫你就这样定了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F如果要一个门外汉跟着我们，\x01",
            "老实说也很不方便……\x02\x03",
            "你有自信不会拖我们的后腿吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 1)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#035F#1P我对自己的枪法和魔法颇有自信。\x02\x03",
            "要知道，天才可不单会演奏，\x01",
            "就连其他技能也都不在话下哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F听了你这一段台词之后，\x01",
            "我越来越感到强烈的不安了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F多一个人帮忙也无妨啊。\x02\x03",
            "毕竟无法指望军队做些什么，\x01",
            "而我们又处于人手不足的状况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026F…………………………\x02\x03",
            "#020F算了。\x01",
            "就让你协助我们的工作吧。\x02\x03",
            "不过事先声明，你要是碍手碍脚的话，\x01",
            "我可会毫不客气地请你离队哦……\x02\x03",
            "明白了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F呵呵，没问题。\x02\x03",
            "我绝对不会让大家失望的，\x01",
            "敬请期待天才演奏家的精彩演出吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F嗯，我们不会失望的，\x01",
            "因为从一开始就没对你抱有期望。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#615F呵呵……\x01",
            "闲话就先到此为止吧。\x02\x03",
            "#612F因为我还有\x01",
            "一件重要的事情要告诉大家。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0x104, 0)
    Sleep(100)
    SetChrSubChip(0x104, 2)
    Sleep(300)

    ChrTalk(
        0x101,
        "#501F重要的事情？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F说起来，在我们来之前，\x01",
            "街上好像发生了什么骚动吧。\x02\x03",
            "究竟是什么事呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#612F我要说的就是这件事……\x02\x03",
            "其实昨天晚上，柏斯南街区发生了\x01",
            "多起大规模的强盗事件。\x02\x03",
            "以武器店和导力器工房为首的\x01",
            "多家商店都遭到了抢劫。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F难道说……\x01",
            "这也是空贼做的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#612F目前还不清楚是何人所为，\x01",
            "不过空贼的嫌疑最大。\x02\x03",
            "现在，王国军的部队正在对\x01",
            "这些连环案件进行调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F原来如此。\x01",
            "看来我们也要马上展开调查才行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#610F嗯，拜托大家了。\x02\x03",
            "至于之前的调查费用\x01",
            "我已经预先向协会支付了。\x02\x03",
            "作为日常的开支，希望\x01",
            "你们能够好好利用。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x35, 0x4, 0x10)
    OP_28(0x36, 0x4, 0x10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrPos(0x101, 3450, 0, -5820, 0)
    SetChrPos(0x102, 4730, 0, -4890, 315)
    SetChrPos(0x103, 2900, 0, -4059, 135)
    SetChrPos(0x104, 4170, 0, -3340, 180)
    SetChrPos(0xA, -6290, 500, -8460, 296)
    SetChrPos(0x8, -120760, 0, 68570, 180)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x104, 65535)
    TurnDirection(0x101, 0x104, 0)
    TurnDirection(0x102, 0x103, 0)
    TurnDirection(0x103, 0x102, 0)
    TurnDirection(0x104, 0x101, 0)
    OP_6D(2900, 0, -3860, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#006F#3P虽然我觉得\x01",
            "军队那些人还会来搅局……\x02\x03",
            "算了，到时候再说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#4P先不说他们会不会来搅局……\x02\x03",
            "我觉得即使我们掌握了什么情报，\x01",
            "也最好不要告诉军队。\x02\x03",
            "要是军队真的有间谍的话，\x01",
            "那么肯定会泄漏给空贼知道的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F#1P只有这样做了，虽然不是我们的本意。\x02\x03",
            "总之，谨慎行动吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#2P呵呵，那么诸位，\x01",
            "马上前往南街区看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#3P我～知～道！\x01",
            "为什么要听你发号施令啊！\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_12_4AC7 end

    SaveToFile()

Try(main)
