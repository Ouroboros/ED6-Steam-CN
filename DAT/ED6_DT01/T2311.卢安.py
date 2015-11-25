from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2311   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2311.x',
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
        '迪恩',                                 # 9
        '雷斯',                                 # 10
        '洛克',                                 # 11
        '青年',                                 # 12
        '青年',                                 # 13
        '青年',                                 # 14
        '青年',                                 # 15
        '青年',                                 # 16
        '青年',                                 # 17
        '秘书基尔巴特',                         # 18
        '卡露娜',                               # 19
        '阿梅莉娅',                             # 20
        '扎古',                                 # 21
        '索雷诺',                               # 22
        '塞尔吉村长',                           # 23
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
        'ED6_DT07/CH00374 ._CH',             # 00
        'ED6_DT07/CH02420 ._CH',             # 01
        'ED6_DT07/CH01240 ._CH',             # 02
        'ED6_DT07/CH01050 ._CH',             # 03
        'ED6_DT07/CH01460 ._CH',             # 04
        'ED6_DT07/CH01040 ._CH',             # 05
        'ED6_DT07/CH01000 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH00374P._CP',             # 00
        'ED6_DT07/CH02420P._CP',             # 01
        'ED6_DT07/CH01240P._CP',             # 02
        'ED6_DT07/CH01050P._CP',             # 03
        'ED6_DT07/CH01460P._CP',             # 04
        'ED6_DT07/CH01040P._CP',             # 05
        'ED6_DT07/CH01000P._CP',             # 06
    )

    DeclNpc(
        X                   = -31270,
        Z                   = 0,
        Y                   = 42780,
        Direction           = 90,
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
        X                   = -30310,
        Z                   = 0,
        Y                   = 42270,
        Direction           = 90,
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
        X                   = -28770,
        Z                   = 0,
        Y                   = 42770,
        Direction           = 90,
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
        X                   = -31020,
        Z                   = 0,
        Y                   = 44700,
        Direction           = 90,
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
        X                   = -30070,
        Z                   = 0,
        Y                   = 44130,
        Direction           = 90,
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
        X                   = -29310,
        Z                   = 0,
        Y                   = 43790,
        Direction           = 90,
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
        X                   = -31330,
        Z                   = 0,
        Y                   = 43790,
        Direction           = 90,
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
        X                   = -30780,
        Z                   = 0,
        Y                   = 43810,
        Direction           = 90,
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
        X                   = -30050,
        Z                   = 0,
        Y                   = 43240,
        Direction           = 90,
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
        X                   = -26650,
        Z                   = 0,
        Y                   = 44050,
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
        X                   = -30050,
        Z                   = 0,
        Y                   = 39240,
        Direction           = 0,
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
        X                   = -200,
        Z                   = 0,
        Y                   = 8850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -3700,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -33200,
        Z                   = 0,
        Y                   = 5700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -26100,
        Z                   = 0,
        Y                   = 4800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    ScpFunction(
        "Function_0_2C2",          # 00, 0
        "Function_1_3F3",          # 01, 1
        "Function_2_3F4",          # 02, 2
        "Function_3_40A",          # 03, 3
        "Function_4_4C0",          # 04, 4
        "Function_5_69C",          # 05, 5
        "Function_6_738",          # 06, 6
        "Function_7_862",          # 07, 7
        "Function_8_8C4",          # 08, 8
    )


    def Function_0_2C2(): pass

    label("Function_0_2C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2CC")
    Jump("loc_374")

    label("loc_2CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_309")
    SetChrPos(0x14, -26670, 0, 39530, 90)
    SetChrPos(0x16, -30150, 0, 3860, 270)
    SetChrPos(0x15, -29310, 0, 43880, 0)
    Jump("loc_374")

    label("loc_309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_313")
    Jump("loc_374")

    label("loc_313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_331")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8)
    Jump("loc_374")

    label("loc_331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_34F")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8)
    Jump("loc_374")

    label("loc_34F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_359")
    Jump("loc_374")

    label("loc_359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_363")
    Jump("loc_374")

    label("loc_363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_36D")
    Jump("loc_374")

    label("loc_36D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_374")

    label("loc_374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A1")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8)

    label("loc_3A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E4")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_3F2")
    OP_A3(0x3FA)
    Event(0, 8)

    label("loc_3F2")

    Return()

    # Function_0_2C2 end

    def Function_1_3F3(): pass

    label("Function_1_3F3")

    Return()

    # Function_1_3F3 end

    def Function_2_3F4(): pass

    label("Function_2_3F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_409")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3F4")

    label("loc_409")

    Return()

    # Function_2_3F4 end

    def Function_3_40A(): pass

    label("Function_3_40A")

    TalkBegin(0x13)

    ChrTalk(
        0xFE,
        (
            "扎古到游击士协会\x01",
            "通报情况去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "出事的时候\x01",
            "弟弟还是值得依靠的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_3_40A end

    def Function_4_4C0(): pass

    label("Function_4_4C0")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CD")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "知道谁是犯人了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "做了那么过分的事，\x01",
            "决不能放过他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一定要抓住犯人，\x01",
            "并狠狠地惩罚他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_698")

    label("loc_5CD")


    ChrTalk(
        0xFE,
        (
            "做了那么过分的事，\x01",
            "决不能放过他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一定要抓住犯人，\x01",
            "并狠狠地惩罚他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_698")

    TalkEnd(0x14)
    Return()

    # Function_4_4C0 end

    def Function_5_69C(): pass

    label("Function_5_69C")

    TalkBegin(0x15)

    ChrTalk(
        0xFE,
        (
            "我想先给孩子们\x01",
            "做些吃的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我和旅店的卡拉商量了一下，\x01",
            "要了些做菜的材料。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x15)
    Return()

    # Function_5_69C end

    def Function_6_738(): pass

    label("Function_6_738")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F4")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "像这样的事件……\x01",
            "绝对不允许再发生了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个村庄的每个人\x01",
            "都会支持你们的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了孩子们，\x01",
            "请一定要抓住犯人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85E")

    label("loc_7F4")


    ChrTalk(
        0xFE,
        (
            "像这样的事件……\x01",
            "绝对不允许再发生了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了孩子们，\x01",
            "请一定要抓住犯人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85E")

    TalkEnd(0x16)
    Return()

    # Function_6_738 end

    def Function_7_862(): pass

    label("Function_7_862")

    TalkBegin(0x12)

    ChrTalk(
        0x12,
        (
            "那帮家伙由我看着。\x02\x03",
            "你们就赶去卢安，\x01",
            "向嘉恩报告昨天的事情吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_7_862 end

    def Function_8_8C4(): pass

    label("Function_8_8C4")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-29840, 0, 41310, 0)
    RemoveParty(0x5, 0xFF)
    SetChrPos(0x101, -29970, 0, 37680, 0)
    SetChrPos(0x102, -30850, 0, 37060, 0)
    SetChrPos(0x105, -29450, 0, 36780, 0)
    OP_8C(0x12, 180, 0)

    ChrTalk(
        0x12,
        (
            "好了……\x01",
            "那帮家伙由我看着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "你们就赶去卢安，\x01",
            "向嘉恩报告昨天的事情吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F我们倒是没关系，不过……\x01",
            "卡露娜姐姐您已经没事了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "当然啦。只是被人抓住破绽，\x01",
            "熏了点催眠药而已嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "还真是丢脸啊。\x01",
            "竟然被那些家伙钻了空子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这也不能怪您。\x02\x03",
            "我们也是四人联手\x01",
            "才勉强击退那些犯人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F那些孩子们平安无事，\x01",
            "也都多亏了卡露娜小姐啊。\x02\x03",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "哈哈……\x01",
            "是啊，总算是不幸中的大幸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "我听说阿加特\x01",
            "自己一个人去追那帮家伙了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "虽然他的身手不容置疑，\x01",
            "但说到底还是有点担心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯、嗯……\x01",
            "要是没捉到他们反而受伤的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F现在也唯有相信阿加特先生了。\x02\x03",
            "从昨天他所说的话判断，\x01",
            "他好像一直在追那些犯人。\x02\x03",
            "对于他们的做事手法似乎也很了解，\x01",
            "我想应该不会那么轻易失手的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯……也对呢。\x02\x03",
            "所以，我们现在也应该\x01",
            "尽力做好自己能做的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "没错，就是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "在事情了结之前，\x01",
            "这些属于特蕾莎院长的捐款\x01",
            "就先由我来暂代保管吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "这次我一定会保护好的，\x01",
            "所以你们就安心出发吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F好的，拜托你了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(
        0x101,
        "#000F那么，我们走吧！\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_8_8C4 end

    SaveToFile()

Try(main)
