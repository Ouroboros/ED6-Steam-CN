from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2310   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2310.x',
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
        X                   = -25570,
        Z                   = 0,
        Y                   = 2300,
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
        X                   = -27510,
        Z                   = 0,
        Y                   = 8670,
        Direction           = 0,
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
        "Function_1_420",          # 01, 1
        "Function_2_442",          # 02, 2
        "Function_3_458",          # 03, 3
        "Function_4_12BE",         # 04, 4
        "Function_5_1D3E",         # 05, 5
        "Function_6_24F9",         # 06, 6
        "Function_7_3053",         # 07, 7
        "Function_8_30AE",         # 08, 8
    )


    def Function_0_2C2(): pass

    label("Function_0_2C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2FF")
    SetChrPos(0x14, -26670, 0, 39530, 90)
    SetChrPos(0x16, -30150, 0, 3860, 270)
    SetChrPos(0x15, -29310, 0, 43880, 0)
    Jump("loc_3E4")

    label("loc_2FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_313")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8)
    Jump("loc_3E4")

    label("loc_313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_31D")
    Jump("loc_3E4")

    label("loc_31D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_33B")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8)
    Jump("loc_3E4")

    label("loc_33B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_359")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8)
    Jump("loc_3E4")

    label("loc_359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_396")
    SetChrPos(0x14, -26670, 0, 39530, 90)
    SetChrPos(0x16, -30150, 0, 3860, 270)
    SetChrPos(0x15, -29310, 0, 43880, 0)
    Jump("loc_3E4")

    label("loc_396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3D3")
    SetChrPos(0x14, -26670, 0, 39530, 90)
    SetChrPos(0x16, -30150, 0, 3860, 270)
    SetChrPos(0x15, -29310, 0, 43880, 0)
    Jump("loc_3E4")

    label("loc_3D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_3DD")
    Jump("loc_3E4")

    label("loc_3DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_3E4")

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_411")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_411")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8)

    label("loc_411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_41F")
    OP_A3(0x3FA)
    Event(0, 8)

    label("loc_41F")

    Return()

    # Function_0_2C2 end

    def Function_1_420(): pass

    label("Function_1_420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_438")
    OP_B1("t2310_y")
    Jump("loc_441")

    label("loc_438")

    OP_B1("t2310_n")

    label("loc_441")

    Return()

    # Function_1_420 end

    def Function_2_442(): pass

    label("Function_2_442")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_457")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_442")

    label("loc_457")

    Return()

    # Function_2_442 end

    def Function_3_458(): pass

    label("Function_3_458")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4C7")

    ChrTalk(
        0xFE,
        (
            "扎古这次\x01",
            "又跑到哪里去了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还想要他\x01",
            "去卢安买东西呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12BA")

    label("loc_4C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_558")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_535")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "听说犯人都藏在\x01",
            "巴伦诺灯塔里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不知道守护灯塔的\x01",
            "弗科特爷爷有没有出事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_555")

    label("loc_535")


    ChrTalk(
        0xFE,
        (
            "不知道守护灯塔的\x01",
            "弗科特爷爷有没有出事……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_555")

    Jump("loc_12BA")

    label("loc_558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_614")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E1")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "孩子们都一边哭，\x01",
            "一边回来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是让人担心啊……\x01",
            "是不是碰到什么事了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_611")

    label("loc_5E1")


    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "扎古去了哪里呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_611")

    Jump("loc_12BA")

    label("loc_614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_C23")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_AFF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8A")
    OP_28(0x1F, 0x1, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_777")

    ChrTalk(
        0xFE,
        "啊，是各位游击士……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "叔父还是没有回家来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，已经没事了。\x02\x03",
            "现在，您叔父\x01",
            "应该已经精神抖擞地向卢安进发了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F您叔父在古罗尼山道\x01",
            "被魔兽袭击的时候，\x01",
            "我们正巧路过把他救了出来。\x02\x03",
            "他没有受伤，请您放心。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_992")

    label("loc_777")


    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "叔父真是的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道真的\x01",
            "自己一个人\x01",
            "去了古罗尼山道吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，\x01",
            "你说的那个叔父，\x02\x03",
            "难不成是去采野菜了吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "他确实这么说过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F那就没事了。\x02\x03",
            "他现在正在去卢安的路上呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F您叔父在古罗尼山道\x01",
            "被魔兽袭击的时候，\x01",
            "我们正巧路过把他救了出来。\x02\x03",
            "他没有受伤，请您放心。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_992")

    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "啊，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对不起啊。\x01",
            "给你们添麻烦了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "发生那种事情，\x01",
            "叔父好歹也该跟家里说一声吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "他也太性急了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFC")

    label("loc_A8A")


    ChrTalk(
        0xFE,
        (
            "对不起啊。\x01",
            "给你们添麻烦了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "叔父他也太性急了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFC")

    Jump("loc_C20")

    label("loc_AFF")


    ChrTalk(
        0xFE,
        (
            "以前我是和扎古还有叔父\x01",
            "三个人一起生活的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从奥维德叔父走了之后\x01",
            "已经过了好几年了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然他偶尔也会回来，\x01",
            "但是马上又不见踪影了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "我可不希望扎古也变成那样……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C20")

    Jump("loc_12BA")

    label("loc_C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_D12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCD")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "听说孤儿院的火灾\x01",
            "是有人故意纵火造成的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好过分啊……\x01",
            "那些人为什么要这么做……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我等会儿也要去\x01",
            "卡拉那里帮忙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D0F")

    label("loc_CCD")


    ChrTalk(
        0xFE,
        (
            "听说孤儿院的火灾\x01",
            "是有人故意纵火造成的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好过分啊……\x02",
    )

    CloseMessageWindow()

    label("loc_D0F")

    Jump("loc_12BA")

    label("loc_D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_E4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD4")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "昨天晚上，一听说孤儿院着火，\x01",
            "扎古就飞奔出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在好像又在\x01",
            "处理火灾的后事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这种时候\x01",
            "他还真靠得住。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E48")

    label("loc_DD4")


    ChrTalk(
        0xFE,
        (
            "昨天晚上，一听说孤儿院着火，\x01",
            "扎古就飞奔出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这种时候\x01",
            "他还真靠得住。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E48")

    Jump("loc_12BA")

    label("loc_E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_F9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F19")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "啊啊～\x01",
            "老是担心弟弟的话，\x01",
            "我就要成老寡妇了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过在扎古成家之前，\x01",
            "还是得不断操心啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "实在没办法\x01",
            "先考虑自己的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F9B")

    label("loc_F19")


    ChrTalk(
        0xFE,
        (
            "啊啊～\x01",
            "老是担心弟弟的话，\x01",
            "我就要成老寡妇了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过在扎古成家之前，\x01",
            "还是得不断操心啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F9B")

    Jump("loc_12BA")

    label("loc_F9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_10FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_107C")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "扎古今后\x01",
            "到底想做什么呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不认真工作的话，\x01",
            "可不会有女孩子喜欢上他哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个孩子，\x01",
            "一直都很让人替他操心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10FA")

    label("loc_107C")


    ChrTalk(
        0xFE,
        (
            "扎古今后\x01",
            "到底想做什么呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个孩子，\x01",
            "一直都很让人替他操心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10FA")

    Jump("loc_12BA")

    label("loc_10FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_116E")

    ChrTalk(
        0xFE,
        "问我有没有看到一个男孩？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要说这村里的孩子，\x01",
            "只有卢希娅一个，\x01",
            "看来他不是这个村里的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12BA")

    label("loc_116E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_12BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1237")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "扎古在卢安工作的时候被开除了，\x01",
            "然后就回村里来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "一点也不为自己的将来着想。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我作为他的姐姐，\x01",
            "为他担心得不得了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12BA")

    label("loc_1237")


    ChrTalk(
        0xFE,
        (
            "扎古在卢安工作的时候被开除了，\x01",
            "然后就回村里来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "一点也不为自己的将来着想。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BA")

    TalkEnd(0x13)
    Return()

    # Function_3_458 end

    def Function_4_12BE(): pass

    label("Function_4_12BE")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1442")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13AE")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "真没想到竟然是市长他们犯的罪，\x01",
            "太让人吃惊了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，事件被查证清楚后\x01",
            "老师他们应该也能获得赔偿金吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是修建孤儿院的话，\x01",
            "我是很乐意帮忙的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_143F")

    label("loc_13AE")


    ChrTalk(
        0xFE,
        (
            "事件被查证清楚后，\x01",
            "老师他们应该也能获得赔偿金吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是修建孤儿院的话，\x01",
            "我是很乐意帮忙的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_143F")

    Jump("loc_1D3A")

    label("loc_1442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_15AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1533")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "纵火犯被关起来了，\x01",
            "是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是你们逮捕他们的吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "干得好啊！\x01",
            "不愧是守护正义的游击士。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15AC")

    label("loc_1533")


    ChrTalk(
        0xFE,
        (
            "就是你们\x01",
            "把纵火犯给逮捕了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "干得好啊！\x01",
            "不愧是守护正义的游击士。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15AC")

    Jump("loc_1D3A")

    label("loc_15AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1824")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_16B1")

    ChrTalk(
        0xFE,
        (
            "就是你们\x01",
            "救了叔父吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是非常感谢。\x01",
            "这么忙还劳烦你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，孤儿院事件的\x01",
            "调查工作也要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "做出那种事情的家伙，\x01",
            "我是绝对不会原谅他的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1821")

    label("loc_16B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A4")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "失火现场的整理\x01",
            "终于告一段落了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "到底是谁做出这种事情的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可恶，\x01",
            "我绝对不饶恕那些放火的犯人……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1821")

    label("loc_17A4")


    ChrTalk(
        0xFE,
        (
            "失火现场的整理\x01",
            "终于告一段落了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可恶，\x01",
            "我绝对不饶恕那些放火的犯人……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1821")

    Jump("loc_1D3A")

    label("loc_1824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1974")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1922")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "那个城市……\x01",
            "卢安变了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前卢安是以贸易\x01",
            "和渔业为中心的城镇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在渐渐被游客看作是\x01",
            "观光和休闲胜地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近听说那里\x01",
            "治安有点不太好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1971")

    label("loc_1922")


    ChrTalk(
        0xFE,
        (
            "最近听说卢安的\x01",
            "治安有点不太好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1971")

    Jump("loc_1D3A")

    label("loc_1974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1B1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A77")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "我也去过\x01",
            "玛西亚孤儿院。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有时候会和索雷诺那家伙\x01",
            "一起去帮忙干些体力活。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为那里只有\x01",
            "特蕾莎老师一个人在打理，\x01",
            "一个男的劳动力都没有。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1A")

    label("loc_1A77")


    ChrTalk(
        0xFE,
        (
            "我也去过\x01",
            "玛西亚孤儿院。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为那里只有\x01",
            "特蕾莎老师一个人在打理，\x01",
            "一个男的劳动力都没有。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B1A")

    Jump("loc_1D3A")

    label("loc_1B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_1B9C")

    ChrTalk(
        0xFE,
        "……男孩吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我一直在家，\x01",
            "没有看到你说的那个男孩。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D3A")

    label("loc_1B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1D3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C97")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "我曾经在卢安的港口工作过，\x01",
            "不过现在我\x01",
            "回到了自己的故乡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "果然还是在自己生长的\x01",
            "土地上生活比较安稳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "除了姐姐一直\x01",
            "在旁边啰里啰嗦的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D3A")

    label("loc_1C97")


    ChrTalk(
        0xFE,
        (
            "我曾经在卢安的港口工作过，\x01",
            "不过现在我\x01",
            "回到了自己的故乡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "果然还是在自己生长的\x01",
            "土地上生活比较安稳。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D3A")

    TalkEnd(0x14)
    Return()

    # Function_4_12BE end

    def Function_5_1D3E(): pass

    label("Function_5_1D3E")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1D8F")

    ChrTalk(
        0xFE,
        (
            "在这里也能听到\x01",
            "孩子们玩耍的声音。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是太好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24F5")

    label("loc_1D8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_1E21")

    ChrTalk(
        0xFE,
        (
            "犯人被逮捕了，\x01",
            "我也松了一口气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真不愧是游击士。\x01",
            "果然很靠得住啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24F5")

    label("loc_1E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_1FBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F11")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "玛西亚孤儿院的老师和孩子们\x01",
            "到底被什么人袭击了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果是同一伙犯人所为，\x01",
            "为什么他们还要加害那些孩子们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那些孩子们\x01",
            "什么坏事也没有做啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FBB")

    label("loc_1F11")


    ChrTalk(
        0xFE,
        (
            "如果是同一伙犯人所为，\x01",
            "为什么他们还要加害那些孩子们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那些孩子们\x01",
            "什么坏事也没有做啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FBB")

    Jump("loc_24F5")

    label("loc_1FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_20E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2074")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "孤儿院里只剩下\x01",
            "瓦砾和灰烬了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那天的火势\x01",
            "还真是强啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那里本来是一个能勾起老师和\x01",
            "孩子们许多回忆的地方……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E4")

    label("loc_2074")


    ChrTalk(
        0xFE,
        (
            "孤儿院里只剩下\x01",
            "瓦砾和灰烬了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那里本来是一个能勾起老师和\x01",
            "孩子们许多回忆的地方……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20E4")

    Jump("loc_24F5")

    label("loc_20E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2201")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2194")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "明天要和扎古一起\x01",
            "运送食物到孤儿院。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我考虑到孩子的数量，\x01",
            "所以准备了很多哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "现在必须要开始准备了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_21FE")

    label("loc_2194")


    ChrTalk(
        0xFE,
        (
            "明天要和扎古一起\x01",
            "运送食物到孤儿院。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "现在必须要开始准备了。\x02",
    )

    CloseMessageWindow()

    label("loc_21FE")

    Jump("loc_24F5")

    label("loc_2201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2360")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22EB")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "这个村的村民\x01",
            "也在帮助玛西亚孤儿院。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特蕾莎院长\x01",
            "真的是非常辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "扎古辞掉了工作\x01",
            "回到这里之后，\x01",
            "好像经常去那里帮忙呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_235D")

    label("loc_22EB")


    ChrTalk(
        0xFE,
        (
            "这个村的村民\x01",
            "也在帮助玛西亚孤儿院。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特蕾莎院长\x01",
            "真的是非常辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_235D")

    Jump("loc_24F5")

    label("loc_2360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_23A0")

    ChrTalk(
        0xFE,
        "戴着帽子的男孩子？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真抱歉，我没看到。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24F5")

    label("loc_23A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_24F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2487")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "啊呀，是旅行者吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果你们要找吃饭的地方，\x01",
            "我推荐你们去『白之木莲亭』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那里的饭菜味道很好，\x01",
            "价格也非常适中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "还有许多额外的赠品哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24F5")

    label("loc_2487")


    ChrTalk(
        0xFE,
        (
            "如果你们要找吃饭的地方，\x01",
            "我推荐你们去『白之木莲亭』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "『白之木莲亭』\x01",
            "就在这座房屋的旁边。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24F5")

    TalkEnd(0x15)
    Return()

    # Function_5_1D3E end

    def Function_6_24F9(): pass

    label("Function_6_24F9")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_25B1")

    ChrTalk(
        0xFE,
        (
            "真没想到戴尔蒙市长\x01",
            "竟然做出这么过分的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "简直不敢相信，\x01",
            "实在难以理解呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304F")

    label("loc_25B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_26AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2655")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "哦哦，是几位游击士啊。\x01",
            "听说你们抓到了犯人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要我们能帮得上忙，\x01",
            "请你们尽管开口。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26AC")

    label("loc_2655")


    ChrTalk(
        0xFE,
        "竟然做出这么过分的事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们到底\x01",
            "打算干什么啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26AC")

    Jump("loc_304F")

    label("loc_26AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_27C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2755")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "事情的经过\x01",
            "我已经听说了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一次还不够，\x01",
            "竟然又做出如此令人发指的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这真是令人\x01",
            "痛心不已啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27C4")

    label("loc_2755")


    ChrTalk(
        0xFE,
        (
            "一次还不够，\x01",
            "竟然又做出如此令人发指的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这真是令人\x01",
            "痛心不已啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27C4")

    Jump("loc_304F")

    label("loc_27C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_28E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2885")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "孤儿院的孩子们\x01",
            "好像渐渐恢复精神了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且也习惯了这里的生活，\x01",
            "最近都能够听得到他们的笑声了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28DE")

    label("loc_2885")


    ChrTalk(
        0xFE,
        (
            "孤儿院的孩子们\x01",
            "好像渐渐恢复精神了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28DE")

    Jump("loc_304F")

    label("loc_28E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B9")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "哎呀～『白之木莲亭』的雷克斯\x01",
            "主动向孤儿院提供房间，\x01",
            "真是帮了院长和孩子们大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这就是患难见真情啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们也会不惜一切\x01",
            "来帮助孤儿院的孩子们的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A2F")

    label("loc_29B9")


    ChrTalk(
        0xFE,
        "这就是患难见真情啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们也会不惜一切\x01",
            "来帮助孤儿院的孩子们的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A2F")

    Jump("loc_304F")

    label("loc_2A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_2C43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B70")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "昨天晚上，\x01",
            "可以在这里看到东边的天空\x01",
            "有红色的火光和冲天的黑烟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我马上叫\x01",
            "村里的年轻人都赶去了，\x01",
            "但还是没有免除全部烧毁的命运……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之，\x01",
            "孤儿院的老师和孩子们都没有受伤，\x01",
            "这已经是不幸中的万幸了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C40")

    label("loc_2B70")


    ChrTalk(
        0xFE,
        (
            "昨天晚上，\x01",
            "可以在这里看到东边的天空\x01",
            "有红色的火光和冲天的黑烟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我马上叫\x01",
            "村里的年轻人都赶去了，\x01",
            "但还是没有免除全部烧毁的命运……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C40")

    Jump("loc_304F")

    label("loc_2C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2DD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D2F")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "通往卢安的\x01",
            "梅威海道被称为\x01",
            "『风与海的道路』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那条街道的景色非常美丽，\x01",
            "经常有舒服的海风吹过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我把去那里散步\x01",
            "作为我的每日必行之事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DCE")

    label("loc_2D2F")


    ChrTalk(
        0xFE,
        (
            "通往卢安的\x01",
            "梅威海道被称为\x01",
            "『风与海的道路』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那条街道的景色非常美丽，\x01",
            "经常有舒服的海风吹过。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DCE")

    Jump("loc_304F")

    label("loc_2DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2E8B")

    ChrTalk(
        0xFE,
        (
            "特蕾莎老师有时候\x01",
            "会带着孤儿院的孩子们\x01",
            "来玛诺利亚村玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大家都相处得非常好，\x01",
            "就像亲兄弟姐妹一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304F")

    label("loc_2E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_2EC4")

    ChrTalk(
        0xFE,
        "男孩子吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "他没有到这里来过哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_304F")

    label("loc_2EC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_304F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC6")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "哦，是旅行者啊。\x01",
            "欢迎来到玛诺利亚村。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前，这个村子是\x01",
            "作为『驿站之村』而繁荣起来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，自从定期船开航以来，\x01",
            "这里过往的行人就明显减少了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在只能勉勉强强\x01",
            "以『花之村』闻名了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304F")

    label("loc_2FC6")


    ChrTalk(
        0xFE,
        (
            "自从定期船开航以来，\x01",
            "这里过往的行人就明显减少了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在只能勉勉强强\x01",
            "以『花之村』闻名了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_304F")

    TalkEnd(0x16)
    Return()

    # Function_6_24F9 end

    def Function_7_3053(): pass

    label("Function_7_3053")

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

    # Function_7_3053 end

    def Function_8_30AE(): pass

    label("Function_8_30AE")

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
        "#000F那么，Let’s go！\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_8_30AE end

    SaveToFile()

Try(main)
