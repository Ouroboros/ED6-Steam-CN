from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3310   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3310.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
        '多杰',                                 # 9
        '拉德米拉',                             # 10
        '卡雷尔',                               # 11
        '士兵布拉姆',                           # 12
        '士兵赫宁',                             # 13
        '派斯队长',                             # 14
        '格温副长',                             # 15
        '伦法',                                 # 16
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
        'ED6_DT07/CH01140 ._CH',             # 00
        'ED6_DT07/CH01690 ._CH',             # 01
        'ED6_DT07/CH02640 ._CH',             # 02
        'ED6_DT07/CH01300 ._CH',             # 03
        'ED6_DT07/CH01300 ._CH',             # 04
        'ED6_DT07/CH01310 ._CH',             # 05
        'ED6_DT07/CH01300 ._CH',             # 06
        'ED6_DT07/CH01270 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01140P._CP',             # 00
        'ED6_DT07/CH01690P._CP',             # 01
        'ED6_DT07/CH02640P._CP',             # 02
        'ED6_DT07/CH01300P._CP',             # 03
        'ED6_DT07/CH01300P._CP',             # 04
        'ED6_DT07/CH01310P._CP',             # 05
        'ED6_DT07/CH01300P._CP',             # 06
        'ED6_DT07/CH01270P._CP',             # 07
    )

    DeclNpc(
        X                   = -44500,
        Z                   = 0,
        Y                   = 7710,
        Direction           = 82,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        TalkScenaIndex      = 10,
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
        TalkScenaIndex      = 11,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    DeclActor(
        TriggerX            = 7230,
        TriggerZ            = 0,
        TriggerY            = 9350,
        TriggerRange        = 400,
        ActorX              = 6990,
        ActorZ              = 1500,
        ActorY              = 11450,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -49710,
        TriggerZ            = 0,
        TriggerY            = 7160,
        TriggerRange        = 400,
        ActorX              = -51810,
        ActorZ              = 1500,
        ActorY              = 6820,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -49710,
        TriggerZ            = 0,
        TriggerY            = 7160,
        TriggerRange        = 400,
        ActorX              = -51810,
        ActorZ              = 1500,
        ActorY              = 6820,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_256",          # 00, 0
        "Function_1_4D3",          # 01, 1
        "Function_2_529",          # 02, 2
        "Function_3_53F",          # 03, 3
        "Function_4_546",          # 04, 4
        "Function_5_B62",          # 05, 5
        "Function_6_B67",          # 06, 6
        "Function_7_16EF",         # 07, 7
        "Function_8_16F4",         # 08, 8
        "Function_9_1B17",         # 09, 9
        "Function_10_24E5",        # 0A, 10
        "Function_11_25DC",        # 0B, 11
        "Function_12_2A73",        # 0C, 12
        "Function_13_2B87",        # 0D, 13
    )


    def Function_0_256(): pass

    label("Function_0_256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_28C")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 6160, 0, 66940, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 11190, 0, 68400, 180)
    Jump("loc_2F7")

    label("loc_28C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_296")
    Jump("loc_2F7")

    label("loc_296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2A0")
    Jump("loc_2F7")

    label("loc_2A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2AA")
    Jump("loc_2F7")

    label("loc_2AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2B4")
    Jump("loc_2F7")

    label("loc_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2BE")
    Jump("loc_2F7")

    label("loc_2BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2C8")
    Jump("loc_2F7")

    label("loc_2C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_2D2")
    Jump("loc_2F7")

    label("loc_2D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2DC")
    Jump("loc_2F7")

    label("loc_2DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2EB")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_2F7")

    label("loc_2EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2F7")
    ClearChrFlags(0x8, 0x80)

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_343")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 11650, 0, 7310, 359)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -51810, 0, 6820, 97)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 6990, 0, 11450, 189)
    Jump("loc_4D2")

    label("loc_343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3A5")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 11650, 0, 7310, 359)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -55630, 0, 9700, 105)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -54180, 0, 9800, 267)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 6990, 0, 11450, 189)
    Jump("loc_4D2")

    label("loc_3A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3DB")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -51810, 0, 6820, 97)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 6990, 0, 11450, 189)
    Jump("loc_4D2")

    label("loc_3DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_427")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 11650, 0, 7310, 359)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -51810, 0, 6820, 97)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 6990, 0, 11450, 189)
    Jump("loc_4D2")

    label("loc_427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_489")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3860, 0, 68230, 108)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3970, 0, 9040, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -51810, 0, 6820, 97)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 6990, 0, 11450, 189)
    Jump("loc_4D2")

    label("loc_489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4D2")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 11650, 0, 7310, 359)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -51810, 0, 6820, 97)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 6990, 0, 11450, 189)

    label("loc_4D2")

    Return()

    # Function_0_256 end

    def Function_1_4D3(): pass

    label("Function_1_4D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_4E1")
    OP_64(0x2, 0x1)
    Jump("loc_528")

    label("loc_4E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_4F3")
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    Jump("loc_528")

    label("loc_4F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_501")
    OP_64(0x2, 0x1)
    Jump("loc_528")

    label("loc_501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_50F")
    OP_64(0x2, 0x1)
    Jump("loc_528")

    label("loc_50F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_51D")
    OP_64(0x1, 0x1)
    Jump("loc_528")

    label("loc_51D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_528")
    OP_64(0x2, 0x1)

    label("loc_528")

    Return()

    # Function_1_4D3 end

    def Function_2_529(): pass

    label("Function_2_529")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_529")

    label("loc_53E")

    Return()

    # Function_2_529 end

    def Function_3_53F(): pass

    label("Function_3_53F")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_3_53F end

    def Function_4_546(): pass

    label("Function_4_546")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_67D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5E4")

    ChrTalk(
        0xFE,
        (
            "哦，\x01",
            "马上就快到门卫的交班时间了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……不过，\x01",
            "还是像平常那样等着吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "等布拉姆那家伙\x01",
            "来叫我之后再离开吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67A")

    label("loc_5E4")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "袭击工房的犯人\x01",
            "究竟逃到哪里去了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们的队长\x01",
            "也百思不得其解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了，\x01",
            "那也不是队长的责任。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67A")

    Jump("loc_B5E")

    label("loc_67D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_7A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_703")

    ChrTalk(
        0xFE,
        (
            "我想大概队长本人\x01",
            "也不愿意接受这个命令吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……算了， \x01",
            "他只是不愿轻易说出自己的意见。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_79E")

    label("loc_703")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "不知道为什么，\x01",
            "上面好像下令解除盘查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎么想都觉得很奇怪啊。\x01",
            "真是不明白上面的人在想什么。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79E")

    Jump("loc_B5E")

    label("loc_7A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_95B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8CC")

    ChrTalk(
        0xFE,
        (
            "一天到晚盯着共和国的动向\x01",
            "也没什么用啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了在关键时刻能发挥力量，\x01",
            "平时就要放松一点嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "队长的这个想法\x01",
            "我也非常地理解，\x01",
            "可是副长的脑袋却很顽固……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从他来到这里，\x01",
            "很多事情都变得难办起来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_958")

    label("loc_8CC")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "工作的时候\x01",
            "还是要讲究方法嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了将来可能出现的关键时刻作准备，\x01",
            "平时要保存力量才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个堡垒\x01",
            "也有这样的地方哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_958")

    Jump("loc_B5E")

    label("loc_95B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_9BC")

    ChrTalk(
        0xFE,
        "我可不是在偷懒。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只是整理一下床单，\x01",
            "把花瓶的位置摆整齐而已。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2F")

    label("loc_9BC")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "这个时间\x01",
            "队长应该下来吃饭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以在这里\x01",
            "先这么坚持吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2F")

    Jump("loc_B5E")

    label("loc_A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_AC7")

    ChrTalk(
        0xFE,
        (
            "虽然已经是交班的时间了， \x01",
            "但是布拉姆那家伙肯定还在睡觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也没有必要\x01",
            "特地过去把他叫醒吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5E")

    label("loc_AC7")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "哦，再过不久就要和布拉姆\x01",
            "进行门卫工作的交班了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……不过，\x01",
            "还是不用那么心急了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "等布拉姆那家伙\x01",
            "来叫我之后再离开吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5E")

    TalkEnd(0xFE)
    Return()

    # Function_4_546 end

    def Function_5_B62(): pass

    label("Function_5_B62")

    Call(0, 6)
    Return()

    # Function_5_B62 end

    def Function_6_B67(): pass

    label("Function_6_B67")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_C87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_BEB")

    ChrTalk(
        0xD,
        "但是，总部的命令真是奇怪。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "说不定背后\x01",
            "有什么见不得人的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C84")

    label("loc_BEB")

    OP_A2(0x5)

    ChrTalk(
        0xD,
        (
            "从军队总部发来了\x01",
            "重新展开盘查的命令……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "恐怖袭击已经过了一段时间了。\x01",
            "现在再盘查已经太迟了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C84")

    Jump("loc_16EB")

    label("loc_C87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_EDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_D54")

    ChrTalk(
        0xD,
        (
            "不过命令是不能违抗的，\x01",
            "那就不要违抗了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "正因如此，\x01",
            "今后就以强化警备为由，\x01",
            "继续维持盘查时的体制吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED9")

    label("loc_D54")

    OP_A2(0x5)

    ChrTalk(
        0xD,
        (
            "副长的疑问暂且不说，\x01",
            "命令就是命令。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "我们是不能违抗的。\x01",
            "重新展开盘查是不可能的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "……但是，\x01",
            "只要不违抗命令就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "正因如此，\x01",
            "今后就以强化警备为由，\x01",
            "继续维持盘查时的体制吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "绝对没有可疑的家伙\x01",
            "从这里逃到国外。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED9")

    Jump("loc_16EB")

    label("loc_EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1083")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_F95")

    ChrTalk(
        0xD,
        (
            "因为蔡斯事件的影响，\x01",
            "现在如果没有充足的理由\x01",
            "是无法通行的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "打算去共和国的话，\x01",
            "我想还是过一阵子再来比较好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1080")

    label("loc_F95")

    OP_A2(0x5)

    ChrTalk(
        0xD,
        (
            "因为蔡斯事件的关系，\x01",
            "现在如果没有充足的理由\x01",
            "是无法通行的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "如果要去共和国的话，\x01",
            "最好还是下次再来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "因为这是个相当严重的事件，\x01",
            "调查也要花些时间。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1080")

    Jump("loc_16EB")

    label("loc_1083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1262")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1167")

    ChrTalk(
        0xD,
        (
            "格温副长\x01",
            "真是让我伤脑筋……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "如果放任他那种人不管的话，\x01",
            "会带来很多麻烦的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "唔，不过大家要是能\x01",
            "学习他的优点就太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125F")

    label("loc_1167")

    OP_A2(0x5)

    ChrTalk(
        0xD,
        (
            "呼，格温副长\x01",
            "真是让我伤脑筋……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "他既有能力，\x01",
            "也很有干劲，\x01",
            "但就是做事有些欠考虑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "如果放任他那种人不管的话，\x01",
            "会带来很多麻烦的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_125F")

    Jump("loc_16EB")

    label("loc_1262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1436")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_133E")

    ChrTalk(
        0xD,
        (
            "这一带本来就有\x01",
            "很多共和国来的移民。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "比如，我们这里的酒保伦法\x01",
            "也是共和国出生的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "作为友好邻邦，\x01",
            "今后也要好好相处啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1433")

    label("loc_133E")

    OP_A2(0x5)

    ChrTalk(
        0xD,
        (
            "通过这个关所的\x01",
            "主要是来往于\x01",
            "共和国和利贝尔之间的商人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "虽然和共和国之间\x01",
            "有定期船的航线，\x01",
            "不过毕竟比较费钱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "现在步行过境的人\x01",
            "还是很多的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1433")

    Jump("loc_16EB")

    label("loc_1436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_16EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_15AF")

    ChrTalk(
        0xD,
        (
            "这个关所的使命\x01",
            "就是避免不必要的紧张局面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "我国已经和帝国不和睦了，\x01",
            "再和共和国交恶的话，\x01",
            "那么处境就很不妙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "所以我让部下\x01",
            "工作时点到为止就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "哈～哈～哈，\x01",
            "这真是受照顾的岗位呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16EB")

    label("loc_15AF")

    OP_A2(0x5)

    ChrTalk(
        0xD,
        (
            "啊，欢迎欢迎。\x01",
            "千里迢迢来到这里真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "这里是沃尔费堡垒， \x01",
            "是和卡尔瓦德共和国\x01",
            "交界的守卫关所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "因为对面是共和国，\x01",
            "所以和哈肯大门那里\x01",
            "是不一样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "……正因如此， \x01",
            "我们守卫起来也很轻松。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16EB")

    TalkEnd(0xD)
    Return()

    # Function_6_B67 end

    def Function_7_16EF(): pass

    label("Function_7_16EF")

    Call(0, 8)
    Return()

    # Function_7_16EF end

    def Function_8_16F4(): pass

    label("Function_8_16F4")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1895")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1795")

    ChrTalk(
        0xE,
        (
            "队长！\x01",
            "请重新开始盘查的工作！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "现在这样的话，\x01",
            "犯人有可能会逃亡国外！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1892")

    label("loc_1795")

    OP_A2(0x6)

    ChrTalk(
        0xE,
        (
            "关于盘查解除的命令\x01",
            "正好要向队长问一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "明明没有犯人被逮捕的消息，\x01",
            "却自作主张下达这样的命令。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "到底该向士兵们\x01",
            "怎么说明才好？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 400)
    SetChrFlags(0xE, 0x10)

    label("loc_1892")

    Jump("loc_1B13")

    label("loc_1895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1B13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_19A3")

    ChrTalk(
        0xE,
        (
            "部下的怠慢\x01",
            "都是上司的责任啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "本来应该坚持让队长重新考虑一下，\x01",
            "可是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "队长是这里的责任人。\x01",
            "我也不能太过越权。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B13")

    label("loc_19A3")

    OP_A2(0x6)

    ChrTalk(
        0xE,
        (
            "士兵们这么怠慢，\x01",
            "派斯队长难逃其责。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "因为队长采取放任主义，\x01",
            "都不注意士兵的行为。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "这件事我以前就和队长探讨过，\x01",
            "但是……\x01",
            "怎么说他也听不进去啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "算了，\x01",
            "这里的负责人是派斯队长。\x01",
            "我不能再多说了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B13")

    TalkEnd(0xE)
    Return()

    # Function_8_16F4 end

    def Function_9_1B17(): pass

    label("Function_9_1B17")

    TalkBegin(0xF)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "休息\x01",        # 2
            "离开\x01",        # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B7C")
    OP_0D()
    OP_A9(0x48)
    OP_56(0x0)
    TalkEnd(0xF)
    Return()

    label("loc_1B7C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B95")
    OP_0D()
    OP_A9(0x47)
    OP_56(0x0)
    TalkEnd(0xF)
    Return()

    label("loc_1B95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BA6")
    TalkEnd(0xF)
    Return()

    label("loc_1BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1C76")

    ChrTalk(
        0xF,
        "你们知道吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "袭击中央工房的犯人\x01",
            "好像还没有抓到哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "军队那些家伙们\x01",
            "到底都在干些什么啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "……连晚饭都不来吃了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24E1")

    label("loc_1C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1E29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1D68")

    ChrTalk(
        0xF,
        (
            "盘查被解除了我是很高兴，\x01",
            "但是……\x01",
            "抓犯人的事该怎么办啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "本来还想着\x01",
            "以逮捕犯人为纪念\x01",
            "发表一下我的新作特制料理呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "唉，\x01",
            "等到下次有机会再说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E26")

    label("loc_1D68")

    OP_A2(0x7)

    ChrTalk(
        0xF,
        (
            "呼，盘查解除了呢。\x01",
            "无论如何，安心了安心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "不过，犯人怎么样了，\x01",
            "却完全没有消息呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "王国军那些家伙\x01",
            "一定在全力搜索吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E26")

    Jump("loc_24E1")

    label("loc_1E29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1FC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1ED8")

    ChrTalk(
        0xF,
        (
            "快点抓到犯人，\x01",
            "这个关所就能\x01",
            "恢复平时的通行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "……不这样的话，\x01",
            "生意也会受到影响的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "哈哈哈，这下可不得了了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FC6")

    label("loc_1ED8")

    OP_A2(0x7)

    ChrTalk(
        0xF,
        (
            "关于那个事件我刚才听说了。\x01",
            "蔡斯的人们遇到难题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "不过，竟然袭击中央工房，\x01",
            "真是胆大妄为的家伙呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "这种事情可不是\x01",
            "一般的罪犯能做出来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC6")

    Jump("loc_24E1")

    label("loc_1FC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_21AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_20BE")

    ChrTalk(
        0xF,
        (
            "我跟你说，\x01",
            "那个人在我的店里吃饭……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "他的食量\x01",
            "和他的外观一样惊人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "连做饭的材料也都被他吃完了，\x01",
            "那天晚上，队长以下的人都得饿肚子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "哈～哈～哈～\x01",
            "但愿那个人不要再来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21AC")

    label("loc_20BE")

    OP_A2(0x7)

    ChrTalk(
        0xF,
        (
            "对了，\x01",
            "最近这里来了个很高大的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "看起来是从共和国来的，\x01",
            "不过他的体形也太过巨大了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "那种体形看起来\x01",
            "简直就和魔兽一样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21AC")

    Jump("loc_24E1")

    label("loc_21AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2314")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_227B")

    ChrTalk(
        0xF,
        (
            "唉，小的时候\x01",
            "我梦想成为七耀石的输出大王，\x01",
            "还要娶很多老婆……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "实际上却沦落到这样偏远的酒馆，\x01",
            "我的人生已经没有未来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "啊哈哈哈哈。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2311")

    label("loc_227B")

    OP_A2(0x7)

    ChrTalk(
        0xF,
        (
            "我也是在\x01",
            "共和国出生的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "由于种种原因，\x01",
            "现在流落到\x01",
            "这样偏远的酒馆来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "哈～哈～哈，\x01",
            "我的人生已经一片黑暗了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2311")

    Jump("loc_24E1")

    label("loc_2314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_24E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_23D8")

    ChrTalk(
        0xF,
        (
            "欢迎光临\x01",
            "这个一成不变的酒馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "从饮料到简单的饭菜，\x01",
            "希望有合你们胃口的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24E1")

    label("loc_23D8")

    OP_A2(0x7)

    ChrTalk(
        0xF,
        (
            "哎呀哎呀，\x01",
            "真是欢迎你们的到来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "就像你们看到的，\x01",
            "这里是一成不变的关所酒馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "就算想要长住，\x01",
            "也不需要付多余的钱，\x01",
            "完全可以放心住下来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24E1")

    TalkEnd(0xF)
    Return()

    # Function_9_1B17 end

    def Function_10_24E5(): pass

    label("Function_10_24E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_25D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2547")
    TurnDirection(0xFE, 0xA, 400)

    ChrTalk(
        0xFE,
        "喂，卡雷尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "差不多要走了，\x01",
            "赶快准备好行李吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D8")

    label("loc_2547")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "嗯，接下来。\x01",
            "对了，\x01",
            "快点去拿通行许可证吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "到卡尔瓦德还很远，\x01",
            "必须早上就出发。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25D8")

    TalkEnd(0xFE)
    Return()

    # Function_10_24E5 end

    def Function_11_25DC(): pass

    label("Function_11_25DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2A6F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2980")
    OP_A2(0x583)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哟，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F……？\x02\x03",
            "#010F啊，我还以为是谁呢……\x01",
            "真的是好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F嗯？是谁啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F呵呵，就是在洛连特\x01",
            "寻找结晶回路碎片的那个孩子啊。\x02\x03",
            "我们之前不是\x01",
            "接受过他的委托去找那碎片吗。\x02\x03",
            "已经要回共和国了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "是啊，马上就要走了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其实……\x01",
            "我还会再来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我决定等妹妹们\x01",
            "稍微再长大一点，\x01",
            "就回蔡斯这里来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为做见习生就可以进入工房，\x01",
            "将来就可以造飞艇了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的手很巧，\x01",
            "这点连我老妈也是知道的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是吗……\x02\x03",
            "这样也挺不错啊。\x01",
            "已经找到了将来的目标。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那当然的啦。\x01",
            "我也要考虑自己的前途才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……唉，\x01",
            "不过现在还是要先给老妈帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我有四个妹妹，\x01",
            "年纪还都很小呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯！你要努力帮忙哦。\x01",
            "就算是为了你的几个妹妹。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "啊，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "再见了，\x01",
            "你们也加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A6F")

    label("loc_2980")


    ChrTalk(
        0xFE,
        (
            "……我决定，\x01",
            "等我的几个妹妹再长大点之后，\x01",
            "就回蔡斯这里来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为做见习生就可以进入工房，\x01",
            "将来就可以造飞艇了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的手很巧，\x01",
            "这点连我老妈也是知道的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A6F")

    TalkEnd(0xFE)
    Return()

    # Function_11_25DC end

    def Function_12_2A73(): pass

    label("Function_12_2A73")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2B0A")

    ChrTalk(
        0xFE,
        (
            "就这样，\x01",
            "尽量穿成像利贝尔人的样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "怎么样？没有哪点不自然吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B83")

    label("loc_2B0A")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "这里已经是利贝尔王国了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，接下来就到蔡斯了，\x01",
            "再坚持一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B83")

    TalkEnd(0xFE)
    Return()

    # Function_12_2A73 end

    def Function_13_2B87(): pass

    label("Function_13_2B87")

    Call(0, 9)
    Return()

    # Function_13_2B87 end

    SaveToFile()

Try(main)
