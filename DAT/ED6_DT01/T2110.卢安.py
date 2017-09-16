from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2110   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        '利顿',                                 # 9
        '希艾尔',                               # 10
        '爱蕾塔',                               # 11
        '基诺奇奥',                             # 12
        '连茨',                                 # 13
        '丽泽',                                 # 14
        '托尼奥',                               # 15
        '波尔多斯',                             # 16
        '诺莉雅',                               # 17
        '罗基克',                               # 18
        '诺曼',                                 # 19
        '布莉洁特',                             # 20
        '路易',                                 # 21
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
        'ED6_DT07/CH01290 ._CH',             # 00
        'ED6_DT07/CH01540 ._CH',             # 01
        'ED6_DT07/CH01170 ._CH',             # 02
        'ED6_DT07/CH01080 ._CH',             # 03
        'ED6_DT07/CH01460 ._CH',             # 04
        'ED6_DT07/CH01030 ._CH',             # 05
        'ED6_DT07/CH01040 ._CH',             # 06
        'ED6_DT07/CH01680 ._CH',             # 07
        'ED6_DT07/CH01690 ._CH',             # 08
        'ED6_DT07/CH01083 ._CH',             # 09
        'ED6_DT07/CH01200 ._CH',             # 0A
        'ED6_DT07/CH01230 ._CH',             # 0B
        'ED6_DT07/CH01470 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH01290P._CP',             # 00
        'ED6_DT07/CH01540P._CP',             # 01
        'ED6_DT07/CH01170P._CP',             # 02
        'ED6_DT07/CH01080P._CP',             # 03
        'ED6_DT07/CH01460P._CP',             # 04
        'ED6_DT07/CH01030P._CP',             # 05
        'ED6_DT07/CH01040P._CP',             # 06
        'ED6_DT07/CH01680P._CP',             # 07
        'ED6_DT07/CH01690P._CP',             # 08
        'ED6_DT07/CH01083P._CP',             # 09
        'ED6_DT07/CH01200P._CP',             # 0A
        'ED6_DT07/CH01230P._CP',             # 0B
        'ED6_DT07/CH01470P._CP',             # 0C
    )

    DeclNpc(
        X                   = 2009,
        Z                   = 0,
        Y                   = -1890,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -5910,
        Z                   = 0,
        Y                   = 5190,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -4500,
        Z                   = 4000,
        Y                   = 5750,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 1670,
        Z                   = 0,
        Y                   = 1890,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 22050,
        Z                   = 0,
        Y                   = -200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 27240,
        Z                   = 0,
        Y                   = -1510,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 26000,
        Z                   = 4000,
        Y                   = -500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 25980,
        Z                   = 0,
        Y                   = 34030,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -2270,
        Z                   = 0,
        Y                   = 37540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -2960,
        Z                   = 0,
        Y                   = 33440,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -31900,
        Z                   = 0,
        Y                   = 63600,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 24980,
        Z                   = 0,
        Y                   = 62760,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 4990,
        Z                   = 0,
        Y                   = 64730,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )


    ScpFunction(
        "Function_0_2B2",          # 00, 0
        "Function_1_328",          # 01, 1
        "Function_2_353",          # 02, 2
        "Function_3_369",          # 03, 3
        "Function_4_38D",          # 04, 4
        "Function_5_8FF",          # 05, 5
        "Function_6_FBA",          # 06, 6
        "Function_7_14AF",         # 07, 7
        "Function_8_15F7",         # 08, 8
        "Function_9_1E65",         # 09, 9
        "Function_10_269C",        # 0A, 10
        "Function_11_2DAF",        # 0B, 11
        "Function_12_2EA6",        # 0C, 12
        "Function_13_35D1",        # 0D, 13
        "Function_14_3670",        # 0E, 14
        "Function_15_3E4C",        # 0F, 15
        "Function_16_41C8",        # 10, 16
    )


    def Function_0_2B2(): pass

    label("Function_0_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2C6")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    Jump("loc_327")

    label("loc_2C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2EE")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    Jump("loc_327")

    label("loc_2EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_302")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_327")

    label("loc_302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_327")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)

    label("loc_327")

    Return()

    # Function_0_2B2 end

    def Function_1_328(): pass

    label("Function_1_328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_349")
    OP_B1("t2110_y")
    Jump("loc_352")

    label("loc_349")

    OP_B1("t2110_n")

    label("loc_352")

    Return()

    # Function_1_328 end

    def Function_2_353(): pass

    label("Function_2_353")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_368")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_353")

    label("loc_368")

    Return()

    # Function_2_353 end

    def Function_3_369(): pass

    label("Function_3_369")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38C")
    OP_8D(0xFE, 22020, 37800, 27710, 33160, 1500)
    Jump("Function_3_369")

    label("loc_38C")

    Return()

    # Function_3_369 end

    def Function_4_38D(): pass

    label("Function_4_38D")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_45E")

    ChrTalk(
        0xFE,
        (
            "主张推进旅游业的市长\x01",
            "已经被逮捕了，\x01",
            "城市的形象也受到了损失。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "旅游和住宿的预约\x01",
            "都大大减少了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FB")

    label("loc_45E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_5B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52B")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "我原来是个渔夫。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，市长换任之后，\x01",
            "城里就开始盛行观光业了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "经过妻子的劝说，\x01",
            "我就开始从事导游的工作了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B4")

    label("loc_52B")


    ChrTalk(
        0xFE,
        (
            "市长换任之后，\x01",
            "城里就开始盛行观光业了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "经过妻子的劝说，\x01",
            "我就开始从事导游的工作了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B4")

    Jump("loc_8FB")

    label("loc_5B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_64F")

    ChrTalk(
        0xFE,
        (
            "我去参观了\x01",
            "儿子学校的学园祭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正好我休息，\x01",
            "我女儿也很高兴。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FB")

    label("loc_64F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_78C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70D")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "嗯～下一个工作计划是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……工作繁忙\x01",
            "也是件很开心的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只是留守在家里的女儿很寂寞，\x01",
            "我有点担心她啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_789")

    label("loc_70D")


    ChrTalk(
        0xFE,
        (
            "……工作繁忙\x01",
            "也是件很开心的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只是留守在家里的女儿很寂寞，\x01",
            "我有点担心她啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_789")

    Jump("loc_8FB")

    label("loc_78C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_8FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_886")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "今天的观光客特别多呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从远方特地来这里\x01",
            "观光的人也增加了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "投注在导游工作里的精力\x01",
            "比当渔夫的时候还要多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FB")

    label("loc_886")


    ChrTalk(
        0xFE,
        (
            "投注在导游工作里的精力\x01",
            "比当渔夫的时候还要多。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FB")

    TalkEnd(0x8)
    Return()

    # Function_4_38D end

    def Function_5_8FF(): pass

    label("Function_5_8FF")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_998")

    ChrTalk(
        0xFE,
        (
            "虽然新任市长\x01",
            "还没有定下来，\x01",
            "但我认为诺曼先生不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果由他来的话，\x01",
            "这里作为观光都市\x01",
            "一定会飞速向前发展的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB6")

    label("loc_998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_B34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A91")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "布朗西酒店的老板\x01",
            "名字叫做诺曼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他是个很有才干的人，\x01",
            "买下了一间普通的旅店，\x01",
            "改建成现在的酒店了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他和市长也很合得来，\x01",
            "在我们的导游工作方面\x01",
            "也帮了我们不少忙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B31")

    label("loc_A91")


    ChrTalk(
        0xFE,
        (
            "布朗西酒店的老板\x01",
            "名字叫做诺曼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他和市长也很合得来，\x01",
            "在我们的导游工作方面\x01",
            "也帮了我们不少忙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B31")

    Jump("loc_FB6")

    label("loc_B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_CA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C57")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "那出剧真是杰作。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，非常可惜，\x01",
            "我儿子没有出场呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了，\x01",
            "只要他认真念书就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA4")

    label("loc_C57")


    ChrTalk(
        0xFE,
        (
            "我去参观儿子的学园祭了呢。\x01",
            "那出剧真是杰作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA4")

    Jump("loc_FB6")

    label("loc_CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_E23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBD")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "学园祭当天的工作，\x01",
            "我准备全部推掉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "之前也给爱蕾塔\x01",
            "添了很多麻烦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "什么才是最重要的事情，\x01",
            "想来想去还是家庭啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E20")

    label("loc_DBD")


    ChrTalk(
        0xFE,
        (
            "为了家庭\x01",
            "而拼命工作的我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "却恰恰错失了最重要的东西。\x02",
    )

    CloseMessageWindow()

    label("loc_E20")

    Jump("loc_FB6")

    label("loc_E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_FB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F17")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "我们夫妻俩\x01",
            "一起在做导游的工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我丈夫本来是一个渔夫，\x01",
            "但是最近做导游的收入很不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从大儿子进入王立学院念书，\x01",
            "家里的开销就大大增加了。 \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB6")

    label("loc_F17")


    ChrTalk(
        0xFE,
        (
            "丈夫好像更愿意\x01",
            "继续当一个渔夫……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从大儿子进入王立学院念书，\x01",
            "家里的开销就大大增加了。 \x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB6")

    TalkEnd(0x9)
    Return()

    # Function_5_8FF end

    def Function_6_FBA(): pass

    label("Function_6_FBA")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_101B")

    ChrTalk(
        0xFE,
        (
            "爸爸和妈妈\x01",
            "今天都在家，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "能不能陪我好好玩玩呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_14AB")

    label("loc_101B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1085")

    ChrTalk(
        0xFE,
        (
            "今天爸爸和妈妈都没有工作，\x01",
            "在家里休息呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "这下子他们可以陪我好好玩了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14AB")

    label("loc_1085")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_11A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1134")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "哥哥的学校有好多摊子，\x01",
            "舞台剧也很好看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "提到要去见哥哥，\x01",
            "不知怎的，我有点害羞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "为什么呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_119D")

    label("loc_1134")


    ChrTalk(
        0xFE,
        (
            "之前，\x01",
            "我到哥哥的学校去玩了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "提到要去见哥哥，\x01",
            "不知怎的，我有点害羞了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_119D")

    Jump("loc_14AB")

    label("loc_11A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1235")

    ChrTalk(
        0xFE,
        "嘿嘿……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次我们全家\x01",
            "都要去哥哥的学校玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "妈妈也陪我们一起去。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嘿嘿，好开心啊⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_14AB")

    label("loc_1235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1298")

    ChrTalk(
        0xFE,
        (
            "啊啊，终于把衣服洗完，\x01",
            "房间也打扫干净了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "希望大家\x01",
            "都能早点回来啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14AB")

    label("loc_1298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1369")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1345")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "今天是爱蕾塔一个人看家。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "爸爸和妈妈要工作，\x01",
            "哥哥去学校上课了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……唉，好寂寞呀。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1366")

    label("loc_1345")


    ChrTalk(
        0xFE,
        "……唉，好寂寞呀。\x02",
    )

    CloseMessageWindow()

    label("loc_1366")

    Jump("loc_14AB")

    label("loc_1369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_1417")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13E1")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "明天又是\x01",
            "我一个人在家啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "爱蕾塔真希望\x01",
            "能够早点在主日学校交到朋友。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1414")

    label("loc_13E1")


    ChrTalk(
        0xFE,
        (
            "爱蕾塔真希望\x01",
            "能够早点在主日学校交到朋友……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1414")

    Jump("loc_14AB")

    label("loc_1417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_14AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_147F")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "我终于把该洗的衣服都洗完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天啊，\x01",
            "哥哥来帮我干活了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14AB")

    label("loc_147F")


    ChrTalk(
        0xFE,
        (
            "爸爸和妈妈\x01",
            "今天也要工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14AB")

    TalkEnd(0xA)
    Return()

    # Function_6_FBA end

    def Function_7_14AF(): pass

    label("Function_7_14AF")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_1526")

    ChrTalk(
        0xFE,
        (
            "好～\x01",
            "明天要上的课已经预习完了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "找点其它事情做吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_15F3")

    label("loc_1526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_15F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C7")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "在学校开始上课前，\x01",
            "要先做好预习才行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "把该做的事情做好，\x01",
            "才不会引来别人的不满。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这是我的座右铭。\x02",
    )

    CloseMessageWindow()
    Jump("loc_15F3")

    label("loc_15C7")


    ChrTalk(
        0xFE,
        (
            "在学校开始上课前，\x01",
            "要先做好预习才行……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F3")

    TalkEnd(0xB)
    Return()

    # Function_7_14AF end

    def Function_8_15F7(): pass

    label("Function_8_15F7")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1698")

    ChrTalk(
        0xFE,
        (
            "戴尔蒙市长竟然\x01",
            "做出了这种事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我本以为他还算有些男子汉气概，\x01",
            "真是看走眼了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E61")

    label("loc_1698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_171A")

    ChrTalk(
        0xFE,
        (
            "要去王立学院念书的话，\x01",
            "是不是要花费很多的米拉？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我妻子她\x01",
            "到底想怎么做呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E61")

    label("loc_171A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_1874")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E3")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "我是被她\x01",
            "强行拉去王立学院的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要进修的话，\x01",
            "那里也许是个不错的选择。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，我想还是要\x01",
            "看孩子他自己的想法才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1871")

    label("loc_17E3")


    ChrTalk(
        0xFE,
        (
            "要进修的话，\x01",
            "王立学院也许是个不错的选择。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，我想还是要\x01",
            "看孩子他自己的想法才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1871")

    Jump("loc_1E61")

    label("loc_1874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1904")

    ChrTalk(
        0xFE,
        "学园祭就是指祭祀典礼吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为什么学校\x01",
            "要举行这样的活动呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E61")

    label("loc_1904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1A6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A00")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "虽然调查一下王立学院\x01",
            "也没什么损失……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在那之前，\x01",
            "不是应该尊重一下孩子的想法吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_198C():
        TurnDirection(0xD, 0xC, 1000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_198C)

    ChrTalk(
        0xD,
        "你在说什么？\x02",
    )

    CloseMessageWindow()

    def lambda_19AE():
        TurnDirection(0xC, 0xD, 1000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_19AE)
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "没～有，什么都没有。\x02",
    )

    CloseMessageWindow()

    def lambda_19E4():
        OP_8C(0xD, 0, 1000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_19E4)
    Sleep(700)

    ChrTalk(
        0xFE,
        "呼……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A6C")

    label("loc_1A00")


    ChrTalk(
        0xFE,
        (
            "虽然调查一下王立学院\x01",
            "也没什么损失……\x02\x03",
            "在那之前，\x01",
            "不是应该尊重一下孩子的想法吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A6C")

    Jump("loc_1E61")

    label("loc_1A6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1C51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BAD")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "对于儿子的将来，\x01",
            "我又重新考虑过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在我不再强求他，\x01",
            "无论他继承我的事业还是去上学，\x01",
            "我都会支持他的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要他有他自己的目标，\x01",
            "堂堂正正地活下去，\x01",
            "这样就足够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只是完全把这些事情\x01",
            "全都交给他自己，\x01",
            "我很难说出口啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C4E")

    label("loc_1BAD")


    ChrTalk(
        0xFE,
        (
            "只要儿子有自己的目标，\x01",
            "堂堂正正地活下去，\x01",
            "这样就足够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只是完全把这些事情\x01",
            "全都交给他自己，\x01",
            "我很难说出口啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C4E")

    Jump("loc_1E61")

    label("loc_1C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_1CF4")

    ChrTalk(
        0xFE,
        (
            "我拥有身为船员的骄傲，\x01",
            "生活得十分满足。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我觉得不用念什么书，\x01",
            "只要活得像个男子汉，\x01",
            "也可以生存下去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E61")

    label("loc_1CF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1E61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DE1")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "卢安原本就是个\x01",
            "船员与渔夫聚集的城市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是一个云集了\x01",
            "在海上生活的男子汉的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也希望儿子能够\x01",
            "做个像样的海上男儿。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E61")

    label("loc_1DE1")


    ChrTalk(
        0xFE,
        (
            "卢安原本就是个\x01",
            "船员与渔夫聚集的城市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也希望儿子能够\x01",
            "做个像样的海上男儿。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E61")

    TalkEnd(0xC)
    Return()

    # Function_8_15F7 end

    def Function_9_1E65(): pass

    label("Function_9_1E65")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1EF2")

    ChrTalk(
        0xFE,
        (
            "虽然市长的事件\x01",
            "引起了很大的骚动……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过必须让我的儿子\x01",
            "集中精力准备考试。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2698")

    label("loc_1EF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2047")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FBE")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "对啊对啊，\x01",
            "妮吉塔也是王立学院的学生呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可以去问一下\x01",
            "考试到底是什么样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过去问隔壁的太太\x01",
            "总有那么点不太甘心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2044")

    label("loc_1FBE")


    ChrTalk(
        0xFE,
        (
            "对啊对啊，\x01",
            "妮吉塔也是王立学院的学生呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可以去问一下\x01",
            "考试到底是什么样的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2044")

    Jump("loc_2698")

    label("loc_2047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_2216")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2184")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "我去王立学院侦察过了。\x01",
            "不愧是一所名校啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然只是一场学园祭，\x01",
            "但是仍让人感到学校优越的氛围啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我要想方设法让托尼奥\x01",
            "能够穿上那里的校服。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2213")

    label("loc_2184")


    ChrTalk(
        0xFE,
        "我去王立学院侦察过了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我要想方设法让托尼奥\x01",
            "能够穿上那里的校服。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2213")

    Jump("loc_2698")

    label("loc_2216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2379")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22DF")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "最近王立学院要举行学园祭。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这是个好机会，\x01",
            "可以让我参观一下孩子将来要上学的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一定要带我去呀。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2376")

    label("loc_22DF")


    ChrTalk(
        0xFE,
        "最近王立学院要举行学园祭。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这是个好机会，\x01",
            "可以让我参观一下孩子将来要上学的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2376")

    Jump("loc_2698")

    label("loc_2379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_242E")

    ChrTalk(
        0xFE,
        (
            "听说希望进入王立学院的人\x01",
            "每年都在增加。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因此入学考试\x01",
            "也变得越来越难了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "对此我真是着急啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2698")

    label("loc_242E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_24D1")

    ChrTalk(
        0xFE,
        (
            "王立学院的入学考试\x01",
            "果然很难啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "光靠在主日学校学到的东西\x01",
            "可远远不够啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2698")

    label("loc_24D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_260C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25B5")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "以孩子他爸的这种陈旧思想，\x01",
            "会被周围人甩在后面的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在这个时代，\x01",
            "如果不去学校上课可是不行的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "隔壁的基诺奇奥\x01",
            "也去学院上学了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我们家的孩子可不能输给他。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2609")

    label("loc_25B5")


    ChrTalk(
        0xFE,
        (
            "隔壁的基诺奇奥\x01",
            "也去学院上学了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我们家的孩子可不能输给他。\x02",
    )

    CloseMessageWindow()

    label("loc_2609")

    Jump("loc_2698")

    label("loc_260C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2698")
    TurnDirection(0xFE, 0x136, 0)

    ChrTalk(
        0xFE,
        (
            "啊呀，那件制服是……\x01",
            "难道你是王立学院的学生？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "看上去果然让人感到与众不同呢～\x02",
    )

    CloseMessageWindow()

    label("loc_2698")

    TalkEnd(0xD)
    Return()

    # Function_9_1E65 end

    def Function_10_269C(): pass

    label("Function_10_269C")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_26E6")

    ChrTalk(
        0xFE,
        (
            "大人们都在议论纷纷的，\x01",
            "发生什么事了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DAB")

    label("loc_26E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2795")

    ChrTalk(
        0xFE,
        (
            "我想自然系的课程\x01",
            "应该和我要成为飞艇乘务员\x01",
            "这个梦想相关吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我要试着努力\x01",
            "去参加王立学院的考试。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DAB")

    label("loc_2795")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_2831")

    ChrTalk(
        0xFE,
        "我去参观过学园祭了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我并不是去看\x01",
            "那里的上课情况，\x01",
            "不过学习的气氛真的很不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DAB")

    label("loc_2831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2929")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F5")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "总之，\x01",
            "我决定去王立学院亲自看一看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，这可不是说我\x01",
            "已经决定去参加入学考试了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只是不想让母亲\x01",
            "对此事过分热心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2926")

    label("loc_28F5")


    ChrTalk(
        0xFE,
        (
            "总之，\x01",
            "我决定去王立学院亲自看一看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2926")

    Jump("loc_2DAB")

    label("loc_2929")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2AA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A22")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "父亲让我认真考虑一下\x01",
            "自己想做的事情是什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "然后，我就去调查了一下。\x01",
            "要成为飞艇的乘务员之一，\x01",
            "我还有许多要努力的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样想的话，\x01",
            "去学院念书也并不坏啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AA1")

    label("loc_2A22")


    ChrTalk(
        0xFE,
        (
            "要成为飞艇的乘务员之一，\x01",
            "我还有许多要努力的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样想的话，\x01",
            "去学院念书也并不坏啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AA1")

    Jump("loc_2DAB")

    label("loc_2AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2BF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B76")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "我想成为\x01",
            "定期船的乘务员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从小时候开始\x01",
            "我就向往这个职业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个梦想\x01",
            "直至今日仍然没有改变。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF2")

    label("loc_2B76")


    ChrTalk(
        0xFE,
        (
            "我想成为\x01",
            "定期船的乘务员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个梦想\x01",
            "直至今日仍然没有改变。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BF2")

    Jump("loc_2DAB")

    label("loc_2BF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_2D4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF5")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "啊啊～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "父亲来劝我，\x01",
            "希望我能够成为船员……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "母亲却要我\x01",
            "去杰尼丝王立学院上学。\x01",
            "真是好麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我既不想成为船员，\x01",
            "也不想去学校念书。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D4B")

    label("loc_2CF5")


    ChrTalk(
        0xFE,
        (
            "我既不想成为船员，\x01",
            "也不想去学校念书。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D4B")

    Jump("loc_2DAB")

    label("loc_2D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2DAB")

    ChrTalk(
        0xFE,
        (
            "我差不多也该决定\x01",
            "自己将来的事情了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "因为我有我想做的工作。\x02",
    )

    CloseMessageWindow()

    label("loc_2DAB")

    TalkEnd(0xE)
    Return()

    # Function_10_269C end

    def Function_11_2DAF(): pass

    label("Function_11_2DAF")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E48")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "好了，\x01",
            "我该去港口了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉～\x01",
            "港口主任这份工作可不是说着玩的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA2")

    label("loc_2E48")


    ChrTalk(
        0xFE,
        (
            "唉～\x01",
            "港口主任这份工作可不是说着玩的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EA2")

    TalkEnd(0xF)
    Return()

    # Function_11_2DAF end

    def Function_12_2EA6(): pass

    label("Function_12_2EA6")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3068")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FDF")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "以前都是戴尔蒙家族的人\x01",
            "垄断了卢安市市长这个职位。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但下任的选举\x01",
            "则打破了这一惯例。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这对想当市长的人来说\x01",
            "是次难得的机会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……我的丈夫\x01",
            "如果能再加把劲就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3065")

    label("loc_2FDF")


    ChrTalk(
        0xFE,
        (
            "这对想当市长的人来说\x01",
            "是次难得的机会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……我的丈夫\x01",
            "如果能再加把劲就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3065")

    Jump("loc_35CD")

    label("loc_3068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_325E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31CF")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "最近，\x01",
            "我丈夫总是在为很多事情烦恼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "反正又是为了\x01",
            "不知道到底该去做哪件事情\x01",
            "而迷茫不已吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这种时候还是\x01",
            "我们的儿子比较有魄力……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他就是那样子，\x01",
            "不知道什么叫做让步。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "两边权衡一下\x01",
            "不是挺好的方法吗，\x01",
            "看他这样我都替他着急。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_325B")

    label("loc_31CF")


    ChrTalk(
        0xFE,
        (
            "最近，\x01",
            "我丈夫总是在为很多事情烦恼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "反正又是为了\x01",
            "不知道到底该去做哪件事情\x01",
            "而迷茫不已吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_325B")

    Jump("loc_35CD")

    label("loc_325E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_33E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3353")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "说起来，我儿子学校的学园祭\x01",
            "应该马上就要到了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，那家伙……\x01",
            "听说我们要去学校就生气了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，这个年纪的孩子，\x01",
            "不管是男孩还是女孩都很难管教啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E5")

    label("loc_3353")


    ChrTalk(
        0xFE,
        (
            "说起来，我儿子学校的学园祭\x01",
            "应该马上就要到了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，那家伙……\x01",
            "听说我们要去学校就生气了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33E5")

    Jump("loc_35CD")

    label("loc_33E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_3466")

    ChrTalk(
        0xFE,
        (
            "啊啊，\x01",
            "我明明打算要在桥起吊之前去买东西的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可恶……\x01",
            "完全忘记了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35CD")

    label("loc_3466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_3539")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F6")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "丈夫去工作，\x01",
            "儿子也去上学了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好吧～\x01",
            "赶快把家务都做完吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3536")

    label("loc_34F6")


    ChrTalk(
        0xFE,
        (
            "好吧～\x01",
            "赶快把家务都做完吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3536")

    Jump("loc_35CD")

    label("loc_3539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_35CD")

    ChrTalk(
        0xFE,
        (
            "我的老公\x01",
            "是港口的负责人，\x01",
            "但他好像没什么干劲……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "既然他受到大家的信任，\x01",
            "在市民间也非常有威望，\x01",
            "为什么不能表现地更加凛然一点呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35CD")

    TalkEnd(0x10)
    Return()

    # Function_12_2EA6 end

    def Function_13_35D1(): pass

    label("Function_13_35D1")

    TalkBegin(0x11)

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "父亲放着我不管\x01",
            "既有好处也有坏处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "母亲也说\x01",
            "这是没办法的事……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x11)
    Return()

    # Function_13_35D1 end

    def Function_14_3670(): pass

    label("Function_14_3670")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_37D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3757")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "这次的事件真让人遗憾，\x01",
            "身为市长怎么能误入歧途呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "既然市长已经犯下了错误，\x01",
            "让卢安繁荣发展的宗旨\x01",
            "谁又能够继承下去呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唔……………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_37D0")

    label("loc_3757")


    ChrTalk(
        0xFE,
        (
            "既然市长已经犯下了错误，\x01",
            "让卢安繁荣发展的宗旨\x01",
            "谁又能够继承下去呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唔……………………\x02",
    )

    CloseMessageWindow()

    label("loc_37D0")

    Jump("loc_3E48")

    label("loc_37D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_39C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38FF")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "卢安的改变果然还是从\x01",
            "定期船通航后开始的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "前些天，定期船停航的时候，\x01",
            "旅客们一个接一个地来退票。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀，可以说定期船\x01",
            "对于卢安来说已经是\x01",
            "一个不可或缺的存在了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39BF")

    label("loc_38FF")


    ChrTalk(
        0xFE,
        (
            "前些天，定期船停航的时候，\x01",
            "旅客们一个接一个地来退票。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀，可以说定期船\x01",
            "对于卢安来说已经是\x01",
            "一个不可或缺的存在了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39BF")

    Jump("loc_3E48")

    label("loc_39C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_3A4D")

    ChrTalk(
        0xFE,
        (
            "说不定能把\x01",
            "王立学院的学园祭\x01",
            "作为季节限定的旅行计划呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，明年这个时候\x01",
            "就这样计划试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E48")

    label("loc_3A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_3B3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B10")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "港口的那些流氓\x01",
            "真得让我很头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "给观光客留下\x01",
            "不愉快的印象\x01",
            "也不是一次两次了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B38")

    label("loc_3B10")


    ChrTalk(
        0xFE,
        (
            "……真是的，\x01",
            "那些混蛋真让人烦恼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B38")

    Jump("loc_3E48")

    label("loc_3B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_3CC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C5C")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "最近的卢安\x01",
            "正在渐渐向\x01",
            "观光城市转变。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对于我来说，\x01",
            "现在正是个好机会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我准备了许多观光计划，\x01",
            "不止是利贝尔各地的客人，\x01",
            "国外的旅客也是我的招揽对象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我非常赞成市长\x01",
            "要振兴观光业的方针。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CC5")

    label("loc_3C5C")


    ChrTalk(
        0xFE,
        (
            "最近的卢安\x01",
            "正在渐渐向\x01",
            "观光城市转变。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对于我来说，\x01",
            "现在正是个好机会。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CC5")

    Jump("loc_3E48")

    label("loc_3CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_3E48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DB3")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "我以卢安为中心\x01",
            "经营观光业和酒店业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "最近建成的布朗西酒店\x01",
            "受到观光客的不少好评。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特别是顶楼那套别致的套房\x01",
            "是我最最骄傲的杰作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E48")

    label("loc_3DB3")


    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "最近建成的布朗西酒店\x01",
            "受到观光客的不少好评。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特别是顶楼那套别致的套房\x01",
            "是我最最骄傲的杰作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E48")

    TalkEnd(0x12)
    Return()

    # Function_14_3670 end

    def Function_15_3E4C(): pass

    label("Function_15_3E4C")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3EEA")

    ChrTalk(
        0xFE,
        (
            "市长先生竟然做了\x01",
            "那么过分的事………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我刚来的时候还以为\x01",
            "他是个很伟大的人呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41C4")

    label("loc_3EEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3F51")

    ChrTalk(
        0xFE,
        (
            "我也知道\x01",
            "丈夫工作非常繁忙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是我还是很希望他\x01",
            "能多点机会和孩子们接触。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41C4")

    label("loc_3F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_3FE3")

    ChrTalk(
        0xFE,
        (
            "我也想让自家的长子\x01",
            "去王立学院上学……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是他本人不想去的话，\x01",
            "我们也没办法。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41C4")

    label("loc_3FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_40A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_407C")
    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "我们家还有\x01",
            "另外一个儿子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为某些原因，\x01",
            "他现在不住在这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个孩子，\x01",
            "有没有好好吃饭呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40A2")

    label("loc_407C")


    ChrTalk(
        0xFE,
        (
            "那个孩子，\x01",
            "有没有好好吃饭呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40A2")

    Jump("loc_41C4")

    label("loc_40A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_4146")

    ChrTalk(
        0xFE,
        (
            "路易真是个\x01",
            "会乱来的孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "脑子里一想到什么事情，\x01",
            "就会立刻去亲自实践一下，\x01",
            "否则就安不下心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41C4")

    label("loc_4146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_41C4")

    ChrTalk(
        0xFE,
        (
            "我丈夫\x01",
            "非常热衷于工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还是担心他会不会\x01",
            "因为工作过度而倒下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41C4")

    TalkEnd(0x13)
    Return()

    # Function_15_3E4C end

    def Function_16_41C8(): pass

    label("Function_16_41C8")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_425B")

    ChrTalk(
        0xFE,
        (
            "哥哥回来了，\x01",
            "但爸爸不让他进家门。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为什么爸爸总是\x01",
            "对哥哥那么冷淡呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_442F")

    label("loc_425B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_4353")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42F6")
    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "我的哥哥\x01",
            "经常呆在港口那边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "爸爸说我不可以跑过去找他玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哼，\x01",
            "爸爸他自己又不陪我玩。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4350")

    label("loc_42F6")


    ChrTalk(
        0xFE,
        (
            "我的哥哥\x01",
            "经常呆在港口那边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "爸爸说我不可以跑过去找他玩。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4350")

    Jump("loc_442F")

    label("loc_4353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_439A")

    ChrTalk(
        0xFE,
        (
            "啊～啊，\x01",
            "我好想去找哥哥玩啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_442F")

    label("loc_439A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_43BA")

    ChrTalk(
        0xFE,
        "妈妈～我肚子饿了～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_442F")

    label("loc_43BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_4402")

    ChrTalk(
        0xFE,
        (
            "前几天，我把爸爸的表给拆了，\x01",
            "被他骂了一顿。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_442F")

    label("loc_4402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_442F")

    ChrTalk(
        0xFE,
        (
            "爸爸他啊～\x01",
            "一天到晚都在工作…… \x02",
        )
    )

    CloseMessageWindow()

    label("loc_442F")

    TalkEnd(0x14)
    Return()

    # Function_16_41C8 end

    SaveToFile()

Try(main)
