from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4203   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4203.x',
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
        '士兵丹',                               # 9
        '士兵阿尔兹',                           # 10
        '杜南公爵',                             # 11
        '管家菲利普',                           # 12
        '特务兵',                               # 13
        '特务兵',                               # 14
        '卡露娜',                               # 15
        '亚妮拉丝',                             # 16
        '库拉茨',                               # 17
        '克鲁茨',                               # 18
        '尤莉亚中尉',                           # 19
        '亲卫队员',                             # 20
        '亲卫队员',                             # 21
        '亲卫队员',                             # 22
        '亲卫队员',                             # 23
        '亲卫队员',                             # 24
        '亲卫队员',                             # 25
        '亲卫队员',                             # 26
        '亲卫队员',                             # 27
        '卡西乌斯',                             # 28
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
        'ED6_DT07/CH01300 ._CH',             # 00
        'ED6_DT07/CH02140 ._CH',             # 01
        'ED6_DT07/CH02470 ._CH',             # 02
        'ED6_DT07/CH01330 ._CH',             # 03
        'ED6_DT07/CH00401 ._CH',             # 04
        'ED6_DT07/CH00421 ._CH',             # 05
        'ED6_DT07/CH00391 ._CH',             # 06
        'ED6_DT07/CH00411 ._CH',             # 07
        'ED6_DT07/CH02090 ._CH',             # 08
        'ED6_DT07/CH00321 ._CH',             # 09
        'ED6_DT07/CH02000 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01300P._CP',             # 00
        'ED6_DT07/CH02140P._CP',             # 01
        'ED6_DT07/CH02470P._CP',             # 02
        'ED6_DT07/CH01330P._CP',             # 03
        'ED6_DT07/CH00401P._CP',             # 04
        'ED6_DT07/CH00421P._CP',             # 05
        'ED6_DT07/CH00391P._CP',             # 06
        'ED6_DT07/CH00411P._CP',             # 07
        'ED6_DT07/CH02090P._CP',             # 08
        'ED6_DT07/CH00321P._CP',             # 09
        'ED6_DT07/CH02000P._CP',             # 0A
    )

    DeclNpc(
        X                   = -790,
        Z                   = 0,
        Y                   = 41980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 950,
        Z                   = 0,
        Y                   = 41980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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


    DeclEvent(
        X                   = -5630,
        Y                   = -1000,
        Z                   = 30090,
        Range               = 6050,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x69BE,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )


    ScpFunction(
        "Function_0_3A2",          # 00, 0
        "Function_1_494",          # 01, 1
        "Function_2_4B3",          # 02, 2
        "Function_3_525",          # 03, 3
        "Function_4_598",          # 04, 4
        "Function_5_F29",          # 05, 5
        "Function_6_1710",         # 06, 6
        "Function_7_2F90",         # 07, 7
        "Function_8_3D16",         # 08, 8
        "Function_9_41AE",         # 09, 9
        "Function_10_4265",        # 0A, 10
        "Function_11_5382",        # 0B, 11
    )


    def Function_0_3A2(): pass

    label("Function_0_3A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_3B0")
    OP_A3(0x3FA)
    Event(0, 8)

    label("loc_3B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_3BE")
    OP_A3(0x3FB)
    Event(0, 9)

    label("loc_3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_3CC")
    OP_A3(0x3FC)
    Event(0, 10)

    label("loc_3CC")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_3DC"),
        (101, "loc_3DC"),
        (SWITCH_DEFAULT, "loc_3F2"),
    )


    label("loc_3DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EF")
    OP_A2(0x60B)
    Event(0, 6)

    label("loc_3EF")

    Jump("loc_3F2")

    label("loc_3F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3FC")
    Jump("loc_493")

    label("loc_3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_43C")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, -790, 0, 41980, 180)
    SetChrPos(0xD, 950, 0, 41980, 180)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_493")

    label("loc_43C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_446")
    Jump("loc_493")

    label("loc_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_450")
    Jump("loc_493")

    label("loc_450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_45A")
    Jump("loc_493")

    label("loc_45A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_464")
    Jump("loc_493")

    label("loc_464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_46E")
    Jump("loc_493")

    label("loc_46E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_478")
    Jump("loc_493")

    label("loc_478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_482")
    Jump("loc_493")

    label("loc_482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_48C")
    Jump("loc_493")

    label("loc_48C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_493")

    label("loc_493")

    Return()

    # Function_0_3A2 end

    def Function_1_494(): pass

    label("Function_1_494")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE4A80, 0x30060)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 450)
    Return()

    # Function_1_494 end

    def Function_2_4B3(): pass

    label("Function_2_4B3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "格兰赛尔城完全封锁。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "上面下了命令，\x01",
            "无论是谁也不能通行。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_2_4B3 end

    def Function_3_525(): pass

    label("Function_3_525")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "你们是在武术大会\x01",
            "取得优胜的游击士吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "晚宴已经结束了。\x01",
            "快回游击士协会去吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_525 end

    def Function_4_598(): pass

    label("Function_4_598")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_75E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_649")

    ChrTalk(
        0xFE,
        (
            "尤莉亚中尉是恐怖分子的说法\x01",
            "让我难以置信……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而理查德上校\x01",
            "是政变的主谋这一点\x01",
            "同样让我难以置信……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75B")

    label("loc_649")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "尤莉亚中尉是恐怖分子的说法\x01",
            "让我难以置信……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而理查德上校\x01",
            "是政变的主谋这一点\x01",
            "同样让我难以置信……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么优秀的一个人，\x01",
            "怎么会做出这种事来啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75B")

    Jump("loc_F25")

    label("loc_75E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_768")
    Jump("loc_F25")

    label("loc_768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_7A6")

    ChrTalk(
        0xFE,
        (
            "哟，\x01",
            "在王城里面好好参观了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F25")

    label("loc_7A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_821")

    ChrTalk(
        0xFE,
        (
            "欢迎来到\x01",
            "女王陛下的格兰赛尔城！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们从这里进去，\x01",
            "就会有接待人员前来迎接。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F25")

    label("loc_821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_8D2")

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "不知道尤莉亚中尉现在怎么样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "每天向中尉打招呼\x01",
            "可是我日常工作当中的一大乐趣啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F25")

    label("loc_8D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_A35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_972")

    ChrTalk(
        0xFE,
        (
            "从今天开始\x01",
            "全城的警戒都加强了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这项工作似乎是由\x01",
            "上校的副官凯诺娜上尉负责的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A32")

    label("loc_972")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "从今天开始\x01",
            "全城的警戒都加强了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这项工作似乎是由\x01",
            "上校的副官凯诺娜上尉负责的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "理查德上校果然相当忙呢。\x02",
    )

    CloseMessageWindow()

    label("loc_A32")

    Jump("loc_F25")

    label("loc_A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_AD3")

    ChrTalk(
        0xFE,
        (
            "特务部队的那群人\x01",
            "在大会中连续获胜啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "比起去参加比赛，\x01",
            "我倒希望他们\x01",
            "快点去搜捕亲卫队的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F25")

    label("loc_AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_C81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B9F")

    ChrTalk(
        0xFE,
        (
            "女王陛下生病后，\x01",
            "就几乎很少能在城外\x01",
            "看见理查德上校。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "情报部的本部好像转移到了王城内。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7E")

    label("loc_B9F")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "理查德上校\x01",
            "好像非常忙碌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "女王陛下生病后，\x01",
            "几乎很少能在城外看见他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "情报部的本部好像转移到了王城内。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7E")

    Jump("loc_F25")

    label("loc_C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_D58")

    ChrTalk(
        0xFE,
        (
            "说起理查德上校，\x01",
            "我当然是很尊敬他啦。\x01",
            "可是那些情报部的黑衣家伙们啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我承认他们有实力，\x01",
            "可他们给人的感觉很不舒服，\x01",
            "在军队里面关于他们的流言也不少。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F25")

    label("loc_D58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_E0C")

    ChrTalk(
        0xFE,
        (
            "理查德上校\x01",
            "的确是个优秀的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为在王国军中颇具人气，\x01",
            "有许多人都慕名\x01",
            "转到情报部去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F25")

    label("loc_E0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_F25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_EC9")

    ChrTalk(
        0xFE,
        (
            "虽然不能进城参观，\x01",
            "也不要这么灰心丧气嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "格兰赛尔的大街上\x01",
            "还有很多观光胜地呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F25")

    label("loc_EC9")


    ChrTalk(
        0xFE,
        "请你们站住。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很抱歉，\x01",
            "王城现在禁止无关人等进入。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F25")

    TalkEnd(0xFE)
    Return()

    # Function_4_598 end

    def Function_5_F29(): pass

    label("Function_5_F29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1010")

    ChrTalk(
        0xFE,
        (
            "这次政变竟然是由\x01",
            "城内的情报部发起的，\x01",
            "的确让我感到震惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过庆典总算能够平安无事地进行，\x01",
            "真的是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_170C")

    label("loc_1010")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_101A")
    Jump("loc_170C")

    label("loc_101A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_10A3")

    ChrTalk(
        0xFE,
        (
            "你们好啊，\x01",
            "晚宴怎么样啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "宫廷料理什么的，\x01",
            "我只在执行警卫时见过，\x01",
            "从来都没机会品尝过呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_170C")

    label("loc_10A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_10C6")

    ChrTalk(
        0xFE,
        "那么，祝各位晚上玩得愉快。\x02",
    )

    CloseMessageWindow()
    Jump("loc_170C")

    label("loc_10C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1136")

    ChrTalk(
        0xFE,
        (
            "刚才，\x01",
            "宫廷料理的材料都已经运到城内来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大概那就是\x01",
            "用来烹制今晚晚宴的食材吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_170C")

    label("loc_1136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1213")

    ChrTalk(
        0xFE,
        (
            "从今晚开始\x01",
            "必须要在市内巡逻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为恐怖分子还未抓到，\x01",
            "要严加防范才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_170C")

    label("loc_1213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1297")

    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "关于女王陛下病情的详细情况，\x01",
            "我们也不太了解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "的确感觉有些不安呢，\x01",
            "也不知道到底会怎么样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_170C")

    label("loc_1297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1309")

    ChrTalk(
        0xFE,
        (
            "大会正式赛第一回合\x01",
            "好像已经结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "代表王国警备队出场的\x01",
            "那些人怎么样了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_170C")

    label("loc_1309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_14A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_13C1")

    ChrTalk(
        0xFE,
        (
            "杜南公爵\x01",
            "就算在王城里也很招人讨厌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "要是理查德上校不在的话，\x01",
            "不知道会变成什么样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A4")

    label("loc_13C1")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "杜南公爵\x01",
            "就算在王城里也很招人讨厌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为无论是谁，\x01",
            "都只看到过他在吃、睡、玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "要是理查德上校不在的话，\x01",
            "不知道会变成什么样子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A4")

    Jump("loc_170C")

    label("loc_14A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_168B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_158B")

    ChrTalk(
        0xFE,
        (
            "因为今年的武术大会是团体战，\x01",
            "比赛场次比以往减少了一些呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正式赛和预选赛不一样，\x01",
            "是在下午进行的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1688")

    label("loc_158B")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "武术大会的预选赛\x01",
            "好像已经结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今年因为是团体战，\x01",
            "比赛场次比以往减少了一些呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正式赛和预选赛不一样，\x01",
            "是在下午进行的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1688")

    Jump("loc_170C")

    label("loc_168B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_170C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_16D7")

    ChrTalk(
        0xFE,
        (
            "好不容易来一次王都，\x01",
            "就请舒舒服服地享受观光的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_170C")

    label("loc_16D7")


    ChrTalk(
        0xFE,
        "现在不能进城参观。\x02",
    )

    CloseMessageWindow()

    label("loc_170C")

    TalkEnd(0xFE)
    Return()

    # Function_5_F29 end

    def Function_6_1710(): pass

    label("Function_6_1710")

    EventBegin(0x0)
    OP_6C(30000, 0)

    def lambda_1721():
        OP_6D(-930, 750, 44710, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1721)

    def lambda_1739():
        OP_67(0, 4250, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1739)

    def lambda_1751():
        OP_6B(11000, 10000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1751)

    def lambda_1761():
        OP_6C(0, 15000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1761)
    Sleep(12000)
    SetChrPos(0x101, -910, 0, 8880, 0)
    SetChrPos(0x102, 2029, 0, 10110, 0)

    def lambda_1798():
        OP_6D(-290, 0, 32350, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1798)

    def lambda_17B0():
        OP_6B(7180, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17B0)

    def lambda_17C0():
        OP_6E(262, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_17C0)

    def lambda_17D0():
        OP_8E(0xFE, 0xFFFFFD62, 0x0, 0x4808, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17D0)

    def lambda_17EB():
        OP_8E(0xFE, 0x51E, 0x0, 0x4808, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17EB)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x101,
        (
            "#000F哇～……\x01",
            "这就是格兰赛尔城啊。\x02\x03",
            "女王住的地方，\x01",
            "果然又气派又漂亮呢……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        (
            "#010F嗯……\x01",
            "不过看起来不仅是漂亮，\x01",
            "也十分地坚固呢。\x02\x03",
            "那个巨大的城门就是很好的例子了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F确实，\x01",
            "不可能那么简单就能进得去。\x02\x03",
            "总之，\x01",
            "只能先向那边的士兵们打听一下了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们先暗中调查一下吧。\x02\x03",
            "……就像刚从乡下来，\x01",
            "想进王城参观那样。\x02\x03",
            "想借此机会拜见女王，\x01",
            "哪怕看一眼也好。\x02\x03",
            "——这种设定不错吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F还是老样子，摆出一幅若无其事的表情，\x01",
            "立刻就能说出想法来。\x02\x03",
            "真是让人感叹啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F这句话我就当成是夸奖收下了。\x02",
    )

    CloseMessageWindow()

    def lambda_1B41():
        OP_6D(0, 250, 42590, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B41)
    OP_6B(5100, 4000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    SetChrPos(0x101, -850, 0, 25330, 0)
    SetChrPos(0x102, 1090, 0, 22700, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#000F喂～你们好～\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_1BC8():

        label("loc_1BC8")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1BC8")

    QueueWorkItem2(0x8, 1, lambda_1BC8)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_1BF0():

        label("loc_1BF0")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1BF0")

    QueueWorkItem2(0x9, 1, lambda_1BF0)

    def lambda_1C01():
        OP_8E(0xFE, 0xFFFFFCAE, 0x0, 0x9290, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C01)

    def lambda_1C1C():
        OP_8E(0xFE, 0x316, 0x0, 0x9290, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C1C)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x8,
        "哦，你们好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "欢迎来到格兰赛尔城。\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们是刚从洛连特\x01",
            "来到王都参观的。\x02\x03",
            "借此机会，\x01",
            "想进城里面参观一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "啊，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "很抱歉，\x01",
            "格兰赛尔城是无关人员禁止入内的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "由于恐怖分子骚乱，\x01",
            "检查更为严格了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不过，抓到了恐怖分子之后，\x01",
            "应该就允许参观了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是这样啊……真可惜。\x02\x03",
            "唉，难道想见女王陛下一面的梦想\x01",
            "还是没办法实现吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "对了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "诞辰庆典那天，\x01",
            "女王会照例在城的阳台上对市民致意，\x01",
            "应该会有见面的机会的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不过最近，\x01",
            "陛下的身体状况不是很好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "例行的致意还会不会有呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那个……\x01",
            "女王陛下生病了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "是啊……\x01",
            "大概是因为操劳过度……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "而且，因为自己十分信赖的亲卫队\x01",
            "被当成恐怖事件嫌疑犯这件事，\x01",
            "也受了相当大的打击吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "最近都没有出现在会见室，\x01",
            "应该是在女王宫静养吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F是这样吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "真是的，亲卫队那些家伙们，\x01",
            "对陛下的信赖反倒恩将仇报……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "平常我就不喜欢\x01",
            "这些所谓的精英们。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)
    OP_44(0x8, 0xFF)
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        (
            "可、可是，\x01",
            "尤莉亚中尉平时不是很亲切的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "对我们这些普通的士兵，\x01",
            "也亲自教剑术和行事方法……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "说她是恐怖分子，\x01",
            "我有点不太相信呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 800)

    ChrTalk(
        0x8,
        "这、这是肯定的啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "大概，她是因为部下的胡作非为\x01",
            "而感到责任重大，所以才失踪了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是啊……\x01",
            "尤莉亚小姐真是可怜啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    ChrTalk(
        0x101,
        (
            "#000F（看起来，这些人……）\x02\x03",
            "（只是因为尤莉亚小姐的关系，\x01",
            "在嫉妒其他的队员呢……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（嗯，好像是这样呢……）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "咳咳……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "总之，就是这个原因，\x01",
            "格兰赛尔城禁止入内。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(
        0x9,
        "抱歉，请回去吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F唉，这样的话，\x01",
            "也只好放弃了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不过，稍微有点担心呢。\x02\x03",
            "女王陛下的健康且不必说，\x01",
            "政务方面不要紧吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "是啊……\x01",
            "这个担心很有道理呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "虽然这样，\x01",
            "还是有名义上的代理人的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F名义上的代理人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "哈哈。\x01",
            "顾名思义，只是『名义上的』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那一位大人和政务\x01",
            "还真是八竿子打不着啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        "喂喂，说话要小心啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不过确实，\x01",
            "我也觉得公主更为适合呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x8,
        "看，你不也是这样想的……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, -370, 750, 48420, 180)
    SetChrPos(0xB, 550, 750, 49230, 180)

    def lambda_2677():
        OP_67(0, 9500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2677)

    def lambda_268F():
        OP_6B(3800, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_268F)

    def lambda_269F():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_269F)
    Sleep(100)

    def lambda_26B4():
        OP_8F(0xFE, 0xFFFFF6F0, 0x0, 0xA406, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_26B4)

    def lambda_26CF():
        OP_8F(0xFE, 0x802, 0x0, 0xA4A6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_26CF)
    OP_6D(-10, 750, 48050, 3000)

    def lambda_26FB():

        label("loc_26FB")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_26FB")

    QueueWorkItem2(0x101, 1, lambda_26FB)

    def lambda_270C():

        label("loc_270C")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_270C")

    QueueWorkItem2(0x102, 1, lambda_270C)

    def lambda_271D():

        label("loc_271D")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_271D")

    QueueWorkItem2(0x9, 1, lambda_271D)

    def lambda_272E():

        label("loc_272E")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_272E")

    QueueWorkItem2(0x8, 1, lambda_272E)
    SetChrPos(0x101, -2130, 0, 39490, 0)
    SetChrPos(0x102, -2130, 0, 37840, 0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x78)
    Sleep(1000)
    Sleep(1000)

    def lambda_2779():
        OP_8E(0xFE, 0xFFFFFE98, 0x2EE, 0xAE2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2779)
    Sleep(500)

    def lambda_2799():
        OP_8E(0xFE, 0x276, 0x2EE, 0xAF78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2799)
    OP_6D(0, 750, 44920, 2000)
    WaitChrThread(0xA, 0x1)
    TurnDirection(0xA, 0xB, 400)

    ChrTalk(
        0xA,
        (
            "#220F哼，这叫什么事啊！\x02\x03",
            "现在预选赛\x01",
            "不是已经开始了吗！\x02\x03",
            "菲利普！\x01",
            "都是因为你没有叫我！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(
        0xB,
        (
            "#720F实在是抱歉，阁下。\x02\x03",
            "不过，这也是因为\x01",
            "阁下不注意生活规律啊……\x02\x03",
            "这几天连续大摆宴席，\x01",
            "又是吃又是唱的大闹……\x02\x03",
            "啤酒和油炸食品\x01",
            "放在一起大量地吃，\x01",
            "还彻夜看漫画杂志一直到早上……\x02\x03",
            "总是这样，\x01",
            "睡过头也是理所当然的了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#220F闭嘴，菲利普！\x01",
            "你的这些话我已经听够了！\x02\x03",
            "作为继任国王的我，\x01",
            "有权力想干什么就干什么！\x02\x03",
            "哎呀，时间紧迫！\x01",
            "赶快赶去王立竞技场！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A9C():
        OP_8E(0xFE, 0xFFFFFEF2, 0x0, 0x6D74, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2A9C)
    Sleep(500)

    def lambda_2ABC():
        OP_8E(0xFE, 0x42E, 0x0, 0x6BF8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2ABC)
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_6D(-30, 0, 40870, 5000)

    def lambda_2B16():
        OP_8F(0xFE, 0xFFFFFCEA, 0x0, 0xA3FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2B16)

    def lambda_2B31():
        OP_8F(0xFE, 0x3B6, 0x0, 0xA3FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2B31)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x101,
        "#000F……哎…………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 0)
    OP_8E(0x102, 0xFFFFFD9E, 0x0, 0x95B0, 0x7D0, 0x0)
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x102,
        "#010F……我说，难道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "……我知道，不用再说了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "刚才那位就是陛下的代理人，\x01",
            "现在主理政务的公爵阁下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F我……\x01",
            "我的头开始疼了……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)
    OP_44(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x9,
        (
            "总、总之不用担心，\x01",
            "有个可靠的人在辅佐，所以没问题的啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "多亏了那个人，\x01",
            "至今还没出什么大乱子。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    def lambda_2CFE():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CFE)
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x102,
        "#010F可靠的辅佐人……吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "嘿嘿，就是王国军情报部\x01",
            "一个叫『理查德上校』的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "可以说，他代替放荡的公爵阁下，\x01",
            "一手处理政务呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(
        0x101,
        "#000F（果、果然……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（比预想的还要更加深入地\x01",
            "控制了国家的核心呢……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过，虽然不能进城参观，\x01",
            "也不要这么灰心丧气嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "格兰赛尔的大街上\x01",
            " \x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(
        0x9,
        (
            "好不容易来一次王都，\x01",
            "就请舒舒服服地享受观光的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，说的也是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F感谢你们的好意。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_1710 end

    def Function_7_2F90(): pass

    label("Function_7_2F90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F9D")
    Return()

    label("loc_2F9D")

    EventBegin(0x0)

    def lambda_2FA5():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FA5)

    def lambda_2FB3():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2FB3)
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(
        0x108,
        (
            "#070F哦，现在就进城去吗？\x02\x03",
            "晚宴结束之后\x01",
            "要在城里的客房过夜，\x01",
            "明天才能回到街上来哦。\x02",
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
            "进入格兰赛尔城\x01",      # 0
            "等一会儿再来\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_30E0"),
        (1, "loc_31AE"),
        (SWITCH_DEFAULT, "loc_31E2"),
    )


    label("loc_30E0")


    ChrTalk(
        0x108,
        (
            "#070F那么就把请帖\x01",
            "给那边的门卫看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯～\x01",
            "总觉得很紧张呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F没错，像这样被招待\x01",
            "这种体验还真是难得呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31E2")

    label("loc_31AE")


    ChrTalk(
        0x108,
        "#070F知道了，一会儿再来吧。\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    label("loc_31E2")


    def lambda_31E8():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31E8)

    def lambda_31F6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_31F6)

    def lambda_3204():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3204)

    def lambda_3212():
        OP_67(0, 5220, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3212)

    def lambda_322A():
        OP_6E(287, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_322A)
    OP_6D(880, 500, 43300, 3000)
    SetChrPos(0x101, -620, 0, 32729, 0)
    SetChrPos(0x102, 920, 0, 32590, 0)
    SetChrPos(0x108, 90, 0, 34050, 0)

    def lambda_327E():
        OP_8E(0xFE, 0xFFFFFCFE, 0x0, 0x9B82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_327E)
    Sleep(300)

    def lambda_329E():
        OP_8E(0xFE, 0x4E2, 0x0, 0x9BD2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_329E)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "这里是女王陛下\x01",
            "居住的格兰赛尔城。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "如果没有事情的话，\x01",
            "就请离开这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "哎。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        "#000F晚上好～\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        "#010F那天麻烦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "怎么，原来是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "你们还呆在王都吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯。\x01",
            "稍微有点事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F今天是因为受到正式的邀请\x01",
            "才来这里的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        "正式的……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "邀请……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F……是公爵亲自\x01",
            "给我们的请帖。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x108, 0x168, 0x0, 0x9862, 0xBB8, 0x0)

    ChrTalk(
        0x8,
        "哇！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "巨、巨人！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F给，这就是请帖。\x02",
    )

    CloseMessageWindow()
    OP_8F(0x108, 0x21C, 0x0, 0xA1D6, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "金把晚宴请帖\x01",
            "递给了士兵们。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0x108, 0x168, 0x0, 0x9862, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        "嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "金·瓦赛克等４人\x01",
            "在武术大会获得优胜，\x01",
            "特此邀请参加晚宴……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "是这样吗……\x01",
            "你们是武术大会的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我记得，获得优胜的是\x01",
            "来自东方的武术家\x01",
            "所率领的小组……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "难道，你们就是\x01",
            "那个小组的人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嘿嘿，你说对了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们只不过是\x01",
            "帮了点微不足道的忙而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "原来如此，是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……你们的事情\x01",
            "我从女官长那里听说了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不过，好像少一个人啊。\x01",
            "那一位怎么没有来呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F因为有点私事，\x01",
            "所以没办法来参加了。\x02\x03",
            "出席的只有我们而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "是吗，那真是遗憾啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "算了……\x01",
            "现在就让你们进城吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3896():
        OP_6D(70, 750, 44190, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3896)

    def lambda_38AE():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_38AE)

    def lambda_38BE():
        OP_6E(438, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_38BE)
    OP_8E(0x9, 0x46, 0x2EE, 0xB19E, 0x7D0, 0x0)
    WaitChrThread(0x102, 0x2)

    ChrTalk(
        0x9,
        (
            "武术大会的优胜者，\x01",
            "金选手等３个人前来光临！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "开门！\x02",
    )

    CloseMessageWindow()

    def lambda_3949():
        OP_6D(70, 3450, 44190, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3949)

    def lambda_3961():
        OP_67(0, 2270, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3961)

    def lambda_3979():
        OP_8E(0x8, 0xFFFFF8D0, 0x2EE, 0xB004, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3979)
    OP_8E(0x9, 0x7A8, 0x2EE, 0xAFC8, 0x7D0, 0x0)
    OP_8C(0x9, 180, 400)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 180, 400)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x78)

    ChrTalk(
        0x101,
        (
            "#000F哇啊……\x02\x03",
            "和哈肯门一样，\x01",
            "这个城门真有魄力啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F而且，只有王城才能\x01",
            "建造得如此坚固呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "这是不可能被攻陷的城呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "建国以来，虽然亚宁堡\x01",
            "没有被外敌突破过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "因为贵族的叛乱，\x01",
            "王都数次被卷入战火之中呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那个时候，这座王城\x01",
            "击退了反叛军的进攻，\x01",
            "保护了王家和避难的人民……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "有很多这种故事流传下来呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎～有这样的事啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F嗯，有悠久历史的国家\x01",
            "总会有古代浪漫的传说呢。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x8,
        (
            "好了，请进吧！\x01",
            "欢迎来到女王陛下的格兰赛尔城！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "从这里进去\x01",
            "就会有接待人员前来迎接。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "那么，祝各位晚上玩得愉快。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x638)
    EventEnd(0x0)
    Return()

    # Function_7_2F90 end

    def Function_8_3D16(): pass

    label("Function_8_3D16")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_6D(70, -1900, 45200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(357, 0)
    SetChrPos(0xC, -790, 0, 41980, 180)
    SetChrPos(0xD, 950, 0, 41980, 180)
    Sleep(500)

    def lambda_3DA5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3DA5)

    def lambda_3DB3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3DB3)
    OP_6D(70, 2550, 45150, 2000)

    ChrTalk(
        0xC,
        "怎、怎么回事……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "奇怪了啊……\x01",
            "不是说已经完全封闭了吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_3E60():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3E60)

    def lambda_3E6E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3E6E)
    OP_6D(70, -1900, 45200, 1000)

    ChrTalk(
        0xC,
        "什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "怎么会！！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-1030, 0, 9000, 0)
    OP_67(0, 9340, -13360, 0)
    OP_6B(1000, 0)
    OP_6C(135000, 0)
    OP_6E(747, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x12, 1730, 0, -280, 0)
    SetChrPos(0x13, 1730, 0, -2790, 180)
    SetChrPos(0x14, 1730, 0, -5480, 180)
    SetChrPos(0x15, 1730, 0, -8070, 180)
    SetChrPos(0x16, 1730, 0, -10050, 180)
    SetChrPos(0xF, 3230, 0, -4350, 0)
    SetChrPos(0x10, 3230, 0, -1480, 0)
    SetChrPos(0x17, -1770, 0, -380, 260)
    SetChrPos(0x18, -1770, 0, -2970, 180)
    SetChrPos(0x19, -1770, 0, -5140, 180)
    SetChrPos(0x1A, -1770, 0, -7650, 180)
    SetChrPos(0xE, -3240, 0, -1470, 360)
    SetChrPos(0x11, -3240, 0, -4130, 360)

    def lambda_4010():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4010)

    def lambda_402B():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_402B)

    def lambda_4046():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4046)

    def lambda_4061():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4061)

    def lambda_407C():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_407C)

    def lambda_4097():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4097)

    def lambda_40B2():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_40B2)

    def lambda_40CD():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_40CD)

    def lambda_40E8():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_40E8)

    def lambda_4103():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4103)

    def lambda_411E():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_411E)

    def lambda_4139():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4139)

    def lambda_4154():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4154)

    def lambda_416F():
        OP_6D(-390, 0, 29050, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_416F)

    def lambda_4187():
        OP_6C(44000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4187)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_3D16 end

    def Function_9_41AE(): pass

    label("Function_9_41AE")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(0, 4000, 27740, 0)
    OP_67(0, 3170, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(12000, 0)
    OP_6E(568, 0)
    OP_6D(0, 1000, 27740, 4000)
    Sleep(1000)

    def lambda_4226():
        OP_6D(-310, 5670, 42340, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4226)

    def lambda_423E():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_423E)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_41AE end

    def Function_10_4265(): pass

    label("Function_10_4265")

    EventBegin(0x0)
    SetChrPos(0x1B, 2600, 0, -3950, 0)
    SetChrPos(0x101, 3420, 0, -2610, 357)
    SetChrPos(0x102, 4150, 0, -4140, 0)
    ClearChrFlags(0x1B, 0x80)
    SetMapFlags(0x1)
    OP_69(0x101, 0x0)
    OP_6A(0x101)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315, 0)
    OP_6E(262, 0)

    def lambda_42E0():
        OP_6C(45000, 20000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_42E0)

    def lambda_42F0():
        OP_91(0xFE, 0xFFFFF272, 0x0, 0xA1D6, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42F0)

    def lambda_430B():
        OP_90(0xFE, 0xFFFFF272, 0x0, 0xA1D6, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_430B)

    def lambda_4326():
        OP_90(0xFE, 0xFFFFF272, 0x0, 0xA1D6, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_4326)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#000F老爸也真是的……\x02\x03",
            "生日庆典、还有王都观光，\x01",
            "如果能一起就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#080F不好意思，必须赶快召开军事会议了。\x02\x03",
            "虽然理查德被逮捕了，\x01",
            "逃亡中的特种兵还有很多。\x02\x03",
            "凯诺娜上尉也不知道什么时候\x01",
            "从那个地下遗迹中失踪了。\x02\x03",
            "而且，参加大会的空贼团\x01",
            "也趁混乱的时候逃走了。\x02\x03",
            "为了在生日庆典中不发生骚动，\x01",
            "必须加强警卫工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F真是的……\x01",
            " \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不过，我觉得在这种情况下\x01",
            "也不会再引起什么骚动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#080F总之，警卫方面可以放心。\x02\x03",
            "问题是，在那个地下遗迹里发生的事情，\x01",
            "到底有什么含义呢。\x02\x03",
            "理查德解开的那个封印，\x01",
            "到底会产生什么样的影响……\x02\x03",
            "『辉之环』是什么……\x02\x03",
            "这些事情必须要弄清楚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯……确实是这样。\x02\x03",
            "而且，理查德上校的\x01",
            "记忆好像也很奇怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#080F嗯，和克鲁茨一样，\x01",
            "有些事情想不起来。\x02\x03",
            "尽管如此，在讯问中\x01",
            "还是弄清楚了一件事。\x02\x03",
            "就是那个黑色导力器的来历。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_481C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_481C)

    ChrTalk(
        0x101,
        "#000F哎……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F查到制造它的人了吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#080F不……\x01",
            "知道把它带到情报部的人了。\x02\x03",
            "是情报部特务部队队长，\x01",
            "洛伦斯·博格少尉。\x02",
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
        "#010F是、是那个人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#080F在被选拔进情报部的时候，\x01",
            "他把那个东西给了理查德。\x02\x03",
            "而且，理查德\x01",
            "开始计划武装政变\x01",
            "大概也是那个时候。\x02\x03",
            "总之，有必要调查清楚\x01",
            "那个洛伦斯少尉的真实身份。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4A15():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4A15)

    ChrTalk(
        0x101,
        (
            "#000F是吗……\x01",
            "虽然不知道具体怎么回事……\x02\x03",
            "不过，只有我们见过他的真面目，\x01",
            "真是幸运啊。\x02\x03",
            "如果可以的话，\x01",
            "我可以画一张肖像画哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#080F啊，那么到时候就拜托了。\x02\x03",
            "虽然，对你的绘画水平\x01",
            "没抱什么希望……\x02\x03",
            "还是去拜托雪拉扎德\x01",
            "或者陛下她们比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1B, 400)

    ChrTalk(
        0x101,
        "#000F呜，这是什么意思！\x02",
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    def lambda_4BB0():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4BB0)
    ClearMapFlags(0x1)
    OP_69(0x101, 0x3E8)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔……\x02\x03",
            "洛伦斯少尉的脸，你看见过了？\x02",
        )
    )

    Sleep(500)
    OP_44(0x101, 0xFF)
    TurnDirection(0x101, 0x102, 400)
    OP_44(0x1B, 0xFF)
    TurnDirection(0x1B, 0x102, 400)
    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哎，我没告诉过你吗？\x02\x03",
            "在他逃跑前看到了一眼，\x01",
            "他把头盔摘掉了。\x02\x03",
            "是个银灰色头发的美男子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F不过女王也说了，\x01",
            "他的眼神非常的狂放。\x02\x03",
            "该怎么说呢……非常冷漠，\x01",
            "却又很炽热……\x02\x03",
            "『您没有怜悯我的资格』\x01",
            "他是这样对女王说的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F没有怜悯的资格……\x02\x03",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F约修亚……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#080F唉，你从以前开始\x01",
            "就经常考虑得太多。\x02\x03",
            "事情的善后处理就交给我们，\x01",
            "你们还是尽情享受生日庆典吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1B, 400)

    ChrTalk(
        0x102,
        (
            "#010F啊……\x02\x03",
            "嗯，说的也是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是啊是啊。\x01",
            "我们一定要玩个痛快。\x02\x03",
            "对了，今天晚上\x01",
            "要在城里住吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x101, 400)

    ChrTalk(
        0x1B,
        (
            "#080F对，女王陛下安排了\x01",
            "王城右翼的两间客房给我们。\x02\x03",
            "我和约修亚在右边，\x01",
            "艾丝蒂尔和雪拉扎德在左边。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1B, 400)

    ChrTalk(
        0x101,
        (
            "#000F哎……？\x01",
            "我和雪拉姐住一起吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#080F别的组合可以吗？\x02\x03",
            "那么，我和艾丝蒂尔，\x01",
            "约修亚和雪拉扎德，这样安排好了。\x02\x03",
            "你可以尽情向老爸撒娇了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F……果然\x01",
            "还是和雪拉姐一起比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#080F哇哈哈，真是害羞啊。\x02\x03",
            "那么，晚上再见了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_511C():

        label("loc_511C")

        TurnDirection(0xFE, 0x1B, 0)
        OP_48()
        Jump("loc_511C")

    QueueWorkItem2(0x101, 1, lambda_511C)

    def lambda_512D():

        label("loc_512D")

        TurnDirection(0xFE, 0x1B, 0)
        OP_48()
        Jump("loc_512D")

    QueueWorkItem2(0x102, 1, lambda_512D)
    OP_43(0x1B, 0x1, 0x0, 0xB)
    Sleep(3000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_92(0x102, 0x101, 0x5DC, 0x3E8, 0x0)

    ChrTalk(
        0x102,
        (
            "#010F好久没能和父亲住在同一间屋子了，\x01",
            "不是很好嘛。\x02\x03",
            "关于你的母亲……\x01",
            "不是有很多想说的事情吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F虽然是这样没错……\x02\x03",
            "不过很不情愿\x01",
            "让约修亚和雪拉姐在一起……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F哎？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F没、没什么啦！\x02\x03",
            "话说回来……\x01",
            "赶快去散步吧！\x02\x03",
            "街上好像很热闹呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊。\x01",
            "还有很多地方没看呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x66B)
    EventEnd(0x0)
    OP_6A(0x0)
    Return()

    # Function_10_4265 end

    def Function_11_5382(): pass

    label("Function_11_5382")

    OP_90(0x1B, 0xFFFFFD26, 0x0, 0x4E2, 0x7D0, 0x0)
    OP_8E(0x1B, 0x46, 0x2EE, 0xAAD2, 0x7D0, 0x0)
    OP_8E(0x1B, 0x190, 0x2EE, 0xBBBC, 0x7D0, 0x0)
    Return()

    # Function_11_5382 end

    SaveToFile()

Try(main)
