from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4135   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4135.x',
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
        '馆长',                                 # 9
        '森特',                                 # 10
        '莉西娅',                               # 11
        '亚鲁瓦教授',                           # 12
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
        'ED6_DT07/CH01490 ._CH',             # 00
        'ED6_DT07/CH01660 ._CH',             # 01
        'ED6_DT07/CH01540 ._CH',             # 02
        'ED6_DT07/CH02050 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01490P._CP',             # 00
        'ED6_DT07/CH01660P._CP',             # 01
        'ED6_DT07/CH01540P._CP',             # 02
        'ED6_DT07/CH02050P._CP',             # 03
    )

    DeclNpc(
        X                   = 1890,
        Z                   = 0,
        Y                   = 77500,
        Direction           = 171,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -69000,
        Z                   = 0,
        Y                   = -2520,
        Direction           = 79,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 4400,
        Z                   = 0,
        Y                   = -5910,
        Direction           = 255,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 470,
        Z                   = 0,
        Y                   = -3730,
        Direction           = 282,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    DeclActor(
        TriggerX            = 2580,
        TriggerZ            = 0,
        TriggerY            = -5970,
        TriggerRange        = 800,
        ActorX              = 4400,
        ActorZ              = 1700,
        ActorY              = -5910,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5090,
        TriggerZ            = 0,
        TriggerY            = 2190,
        TriggerRange        = 800,
        ActorX              = 5090,
        ActorZ              = 800,
        ActorY              = 2190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7840,
        TriggerZ            = 4000,
        TriggerY            = 6700,
        TriggerRange        = 800,
        ActorX              = 7840,
        ActorZ              = 5700,
        ActorY              = 6700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75860,
        TriggerZ            = 0,
        TriggerY            = -2000,
        TriggerRange        = 800,
        ActorX              = 75860,
        ActorZ              = 1500,
        ActorY              = -2000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 73200,
        TriggerZ            = 0,
        TriggerY            = 710,
        TriggerRange        = 800,
        ActorX              = 73200,
        ActorZ              = 800,
        ActorY              = 710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 68740,
        TriggerZ            = 0,
        TriggerY            = 7310,
        TriggerRange        = 800,
        ActorX              = 68740,
        ActorZ              = 800,
        ActorY              = 7310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 73480,
        TriggerZ            = 0,
        TriggerY            = 6420,
        TriggerRange        = 800,
        ActorX              = 73480,
        ActorZ              = 800,
        ActorY              = 6420,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75820,
        TriggerZ            = 4000,
        TriggerY            = 8010,
        TriggerRange        = 800,
        ActorX              = 75820,
        ActorZ              = 5700,
        ActorY              = 8010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 71960,
        TriggerZ            = 4000,
        TriggerY            = 9290,
        TriggerRange        = 800,
        ActorX              = 71960,
        ActorZ              = 4800,
        ActorY              = 9290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20,
        TriggerZ            = 0,
        TriggerY            = 77880,
        TriggerRange        = 800,
        ActorX              = -20,
        ActorZ              = 1700,
        ActorY              = 77880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -770,
        TriggerZ            = 0,
        TriggerY            = 72650,
        TriggerRange        = 800,
        ActorX              = -770,
        ActorZ              = 800,
        ActorY              = 72650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7000,
        TriggerZ            = 0,
        TriggerY            = 66550,
        TriggerRange        = 1200,
        ActorX              = 7000,
        ActorZ              = 800,
        ActorY              = 66550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1770,
        TriggerZ            = 0,
        TriggerY            = 66890,
        TriggerRange        = 800,
        ActorX              = 1770,
        ActorZ              = 800,
        ActorY              = 66890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3790,
        TriggerZ            = 0,
        TriggerY            = 64959,
        TriggerRange        = 800,
        ActorX              = -3790,
        ActorZ              = 800,
        ActorY              = 64959,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_342",          # 00, 0
        "Function_1_514",          # 01, 1
        "Function_2_561",          # 02, 2
        "Function_3_577",          # 03, 3
        "Function_4_1A6B",         # 04, 4
        "Function_5_1A70",         # 05, 5
        "Function_6_2285",         # 06, 6
        "Function_7_2FE0",         # 07, 7
        "Function_8_3AD7",         # 08, 8
        "Function_9_3C78",         # 09, 9
        "Function_10_3E20",        # 0A, 10
        "Function_11_3FCD",        # 0B, 11
        "Function_12_40BC",        # 0C, 12
        "Function_13_41A9",        # 0D, 13
        "Function_14_4299",        # 0E, 14
        "Function_15_4378",        # 0F, 15
        "Function_16_4458",        # 10, 16
        "Function_17_45F1",        # 11, 17
        "Function_18_477F",        # 12, 18
        "Function_19_48B0",        # 13, 19
        "Function_20_4977",        # 14, 20
    )


    def Function_0_342(): pass

    label("Function_0_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_362")
    SetChrPos(0x9, -69600, 0, 3910, 71)
    SetChrFlags(0xB, 0x80)
    Jump("loc_513")

    label("loc_362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_393")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, -72260, 0, -3090, 183)
    SetChrPos(0xB, -73180, 0, 58630, 225)
    Jump("loc_513")

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3C4")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, -75330, 0, 2770, 173)
    SetChrPos(0xB, -73180, 0, 58630, 225)
    Jump("loc_513")

    label("loc_3C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3F5")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, -69770, 0, 6640, 341)
    SetChrPos(0xB, -73180, 0, 58630, 225)
    Jump("loc_513")

    label("loc_3F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_415")
    SetChrPos(0xB, -73180, 0, 58630, 225)
    SetChrFlags(0xB, 0x80)
    Jump("loc_513")

    label("loc_415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_441")
    SetChrPos(0x9, -69200, 0, 0, 111)
    SetChrPos(0xB, -73180, 0, 58630, 225)
    Jump("loc_513")

    label("loc_441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_46D")
    SetChrPos(0x9, 70400, 0, 3610, 0)
    SetChrPos(0xB, -72380, 0, -1410, 254)
    Jump("loc_513")

    label("loc_46D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_499")
    SetChrPos(0x9, -72260, 0, -3090, 183)
    SetChrPos(0xB, 69350, 0, 6420, 315)
    Jump("loc_513")

    label("loc_499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4C5")
    SetChrPos(0x9, -75330, 0, 2770, 173)
    SetChrPos(0xB, 72040, 0, 2370, 109)
    Jump("loc_513")

    label("loc_4C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4F1")
    SetChrPos(0x9, -69770, 0, 6640, 341)
    SetChrPos(0xB, 3520, 0, 1550, 57)
    Jump("loc_513")

    label("loc_4F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_513")
    SetChrPos(0x8, -1010, 0, -3780, 75)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_513")

    Return()

    # Function_0_342 end

    def Function_1_514(): pass

    label("Function_1_514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_547")
    OP_B1("t4135_y")
    Jump("loc_550")

    label("loc_547")

    OP_B1("t4135_n")

    label("loc_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_560")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_560")

    Return()

    # Function_1_514 end

    def Function_2_561(): pass

    label("Function_2_561")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_576")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_561")

    label("loc_576")

    Return()

    # Function_2_561 end

    def Function_3_577(): pass

    label("Function_3_577")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_584")
    Jump("loc_1A67")

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_7C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_68C")
    TurnDirection(0xB, 0x102, 400)

    ChrTalk(
        0xB,
        (
            "#130F越是困难的任务，\x01",
            "越要充分休息才能取得良好的结果哦。\x01",
            "　\x02\x03",
            "#132F哈哈，\x01",
            "我这一年里可是不停地在休息呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C3")

    label("loc_68C")

    OP_A2(0x3)
    TurnDirection(0xB, 0x102, 400)

    ChrTalk(
        0xB,
        (
            "#130F哦，是约修亚啊。\x02\x03",
            "从你的脸色来看，\x01",
            "好像相当紧张啊，\x01",
            "怎么回事呢？\x02\x03",
            "越是困难的任务，\x01",
            "越要充分休息才能取得良好的结果哦。\x01",
            "　\x02\x03",
            "#132F哈哈，\x01",
            "我这一年里可是不停地在休息呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C3")

    Jump("loc_1A67")

    label("loc_7C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_BDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_87B")

    ChrTalk(
        0xB,
        (
            "#132F我对王城里面的样子相当感兴趣……\x01",
            " \x02\x03",
            "不过照现在这种情况看来，\x01",
            "只有等王城再次向普通市民开放了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDC")

    label("loc_87B")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "#130F说起来，\x01",
            "利贝尔王室的历史似乎相当悠久呢。\x02\x03",
            "如果追寻源头的话，\x01",
            "可是要回溯到一千多年以前呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F咦～\x01",
            "利贝尔王室那么早就有了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#132F是的，正因为如此，\x01",
            "我对王城里面的样子相当感兴趣……\x01",
            "　\x02\x03",
            "艾丝蒂尔你们昨天\x01",
            "被招待进王城做客了吧？\x02\x03",
            "方便的话，\x01",
            "可以把你们的见闻告诉我吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F唔……这个……\x02\x03",
            "好像体会到了历史传统的厚重感……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我觉得确实有不少地方值得一看。\x01",
            "　\x02\x03",
            "不过，\x01",
            "我们也没有时间将每个角落都逛一遍。\x02\x03",
            "或许不能给教授太多的参考吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#131F是吗……\x02\x03",
            "好可惜啊，\x01",
            "只有等王城再次向普通市民开放了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDC")

    Jump("loc_1A67")

    label("loc_BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_11A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_C6A")

    ChrTalk(
        0xFE,
        (
            "#132F多亏了艾丝蒂尔你们的大力协助，\x01",
            "我的研究才会那么顺利。\x01",
            "　\x02\x03",
            "近期肯定会做出成果让你们看的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A6")

    label("loc_C6A")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "#130F呀，艾丝蒂尔、约修亚。\x02\x03",
            "#132F我看到了，决赛很精彩，\x01",
            "恭喜你们取得优胜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿，谢谢。\x02\x03",
            "……对了，\x01",
            "#501F亚鲁瓦教授你这边又怎样了？\x02\x03",
            "研究有进展吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#130F嗯，\x01",
            "资料馆委托的古代文书的解析很顺利……\x02\x03",
            "也找到了很多我向往以久的文献。\x01",
            "　\x02\x03",
            "要做的事真是很多啊，\x01",
            "不过时间好像怎么都不够用呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊～……\x01",
            "我要对你刮目相看了呢。\x02\x03",
            "#007F教授到底不愧是\x01",
            "醉心于研究的学者呢～\x02\x03",
            "要是我的话，\x01",
            "肯定不可能做到像你那样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F哈哈，\x01",
            "首先要让艾丝蒂尔一直坐在椅子上不动，\x01",
            "这点就做不到呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯嗯，\x01",
            "我一坐下就感到非常困，\x01",
            "必须得活动活动身体才行。\x02\x03",
            "#001F对了，\x01",
            "正所谓只有流动的水中\x01",
            "才会有鱼儿生存嘛。\x02\x03",
            "我想和这是一样的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F呼～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F唔，你有什么不满吗……\x02\x03",
            "#506F不、不过，\x01",
            "研究能顺利地进行实在是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#132F哈哈，\x01",
            "这也多亏了艾丝蒂尔你们的大力协助啊。\x01",
            "　\x02\x03",
            "近期肯定会做出成果让你们看的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A6")

    Jump("loc_1A67")

    label("loc_11A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_129D")

    ChrTalk(
        0xB,
        (
            "#130F呼，\x01",
            "整整三天都埋头在资料馆里搞研究，　\x01",
            "好久没有去晒晒太阳了。\x02\x03",
            "我也感觉到有些累了，\x01",
            "为了转换心情就出去转转吧。\x02\x03",
            "偶尔奢侈一下，\x01",
            "去尝尝冰淇淋也不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A67")

    label("loc_129D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1369")

    ChrTalk(
        0xB,
        (
            "#130F哎呀，找到不少似乎可以\x01",
            "当作研究材料的资料呢。\x02\x03",
            "我打算马上着手解析古文书。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A67")

    label("loc_1369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_14D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_13F0")

    ChrTalk(
        0xB,
        (
            "#130F呵呵，\x01",
            "这些可都是没有公开过的收藏品啊……\x02\x03",
            "哎呀，\x01",
            "真是又开心又紧张呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D4")

    label("loc_13F0")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "#130F呵呵，\x01",
            "这些可都是没有公开过的收藏品啊……\x02\x03",
            "我来看看，\x01",
            "究竟会有些什么样的宝贝呢。\x02\x03",
            "哎呀，\x01",
            "真是又开心又紧张呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D4")

    Jump("loc_1A67")

    label("loc_14D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1715")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1581")

    ChrTalk(
        0xB,
        (
            "#130F想象力对于考古学而言\x01",
            "可是很重要的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1712")

    label("loc_1581")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "#130F唔～\x01",
            "这些展品我都很感兴趣。\x02\x03",
            "那边的浮雕\x01",
            "很可能是大崩坏之前的产物。\x02\x03",
            "不觉得其风格和\x01",
            "四轮之塔的内部有些相似吗？\x02\x03",
            "想象力对于考古学而言\x01",
            "可是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1712")

    Jump("loc_1A67")

    label("loc_1715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_18D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_17DB")

    ChrTalk(
        0xFE,
        (
            "#132F利贝尔各地散布着的遗迹\x01",
            "可能是古代塞姆里亚文明的遗物啊。\x01",
            "　\x02\x03",
            "实地调查已经完成了，\x01",
            "接下来就是参考各种文献，\x01",
            "让考察获得更多进展。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D5")

    label("loc_17DB")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "#130F卢安近郊的大型水道桥『艾尔·雷登』……\x01",
            "　\x02\x03",
            "环绕王都格兰赛尔的长城『亚宁堡』……\x01",
            "　\x02\x03",
            "以及散布在各地的『四轮之塔』……\x01",
            "　\x02\x03",
            "#132F这些都有可能是\x01",
            "古代塞姆里亚文明的遗迹。\x02\x03",
            "实地调查已经完成了，\x01",
            "接下来就是参考各种文献，\x01",
            "让考察获得更多进展。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D5")

    Jump("loc_1A67")

    label("loc_18D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1A48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_195E")

    ChrTalk(
        0xB,
        (
            "#130F是立刻展开研究呢，\x01",
            "还是先到街上游览呢……\x02\x03",
            "哈哈，真是举棋不定呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A45")

    label("loc_195E")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "#130F不愧是王都格兰赛尔。\x02\x03",
            "恐怖事件基本没有造成什么影响，\x01",
            "街道依旧那么热闹。\x01",
            "　\x02\x03",
            "唔，是立刻展开研究工作呢，\x01",
            "还是先到街上游览呢……\x01",
            "　\x02\x03",
            "哈哈，真是举棋不定呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A45")

    Jump("loc_1A67")

    label("loc_1A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1A67")

    ChrTalk(
        0xB,
        "#130F承蒙您的关照了，馆长。\x02",
    )

    CloseMessageWindow()

    label("loc_1A67")

    TalkEnd(0xFE)
    Return()

    # Function_3_577 end

    def Function_4_1A6B(): pass

    label("Function_4_1A6B")

    Call(0, 5)
    Return()

    # Function_4_1A6B end

    def Function_5_1A70(): pass

    label("Function_5_1A70")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1AEB")

    ChrTalk(
        0xA,
        (
            "亚鲁瓦教授\x01",
            "跑到哪里去了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我还想听听\x01",
            "教授的特别演讲呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2281")

    label("loc_1AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1BC4")

    ChrTalk(
        0xA,
        (
            "外面的情况\x01",
            "似乎和平常不太一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "刚才还吵吵嚷嚷的，\x01",
            "现在一下就安静了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2281")

    label("loc_1BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1DE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1CAF")

    ChrTalk(
        0xA,
        (
            "诞辰庆典\x01",
            "准备得怎么样了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "总不能让女王陛下\x01",
            "带着病体参加吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DDE")

    label("loc_1CAF")

    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "武术大会结束以后，\x01",
            "感觉街上也安静下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不过，诞辰庆典方面\x01",
            "准备得怎么样了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "总不能让女王陛下\x01",
            "带着病体参加吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DDE")

    Jump("loc_2281")

    label("loc_1DE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1E95")

    ChrTalk(
        0xA,
        (
            "武术大会\x01",
            "平安无事地结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "亚鲁瓦教授\x01",
            "去看比赛了，\x01",
            "我真有点羡慕他呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2281")

    label("loc_1E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1EFA")

    ChrTalk(
        0xA,
        (
            "今天终于到了\x01",
            "武术大会总决赛了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我不能去看比赛，\x01",
            "呆在这儿心里直痒痒。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2281")

    label("loc_1EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1F99")

    ChrTalk(
        0xA,
        (
            "刚才收到了一封\x01",
            "从柏斯寄给馆长的快递。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "必须快点交给他。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2281")

    label("loc_1F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_206D")

    ChrTalk(
        0xA,
        (
            "本资料馆内\x01",
            "禁止吸烟和摄影。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "请客人予以配合。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2281")

    label("loc_206D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2104")

    ChrTalk(
        0xA,
        (
            "本来在研究者中\x01",
            "奇怪的人就不少……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "但亚鲁瓦教授\x01",
            "更让人感到不可思议。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2281")

    label("loc_2104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_214D")

    ChrTalk(
        0xA,
        (
            "唔～武术大会开始后，\x01",
            "到馆里来的游客变得稀少了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2281")

    label("loc_214D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_21E9")

    ChrTalk(
        0xA,
        (
            "最近在街道上\x01",
            "也时常见到王国军的士兵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "是因为亲卫队使用的飞艇\x01",
            "停泊在空港吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2281")

    label("loc_21E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2281")

    ChrTalk(
        0xA,
        (
            "欢迎光临\x01",
            "格兰赛尔历史资料馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "现在正在举行\x01",
            "『利贝尔现代化之路』\x01",
            "收藏资料主题展。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2281")

    TalkEnd(0xA)
    Return()

    # Function_5_1A70 end

    def Function_6_2285(): pass

    label("Function_6_2285")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2303")

    ChrTalk(
        0xFE,
        "外面很是热闹啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "等我手头的工作做完后，\x01",
            "也要到街上去\x01",
            "体验一下庆典的氛围。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FDC")

    label("loc_2303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_246E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_23AB")

    ChrTalk(
        0xFE,
        (
            "刚才王国军的士兵\x01",
            "也到这里来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像是为了搜捕\x01",
            "亲卫队的人而来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_246B")

    label("loc_23AB")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "昨天王国军的士兵\x01",
            "也到这里来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像是为了搜捕\x01",
            "亲卫队的人而来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "士兵们都是一幅\x01",
            "很焦急的样子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_246B")

    Jump("loc_2FDC")

    label("loc_246E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2595")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2501")

    ChrTalk(
        0xFE,
        (
            "刚才接到了馆长\x01",
            "从柏斯传来的消息……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像因为定期船全部停航\x01",
            "而无法回王都来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2592")

    label("loc_2501")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "刚才接到了馆长\x01",
            "从柏斯传来的消息……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像因为定期船全部停航\x01",
            "而无法回王都来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是麻烦啊……\x02",
    )

    CloseMessageWindow()

    label("loc_2592")

    Jump("loc_2FDC")

    label("loc_2595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_25FD")

    ChrTalk(
        0xFE,
        (
            "馆长收到了一封信，\x01",
            "就急急忙忙地出差去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在也许\x01",
            "已经到柏斯了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FDC")

    label("loc_25FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_26DE")

    ChrTalk(
        0xFE,
        (
            "馆长把今天的决赛门票\x01",
            "送给了亚鲁瓦教授。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真羡慕啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了，他们谁去看比赛和我无关，\x01",
            "反正我是要留在这里干活的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FDC")

    label("loc_26DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_28F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_27A1")

    ChrTalk(
        0xFE,
        (
            "古代文明繁荣的时候，\x01",
            "还存在着人类以外的\x01",
            "拥有高度智慧的生物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其中的代表就是\x01",
            "一种被称为『古代龙』的龙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28ED")

    label("loc_27A1")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "古代文明繁荣的时候，\x01",
            "还存在着人类以外的\x01",
            "拥有高度智慧的生物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其中的代表就是\x01",
            "一种被称为『古代龙』的龙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "幸存下来的少数古代龙\x01",
            "数十年前还在柏斯附近的地方生活，\x01",
            "但最近以来再也没有人见到过了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28ED")

    Jump("loc_2FDC")

    label("loc_28F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2A5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2991")

    ChrTalk(
        0xFE,
        (
            "这里所展示的文物是\x01",
            "以前沉在瓦雷利亚湖底的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "搞不好，\x01",
            "瓦雷利亚湖底\x01",
            "也沉睡着巨大的遗迹呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A57")

    label("loc_2991")

    OP_A2(0x1)
    SetChrName("≡１Ｆ东展示室")

    ChrTalk(
        0xFE,
        (
            "这里所展示的文物是\x01",
            "以前沉在瓦雷利亚湖底的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一次偶然的机会\x01",
            "被渔夫给捞上来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "搞不好，\x01",
            "瓦雷利亚湖底\x01",
            "也沉睡着巨大的遗迹呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A57")

    Jump("loc_2FDC")

    label("loc_2A5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2C25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2B36")

    ChrTalk(
        0xFE,
        (
            "大崩坏之后，残存下来的人们\x01",
            "有着一段非常悲惨的历史。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现今人们的生活\x01",
            "已经安定下来了，\x01",
            "但这都是导力革命之后的事了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C22")

    label("loc_2B36")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "大崩坏之后，残存下来的人们\x01",
            "有着一段非常悲惨的历史。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "接二连三的战乱、贫困、流行病……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现今人们的生活\x01",
            "已经安定下来了，\x01",
            "但这都是导力革命之后的事了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C22")

    Jump("loc_2FDC")

    label("loc_2C25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2CCA")

    ChrTalk(
        0xFE,
        (
            "大崩坏之前的\x01",
            "相关资料基本上\x01",
            "都没有保存下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过说实话，\x01",
            "那时的文明发达的程度\x01",
            "似乎比现在还高。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FDC")

    label("loc_2CCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2EC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2D93")

    ChrTalk(
        0xFE,
        (
            "今天本应是把市民聚集起来\x01",
            "开展研讨会的日子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过在每年的武术大会\x01",
            "和诞辰庆典期间都要休会的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC5")

    label("loc_2D93")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "今天本应是把市民聚集起来\x01",
            "开展研讨会的日子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过在每年的武术大会\x01",
            "和诞辰庆典期间都要休会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你问为什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这是因为无法聚集\x01",
            "足够的人来参加研讨会。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC5")

    Jump("loc_2FDC")

    label("loc_2EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2FDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2F12")

    ChrTalk(
        0xFE,
        (
            "资料馆并非\x01",
            "只是展示资料而已。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FDC")

    label("loc_2F12")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "资料馆并非\x01",
            "只是展示资料而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "像这样对收集来的资料\x01",
            "进行整理分类保管\x01",
            "也是资料馆的任务之一。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有时还要接待\x01",
            "像亚鲁瓦教授这样\x01",
            "来讨论研究的学术派客人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FDC")

    TalkEnd(0xFE)
    Return()

    # Function_6_2285 end

    def Function_7_2FE0(): pass

    label("Function_7_2FE0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3094")

    ChrTalk(
        0xFE,
        (
            "我到柏斯出差的时候，\x01",
            "定期船停航给我带来很大麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "外出期间虽然发生了许多事情，\x01",
            "但资料馆完好无损，这就很好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AD3")

    label("loc_3094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_309E")
    Jump("loc_3AD3")

    label("loc_309E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_30A8")
    Jump("loc_3AD3")

    label("loc_30A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_30B2")
    Jump("loc_3AD3")

    label("loc_30B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3301")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3196")

    ChrTalk(
        0xFE,
        (
            "今天我需要去和一个\x01",
            "研究柏斯古代生物的学者见面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "过了中午我就要去搭乘定期船，\x01",
            "所以没办法去观看今天的决赛了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32FE")

    label("loc_3196")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "其实我非常想去竞技场\x01",
            "看武术大会的总决赛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过今天我需要去和一个\x01",
            "研究柏斯古代生物的学者见面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "过了中午我就要去搭乘定期船，\x01",
            "所以没办法去观看比赛了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "遗憾也没有办法，\x01",
            "唯有将门票让给亚鲁瓦教授了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32FE")

    Jump("loc_3AD3")

    label("loc_3301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_33AD")

    ChrTalk(
        0xFE,
        (
            "明天武术大会的决赛\x01",
            "我也打算去看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "实际上我连票都已经买好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AD3")

    label("loc_33AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3585")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3471")

    ChrTalk(
        0xFE,
        (
            "作为学术调查的对象，\x01",
            "我很想将古代遗物\x01",
            "也收入本资料馆里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但就算向负责管理的\x01",
            "七耀教会提出申请，\x01",
            "他们也不会同意吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3582")

    label("loc_3471")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "据说古代遗物\x01",
            "也和塞姆里亚文明\x01",
            "有着很深的联系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "作为学术调查的对象，\x01",
            "我很想将古代遗物\x01",
            "也收入本资料馆里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但就算向负责管理的\x01",
            "七耀教会提出申请，\x01",
            "他们也不会同意吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3582")

    Jump("loc_3AD3")

    label("loc_3585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_36D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_361F")

    ChrTalk(
        0xFE,
        (
            "亚鲁瓦教授\x01",
            "对我们这儿的未公开资料\x01",
            "也一并进行了调查研究。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说不定还会有\x01",
            "新的历史性发现呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36CD")

    label("loc_361F")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "亚鲁瓦教授是个很沉稳的人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他对我们这儿的未公开资料\x01",
            "也一并进行了调查研究。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说不定还会有\x01",
            "新的历史性发现呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36CD")

    Jump("loc_3AD3")

    label("loc_36D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3997")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_37CE")

    ChrTalk(
        0xFE,
        (
            "虽然主张『七至宝』只是\x01",
            "单纯的传说的学者也不少……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但各地残留下的遗迹是\x01",
            "塞姆里亚文明遗物的推测，\x01",
            "还是有几分可能性的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3994")

    label("loc_37CE")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "上天赐予古代人的\x01",
            "蕴藏着力量的『七至宝』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "至今为止，\x01",
            "还是没有发现能说明\x01",
            "其为何物的相关文献。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然也有不少学者\x01",
            "主张那只是传说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但各地残留下的遗迹是\x01",
            "塞姆里亚文明遗物的推测，\x01",
            "还是有几分可能性的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3994")

    Jump("loc_3AD3")

    label("loc_3997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3A71")

    ChrTalk(
        0xFE,
        (
            "唔～亚鲁瓦教授的研究\x01",
            "和我的兴趣不谋而合。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "七至宝之一的『辉之环』\x01",
            "长眠于利贝尔某处的传说，\x01",
            "实在含义颇深啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AD3")

    label("loc_3A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3AD3")

    ChrTalk(
        0xFE,
        "您客气了，亚鲁瓦教授。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我刚才就想着\x01",
            "你是不是快要到了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AD3")

    TalkEnd(0xFE)
    Return()

    # Function_7_2FE0 end

    def Function_8_3AD7(): pass

    label("Function_8_3AD7")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【『四轮之塔』的外壁】\x01",
            "　　　　　　　　　　　年代：七耀历以前？\x01",
            "　　这块朴素的石壁，是从『大崩坏』后所建\x01",
            "的『四轮之塔』上作为研究资料切割出来的。\x01",
            "其上所绘制的纹样是同时代建筑物中的典型，\x01",
            "据说描述的是持杖的祭司，以及展翅的神祗的\x01",
            "身姿。关于其与七耀教会成立之后的代表神格\x01",
            "『空之女神』的关系，各方面的研究仍在进行\x01",
            "中。\x01",
            "　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_3AD7 end

    def Function_9_3C78(): pass

    label("Function_9_3C78")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【七耀历１１５０～１２００年\x01",
            "　　　　　　　～导力革命以后的世界～】\x01",
            "　　Ｃ·爱普斯泰恩博士发明导力器后仅仅五\x01",
            "十年。世界以惊人的速度进步着，接连不断地\x01",
            "开拓岀导力技术新的应用领域。堪称其象征的\x01",
            "就是飞艇。\x01",
            "　　\x01",
            "　　利贝尔王国定期飞艇的运航已经成为国民\x01",
            "们习以为常的交通方式，近年来埃雷波尼亚帝\x01",
            "国等其他国家也开始正式引进飞艇制造业，使\x01",
            "得飞艇级的船体逐步实用化。\x01",
            "　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_9_3C78 end

    def Function_10_3E20(): pass

    label("Function_10_3E20")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【七耀历以前\x01",
            "　　　　　～古代塞姆里亚文明～】\x01",
            "　　距今约１２００年前，当时繁荣绝顶的塞\x01",
            "姆里亚文明突然迎来了终结，失去了文明的人\x01",
            "们开始度过漫长的暗黑时代。\x01",
            "　　\x01",
            "　　第一层的展示物据考证是『大崩坏』之后\x01",
            "所制造的遗物。虽然据判断并非古代文明的直\x01",
            "接遗物，但因受到其深刻影响，学术方面的价\x01",
            "值极高。\x01",
            "　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_3E20 end

    def Function_11_3FCD(): pass

    label("Function_11_3FCD")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【古代的照明器具】\x01",
            "　　　　　　　　　　　年代：七耀历以前？\x01",
            "　　专用于焚烧篝火的容器。在塔之类被认为\x01",
            "与祭祀仪式有关联的建筑物中频繁被使用，其\x01",
            "具体用途不仅仅是照明，在宗教上可能也拥有\x01",
            "某种程度的意义。当然这点目前还只是推测罢\x01",
            "了。  \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_3FCD end

    def Function_12_40BC(): pass

    label("Function_12_40BC")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【浮雕石柱】\x01",
            "　　　　　　　　　　　年代：七耀历以前？\x01",
            "　　刻有优美雕刻的石柱。在瓦雷利亚湖的湖\x01",
            "底被打捞上来，可以看出与『四轮之塔』的壁\x01",
            "画类似的纹样在其上也被反复使用。\x01",
            "　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_12_40BC end

    def Function_13_41A9(): pass

    label("Function_13_41A9")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【瓷工艺的地板】\x01",
            "　　　　　　　　　　　年代：七耀历以前？\x01",
            "　　遗迹内部彩色镶嵌的瓷工艺地板。将破碎\x01",
            "的天然石块巧妙拼接，作出朴素而美妙的花纹\x01",
            "样式。\x01",
            "　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_41A9 end

    def Function_14_4299(): pass

    label("Function_14_4299")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【七耀历１～５００年左右\x01",
            "　　　　　　　　～暗黑时代的到来～】\x01",
            "　　由于『大崩坏』而导致文明尽失，世界陷\x01",
            "入了长期的混乱时代。\x01",
            "　　大小各异的国家、势力使得无尽的战争持\x01",
            "续了约５００年间，后世称此时代为『暗黑时\x01",
            "代』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_4299 end

    def Function_15_4378(): pass

    label("Function_15_4378")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【骑士们的武具】\x01",
            "　　　　　　　　年代：七耀历５００年左右\x01",
            "　　日夜征战的时代中，战士们的集团拥有社\x01",
            "会性的强大影响力，最终成长为特权的骑士阶\x01",
            "级。\x01",
            "　　他们佩戴着如展品所示的武具投身沙场，\x01",
            "获得战利品和领土，势力不断扩大。\x01",
            " \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_4378 end

    def Function_16_4458(): pass

    label("Function_16_4458")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【七耀历５００～１１００年左右\x01",
            "　　　　　　～七耀教会带来的安定期～】\x01",
            "　　七耀教会登上历史舞台，正值暗黑时代末\x01",
            "期，七耀历５００年左右。\x01",
            "　　以『空之女神』为中心所整理的教义，通\x01",
            "过教会救济民众的社会活动，瞬间深入人心。\x01",
            "　　它的权威很快成长到连贵族、骑士阶级也\x01",
            "无法忽视的地步，其后以教会为中心的新秩序\x01",
            "便逐步形成了。\x01",
            " \x02",
        )
    )

    CloseMessageWindow()

    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_4458 end

    def Function_17_45F1(): pass

    label("Function_17_45F1")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【古代文明的遗物——\x01",
            "　　　　　　　　『古代遗产』】\x01",
            "　　　　　　　　　　　　　　　年代：不明\x01",
            "　　『古代遗产』是从各地发现的古代遗迹中\x01",
            "出土的诸如器物、杖等形态各异、不可思议的\x01",
            "遗物。\x01",
            "　　在七耀教会的教义中，作为与女神赐予的\x01",
            "『七至宝』相关的物品，其回收成为教会必须\x01",
            "履行的义务之一。展品的『古代遗产』也是教\x01",
            "会所回收的物品。\x01",
            "　　许多传闻称其拥有超常的力量，但此展品\x01",
            "已经失去能力，无法启动。\x01",
            "　　\x02",
        )
    )

    CloseMessageWindow()

    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_45F1 end

    def Function_18_477F(): pass

    label("Function_18_477F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【七耀教会的祭具】\x01",
            "　　　　　　　　年代：七耀历９００年左右\x01",
            "　　七耀教会创造岀种种的宗教艺术，由此开\x01",
            "始教会开拓出一个稳定的时代。据考证，『空\x01",
            "之女神』的圣像也是由此时起被塑造为现今的\x01",
            "姿态。此外，现在所使用的祭祀道具多数也是\x01",
            "在这个时代被定型的。\x01",
            "　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_477F end

    def Function_19_48B0(): pass

    label("Function_19_48B0")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【七耀教会圣典的抄本】\x01",
            "　　　　　　　　年代：七耀历５００年左右\x01",
            "　　暗黑时代末期的原始七耀教会所使用的圣\x01",
            "典抄本。中世纪没有印刷技术，因此这本书是\x01",
            "由人手工抄写在兽皮制的纸张上的。\x01",
            "　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_48B0 end

    def Function_20_4977(): pass

    label("Function_20_4977")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【中世纪的纺纱机】\x01",
            "　　　　　　　　年代：七耀历９００年左右\x01",
            "　　纺纱用的手工机械。到了稳定的中世纪，\x01",
            "农民的生活逐渐富裕，作为商品作物的棉花栽\x01",
            "培日渐繁盛。为了收入货币，这个时代的手工\x01",
            "业也开始发展。\x01",
            "　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_20_4977 end

    SaveToFile()

Try(main)
