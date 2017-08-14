from ED6ScenarioHelper import *

def main():
    # 封印区域

    CreateScenaFile(
        FileName            = 'C4300   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4300.x',
        MapIndex            = 216,
        MapDefaultBGM       = "ed60035",
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
        '雪拉扎德',                             # 9
        '奥利维尔',                             # 10
        '科洛丝',                               # 11
        '阿加特',                               # 12
        '提妲',                                 # 13
        '金',                                   # 14
        '拉赛尔博士',                           # 15
        '基库',                                 # 16
        '特务兵',                               # 17
        '特务兵',                               # 18
        '特务兵',                               # 19
        '特务兵',                               # 20
        '特务兵',                               # 21
        '特务兵',                               # 22
        '特务兵',                               # 23
        '特务兵',                               # 24
        '特务兵',                               # 25
        '理查德上校',                           # 26
        '洛伦斯少尉',                           # 27
        '机器',                                 # 28
        '机器',                                 # 29
        '卡西乌斯',                             # 30
        '卡西乌斯',                             # 31
        '卡西乌斯',                             # 32
        '卡西乌斯',                             # 33
        '卡西乌斯',                             # 34
        '卡西乌斯',                             # 35
        '卡西乌斯',                             # 36
        '卡西乌斯',                             # 37
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
        'ED6_DT07/CH00020 ._CH',             # 00
        'ED6_DT07/CH00030 ._CH',             # 01
        'ED6_DT07/CH00040 ._CH',             # 02
        'ED6_DT06/CH20053 ._CH',             # 03
        'ED6_DT07/CH00060 ._CH',             # 04
        'ED6_DT07/CH00070 ._CH',             # 05
        'ED6_DT07/CH02020 ._CH',             # 06
        'ED6_DT07/CH02320 ._CH',             # 07
        'ED6_DT07/CH02030 ._CH',             # 08
        'ED6_DT07/CH02200 ._CH',             # 09
        'ED6_DT07/CH01610 ._CH',             # 0A
        'ED6_DT09/CH10941 ._CH',             # 0B
        'ED6_DT09/CH10940 ._CH',             # 0C
        'ED6_DT07/CH00260 ._CH',             # 0D
        'ED6_DT07/CH00262 ._CH',             # 0E
        'ED6_DT07/CH00270 ._CH',             # 0F
        'ED6_DT07/CH00272 ._CH',             # 10
        'ED6_DT06/CH20051 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT07/CH00020P._CP',             # 00
        'ED6_DT07/CH00030P._CP',             # 01
        'ED6_DT07/CH00040P._CP',             # 02
        'ED6_DT06/CH20053P._CP',             # 03
        'ED6_DT07/CH00060P._CP',             # 04
        'ED6_DT07/CH00070P._CP',             # 05
        'ED6_DT07/CH02020P._CP',             # 06
        'ED6_DT07/CH02320P._CP',             # 07
        'ED6_DT07/CH02030P._CP',             # 08
        'ED6_DT07/CH02200P._CP',             # 09
        'ED6_DT07/CH01610P._CP',             # 0A
        'ED6_DT09/CH10941P._CP',             # 0B
        'ED6_DT09/CH10940P._CP',             # 0C
        'ED6_DT07/CH00260P._CP',             # 0D
        'ED6_DT07/CH00262P._CP',             # 0E
        'ED6_DT07/CH00270P._CP',             # 0F
        'ED6_DT07/CH00272P._CP',             # 10
        'ED6_DT06/CH20051P._CP',             # 11
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 38290,
        TriggerZ            = 0,
        TriggerY            = -3310,
        TriggerRange        = 1000,
        ActorX              = 38290,
        ActorZ              = 1200,
        ActorY              = -3310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4FE",          # 00, 0
        "Function_1_54A",          # 01, 1
        "Function_2_594",          # 02, 2
        "Function_3_5AA",          # 03, 3
        "Function_4_65F",          # 04, 4
        "Function_5_736",          # 05, 5
        "Function_6_7D0",          # 06, 6
        "Function_7_860",          # 07, 7
        "Function_8_8DF",          # 08, 8
        "Function_9_93F",          # 09, 9
        "Function_10_AF5",         # 0A, 10
        "Function_11_B3B",         # 0B, 11
        "Function_12_B5E",         # 0C, 12
        "Function_13_19E4",        # 0D, 13
        "Function_14_1A76",        # 0E, 14
        "Function_15_1B12",        # 0F, 15
        "Function_16_1B8F",        # 10, 16
        "Function_17_2D26",        # 11, 17
        "Function_18_336B",        # 12, 18
        "Function_19_348A",        # 13, 19
    )


    def Function_0_4FE(): pass

    label("Function_0_4FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_515")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 12)

    label("loc_515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_528")
    SetMapFlags(0x40000000)
    OP_A3(0x3FB)
    Event(0, 16)

    label("loc_528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_538")
    Call(0, 18)

    label("loc_538")

    OP_51(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_4FE end

    def Function_1_54A(): pass

    label("Function_1_54A")

    LoadEffect(0x5, "map\\\\mp027_00.eff")
    PlayEffect(0x5, 0x6, 0xFF, 38290, 1200, -3310, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_54A end

    def Function_2_594(): pass

    label("Function_2_594")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_594")

    label("loc_5A9")

    Return()

    # Function_2_594 end

    def Function_3_5AA(): pass

    label("Function_3_5AA")

    TalkBegin(0x8)

    ChrTalk(
        0x8,
        (
            "#022F上校如此不择手段\x01",
            "想要得到的『辉之环』究竟是……\x02\x03",
            "不管怎样，\x01",
            "应该不是个受欢迎的东西。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_3_5AA end

    def Function_4_65F(): pass

    label("Function_4_65F")

    TalkBegin(0x9)

    ChrTalk(
        0x9,
        (
            "#035F在地下企图做的\x01",
            "肯定不是什么好事，\x01",
            "前人的经验这么告诉我们的。\x02\x03",
            "#030F早点把上校逼入绝境，\x01",
            "然后华丽地演奏最终乐章吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_4_65F end

    def Function_5_736(): pass

    label("Function_5_736")

    TalkBegin(0xA)

    ChrTalk(
        0xA,
        (
            "#042F祖母大人有尤莉亚中尉跟随，\x01",
            "肯定不会有事的。\x02\x03",
            "我相信她们，\x01",
            "所以现在要前进……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_5_736 end

    def Function_6_7D0(): pass

    label("Function_6_7D0")

    TalkBegin(0xB)

    ChrTalk(
        0xB,
        (
            "#050F如何，路线清楚了吗？\x02\x03",
            "尽快找到上校，\x01",
            "然后狠狠教训他一顿吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_6_7D0 end

    def Function_7_860(): pass

    label("Function_7_860")

    TalkBegin(0xC)

    ChrTalk(
        0xC,
        (
            "#063F艾丝蒂尔姐姐，\x01",
            "约修亚哥哥……\x02\x03",
            "如果遇到什么危险，\x01",
            "可要立刻回到这里来哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_7_860 end

    def Function_8_8DF(): pass

    label("Function_8_8DF")

    TalkBegin(0xD)

    ChrTalk(
        0xD,
        (
            "#070F这里就由我『不动金』来守护。\x02\x03",
            "你们就放心\x01",
            "去前方探路吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xD)
    Return()

    # Function_8_8DF end

    def Function_9_93F(): pass

    label("Function_9_93F")

    TalkBegin(0xE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",            # 0
            "改造·换钱\x01",      # 1
            "购买道具\x01",        # 2
            "更换队员\x01",        # 3
            "取消\x01",            # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BE")
    Call(0, 10)
    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_9BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D8")
    Call(0, 11)
    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_9D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2C")
    EventBegin(0x0)
    OP_4A(0xE, 255)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    Call(0, 17)
    OP_4B(0xE, 255)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_4B(0xA, 255)
    OP_4B(0xB, 255)
    OP_4B(0xC, 255)
    OP_4B(0xD, 255)
    EventEnd(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_A2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A3D")
    TalkEnd(0xE)
    Return()

    label("loc_A3D")


    ChrTalk(
        0xE,
        (
            "#100F如果需要改造导力器的话，\x01",
            "说一声就行了。\x02\x03",
            "我从王都的店铺里拿来了一些道具，\x01",
            "可以代其进行销售。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    # Function_9_93F end

    def Function_10_AF5(): pass

    label("Function_10_AF5")


    ChrTalk(
        0xE,
        (
            "#100F来吧，我会给你们\x01",
            "比这边的工房更好的服务。\x02",
        )
    )

    CloseMessageWindow()
    OP_0D()
    OP_A9(0x6A)
    Return()

    # Function_10_AF5 end

    def Function_11_B3B(): pass

    label("Function_11_B3B")


    ChrTalk(
        0xE,
        "#100F有什么需要的吗？\x02",
    )

    CloseMessageWindow()
    OP_0D()
    OP_A9(0x6B)
    Return()

    # Function_11_B3B end

    def Function_12_B5E(): pass

    label("Function_12_B5E")

    EventBegin(0x0)
    LoadEffect(0x0, "battle\\\\btbomb00.eff")
    FadeToBright(2000, 0)
    OP_6D(38000, 17050, -14020, 0)
    OP_67(0, 4150, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(418, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x19, 34660, 0, -13430, 270)
    SetChrPos(0x1A, 35900, 0, -15200, 270)
    SetChrPos(0x10, 36160, 0, -11160, 270)
    SetChrPos(0x11, 37460, 0, -14780, 270)
    SetChrPos(0x12, 37460, 0, -13340, 270)
    SetChrPos(0x13, 36220, 0, -17220, 270)
    SetChrPos(0x14, 37460, 0, -12070, 270)
    SetChrPos(0x15, 39500, 0, -13290, 270)
    SetChrPos(0x16, 39500, 0, -14730, 270)
    SetChrPos(0x17, 37460, 0, -16090, 270)
    FadeToBright(2000, 0)
    OP_6D(38000, 2550, -14020, 5000)

    ChrTalk(
        0x10,
        "#5P这、这里是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P这、这种地方\x01",
            "竟然真的存在……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D28():
        OP_6D(19210, 0, -13380, 3500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_D28)

    def lambda_D40():
        OP_6C(135000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_D40)
    Sleep(2000)

    def lambda_D55():
        OP_67(0, 10910, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D55)

    def lambda_D6D():
        OP_6E(514, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_D6D)
    Sleep(4000)
    Fade(1000)
    OP_6D(36830, 0, -13980, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(135000, 0)
    OP_6E(332, 0)
    OP_0D()

    ChrTalk(
        0x19,
        (
            "#115F#6P呵呵，规模比预想的还要大啊。\x02\x03",
            "#110F洛伦斯少尉，\x01",
            "带我到最深处去好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#281F#5P明白……\x02",
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1B, 0x4)
    SetChrFlags(0x1C, 0x4)
    SetChrPos(0x1B, 18010, 20220, 5070, 108)
    SetChrPos(0x1C, 16410, 20220, -120, 108)

    def lambda_EBE():

        label("loc_EBE")

        TurnDirection(0xFE, 0x1A, 0)
        OP_48()
        Jump("loc_EBE")

    QueueWorkItem2(0x1B, 3, lambda_EBE)

    def lambda_ECF():

        label("loc_ECF")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_ECF")

    QueueWorkItem2(0x1C, 3, lambda_ECF)
    ClearChrFlags(0x1B, 0x1)
    ClearChrFlags(0x1C, 0x1)

    def lambda_EEA():
        OP_8F(0xFE, 0x7A76, 0x0, 0xFFFFD03A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_EEA)
    Sleep(300)

    def lambda_F0A():
        OP_8F(0xFE, 0x79FE, 0x0, 0xFFFFC2C0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_F0A)
    TurnDirection(0x1A, 0x1B, 400)

    def lambda_F2C():
        OP_6D(32409, 0, -13750, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_F2C)

    def lambda_F44():
        OP_6C(90000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_F44)

    def lambda_F54():
        OP_67(0, 7160, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_F54)
    OP_8E(0x1A, 0x869C, 0x0, 0xFFFFC482, 0x1388, 0x0)

    def lambda_F80():

        label("loc_F80")

        TurnDirection(0xFE, 0x1C, 0)
        OP_48()
        Jump("loc_F80")

    QueueWorkItem2(0x1A, 1, lambda_F80)

    def lambda_F91():

        label("loc_F91")

        TurnDirection(0xFE, 0x1B, 0)
        OP_48()
        Jump("loc_F91")

    QueueWorkItem2(0x19, 1, lambda_F91)
    SetChrChipByIndex(0x1A, 13)
    SetChrChipByIndex(0x19, 15)
    OP_22(0xE7, 0x0, 0x64)
    WaitChrThread(0x1B, 0x1)
    SetChrChipByIndex(0x1B, 12)
    SetChrFlags(0x1B, 0x1)
    SetChrFlags(0x1C, 0x1)

    def lambda_FC5():

        label("loc_FC5")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_FC5")

    QueueWorkItem2(0x1B, 0, lambda_FC5)
    TurnDirection(0x1B, 0x19, 0)
    WaitChrThread(0x1C, 0x1)
    SetChrChipByIndex(0x1C, 12)

    def lambda_FE9():

        label("loc_FE9")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_FE9")

    QueueWorkItem2(0x1C, 0, lambda_FE9)
    TurnDirection(0x1C, 0x1A, 0)
    TurnDirection(0x10, 0x1B, 0)
    TurnDirection(0x11, 0x1B, 0)
    TurnDirection(0x12, 0x1B, 0)
    TurnDirection(0x13, 0x1B, 0)
    TurnDirection(0x14, 0x1B, 0)
    TurnDirection(0x15, 0x1B, 0)
    TurnDirection(0x16, 0x1B, 0)
    TurnDirection(0x17, 0x1B, 0)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_10CB():
        OP_94(0x1, 0xFE, 0xB4, 0x44C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_10CB)

    def lambda_10E1():
        OP_94(0x1, 0xFE, 0xB4, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_10E1)
    Sleep(50)

    def lambda_10FC():
        OP_94(0x1, 0xFE, 0xB4, 0x2BC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_10FC)

    def lambda_1112():
        OP_94(0x1, 0xFE, 0xB4, 0x44C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1112)
    Sleep(100)

    def lambda_112D():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_112D)

    def lambda_1143():
        OP_94(0x1, 0xFE, 0xB4, 0x514, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1143)
    Sleep(50)

    def lambda_115E():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_115E)
    Sleep(50)

    def lambda_1179():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1179)
    WaitChrThread(0x0, 0x2)

    ChrTalk(
        0x10,
        "哦啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "机、机械怪物！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#110F#5P呵呵……\x01",
            "是古代的人形兵器啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_120A():
        OP_6C(70000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_120A)
    OP_6B(2900, 1500)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x19, 0x40)

    def lambda_122D():
        OP_6D(30310, 0, -13620, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_122D)

    def lambda_1245():
        OP_6B(2500, 1000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_1245)

    def lambda_1255():
        OP_67(0, 5500, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1255)

    def lambda_126D():
        OP_6C(42000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_126D)
    OP_9F(0x1D, 0xFF, 0xC8, 0xC8, 0xC8, 0x0)
    OP_9F(0x1E, 0xFF, 0x96, 0x96, 0x96, 0x0)
    OP_9F(0x1F, 0xFF, 0x64, 0x64, 0x64, 0x0)
    OP_9F(0x20, 0xFF, 0x32, 0x32, 0x32, 0x0)
    OP_9F(0x21, 0xC8, 0xFF, 0xFF, 0xC8, 0x0)
    OP_9F(0x22, 0x96, 0xFF, 0xFF, 0x96, 0x0)
    OP_9F(0x23, 0x64, 0xFF, 0xFF, 0x64, 0x0)
    OP_9F(0x24, 0x32, 0xFF, 0xFF, 0x32, 0x0)
    OP_43(0x11, 0x0, 0x0, 0xD)
    Sleep(530)
    OP_22(0x1F5, 0x0, 0x64)
    PlayEffect(0x8, 0xFF, 0xFF, 31350, 1500, -12230, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_44(0x1B, 0xFF)
    Sleep(150)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x8, 0xFF, 0xFF, 31230, 1500, -15680, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_44(0x1C, 0xFF)
    Sleep(900)

    def lambda_1367():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_1367)

    def lambda_1377():
        OP_6C(19000, 2000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_1377)

    def lambda_1387():
        OP_67(0, 7160, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1387)

    def lambda_139F():
        OP_6D(30310, 0, -13620, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_139F)
    SetChrFlags(0x1B, 0x4)
    PlayEffect(0x0, 0xFF, 0x1B, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_13F1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_13F1)

    def lambda_1403():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1403)
    Sleep(300)
    SetChrFlags(0x1C, 0x4)
    PlayEffect(0x0, 0xFF, 0x1C, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_145D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_145D)

    def lambda_146F():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_146F)
    Sleep(1500)

    def lambda_148F():
        OP_99(0xFE, 0x9, 0xB, 0x640)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_148F)

    def lambda_149F():
        OP_96(0xFE, 0x7AE4, 0x0, 0xFFFFC40A, 0x2BC, 0xFA0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_149F)
    SetChrFlags(0x19, 0x800)

    def lambda_14C2():
        OP_99(0xFE, 0x5, 0xB, 0x7D0)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_14C2)
    WaitChrThread(0x19, 0x3)
    SetChrChipByIndex(0x19, 15)
    SetChrSubChip(0x19, 0)
    Sleep(500)

    ChrTalk(
        0x10,
        "好、好厉害……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "那样的怪物一刀就……\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    SetChrFlags(0x19, 0x20)
    TurnDirection(0x19, 0x1A, 400)

    ChrTalk(
        0x19,
        (
            "#111F#5P呵呵，\x01",
            "还是你的反应要快一些啊。\x02\x03",
            "如果你真的出尽全力，\x01",
            "我也许真的没有什么胜算。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    SetChrFlags(0x1A, 0x20)
    TurnDirection(0x1A, 0x19, 400)

    def lambda_15CD():

        label("loc_15CD")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_15CD")

    QueueWorkItem2(0x1A, 3, lambda_15CD)

    ChrTalk(
        0x1A,
        (
            "#280F#6P您过谦了。\x02\x03",
            "不愧是继承了『剑圣』\x01",
            "之技的神速拔剑法……\x02\x03",
            "终于可以一睹其风采了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#115F#5P呼，还不成熟。\x02\x03",
            "#116F不过，时代正在迅速地远去，\x01",
            "不能继续等待不成熟的人停滞不前啊。\x02\x03",
            "不管怎样，也只有靠这笨拙的双手\x01",
            "来为王国的明天开拓出一个新天地了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A, 0)
    SetChrChipByIndex(0x1A, 9)
    ClearChrFlags(0x1A, 0x20)
    ClearChrFlags(0x1A, 0x800)

    def lambda_17B5():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_17B5)

    def lambda_17C5():
        OP_6D(35740, 0, -13960, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_17C5)
    ClearChrFlags(0x19, 0x20)
    ClearChrFlags(0x19, 0x800)
    SetChrChipByIndex(0x19, 8)
    OP_8E(0x19, 0x7B66, 0x0, 0xFFFFCBDA, 0x7D0, 0x0)
    OP_8C(0x19, 90, 400)
    WaitChrThread(0x0, 0x1)

    ChrTalk(
        0x19,
        (
            "#114F#5P各位勇士！\x01",
            "通向巨硕之力地道路已经开启！\x02\x03",
            "我们所热爱的利贝尔\x01",
            "即将迎来光辉的黎明！\x02\x03",
            "我期待各位的表现！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5P明白！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5P我们特务兵会团结一致，\x01",
            "竭尽全力效忠上校！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    SetMessageWindowPos(40, 60, -1, -1)
    SetChrName("特务兵们")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#3S为利贝尔的荣誉而战！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    Sleep(400)
    SetMessageWindowPos(150, 100, -1, -1)
    SetChrName("特务兵们")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5S为利贝尔的荣誉而战！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    Sleep(2000)
    OP_22(0xD, 0x0, 0x64)
    Sleep(3000)
    SetMapFlags(0x100000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_B5E end

    def Function_13_19E4(): pass

    label("Function_13_19E4")

    OP_43(0x1A, 0x1, 0x0, 0xE)
    Sleep(70)
    OP_43(0x1D, 0x1, 0x0, 0xE)
    OP_43(0x19, 0x1, 0x0, 0xF)
    Sleep(70)
    OP_43(0x1E, 0x1, 0x0, 0xE)
    OP_43(0x21, 0x1, 0x0, 0xF)
    Sleep(70)
    OP_43(0x1F, 0x1, 0x0, 0xE)
    OP_43(0x22, 0x1, 0x0, 0xF)
    Sleep(70)
    OP_43(0x20, 0x1, 0x0, 0xE)
    OP_43(0x23, 0x1, 0x0, 0xF)
    Sleep(70)
    OP_43(0x24, 0x1, 0x0, 0xF)
    WaitChrThread(0x20, 0x1)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    WaitChrThread(0x24, 0x1)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    Return()

    # Function_13_19E4 end

    def Function_14_1A76(): pass

    label("Function_14_1A76")

    SetChrChipByIndex(0xFE, 13)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, 34460, 0, -15230, 270)

    def lambda_1A9C():

        label("loc_1A9C")

        TurnDirection(0xFE, 0x1C, 0)
        OP_48()
        Jump("loc_1A9C")

    QueueWorkItem2(0xFE, 3, lambda_1A9C)
    OP_96(0xFE, 0x8246, 0x0, 0xFFFFC31A, 0x3E8, 0x2328)
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 14)
    SetChrFlags(0xFE, 0x800)

    def lambda_1AD2():
        OP_99(0xFE, 0x0, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1AD2)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    OP_96(0xFE, 0x7F6B, 0x4B0, 0xFFFFC360, 0x4E2, 0x1388)
    OP_8F(0xFE, 0x7274, 0x96, 0xFFFFC41E, 0x32C8, 0x0)
    Return()

    # Function_14_1A76 end

    def Function_15_1B12(): pass

    label("Function_15_1B12")

    ClearChrFlags(0x1A, 0x800)
    SetChrChipByIndex(0xFE, 15)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, 34660, 0, -13430, 270)

    def lambda_1B3D():

        label("loc_1B3D")

        TurnDirection(0xFE, 0x1B, 0)
        OP_48()
        Jump("loc_1B3D")

    QueueWorkItem2(0xFE, 3, lambda_1B3D)
    OP_8F(0xFE, 0x8282, 0x0, 0xFFFFCFE0, 0x1388, 0x0)
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 16)
    SetChrFlags(0xFE, 0x800)

    def lambda_1B70():
        OP_99(0xFE, 0x0, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_1B70)
    OP_8E(0xFE, 0x70D0, 0x96, 0xFFFFD03A, 0x2AF8, 0x0)
    Return()

    # Function_15_1B12 end

    def Function_16_1B8F(): pass

    label("Function_16_1B8F")

    EventBegin(0x0)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x2, 0xFF)
    AddParty(0x1, 0xFF)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_4A(0xE, 255)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    SetChrPos(0x101, 37080, 0, -15050, 270)
    SetChrPos(0x102, 37170, 0, -12980, 270)
    SetChrPos(0xE, 38760, 0, -14790, 258)
    SetChrPos(0xB, 37850, 0, -16410, 222)
    SetChrPos(0xC, 39400, 0, -15590, 222)
    SetChrPos(0x9, 39020, 0, -12220, 293)
    SetChrPos(0x8, 39710, 0, -13330, 262)
    SetChrPos(0xD, 40420, 0, -14130, 260)
    SetChrPos(0xA, 38260, 0, -13640, 265)
    SetChrPos(0xF, 40960, 500, -20390, 314)
    OP_6D(80, 0, 35850, 0)
    OP_67(0, 9440, -34740, 0)
    OP_6B(1000, 0)
    OP_6C(0, 0)
    OP_6E(663, 0)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    FadeToBright(2000, 0)

    def lambda_1CF7():
        OP_6D(50, 0, -20330, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CF7)
    Sleep(3000)

    def lambda_1D14():
        OP_6C(77000, 11000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D14)
    Sleep(7000)

    def lambda_1D29():
        OP_6D(39590, 0, -14310, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D29)

    def lambda_1D41():
        OP_67(0, 22340, -34740, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1D41)

    def lambda_1D59():
        OP_6E(343, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1D59)
    Sleep(6000)

    ChrTalk(
        0x101,
        "#580F这、这里是什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F古代塞姆里亚文明的遗迹……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#102F#5P看来这里是相当古老的遗迹啊，\x01",
            "而且竟然还没有湮灭掉……\x02\x03",
            "和『四轮之塔』不同，\x01",
            "这里的装置还在继续运转着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#057F而且还不只是装置在运转吧。\x02\x03",
            "我注意到这个地方\x01",
            "还有许多怪物在成群地蠕动着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#065F#2P啊，呀啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#022F那边的建筑材料是最近才拿进来的。\x01",
            "　\x02\x03",
            "是根据上校的指示去修建的吗……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#030F应该没错吧。\x02\x03",
            "#035F在这样深的地下施工，\x01",
            "那些黑衣男子一定很辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#043F不过这个巨大的遗迹\x01",
            "远远超出了我的想象……\x02\x03",
            "如果不用心去探索，\x01",
            "肯定很快就会被困在里面的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#074F嗯……\x02\x03",
            "#072F我们最好在这里将人员分为\x01",
            "探索组和待机组。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20C8():
        OP_6E(300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_20C8)

    def lambda_20D8():
        OP_6C(90000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20D8)

    def lambda_20E8():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_20E8)

    def lambda_20F6():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_20F6)
    Sleep(100)

    def lambda_2109():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2109)
    Sleep(100)

    def lambda_211C():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_211C)

    def lambda_212A():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_212A)
    Sleep(100)

    def lambda_213D():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_213D)

    def lambda_214B():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_214B)
    TurnDirection(0x102, 0xD, 400)
    TurnDirection(0x101, 0xD, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        "#505F啊，这是什么意思？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F也就是说，以安全的地方作为据点，\x01",
            "然后从那里展开搜索对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#070F对，就是这样。\x02\x03",
            "探索组在寻找路线的同时，\x01",
            "待机组守卫据点，然后准备随时交换成员。\x01",
            "　\x02\x03",
            "一旦找到了正确的路线，\x01",
            "我们就全部移动过去并将那作为新的据点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#051F原来如此……很合理嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#104F#2P就这样决定好了。\x01",
            "就把目前我们所在的地方作为据点吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(
        0xE,
        (
            "#100F艾丝蒂尔、约修亚，\x01",
            "立刻决定探索组的成员吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_23B3():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_23B3)

    def lambda_23C1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_23C1)

    def lambda_23CF():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_23CF)

    def lambda_23DD():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_23DD)

    def lambda_23EB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_23EB)

    def lambda_23F9():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_23F9)

    def lambda_2407():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2407)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F啊，我们决定！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#100F#2P与这次事件关联最深的就是你们俩了。\x01",
            "　\x02\x03",
            "大家都没有异议吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#021F嗯，我很赞成哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#040F我当然也赞成。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#560F我、我也赞成让姐姐他们来决定呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#053F哼，没办法了。\x01",
            "也只有听从你们两个的指挥了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#035F#5P呵呵……我相信你们哦。\x01",
            "我看中的小猫咪准能成大事的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#070F嗯，就是这样，\x01",
            "好好的选择组员吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#505F约修亚……怎么办？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F已经来不及仔细考虑了。\x02\x03",
            "如果想改变主意，\x01",
            "回据点这里替换成员就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F对啊，这样就行了……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Call(0, 17)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_265A")
    OP_83(0x17, 0x0)

    label("loc_265A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2676")
    OP_83(0x17, 0x0)

    label("loc_2676")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2692")
    OP_83(0x17, 0x0)

    label("loc_2692")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26AE")
    OP_83(0x18, 0x0)

    label("loc_26AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26CA")
    OP_83(0x18, 0x0)

    label("loc_26CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26E6")
    OP_83(0x18, 0x0)

    label("loc_26E6")

    SetChrFlags(0xF, 0x80)

    def lambda_26F1():
        TurnDirection(0xFE, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_26F1)

    def lambda_26FF():
        TurnDirection(0xFE, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_26FF)

    def lambda_270D():
        TurnDirection(0xFE, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_270D)

    def lambda_271B():
        TurnDirection(0xFE, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_271B)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_283A")
    SetChrPos(0xA, 36030, 0, -8640, 225)
    SetChrPos(0xF, 36210, 0, -9110, 225)
    SetChrChipByIndex(0xA, 17)
    SetChrSubChip(0xA, 1)
    OP_44(0xA, 0xFF)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#040F#5P基库这孩子也会跟着艾丝蒂尔你们\x01",
            "一起行动的。\x02\x03",
            "如果发现了可以作为新据点的地方，\x01",
            "它会回来向我们报告的。\x02\x03",
            "然后我们就会跟着它\x01",
            "到艾丝蒂尔你们所在的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#310F#2P啾。\x02",
    )

    CloseMessageWindow()
    Jump("loc_296F")

    label("loc_283A")


    def lambda_2840():
        OP_8C(0xFE, 225, 0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2840)
    SetChrPos(0x105, 36030, 0, -8640, 225)
    SetChrPos(0xF, 36210, 0, -9110, 225)
    SetChrChipByIndex(0x105, 17)
    SetChrSubChip(0x105, 1)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#040F#5P如果发现了可以作为新的据点的地方，\x01",
            "基库会回来报告的。\x02\x03",
            "跟着它就可以来到我们所在的地方了。\x01",
            "　\x02\x03",
            "还有，就算我离开探索组，\x01",
            "基库还是会跟着艾丝蒂尔你们行动哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#310F#2P啾。\x02",
    )

    CloseMessageWindow()

    label("loc_296F")


    ChrTalk(
        0x102,
        (
            "#010F原来如此，\x01",
            "这样我们就不用专程赶回这里来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F靠你了哦，基库！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#311F#2P啾啾！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0xF, 0x80)

    def lambda_2A14():

        label("loc_2A14")

        TurnDirection(0xFE, 0xF, 800)
        OP_48()
        Jump("loc_2A14")

    QueueWorkItem2(0x0, 1, lambda_2A14)

    def lambda_2A25():

        label("loc_2A25")

        TurnDirection(0xFE, 0xF, 800)
        OP_48()
        Jump("loc_2A25")

    QueueWorkItem2(0x1, 1, lambda_2A25)

    def lambda_2A36():

        label("loc_2A36")

        TurnDirection(0xFE, 0xF, 800)
        OP_48()
        Jump("loc_2A36")

    QueueWorkItem2(0x2, 1, lambda_2A36)

    def lambda_2A47():

        label("loc_2A47")

        TurnDirection(0xFE, 0xF, 800)
        OP_48()
        Jump("loc_2A47")

    QueueWorkItem2(0x3, 1, lambda_2A47)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A6D")
    SetChrFlags(0xA, 0x20)
    SetChrSubChip(0xA, 3)
    Jump("loc_2A7B")

    label("loc_2A6D")

    OP_44(0x105, 0xFF)
    SetChrFlags(0x105, 0x20)
    SetChrSubChip(0x105, 3)

    label("loc_2A7B")

    OP_22(0x8C, 0x0, 0x64)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0xF, 0x4)

    def lambda_2A90():
        OP_8E(0xFE, 0x88FE, 0x7D0, 0xFFFFD7C4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2A90)
    Sleep(100)

    def lambda_2AB0():
        OP_8E(0xFE, 0x88FE, 0x7D0, 0xFFFFD7C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2AB0)
    Sleep(100)

    def lambda_2AD0():
        OP_8E(0xFE, 0x88FE, 0x7D0, 0xFFFFD7C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2AD0)
    Sleep(100)

    def lambda_2AF0():
        OP_8E(0xFE, 0x7B0C, 0x0, 0xFFFFCDA6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2AF0)

    def lambda_2B0B():
        OP_6D(25620, 0, -12350, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2B0B)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B42")
    SetChrChipByIndex(0xA, 2)
    ClearChrFlags(0xA, 0x20)
    SetChrSubChip(0xA, 0)
    Jump("loc_2B51")

    label("loc_2B42")

    SetChrChipByIndex(0x105, 65535)
    ClearChrFlags(0x105, 0x20)
    SetChrSubChip(0x105, 0)

    label("loc_2B51")


    def lambda_2B57():
        OP_8E(0xFE, 0x3016, 0x1388, 0xFFFFC720, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2B57)
    Sleep(2500)

    def lambda_2B77():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2B77)

    def lambda_2B85():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2B85)

    def lambda_2B93():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2B93)

    def lambda_2BA1():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2BA1)

    def lambda_2BAF():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2BAF)
    OP_6D(35010, 0, -7430, 2000)

    ChrTalk(
        0xE,
        (
            "#102F#5P探索的任务就拜托你们了。\x01",
            "　\x02\x03",
            "为了慎重起见，我为你们准备了\x01",
            "一整套工具和简单的物品箱。\x02\x03",
            "如果要改造导力器，\x01",
            "你们就尽管告诉我就是了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，明白啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F那么我们就出发吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x667)
    OP_28(0x4F, 0x1, 0x1)
    OP_28(0x4F, 0x1, 0x2)
    OP_28(0x4F, 0x1, 0x4)
    SetChrFlags(0xF, 0x80)
    OP_4B(0xE, 255)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_4B(0xA, 255)
    OP_4B(0xB, 255)
    OP_4B(0xC, 255)
    OP_4B(0xD, 255)
    OP_43(0xE, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    EventEnd(0x0)
    Return()

    # Function_16_1B8F end

    def Function_17_2D26(): pass

    label("Function_17_2D26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D37")
    RemoveParty(0x2, 0xFF)

    label("loc_2D37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D48")
    RemoveParty(0x3, 0xFF)

    label("loc_2D48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D59")
    RemoveParty(0x5, 0xFF)

    label("loc_2D59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D6A")
    RemoveParty(0x4, 0xFF)

    label("loc_2D6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D7B")
    RemoveParty(0x6, 0xFF)

    label("loc_2D7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D8C")
    RemoveParty(0x7, 0xFF)

    label("loc_2D8C")

    Fade(1000)
    SetChrPos(0x101, 34210, 0, -9750, 350)
    SetChrPos(0x102, 33060, 0, -8430, 45)
    SetChrPos(0xE, 34700, 0, -7770, 222)
    Call(0, 18)
    OP_6D(35570, 0, -7090, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请选择除约修亚和艾丝蒂尔以外的两名成员。\x01",
            "　\x02",
        )
    )


    label("loc_2E59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32BF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EBC")

    Menu(
        0,
        10,
        106,
        1,
        (
            "★【　雪拉扎德　】\x01",      # 0
            "　【　奥利维尔　】\x01",      # 1
            "　【　 阿加特 　】\x01",      # 2
            "　【　　提妲　　】\x01",      # 3
            "　【　　 金 　　】\x01",      # 4
            "　【　 科洛丝 　】\x01",      # 5
        )
    )

    Jump("loc_30B0")

    label("loc_2EBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F12")

    Menu(
        0,
        10,
        106,
        1,
        (
            "　【　雪拉扎德　】\x01",      # 0
            "★【　奥利维尔　】\x01",      # 1
            "　【　 阿加特 　】\x01",      # 2
            "　【　　提妲　　】\x01",      # 3
            "　【　　 金 　　】\x01",      # 4
            "　【　 科洛丝 　】\x01",      # 5
        )
    )

    Jump("loc_30B0")

    label("loc_2F12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F68")

    Menu(
        0,
        10,
        106,
        1,
        (
            "　【　雪拉扎德　】\x01",      # 0
            "　【　奥利维尔　】\x01",      # 1
            "★【　 阿加特 　】\x01",      # 2
            "　【　　提妲　　】\x01",      # 3
            "　【　　 金 　　】\x01",      # 4
            "　【　 科洛丝 　】\x01",      # 5
        )
    )

    Jump("loc_30B0")

    label("loc_2F68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FBE")

    Menu(
        0,
        10,
        106,
        1,
        (
            "　【　雪拉扎德　】\x01",      # 0
            "　【　奥利维尔　】\x01",      # 1
            "　【　 阿加特 　】\x01",      # 2
            "★【　　提妲　　】\x01",      # 3
            "　【　　 金 　　】\x01",      # 4
            "　【　 科洛丝 　】\x01",      # 5
        )
    )

    Jump("loc_30B0")

    label("loc_2FBE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3014")

    Menu(
        0,
        10,
        106,
        1,
        (
            "　【　雪拉扎德　】\x01",      # 0
            "　【　奥利维尔　】\x01",      # 1
            "　【　 阿加特 　】\x01",      # 2
            "　【　　提妲　　】\x01",      # 3
            "★【　　 金 　　】\x01",      # 4
            "　【　 科洛丝 　】\x01",      # 5
        )
    )

    Jump("loc_30B0")

    label("loc_3014")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_306B")

    Menu(
        0,
        10,
        106,
        1,
        (
            "　【　雪拉扎德　】\x01",      # 0
            "　【　奥利维尔　】\x01",      # 1
            "　【　 阿加特 　】\x01",      # 2
            "　【　　提妲　　】\x01",      # 3
            "　【　　 金 　　】\x01",      # 4
            "★【　 科洛丝 　】\x01",      # 5
        )
    )

    Jump("loc_30B0")

    label("loc_306B")


    Menu(
        0,
        10,
        106,
        0,
        (
            "　【　雪拉扎德　】\x01",      # 0
            "　【　奥利维尔　】\x01",      # 1
            "　【　 阿加特 　】\x01",      # 2
            "　【　　提妲　　】\x01",      # 3
            "　【　　 金 　　】\x01",      # 4
            "　【　 科洛丝 　】\x01",      # 5
        )
    )


    label("loc_30B0")

    MenuEnd(0x0)
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_30D7"),
        (1, "loc_30F1"),
        (2, "loc_310B"),
        (3, "loc_3125"),
        (4, "loc_313F"),
        (5, "loc_3159"),
        (SWITCH_DEFAULT, "loc_3173"),
    )


    label("loc_30D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30EB")
    AddParty(0x2, 0xFF)
    Jump("loc_30EE")

    label("loc_30EB")

    RemoveParty(0x2, 0xFF)

    label("loc_30EE")

    Jump("loc_31EB")

    label("loc_30F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3105")
    AddParty(0x3, 0xFF)
    Jump("loc_3108")

    label("loc_3105")

    RemoveParty(0x3, 0xFF)

    label("loc_3108")

    Jump("loc_31EB")

    label("loc_310B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_311F")
    AddParty(0x5, 0xFF)
    Jump("loc_3122")

    label("loc_311F")

    RemoveParty(0x5, 0xFF)

    label("loc_3122")

    Jump("loc_31EB")

    label("loc_3125")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3139")
    AddParty(0x6, 0xFF)
    Jump("loc_313C")

    label("loc_3139")

    RemoveParty(0x6, 0xFF)

    label("loc_313C")

    Jump("loc_31EB")

    label("loc_313F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3153")
    AddParty(0x7, 0xFF)
    Jump("loc_3156")

    label("loc_3153")

    RemoveParty(0x7, 0xFF)

    label("loc_3156")

    Jump("loc_31EB")

    label("loc_3159")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_316D")
    AddParty(0x4, 0xFF)
    Jump("loc_3170")

    label("loc_316D")

    RemoveParty(0x4, 0xFF)

    label("loc_3170")

    Jump("loc_31EB")

    label("loc_3173")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3187")
    RemoveParty(0x2, 0xFF)
    Jump("loc_31E8")

    label("loc_3187")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_319B")
    RemoveParty(0x3, 0xFF)
    Jump("loc_31E8")

    label("loc_319B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31AF")
    RemoveParty(0x5, 0xFF)
    Jump("loc_31E8")

    label("loc_31AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31C3")
    RemoveParty(0x4, 0xFF)
    Jump("loc_31E8")

    label("loc_31C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31D7")
    RemoveParty(0x6, 0xFF)
    Jump("loc_31E8")

    label("loc_31D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31E8")
    RemoveParty(0x7, 0xFF)

    label("loc_31E8")

    Jump("loc_31EB")

    label("loc_31EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_320E")
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x2, 0x80)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_329A")

    label("loc_320E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3253")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请选择除约修亚和艾丝蒂尔以外的两名成员。\x01",
            "　\x02",
        )
    )

    Jump("loc_329A")

    label("loc_3253")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_329A")
    SetChrFlags(0x2, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请选择除约修亚和艾丝蒂尔以外的两名成员。\x01",
            "　\x02",
        )
    )


    label("loc_329A")

    SetChrPos(0x101, 34210, 0, -9750, 350)
    SetChrPos(0x102, 33060, 0, -8430, 45)
    Jump("loc_2E59")

    label("loc_32BF")

    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(300, 0)
    Fade(1000)
    SetChrPos(0x101, 34210, 0, -9750, 350)
    SetChrPos(0x102, 33060, 0, -8430, 45)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x2, 32130, 0, -9730, 45)
    SetChrPos(0x3, 33020, 0, -10520, 45)
    Call(0, 18)
    OP_6D(35570, 0, -7090, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Return()

    # Function_17_2D26 end

    def Function_18_336B(): pass

    label("Function_18_336B")

    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 34700, 0, -7770, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33A8")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 35690, 0, -4120, 180)
    Jump("loc_33AD")

    label("loc_33A8")

    SetChrFlags(0xB, 0x80)

    label("loc_33AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33D4")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 34740, 0, -6560, 180)
    Jump("loc_33D9")

    label("loc_33D4")

    SetChrFlags(0xC, 0x80)

    label("loc_33D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3400")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 37870, 0, -7040, 225)
    Jump("loc_3405")

    label("loc_3400")

    SetChrFlags(0x9, 0x80)

    label("loc_3405")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_342C")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 37210, 0, -5860, 225)
    Jump("loc_3431")

    label("loc_342C")

    SetChrFlags(0x8, 0x80)

    label("loc_3431")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3458")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 39350, 0, -8220, 270)
    Jump("loc_345D")

    label("loc_3458")

    SetChrFlags(0xD, 0x80)

    label("loc_345D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3484")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 36420, 0, -7530, 225)
    Jump("loc_3489")

    label("loc_3484")

    SetChrFlags(0xA, 0x80)

    label("loc_3489")

    Return()

    # Function_18_336B end

    def Function_19_348A(): pass

    label("Function_19_348A")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在此休息\x01",      # 0
            "离开\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3648")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_72(0x10, 0x20)
    OP_6F(0x10, 300)
    OP_70(0x10, 0x1F4)
    OP_73(0x10)
    OP_6F(0x10, 500)
    OP_70(0x10, 0x2BC)
    OP_71(0x10, 0x20)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x6, 0x2)
    LoadEffect(0x5, "map\\\\mp027_01.eff")
    PlayEffect(0x5, 0x6, 0xFF, 38290, 1200, -3310, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1500, 0, -1)
    Sleep(1500)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Sleep(3500)
    OP_82(0x6, 0x0)
    LoadEffect(0x5, "map\\\\mp027_00.eff")
    PlayEffect(0x5, 0x0, 0xFF, 38290, 1200, -3310, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x10, 0)
    OP_70(0x10, 0xFA)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_3648")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3662")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_3662")

    Return()

    # Function_19_348A end

    SaveToFile()

Try(main)
