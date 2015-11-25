from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4222   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4222.x',
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
        '克劳斯市长',                           # 9
        '莉拉',                                 # 10
        '梅贝尔市长',                           # 11
        '科林兹校长',                           # 12
        '茜亚',                                 # 13
        '金',                                   # 14
        '里拉老人',                             # 15
        '布莉姆',                               # 16
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
        'ED6_DT07/CH02350 ._CH',             # 00
        'ED6_DT07/CH02370 ._CH',             # 01
        'ED6_DT07/CH02360 ._CH',             # 02
        'ED6_DT07/CH02600 ._CH',             # 03
        'ED6_DT07/CH02620 ._CH',             # 04
        'ED6_DT07/CH02540 ._CH',             # 05
        'ED6_DT07/CH00070 ._CH',             # 06
        'ED6_DT07/CH02460 ._CH',             # 07
        'ED6_DT07/CH02230 ._CH',             # 08
        'ED6_DT07/CH02240 ._CH',             # 09
        'ED6_DT07/CH01100 ._CH',             # 0A
        'ED6_DT07/CH01350 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH02350P._CP',             # 00
        'ED6_DT07/CH02370P._CP',             # 01
        'ED6_DT07/CH02360P._CP',             # 02
        'ED6_DT07/CH02600P._CP',             # 03
        'ED6_DT07/CH02620P._CP',             # 04
        'ED6_DT07/CH02540P._CP',             # 05
        'ED6_DT07/CH00070P._CP',             # 06
        'ED6_DT07/CH02460P._CP',             # 07
        'ED6_DT07/CH02230P._CP',             # 08
        'ED6_DT07/CH02240P._CP',             # 09
        'ED6_DT07/CH01100P._CP',             # 0A
        'ED6_DT07/CH01350P._CP',             # 0B
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
        TalkScenaIndex      = 6,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        X                   = -139550,
        Z                   = 4000,
        Y                   = 9480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -78950,
        Z                   = 0,
        Y                   = 5960,
        Direction           = 359,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_20A",          # 00, 0
        "Function_1_358",          # 01, 1
        "Function_2_362",          # 02, 2
        "Function_3_378",          # 03, 3
        "Function_4_3D9",          # 04, 4
        "Function_5_59A",          # 05, 5
        "Function_6_5A7",          # 06, 6
        "Function_7_EE3",          # 07, 7
        "Function_8_EF0",          # 08, 8
        "Function_9_187E",         # 09, 9
        "Function_10_2539",        # 0A, 10
        "Function_11_2574",        # 0B, 11
        "Function_12_2FB0",        # 0C, 12
        "Function_13_358A",        # 0D, 13
        "Function_14_3737",        # 0E, 14
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_218")
    OP_A3(0x3FA)
    Event(0, 9)

    label("loc_218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_226")
    OP_A3(0x3FB)
    Event(0, 12)

    label("loc_226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_234")
    OP_A3(0x3FC)
    Event(0, 14)

    label("loc_234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_298")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, -28870, 0, 53540, 270)
    SetChrPos(0x9, -28040, 0, 54950, 211)
    SetChrPos(0xB, -83970, 0, -52980, 270)
    SetChrPos(0x8, -86020, 0, -52980, 90)

    label("loc_298")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (106, "loc_2A8"),
        (101, "loc_2CA"),
        (SWITCH_DEFAULT, "loc_2E0"),
    )


    label("loc_2A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C7")
    OP_A2(0x63F)
    Event(0, 11)

    label("loc_2C7")

    Jump("loc_2E0")

    label("loc_2CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DD")
    OP_A2(0x640)
    Event(0, 13)

    label("loc_2DD")

    Jump("loc_2E0")

    label("loc_2E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30A")
    SetChrChipByIndex(0x0, 7)
    SetChrChipByIndex(0x1, 8)
    SetChrChipByIndex(0x138, 9)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_30A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_319")
    SetChrFlags(0xE, 0x80)
    Jump("loc_357")

    label("loc_319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_328")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_357")

    label("loc_328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_337")
    SetChrFlags(0xE, 0x80)
    Jump("loc_357")

    label("loc_337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_346")
    SetChrFlags(0xE, 0x80)
    Jump("loc_357")

    label("loc_346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_350")
    Jump("loc_357")

    label("loc_350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_357")

    label("loc_357")

    Return()

    # Function_0_20A end

    def Function_1_358(): pass

    label("Function_1_358")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_358 end

    def Function_2_362(): pass

    label("Function_2_362")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_377")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_362")

    label("loc_377")

    Return()

    # Function_2_362 end

    def Function_3_378(): pass

    label("Function_3_378")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "嗯，接下来是打扫客房。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为今天有许多客人要在城里留宿，\x01",
            "所以要做的准备不少啊～\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_378 end

    def Function_4_3D9(): pass

    label("Function_4_3D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_3E6")
    Jump("loc_596")

    label("loc_3E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_495")

    ChrTalk(
        0xFE,
        (
            "《王城设计图》、《七至宝》、\x01",
            "《百日战役全貌》……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀呀，\x01",
            "被情报部拿走的这些书\x01",
            "终于又回来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_596")

    label("loc_495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_49F")
    Jump("loc_596")

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_4A9")
    Jump("loc_596")

    label("loc_4A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_510")

    ChrTalk(
        0xFE,
        (
            "完了，\x01",
            "格兰赛尔城的设计图纸竟然也不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "情报部的家伙\x01",
            "究竟打算拿去做什么啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_596")

    label("loc_510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_596")

    ChrTalk(
        0xFE,
        (
            "情报部的那群家伙，\x01",
            "到底要做什么啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "竟然把严禁外借的\x01",
            "重要资料强行取走了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_596")

    TalkEnd(0xFE)
    Return()

    # Function_4_3D9 end

    def Function_5_59A(): pass

    label("Function_5_59A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A6")
    Call(0, 6)

    label("loc_5A6")

    Return()

    # Function_5_59A end

    def Function_6_5A7(): pass

    label("Function_6_5A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE2")
    OP_A2(0x63B)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -85860, 0, -55170, 0)
    SetChrPos(0x102, -84960, 0, -55250, 0)
    OP_6D(-85030, 450, -53200, 1000)

    ChrTalk(
        0x8,
        (
            "#600F哦哦，来了吗。\x01",
            "艾丝蒂尔、约修亚，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#780F呵呵，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎……校长先生！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F难道校长先生您\x01",
            "也被邀请参加晚宴吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#780F是啊，就是乘今天的定期船\x01",
            "从卢安赶过来的呢。\x02\x03",
            "我已经听说了，\x01",
            "你们不是获得武术大会的冠军了吗？\x02\x03",
            "学生们听到了肯定也会十分高兴的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嘿嘿……\x01",
            "真的非常感谢您。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不过，只凭我们自己的力量\x01",
            "是不可能赢的。\x02\x03",
            "说起来，我没有想到\x01",
            "校长也会被邀请来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#600F科林兹校长作为\x01",
            "利贝尔首屈一指的贤者，\x01",
            "每年都会出席王国会议呢。\x02\x03",
            "被邀请出席晚宴\x01",
            "也没有什么奇怪的啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#780F哈哈，说我是贤者，\x01",
            "真是太过誉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯……王国会议是什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是为解决整个王国范围的问题，\x01",
            "而召开的一年一度的例会。\x02\x03",
            "女王陛下、各地区的市长，\x01",
            "以及各界的代表人士齐聚一堂，\x01",
            "讨论和协商各种各样的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哎～是这样啊。\x02\x03",
            "那么，今天的晚宴邀请的\x01",
            "都是这些人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#780F不……\x01",
            "其实连一半都不到。\x02\x03",
            "女王陛下身体欠佳，\x01",
            "摩尔根将军忙于军务……\x02\x03",
            "卢安的戴尔蒙市长\x01",
            "也因为那个案件被逮捕了。\x02\x03",
            "还有，拉赛尔博士也……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#600F和他相关的那个案件，\x01",
            "现在还有很多地方没有弄清楚呢。\x02\x03",
            "不仅牵扯到了亲卫队，\x01",
            "还说是大规模的恐怖组织所为，\x01",
            "到底有多少是真相啊……\x02\x03",
            "真是的，在这种情况下，\x01",
            "还有心思召开什么晚宴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#780F不过，为了确认\x01",
            "公爵阁下真正的心意，\x01",
            "也有出席这次晚宴的必要。\x02\x03",
            "而且，还要借此机会\x01",
            "探望和问候女王陛下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#600F嗯嗯。\x01",
            "这个才是最重要的呢。\x02\x03",
            "来到这格兰赛尔城，\x01",
            "不能拜见陛下\x01",
            "这不是扯的么。\x02\x03",
            "而且，也很久没有见到\x01",
            "科洛蒂娅公主了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F科洛蒂娅公主……\x01",
            "我记得是女王陛下的孙女吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F公主殿下\x01",
            "也住在格兰赛尔城吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#600F不，平常是住在\x01",
            "另外一个地方的。\x02\x03",
            "不过，听说几天前\x01",
            "回到王都来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哎～是这样啊……\x02\x03",
            "嗯～如果有机会，\x01",
            "一定要和她见上一面呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#780F呵呵，如果是你们，\x01",
            "肯定能见到她的。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_EE2")

    Return()

    # Function_6_5A7 end

    def Function_7_EE3(): pass

    label("Function_7_EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EEF")
    Call(0, 8)

    label("loc_EEF")

    Return()

    # Function_7_EE3 end

    def Function_8_EF0(): pass

    label("Function_8_EF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187D")
    OP_A2(0x63A)
    EventBegin(0x0)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -29280, 0, 55240, 135)
    SetChrPos(0x102, -30310, 0, 54780, 135)
    OP_6D(-28840, 0, 54560, 1000)

    ChrTalk(
        0x101,
        "#000F啊……梅贝尔市长！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F莉拉小姐也来了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#620F艾丝蒂尔小姐，约修亚先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#610F呵呵，我们又见面了呢。\x02\x03",
            "我一直等着\x01",
            "你们两个的到来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F梅贝尔市长\x01",
            "果然也被邀请参加晚宴呢。\x02\x03",
            "哎，\x01",
            "为什么会知道我们要来……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#610F我是听克劳斯市长说的。\x02\x03",
            "你们在武术大会中获得优胜，\x01",
            "从而被邀请出席晚宴。\x02\x03",
            "啊～如果早知道的话，\x01",
            " \x01",
            "来给你们加油了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#620F小姐，话虽这么说……\x02\x03",
            "如果这样，之后小姐自己\x01",
            "不是要非常辛苦了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#610F呜～我知道啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊哈哈……\x01",
            " \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#610F真是的，女王陛下暂且不论，\x01",
            "那个公爵举办的晚宴，\x01",
            "本来就没有什么闲工夫来参加啊……\x02\x03",
            "都是因为那个军队的女士官\x01",
            "固执地催促让我出席，\x01",
            "实在没办法才来王都的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F是情报部的凯诺娜上尉吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#610F嗯，就是她。\x02\x03",
            "虽然很有礼貌，其实不把人放在眼里，\x01",
            "我真是不喜欢那个人呢。\x02\x03",
            "最近，也没办法\x01",
            "和摩尔根将军取得联系……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F那是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F和哈肯门那边\x01",
            "联系不上吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#610F坚持说『将军不在』，\x01",
            "让我吃了闭门羹。\x02\x03",
            "好像是为了应对恐怖事件，\x01",
            "工作相当地繁忙呢。\x02\x03",
            "本来还想能不能\x01",
            "在今天的晚宴上见面呢……\x02\x03",
            "看起来好像也没有出席呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F是这样吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F市长对这件事是怎么想的？\x02\x03",
            "在这个时候把市长们召集起来\x01",
            "召开这样的晚宴……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#610F是呢……\x02\x03",
            "如果是女王陛下举办的话，\x01",
            "应该是要宣布重要的事情吧……\x02\x03",
            "不过这次大概只是为了\x01",
            "陪公爵阁下打发时间而已。\x02\x03",
            "滥用陛下代理人的特权，\x01",
            "让人认为他大权在握而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哇～真是精辟啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不过，\x01",
            "也有可能不只是为这样的理由。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#610F算了，听说这里的西餐\x01",
            "是整个王国最棒的……\x02\x03",
            "享用完美味的晚餐，\x01",
            "探望一下女王陛下，\x01",
            "然后就赶快回柏斯吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_187D")

    Return()

    # Function_8_EF0 end

    def Function_9_187E(): pass

    label("Function_9_187E")

    EventBegin(0x0)
    SetChrPos(0x101, -52050, 0, 2040, 0)
    SetChrPos(0x102, -52050, 0, 2040, 0)
    SetChrPos(0x108, -52050, 0, 2040, 0)
    SetChrPos(0xC, -52050, 0, 2040, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x40)
    OP_69(0x102, 0x0)
    OP_6A(0x102)

    def lambda_18DE():
        OP_8E(0xFE, 0xFFFECE9C, 0x0, 0x884, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_18DE)
    Sleep(500)

    def lambda_18FE():
        OP_8E(0xFE, 0xFFFECE9C, 0x0, 0x884, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18FE)
    Sleep(500)

    def lambda_191E():
        OP_8E(0xFE, 0xFFFECE9C, 0x0, 0x884, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_191E)
    Sleep(500)

    def lambda_193E():
        OP_8E(0xFE, 0xFFFECE9C, 0x0, 0x884, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_193E)
    WaitChrThread(0xC, 0x1)

    def lambda_195E():
        OP_8E(0xFE, 0xFFFECB86, 0x0, 0x1CDE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_195E)
    WaitChrThread(0x102, 0x1)

    def lambda_197E():
        OP_8E(0xFE, 0xFFFEC7F8, 0x0, 0x159A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_197E)
    WaitChrThread(0x101, 0x1)

    def lambda_199E():
        OP_8E(0xFE, 0xFFFECD2A, 0x0, 0x1554, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_199E)
    WaitChrThread(0x108, 0x1)

    def lambda_19BE():
        OP_8E(0xFE, 0xFFFECA50, 0x0, 0x1162, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_19BE)
    WaitChrThread(0xC, 0x1)
    Sleep(200)
    OP_8E(0xC, 0xFFFEC668, 0x0, 0x1C52, 0x7D0, 0x0)
    TurnDirection(0xC, 0x102, 0)

    ChrTalk(
        0xC,
        (
            "这个就是各位\x01",
            "晚上可以使用的房间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "请进吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯、嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么我们就告辞了。\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0xA)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0xA)
    Sleep(500)
    OP_43(0x108, 0x1, 0x0, 0xA)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    ClearMapFlags(0x1)
    Fade(1000)
    OP_6D(-79120, 0, 55910, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x108, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xC, -80040, 0, 50510, 0)
    SetChrPos(0x101, -80880, 0, 53000, 315)
    SetChrPos(0x102, -79650, 0, 53710, 270)
    SetChrPos(0x108, -78830, 0, 52390, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#000F哇……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F能在这种地方过夜，\x01",
            "真是无法想象呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哎呀～真是不错啊，\x01",
            "可以当成炫耀的资本了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "在晚宴开始之前，\x01",
            "请在此等候。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1C1C():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C1C)

    def lambda_1C2A():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C2A)

    def lambda_1C38():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1C38)
    OP_6D(-79790, 0, 52600, 1000)

    ChrTalk(
        0xC,
        (
            "虽然城内允许自由参观，\x01",
            "不过因为警卫上的理由，\x01",
            "有一些禁止进入的区域。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "请不要到那些地方去。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，具体来说\x01",
            "哪些地方不能去呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "首先是，\x01",
            "女王陛下居住的女王宫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "就是在屋顶空中庭园的一角\x01",
            "建造的小型宫殿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F空中庭园……\x01",
            "听起来感觉十分地美丽呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "嘻嘻……生日庆典的时候，\x01",
            "陛下会在那里的阳台上\x01",
            "向王都的市民致意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "如果只是到空中庭园去的话，\x01",
            "也应该足够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "还有，其他禁止进入的场所……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "在１楼的亲卫队办公室\x01",
            "以及地下的宝物库。\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0x108, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    ChrTalk(
        0x102,
        "#010F亲卫队办公室……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F是不是作为恐怖分子\x01",
            "受到通缉的那些人呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "是、是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "现在，那个办公室\x01",
            "正由情报部的人使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "所以不允许进入，\x01",
            "请你们理解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F差不多明白了。\x02\x03",
            "对了，晚宴邀请的其他客人\x01",
            "现在在哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "过一会儿，\x01",
            "你们就能见到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "大概他们现在\x01",
            "正在各自的房间里休息吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F那么，\x01",
            "克劳斯市长已经来了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "是的，\x01",
            "刚刚才招待过他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "那么，我先告退了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "如果有什么事情的话，\x01",
            "请到１楼的休息室来找我。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)

    def lambda_21AF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_21AF)
    OP_8E(0xC, 0xFFFEC6F4, 0x0, 0xBC3E, 0x3E8, 0x0)
    SetChrFlags(0xC, 0x4)

    ChrTalk(
        0x101,
        "#000F嗯……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    TurnDirection(0x102, 0x101, 400)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔和约修亚\x01",
            "趁金没有注意交换了眼色。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    def lambda_225A():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_225A)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(
        0x101,
        (
            "#000F……我说，金先生。\x02\x03",
            "我们想借此机会\x01",
            "在城里参观一下……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_22C5():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_22C5)

    ChrTalk(
        0x102,
        "#010F晚宴开始之前就会回来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哎呀哎呀，刚刚比赛完，\x01",
            "年轻人真是精力旺盛啊。\x02\x03",
            "好，你们去吧。\x02\x03",
            "吃饭之前\x01",
            "我就在这豪华的房间里休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6D(-79060, 0, 5580, 0)
    RemoveParty(0x7, 0xFF)
    SetChrPos(0x101, -79060, 0, 9840, 0)
    SetChrPos(0x102, -79060, 0, 9840, 0)

    def lambda_23EC():
        OP_8E(0xFE, 0xFFFECE2E, 0x0, 0x15B8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23EC)
    Sleep(600)

    def lambda_240C():
        OP_8E(0xFE, 0xFFFECA5A, 0x0, 0x190A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_240C)
    WaitChrThread(0x101, 0x1)

    def lambda_242C():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_242C)
    WaitChrThread(0x102, 0x1)

    def lambda_243F():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_243F)

    ChrTalk(
        0x101,
        (
            "#000F在晚宴开始之前，\x01",
            "一定要尽可能多做一些事情。\x02\x03",
            "首先要去找\x01",
            "尤莉亚小姐所说的希尔丹夫人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F还有，我们最好\x01",
            "去和其他的客人打个招呼。\x02\x03",
            "大概，认识的人会很多吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_6A(0x0)
    ClearMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_9_187E end

    def Function_10_2539(): pass

    label("Function_10_2539")

    OP_8E(0xFE, 0xFFFECB5E, 0x0, 0x1CA2, 0xBB8, 0x0)

    def lambda_2553():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2553)
    OP_8E(0xFE, 0xFFFECB68, 0x0, 0x2602, 0xBB8, 0x0)
    Return()

    # Function_10_2539 end

    def Function_11_2574(): pass

    label("Function_11_2574")

    EventBegin(0x0)
    OP_6D(-80130, 0, 51090, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    AddParty(0x7, 0xFF)
    SetChrPos(0x101, -80670, 0, 51310, 270)
    SetChrPos(0x102, -79770, 0, 50560, 270)
    SetChrPos(0x108, -87580, 0, 52200, 90)
    OP_6D(-83020, 0, 52310, 2000)

    ChrTalk(
        0x108,
        (
            "#070F哟，艾丝蒂尔、约修亚。\x01",
            "回来的是不是有些晚呢。\x02\x03",
            "就要到晚宴开始的时候了吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2653():
        OP_8E(0xFE, 0xFFFEBD4E, 0x0, 0xCDA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2653)
    Sleep(300)

    def lambda_2673():
        OP_6D(-86640, 0, 52720, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2673)

    def lambda_268B():
        OP_8E(0xFE, 0xFFFEBD4E, 0x0, 0xCDA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_268B)
    WaitChrThread(0x101, 0x1)

    def lambda_26AB():
        OP_8E(0xFE, 0xFFFEB042, 0x0, 0xD0D4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26AB)
    WaitChrThread(0x102, 0x1)

    def lambda_26CB():
        OP_8E(0xFE, 0xFFFEAFF2, 0x0, 0xCB48, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_26CB)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x108, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x101,
        (
            "#000F抱歉啊，金大哥。\x02\x03",
            "东看看西逛逛的\x01",
            "就把时间给忘了～\x02\x03",
            "而且还和各地的市长们\x01",
            "谈了许多哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F咦，你们俩之前就\x01",
            "认识那些有身份的人物吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F洛连特的市长\x01",
            "平日里就对我们很亲切。\x02\x03",
            "其他的几位是我们在旅行\x01",
            "途中经过各个城市时认识的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F原来如此啊。\x02\x03",
            "游击士在完成任务的时候，\x01",
            "的确有许多结识有身份人物的机会呢。\x02\x03",
            "可是这样看来，\x01",
            "你们好像极为活跃对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哈哈哈……还没有到那种程度啦。\x02\x03",
            "金大哥到王都来是因为\x01",
            "有什么任务要完成吗？\x02\x03",
            "我想，虽说是在别国，\x01",
            "但还是照样可以完成相关任务吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F是啊，一旦成为了正游击士，\x01",
            "就可以去做一些超越国界的任务了……\x02\x03",
            "预选赛啊，大使馆的手续啊什么的，\x01",
            "弄得我连接受任务的时间都没有了。\x02\x03",
            "唉，如果另外再来四位游击士的话，\x01",
            "就可以不用我来参加比赛了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F的确，如果游击士们都聚集到了这里，\x01",
            "大部分事件都可以很快解决的。\x02\x03",
            "可若是都在王都集中了的话，\x01",
            "其他地方的支部可就难办了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F哇哈哈，说的也是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F呼，总觉得到现在才\x01",
            "想到这些也用处不大了。\x02\x03",
            "雪拉姐现在在洛连特\x01",
            "做什么呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F雪拉姐……\x01",
            "是指雪拉扎德吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F咦……你认识她！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是呀，她是我们的前辈，\x01",
            "过去一直都在照顾着我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F原来如此，竟然是这样。\x02\x03",
            "以前她到卡尔瓦德来的时候\x01",
            "和我认识的。\x02\x03",
            "她有一个很好的老师啊，\x01",
            "年纪轻轻却是见多识广。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2D1A():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D1A)

    def lambda_2D28():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D28)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#000F（他说的那个老师不就是……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（嗯，就是父亲呢。）\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0xC, -80120, 0, 48440, 315)

    def lambda_2DD1():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2DD1)

    def lambda_2DDF():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2DDF)

    def lambda_2DED():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2DED)

    ChrTalk(
        0xC,
        (
            "打搅一下，\x01",
            "晚宴已经准备完毕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "让我带你们大家去可以吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哦啊，我等的都有些腻烦了呢。\x02\x03",
            "那～么，我们这就去\x01",
            "好好享用这顿美餐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，说起来在比赛之后\x01",
            "我的肚子已经饿的不行了。\x02\x03",
            "走吧～大吃一顿去了～⊙\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_8C(0x102, 315, 400)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#010F我说你们俩啊……\x02\x03",
            "还是不要忘记了\x01",
            "餐桌上的那些礼仪了哦……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4251   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_2574 end

    def Function_12_2FB0(): pass

    label("Function_12_2FB0")

    EventBegin(0x0)
    OP_6D(-79320, 0, 55910, 0)
    RemoveParty(0x7, 0xFF)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -79660, 0, 56600, 192)
    SetChrPos(0x101, -80390, 0, 55080, 23)
    SetChrPos(0x102, -78690, 0, 55240, 315)

    ChrTalk(
        0xD,
        (
            "#070F哎呀，出乎预料的事\x01",
            "竟然意外的听说了。\x02\x03",
            "我一来就插入你们国家的谈话，\x01",
            "把你们两个很是\x01",
            "吓了一跳对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F那、那是当然的了！\x02\x03",
            "要、要不是说的\x01",
            "还比较周到的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#070F啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，嗯，没什么。\x02\x03",
            "其实……\x01",
            "真是遗憾啊。\x02\x03",
            "虽然特地让舌头沉醉于\x01",
            "美味的料理之中，\x01",
            "可最后那道菜的精妙还是没能体会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F哈哈，不用强求嘛。\x02\x03",
            "对了，艾丝蒂尔，\x01",
            "去散散步消化一下食物如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F咦……？\x02\x03",
            "啊啊！\x01",
            "对呀，好建议！\x02\x03",
            "不错呢～我也想好好\x01",
            "呼吸一下外面的新鲜空气了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#070F啊～刚才去参观各处，\x01",
            "这回吃完饭又要去散步了……\x02\x03",
            "想不承认都不行啊，\x01",
            "这就是年纪的差异导致的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊哈哈，金大哥你太夸张了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F金兄也去\x01",
            "走走如何？\x02\x03",
            "这个历史久远的建筑\x01",
            "可供参观的地方不少呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#070F嗯，等我想到了的时候\x01",
            "再到处溜达一下也不迟。\x02\x03",
            "我要去厨房看看，\x01",
            "应该还有一些剩余的食物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F不会吧……\x01",
            "还要打算吃吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#070F也算是吧，\x01",
            "就是想弄点酒菜。\x02\x03",
            "想喝酒可以到谈话室去，\x01",
            "待会儿我就去瞧瞧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4A, 0x4, 0x2)
    OP_28(0x4A, 0x4, 0x4)
    OP_28(0x4A, 0x1, 0x1)
    OP_28(0x4A, 0x1, 0x2)
    OP_28(0x4A, 0x1, 0x4)
    EventEnd(0x0)
    Return()

    # Function_12_2FB0 end

    def Function_13_358A(): pass

    label("Function_13_358A")

    EventBegin(0x0)
    OP_6D(-79060, 0, 5580, 0)
    SetChrPos(0x101, -79060, 0, 9840, 0)
    SetChrPos(0x102, -79060, 0, 9840, 0)

    def lambda_35C5():
        OP_8E(0xFE, 0xFFFECE2E, 0x0, 0x15B8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35C5)
    Sleep(600)

    def lambda_35E5():
        OP_8E(0xFE, 0xFFFECA5A, 0x0, 0x190A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_35E5)
    WaitChrThread(0x101, 0x1)

    def lambda_3605():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3605)
    WaitChrThread(0x102, 0x1)

    def lambda_3618():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3618)

    ChrTalk(
        0x101,
        (
            "#000F呼～……\x01",
            "真是出乎预料的事啊。\x02\x03",
            "越来越想去见女王陛下，\x01",
            "并问问到底怎么回事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F首先按照约定\x01",
            "去见希尔丹夫人吧。\x02\x03",
            "她应该有办法\x01",
            "让我们见到陛下的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，明白。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_13_358A end

    def Function_14_3737(): pass

    label("Function_14_3737")

    EventBegin(0x0)
    OP_6D(-79860, 0, 50720, 0)
    SetChrPos(0x101, -80040, 0, 48610, 0)
    SetChrPos(0x102, -80040, 0, 48610, 0)
    SetChrPos(0x108, -80040, 0, 48610, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x108, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_37A4():
        OP_6D(-79660, 0, 55360, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_37A4)

    def lambda_37BC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_37BC)

    def lambda_37CE():
        OP_8E(0xFE, 0xFFFEC762, 0x0, 0xDA52, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_37CE)
    Sleep(500)

    def lambda_37EE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_37EE)

    def lambda_3800():
        OP_8E(0xFE, 0xFFFEC640, 0x0, 0xD426, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3800)
    Sleep(500)

    def lambda_3820():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3820)

    def lambda_3832():
        OP_8E(0xFE, 0xFFFECAC8, 0x0, 0xD3CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3832)
    WaitChrThread(0x108, 0x1)
    OP_8C(0x108, 180, 400)

    ChrTalk(
        0x108,
        (
            "#070F哎呀哎呀……\x02\x03",
            "总算是用比较擅长的\x01",
            "手法蒙混过去了。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#000F哎……！\x02\x03",
            "金大哥，\x01",
            "你不是喝醉了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F那个啊，只是演技而已。\x02\x03",
            "我可是一滴酒都没喝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F说谎！？\x01",
            "明明脸那么红……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F驱动内力，让血气上游，\x01",
            "让表面看起来一副喝醉的样子……\x02\x03",
            "在东方武术里，\x01",
            "这就是所谓『气功』的功夫对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哦，这种事情\x01",
            "你都知道，让我吃惊不小呢。\x02\x03",
            "哎呀，刚才看见你们陷入困境，\x01",
            "我就忍不住叫了你们一声。\x02\x03",
            "如何，还算帮了点忙吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F真是的，金大哥你呀，\x01",
            "让人捉摸不透～\x02\x03",
            "虽说是来帮忙的，\x01",
            "但着实吓了人一跳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哈哈，抱歉抱歉。\x02\x03",
            "那么，情况怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F？？？\x02\x03",
            "什么怎么样呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F办完了吧。\x02\x03",
            "和女王陛下见面的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#000F什、什么～！？\x02\x03",
            "为、为、为什么金大哥你知道！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F难道说是在艾南先生\x01",
            "那里听说了什么吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F协会那个兄弟\x01",
            "并没有告诉我什么。\x02\x03",
            "如果要说有什么的话，\x01",
            "就是他曾经款待过我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F款待……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F……没有任何情报，\x01",
            "是不可能做出这样的推断的。\x02\x03",
            "金兄……\x01",
            "你究竟知道些什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F嗯……\x02\x03",
            "也该是时候把那个东西\x01",
            "拿给你们看看了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x108, 0xFFFEC6D6, 0x0, 0xD6B0, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "金从怀中取出一封信\x01",
            "递给了艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0x108, 0xFFFEC762, 0x0, 0xDA52, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        "#000F信、信……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F这个笔迹是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F嗯，你们先拿来\x01",
            "读一读吧。\x02\x03",
            "然后就知道怎么回事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯、嗯……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔\x01",
            "开始阅读信的内容。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "金·瓦赛克阁下敬启。\x01",
            "久疏问候，身体可好。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "由于事出匆忙，我只有采取\x01",
            "开门见山的方式，万望见谅。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "事实上，连同猎兵团在内的事件\x01",
            "已经朝向帝国方向发展了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "可是，利贝尔国内似乎正有\x01",
            "一股微妙的势力正在滋长蔓延着。\x01",
            "若只是交给年轻人去处理，我有些放心不下。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我想请您帮忙。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在我外出的时候，您到利贝尔来，\x01",
            "如果有什么情况发生的话，\x01",
            "就帮帮那些年轻人们，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "因为您是第一次前往利贝尔，\x01",
            "所以顺便游山玩水也是不错的选择。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "女王诞辰庆典前夕，会召开\x01",
            "允许外国人参加的武术大会，\x01",
            "这是一个很好的机会呢。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "突然提出这样的请求，或许让您有些为难，\x01",
            "不过如果您有空的话，还请帮一帮忙。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "女王诞辰庆典时我会回来，\x01",
            "到那时我再一并感谢。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　　　　　卡西乌斯·布莱特\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "另：\x01",
            "您也许会有机会见到\x01",
            "我的女儿和儿子。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我让他们在游击士协会实习，\x01",
            "当时没有想太多，只是锻炼一下他们。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "如果他们有什么事，还请您\x01",
            "助他们一臂之力，帮他们摆脱困境。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#000F……这、这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F金兄是父亲委托\x01",
            "来利贝尔的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F嗯，就是这样的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F什么叫就是这样的……\x02\x03",
            "关、关键的是金大哥\x01",
            "你竟然和老爸串通一气！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F串通一气什么的不太好听啊。\x02\x03",
            "以前卡西乌斯大人\x01",
            "来到我们卡尔瓦德时，\x01",
            "我也受到了他很多的关照。\x02\x03",
            "我一直都想报答他，\x01",
            "这封信正好了却了我的心愿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是什么时候\x01",
            "发觉我们是父亲的孩子的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F第一次见面时，\x01",
            "看见艾丝蒂尔拿着棒子，\x01",
            "我就开始有些注意了……\x02\x03",
            "在询问了雾香之后我才确信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F真是的，怎么能这样……\x02\x03",
            "之前连一个字\x01",
            "也没有和我们提起过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哈哈，大人的信上\x01",
            "写着『不要太溺爱他们』呢。\x02\x03",
            "让我最低限度地帮助你们，\x01",
            "平时守护着就可以了……\x02\x03",
            "话又说回来，看来你们俩已经\x01",
            "完成了一件不小的事情对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，嗯……\x02\x03",
            "我说约修亚，\x01",
            "现在说出来就没问题了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，既然如此，\x01",
            "我就一一道来吧。\x02\x03",
            "我们刚刚办完的事情\x01",
            "要说起来是一个很长的故事呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔她们把博士的委托，\x01",
            "见到艾莉茜雅女王……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "还有接受了女王的委托，要将被捉走的\x01",
            "科洛蒂娅公主解救出来的事情说了出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x108,
        (
            "#070F原来如此啊……\x02\x03",
            "听了晚宴上那些话后，\x01",
            "我就感觉充满了火药味……\x02\x03",
            "好的，为了完成这个委托，\x01",
            "也让我助你们一臂之力吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎，可以吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F啊，这是报答卡西乌斯大人\x01",
            "恩情的绝好机会呢。\x02\x03",
            "请务必让我帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F我、我们俩也请你\x01",
            "多多关照了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F再次请您多多关照。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F哦，彼此彼此啦。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C4300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_3737 end

    SaveToFile()

Try(main)
