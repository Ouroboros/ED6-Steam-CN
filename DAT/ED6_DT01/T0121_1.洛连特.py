from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T0121_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        "Function_1_196",          # 01, 1
        "Function_2_2ED",          # 02, 2
    )


    def Function_0_66(): pass

    label("Function_0_66")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "真是的，开什么玩笑。\x01",
            "什么商品都缺货！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可恶，在下次谈判之前\x01",
            "必须发掘些超热门产品才行啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_192")

    label("loc_12D")


    ChrTalk(
        0xFE,
        (
            "在下次谈判之前\x01",
            "必须发掘些超热门产品才行啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_192")

    TalkEnd(0xE)
    Return()

    # Function_0_66 end

    def Function_1_196(): pass

    label("Function_1_196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1B5")
    OP_2A(0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xB, 0xC, 0xD, 0xFFFF)
    Jump("loc_2E9")

    label("loc_1B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1D2")
    OP_2A(0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xB, 0xC, 0xFFFF)
    Jump("loc_2E9")

    label("loc_1D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_1EF")
    OP_2A(0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xB, 0xC, 0xFFFF)
    Jump("loc_2E9")

    label("loc_1EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_20C")
    OP_2A(0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xB, 0xC, 0xFFFF)
    Jump("loc_2E9")

    label("loc_20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 2)), scpexpr(EXPR_END)), "loc_225")
    OP_2A(0x4, 0x5, 0x6, 0x7, 0x8, 0xB, 0xFFFF)
    Jump("loc_2E9")

    label("loc_225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_23E")
    OP_2A(0x4, 0x5, 0x6, 0x7, 0x8, 0xB, 0xFFFF)
    Jump("loc_2E9")

    label("loc_23E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_24F")
    OP_2A(0x4, 0xB, 0xFFFF)
    Jump("loc_2E9")

    label("loc_24F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_2A1")
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "现在没有什么特别的委托。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_2E9")

    label("loc_2A1")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "现在没有什么特别的委托。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2E9")

    TalkEnd(0xFF)
    Return()

    # Function_1_196 end

    def Function_2_2ED(): pass

    label("Function_2_2ED")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_87D")
    Sleep(100)
    OP_AF(0x4, 0xA)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    EventBegin(0x0)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#741F辛苦了。\x01",
            "看来你们很顺利地完成了任务呢。\x02\x03",
            "#741F有时工作中的具体表现\x01",
            "也会影响到最后所得的报酬，\x01",
            "这点你们俩一定要注意哦。 \x02\x03",
            "#740F报告之后，不仅会得到米拉，\x01",
            "而且会为自己加算一种叫做ＢＰ的点数。\x02\x03",
            "ＢＰ是游击士点数的缩写，\x01",
            "是用来衡量游击士实绩的数据。\x02\x03",
            "这个点数达到一定值数的话，\x01",
            "你们的游击士等级就能提升，\x01",
            "同时也会得到协会奖励的特别物品。\x02\x03",
            "准游击士一共分为９个等级，\x01",
            "９级是初始等级，１级是最高等级。\x01",
            "为了达到１级，你们俩要好好加油哦！\x02\x03",
            "#740F工作中实际获得的米拉和ＢＰ\x01",
            "在游击士手册中都有记录，\x01",
            "完成任务之后可以确认一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#020F这样的话，\x01",
            "剩下的就是例行的仪式了。\x02\x03",
            "你们两个，\x01",
            "先跟我回到二楼再说吧。\x02\x03",
            "回头见，爱娜。\x01",
            "这么忙还要麻烦你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#741F呵呵，没关系。\x01",
            "这是为了培养新生的战斗力嘛。\x02\x03",
            "以后还要靠他们\x01",
            "上刀山、下火海呢，呵呵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F上、上刀山……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F……还是先做好心里准备吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Call(0, 23)
    Jump("loc_9AA")

    label("loc_87D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x4)"), scpexpr(EXPR_END)), "loc_923")
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#740F辛苦了。\x01",
            "看来你们很顺利地完成了任务呢。\x02\x03",
            "如果完成其他任务的话，\x01",
            "别忘记回协会报告一下哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AA")

    label("loc_923")

    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#740F哎呀，\x01",
            "现在好像没有需要报告的工作任务呢。\x02\x03",
            "如果完成其他任务的话，\x01",
            "别忘记回协会报告一下哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AA")

    Return()

    # Function_2_2ED end

    SaveToFile()

Try(main)
