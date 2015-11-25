from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4214   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4214.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '希尔丹夫人',                           # 9
        '茜亚',                                 # 10
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
        'ED6_DT07/CH02460 ._CH',             # 00
        'ED6_DT07/CH02540 ._CH',             # 01
        'ED6_DT07/CH02230 ._CH',             # 02
        'ED6_DT07/CH02240 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02540P._CP',             # 01
        'ED6_DT07/CH02230P._CP',             # 02
        'ED6_DT07/CH02240P._CP',             # 03
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_10A",          # 00, 0
        "Function_1_240",          # 01, 1
        "Function_2_24A",          # 02, 2
        "Function_3_3C7",          # 03, 3
        "Function_4_634",          # 04, 4
        "Function_5_957",          # 05, 5
        "Function_6_FDA",          # 06, 6
        "Function_7_2994",         # 07, 7
    )


    def Function_0_10A(): pass

    label("Function_0_10A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_134")
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 2)
    SetChrChipByIndex(0x138, 3)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_142")
    OP_A3(0x3FA)
    Event(0, 5)

    label("loc_142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_150")
    OP_A3(0x3FB)
    Event(0, 7)

    label("loc_150")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_15C"),
        (SWITCH_DEFAULT, "loc_172"),
    )


    label("loc_15C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16F")
    OP_A2(0x642)
    Event(0, 6)

    label("loc_16F")

    Jump("loc_172")

    label("loc_172")

    OP_A2(0x639)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_19C")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 64129, 0, 99150, 167)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Jump("loc_23F")

    label("loc_19C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1C3")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 70620, 0, 69790, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Jump("loc_23F")

    label("loc_1C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_1CD")
    Jump("loc_23F")

    label("loc_1CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_1F4")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 70630, 0, 98590, 48)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_23F")

    label("loc_1F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_1FE")
    Jump("loc_23F")

    label("loc_1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_23F")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 64129, 0, 99150, 167)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 70630, 0, 98590, 48)
    OP_43(0x9, 0x0, 0x0, 0x2)

    label("loc_23F")

    Return()

    # Function_0_10A end

    def Function_1_240(): pass

    label("Function_1_240")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_240 end

    def Function_2_24A(): pass

    label("Function_2_24A")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3B1")

    label("loc_26F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_288")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3B1")

    label("loc_288")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A1")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3B1")

    label("loc_2A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BA")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3B1")

    label("loc_2BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D3")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3B1")

    label("loc_2D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EC")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3B1")

    label("loc_2EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_305")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3B1")

    label("loc_305")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31E")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3B1")

    label("loc_31E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_337")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3B1")

    label("loc_337")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_350")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3B1")

    label("loc_350")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_369")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3B1")

    label("loc_369")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_382")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3B1")

    label("loc_382")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3B1")

    label("loc_39B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B1")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3B1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3B1")

    label("loc_3C6")

    Return()

    # Function_2_24A end

    def Function_3_3C7(): pass

    label("Function_3_3C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_3D4")
    Jump("loc_630")

    label("loc_3D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3DE")
    Jump("loc_630")

    label("loc_3DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_3E8")
    Jump("loc_630")

    label("loc_3E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_471")

    ChrTalk(
        0xFE,
        (
            "约修亚先生的肌肤\x01",
            "和女性一样细腻呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要化妆得当，\x01",
            "就会变得相当漂亮哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_630")

    label("loc_471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_47B")
    Jump("loc_630")

    label("loc_47B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_630")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_517")

    ChrTalk(
        0xFE,
        (
            "距晚宴开始\x01",
            "还有一段时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请慢慢在城里参观。\x02",
    )

    CloseMessageWindow()
    Jump("loc_630")

    label("loc_517")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎么了？\x01",
            "是不是有什么事情呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，没什么，\x01",
            "我们正在城里参观呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "距晚宴开始\x01",
            "还有一段时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请慢慢在城里参观。\x02",
    )

    CloseMessageWindow()

    label("loc_630")

    TalkEnd(0xFE)
    Return()

    # Function_3_3C7 end

    def Function_4_634(): pass

    label("Function_4_634")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_72E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6AE")

    ChrTalk(
        0x8,
        (
            "#710F在诞辰庆典上玩累了吗？\x01",
            "　\x02\x03",
            "如果有什么难处，\x01",
            "尽管告诉我就可以了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72B")

    label("loc_6AE")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#710F艾丝蒂尔。\x02\x03",
            "在诞辰庆典上玩累了吗？\x01",
            "　\x02\x03",
            "如果有什么难处，\x01",
            "尽管告诉我就可以了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72B")

    Jump("loc_953")

    label("loc_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_83F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7AD")

    ChrTalk(
        0x8,
        (
            "#710F因为诞辰庆典，\x01",
            "现在街上变得很热闹。\x02\x03",
            "你们就去好好玩玩吧，\x01",
            "要注意安全哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83C")

    label("loc_7AD")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#711F啊，\x01",
            "你们两个打算出去吗？\x02\x03",
            "因为诞辰庆典，\x01",
            "现在王都变得很热闹。\x02\x03",
            "你们就去好好玩玩吧，\x01",
            "要注意安全哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83C")

    Jump("loc_953")

    label("loc_83F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_849")
    Jump("loc_953")

    label("loc_849")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_853")
    Jump("loc_953")

    label("loc_853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_85D")
    Jump("loc_953")

    label("loc_85D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_953")

    ChrTalk(
        0x8,
        (
            "#710F是问晚宴吗……\x02\x03",
            "因为料理还在准备，\x01",
            "请再稍等片刻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#710F料理准备完毕之后，\x01",
            "晚宴就会立刻开始。\x02\x03",
            "你们就请先回房间休息一下吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x49, 0x1, 0x800)

    label("loc_953")

    TalkEnd(0xFE)
    Return()

    # Function_4_634 end

    def Function_5_957(): pass

    label("Function_5_957")

    EventBegin(0x0)
    OP_6D(62970, 640, 71000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 64390, 0, 71030, 270)
    SetChrPos(0x101, 61580, 0, 71540, 90)
    SetChrPos(0x102, 61580, 0, 70620, 90)

    ChrTalk(
        0x8,
        (
            "#710F……你们要说的我明白了。\x02\x03",
            "想要把拉赛尔博士的传话\x01",
            "直接的告诉女王陛下……\x02\x03",
            "就是这件事对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F对……就是这样的。\x02\x03",
            "如果女王陛下真的是身体不适，\x01",
            "我们就重新再考虑一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#710F那并不是主要的问题……\x02\x03",
            "女王宫正处于刚才那些特务兵\x01",
            "的２４小时监控状态。\x02\x03",
            "能够进去的只有公爵大人和上校，\x01",
            "以及在女王身边照料她的\x01",
            "我和侍女们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F这么说来，想要去见女王\x01",
            "果真是非常困难的了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F怎么办，艾丝蒂尔？\x02\x03",
            "只有把博士的传话让\x01",
            "希尔丹夫人转达这个办法了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F唔～嗯，可是还是\x01",
            "直接去和女王谈谈更好……\x02\x03",
            "杜南公爵的目的\x01",
            "和理查德上校的企图……\x02\x03",
            "不清楚的事情还有很多呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#710F……艾丝蒂尔、约修亚。\x02\x03",
            "我已经有些打算了。\x02\x03",
            "晚宴结束之后\x01",
            "你们再来这里一趟可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F咦，这么说来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们和女王见面的\x01",
            "方法已经有了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#710F这样认为也是可以的。\x02\x03",
            "虽然可能比较困难……\x01",
            "但还是有试一试的价值。\x02\x03",
            "因为还要做一些准备的缘故，\x01",
            "请等到晚宴结束，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F好～的，太幸运了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F明白了。\x01",
            "晚宴一结束就来向您请教。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#710F我会等候你们的到来的。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F29")

    ChrTalk(
        0x8,
        (
            "#710F啊，说到晚宴的事情……\x02\x03",
            "因为料理还在准备，\x01",
            "请再稍等片刻。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FAB")

    label("loc_F29")


    ChrTalk(
        0x8,
        (
            "#710F料理准备完毕之后，\x01",
            "晚宴就会立刻开始。\x02\x03",
            "先回房间休息一下\x01",
            "也许是个不错的选择。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x49, 0x1, 0x800)

    label("loc_FAB")

    Sleep(300)
    Fade(1000)
    SetChrPos(0x101, 62550, 0, 68550, 45)
    SetChrPos(0x102, 62550, 0, 68550, 45)
    EventEnd(0x0)
    Return()

    # Function_5_957 end

    def Function_6_FDA(): pass

    label("Function_6_FDA")

    EventBegin(0x0)
    OP_6D(67590, 0, 65319, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 70120, 0, 69770, 225)
    SetChrPos(0x101, 66580, 0, 64769, 45)
    SetChrPos(0x102, 67630, 0, 64590, 45)

    def lambda_102B():
        OP_6D(69520, 0, 68800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_102B)

    def lambda_1043():
        OP_8E(0xFE, 0x10B6C, 0x0, 0x10BE4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1043)

    def lambda_105E():
        OP_8E(0xFE, 0x1113E, 0x0, 0x1095A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_105E)
    WaitChrThread(0x102, 0x2)
    TurnDirection(0x102, 0x8, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x8,
        (
            "料理还在准备中，\x01",
            "请稍等片刻。\x02\x03",
            "不觉得迟到了很久吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F这个……对不起。\x02\x03",
            "不巧被理查德上校\x01",
            "抓住了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#710F上校……吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F只是谈了谈关于我们\x01",
            "父亲过去的事情。\x02\x03",
            "与这边的行动无关，\x01",
            "请不用在意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#710F是这样啊……\x02\x03",
            "根据介绍信来看，\x01",
            "你们两位是卡西乌斯先生\x01",
            "的孩子吧。\x02\x03",
            "理查德上校\x01",
            "会有一些感慨也是理所当然的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F请问，希尔丹夫人也\x01",
            "知道父亲的事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#710F曾经作为摩尔根将军副官\x01",
            "的他经常到王城这里来。\x02\x03",
            "是去世的王子……陛下的儿子\x01",
            "以前的学友。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F去世的王子……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F就是科洛蒂亚公主\x01",
            "的父亲大人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#710F嗯，因为１５年前的海难事故\x01",
            "而不幸身亡。\x02\x03",
            "倘若王子还活着的话，\x01",
            "现在这样的局面是\x01",
            "不会发生的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#710F……对于已经发生的事情，\x01",
            "后悔是没有用处的。\x02\x03",
            "夜色已晚，\x01",
            "这就准备出发吧。\x02\x03",
            "茜亚，过来吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 69050, 0, 75720, 180)

    def lambda_14BF():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_14BF)

    def lambda_14CD():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14CD)

    def lambda_14DB():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14DB)
    Sleep(300)

    def lambda_14EE():

        label("loc_14EE")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_14EE")

    QueueWorkItem2(0x9, 1, lambda_14EE)

    def lambda_14FF():
        OP_8E(0xFE, 0x10CCA, 0x0, 0x112B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_14FF)

    def lambda_151A():

        label("loc_151A")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_151A")

    QueueWorkItem2(0x8, 1, lambda_151A)

    def lambda_152B():

        label("loc_152B")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_152B")

    QueueWorkItem2(0x101, 1, lambda_152B)

    def lambda_153C():

        label("loc_153C")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_153C")

    QueueWorkItem2(0x102, 1, lambda_153C)
    OP_6D(70030, 0, 70300, 2000)

    ChrTalk(
        0x101,
        "#000F咦，你不是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F您是茜亚小姐\x01",
            "对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "你、你们好……\x01",
            "艾丝蒂尔小姐，约修亚先生，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "事情我已经知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#710F这个孩子\x01",
            "你们完全可以相信她。\x02\x03",
            "公主殿下在城里的时候，\x01",
            "就是由这位侍女照顾的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F公主殿下……\x01",
            "就是科洛蒂亚公主吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F这样的话就没问题了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "谢、谢谢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那么这就把准备好的制服\x01",
            " \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "丝带呀头饰呀那些\x01",
            "细小的方面我都已经\x01",
            "准备完毕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F这么说……难道？\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x8, 0xFF)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "#710F是啊，艾丝蒂尔如果\x01",
            "装扮成侍女的样子\x01",
            "就可以进入女王宫了。\x02\x03",
            "在把头发的样式改变一下，\x01",
            "看守也就觉察不出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F原～来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F的确，制服可以很好\x01",
            "将个人特点隐藏起来。\x02\x03",
            "用于潜入\x01",
            "就再好不过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊～侍女的服饰啊。\x02\x03",
            "看到过莉拉小姐的着装，\x01",
            "觉得很不错呢。\x02\x03",
            "既飘逸而又很可爱，\x01",
            "行动起来也很方便的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嘻嘻，如果行动不方便\x01",
            "那扫除的时候就麻烦了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，果然是这样吗？\x02\x03",
            "那就立刻穿上吧！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F很开心嘛……\x02\x03",
            "蹦蹦跳跳的虽然是可以，\x01",
            "但不要在陛下面前失礼哦。\x02\x03",
            "这次我是\x01",
            "不能和你一起了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F哎？为什么？\x02\x03",
            "约修亚也换装不就行了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F…………………………\x02\x03",
            "……咦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B0A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1B0A)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "#710F你说什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F约修亚你在学院祭的舞台剧\x01",
            "中扮演的公主不是很合适的吗？\x02\x03",
            "礼服和侍女装不是差不多吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这、这可不是在演戏。\x02\x03",
            "和女王陛下见面时\x01",
            "却穿的女装，这有点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F没关系，没关系。\x01",
            "一点都不难看！\x02\x03",
            "当时约修亚装扮的公主\x01",
            "可是非常美丽哟！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F又、又来了……别开玩笑了。\x02\x03",
            "希尔丹夫人你们\x01",
            "怎么说我就怎么做吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D1B():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1D1B)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        "#710F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#010F我、我说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#710F原来如此……\x01",
            "好像的确没有什么问题。\x02\x03",
            "茜亚，为公主殿下准备的\x01",
            "假发还在吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "是、是的……\x01",
            "一次都没有使用过呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "如果是长长的黑发，\x01",
            "和约修亚公子是很配的哦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我、我说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F就这样，３比１多数取胜，\x01",
            "最终的结果出现⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那就请到这边来。\x01",
            "更衣室已经准备好了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F06():

        label("loc_1F06")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1F06")

    QueueWorkItem2(0x8, 1, lambda_1F06)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)

    def lambda_1F2B():
        OP_8E(0xFE, 0x10C48, 0x0, 0x12D4A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1F2B)
    Sleep(300)
    OP_8E(0x101, 0x10FF4, 0x0, 0x10AEA, 0xBB8, 0x0)

    ChrTalk(
        0x102,
        (
            "#010F请等一下！\x01",
            "我换衣服这件事怎么一句话就……\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x102, 0x10FEA, 0x0, 0x1090A, 0x7D0, 0x0)
    OP_8C(0x102, 180, 400)

    def lambda_1FC1():
        OP_6D(69970, 0, 72360, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1FC1)

    def lambda_1FD9():
        OP_8E(0xFE, 0x10C48, 0x0, 0x12D4A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FD9)

    def lambda_1FF4():
        OP_8F(0xFE, 0x10C48, 0x0, 0x12D4A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1FF4)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)

    ChrTalk(
        0x102,
        (
            "#010F我知道，我知道的啊……\x01",
            "衣服什么的由我自己来脱……\x02\x03",
            "啊……茜亚小姐……\x01",
            "还要化妆的啊……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8)

    ChrTalk(
        0x8,
        (
            "#710F呼……\x01",
            "现在的年轻人啊……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(69200, 0, 72370, 0)
    SetChrPos(0x8, 68890, 0, 69520, 0)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x102, 3)
    FadeToBright(2000, 0)

    def lambda_2126():
        OP_8E(0xFE, 0x11062, 0x0, 0x116F2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2126)
    Sleep(600)

    def lambda_2146():
        OP_8E(0xFE, 0x10E00, 0x0, 0x11D78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2146)
    WaitChrThread(0x9, 0x1)

    def lambda_2166():
        OP_8E(0xFE, 0x1090A, 0x0, 0x11E18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2166)
    WaitChrThread(0x9, 0x1)

    def lambda_2186():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2186)

    ChrTalk(
        0x8,
        "#710F啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 317, 400)
    OP_8C(0x101, 75, 400)
    OP_8C(0x101, 180, 400)

    ChrTalk(
        0x101,
        (
            "#000F您～好。\x02\x03",
            "嗯，怎么样－呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嘿嘿嘿……\x01",
            "非常合适呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#710F刚到城里不久，\x01",
            "活泼开郎的实习侍女……\x01",
            "这种说法十分有说服力啊。\x02\x03",
            "头发也批下来之后，\x01",
            "就更不容易被注意到了。\x02\x03",
            "不如就到我们这个\x01",
            "格兰赛尔城来工作如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F游、游击士那边还有任务，\x01",
            "所以这个就……\x02\x03",
            "啊，对了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F喂喂，约修亚。\x01",
            "快点出来吧～\x02",
        )
    )

    CloseMessageWindow()

    def lambda_23A2():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_23A2)

    def lambda_23B0():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_23B0)
    OP_6D(69080, 0, 73680, 1000)

    ChrTalk(
        0x102,
        (
            "#010F啊……\x02\x03",
            "不出来不行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F不－行。\x02\x03",
            "再喋喋不休的话\x01",
            "我就去把你拖出来了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我明白了……\x02\x03",
            "唉，没办法了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2479():

        label("loc_2479")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_2479")

    QueueWorkItem2(0x9, 1, lambda_2479)

    def lambda_248A():

        label("loc_248A")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_248A")

    QueueWorkItem2(0x8, 1, lambda_248A)

    def lambda_249B():

        label("loc_249B")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_249B")

    QueueWorkItem2(0x101, 1, lambda_249B)
    OP_8E(0x102, 0x10DBA, 0x0, 0x11DC8, 0x3E8, 0x0)

    ChrTalk(
        0x102,
        "#010F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#710F这竟然会……\x01",
            "相称的到了可怕的程度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F怎么样，我说过的吧！？\x02\x03",
            "真是的，竟然比身为\x01",
            "女子的我还要有形，\x01",
            "这到底是怎－么回事嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嘿嘿嘿……\x01",
            "我还为他好好的化了妆的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F好了……\x01",
            "请不要再说了……\x02",
        )
    )

    CloseMessageWindow()
    OP_6D(68990, 0, 71660, 1000)

    def lambda_25F1():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25F1)

    def lambda_25FF():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_25FF)

    ChrTalk(
        0x8,
        (
            "#710F嗯……\x01",
            "准备完毕了。\x02\x03",
            "那么我现在就\x01",
            "带领你们去女王宫吧。\x02\x03",
            "彻底的把自己当成\x01",
            "实习侍女，这一点要记住。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，好的，明白了。\x02\x03",
            "唔……\x01",
            "终于要见到女王了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯……到了关键时刻了。\x02\x03",
            "集中精力，\x01",
            "无论如何也要进入女王宫。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F噗哧，你这身打扮配合这样\x01",
            "严肃的话真是天衣无缝啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 800)

    ChrTalk(
        0x102,
        (
            "#010F太、太坏了！\x01",
            "什么天衣无缝！\x02\x03",
            "我都打扮成这副\x01",
            "模样了，你还取笑我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F对不起对不起，\x01",
            "不要那么倔犟嘛。\x02\x03",
            "下次我请你吃冰淇淋\x01",
            "消消气哈～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F哼，我又不像你，\x01",
            "用吃的是不能收买我的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F我、我什么时候\x01",
            "被吃的给收买过？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嘿嘿嘿……\x01",
            "真是一对好伙伴呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#710F时间快来不及了……\x01",
            "立刻前往女王宫吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4A, 0x1, 0x20)
    OP_28(0x4A, 0x1, 0x40)
    SetChrFlags(0x8, 0x40)

    def lambda_295C():
        OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_295C)
    EventEnd(0x0)
    AddParty(0x37, 0xFF)
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 2)
    SetChrChipByIndex(0x138, 3)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)
    SetChrFlags(0x8, 0x80)
    Return()

    # Function_6_FDA end

    def Function_7_2994(): pass

    label("Function_7_2994")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    OP_6D(68370, 0, 69650, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 68920, 0, 70070, 180)
    SetChrPos(0x9, 67750, 0, 70350, 180)
    RemoveParty(0x37, 0xFF)
    SetChrPos(0x101, 67080, 0, 68350, 0)
    SetChrPos(0x102, 68360, 0, 68190, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#000F希尔丹夫人，茜亚小姐，\x01",
            "真是太感谢你们了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F帮了我们大忙啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#710F哪里，这是为陛下服务\x01",
            "的人理所当然的义务。\x02\x03",
            "陛下委托的任务\x01",
            "无论如何拜托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那、那个……\x01",
            "我也要拜托你们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "请一定替我们……\x01",
            "把公主殿下救出来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，茜亚小姐\x01",
            "服侍过公主殿下的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "是、是的……\x01",
            "虽然能够照顾她的\x01",
            "机会并不多，很遗憾……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "但是她把我这种下人\x01",
            "当作朋友一样对待，\x01",
            "是一个平易近人而又温柔的人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "当听说她被\x01",
            "囚禁了的时候，\x01",
            "我每天都担心的睡不着觉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是吗……\x01",
            "我们一定会把她救出来的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那我们就告辞了。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_7_2994 end

    SaveToFile()

Try(main)
