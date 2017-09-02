from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4120   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '卡露娜',                               # 9
        '史帕德',                               # 10
        '夏伊',                                 # 11
        '塞森',                                 # 12
        '多姆',                                 # 13
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
        'ED6_DT07/CH01240 ._CH',             # 00
        'ED6_DT07/CH01680 ._CH',             # 01
        'ED6_DT07/CH01690 ._CH',             # 02
        'ED6_DT07/CH01140 ._CH',             # 03
        'ED6_DT07/CH01040 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01240P._CP',             # 00
        'ED6_DT07/CH01680P._CP',             # 01
        'ED6_DT07/CH01690P._CP',             # 02
        'ED6_DT07/CH01140P._CP',             # 03
        'ED6_DT07/CH01040P._CP',             # 04
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
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -1540,
        Z                   = 0,
        Y                   = 69240,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 1260,
        Z                   = 0,
        Y                   = -240,
        Direction           = 236,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 58580,
        Z                   = 0,
        Y                   = 360,
        Direction           = 102,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 120030,
        Z                   = 0,
        Y                   = -1260,
        Direction           = 10,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = -10,
        TriggerZ            = 0,
        TriggerY            = -1600,
        TriggerRange        = 800,
        ActorX              = 1260,
        ActorZ              = 1500,
        ActorY              = -240,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 60410,
        TriggerZ            = 0,
        TriggerY            = 390,
        TriggerRange        = 800,
        ActorX              = 58580,
        ActorZ              = 1500,
        ActorY              = 360,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 119960,
        TriggerZ            = 0,
        TriggerY            = 650,
        TriggerRange        = 800,
        ActorX              = 120030,
        ActorZ              = 1500,
        ActorY              = -1260,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_27D",          # 01, 1
        "Function_2_2CA",          # 02, 2
        "Function_3_2E0",          # 03, 3
        "Function_4_2E5",          # 04, 4
        "Function_5_E87",          # 05, 5
        "Function_6_E8C",          # 06, 6
        "Function_7_1C0A",         # 07, 7
        "Function_8_22F4",         # 08, 8
        "Function_9_22F9",         # 09, 9
        "Function_10_3534",        # 0A, 10
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_200")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 5480, 4000, -2590, 90)

    label("loc_200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_20A")
    Jump("loc_27C")

    label("loc_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_214")
    Jump("loc_27C")

    label("loc_214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_21E")
    Jump("loc_27C")

    label("loc_21E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_228")
    Jump("loc_27C")

    label("loc_228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_232")
    Jump("loc_27C")

    label("loc_232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_23C")
    Jump("loc_27C")

    label("loc_23C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_246")
    Jump("loc_27C")

    label("loc_246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_250")
    Jump("loc_27C")

    label("loc_250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_26B")
    SetChrPos(0x9, 3310, 0, 129900, 0)
    Jump("loc_27C")

    label("loc_26B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_275")
    Jump("loc_27C")

    label("loc_275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_27C")

    label("loc_27C")

    Return()

    # Function_0_1DE end

    def Function_1_27D(): pass

    label("Function_1_27D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B0")
    OP_B1("t4120_y")
    Jump("loc_2B9")

    label("loc_2B0")

    OP_B1("t4120_n")

    label("loc_2B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_2C9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C9")

    Return()

    # Function_1_27D end

    def Function_2_2CA(): pass

    label("Function_2_2CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2CA")

    label("loc_2DF")

    Return()

    # Function_2_2CA end

    def Function_3_2E0(): pass

    label("Function_3_2E0")

    Call(0, 4)
    Return()

    # Function_3_2E0 end

    def Function_4_2E5(): pass

    label("Function_4_2E5")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_381")

    ChrTalk(
        0xC,
        (
            "今天天气不错啊，\x01",
            "和诞辰庆典很合称呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "好的，\x01",
            "今天的工作也要加油干。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E83")

    label("loc_381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3C3")

    ChrTalk(
        0xC,
        (
            "今天的顾客\x01",
            "为何减少了许多呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "发生什么事了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_E83")

    label("loc_3C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_520")

    ChrTalk(
        0xC,
        "必须重视客户的想法。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "如果客户有急需，\x01",
            "就算已经下班了也要接受维修委托。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "我要把这些想法\x01",
            "和塞森交流一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E83")

    label("loc_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5AE")

    ChrTalk(
        0xC,
        "马上就要关店了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "不过，\x01",
            "修理的委托还是要尽快完成，\x01",
            "然后把东西交还给客人才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E83")

    label("loc_5AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_651")

    ChrTalk(
        0xC,
        "今天好像是武术大会的决赛日啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "在客人都去看比赛的这段时间，\x01",
            "我一定要把东西修理好才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E83")

    label("loc_651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_7E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6BB")

    ChrTalk(
        0xC,
        (
            "好像就连空贼\x01",
            "都参加比赛了，\x01",
            "这样好吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E3")

    label("loc_6BB")

    OP_A2(0x3)

    ChrTalk(
        0xC,
        (
            "武术大会\x01",
            "似乎相当热闹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "刚才，\x01",
            "来取商品的客人\x01",
            "都在和我兴奋地谈论这件事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "好像就连空贼\x01",
            "都参加比赛了，\x01",
            "这样好吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E3")

    Jump("loc_E83")

    label("loc_7E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_974")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_84B")

    ChrTalk(
        0xC,
        (
            "对于我来说，\x01",
            "能用自己的技术帮助顾客，\x01",
            "那就是最快乐的事了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_971")

    label("loc_84B")

    OP_A2(0x3)

    ChrTalk(
        0xC,
        (
            "对于我来说，\x01",
            "能用自己的技术帮助顾客，\x01",
            "那就是最快乐的事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "老爷爷爱惜了\x01",
            "一辈子的时钟，\x01",
            "孩子们心爱的玩具……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "每当修理好那些东西时，\x01",
            "他们绽放出的笑颜是我最想看到的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_971")

    Jump("loc_E83")

    label("loc_974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_AE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_A15")

    ChrTalk(
        0xC,
        (
            "本店销售的商品\x01",
            "当然会给您保修……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "就算不是在本店买的商品，\x01",
            "出问题了也可以拿来修理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE4")

    label("loc_A15")

    OP_A2(0x3)

    ChrTalk(
        0xC,
        (
            "我会尽量根据顾客的意见\x01",
            "来满足他们的要求。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "对销售的商品\x01",
            "进行修理和维护……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "就算不是在本店买的商品，\x01",
            "出问题了也可以拿来修理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE4")

    Jump("loc_E83")

    label("loc_AE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_CA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_B9C")

    ChrTalk(
        0xC,
        (
            "虽然我很想去看武术大会，\x01",
            "但还有修理的任务要做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "要优先处理顾客的委托。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CA5")

    label("loc_B9C")

    OP_A2(0x3)

    ChrTalk(
        0xC,
        "今天开始大会就进入正式赛了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "虽然我很想去看，\x01",
            "但还有修理的任务要做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "要优先处理顾客的委托。\x02",
    )

    CloseMessageWindow()

    label("loc_CA5")

    Jump("loc_E83")

    label("loc_CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_DB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D11")

    ChrTalk(
        0xC,
        (
            "我还以为今年的武术大会\x01",
            "肯定要取消呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DAF")

    label("loc_D11")

    OP_A2(0x3)

    ChrTalk(
        0xC,
        (
            "政变的混乱和女王陛下的卧病在床\x01",
            "好像并没有带来太大的影响。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "我还以为今年的武术大会\x01",
            "肯定要取消呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DAF")

    Jump("loc_E83")

    label("loc_DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_E83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E0C")

    ChrTalk(
        0xC,
        (
            "这个『文加尔德工房』的三楼\x01",
            "是负责修理和维护的地方。\x01",
            "请好好利用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E83")

    label("loc_E0C")

    OP_A2(0x3)

    ChrTalk(
        0xC,
        "您好，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "这个『文加尔德工房』的三楼\x01",
            "是负责修理和维护的地方。\x01",
            "请好好利用。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E83")

    TalkEnd(0xC)
    Return()

    # Function_4_2E5 end

    def Function_5_E87(): pass

    label("Function_5_E87")

    Call(0, 6)
    Return()

    # Function_5_E87 end

    def Function_6_E8C(): pass

    label("Function_6_E8C")

    TalkBegin(0xB)
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
            "离开\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF7")
    OP_0D()
    OP_A9(0x5A)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_EF7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F08")
    TalkEnd(0xB)
    Return()

    label("loc_F08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1027")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F56")

    ChrTalk(
        0xB,
        (
            "女王陛下的病好了，\x01",
            "让人非常欣慰啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1024")

    label("loc_F56")

    OP_A2(0x2)

    ChrTalk(
        0xB,
        "街上一热闹，这里的客人也会增加。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "诞辰庆典的销售额\x01",
            "应该会比平常高出五倍以上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "女王陛下的病好了，\x01",
            "让人非常欣慰啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1024")

    Jump("loc_1C06")

    label("loc_1027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_10AF")

    ChrTalk(
        0xB,
        (
            "王国军为了\x01",
            "防止政变而加强了警戒，\x01",
            "所以顾客减少了很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "真是的……\x01",
            "没想到会这样啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C06")

    label("loc_10AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_123F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_114E")

    ChrTalk(
        0xB,
        (
            "希望这种势头能持续到诞辰庆典，\x01",
            "这样就可以大赚特赚了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_123C")

    label("loc_114E")

    OP_A2(0x2)

    ChrTalk(
        0xB,
        (
            "哎呀，武术大会期间，\x01",
            "每天的营业额相当可观啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "希望这种势头能持续到诞辰庆典，\x01",
            "这样就可以大赚特赚了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_123C")

    Jump("loc_1C06")

    label("loc_123F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_12BF")

    ChrTalk(
        0xB,
        (
            "好了，\x01",
            "差不多该关店门了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "今天赚了多少钱呢？\x01",
            "我已经迫不及待要去结算了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C06")

    label("loc_12BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1499")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1391")

    ChrTalk(
        0xB,
        (
            "请你们使用我们店里的结晶回路\x01",
            "来获得最后的胜利吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "这样的话，\x01",
            "本店既能赚钱又能得到宣传，\x01",
            "真可谓是一举两得的妙计。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1496")

    label("loc_1391")

    OP_A2(0x2)

    ChrTalk(
        0xB,
        (
            "你们不就是要出战\x01",
            "今天总决赛的游击士组吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "那么就使用我们店里的结晶回路\x01",
            "来获得最后的胜利吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "这样的话，\x01",
            "本店既能赚钱又能得到宣传，\x01",
            "真可谓是一举两得的妙计。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1496")

    Jump("loc_1C06")

    label("loc_1499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_15AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1502")

    ChrTalk(
        0xB,
        (
            "对我而言，\x01",
            "最期待的还是明天能赚多少钱。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15AA")

    label("loc_1502")

    OP_A2(0x2)

    ChrTalk(
        0xB,
        (
            "虽然很想知道谁会取胜，\x01",
            "不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "对我而言，\x01",
            "最期待的还是明天能赚多少钱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15AA")

    Jump("loc_1C06")

    label("loc_15AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_16B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1622")

    ChrTalk(
        0xB,
        (
            "这家店是我和从小长大的\x01",
            "好友多姆一同经营的，\x01",
            "不过工作上的想法总是合不到一起。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16AF")

    label("loc_1622")

    OP_A2(0x2)

    ChrTalk(
        0xB,
        (
            "这家店是我和从小长大的\x01",
            "好友多姆一同经营的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "那家伙很有本事哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "不过，作为同事而言\x01",
            "就不是那么投缘了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16AF")

    Jump("loc_1C06")

    label("loc_16B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_183B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1756")

    ChrTalk(
        0xB,
        (
            "武术大会期间，\x01",
            "大部分委托都是修理和改造。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "还是新商品的销售\x01",
            "更能够盈利啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1838")

    label("loc_1756")

    OP_A2(0x2)

    ChrTalk(
        0xB,
        (
            "虽说武术大会\x01",
            "带来了很多顾客……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "但实际上，\x01",
            "大部分人主要是来\x01",
            "委托我们进行修理和改造。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "还是新商品的销售\x01",
            "更能够盈利啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1838")

    Jump("loc_1C06")

    label("loc_183B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_19EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_18E3")

    ChrTalk(
        0xB,
        (
            "一定要用我们的结晶回路\x01",
            "作为武器去获得胜利。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "这样对本店也是个很好的宣传。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19EC")

    label("loc_18E3")

    OP_A2(0x2)

    ChrTalk(
        0xB,
        (
            "难道说你们要\x01",
            "在武术大会当中出场吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我正准备关门，\x01",
            "去竞技场观战呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "请一定要用我们的结晶回路\x01",
            "作为武器去获得胜利。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "这样对本店也是个很好的宣传。\x02",
    )

    CloseMessageWindow()

    label("loc_19EC")

    Jump("loc_1C06")

    label("loc_19EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1A8F")

    ChrTalk(
        0xB,
        (
            "由于没有亲卫队来关照，\x01",
            "这里的生意都开始萧条了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "他们怎么会去做发动政变这种\x01",
            "毫无价值可言的事情呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C06")

    label("loc_1A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1C06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1B59")

    ChrTalk(
        0xB,
        (
            "导力器的相关事宜一定要\x01",
            "交给我们『文加尔德工房』来处理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "相信我准没错，\x01",
            "不会让你们失望的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C06")

    label("loc_1B59")

    OP_A2(0x2)

    ChrTalk(
        0xB,
        "哦，你们是游击士吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "如果是的话，导力器的相关事宜一定要\x01",
            "交给我们『文加尔德工房』来处理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "相信我准没错，\x01",
            "这里不会让你们失望的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C06")

    TalkEnd(0xB)
    Return()

    # Function_6_E8C end

    def Function_7_1C0A(): pass

    label("Function_7_1C0A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1C37")

    ChrTalk(
        0xFE,
        (
            "今天外面\x01",
            "实在是很热闹啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F0")

    label("loc_1C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1CA2")

    ChrTalk(
        0xFE,
        (
            "我刚才在外面看到了……\x01",
            "那些黑衣士兵也是王国军吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是令人感到\x01",
            "可怕的一群家伙……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F0")

    label("loc_1CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1CFE")

    ChrTalk(
        0xFE,
        (
            "……武术大会\x01",
            "才刚刚结束，\x01",
            "街上也太过太安静些了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F0")

    label("loc_1CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1D6D")

    ChrTalk(
        0xFE,
        (
            "……大会结束了，\x01",
            "店里也稍微冷清了些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "今天好像可以悠闲一会儿了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_22F0")

    label("loc_1D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1E25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1DAD")

    ChrTalk(
        0xFE,
        (
            "我也想让\x01",
            "自己的口才变好一些……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E22")

    label("loc_1DAD")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "唉，我也想让\x01",
            "自己的口才变好一些……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总是不知道\x01",
            "在别人面前说什么才好……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E22")

    Jump("loc_22F0")

    label("loc_1E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1E94")

    ChrTalk(
        0xFE,
        "明天要和妻子一起外出了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天就把这里的事情\x01",
            "全部摆平吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F0")

    label("loc_1E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2003")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F49")

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "现在商品的数量已经足够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有这么多库存的话，\x01",
            "撑到诞辰庆典结束应该没问题。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2000")

    label("loc_1F49")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "……前几天来的那些戴手铐的人，\x01",
            "好像也是大赛选手呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没想到他们竟然是\x01",
            "柏斯事件的犯人……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2000")

    Jump("loc_22F0")

    label("loc_2003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_20D1")

    ChrTalk(
        0xFE,
        (
            "大会开始以后，\x01",
            "就会有许多选手前来光顾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以要在大会前\x01",
            "进一些好装备……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F0")

    label("loc_20D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2193")

    ChrTalk(
        0xFE,
        (
            "得去进一些\x01",
            "导力炮和导力枪了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "昨天来的客人\x01",
            "买了不少这类的武器……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "让本店的库存都清空了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22F0")

    label("loc_2193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_21F6")

    ChrTalk(
        0xFE,
        (
            "……欢迎光临，\x01",
            "请随便看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F0")

    label("loc_21F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_22F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2273")

    ChrTalk(
        0xFE,
        "我不太会接待客人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近店铺都是\x01",
            "交给妻子打理的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F0")

    label("loc_2273")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "……欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我不太会接待客人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近店铺都是\x01",
            "交给妻子打理的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22F0")

    TalkEnd(0xFE)
    Return()

    # Function_7_1C0A end

    def Function_8_22F4(): pass

    label("Function_8_22F4")

    Call(0, 9)
    Return()

    # Function_8_22F4 end

    def Function_9_22F9(): pass

    label("Function_9_22F9")

    TalkBegin(0xA)
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
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2365")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_235A")
    OP_A9(0x60)
    Jump("loc_235C")

    label("loc_235A")

    OP_A9(0x5B)

    label("loc_235C")

    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_2365")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2376")
    TalkEnd(0xA)
    Return()

    label("loc_2376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2464")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_END)), "loc_23D8")

    ChrTalk(
        0xA,
        (
            "女王陛下的病治好了，\x01",
            "真是太令人欣慰了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "这样一来利贝尔就可以国泰民安了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2461")

    label("loc_23D8")


    ChrTalk(
        0xA,
        (
            "女王陛下和科洛蒂娅公主\x01",
            "真是气质优雅啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "女王陛下的病治好了，\x01",
            "真是太令人欣慰了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "这样一来利贝尔就可以国泰民安了。\x02",
    )

    CloseMessageWindow()

    label("loc_2461")

    Jump("loc_3530")

    label("loc_2464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_24CF")

    ChrTalk(
        0xA,
        (
            "今天的天气\x01",
            "虽然一点都不差，\x01",
            "但却没有什么顾客啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3530")

    label("loc_24CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_260D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_END)), "loc_2544")

    ChrTalk(
        0xA,
        (
            "据说女王陛下也是有病在身，\x01",
            "诞辰庆典到底会怎么样啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_260A")

    label("loc_2544")


    ChrTalk(
        0xA,
        (
            "最近在街上经常能够\x01",
            "见到穿黑衣服的士兵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "兵荒马乱啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "据说女王陛下也是有病在身，\x01",
            "诞辰庆典到底会怎么样啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_260A")

    Jump("loc_3530")

    label("loc_260D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2890")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_END)), "loc_278E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_26A1")

    ChrTalk(
        0xA,
        (
            "真是这几年里\x01",
            "难得一见的激战啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我真是太感动了。\x01",
            "我已经完全成为你们的支持者了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_278B")

    label("loc_26A1")

    OP_A2(0x1)

    ChrTalk(
        0xA,
        "你们干得太棒啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "恭喜你们获得优胜。\x01",
            "比赛很精彩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "真是这几年里\x01",
            "难得一见的激战啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "啊～我太感动了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我已经完全\x01",
            "成为你们的支持者了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_278B")

    Jump("loc_288D")

    label("loc_278E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_27F4")

    ChrTalk(
        0xA,
        "今天的决赛很精彩呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "没有工作\x01",
            "而去观看比赛真是值得。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_288D")

    label("loc_27F4")

    OP_A2(0x1)

    ChrTalk(
        0xA,
        "今天的决赛很精彩呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我想是这几年里\x01",
            "最棒的比赛了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "没有工作\x01",
            "而去观看比赛真是值得。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_288D")

    Jump("loc_3530")

    label("loc_2890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_29B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_END)), "loc_2941")

    ChrTalk(
        0xA,
        (
            "啊，是你们……\x01",
            "今天终于要进行决赛了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我们一会儿就暂停营业\x01",
            "去赛场给你们加油！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B3")

    label("loc_2941")


    ChrTalk(
        0xA,
        "今天是大会的第二天呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "啊啊，\x01",
            "我也想到大会现场去看看呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29B3")

    Jump("loc_3530")

    label("loc_29B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2D1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2A25")

    ChrTalk(
        0xA,
        (
            "为了明天的决赛，\x01",
            "你们今天要好好休息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D17")

    label("loc_2A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C93")
    OP_A2(0x1)
    OP_A2(0x67B)

    ChrTalk(
        0xA,
        "啊，你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "干得真不错！\x01",
            "恭喜你们进入决赛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，谢谢～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "今天的比赛\x01",
            "真是白热化呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "作为你们的支持者，我也很自豪。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嘿嘿，\x01",
            "总算战胜了游击士前辈们，\x01",
            "这样离冠军就是一步之遥了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F（又立刻得意忘形起来了……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "嗯嗯，已经到这一步了，\x01",
            "就一定要取得优胜啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "总之，你们一定要加油！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D17")

    label("loc_2C93")

    OP_A2(0x1)

    ChrTalk(
        0xA,
        (
            "今天比赛的看点\x01",
            "好像非常多呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "从街道上沸腾的气氛中\x01",
            "就可以感觉得到。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D17")

    Jump("loc_3530")

    label("loc_2D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_30E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_END)), "loc_2D9B")

    ChrTalk(
        0xA,
        (
            "我决定决赛那天\x01",
            "歇业去看比赛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "为了晋级决赛，\x01",
            "要加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30E0")

    label("loc_2D9B")

    OP_A2(0x67A)

    ChrTalk(
        0xA,
        "啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "莫非你们是\x01",
            "武术大会的选手？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#073F唔，是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "啊，果然！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "就是传说中的那个由壮汉、\x01",
            "少年、还有少女组成的队伍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我决定今年\x01",
            "替你们加油啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F哈、哈哈，\x01",
            "真是非常感谢啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "嗯嗯，\x01",
            "那么我想要你们的签名可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F签、签名！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F总觉得有点难为情……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "因为平时要看店，\x01",
            "不能去竞技场呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我决定决赛那天\x01",
            "歇业去看比赛哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "你们请一定要努力。\x01",
            "一定要让我看到\x01",
            "你们的精彩比赛啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嗯，虽说选手中高手如云，\x01",
            "但我们保证一定会全力以赴的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30E0")

    Jump("loc_3530")

    label("loc_30E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_31BA")

    ChrTalk(
        0xA,
        (
            "武术大会总是会有\x01",
            "引人注目的军队成员，\x01",
            "今年好像也有许多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "究竟哪个小组会取得优胜\x01",
            "我真是十分期待啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3530")

    label("loc_31BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_334E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_326F")

    ChrTalk(
        0xA,
        (
            "昨天士兵押送的\x01",
            "几个戴手铐的人来了这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "按照常理，做了坏事被捕的人\x01",
            "怎么能来买武器呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_334B")

    label("loc_326F")

    OP_A2(0x1)

    ChrTalk(
        0xA,
        (
            "昨天士兵押送的\x01",
            "几个戴手铐的人来了这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "按照常理，做了坏事被捕的人\x01",
            "怎么能来买武器呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "究竟要干什么？\x01",
            "有点可怕……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_334B")

    Jump("loc_3530")

    label("loc_334E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_34E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_33F4")

    ChrTalk(
        0xA,
        (
            "亲卫队的中队长也\x01",
            "经常到这里来光顾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "她是一位时常关心着\x01",
            "女王陛下的好人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34DD")

    label("loc_33F4")

    OP_A2(0x1)

    ChrTalk(
        0xA,
        (
            "不管怎样，\x01",
            "我还是不相信亲卫队的人是恐怖分子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "那位中队长也\x01",
            "经常到这里来光顾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "她是一位时常关心着\x01",
            "女王陛下的好人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34DD")

    Jump("loc_3530")

    label("loc_34E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3530")

    ChrTalk(
        0xA,
        "欢迎光临，各位游击士。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "请慢慢挑选吧。\x02",
    )

    CloseMessageWindow()

    label("loc_3530")

    TalkEnd(0xA)
    Return()

    # Function_9_22F9 end

    def Function_10_3534(): pass

    label("Function_10_3534")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38CC")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(4690, 4000, -2480, 0)
    SetChrPos(0x101, 4350, 4000, -2160, 90)
    SetChrPos(0x102, 4390, 4000, -3250, 90)
    SetChrPos(0x108, 3200, 4000, -2630, 90)
    TurnDirection(0x8, 0x108, 0)
    OP_A2(0x64B)
    OP_28(0x4B, 0x1, 0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x80)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35C7")
    OP_28(0x4B, 0x1, 0x100)

    label("loc_35C7")

    OP_0D()
    SetChrSubChip(0xFE, 0)

    ChrTalk(
        0x101,
        "#004F啊，卡露娜姐姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#830F哦，是你们啊。\x02\x03",
            "金大哥也在，\x01",
            "到底有什么事呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#074F实际上，\x01",
            "发生了一件十分棘手的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#832F……什么？\x01",
            "究竟是怎么回事。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们向卡露娜说明了\x01",
            "至今为止发生的事情和女王的委托。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#832F…………………………\x02\x03",
            "……唔……\x01",
            "这可不能开玩笑的啊。\x02\x03",
            "#833F关所和飞艇坪被封锁，\x01",
            "虽然我从其中也嗅出了一些火药味……\x02\x03",
            "#832F事情明白了。\x01",
            "我该怎么做？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F首先大家要集中在一起，\x01",
            "然后商量和制定作战计划。\x02\x03",
            "请回游击士协会去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#832F知道了。\x02\x03",
            "那我就先行一步了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3850():

        label("loc_3850")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3850")

    QueueWorkItem2(0x101, 1, lambda_3850)

    def lambda_3861():

        label("loc_3861")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3861")

    QueueWorkItem2(0x102, 1, lambda_3861)

    def lambda_3872():

        label("loc_3872")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3872")

    QueueWorkItem2(0x108, 1, lambda_3872)
    OP_8E(0x8, 0x1522, 0xFA0, 0x276, 0xFA0, 0x0)
    OP_8E(0x8, 0xC58, 0xFA0, 0x9F6, 0xFA0, 0x0)
    OP_8E(0x8, 0xFFFFF254, 0x0, 0x9F6, 0xFA0, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    EventEnd(0x0)

    label("loc_38CC")

    TalkEnd(0x8)
    Return()

    # Function_10_3534 end

    SaveToFile()

Try(main)
