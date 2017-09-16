from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T2120_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2120.x',
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
    )

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_107",          # 01, 1
        "Function_2_3B9",          # 02, 2
        "Function_3_120C",         # 03, 3
        "Function_4_1502",         # 04, 4
    )


    def Function_0_66(): pass

    label("Function_0_66")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_8A")
    OP_2A(0x24, 0x21, 0x22, 0x26, 0x1D, 0x1E, 0x1F, 0x20, 0x23, 0x25, 0xFFFF)
    Jump("loc_103")

    label("loc_8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_AB")
    OP_2A(0x24, 0x21, 0x22, 0x26, 0x1D, 0x1E, 0x1F, 0x20, 0x23, 0x25, 0xFFFF)
    Jump("loc_103")

    label("loc_AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_CA")
    OP_2A(0x24, 0x21, 0x22, 0x26, 0x1D, 0x1E, 0x1F, 0x20, 0x23, 0xFFFF)
    Jump("loc_103")

    label("loc_CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_E9")
    OP_2A(0x24, 0x21, 0x22, 0x26, 0x1D, 0x1E, 0x1F, 0x20, 0x23, 0xFFFF)
    Jump("loc_103")

    label("loc_E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_FE")
    OP_2A(0x24, 0x21, 0x22, 0x26, 0xFFFF)
    Jump("loc_103")

    label("loc_FE")

    OP_2A(0x24, 0xFFFF)

    label("loc_103")

    TalkEnd(0xFF)
    Return()

    # Function_0_66 end

    def Function_1_107(): pass

    label("Function_1_107")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_233")
    OP_A2(0xB)
    OP_28(0x1D, 0x1, 0x8000)

    ChrTalk(
        0xB,
        (
            "哦，\x01",
            "看样子进行得很顺利嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是的，\x01",
            "已经安全地送到弗科特老人手里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F老爷爷他也十分精神健康呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(
        0xB,
        (
            "哦，是吗。\x01",
            "那就太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "再见了。\x01",
            "以后有什么事情还得拜托你们哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F彼此彼此，请多多关照。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，再见。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B5")

    label("loc_233")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26D")

    ChrTalk(
        0xB,
        "哦，有什么事吗？\x02",
    )

    CloseMessageWindow()
    Call(1, 3)
    Jump("loc_3B5")

    label("loc_26D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_2EF")

    ChrTalk(
        0xB,
        "哦，办完事情了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "运送维修工具箱的工作\x01",
            "可以开始了吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 2)
    Jump("loc_3B5")

    label("loc_2EF")


    ChrTalk(
        0x101,
        (
            "#000F请问您是索姆茨先生吗？\x02\x03",
            "我们是游击士协会派来的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(
        0xB,
        (
            "哦，是运送维修工具箱的事吧。\x01",
            "我正在等你们呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "如何，\x01",
            "可以现在就去吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 2)

    label("loc_3B5")

    TalkEnd(0xB)
    Return()

    # Function_1_107 end

    def Function_2_3B9(): pass

    label("Function_2_3B9")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_415"),
        (1, "loc_111D"),
        (SWITCH_DEFAULT, "loc_1208"),
    )


    label("loc_415")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_5BB")
    OP_28(0x1D, 0x4, 0x8)

    ChrTalk(
        0xB,
        (
            "太好了，\x01",
            "那么我就把这个庞然大物交给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "维修工具箱\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x326, 1)

    ChrTalk(
        0xB,
        (
            "把这个箱子\x01",
            "亲手交给巴伦诺灯塔的\x01",
            "弗科特老人就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "因为都是些比较昂贵的物品，\x01",
            "所以一定要小心才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "巴伦诺灯塔\x01",
            "位于玛诺利亚村西面、\x01",
            "三叉路口南面的海角上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "……就是这样的。\x01",
            "那么就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Jump("loc_111A")

    label("loc_5BB")

    OP_28(0x1D, 0x4, 0x4)
    OP_28(0x1D, 0x4, 0x8)
    OP_28(0x1D, 0x1, 0x1)
    OP_28(0x1D, 0x1, 0x2)

    ChrTalk(
        0xB,
        (
            "太好了，\x01",
            "那么我就把这个庞然大物交给你们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F庞、庞然大物？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 400)

    ChrTalk(
        0xB,
        "有点重，小心点哟。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "维修工具箱\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x326, 1)

    ChrTalk(
        0xB,
        "你们能行吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "交换用的导力器部件\x01",
            "和套装工具等东西\x01",
            "全部都装在里面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F运送到巴伦诺灯塔就可以了吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(
        0xB,
        (
            "啊，是的，\x01",
            "一定要亲手交给看守灯塔的\x01",
            "弗科特老人哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "因为都是些比较昂贵的物品，\x01",
            "所以一定要小心才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "……对了，\x01",
            "我听嘉恩那小子说了哦。\x01",
            "说实话，我还真没想到啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯？什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "当然是关于你们啊，\x01",
            "虽然听说你们身手敏捷、活蹦乱跳的，\x01",
            "但没有想到竟然如此年轻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F活、活蹦乱跳……\x01",
            "我又不是小兔子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "不过啊，\x01",
            "现在我反而对你们这么年轻感到担忧呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F唔……\x02\x03",
            "我说叔叔！\x01",
            "年轻是年轻，\x01",
            "但不见得年纪小就没能力吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(
        0xB,
        (
            "啊，不、不是！\x01",
            "我不是那个意思……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "……我是认为弗科特老人\x01",
            "可能会这么想。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_C67")

    ChrTalk(
        0x101,
        "#505F哦～原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "怎么了，\x01",
            "你们认识他老人家？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嗯，\x01",
            "的确是位比较难应付的老爷爷呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F唉，我们之前受过他的训导……\x01",
            "所以对他的事情也略知一二。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 400)

    ChrTalk(
        0xB,
        (
            "哈哈哈～\x01",
            "听你们这么说就没问题了，\x01",
            "看来你们明白我的意思了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D87")

    label("loc_C67")


    ChrTalk(
        0x101,
        "#000F弗科特老人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那位老人家怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "唔～\x01",
            "事实上弗科特老人他\x01",
            "是一个性格有点乖僻的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "他经常会针对年轻人\x01",
            "说一些过分挑剔的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F……总之就是一个怪人，对吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "……嗯，\x01",
            "这么说的确也毫不为过。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D87")

    TurnDirection(0xB, 0x0, 400)

    ChrTalk(
        0xB,
        (
            "不过，\x01",
            "你们也得理解他老人家的心情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "看守灯塔是一件很孤独的工作，\x01",
            "性格变得倔犟也是情有可原的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#040F对于航行中的船只而言，\x01",
            "灯塔就像安全带一样重要……\x02\x03",
            "看守灯塔的工作\x01",
            "是要肩负很重大的责任的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#003F这样啊……\x01",
            "的确是很费力的工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "在他老人家还是个渔夫的时候，\x01",
            "总是爱去『拉旺塔尔』喝酒哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "但是现在一直住在灯塔，\x01",
            "几乎就没什么机会再去喝\x01",
            "那里著名的鸡尾酒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "真是沉重的话题啊。\x01",
            "我好想把酒\x01",
            "也给他捎去呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "哦，\x01",
            "我一说起来就没完没了的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "就是因为我说的这些原因，\x01",
            "他老人家如果说了什么不中听的话，\x01",
            "你们可别往心里去哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(
        0x101,
        (
            "#000F嗯，明白了。\x02\x03",
            "那我们这就出发了，\x01",
            "您还有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(
        0xB,
        (
            "不，已经没了。\x01",
            "如果有疑问或者想取消任务的话，\x01",
            "就再到这里来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "那就拜托你们了。\x02",
    )

    CloseMessageWindow()

    label("loc_111A")

    Jump("loc_1208")

    label("loc_111D")

    OP_28(0x1D, 0x1, 0x4000)

    ChrTalk(
        0x101,
        (
            "#505F唔，\x01",
            "现在有些不太方便。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(
        0xB,
        (
            "这样啊。\x01",
            "那么等你们办完事情之后\x01",
            "再来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我这里的事情有些急，\x01",
            "如果可以的话，\x01",
            "还请你们尽快过来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1208")

    label("loc_1208")

    TalkEnd(0xB)
    Return()

    # Function_2_3B9 end

    def Function_3_120C(): pass

    label("Function_3_120C")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【再次确认委托内容】\x01",      # 0
            "【取消委托任务】\x01",          # 1
            "【没什么事】\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1292"),
        (1, "loc_1352"),
        (2, "loc_14DD"),
        (SWITCH_DEFAULT, "loc_14FE"),
    )


    label("loc_1292")


    ChrTalk(
        0xB,
        (
            "把给你们的维修工具箱\x01",
            "亲手交给巴伦诺灯塔的\x01",
            "弗科特老人就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "巴伦诺灯塔\x01",
            "位于玛诺利亚村西面、\x01",
            "三叉路口南面的海角上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "那么就拜托了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14FE")

    label("loc_1352")

    OP_28(0x1D, 0x3, 0x8)
    OP_28(0x1D, 0x1, 0x4000)

    ChrTalk(
        0x101,
        (
            "#007F抱歉，索姆茨先生。\x01",
            "我们突然有件很急的事要办……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(
        0xB,
        (
            "哦，我知道了。\x01",
            "这种事情是没办法的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "那就暂且先把\x01",
            "工具箱还给我吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了\x07\x02",
            "维修工具箱\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x326, 1)

    ChrTalk(
        0xB,
        (
            "我这里的事情有些急，\x01",
            "如果可以的话，\x01",
            "还请你们尽快过来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14FE")

    label("loc_14DD")


    ChrTalk(
        0xB,
        "那么就拜托了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14FE")

    label("loc_14FE")

    TalkEnd(0xB)
    Return()

    # Function_3_120C end

    def Function_4_1502(): pass

    label("Function_4_1502")

    OP_28(0x22, 0x4, 0x10)
    OP_28(0x22, 0x1, 0x4)
    OP_A2(0x1)
    OP_3F(0x67, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1858")

    ChrTalk(
        0x101,
        (
            "#501F那个试制的导力枪\x01",
            "是不是就是这个呢？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "试·零式导力枪\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(800)

    ChrTalk(
        0xFE,
        (
            "哎呀……！\x01",
            "怎、怎么会！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为、为什么，\x01",
            "你们从哪儿得到的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F从在『绀碧之塔』消灭的通缉魔兽那里得到的。\x01",
            "　\x02\x03",
            "很可能是由于\x01",
            "导力器里的七耀石吸引了它们。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "啊啊，女神啊！\x01",
            "由衷地感谢您！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼～～\x01",
            "找到了就好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F那么这样任务就算完成了吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对不起，\x01",
            "我们这就告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "不用那么急急忙忙的吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(
        0xFE,
        (
            "稍等一下，\x01",
            "请你们务必收下这个东西。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "攻击２\x07\x00",
            "的结晶回路。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0xFE,
        "这是我小小的心意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们在日后的工作中\x01",
            "也要好好加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#508F嗯，谢谢！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FF3")

    label("loc_1858")


    ChrTalk(
        0x101,
        (
            "#002F……啊，难道是……\x02\x03",
            "那个试制的导力枪\x01",
            "是不是就是这个呢？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "试·零式导力枪\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(800)

    ChrTalk(
        0xFE,
        (
            "哎呀……！\x01",
            "怎、怎么会！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为、为什么，\x01",
            "你们从哪儿得到的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F从在『绀碧之塔』消灭的通缉魔兽那里得到的。\x01",
            "　\x02\x03",
            "很可能是由于\x01",
            "导力器里的七耀石吸引了它们。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "啊啊，女神啊！\x01",
            "由衷地感谢您！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊啊啊啊，你们！\x01",
            "我已经激动地说不出话了！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "总、总之现在让我\x01",
            "紧紧拥抱你们亲上几口以表谢意……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#008F哇哇。\x02\x03",
            "我、我就免了吧！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1AB4")
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(
        0x105,
        "#045F我、我也……\x02",
    )

    CloseMessageWindow()

    label("loc_1AB4")


    ChrTalk(
        0x102,
        "#018F……我也是。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "呼呼～～～～\x01",
            "是、是吗……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#010F这个试制品有这么重要吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，当然了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管怎么说这可是\x01",
            "蔡斯中央工房研究中的试制品啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "离预定的上市日期\x01",
            "还有一段时间呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊～听你这么说，\x01",
            "它的性能应该相当不错吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "你对武器很有兴趣吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哦，你们是游击士，\x01",
            "关心这类商品也是理所当然的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，我就把这个结晶回路\x01",
            "送给你们作为谢礼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果你们能用得上它的话\x01",
            "就再好不过了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "攻击２\x07\x00",
            "的结晶回路。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#014F真过意不去，\x01",
            "还送我们这么好的东西……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "没什么没什么，\x01",
            "你们帮了我很大的忙嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正式的报酬我也会通过协会支付给你们的，\x01",
            "请放心吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F哎，\x01",
            "还要支付米拉吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "嗯，不要介意啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "反正都是记在\x01",
            "中央工房的金库的账上。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#509F不、不是，\x01",
            "我不是这个意思……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样不是也很好吗。\x01",
            "这种情况下\x01",
            "就不要推托了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之，\x01",
            "今天谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果再有什么事情的话，\x01",
            "还得麻烦你们哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FF3")

    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【搜寻试制品】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    OP_3E(0x25F, 1)
    OP_8C(0xFE, 0, 400)
    EventEnd(0x1)
    TalkEnd(0xC)
    Return()

    # Function_4_1502 end

    SaveToFile()

Try(main)
