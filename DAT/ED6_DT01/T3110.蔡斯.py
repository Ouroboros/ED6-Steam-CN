from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3110   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3110.x',
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
        '露依赛',                               # 9
        '乌缇',                                 # 10
        '鲁特尔',                               # 11
        '索黛丽娅',                             # 12
        '米优',                                 # 13
        '兰达',                                 # 14
        '斯坦因',                               # 15
        '阿利瑟',                               # 16
        '温丝',                                 # 17
        '乌尔斯',                               # 18
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
        'ED6_DT07/CH01430 ._CH',             # 00
        'ED6_DT07/CH01070 ._CH',             # 01
        'ED6_DT07/CH01020 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH01050 ._CH',             # 04
        'ED6_DT07/CH01000 ._CH',             # 05
        'ED6_DT07/CH01200 ._CH',             # 06
        'ED6_DT07/CH01130 ._CH',             # 07
        'ED6_DT07/CH01470 ._CH',             # 08
        'ED6_DT07/CH01270 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01430P._CP',             # 00
        'ED6_DT07/CH01070P._CP',             # 01
        'ED6_DT07/CH01020P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH01050P._CP',             # 04
        'ED6_DT07/CH01000P._CP',             # 05
        'ED6_DT07/CH01200P._CP',             # 06
        'ED6_DT07/CH01130P._CP',             # 07
        'ED6_DT07/CH01470P._CP',             # 08
        'ED6_DT07/CH01270P._CP',             # 09
    )

    DeclNpc(
        X                   = -1900,
        Z                   = 4000,
        Y                   = 23230,
        Direction           = 254,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -100,
        Z                   = 0,
        Y                   = 25860,
        Direction           = 263,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
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
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -3290,
        Z                   = 0,
        Y                   = 2790,
        Direction           = 224,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 23740,
        Z                   = 0,
        Y                   = 1040,
        Direction           = 142,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 23410,
        Z                   = 150,
        Y                   = 740,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 27780,
        Z                   = 0,
        Y                   = 25700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        TalkScenaIndex      = 15,
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
        TalkScenaIndex      = 16,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )


    ScpFunction(
        "Function_0_23A",          # 00, 0
        "Function_1_446",          # 01, 1
        "Function_2_468",          # 02, 2
        "Function_3_47E",          # 03, 3
        "Function_4_4A2",          # 04, 4
        "Function_5_4C6",          # 05, 5
        "Function_6_4EA",          # 06, 6
        "Function_7_50E",          # 07, 7
        "Function_8_532",          # 08, 8
        "Function_9_136A",         # 09, 9
        "Function_10_1F77",        # 0A, 10
        "Function_11_2B4F",        # 0B, 11
        "Function_12_3342",        # 0C, 12
        "Function_13_3B84",        # 0D, 13
        "Function_14_3D04",        # 0E, 14
        "Function_15_4A0B",        # 0F, 15
        "Function_16_4BDB",        # 10, 16
        "Function_17_4E3B",        # 11, 17
    )


    def Function_0_23A(): pass

    label("Function_0_23A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_270")
    SetChrFlags(0xA, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0xC, 21930, 0, 2180, 138)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    Jump("loc_445")

    label("loc_270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2A6")
    SetChrFlags(0xA, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0xC, 21930, 0, 2180, 138)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    Jump("loc_445")

    label("loc_2A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2BF")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_445")

    label("loc_2BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2EE")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 28100, 0, 22440, 0)
    Jump("loc_445")

    label("loc_2EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_38A")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1800, 0, 21070, 263)
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrPos(0x8, -1720, 0, 24500, 275)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -4050, 0, -3180, 348)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 26330, 4000, 25200, 76)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 27970, 4000, 25230, 275)
    SetChrPos(0xA, 21330, 0, 3950, 352)
    OP_43(0xA, 0x0, 0x0, 0x2)
    Jump("loc_445")

    label("loc_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3D3")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x80)
    OP_43(0xB, 0x0, 0x0, 0x2)
    SetChrPos(0xB, -4740, 0, 2840, 90)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -3450, 0, 2830, 270)
    OP_43(0xF, 0x0, 0x0, 0x2)
    Jump("loc_445")

    label("loc_3D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_3F1")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_445")

    label("loc_3F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_420")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, -1800, 0, 21070, 263)
    Jump("loc_445")

    label("loc_420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_434")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_445")

    label("loc_434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_445")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xA, 0x80)

    label("loc_445")

    Return()

    # Function_0_23A end

    def Function_1_446(): pass

    label("Function_1_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45E")
    OP_B1("t3110_y")
    Jump("loc_467")

    label("loc_45E")

    OP_B1("t3110_n")

    label("loc_467")

    Return()

    # Function_1_446 end

    def Function_2_468(): pass

    label("Function_2_468")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_468")

    label("loc_47D")

    Return()

    # Function_2_468 end

    def Function_3_47E(): pass

    label("Function_3_47E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A1")
    OP_8D(0xFE, 290, 22470, 1800, 25300, 2000)
    Jump("Function_3_47E")

    label("loc_4A1")

    Return()

    # Function_3_47E end

    def Function_4_4A2(): pass

    label("Function_4_4A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C5")
    OP_8D(0xFE, -1920, 1860, 2170, -2770, 2000)
    Jump("Function_4_4A2")

    label("loc_4C5")

    Return()

    # Function_4_4A2 end

    def Function_5_4C6(): pass

    label("Function_5_4C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E9")
    OP_8D(0xFE, -4730, 3760, -1290, 1770, 2000)
    Jump("Function_5_4C6")

    label("loc_4E9")

    Return()

    # Function_5_4C6 end

    def Function_6_4EA(): pass

    label("Function_6_4EA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_50D")
    OP_8D(0xFE, 20960, 3050, 25510, -530, 2000)
    Jump("Function_6_4EA")

    label("loc_50D")

    Return()

    # Function_6_4EA end

    def Function_7_50E(): pass

    label("Function_7_50E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_531")
    OP_8D(0xFE, -5320, 520, -1440, 630, 2000)
    Jump("Function_7_50E")

    label("loc_531")

    Return()

    # Function_7_50E end

    def Function_8_532(): pass

    label("Function_8_532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_59C")
    TalkBegin(0x8)

    ChrTalk(
        0xFE,
        "啊，今天早上也是神清气爽呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "工作充实的话，\x01",
            "就连睡醒的感觉也很好。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_1369")

    label("loc_59C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_73B")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_66F")

    ChrTalk(
        0xFE,
        (
            "竟然能够参加\x01",
            "新型导力引擎的开发，\x01",
            "这样的机会绝没有第二次了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔唔唔唔，\x01",
            "不绞尽脑汁的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哪里还有\x01",
            "喝汤的空闲啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_735")

    label("loc_66F")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "呜呜，\x01",
            "虽说我被调动到了\x01",
            "开发导力引擎的工作岗位……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是自己连一个有份量的主意\x01",
            "都还没有提出呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……唉，不行。\x01",
            "这可不是发牢骚的时候。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_735")

    TalkEnd(0x8)
    Jump("loc_1369")

    label("loc_73B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_884")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7C3")
    TalkBegin(0x8)

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "总觉得今天外面很吵闹啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……嗯，不行不行。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对现在的我来说\x01",
            "可没有闲功夫注意别的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87E")

    label("loc_7C3")

    OP_A2(0x2)
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0x8)

    ChrTalk(
        0xFE,
        (
            "啊～？\x01",
            "要重新设计枪筒吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，真麻烦，\x01",
            "一点干劲也没有了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊啊～女神爱德丝啊。\x01",
            "就算是做梦也行，\x01",
            "请让我被调到与飞艇有关的工作吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87E")

    TalkEnd(0x8)
    Jump("loc_1369")

    label("loc_884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_93A")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0x8)

    ChrTalk(
        0xFE,
        (
            "资料我带了，\x01",
            "妹妹也拜托给乌尔斯了……嗯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好了～\x01",
            "差不多该去上班了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊啊～\x01",
            "还是觉得很累。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_1369")

    label("loc_93A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_BB5")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9E3")

    ChrTalk(
        0xFE,
        (
            "导力自身停止运行这种事\x01",
            "以前听也没听说过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在中央工房\x01",
            "一定是乱成一团了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAF")

    label("loc_9E3")

    OP_A2(0x2)
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        "噢，提妲，早呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘻嘻～～\x01",
            "昨晚的麻烦可真不小呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x107,
        (
            "#562F呜呜……\x02\x03",
            "真是的，\x01",
            "不要再笑话我啦。\x02\x03",
            "玛多克工房长因为此事\x01",
            "已经忙得不可开交了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过导力自身停止运行\x01",
            "这种事还是第一次遇到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "演算室的威尔姆他们\x01",
            "现在一定慌乱不堪吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "光是维护和检修\x01",
            "那部演算导力器\x01",
            "就够他们忙的了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BAF")

    TalkEnd(0x8)
    Jump("loc_1369")

    label("loc_BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1180")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_CB3")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0x8)

    ChrTalk(
        0xFE,
        (
            "……嗯，\x01",
            "结晶光学论集、结晶光学论集……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "那本书放到哪里了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，我进工房\x01",
            "不是想要做导力枪啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呜呜，工作真是辛苦呀。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_117D")

    label("loc_CB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10CE")
    OP_A2(0x573)
    OP_A2(0x2)
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF4")

    ChrTalk(
        0xFE,
        (
            "哎？\x01",
            "提妲，有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2F")

    label("loc_CF4")


    ChrTalk(
        0xFE,
        "……嗯？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(
        0xFE,
        (
            "哦，提妲。\x01",
            "来这里有什么事呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2F")


    ChrTalk(
        0x107,
        (
            "#064F露依赛姐姐\x01",
            "你今天不用去设计室吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，刚才在整理\x01",
            "正在设计中的导力枪资料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "提妲你是不是\x01",
            "在给客人们带路啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#061F是呀，没错。\x01",
            "正在回家的路上呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说到提妲的家，\x01",
            "最近是不是太过于安静了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好久没有发生爆炸\x01",
            "或者瓦斯泄漏的事故了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F（……爆、爆炸？）\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x107,
        (
            "#560F那、那个……虽说是爆炸，\x01",
            "其实呢，也不是很严重的啦。\x02\x03",
            "只是把窗户上的玻璃\x01",
            "都炸飞了而已……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F唔……\x01",
            "那个已经十分严重了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F……就是啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(
        0xFE,
        (
            "其实呀，\x01",
            "我也对博士的新发明十分好奇呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果发明进入了测试阶段，\x01",
            "一定会让邻居们听到\x01",
            "叮叮当当的做实验的声音吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F啊，是的。\x01",
            "总是一次次地给大家添麻烦呢。\x02\x03",
            "#061F露依赛姐姐也在\x01",
            "负责新型导力枪的研制工作吧，\x01",
            "请一定要加油啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯。\x01",
            "我看情况加油吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_117D")

    label("loc_10CE")

    TalkBegin(0x8)
    OP_A2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1123")

    ChrTalk(
        0xFE,
        (
            "呀，提妲。\x01",
            "还在给客人带路吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_117A")

    label("loc_1123")


    ChrTalk(
        0xFE,
        "……嗯？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(
        0xFE,
        (
            "呀，提妲。\x01",
            "还在给客人带路吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_117A")

    TalkEnd(0x8)

    label("loc_117D")

    Jump("loc_1369")

    label("loc_1180")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1237")
    OP_A2(0x0)
    OP_4A(0x9, 255)
    TurnDirection(0x9, 0xFE, 400)

    ChrTalk(
        0x9,
        (
            "姐姐，\x01",
            "拜托收拾一下床铺吧～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这个样子，\x01",
            "都不能睡午觉啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是吗。\x01",
            "嗯，我知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "现在有点忙，一会儿收拾吧。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x9, 255)
    Jump("loc_135F")

    label("loc_1237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D6")
    OP_A2(0x1)
    OP_4A(0x9, 255)
    TurnDirection(0x9, 0xFE, 400)

    ChrTalk(
        0x9,
        (
            "喂！\x01",
            "姐姐你听到了没有？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "快·来·收·拾·啦！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x9, 400)

    ChrTalk(
        0xFE,
        (
            "啊～～\x01",
            "真是啰嗦呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我正在找论文呢。\x01",
            "拜托你安静点！\x02",
        )
    )

    OP_8C(0xFE, 254, 400)
    CloseMessageWindow()
    OP_4B(0x9, 255)
    Jump("loc_135F")

    label("loc_12D6")


    ChrTalk(
        0xFE,
        (
            "……真是的，\x01",
            "我妹妹总是啰嗦个不停。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她如果能像\x01",
            "拉赛尔博士的孙女提妲一样就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_135F")

    OP_8C(0x9, 263, 0)
    TalkEnd(0x8)

    label("loc_1369")

    Return()

    # Function_8_532 end

    def Function_9_136A(): pass

    label("Function_9_136A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_144E")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13DD")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "一睁开眼睛，\x01",
            "就看见被子上\x01",
            "压着一本很大的书。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "怪不得睡得那么难受。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1448")

    label("loc_13DD")


    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "姐姐为什么就不能\x01",
            "把书给收拾好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明明床边\x01",
            "就有书架的嘛……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1448")

    TalkEnd(0xFE)
    Jump("loc_1F76")

    label("loc_144E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_151C")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14AD")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "……姐姐也真是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算是工作有干劲的时候， \x01",
            "也从来不会收拾一下东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1516")

    label("loc_14AD")


    ChrTalk(
        0xFE,
        (
            "唉，算了～\x01",
            "还是拜托乌尔斯哥哥吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他是姐姐的男朋友，\x01",
            "肯定要负一些连带责任的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1516")

    TalkEnd(0xFE)
    Jump("loc_1F76")

    label("loc_151C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_166B")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F2")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "我姐姐她昨晚\x01",
            "为了工作的事头疼不已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过呢，\x01",
            "喝了点汤之后好像就有好主意了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔，汤里面是不是放了什么\x01",
            "能让人的脑袋变聪明的东西啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1665")

    label("loc_15F2")


    ChrTalk(
        0xFE,
        (
            "汤里面含有什么\x01",
            "让脑子变聪明的东西吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "去问问琪爱拉老师吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1665")

    TalkEnd(0xFE)
    Jump("loc_1F76")

    label("loc_166B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1789")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1717")
    OP_A2(0x3)
    SetChrName("民家１")

    ChrTalk(
        0xFE,
        (
            "真是奇怪，\x01",
            "姐姐她突然变得很有干劲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她的男朋友乌尔斯来了，\x01",
            "也不去聊天，只顾着埋头工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……呜呜，感觉真糟糕啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1783")

    label("loc_1717")


    ChrTalk(
        0xFE,
        (
            "不过在这里抱怨也没用，\x01",
            "还不如好好休息一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "乌尔斯哥哥做的汤\x01",
            "真是很好喝啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1783")

    TalkEnd(0xFE)
    Jump("loc_1F76")

    label("loc_1789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_19B8")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_191D")
    OP_A2(0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1845")
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        (
            "听说工房那边\x01",
            "出了什么事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "提妲你没事吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#063F啊……\x02\x03",
            "嗯、嗯！\x01",
            "都没事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那样就好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_191A")

    label("loc_1845")


    ChrTalk(
        0xFE,
        (
            "听说工房那边\x01",
            "似乎是发生了什么事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的姐姐\x01",
            "今天没有去工房上班，\x01",
            "所以完全没有受伤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "平安无事虽然好，\x01",
            "不过擅离岗位说不过去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_191A")

    Jump("loc_19B2")

    label("loc_191D")


    ChrTalk(
        0xFE,
        (
            "我的姐姐\x01",
            "今天没有去工房上班，\x01",
            "所以完全没有受伤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "平安无事虽然好，\x01",
            "不过擅离岗位说不过去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B2")

    TalkEnd(0xFE)
    Jump("loc_1F76")

    label("loc_19B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1ADD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19CC")
    SetChrFlags(0xFE, 0x10)

    label("loc_19CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A72")
    OP_A2(0x3)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x11, 400)

    ChrTalk(
        0xFE,
        "对了，乌尔斯哥哥。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "午饭做好的话，\x01",
            "拜托你打扫一下床铺哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "姐姐她连书也不收拾，\x01",
            "让我很头疼呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 263, 400)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_1AD7")

    label("loc_1A72")


    ChrTalk(
        0xFE,
        (
            "乌尔斯哥哥\x01",
            "是姐姐的男朋友哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "他偏偏会跟这样的姐姐交往……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……还真的有点同情他呢。\x02",
    )

    CloseMessageWindow()

    label("loc_1AD7")

    TalkEnd(0xFE)
    Jump("loc_1F76")

    label("loc_1ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_1B61")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "姐姐，\x01",
            "你最好还是赶快去上班吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "再磨蹭的话\x01",
            "就会迟到了呢……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1F76")

    label("loc_1B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_1CC0")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C76")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "呼啊，早上好。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(
        0xFE,
        "呀，是提妲啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#061F早上好，乌缇。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "提妲今天\x01",
            "也要去工房工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F嗯，是呀。\x02\x03",
            "我今天要去\x01",
            "协助爷爷工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哦，是吗。\x01",
            "看来你真的很忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真不愧是提妲啊。\x01",
            "感觉就像是个著名研究员。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CBA")

    label("loc_1C76")

    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        (
            "嗯，提妲。\x01",
            "看来你真的很忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的姐姐有你一半就好了，\x01",
            "她实在是太散漫了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CBA")

    TalkEnd(0xFE)
    Jump("loc_1F76")

    label("loc_1CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1EAF")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 4)), scpexpr(EXPR_END)), "loc_1D3A")

    ChrTalk(
        0xFE,
        (
            "呼～就算这样，\x01",
            "姐姐也一点没有\x01",
            "要收拾干净的意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "实在是～\x01",
            "一个吊儿郎当的姐姐啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EA9")

    label("loc_1D3A")

    OP_A2(0x574)

    ChrTalk(
        0xFE,
        "啊，提妲。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F乌缇，\x01",
            "已经放学了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎，你在说什么啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "今天可不是主日学校上课的日子哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F咦……\x02\x03",
            "是这样吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "提妲啊，\x01",
            "你偶尔也得休息一下嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你也来学校吧。\x01",
            "大家都等着你来玩呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F啊，嗯，不好意思。\x01",
            "最近一直在工房帮忙工作……\x02\x03",
            "但是呢，\x01",
            "有空的话我一定去哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，那说定了。\x02",
    )

    CloseMessageWindow()

    label("loc_1EA9")

    TalkEnd(0xFE)
    Jump("loc_1F76")

    label("loc_1EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EBC")
    SetChrFlags(0xFE, 0x10)

    label("loc_1EBC")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F37")
    OP_A2(0x0)
    TurnDirection(0xFE, 0x8, 400)

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "姐姐还真是邋遢呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "赶快把床铺收拾了吧～\x01",
            "要不然就睡不了午觉了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 263, 400)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_1F73")

    label("loc_1F37")


    ChrTalk(
        0xFE,
        (
            "我的姐姐\x01",
            "真是行为散漫啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你看吧，乱成这个样子。\x01",
            "实在让人没话说了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F73")

    TalkEnd(0x9)

    label("loc_1F76")

    Return()

    # Function_9_136A end

    def Function_10_1F77(): pass

    label("Function_10_1F77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2193")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2014")

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "最近都没见到拉赛尔博士呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没准又是呆在研究室里闭门不出，\x01",
            "埋头于某项发明吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2190")

    label("loc_2014")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "从雨果先生那里传来了消息，\x01",
            "说是已经决定了共同参与\x01",
            "导力引擎研究的人员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然研究者好像是位年轻的女性，\x01",
            "不过现今的世界上，性别和年龄都没有界限。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要看见那位拉赛尔博士，\x01",
            "就会明白年龄已经无关紧要了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀……说起来\x01",
            "最近都没见到拉赛尔博士呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2190")

    Jump("loc_2B4B")

    label("loc_2193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_22B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2237")

    ChrTalk(
        0xFE,
        (
            "在这种时候，\x01",
            "外出旅游的记忆就会浮现在脑海中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真想再到海边的赌吧玩玩，\x01",
            "好好放松一下啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22AE")

    label("loc_2237")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "呼呼，这样的话，\x01",
            "合同书就算整理完了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "一个人干活的时候是最忙的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22AE")

    Jump("loc_2B4B")

    label("loc_22B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2471")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2368")

    ChrTalk(
        0xFE,
        (
            "被盗走的……\x01",
            "只有演算导力器吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说被犯人偷走了，\x01",
            "不过他们也不懂得运用吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为能够完美运用那个机器的人\x01",
            "也只有拉赛尔博士一个人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_246E")

    label("loc_2368")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "真让人吃惊啊。\x01",
            "听说中央工房那里出事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "万幸的是没有人受伤，\x01",
            "但据说演算导力器被盗了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，老实说，\x01",
            "我也不太明白犯人的动机呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_246E")

    Jump("loc_2B4B")

    label("loc_2471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_260D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2500")

    ChrTalk(
        0xFE,
        (
            "今天大街上\x01",
            "还真是热闹啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是不是拉赛尔博士\x01",
            "又做了什么试验啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_260A")

    label("loc_2500")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "昨天，\x01",
            "我在工房认识了一个\x01",
            "从卡尔瓦德共和国来的年轻商人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他好像是个导力器商人，\x01",
            "所以我想多向他打听一些事情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以后向共和国出口的飞艇\x01",
            "也会继续增加吧。\x01",
            "真想和他尽快建立好合作关系。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_260A")

    Jump("loc_2B4B")

    label("loc_260D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_27BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_26BC")

    ChrTalk(
        0xFE,
        (
            "我妻子索黛丽娅\x01",
            "本来就很讨厌大型飞艇……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看见了昨天的现象，\x01",
            "她这种情绪更加严重了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不知不觉间\x01",
            "就有了这么多影响了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27BA")

    label("loc_26BC")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "『如果正在飞行中的飞艇\x01",
            "　真的像昨天晚上那样突然失去了导力，\x01",
            "　那会怎么样呢……』\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "妻子索黛丽娅这样问我，\x01",
            "我也无言以对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她本来就\x01",
            "十分害怕乘坐飞艇……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为昨夜的事，\x01",
            "她这种情绪更加严重了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27BA")

    Jump("loc_2B4B")

    label("loc_27BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_294D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2846")

    ChrTalk(
        0xFE,
        (
            "昨天的现象\x01",
            "真的有点可怕呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没有给来买飞艇的客人\x01",
            "留下坏印象就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_294A")

    label("loc_2846")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "我的工作就是\x01",
            "飞艇买卖的中介。\x01",
            "昨天的现象真有点让人害怕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果这事在飞艇飞行时发生，\x01",
            "肯定会酿成大惨剧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没有给来买飞艇的客人\x01",
            "留下坏印象就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_294A")

    Jump("loc_2B4B")

    label("loc_294D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_298C")

    ChrTalk(
        0xFE,
        (
            "好～\x01",
            "休息完了就开始工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B4B")

    label("loc_298C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2A98")

    ChrTalk(
        0xFE,
        (
            "我的工作就是\x01",
            "飞艇买卖的中介。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在『埃尔赛尤号』开始服役之前，\x01",
            "我也在工房和亲卫队之间\x01",
            "作了很多工作上的协调哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过自从试飞测试结束之后，\x01",
            "我就再没有机会听到\x01",
            "有关『埃尔赛尤号』的消息了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过只要知道它在顺利执行任务，\x01",
            "我就安心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B4B")

    label("loc_2A98")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "我正好刚从\x01",
            "卢安旅行回来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在我离开之后，\x01",
            "『埃尔赛尤号』好像在卢安出现了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是可惜啊。\x01",
            "要是在那再呆上一阵子，\x01",
            "也许就能再次见到『埃尔赛尤号』。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B4B")

    TalkEnd(0xFE)
    Return()

    # Function_10_1F77 end

    def Function_11_2B4F(): pass

    label("Function_11_2B4F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2C51")

    ChrTalk(
        0xFE,
        (
            "我家孩子米优啊，\x01",
            "上次对我说\x01",
            "将来想进入中央工房……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "仔细问了问她，\x01",
            "原来是想成为接待小姐呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听她这么说，总算让人放心一点了。\x01",
            "因为，怎么看那孩子\x01",
            "也不像是当研究者的料呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_333E")

    label("loc_2C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2D61")

    ChrTalk(
        0xFE,
        (
            "那次事件之后，\x01",
            "米优很快对工房有了兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果她是认真的话，\x01",
            "不如和爷爷商量一下吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……不过，不管怎么想\x01",
            "我都不觉得那孩子可以进入工房。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_333E")

    label("loc_2D61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2E61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2DCE")

    ChrTalk(
        0xFE,
        (
            "因为我当时在酒馆里面，\x01",
            "所以我一点也不知道\x01",
            "中央工房出了事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E5E")

    label("loc_2DCE")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "我家爷爷\x01",
            "刚刚终于回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "白天泡在酒馆，\x01",
            "到了晚上才回来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我觉得有点反常呢。\x02",
    )

    CloseMessageWindow()

    label("loc_2E5E")

    Jump("loc_333E")

    label("loc_2E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2EB1")

    ChrTalk(
        0xFE,
        "竟然袭击中央工房……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "到底是谁干的好事呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_333E")

    label("loc_2EB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2FC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2F02")

    ChrTalk(
        0xFE,
        "啊，说起来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我家爷爷，\x01",
            "又跑到哪里去了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FC1")

    label("loc_2F02")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "提妲。\x01",
            "又要出去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊，是的。\x01",
            "要去亚尔摩村呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，是吗？\x01",
            "总是忙着工作，真辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "趁这次机会，\x01",
            "把工作做完之后\x01",
            "去好好泡泡温泉怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我家爷爷\x01",
            "也很喜欢\x01",
            "那里的温泉呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FC1")

    Jump("loc_333E")

    label("loc_2FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_307E")

    ChrTalk(
        0xFE,
        (
            "我问了一下我丈夫，\x01",
            "要是飞艇上的导力停止的话会怎么样呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如我所料，\x01",
            "丈夫答不上来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以我说，\x01",
            "飞艇这东西根本不能信赖啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_333E")

    label("loc_307E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3186")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_30E8")

    ChrTalk(
        0xFE,
        (
            "我在准备晚饭的时候，\x01",
            "一下子没有导力了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "导力器这东西，\x01",
            "经常会吓人一跳。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3183")

    label("loc_30E8")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "我在准备晚饭的时候，\x01",
            "突然导力停止供应了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，多亏了这样，\x01",
            "女儿丢下不管的炖汤\x01",
            "最后才没有被烧干。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3183")

    Jump("loc_333E")

    label("loc_3186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3290")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3217")
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        (
            "上学的时候，\x01",
            "请在学习上多多帮助我们家米优啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "拜托了，提妲。\x02",
    )

    CloseMessageWindow()
    Jump("loc_328D")

    label("loc_3217")

    OP_A2(0x5)
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        (
            "哎呀，是提妲啊。\x01",
            "欢迎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的家人\x01",
            "去卢安旅行回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "米优她好像玩闹过头了，\x01",
            "这孩子这么大了\x01",
            "却还是个野丫头呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_328D")

    Jump("loc_333E")

    label("loc_3290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_32E9")

    ChrTalk(
        0xFE,
        (
            "从今天开始又要回到\x01",
            "每天的忙碌生活之中了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_333E")

    label("loc_32E9")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "我的家人\x01",
            "去卢安旅行回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，大家看起来都玩得很开心，\x01",
            "这真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_333E")

    TalkEnd(0xFE)
    Return()

    # Function_11_2B4F end

    def Function_12_3342(): pass

    label("Function_12_3342")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_33E7")

    ChrTalk(
        0xFE,
        (
            "我说爷爷啊。\x01",
            "我想当工房接待处的服务小姐啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "爷爷，\x01",
            "你在中央工房有很多熟人吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "给我介绍一个信得过的人吧～\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B80")

    label("loc_33E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_3470")

    ChrTalk(
        0xFE,
        (
            "嗯～\x01",
            "考虑到将来，\x01",
            "还是到中央工房工作最好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且受人注目的程度\x01",
            "在蔡斯也应该是第一的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B80")

    label("loc_3470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3544")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_34D3")

    ChrTalk(
        0xFE,
        (
            "不、不过\x01",
            "我可不是在幸灾乐祸啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我只是觉得中央工房\x01",
            "真～的是相当厉害呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3541")

    label("loc_34D3")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "听说了吗？\x01",
            "中央工房的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不愧是中央工房啊。\x01",
            "在蔡斯那是\x01",
            "最受人瞩目的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3541")

    Jump("loc_3B80")

    label("loc_3544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3647")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_35CB")

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "我将来也想在中央工房工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "又有拉赛尔博士在，\x01",
            "就不会无聊了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3644")

    label("loc_35CB")

    OP_A2(0x6)
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "我好羡慕提妲啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#064F嗯？\x01",
            "为什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那里每天都有事做啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#067F……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呜呜，很闲呢。\x02",
    )

    CloseMessageWindow()

    label("loc_3644")

    Jump("loc_3B80")

    label("loc_3647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_37C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_36B3")

    ChrTalk(
        0xFE,
        (
            "在见惯了的事物中，\x01",
            "说不定也会存在着\x01",
            "从来没见过的东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……唔，\x01",
            "真是有哲理啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37C6")

    label("loc_36B3")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "虽然旅行已经结束了，\x01",
            "又回到了平常的无聊生活，\x01",
            "不过昨晚真是好刺激啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "导力停了，\x01",
            "街上一片漆黑……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "无意间向上一望，\x01",
            "发现星空真是美丽啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为平时看不到这样的天空，\x01",
            "所以觉得有些不可思议。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37C6")

    Jump("loc_3B80")

    label("loc_37C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3940")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_385A")

    ChrTalk(
        0xFE,
        (
            "我在和妈妈准备晚饭的时候，\x01",
            "导力灯突然灭掉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我就到外面看了一下，\x01",
            "周围一片漆黑的，\x01",
            "那时侯可真急死我了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_393D")

    label("loc_385A")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "我在和妈妈准备晚饭的时候，\x01",
            "导力灯突然灭掉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我慌慌张张地跑出去看，\x01",
            "外面一片漆黑，真是急死我了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#561F啊呀呀……\x01",
            "对不起，米优。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(
        0xFE,
        "咦？怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为什么\x01",
            "提妲你要向我道歉？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_393D")

    Jump("loc_3B80")

    label("loc_3940")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3B0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_39C5")

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "无聊的日子又要开始了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "爷爷什么时候再带我出去玩啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B08")

    label("loc_39C5")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "啊啊，真讨厌啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊，米优。\x01",
            "到卢安旅行好玩吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        (
            "实在是太棒了！\x01",
            "真是让人兴奋得不得了呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……不过呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "到了要回蔡斯的时候，\x01",
            "心情就一落千丈了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "等待着我的就是\x01",
            "无聊的生活和主日学校的作业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#067F啊，啊哈哈……\x02",
    )

    CloseMessageWindow()

    label("loc_3B08")

    Jump("loc_3B80")

    label("loc_3B0B")


    ChrTalk(
        0xFE,
        (
            "妈妈要是也一起\x01",
            "去卢安旅行就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过这是不可能的。\x01",
            "因为妈妈有飞艇恐惧症呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B80")

    TalkEnd(0xFE)
    Return()

    # Function_12_3342 end

    def Function_13_3B84(): pass

    label("Function_13_3B84")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3C9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3BF9")

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "这可是我可爱的孙女的请求。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "无论如何，\x01",
            "我也会如她所愿，\x01",
            "让她能在工房工作的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C99")

    label("loc_3BF9")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "虽说有熟人……\x01",
            "但大家都是搞技术的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "跟他们说接待处小姐的事\x01",
            "大概也没有什么意义吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唉，这可为难了。\x02",
    )

    CloseMessageWindow()

    label("loc_3C99")

    Jump("loc_3D00")

    label("loc_3C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_3D00")

    ChrTalk(
        0xFE,
        (
            "索黛丽娅，\x01",
            "晚饭还没有好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天一天\x01",
            "忙着和别人说话，\x01",
            "肚子饿得受不了了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D00")

    TalkEnd(0xFE)
    Return()

    # Function_13_3B84 end

    def Function_14_3D04(): pass

    label("Function_14_3D04")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3F11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3DF4")

    ChrTalk(
        0xFE,
        (
            "耶鲁克店长\x01",
            "好像终于也开始\x01",
            "认同我的理念了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他调整武器的技术很棒，\x01",
            "是个了不起的鉴定人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但愿他能成为\x01",
            "一个不拘小节，\x01",
            "能够成就更大事业的商人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F0E")

    label("loc_3DF4")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "昨晚，我和耶鲁克店长\x01",
            "商量了进货的情况……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "终于，他也稍许表示出\x01",
            "对我的理念的理解和赞同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "武器店做的可是\x01",
            "关系到顾客生命的买卖。\x01",
            "马马虎虎做出来的东西可不能使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从今往后，\x01",
            "我也要坚持不懈地\x01",
            "把这个想法传达给他才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F0E")

    Jump("loc_4A07")

    label("loc_3F11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_407B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3FA5")

    ChrTalk(
        0xFE,
        (
            "我家温丝的内心似乎\x01",
            "也憧憬着做一名研究者呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果他决定要走这条路的话，\x01",
            "我希望他能成为一名视野广阔的学者。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4078")

    label("loc_3FA5")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "单单将性能提高的话，\x01",
            "新技术是无法得到普及的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "初次在世界上进行推广的时候，\x01",
            "应该注重易用性，好让更多人接受。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就像把七耀石\x01",
            "利用在导力器的技术上，\x01",
            "从而引起一场导力革命那样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4078")

    Jump("loc_4A07")

    label("loc_407B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_4267")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4156")

    ChrTalk(
        0xFE,
        (
            "加鲁诺他\x01",
            "好像也终于理解我那种\x01",
            "重视武器可靠性的想法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他终于学会\x01",
            "从使用者的角度来\x01",
            "重新认识自己的研究了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉呀，要是耶鲁克店长\x01",
            "也能早点注意到就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4264")

    label("loc_4156")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "今天早上加鲁诺他\x01",
            "突然来拜访我了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他对我说，终于理解了我的\x01",
            "重视武器可靠性的方针呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他终于学会\x01",
            "从使用者的角度来\x01",
            "重新认识自己的研究了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "或许是什么事\x01",
            "让他发生了转变吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4264")

    Jump("loc_4A07")

    label("loc_4267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_4534")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_43DC")

    ChrTalk(
        0xFE,
        (
            "对于武器来说， \x01",
            "最重要的就是可靠性和操作性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "紧急时刻，\x01",
            "谁都能够自如地使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这对于使用者来说\x01",
            "是最重要的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过竟然把还处于\x01",
            "试制阶段的导力枪拿出来出售……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来加鲁诺他有必要\x01",
            "站在使用者的角度\x01",
            "来考虑一下问题呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4531")

    label("loc_43DC")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "今天，\x01",
            "我要去和中央工房的加鲁诺面谈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他似乎在向\x01",
            "耶鲁克店长兜售试制品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我要清楚地告诉他，\x01",
            "在我的店里面\x01",
            "只能销售让顾客放心的武器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "今天偏偏又发生了那样的事，\x01",
            "没能和他见到面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我会改天\x01",
            "重新找个机会找他谈谈的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4531")

    Jump("loc_4A07")

    label("loc_4534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4691")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_45C3")

    ChrTalk(
        0xFE,
        (
            "工房周围\x01",
            "好不容易安静了下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，学校差不多也该放学了。\x01",
            "一会儿温丝也该回来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_468E")

    label("loc_45C3")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "工房周围\x01",
            "好不容易安静了下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在主日学校放学前，\x01",
            "骚乱能够结束真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不想让孩子们\x01",
            "看见那样的骚动呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_468E")

    Jump("loc_4A07")

    label("loc_4691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_47FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4718")

    ChrTalk(
        0xFE,
        (
            "当然啦，\x01",
            "也不是耶鲁克一个人的错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "毕竟技术人员的那种\x01",
            "仅仅追求性能的态度也是个问题。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F9")

    label("loc_4718")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "店长耶鲁克虽说人很热心，\x01",
            "维修武器的技术也相当不错，\x01",
            "却有一种只关心武器性能的癖好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，无论武器的性能如何优秀，\x01",
            "如果难以自如运用就变得没意义了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "反反复复地跟他说，\x01",
            "不要单单追求性能……\x01",
            "怎么就不能理解一下呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47F9")

    Jump("loc_4A07")

    label("loc_47FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_488A")

    ChrTalk(
        0xFE,
        (
            "身为一个有尊严的原技师，\x01",
            "我在武器进货的时候，\x01",
            "也是特别用心的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我准备了很多不错的商品，\x01",
            "请一定要来看看哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A07")

    label("loc_488A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4956")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "我家世代都是钟表工匠。\x01",
            "我年轻的时候也在\x01",
            "中央工房担任过技师的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "和客人交涉可真是一点都没趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "当我意识到这点的时候，\x01",
            "我的店子已经开张了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A07")

    label("loc_4956")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        "哎，你们是游击士吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想要订购武器的话，\x01",
            "就交给我们斯坦因武器商会吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我家的店正好\x01",
            "在你们游击士协会对面，\x01",
            "有空的话，请你们务必要来看看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A07")

    TalkEnd(0xFE)
    Return()

    # Function_14_3D04 end

    def Function_15_4A0B(): pass

    label("Function_15_4A0B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_4A80")

    ChrTalk(
        0xFE,
        (
            "温丝！\x01",
            "你又旷课了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎么老是那样啊。\x01",
            "又不是学不会。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BD7")

    label("loc_4A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4BD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4AFE")

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "主日学校一会儿就该放学了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "温丝今天\x01",
            "有没有认真上课啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BD7")

    label("loc_4AFE")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "之前知道不是火灾或事故的时候，\x01",
            "还松了一口气……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没想到偏偏是个案件。\x01",
            "真是做梦都想不到啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……哎呀，\x01",
            "主日学校一会儿就该放学了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我是不是该去\x01",
            "接温丝回家呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BD7")

    TalkEnd(0xFE)
    Return()

    # Function_15_4A0B end

    def Function_16_4BDB(): pass

    label("Function_16_4BDB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_4D51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_4C9B")

    ChrTalk(
        0xFE,
        (
            "我将来\x01",
            "想成为一名研究员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说从我的性格来看，\x01",
            "要将精力集中在某件事上\x01",
            "来进行研究是很困难的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是我相信成为研究员\x01",
            "对我的发展很有好处。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D4E")

    label("loc_4C9B")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "一清早加鲁诺叔叔\x01",
            "就来拜访爸爸了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "加鲁诺叔叔两眼通红。\x01",
            "看起来昨天一夜没睡的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "专注于某件事的研究员\x01",
            "看起来还真是光彩耀人呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D4E")

    Jump("loc_4E37")

    label("loc_4D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_4E37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_4DD6")

    ChrTalk(
        0xFE,
        (
            "妈妈，\x01",
            "请不要评价得这么主观哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我并非那种对某一件事\x01",
            "可以保持长久兴趣的孩子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E37")

    label("loc_4DD6")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "妈妈，\x01",
            "我并不是偷懒不学习哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只不过是，\x01",
            "我的兴趣与大家不一样而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E37")

    TalkEnd(0xFE)
    Return()

    # Function_16_4BDB end

    def Function_17_4E3B(): pass

    label("Function_17_4E3B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_4ED8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4E73")

    ChrTalk(
        0xFE,
        (
            "总之，\x01",
            "汤要重新热一下对吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ED5")

    label("loc_4E73")

    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "啊，露依赛那家伙\x01",
            "好像把汤完全煮干了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本来还想叫她\x01",
            "吃点什么呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4ED5")

    Jump("loc_4FCC")

    label("loc_4ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_4FCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4F63")

    ChrTalk(
        0xFE,
        (
            "得赶快做好饭，\x01",
            "回店里干活去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "光老板一个人的话，\x01",
            "无论如何都不行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FCC")

    label("loc_4F63")

    OP_A2(0xC)
    TurnDirection(0x11, 0x9, 400)

    ChrTalk(
        0xFE,
        (
            "给你做午饭\x01",
            "倒是没什么问题啦……\x01",
            "不过我说乌缇，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算我是她的男友，\x01",
            "为什么非要我给她收拾床铺不可啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 263, 0)

    label("loc_4FCC")

    TalkEnd(0xFE)
    Return()

    # Function_17_4E3B end

    SaveToFile()

Try(main)
