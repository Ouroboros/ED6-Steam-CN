from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2410   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2410.x',
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
        '特蕾莎院长',                           # 9
        '达尼艾尔',                             # 10
        '玛丽',                                 # 11
        '克拉姆',                               # 12
        '波利',                                 # 13
        '壶',                                   # 14
        '红茶',                                 # 15
        '红茶',                                 # 16
        '红茶',                                 # 17
        '红茶',                                 # 18
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
        'ED6_DT07/CH02570 ._CH',             # 00
        'ED6_DT07/CH02640 ._CH',             # 01
        'ED6_DT07/CH02630 ._CH',             # 02
        'ED6_DT07/CH02590 ._CH',             # 03
        'ED6_DT07/CH02500 ._CH',             # 04
        'ED6_DT07/CH00003 ._CH',             # 05
        'ED6_DT07/CH00013 ._CH',             # 06
        'ED6_DT07/CH00043 ._CH',             # 07
        'ED6_DT06/CH20020 ._CH',             # 08
        'ED6_DT06/CH20021 ._CH',             # 09
        'ED6_DT07/CH02573 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH02570P._CP',             # 00
        'ED6_DT07/CH02640P._CP',             # 01
        'ED6_DT07/CH02630P._CP',             # 02
        'ED6_DT07/CH02590P._CP',             # 03
        'ED6_DT07/CH02500P._CP',             # 04
        'ED6_DT07/CH00003P._CP',             # 05
        'ED6_DT07/CH00013P._CP',             # 06
        'ED6_DT07/CH00043P._CP',             # 07
        'ED6_DT06/CH20020P._CP',             # 08
        'ED6_DT06/CH20021P._CP',             # 09
        'ED6_DT07/CH02573P._CP',             # 0A
    )

    DeclNpc(
        X                   = -3700,
        Z                   = 0,
        Y                   = 14600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 35100,
        Z                   = 0,
        Y                   = 2300,
        Direction           = 180,
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
        X                   = 35300,
        Z                   = 0,
        Y                   = -35300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -3400,
        Z                   = 0,
        Y                   = 1700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 32500,
        Z                   = 0,
        Y                   = -34400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703944,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1638408,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1638408,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1638408,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1638408,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_242",          # 00, 0
        "Function_1_2B0",          # 01, 1
        "Function_2_2B1",          # 02, 2
        "Function_3_2C7",          # 03, 3
        "Function_4_372",          # 04, 4
        "Function_5_3CC",          # 05, 5
        "Function_6_434",          # 06, 6
        "Function_7_48D",          # 07, 7
        "Function_8_505",          # 08, 8
        "Function_9_1240",         # 09, 9
    )


    def Function_0_242(): pass

    label("Function_0_242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_24C")
    Jump("loc_28A")

    label("loc_24C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_256")
    Jump("loc_28A")

    label("loc_256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 0)), scpexpr(EXPR_END)), "loc_260")
    Jump("loc_28A")

    label("loc_260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_26A")
    Jump("loc_28A")

    label("loc_26A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_279")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_28A")

    label("loc_279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_283")
    Jump("loc_28A")

    label("loc_283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_28A")

    label("loc_28A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_298")
    OP_A3(0x3FA)
    Event(0, 8)

    label("loc_298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_2AF")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 9)

    label("loc_2AF")

    Return()

    # Function_0_242 end

    def Function_1_2B0(): pass

    label("Function_1_2B0")

    Return()

    # Function_1_2B0 end

    def Function_2_2B1(): pass

    label("Function_2_2B1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2B1")

    label("loc_2C6")

    Return()

    # Function_2_2B1 end

    def Function_3_2C7(): pass

    label("Function_3_2C7")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_36E")

    ChrTalk(
        0x8,
        (
            "#750F那些孩子也都很喜欢热闹，\x01",
            "你们有空一定要过来玩哦。\x02\x03",
            "这里也没什么别的东西能招待你们……\x01",
            "我会准备好香草茶和点心，\x01",
            "等你们过来品尝。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36E")

    TalkEnd(0x8)
    Return()

    # Function_3_2C7 end

    def Function_4_372(): pass

    label("Function_4_372")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_3C8")

    ChrTalk(
        0xFE,
        (
            "#770F科洛丝姐姐，\x01",
            "下次再来玩啊。\x02\x03",
            "大家都盼望着呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C8")

    TalkEnd(0xB)
    Return()

    # Function_4_372 end

    def Function_5_3CC(): pass

    label("Function_5_3CC")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_430")

    ChrTalk(
        0xFE,
        (
            "科洛丝姐姐做的\x01",
            "苹果派最好吃了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不管有多少我都能吃下。\x02",
    )

    CloseMessageWindow()

    label("loc_430")

    TalkEnd(0x9)
    Return()

    # Function_5_3CC end

    def Function_6_434(): pass

    label("Function_6_434")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_489")

    ChrTalk(
        0xFE,
        (
            "艾丝蒂尔和约修亚，\x01",
            "你们要再来玩啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_489")

    TalkEnd(0xC)
    Return()

    # Function_6_434 end

    def Function_7_48D(): pass

    label("Function_7_48D")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_501")

    ChrTalk(
        0xFE,
        (
            "我们院的克拉姆给你们添麻烦了，\x01",
            "真是对不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那孩子\x01",
            "总是这个样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真伤脑筋……\x02",
    )

    CloseMessageWindow()

    label("loc_501")

    TalkEnd(0xA)
    Return()

    # Function_7_48D end

    def Function_8_505(): pass

    label("Function_8_505")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x136, 0x4)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x136, 7)
    SetChrPos(0x101, -5240, 200, 7350, 90)
    SetChrPos(0x102, -5240, 200, 6050, 90)
    SetChrPos(0x136, -2550, 200, 6100, 270)
    SetChrPos(0x8, -2550, 200, 7350, 270)
    SetChrChipByIndex(0x8, 10)
    OP_4A(0x8, 255)
    SetChrPos(0xD, -4100, 750, 5310, 0)
    SetChrPos(0xE, -4550, 700, 6860, 0)
    SetChrPos(0xF, -4530, 700, 6060, 0)
    SetChrPos(0x10, -3810, 700, 6860, 0)
    SetChrPos(0x11, -3710, 700, 6060, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_6D(-2580, 0, 14700, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在特蕾莎院长的款待之下，\x01",
            "艾丝蒂尔他们一边喝茶吃苹果派，\x01",
            "一边做自我介绍并说出之前发生的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(1500, 0)
    OP_6D(-3770, 100, 7530, 3000)

    ChrTalk(
        0x8,
        (
            "#756F原来是这样啊……\x02\x03",
            "那孩子本性并不坏，\x01",
            "只是喜欢恶作剧而且做事又欠考虑……\x02\x03",
            "#754F真是非常抱歉。\x01",
            "我作为他的监护人也感到十分羞愧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，已经没事了。\x01",
            "反正他已经把徽章还给我们了。\x02\x03",
            "#001F而且还喝到这么棒的香草茶，\x01",
            "吃上这么美味的苹果派。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#750F呵呵，你们太过奖了。\x01",
            "艾丝蒂尔、约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不过，这茶真的是非常清甜可口。\x02\x03",
            "和玛诺利亚村旅馆的\x01",
            "香草茶同样美味。\x02\x03",
            "这难道是从外面\x01",
            "那些茶树上采下的茶叶吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#750F嗯。\x01",
            "栽种茶树算是我的兴趣。\x02\x03",
            "而且承蒙旅馆老板的好意，\x01",
            "他经常到我们这里收购茶叶。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F原来是这样啊……\x02\x03",
            "刚才吃的苹果派\x01",
            "味道也很棒呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#751F呵呵，那不是我做的，\x01",
            "而是这孩子亲手做的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊，科洛丝吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#045F真是不好意思……\x02\x03",
            "#043F那个……\x01",
            "刚才实在是太失礼了。\x02\x03",
            "我并不是有意的，\x01",
            "只是听到那孩子的叫嚷才会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F不要放在心上啦。\x02\x03",
            "我抓到那孩子的时候，\x01",
            "自己也有点太过冲动了呢。\x02\x03",
            "不过呢，\x01",
            "那只白鹰真是差点把我吓坏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#040F啊，你说的是基库吧。\x02\x03",
            "它是只白隼哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F白隼……\x01",
            "是利贝尔的国鸟吧。\x02\x03",
            "看得出它经过了严格训练。\x01",
            "是你的宠物吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#041F呵呵，\x01",
            "其实并不是我饲养的。\x02\x03",
            "应该说我们是好朋友吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哇～你有这么厉害的朋友啊。\x02\x03",
            "#000F话说回来，\x01",
            "科洛丝你是杰尼丝王立学院的学生吧。\x02\x03",
            "为什么你会住在这里呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#040F不是呢……\x01",
            "我是住在学院宿舍里面的。\x02\x03",
            "因为学院离这里不远，\x01",
            "所以我经常在休息的时候来玩。\x02\x03",
            "#045F也给老师添了很多麻烦……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)

    ChrTalk(
        0x8,
        (
            "#751F哎呀哎呀。\x01",
            "哪里有给我添麻烦啊。\x02\x03",
            "你每次来都帮我做家务，\x01",
            "是我给你添麻烦才对。\x02\x03",
            "而且看到你来，孩子们都很开心呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x136, 2)

    ChrTalk(
        0x136,
        "#040F特蕾莎老师……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#750F不过，可不要为了经常来这里\x01",
            "而影响了学院的生活哦。\x02\x03",
            "呵呵，我可能是多说了，\x01",
            "不过你不会让我这么担心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#045F嗯，我会铭记于心的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊，学院生活……\x02\x03",
            "我也想体验一下呢，\x01",
            "就算只有一次也好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我也有同感。\x01",
            "毕竟主日学校一个星期才上一次课。\x02\x03",
            "不过，我听说王立学院的\x01",
            "入学考试不是一般的难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F唉，要是我去考试，\x01",
            "肯定没法通过的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    Sleep(300)
    SetChrSubChip(0x136, 0)

    ChrTalk(
        0x136,
        (
            "#040F呵呵，没有这回事。\x02\x03",
            "我倒是觉得要成为游击士\x01",
            "才不是一般的难呢。\x02\x03",
            "#041F而且这么年轻就……\x01",
            "是我该羡慕你们才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F嘿嘿……\x01",
            "我都被你说得难为情了。\x02\x03",
            "说是游击士，\x01",
            "其实我们只是见习的而已啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F为了能成为独当一面的游击士，\x01",
            "我们正在到王国各地修行的途中。\x02\x03",
            "最近正打算在\x01",
            "卢安地区进行活动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#750F这样啊，说不定以后\x01",
            "还会有需要你们照顾的地方呢。\x02\x03",
            "#751F那些孩子也都很喜欢热闹，\x01",
            "你们有空一定要过来玩哦。\x02\x03",
            "我会准备好香草茶和点心，\x01",
            "等你们过来品尝。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_505 end

    def Function_9_1240(): pass

    label("Function_9_1240")

    EventBegin(0x0)
    OP_A2(0x41C)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x9, 37220, 0, -33090, 180)
    SetChrPos(0xA, 37310, 1700, -33090, 180)
    SetChrPos(0xC, 37220, 0, -36830, 180)
    SetChrPos(0xB, 37220, 1700, -36830, 180)
    SetChrPos(0x8, 36300, 0, 42360, 270)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xC, 255)
    OP_4A(0xB, 255)
    OP_4A(0x8, 255)
    OP_6D(38522, 0, -31220, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(500, 0)
    OP_6D(35522, 0, -34220, 3000)
    Sleep(2000)
    Fade(1000)
    OP_6D(36570, 0, 42820, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#750F呵呵，要修补的东西还真多，\x01",
            "这也说明孩子们的精力都很旺盛吧……\x02\x03",
            "好了，差不多该休息了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrPos(0x8, 35780, 0, 42330, 270)
    OP_0D()
    Sleep(500)

    def lambda_141E():
        OP_6D(35930, 0, 43280, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_141E)
    OP_8E(0x8, 0x87DC, 0x0, 0xA546, 0x3E8, 0x0)
    OP_8E(0x8, 0x864C, 0x0, 0xAA50, 0x3E8, 0x0)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#754F女神啊， \x01",
            "请赐予这些孩子健康的明天吧……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在这里能渐渐听到火苗燃烧的声音＃\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#753F这是什么声音？\x01",
            "好像是柴火的声音……\x02\x03",
            "#753F……还有这气味是……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x8, 180, 500)

    ChrTalk(
        0x8,
        "#755F………………难道！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T2400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1240 end

    SaveToFile()

Try(main)
