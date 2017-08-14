from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3160   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3160.x',
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
        '乌缇',                                 # 9
        '米优',                                 # 10
        '加雷利',                               # 11
        '艾妲',                                 # 12
        '呆呆',                                 # 13
        '库诺',                                 # 14
        '皮克塞恩教区长',                       # 15
        '修女琪爱拉',                           # 16
        '莱恩',                                 # 17
        '西加罗',                               # 18
        '艾德尔',                               # 19
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
        'ED6_DT07/CH01070 ._CH',             # 00
        'ED6_DT07/CH01050 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH01160 ._CH',             # 04
        'ED6_DT07/CH01060 ._CH',             # 05
        'ED6_DT07/CH01400 ._CH',             # 06
        'ED6_DT07/CH01410 ._CH',             # 07
        'ED6_DT07/CH01450 ._CH',             # 08
        'ED6_DT07/CH01140 ._CH',             # 09
        'ED6_DT07/CH01130 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01070P._CP',             # 00
        'ED6_DT07/CH01050P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH01160P._CP',             # 04
        'ED6_DT07/CH01060P._CP',             # 05
        'ED6_DT07/CH01400P._CP',             # 06
        'ED6_DT07/CH01410P._CP',             # 07
        'ED6_DT07/CH01450P._CP',             # 08
        'ED6_DT07/CH01140P._CP',             # 09
        'ED6_DT07/CH01130P._CP',             # 0A
    )

    DeclNpc(
        X                   = 61430,
        Z                   = 0,
        Y                   = 45130,
        Direction           = 345,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 54510,
        Z                   = 0,
        Y                   = 43560,
        Direction           = 345,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
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
        TalkScenaIndex      = 13,
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
        TalkScenaIndex      = 14,
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
        TalkScenaIndex      = 5,
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
        TalkScenaIndex      = 3,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = 58950,
        TriggerZ            = 1000,
        TriggerY            = 50290,
        TriggerRange        = 400,
        ActorX              = 58800,
        ActorZ              = 2500,
        ActorY              = 52200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_286",          # 00, 0
        "Function_1_637",          # 01, 1
        "Function_2_6A7",          # 02, 2
        "Function_3_6BD",          # 03, 3
        "Function_4_743",          # 04, 4
        "Function_5_7F6",          # 05, 5
        "Function_6_8C4",          # 06, 6
        "Function_7_912",          # 07, 7
        "Function_8_9B6",          # 08, 8
        "Function_9_AE9",          # 09, 9
        "Function_10_CD2",         # 0A, 10
        "Function_11_DA0",         # 0B, 11
        "Function_12_E4E",         # 0C, 12
        "Function_13_E53",         # 0D, 13
        "Function_14_3157",        # 0E, 14
    )


    def Function_0_286(): pass

    label("Function_0_286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2BC")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    Jump("loc_636")

    label("loc_2BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2F2")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    Jump("loc_636")

    label("loc_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_328")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    Jump("loc_636")

    label("loc_328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_394")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_365")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 15690, 4000, 42960, 96)
    Jump("loc_37B")

    label("loc_365")

    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 60250, 1000, 51160, 270)

    label("loc_37B")

    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 61930, 0, 46550, 4)
    Jump("loc_636")

    label("loc_394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3CA")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 57890, 0, 48010, 82)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 59610, 0, 47980, 274)
    Jump("loc_636")

    label("loc_3CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_43B")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 54110, 0, 42050, 20)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 55350, 0, 42050, 1)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    Jump("loc_636")

    label("loc_43B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_4A7")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 63500, 0, 46550, 348)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 62290, 0, 46560, 338)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    Jump("loc_636")

    label("loc_4A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_529")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 60350, 1000, 51110, 285)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 60270, 1000, 52070, 281)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 56260, 0, 45050, 348)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    Jump("loc_636")

    label("loc_529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_575")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 56260, 0, 45050, 348)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    Jump("loc_636")

    label("loc_575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_5D7")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 61490, 0, 45200, 2)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 62440, 0, 45200, 3)
    Jump("loc_636")

    label("loc_5D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_636")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 61490, 0, 45200, 2)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 62440, 0, 45200, 3)

    label("loc_636")

    Return()

    # Function_0_286 end

    def Function_1_637(): pass

    label("Function_1_637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_641")
    Jump("loc_6A6")

    label("loc_641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_64B")
    Jump("loc_6A6")

    label("loc_64B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_655")
    Jump("loc_6A6")

    label("loc_655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_65F")
    Jump("loc_6A6")

    label("loc_65F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_66D")
    OP_64(0x0, 0x1)
    Jump("loc_6A6")

    label("loc_66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_677")
    Jump("loc_6A6")

    label("loc_677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_681")
    Jump("loc_6A6")

    label("loc_681")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_68B")
    Jump("loc_6A6")

    label("loc_68B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_695")
    Jump("loc_6A6")

    label("loc_695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_69F")
    Jump("loc_6A6")

    label("loc_69F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6A6")

    label("loc_6A6")

    Return()

    # Function_1_637 end

    def Function_2_6A7(): pass

    label("Function_2_6A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6BC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6A7")

    label("loc_6BC")

    Return()

    # Function_2_6A7 end

    def Function_3_6BD(): pass

    label("Function_3_6BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_73F")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "终于到达蔡斯的礼拜堂了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这下我们的巡礼之旅\x01",
            "只剩下格兰赛尔的大圣堂了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73F")

    TalkEnd(0xFE)
    Return()

    # Function_3_6BD end

    def Function_4_743(): pass

    label("Function_4_743")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7F2")

    ChrTalk(
        0xFE,
        (
            "和城里不同，\x01",
            "礼拜堂真是出乎意料地简单呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没有一些让人吃惊的隐藏功能吗？\x01",
            "比如椅子可以自动旋转什么的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F2")

    TalkEnd(0xFE)
    Return()

    # Function_4_743 end

    def Function_5_7F6(): pass

    label("Function_5_7F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_8C0")

    ChrTalk(
        0xFE,
        (
            "你们是来向女神爱德丝请教\x01",
            "今天的事情该如何处理的吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "在这种时候来到礼拜堂，\x01",
            "你们也有什么烦恼吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C0")

    TalkEnd(0xFE)
    Return()

    # Function_5_7F6 end

    def Function_6_8C4(): pass

    label("Function_6_8C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_911")
    TalkBegin(0x8)

    ChrTalk(
        0xFE,
        (
            "真是的，外面好吵，\x01",
            "都没办法集中精神学习了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_911")

    Return()

    # Function_6_8C4 end

    def Function_7_912(): pass

    label("Function_7_912")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_9B2")

    ChrTalk(
        0xFE,
        (
            "不管怎么说\x01",
            "因为来到主日学校，\x01",
            "我意想不到的认真呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……不过，\x01",
            "今天外头很热闹哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "人家本来还想好好学习呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B2")

    TalkEnd(0xFE)
    Return()

    # Function_7_912 end

    def Function_8_9B6(): pass

    label("Function_8_9B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_A51")

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "接下来要去哪儿呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我是个逍遥自在、\x01",
            "漫无目的的流浪者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "随心所欲，走遍四方，\x01",
            "过着自由的旅行生活。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE5")

    label("loc_A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_AE5")

    ChrTalk(
        0xFE,
        "哟，早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "早上的祈祷\x01",
            "一定要集中精神呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样闭着眼睛的话，\x01",
            "就算导力停了都没有关系哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE5")

    TalkEnd(0xFE)
    Return()

    # Function_8_9B6 end

    def Function_9_AE9(): pass

    label("Function_9_AE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_BAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_B36")
    TurnDirection(0xFE, 0xC, 400)

    ChrTalk(
        0xFE,
        (
            "我说呆呆。\x01",
            "马上就完了，乖一点啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAC")

    label("loc_B36")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "好不容易来一次，\x01",
            "最好顺便去祈祷一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "空之女神啊……\x01",
            "谢谢您赐予的药。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BAC")

    Jump("loc_CCE")

    label("loc_BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_CCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_C36")

    ChrTalk(
        0xFE,
        (
            "教区长您调制的药相当有效，\x01",
            "在附近可是有口皆碑呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就是这种时候\x01",
            "才能感受到教会的恩德呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCE")

    label("loc_C36")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "不好意思，\x01",
            "我还想要取些药。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为肩部非常酸疼，\x01",
            "导致现在连头也疼起来了。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)

    label("loc_CCE")

    TalkEnd(0xFE)
    Return()

    # Function_9_AE9 end

    def Function_10_CD2(): pass

    label("Function_10_CD2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_D01")

    ChrTalk(
        0xFE,
        (
            "哥哥～\x01",
            "这个真没意思啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D9C")

    label("loc_D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_D2F")

    ChrTalk(
        0xFE,
        (
            "呜呜，妈妈～\x01",
            "我已经厌烦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D9C")

    label("loc_D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_D9C")

    ChrTalk(
        0xFE,
        "妈妈，没事吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想，\x01",
            "大概是因为肩膀的导力压变低了吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9C")

    TalkEnd(0xFE)
    Return()

    # Function_10_CD2 end

    def Function_11_DA0(): pass

    label("Function_11_DA0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_E4A")

    ChrTalk(
        0xFE,
        "呜～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为什么这些东西\x01",
            "摆放得这么混乱呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，我想将它们重新摆一下！\x02",
    )

    CloseMessageWindow()

    label("loc_E4A")

    TalkEnd(0xFE)
    Return()

    # Function_11_DA0 end

    def Function_12_E4E(): pass

    label("Function_12_E4E")

    Call(0, 13)
    Return()

    # Function_12_E4E end

    def Function_13_E53(): pass

    label("Function_13_E53")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1553")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x107, 57370, 1000, 52020, 90)
    SetChrPos(0x102, 56420, 1000, 52490, 90)
    SetChrPos(0x101, 56210, 1000, 51250, 90)
    SetChrPos(0x108, 57250, 1000, 50620, 45)
    TurnDirection(0xE, 0x107, 0)
    OP_6D(58050, 1000, 52120, 1000)

    ChrTalk(
        0x101,
        (
            "#006F教区长！\x01",
            "『塞姆里亚苔藓』采到了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "哦哦……真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "那太好了。\x01",
            "没想到你们这么快就采集到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F那、那个……\x01",
            "这样就可以做药了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "啊啊，当然可以了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "我到里面去配药，\x01",
            "你们在此稍等片刻吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(16290, 4000, 43670, 0)
    OP_67(0, 6330, -10000, 0)
    OP_6B(3090, 0)
    OP_6C(41000, 0)
    OP_6E(262, 0)
    SetChrPos(0xE, 15590, 4000, 43000, 90)
    SetChrPos(0xF, 15690, 4000, 41980, 45)
    OP_4A(0xF, 255)

    def lambda_103B():

        label("loc_103B")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_103B")

    QueueWorkItem2(0x0, 1, lambda_103B)

    def lambda_104C():

        label("loc_104C")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_104C")

    QueueWorkItem2(0x1, 1, lambda_104C)

    def lambda_105D():

        label("loc_105D")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_105D")

    QueueWorkItem2(0x2, 1, lambda_105D)

    def lambda_106E():

        label("loc_106E")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_106E")

    QueueWorkItem2(0x3, 1, lambda_106E)
    SetChrPos(0x101, 14110, 4000, 44580, 150)
    SetChrPos(0x102, 14410, 4000, 45600, 176)
    SetChrPos(0x107, 14890, 4000, 44370, 153)
    SetChrPos(0x108, 15390, 4000, 45540, 176)
    Sleep(500)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "#6P万物之根，源自七耀，\x01",
            "圣化苍金，汇聚于此。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6P女神圣礼，流转万物，\x01",
            "净化活性，相融相成。\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x0, "magic\\\\mg110_0.eff")
    PlayEffect(0x0, 0x0, 0xFF, 16260, 4100, 42980, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(
        0xE,
        "#6P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#6P嗯……这样就完成了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x107, 400)

    def lambda_1202():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1202)

    def lambda_1210():
        OP_6D(16290, 4000, 44670, 1000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1210)
    OP_8E(0xE, 0x3A48, 0xFA0, 0xAA32, 0x3E8, 0x0)
    TurnDirection(0xE, 0x107, 400)

    ChrTalk(
        0xE,
        "给，拿去吧。\x02",
    )

    CloseMessageWindow()
    OP_3F(0x365, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "亚鲁福灵药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x366, 1)
    OP_8F(0xE, 0x3A5C, 0xFA0, 0xA910, 0x3E8, 0x0)

    ChrTalk(
        0x107,
        "#560F哇……好漂亮的颜色！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F这个是喝的药吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "啊啊，是内服药。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "药的作用不在于清除毒的成分，\x01",
            "而是通过大幅度提高患者的免疫力\x01",
            "从而使之自然痊愈和康复。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哦……原来如此。\x01",
            "和东方的医术也有共通之处啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "这的确是源于东方的医术……\x01",
            "可以说两者都是一脉相承的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "好了。\x01",
            "快点把这药拿给那位伤者服用吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，好的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#061F教区长！\x01",
            "真的非常谢谢您！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)
    SetChrPos(0x101, 11980, 2000, 47970, 270)
    SetChrPos(0x102, 11980, 2000, 47970, 270)
    SetChrPos(0x107, 11980, 2000, 47970, 270)
    SetChrPos(0x108, 11980, 2000, 47970, 270)
    SetChrPos(0xE, 59070, 1000, 52160, 180)
    SetChrPos(0xF, 15690, 4000, 42960, 90)
    OP_4B(0xF, 255)
    OP_6D(11980, 2000, 47970, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_A2(0x557)
    OP_28(0x42, 0x1, 0x100)
    EventEnd(0x0)
    Jump("loc_3153")

    label("loc_1553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BE6")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x107, 57370, 1000, 52020, 90)
    SetChrPos(0x102, 56420, 1000, 52490, 90)
    SetChrPos(0x101, 56210, 1000, 51250, 90)
    TurnDirection(0xE, 0x107, 0)
    OP_4A(0xF, 255)
    OP_6D(58050, 1000, 52120, 1000)

    ChrTalk(
        0xE,
        "哎呀，这不是提妲吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "这么晚来这里有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#068F那、那个，教区长！\x02\x03",
            "请您一定要\x01",
            "救救阿加特大哥哥！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0xF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xE,
        "发生什么事了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F提、提妲，\x01",
            "稍微冷静一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F其实是……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们向教区长说明了\x01",
            "阿加特中毒倒下以及他处于昏迷症状一事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xF,
        "竟然出了这种事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "唔……\x01",
            "这下可伤脑筋了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F果、果然……\x01",
            "很难治疗这种毒吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "不，并不是这意思。\x01",
            "所幸的是七耀教会那种能解\x01",
            "所有神经毒药的配方至今仍流传下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "那种解药并非含有解毒的成分，\x01",
            "而是一种通过增强患者的抵抗力\x01",
            "而使其自然痊愈的药……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 400)

    ChrTalk(
        0xE,
        (
            "#1P琪爱拉修女，\x01",
            "那种解药好像……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "是的……\x01",
            "刚好药料已经用完了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#069F怎、怎么会……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F药料……\x01",
            "请问那是什么样的药料？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x107, 400)

    ChrTalk(
        0xE,
        (
            "是以古代文明的名字为典故，\x01",
            "被称为『塞姆里亚苔藓』的发光植物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "在蔡斯地区附近，\x01",
            "也只有卡鲁迪亚隧道的钟乳洞里\x01",
            "有这种珍稀的植物生长着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "以前我都是委托\x01",
            "游击士协会帮忙采集的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F卡鲁迪亚隧道……\x01",
            "就是我们来蔡斯时所通过的\x01",
            "那条超长地下隧道吧。\x02\x03",
            "#006F什～么嘛！\x01",
            "这样的话不就好办了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们马上前往钟乳洞\x01",
            "采集『塞姆里亚苔藓』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "什么……你们要去吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F那个，教区长。\x01",
            "姐姐他们是游击士协会的游击士呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "原来如此……\x01",
            "那么就交给你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "总之去钟乳洞前，\x01",
            "先去问问协会的负责人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "协会应该还保留着\x01",
            "以前采集时所做的记录。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，知道了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F谢谢您，我们就先告辞了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x551)
    OP_28(0x42, 0x1, 0x4)
    OP_28(0x42, 0x1, 0x8)
    OP_28(0x42, 0x1, 0x10)
    OP_4B(0xF, 255)
    EventEnd(0x0)
    Jump("loc_3153")

    label("loc_1BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1DC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1C67")

    ChrTalk(
        0xE,
        (
            "无论有什么烦恼，\x01",
            "都可以到礼拜堂来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "为市民服务\x01",
            "也是七耀教会的宗旨之一。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DC2")

    label("loc_1C67")

    OP_A2(0x6)

    ChrTalk(
        0xE,
        "哟，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "真是辛苦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F我们也要感谢教区长您呢。\x01",
            "　\x02\x03",
            "托教区长您的福，\x01",
            "阿加特他现在好了很多呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F承蒙您的照顾了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "不不不，\x01",
            "我也只是尽了应尽的义务罢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "以后无论有什么烦恼，\x01",
            "都可以到礼拜堂来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "为市民服务\x01",
            "也是七耀教会的宗旨之一。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC2")

    Jump("loc_3153")

    label("loc_1DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_218A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 1)), scpexpr(EXPR_END)), "loc_1E3B")

    ChrTalk(
        0xE,
        (
            "虽说身上的毒已经祛除了，\x01",
            "但他的身体状况还没有完全恢复。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "一定要叮嘱他\x01",
            "不要太过勉强啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2187")

    label("loc_1E3B")

    OP_A2(0x579)

    ChrTalk(
        0x107,
        (
            "#060F啊，教区长大人！\x02\x03",
            "太感谢您的药了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "哦，是提妲大小姐啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "后来他没什么事吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#050F药……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊、是的，没事了。\x02\x03",
            "阿加特大哥哥的药，\x01",
            "就是这位皮克塞恩教区长\x01",
            "给我们调制的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F是吗……\x02\x03",
            "……给别人添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F真是的，\x01",
            "还是不会道声谢呢～\x02\x03",
            "为什么不诚恳一些\x01",
            "向教区长表示感谢呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔， \x01",
            "你也不要总是顶嘴啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "哎呀～\x01",
            "竟然已经可以站起来走路了……\x01",
            "不愧是游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "但是，毕竟还没有完全恢复。\x01",
            "千万不要太勉强了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F啊，是自己的身体嘛。\x01",
            "我是最了解不过了。\x02\x03",
            "………………\x02\x03",
            "……说太多话了。\x01",
            "我们该走了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊。\x01",
            "确实是呢。\x02\x03",
            "那再见了，教区长大人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "嗯，再见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "提妲大小姐……\x01",
            "你也要好好加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F………………\x02\x03",
            "………是的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2187")

    Jump("loc_3153")

    label("loc_218A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_254C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 0)), scpexpr(EXPR_END)), "loc_220B")

    ChrTalk(
        0xE,
        (
            "我也会在这里\x01",
            "祈愿阿加特早日康复。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "再有什么事的话，\x01",
            "随时都可以过来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2549")

    label("loc_220B")

    OP_A2(0x578)

    ChrTalk(
        0xE,
        "哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "怎么样？药有效果吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是的，病情总算是稳住了。\x02\x03",
            "中央工房的米妮亚姆医生说，\x01",
            "阿加特兄已经脱离危险期了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "是吗？渡过危险期了？\x01",
            "这样一来我也就稍稍安心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，我想没问题的。\x02\x03",
            "因为病人\x01",
            "可是那个阿加特呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我也是这么想的。\x02\x03",
            "要是比起体力的话，\x01",
            "他一定和金先生有一拼吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F不过，\x01",
            "这次真的是麻烦教区长您了。\x02\x03",
            "那么晚突然跑过来，\x01",
            "还让您给我们配药……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "那个时候，\x01",
            "提妲大小姐那么紧张……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "一贯内向的那个孩子\x01",
            "也会那样拼命地诉说自己的请求，\x01",
            "我想不管是谁看到都会帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "我也会在这里\x01",
            "祈愿阿加特早日康复。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，非常感谢您。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F真是帮了我们大忙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "呵呵，再有什么事的话，\x01",
            "随时都可以过来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2549")

    Jump("loc_3153")

    label("loc_254C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2739")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 7)), scpexpr(EXPR_END)), "loc_2633")

    ChrTalk(
        0xE,
        (
            "这种解药并非含有解毒的成分，\x01",
            "而是一种通过增强患者抵抗力使其自然痊愈的药……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "对于未知的毒药\x01",
            "应该也能起到一些作用吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "好了，你们赶快去吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2736")

    label("loc_2633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_269A")

    ChrTalk(
        0xE,
        (
            "那么，我们在这边\x01",
            "先做一下调药的准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "钟乳洞里面十分危险。\x01",
            "你们千万要小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2736")

    label("loc_269A")


    ChrTalk(
        0xE,
        (
            "总之去钟乳洞前，\x01",
            "先去问问协会的负责人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "协会应该还保留着\x01",
            "以前采集时所做的记录。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2736")

    Jump("loc_3153")

    label("loc_2739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2821")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_27A7")

    ChrTalk(
        0xE,
        "事态的发展似乎很严重。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "正是在这种非常时期，\x01",
            "我们更要振作起来才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_281E")

    label("loc_27A7")

    OP_A2(0x6)

    ChrTalk(
        0xE,
        "事态的发展似乎很严重。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "虽然目前还没收到有伤者的报告，\x01",
            "但最好还是准备些药物比较稳妥……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_281E")

    Jump("loc_3153")

    label("loc_2821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_28E0")

    ChrTalk(
        0xE,
        (
            "……在时间的洪流中，\x01",
            "作为『钟表之城』的蔡斯市\x01",
            "已经完成了它伟大的使命。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "以蔡斯为中心生产的导力器\x01",
            "在各地全面普及，\x01",
            "给利贝尔王国带来一场导力革命……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3153")

    label("loc_28E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2934")

    ChrTalk(
        0xE,
        "空之女神爱德丝啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "请给予广大民众\x01",
            "保佑和引导……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3153")

    label("loc_2934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_2B2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_29F6")

    ChrTalk(
        0xE,
        (
            "虽然我也很明白\x01",
            "修女琪爱拉那份要好好爱护\x01",
            "礼拜堂这种祈祷之地的心情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "但我想比起别的，\x01",
            "教会不就该是个\x01",
            "让有困难的人可以安心落脚的地方吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B2B")

    label("loc_29F6")

    OP_A2(0x6)

    ChrTalk(
        0xE,
        (
            "向人们提供传统医疗的服务\x01",
            "也是礼拜堂的重要职责。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "除了医疗，\x01",
            "还有大家都头疼的小孩教育问题……\x01",
            "教会的使命有很多啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "对社会做出贡献是\x01",
            "未来的七耀教会必须承担的责任。\x01",
            "我是这样想的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B2B")

    Jump("loc_3153")

    label("loc_2B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2DD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2BC3")

    ChrTalk(
        0xE,
        (
            "如果可以的话，\x01",
            "就经常来找我谈谈心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "遇到什么麻烦的事情，\x01",
            "也可以尽管来找我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD6")

    label("loc_2BC3")

    OP_A2(0x6)

    ChrTalk(
        0xE,
        "早上好啊，提妲大小姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "不……\x01",
            "你什么都不用说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "总之昨晚真是一团糟啊\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F呜……\x01",
            "对不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "哎呀，你用不着道歉啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "为了进步试验是必不可少的，\x01",
            "而试验也往往伴随着失败。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "这个城市的人们\x01",
            "对此都十分地理解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "提妲，\x01",
            "今后你也要好好协助博士哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060F……是，教区长大人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "如果可以的话，\x01",
            "就经常来找我谈谈心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "遇到什么麻烦的事情，\x01",
            "也可以尽管来找我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DD6")

    Jump("loc_3153")

    label("loc_2DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_30A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2E63")

    ChrTalk(
        0xE,
        (
            "要是有用得着的地方\x01",
            "就尽管到这里来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "教会并不是\x01",
            "只为了祈祷而设立的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_309F")

    label("loc_2E63")

    OP_A2(0x6)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E9E")

    ChrTalk(
        0xE,
        "嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "这个小姑娘\x01",
            "不就是提妲大小姐吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EEF")

    label("loc_2E9E")


    ChrTalk(
        0xE,
        "哦哦，提妲大小姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "我觉得好像有很久\x01",
            "都没有见到过你了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EEF")


    ChrTalk(
        0x107,
        "#060F您好，教区长大人！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "你也和爷爷一样\x01",
            "总是一天到晚地忙碌呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "不过，工作告一段落之后，\x01",
            "还得来主日学校学习哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "你毕竟还是个孩子啊。\x01",
            "多花点时间和同龄的朋友\x01",
            "一起玩耍也是很有必要的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F嗯，是的。\x01",
            "我明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "嗯，如果需要什么帮助的话，\x01",
            "就尽管到这里来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "教会并不是只为了\x01",
            "祈祷而设立的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_309F")

    Jump("loc_3153")

    label("loc_30A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3153")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_30EB")

    ChrTalk(
        0xE,
        (
            "当然，\x01",
            "来祈祷的话更是欢迎啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3153")

    label("loc_30EB")

    OP_A2(0x6)

    ChrTalk(
        0xE,
        "欢迎来到七耀教会。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "从恋爱的烦恼到胃疼，\x01",
            "任何事情都可以找我商量。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3153")

    TalkEnd(0xE)
    Return()

    # Function_13_E53 end

    def Function_14_3157(): pass

    label("Function_14_3157")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_31F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_31AD")

    ChrTalk(
        0xFE,
        (
            "今后也欢迎\x01",
            "随时光临教会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只不过， \x01",
            "来了就请好好祈祷。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F5")

    label("loc_31AD")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        "啊，欢迎来到七耀教会。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有什么事\x01",
            "就请尽管说吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31F5")

    Jump("loc_3AF7")

    label("loc_31F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_32D6")

    ChrTalk(
        0xFE,
        (
            "药似乎很有效果呢。\x01",
            "不愧是皮克塞恩教区长大人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "拯救别人的生命，\x01",
            "果然是件了不起的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我重新考虑了一下，\x01",
            "这样做对于传播教会的智慧\x01",
            "也是很重要的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_32D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_3495")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3398")

    ChrTalk(
        0xFE,
        (
            "像昨天晚上那种情况，\x01",
            "我不知道教区长的想法\x01",
            "到底是不是正确的呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……我还是认为\x01",
            "过来拿药的时候才顺便祈祷一下，\x01",
            "这种做法不能原谅啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3492")

    label("loc_3398")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "像昨天晚上那种情况，\x01",
            "我不知道教区长的想法\x01",
            "到底是不是正确的呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正因为得到了大家信赖，\x01",
            "在紧急时刻，\x01",
            "大家才会来拜托教会吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……唉，不过我还是认为\x01",
            "过来拿药的时候才顺便祈祷一下，\x01",
            "这种做法不能原谅啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3492")

    Jump("loc_3AF7")

    label("loc_3495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_361D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 7)), scpexpr(EXPR_END)), "loc_3502")

    ChrTalk(
        0xFE,
        (
            "请不要耽误时间，\x01",
            "尽快把药送过去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们也会祈祷患者\x01",
            "能够尽快恢复健康。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_361A")

    label("loc_3502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_358B")

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "难道你们已经找到材料了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "教区长大人已经做好调药的准备了。\x01",
            "请把材料交给教区长吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_361A")

    label("loc_358B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_END)), "loc_35D1")

    ChrTalk(
        0xFE,
        (
            "我们先进行着\x01",
            "调制药水的准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "各位，路上请当心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_361A")

    label("loc_35D1")


    ChrTalk(
        0xFE,
        "啊，各位……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "都已经夜深了，\x01",
            "来教会有什么指教吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_361A")

    Jump("loc_3AF7")

    label("loc_361D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_36A9")

    ChrTalk(
        0xFE,
        (
            "工房那边\x01",
            "似乎出了什么事呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过详细的情况\x01",
            "我还不太清楚。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_36A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_37DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3722")

    ChrTalk(
        0xFE,
        (
            "为什么今天\x01",
            "城里那么吵闹呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "孩子们好像也是\x01",
            "一副坐立不安的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37D8")

    label("loc_3722")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "今天主日学校的课\x01",
            "讲的是这个城市的历史。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "从刚才开始就觉得城里就很吵闹……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "孩子们好像也是\x01",
            "一副坐立不安的样子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37D8")

    Jump("loc_3AF7")

    label("loc_37DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3863")

    ChrTalk(
        0xFE,
        (
            "刚才还以为是有人来祈祷呢，\x01",
            "原来是来取药的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "教区长应该对他们说说\x01",
            "让他们能更常来祈祷……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_3863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_39F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3903")

    ChrTalk(
        0xFE,
        (
            "我想教会毕竟是个\x01",
            "怀着虔诚的心祈祷的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样下去的话，\x01",
            "教会都要变成观光地或者药店了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39ED")

    label("loc_3903")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "蔡斯的市民们\x01",
            "每个人都很忙\x01",
            "很少有人会来教会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "教区长对于那些\x01",
            "来教会却做别的事情的人\x01",
            "也会热情地接待……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过我还是觉得\x01",
            "教会毕竟是个怀着虔诚的心祈祷的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39ED")

    Jump("loc_3AF7")

    label("loc_39F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3AA9")

    ChrTalk(
        0xFE,
        "昨晚真是不得了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "中央工房\x01",
            "好像已经一团糟了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在那种时候\x01",
            "就应该静下心来祈祷……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_3AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3AF7")

    ChrTalk(
        0xFE,
        "欢迎来到七耀教会。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "请各位\x01",
            "虔诚地祈祷一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AF7")

    TalkEnd(0xFE)
    Return()

    # Function_14_3157 end

    SaveToFile()

Try(main)
