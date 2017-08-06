from ED6ScenarioHelper import *

def main():
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
        "Function_4_610",          # 04, 4
        "Function_5_694",          # 05, 5
        "Function_6_6F2",          # 06, 6
        "Function_7_73F",          # 07, 7
        "Function_8_799",          # 08, 8
        "Function_9_7E2",          # 09, 9
        "Function_10_93B",         # 0A, 10
        "Function_11_973",         # 0B, 11
        "Function_12_992",         # 0C, 12
        "Function_13_160F",        # 0D, 13
        "Function_14_16A1",        # 0E, 14
        "Function_15_173D",        # 0F, 15
        "Function_16_17BA",        # 10, 16
        "Function_17_26E2",        # 11, 17
        "Function_18_2E8E",        # 12, 18
        "Function_19_2FAD",        # 13, 19
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

    def Function_4_610(): pass

    label("Function_4_610")

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

    # Function_4_610 end

    def Function_5_694(): pass

    label("Function_5_694")

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

    # Function_5_694 end

    def Function_6_6F2(): pass

    label("Function_6_6F2")

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

    # Function_6_6F2 end

    def Function_7_73F(): pass

    label("Function_7_73F")

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

    # Function_7_73F end

    def Function_8_799(): pass

    label("Function_8_799")

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

    # Function_8_799 end

    def Function_9_7E2(): pass

    label("Function_9_7E2")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_857")
    Call(0, 10)
    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_857")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86E")
    Call(0, 11)
    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_86E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BF")
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

    label("loc_8BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8D0")
    TalkEnd(0xE)
    Return()

    label("loc_8D0")


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

    # Function_9_7E2 end

    def Function_10_93B(): pass

    label("Function_10_93B")


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

    # Function_10_93B end

    def Function_11_973(): pass

    label("Function_11_973")


    ChrTalk(
        0xE,
        "#100F有什么需要的吗？\x02",
    )

    CloseMessageWindow()
    OP_0D()
    OP_A9(0x6B)
    Return()

    # Function_11_973 end

    def Function_12_992(): pass

    label("Function_12_992")

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

    def lambda_B2A():
        OP_6D(19210, 0, -13380, 3500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_B2A)

    def lambda_B42():
        OP_6C(135000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_B42)
    Sleep(2000)

    def lambda_B57():
        OP_67(0, 10910, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B57)

    def lambda_B6F():
        OP_6E(514, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_B6F)
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

    def lambda_C81():

        label("loc_C81")

        TurnDirection(0xFE, 0x1A, 0)
        OP_48()
        Jump("loc_C81")

    QueueWorkItem2(0x1B, 3, lambda_C81)

    def lambda_C92():

        label("loc_C92")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_C92")

    QueueWorkItem2(0x1C, 3, lambda_C92)
    ClearChrFlags(0x1B, 0x1)
    ClearChrFlags(0x1C, 0x1)

    def lambda_CAD():
        OP_8F(0xFE, 0x7A76, 0x0, 0xFFFFD03A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_CAD)
    Sleep(300)

    def lambda_CCD():
        OP_8F(0xFE, 0x79FE, 0x0, 0xFFFFC2C0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_CCD)
    TurnDirection(0x1A, 0x1B, 400)

    def lambda_CEF():
        OP_6D(32409, 0, -13750, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_CEF)

    def lambda_D07():
        OP_6C(90000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_D07)

    def lambda_D17():
        OP_67(0, 7160, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_D17)
    OP_8E(0x1A, 0x869C, 0x0, 0xFFFFC482, 0x1388, 0x0)

    def lambda_D43():

        label("loc_D43")

        TurnDirection(0xFE, 0x1C, 0)
        OP_48()
        Jump("loc_D43")

    QueueWorkItem2(0x1A, 1, lambda_D43)

    def lambda_D54():

        label("loc_D54")

        TurnDirection(0xFE, 0x1B, 0)
        OP_48()
        Jump("loc_D54")

    QueueWorkItem2(0x19, 1, lambda_D54)
    SetChrChipByIndex(0x1A, 13)
    SetChrChipByIndex(0x19, 15)
    OP_22(0xE7, 0x0, 0x64)
    WaitChrThread(0x1B, 0x1)
    SetChrChipByIndex(0x1B, 12)
    SetChrFlags(0x1B, 0x1)
    SetChrFlags(0x1C, 0x1)

    def lambda_D88():

        label("loc_D88")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_D88")

    QueueWorkItem2(0x1B, 0, lambda_D88)
    TurnDirection(0x1B, 0x19, 0)
    WaitChrThread(0x1C, 0x1)
    SetChrChipByIndex(0x1C, 12)

    def lambda_DAC():

        label("loc_DAC")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_DAC")

    QueueWorkItem2(0x1C, 0, lambda_DAC)
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

    def lambda_E8E():
        OP_94(0x1, 0xFE, 0xB4, 0x44C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E8E)

    def lambda_EA4():
        OP_94(0x1, 0xFE, 0xB4, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_EA4)
    Sleep(50)

    def lambda_EBF():
        OP_94(0x1, 0xFE, 0xB4, 0x2BC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_EBF)

    def lambda_ED5():
        OP_94(0x1, 0xFE, 0xB4, 0x44C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_ED5)
    Sleep(100)

    def lambda_EF0():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_EF0)

    def lambda_F06():
        OP_94(0x1, 0xFE, 0xB4, 0x514, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_F06)
    Sleep(50)

    def lambda_F21():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_F21)
    Sleep(50)

    def lambda_F3C():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_F3C)
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

    def lambda_FA4():
        OP_6C(70000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_FA4)
    OP_6B(2900, 1500)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x19, 0x40)

    def lambda_FC7():
        OP_6D(30310, 0, -13620, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_FC7)

    def lambda_FDF():
        OP_6B(2500, 1000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_FDF)

    def lambda_FEF():
        OP_67(0, 5500, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_FEF)

    def lambda_1007():
        OP_6C(42000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1007)
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

    def lambda_1101():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_1101)

    def lambda_1111():
        OP_6C(19000, 2000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_1111)

    def lambda_1121():
        OP_67(0, 7160, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1121)

    def lambda_1139():
        OP_6D(30310, 0, -13620, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1139)
    SetChrFlags(0x1B, 0x4)
    PlayEffect(0x0, 0xFF, 0x1B, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_118B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_118B)

    def lambda_119D():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_119D)
    Sleep(300)
    SetChrFlags(0x1C, 0x4)
    PlayEffect(0x0, 0xFF, 0x1C, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_11F7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_11F7)

    def lambda_1209():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_1209)
    Sleep(1500)

    def lambda_1229():
        OP_99(0xFE, 0x9, 0xB, 0x640)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_1229)

    def lambda_1239():
        OP_96(0xFE, 0x7AE4, 0x0, 0xFFFFC40A, 0x2BC, 0xFA0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_1239)
    SetChrFlags(0x19, 0x800)

    def lambda_125C():
        OP_99(0xFE, 0x5, 0xB, 0x7D0)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_125C)
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

    def lambda_132C():

        label("loc_132C")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_132C")

    QueueWorkItem2(0x1A, 3, lambda_132C)

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

    def lambda_1451():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1451)

    def lambda_1461():
        OP_6D(35740, 0, -13960, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1461)
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

    # Function_12_992 end

    def Function_13_160F(): pass

    label("Function_13_160F")

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

    # Function_13_160F end

    def Function_14_16A1(): pass

    label("Function_14_16A1")

    SetChrChipByIndex(0xFE, 13)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, 34460, 0, -15230, 270)

    def lambda_16C7():

        label("loc_16C7")

        TurnDirection(0xFE, 0x1C, 0)
        OP_48()
        Jump("loc_16C7")

    QueueWorkItem2(0xFE, 3, lambda_16C7)
    OP_96(0xFE, 0x8246, 0x0, 0xFFFFC31A, 0x3E8, 0x2328)
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 14)
    SetChrFlags(0xFE, 0x800)

    def lambda_16FD():
        OP_99(0xFE, 0x0, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_16FD)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    OP_96(0xFE, 0x7F6B, 0x4B0, 0xFFFFC360, 0x4E2, 0x1388)
    OP_8F(0xFE, 0x7274, 0x96, 0xFFFFC41E, 0x32C8, 0x0)
    Return()

    # Function_14_16A1 end

    def Function_15_173D(): pass

    label("Function_15_173D")

    ClearChrFlags(0x1A, 0x800)
    SetChrChipByIndex(0xFE, 15)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, 34660, 0, -13430, 270)

    def lambda_1768():

        label("loc_1768")

        TurnDirection(0xFE, 0x1B, 0)
        OP_48()
        Jump("loc_1768")

    QueueWorkItem2(0xFE, 3, lambda_1768)
    OP_8F(0xFE, 0x8282, 0x0, 0xFFFFCFE0, 0x1388, 0x0)
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 16)
    SetChrFlags(0xFE, 0x800)

    def lambda_179B():
        OP_99(0xFE, 0x0, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_179B)
    OP_8E(0xFE, 0x70D0, 0x96, 0xFFFFD03A, 0x2AF8, 0x0)
    Return()

    # Function_15_173D end

    def Function_16_17BA(): pass

    label("Function_16_17BA")

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

    def lambda_1922():
        OP_6D(50, 0, -20330, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1922)
    Sleep(3000)

    def lambda_193F():
        OP_6C(77000, 11000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_193F)
    Sleep(7000)

    def lambda_1954():
        OP_6D(39590, 0, -14310, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1954)

    def lambda_196C():
        OP_67(0, 22340, -34740, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_196C)

    def lambda_1984():
        OP_6E(343, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1984)
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

    def lambda_1BFF():
        OP_6E(300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1BFF)

    def lambda_1C0F():
        OP_6C(90000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C0F)

    def lambda_1C1F():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1C1F)

    def lambda_1C2D():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1C2D)
    Sleep(100)

    def lambda_1C40():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1C40)
    Sleep(100)

    def lambda_1C53():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1C53)

    def lambda_1C61():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1C61)
    Sleep(100)

    def lambda_1C74():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1C74)

    def lambda_1C82():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1C82)
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

    def lambda_1E56():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1E56)

    def lambda_1E64():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1E64)

    def lambda_1E72():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E72)

    def lambda_1E80():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E80)

    def lambda_1E8E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1E8E)

    def lambda_1E9C():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1E9C)

    def lambda_1EAA():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1EAA)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20F2")
    OP_83(0x17, 0x0)

    label("loc_20F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_210E")
    OP_83(0x17, 0x0)

    label("loc_210E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_212A")
    OP_83(0x17, 0x0)

    label("loc_212A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2146")
    OP_83(0x18, 0x0)

    label("loc_2146")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2162")
    OP_83(0x18, 0x0)

    label("loc_2162")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_217E")
    OP_83(0x18, 0x0)

    label("loc_217E")

    SetChrFlags(0xF, 0x80)

    def lambda_2189():
        TurnDirection(0xFE, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2189)

    def lambda_2197():
        TurnDirection(0xFE, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2197)

    def lambda_21A5():
        TurnDirection(0xFE, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_21A5)

    def lambda_21B3():
        TurnDirection(0xFE, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_21B3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22B4")
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
    Jump("loc_23AF")

    label("loc_22B4")


    def lambda_22BA():
        OP_8C(0xFE, 225, 0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_22BA)
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

    label("loc_23AF")


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

    def lambda_2424():

        label("loc_2424")

        TurnDirection(0xFE, 0xF, 800)
        OP_48()
        Jump("loc_2424")

    QueueWorkItem2(0x0, 1, lambda_2424)

    def lambda_2435():

        label("loc_2435")

        TurnDirection(0xFE, 0xF, 800)
        OP_48()
        Jump("loc_2435")

    QueueWorkItem2(0x1, 1, lambda_2435)

    def lambda_2446():

        label("loc_2446")

        TurnDirection(0xFE, 0xF, 800)
        OP_48()
        Jump("loc_2446")

    QueueWorkItem2(0x2, 1, lambda_2446)

    def lambda_2457():

        label("loc_2457")

        TurnDirection(0xFE, 0xF, 800)
        OP_48()
        Jump("loc_2457")

    QueueWorkItem2(0x3, 1, lambda_2457)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_247D")
    SetChrFlags(0xA, 0x20)
    SetChrSubChip(0xA, 3)
    Jump("loc_248B")

    label("loc_247D")

    OP_44(0x105, 0xFF)
    SetChrFlags(0x105, 0x20)
    SetChrSubChip(0x105, 3)

    label("loc_248B")

    OP_22(0x8C, 0x0, 0x64)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0xF, 0x4)

    def lambda_24A0():
        OP_8E(0xFE, 0x88FE, 0x7D0, 0xFFFFD7C4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_24A0)
    Sleep(100)

    def lambda_24C0():
        OP_8E(0xFE, 0x88FE, 0x7D0, 0xFFFFD7C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_24C0)
    Sleep(100)

    def lambda_24E0():
        OP_8E(0xFE, 0x88FE, 0x7D0, 0xFFFFD7C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_24E0)
    Sleep(100)

    def lambda_2500():
        OP_8E(0xFE, 0x7B0C, 0x0, 0xFFFFCDA6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2500)

    def lambda_251B():
        OP_6D(25620, 0, -12350, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_251B)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2552")
    SetChrChipByIndex(0xA, 2)
    ClearChrFlags(0xA, 0x20)
    SetChrSubChip(0xA, 0)
    Jump("loc_2561")

    label("loc_2552")

    SetChrChipByIndex(0x105, 65535)
    ClearChrFlags(0x105, 0x20)
    SetChrSubChip(0x105, 0)

    label("loc_2561")


    def lambda_2567():
        OP_8E(0xFE, 0x3016, 0x1388, 0xFFFFC720, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2567)
    Sleep(2500)

    def lambda_2587():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2587)

    def lambda_2595():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2595)

    def lambda_25A3():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_25A3)

    def lambda_25B1():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_25B1)

    def lambda_25BF():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_25BF)
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

    # Function_16_17BA end

    def Function_17_26E2(): pass

    label("Function_17_26E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26F3")
    RemoveParty(0x2, 0xFF)

    label("loc_26F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2704")
    RemoveParty(0x3, 0xFF)

    label("loc_2704")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2715")
    RemoveParty(0x5, 0xFF)

    label("loc_2715")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2726")
    RemoveParty(0x4, 0xFF)

    label("loc_2726")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2737")
    RemoveParty(0x6, 0xFF)

    label("loc_2737")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2748")
    RemoveParty(0x7, 0xFF)

    label("loc_2748")

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


    label("loc_280F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DE2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28A8")

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

    Jump("loc_2BDF")

    label("loc_28A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2934")

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

    Jump("loc_2BDF")

    label("loc_2934")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29C0")

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

    Jump("loc_2BDF")

    label("loc_29C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A4C")

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

    Jump("loc_2BDF")

    label("loc_2A4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AD8")

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

    Jump("loc_2BDF")

    label("loc_2AD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B64")

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

    Jump("loc_2BDF")

    label("loc_2B64")


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


    label("loc_2BDF")

    MenuEnd(0x0)
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C06"),
        (1, "loc_2C20"),
        (2, "loc_2C3A"),
        (3, "loc_2C54"),
        (4, "loc_2C6E"),
        (5, "loc_2C88"),
        (SWITCH_DEFAULT, "loc_2CA2"),
    )


    label("loc_2C06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C1A")
    AddParty(0x2, 0xFF)
    Jump("loc_2C1D")

    label("loc_2C1A")

    RemoveParty(0x2, 0xFF)

    label("loc_2C1D")

    Jump("loc_2D1A")

    label("loc_2C20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C34")
    AddParty(0x3, 0xFF)
    Jump("loc_2C37")

    label("loc_2C34")

    RemoveParty(0x3, 0xFF)

    label("loc_2C37")

    Jump("loc_2D1A")

    label("loc_2C3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C4E")
    AddParty(0x5, 0xFF)
    Jump("loc_2C51")

    label("loc_2C4E")

    RemoveParty(0x5, 0xFF)

    label("loc_2C51")

    Jump("loc_2D1A")

    label("loc_2C54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C68")
    AddParty(0x6, 0xFF)
    Jump("loc_2C6B")

    label("loc_2C68")

    RemoveParty(0x6, 0xFF)

    label("loc_2C6B")

    Jump("loc_2D1A")

    label("loc_2C6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C82")
    AddParty(0x7, 0xFF)
    Jump("loc_2C85")

    label("loc_2C82")

    RemoveParty(0x7, 0xFF)

    label("loc_2C85")

    Jump("loc_2D1A")

    label("loc_2C88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C9C")
    AddParty(0x4, 0xFF)
    Jump("loc_2C9F")

    label("loc_2C9C")

    RemoveParty(0x4, 0xFF)

    label("loc_2C9F")

    Jump("loc_2D1A")

    label("loc_2CA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CB6")
    RemoveParty(0x2, 0xFF)
    Jump("loc_2D17")

    label("loc_2CB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CCA")
    RemoveParty(0x3, 0xFF)
    Jump("loc_2D17")

    label("loc_2CCA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CDE")
    RemoveParty(0x5, 0xFF)
    Jump("loc_2D17")

    label("loc_2CDE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CF2")
    RemoveParty(0x4, 0xFF)
    Jump("loc_2D17")

    label("loc_2CF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D06")
    RemoveParty(0x6, 0xFF)
    Jump("loc_2D17")

    label("loc_2D06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D17")
    RemoveParty(0x7, 0xFF)

    label("loc_2D17")

    Jump("loc_2D1A")

    label("loc_2D1A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D3D")
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x2, 0x80)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2DBD")

    label("loc_2D3D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7C")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请选择除约修亚和艾丝蒂尔以外的两名成员。\x01",
            "　\x02",
        )
    )

    Jump("loc_2DBD")

    label("loc_2D7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DBD")
    SetChrFlags(0x2, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请选择除约修亚和艾丝蒂尔以外的两名成员。\x01",
            "　\x02",
        )
    )


    label("loc_2DBD")

    SetChrPos(0x101, 34210, 0, -9750, 350)
    SetChrPos(0x102, 33060, 0, -8430, 45)
    Jump("loc_280F")

    label("loc_2DE2")

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

    # Function_17_26E2 end

    def Function_18_2E8E(): pass

    label("Function_18_2E8E")

    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 34700, 0, -7770, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ECB")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 35690, 0, -4120, 180)
    Jump("loc_2ED0")

    label("loc_2ECB")

    SetChrFlags(0xB, 0x80)

    label("loc_2ED0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF7")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 34740, 0, -6560, 180)
    Jump("loc_2EFC")

    label("loc_2EF7")

    SetChrFlags(0xC, 0x80)

    label("loc_2EFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F23")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 37870, 0, -7040, 225)
    Jump("loc_2F28")

    label("loc_2F23")

    SetChrFlags(0x9, 0x80)

    label("loc_2F28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F4F")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 37210, 0, -5860, 225)
    Jump("loc_2F54")

    label("loc_2F4F")

    SetChrFlags(0x8, 0x80)

    label("loc_2F54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F7B")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 39350, 0, -8220, 270)
    Jump("loc_2F80")

    label("loc_2F7B")

    SetChrFlags(0xD, 0x80)

    label("loc_2F80")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FA7")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 36420, 0, -7530, 225)
    Jump("loc_2FAC")

    label("loc_2FA7")

    SetChrFlags(0xA, 0x80)

    label("loc_2FAC")

    Return()

    # Function_18_2E8E end

    def Function_19_2FAD(): pass

    label("Function_19_2FAD")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3169")
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

    label("loc_3169")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3183")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_3183")

    Return()

    # Function_19_2FAD end

    SaveToFile()

Try(main)
