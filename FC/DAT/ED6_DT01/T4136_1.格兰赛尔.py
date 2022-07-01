from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4136_1 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4136.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60018",
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
    )

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_67",           # 01, 1
        "Function_2_68",           # 02, 2
        "Function_3_134",          # 03, 3
        "Function_4_22F",          # 04, 4
        "Function_5_30A",          # 05, 5
        "Function_6_45B",          # 06, 6
        "Function_7_53B",          # 07, 7
        "Function_8_64A",          # 08, 8
        "Function_9_6D1",          # 09, 9
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Return()

    # Function_0_66 end

    def Function_1_67(): pass

    label("Function_1_67")

    Return()

    # Function_1_67 end

    def Function_2_68(): pass

    label("Function_2_68")

    TalkBegin(0xFE)
    OP_A2(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_F0")

    ChrTalk(
        0xFE,
        (
            "突击骑兵队被打败了吗。\x01",
            "游击士干得不错嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C")

    label("loc_F0")


    ChrTalk(
        0xFE,
        (
            "不管对手是谁，\x01",
            "我一定会全力战斗的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12C")

    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_2_68 end

    def Function_3_134(): pass

    label("Function_3_134")

    TalkBegin(0xFE)
    OP_A2(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1A3")

    ChrTalk(
        0xFE,
        (
            "今年游击士的小组\x01",
            "还剩下两组。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不管怎么样，互相加油吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_227")

    label("loc_1A3")


    ChrTalk(
        0xFE,
        "一会儿就轮到我们出场了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正好趁这个机会\x01",
            "检验一下平时训练的成果。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_227")

    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_3_134 end

    def Function_4_22F(): pass

    label("Function_4_22F")

    TalkBegin(0xFE)
    OP_A2(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_2CB")

    ChrTalk(
        0xFE,
        (
            "『渡鸦帮』那些家伙们\x01",
            "打得不错啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "游击士以外的平民小组\x01",
            "在正式比赛中出场还真是少见呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_302")

    label("loc_2CB")


    ChrTalk(
        0xFE,
        "还没轮到我们出场吗？\x02",
    )

    CloseMessageWindow()

    label("loc_302")

    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_4_22F end

    def Function_5_30A(): pass

    label("Function_5_30A")

    TalkBegin(0xFE)
    OP_A2(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_3C5")

    ChrTalk(
        0xFE,
        (
            "你们的战斗在王国军中\x01",
            "得到了很高的评价呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天也要仔细地\x01",
            "观摩你们的比赛啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_453")

    label("loc_3C5")


    ChrTalk(
        0xFE,
        (
            "摩尔根将军不能参赛，\x01",
            "我们一定要连他的那份一起加油啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_453")

    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_5_30A end

    def Function_6_45B(): pass

    label("Function_6_45B")

    TalkBegin(0xFE)
    OP_A2(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_4D8")

    ChrTalk(
        0xFE,
        (
            "唔，我们的对手\x01",
            "说不定是那些家伙……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_533")

    label("loc_4D8")


    ChrTalk(
        0xFE,
        "我们国境守卫队是精锐部队。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管对手是谁，\x01",
            "也绝对不能轻易地输掉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_533")

    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_6_45B end

    def Function_7_53B(): pass

    label("Function_7_53B")

    TalkBegin(0xFE)
    OP_A2(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_57B")

    ChrTalk(
        0xFE,
        (
            "接下来轮到你们了呢。\x01",
            "祝你们取得胜利。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_642")

    label("loc_57B")


    ChrTalk(
        0xFE,
        (
            "通过这次武术大会，\x01",
            "就能了解到其他的部队\x01",
            "和你们游击士的水平了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对我们来说\x01",
            "也有很好的促进作用。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_642")

    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_7_53B end

    def Function_8_64A(): pass

    label("Function_8_64A")

    TalkBegin(0xFE)
    OP_A2(0x7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_68E")

    ChrTalk(
        0xFE,
        (
            "身体状态非常不错，\x01",
            "今年应该能取得好成绩吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C9")

    label("loc_68E")


    ChrTalk(
        0xFE,
        (
            "请不要打扰。\x01",
            "我现在正在集中精神。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C9")

    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_8_64A end

    def Function_9_6D1(): pass

    label("Function_9_6D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_726")

    ChrTalk(
        0xFE,
        (
            "为了不留下遗憾，\x01",
            "一定要尽全力战斗到最后。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EE")

    label("loc_726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_77F")

    ChrTalk(
        0xFE,
        (
            "唔，虽然年轻，\x01",
            "但是看起来很厉害的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "今天一起奋战吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7EE")

    label("loc_77F")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "你们是游击士吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔，虽然年轻，\x01",
            "但是看起来很厉害的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "今天一起奋战吧。\x02",
    )

    CloseMessageWindow()

    label("loc_7EE")

    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_9_6D1 end

    SaveToFile()

Try(main)
