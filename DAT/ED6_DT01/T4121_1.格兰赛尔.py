from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4121_1 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4121.x',
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
    )

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_67",           # 01, 1
        "Function_2_68",           # 02, 2
        "Function_3_307",          # 03, 3
        "Function_4_A89",          # 04, 4
        "Function_5_DFE",          # 05, 5
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_75")
    Jump("loc_303")

    label("loc_75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_7F")
    Jump("loc_303")

    label("loc_7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 0)), scpexpr(EXPR_END)), "loc_113")

    ChrTalk(
        0xFE,
        (
            "#812F作战一旦开始，\x01",
            "就没有回旋余地了。\x02\x03",
            "所以趁现在\x01",
            "赶快整理好装备吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC")

    label("loc_113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 4)), scpexpr(EXPR_END)), "loc_1CC")

    ChrTalk(
        0xFE,
        (
            "#854F事态很严重啊，\x01",
            "刚才一时手足无措，\x01",
            "现在终于弄明白情况了。\x02\x03",
            "出了这么大的事，\x01",
            "的确让人紧张啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC")

    Jump("loc_303")

    label("loc_1CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1D9")
    Jump("loc_303")

    label("loc_1D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1E3")
    Jump("loc_303")

    label("loc_1E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1ED")
    Jump("loc_303")

    label("loc_1ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_239")

    ChrTalk(
        0xFE,
        (
            "#850F好～的，今天也一样，\x01",
            "工作、比赛都要努力！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_303")

    label("loc_239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_243")
    Jump("loc_303")

    label("loc_243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_24D")
    Jump("loc_303")

    label("loc_24D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_290")

    ChrTalk(
        0xFE,
        (
            "#850F哟，是两位新人啊，\x01",
            "找到金大哥了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F9")

    label("loc_290")


    ChrTalk(
        0xFE,
        (
            "#850F哟，是两位新人啊，\x01",
            "找到金大哥了吗？\x02\x03",
            "我很期待\x01",
            "和你们的对战哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F9")

    Jump("loc_303")

    label("loc_2FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_303")

    label("loc_303")

    TalkEnd(0xFE)
    Return()

    # Function_2_68 end

    def Function_3_307(): pass

    label("Function_3_307")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_314")
    Jump("loc_A85")

    label("loc_314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_31E")
    Jump("loc_A85")

    label("loc_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 0)), scpexpr(EXPR_END)), "loc_393")

    ChrTalk(
        0xFE,
        (
            "#830F突入的任务就拜托你们了。\x02\x03",
            "没问题，\x01",
            "你们一定能办到的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FA")

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 3)), scpexpr(EXPR_END)), "loc_3FA")

    ChrTalk(
        0xFE,
        (
            "#832F这么大的一宗委托\x01",
            "我也是第一次碰到呢。\x02\x03",
            "这次只许成功不许失败，\x01",
            "必须制定严密的作战计划才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FA")

    Jump("loc_A85")

    label("loc_3FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_542")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_49C")

    ChrTalk(
        0xFE,
        (
            "#831F真是很值得一看的比赛呢，\x01",
            "对我们也很有参考价值。\x02\x03",
            "真想什么时候有机会\x01",
            "和你们一起执行任务呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53F")

    label("loc_49C")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "#831F呀，恭喜你们获胜。\x02\x03",
            "真是很值得一看的比赛呢，\x01",
            "对我们也很有参考价值。\x02\x03",
            "真想什么时候有机会\x01",
            "和你们一起执行任务呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53F")

    Jump("loc_A85")

    label("loc_542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_54C")
    Jump("loc_A85")

    label("loc_54C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_658")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5BF")

    ChrTalk(
        0xFE,
        (
            "#830F你们明天要参加决赛吧。\x02\x03",
            "作为游击士协会的代表，\x01",
            "不要给协会蒙羞哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_655")

    label("loc_5BF")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "#830F你们明天要参加决赛吧。\x02\x03",
            "作为游击士协会的代表，\x01",
            "不要给协会蒙羞哦。\x02\x03",
            "#835F不过，其实这些话\x01",
            "也用不着对现在的你们说了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_655")

    Jump("loc_A85")

    label("loc_658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_692")

    ChrTalk(
        0xFE,
        (
            "#831F那么……\x02\x03",
            "今天也要\x01",
            "鼓足干劲啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A85")

    label("loc_692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_701")

    ChrTalk(
        0xFE,
        (
            "#830F艾丝蒂尔、约修亚，\x01",
            "我从现在开始就期待着\x01",
            "能和你们交手哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E4")

    label("loc_701")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "#831F呀，是你们啊。\x01",
            "恭喜你们首战告捷。\x02\x03",
            "哈哈，\x01",
            "你们没有想到会和\x01",
            "渡鸦帮那群家伙交手吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F是、是啊……\x01",
            "吃了一惊呢。\x02\x03",
            "#006F不过自从那次之后，\x01",
            "他们已经有很大的变化了呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F是啊，他们如果能改过自身，\x01",
            "说不定会成为像阿加特前辈那样的游击士了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F哼……\x01",
            "那样的家伙有一个都已经嫌多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#833F呵呵，\x01",
            "虽然他们也很努力，\x01",
            "但说实话让我吃惊的是你们呢。\x02\x03",
            "#830F虽说通过卢安支部\x01",
            "听说了你们的活跃表现，\x01",
            "但实力的成长已经超出了我的想象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F是、是吗……\x02\x03",
            "让卡露娜姐姐这样一称赞，\x01",
            "我都有些不好意思了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#831F哈哈，\x01",
            "我非常期待和你们交手哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，我也是！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F到时候还请多多关照。\x02",
    )

    CloseMessageWindow()

    label("loc_9E4")

    Jump("loc_A85")

    label("loc_9E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_A74")

    ChrTalk(
        0xFE,
        "那么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "比赛之前就去找些\x01",
            "通缉魔兽热一热身吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A85")

    label("loc_A74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_A7E")
    Jump("loc_A85")

    label("loc_A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_A85")

    label("loc_A85")

    TalkEnd(0xFE)
    Return()

    # Function_3_307 end

    def Function_4_A89(): pass

    label("Function_4_A89")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_A96")
    Jump("loc_DFA")

    label("loc_A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_AA0")
    Jump("loc_DFA")

    label("loc_AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_BB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 0)), scpexpr(EXPR_END)), "loc_B25")

    ChrTalk(
        0xFE,
        (
            "#824F情报部竟然也采取\x01",
            "扣押人质这种低级的手段……\x02\x03",
            "#822F一定要将\x01",
            "公主殿下他们救出来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB1")

    label("loc_B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_END)), "loc_BB1")

    ChrTalk(
        0xFE,
        (
            "#822F那位理查德上校\x01",
            "竟然是政变的策划人……\x02\x03",
            "没想到，\x01",
            "我们一直被蒙在鼓里啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB1")

    Jump("loc_DFA")

    label("loc_BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_BBE")
    Jump("loc_DFA")

    label("loc_BBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_BC8")
    Jump("loc_DFA")

    label("loc_BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_CA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_C35")

    ChrTalk(
        0xFE,
        (
            "#820F今天我们虽然输了，\x01",
            "但比赛本身一点也不让我后悔。\x02\x03",
            "你们决赛可要加油啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA5")

    label("loc_C35")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "#820F哦，是你们啊！\x02\x03",
            "今天我们虽然输了，\x01",
            "但比赛本身一点也不让我后悔。\x02\x03",
            "你们决赛可要加油啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA5")

    Jump("loc_DFA")

    label("loc_CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_CB2")
    Jump("loc_DFA")

    label("loc_CB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_DDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_D40")

    ChrTalk(
        0xFE,
        (
            "#821F连你们在内，\x01",
            "明天全都是劲敌啊。\x02\x03",
            "我已经跃跃欲试了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDC")

    label("loc_D40")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "#821F哟，今天辛苦了。\x02\x03",
            "连你们在内，\x01",
            "明天不管遇到那一组，都是强敌呢。\x02\x03",
            "我已经跃跃欲试了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDC")

    Jump("loc_DFA")

    label("loc_DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_DE9")
    Jump("loc_DFA")

    label("loc_DE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_DF3")
    Jump("loc_DFA")

    label("loc_DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_DFA")

    label("loc_DFA")

    TalkEnd(0xFE)
    Return()

    # Function_4_A89 end

    def Function_5_DFE(): pass

    label("Function_5_DFE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_E0B")
    Jump("loc_10C5")

    label("loc_E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_E15")
    Jump("loc_10C5")

    label("loc_E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_F18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 0)), scpexpr(EXPR_END)), "loc_E7B")

    ChrTalk(
        0xFE,
        (
            "#840F这次作战是我们\x01",
            "孤注一掷的选择。\x02\x03",
            "所以一定要成功。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F15")

    label("loc_E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 5)), scpexpr(EXPR_END)), "loc_F15")

    ChrTalk(
        0xFE,
        (
            "#845F不好意思，\x01",
            "刚才让你们见笑了。\x02\x03",
            "虽说有点在意自己的记忆，\x01",
            "但现在必须集中精力完成女王陛下的委托。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F15")

    Jump("loc_10C5")

    label("loc_F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1082")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_FB8")

    ChrTalk(
        0xFE,
        (
            "#840F你们这样年轻的游击士\x01",
            "能获得武术大会的优胜，\x01",
            "对我们来说更是种激励。\x02\x03",
            "我也要更加\x01",
            "努力修炼才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_107F")

    label("loc_FB8")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "#840F呀，恭喜你们获胜。\x01",
            "那场比赛真是非常精彩刺激哦。\x02\x03",

            "你们这样年轻的游击士\x01",
            "能获得武术大会的优胜，\x01",
            "对我们来说更是种激励。\x02\x03",

            "你们这样年轻的游击士\x01",
            "能获得武术大会的优胜，\x01",
            "对我们来说更是种激励。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_107F")

    Jump("loc_10C5")

    label("loc_1082")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_108C")
    Jump("loc_10C5")

    label("loc_108C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1096")
    Jump("loc_10C5")

    label("loc_1096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_10A0")
    Jump("loc_10C5")

    label("loc_10A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_10AA")
    Jump("loc_10C5")

    label("loc_10AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_10B4")
    Jump("loc_10C5")

    label("loc_10B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_10BE")
    Jump("loc_10C5")

    label("loc_10BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_10C5")

    label("loc_10C5")

    TalkEnd(0xFE)
    Return()

    # Function_5_DFE end

    SaveToFile()

Try(main)
