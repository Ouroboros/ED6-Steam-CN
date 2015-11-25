from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T1130_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T1130.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
    )


    def Function_0_66(): pass

    label("Function_0_66")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_A2(0x1)
    OP_28(0xD, 0x4, 0x10)
    OP_3F(0x329, 1)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE6DC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_44D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A5")
    Fade(1000)
    SetChrPos(0x101, 60600, 1000, 52500, 270)
    SetChrPos(0x102, 60600, 1000, 51300, 315)
    SetChrPos(0x103, 61600, 1000, 51500, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE")
    SetChrPos(0x104, 61600, 1000, 50200, 315)
    Jump("loc_10D")

    label("loc_EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x33)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10D")
    SetChrPos(0x134, 61600, 1000, 50200, 315)

    label("loc_10D")

    TurnDirection(0x101, 0x8, 0)
    OP_69(0x101, 0x7D0)

    ChrTalk(
        0x101,
        "#000F那个～可以打扰一下吗？\x02",
    )

    CloseMessageWindow()
    TalkBegin(0x8)

    ChrTalk(
        0x8,
        "嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F您是豪尔斯教区长吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "呵～呵～呵。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我就是豪尔斯没错啊……\x01",
            "找我有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44A")

    label("loc_1A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28D")
    Fade(1000)
    SetChrPos(0x102, 60600, 1000, 52500, 270)
    SetChrPos(0x101, 60600, 1000, 51300, 315)
    SetChrPos(0x103, 61600, 1000, 51500, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20B")
    SetChrPos(0x104, 61600, 1000, 50200, 315)
    Jump("loc_22A")

    label("loc_20B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x33)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22A")
    SetChrPos(0x134, 61600, 1000, 50200, 315)

    label("loc_22A")

    TurnDirection(0x102, 0x8, 0)
    OP_69(0x102, 0x7D0)

    ChrTalk(
        0x102,
        (
            "#010F教区长，\x01",
            "可以打扰您一下吗？\x02",
        )
    )

    CloseMessageWindow()
    TalkBegin(0x8)

    ChrTalk(
        0x8,
        "嗯？\x02",
    )

    CloseMessageWindow()
    Jump("loc_44A")

    label("loc_28D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36A")
    Fade(1000)
    SetChrPos(0x103, 60600, 1000, 52500, 270)
    SetChrPos(0x101, 60600, 1000, 51300, 315)
    SetChrPos(0x102, 61600, 1000, 51500, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F3")
    SetChrPos(0x104, 61600, 1000, 50200, 315)
    Jump("loc_312")

    label("loc_2F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x33)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_312")
    SetChrPos(0x134, 61600, 1000, 50200, 315)

    label("loc_312")

    TurnDirection(0x103, 0x8, 0)
    OP_69(0x103, 0x7D0)

    ChrTalk(
        0x103,
        (
            "#020F教区长，\x01",
            "可以打扰您一下吗？\x02",
        )
    )

    CloseMessageWindow()
    TalkBegin(0x8)

    ChrTalk(
        0x8,
        "嗯？\x02",
    )

    CloseMessageWindow()
    Jump("loc_44A")

    label("loc_36A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44A")
    Fade(1000)
    SetChrPos(0x104, 60600, 1000, 52500, 270)
    SetChrPos(0x101, 60600, 1000, 51300, 315)
    SetChrPos(0x103, 61600, 1000, 50200, 315)
    SetChrPos(0x102, 61600, 1000, 51500, 270)
    TurnDirection(0x104, 0x8, 0)
    OP_69(0x104, 0x7D0)

    ChrTalk(
        0x104,
        (
            "#030F哟，亲爱的教区长您好啊。\x02\x03",
            "不好意思，\x01",
            "不知道能不能和你聊几句呢。 \x02",
        )
    )

    CloseMessageWindow()
    TalkBegin(0x8)

    ChrTalk(
        0x8,
        "嗯？\x02",
    )

    CloseMessageWindow()

    label("loc_44A")

    Jump("loc_80F")

    label("loc_44D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56A")
    Fade(1000)
    SetChrPos(0x101, 57400, 1000, 52500, 90)
    SetChrPos(0x102, 57400, 1000, 51300, 45)
    SetChrPos(0x103, 56400, 1000, 51500, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B3")
    SetChrPos(0x104, 56400, 1000, 50200, 45)
    Jump("loc_4D2")

    label("loc_4B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x33)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D2")
    SetChrPos(0x134, 56400, 1000, 50200, 45)

    label("loc_4D2")

    TurnDirection(0x101, 0x8, 0)
    OP_69(0x101, 0x7D0)

    ChrTalk(
        0x101,
        "#000F那个～可以打扰一下吗？\x02",
    )

    CloseMessageWindow()
    TalkBegin(0x8)

    ChrTalk(
        0x8,
        "嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F您是豪尔斯教区长吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "呵～呵～呵。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我就是豪尔斯没错啊……\x01",
            "找我有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80F")

    label("loc_56A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_652")
    Fade(1000)
    SetChrPos(0x102, 57400, 1000, 52500, 90)
    SetChrPos(0x101, 57400, 1000, 51300, 45)
    SetChrPos(0x103, 56400, 1000, 51500, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D0")
    SetChrPos(0x104, 56400, 1000, 50200, 45)
    Jump("loc_5EF")

    label("loc_5D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x33)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5EF")
    SetChrPos(0x134, 56400, 1000, 50200, 45)

    label("loc_5EF")

    TurnDirection(0x102, 0x8, 0)
    OP_69(0x102, 0x7D0)

    ChrTalk(
        0x102,
        (
            "#010F教区长，\x01",
            "可以打扰您一下吗？\x02",
        )
    )

    CloseMessageWindow()
    TalkBegin(0x8)

    ChrTalk(
        0x8,
        "嗯？\x02",
    )

    CloseMessageWindow()
    Jump("loc_80F")

    label("loc_652")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72F")
    Fade(1000)
    SetChrPos(0x103, 57400, 1000, 52500, 90)
    SetChrPos(0x101, 57400, 1000, 51300, 45)
    SetChrPos(0x102, 56400, 1000, 51500, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B8")
    SetChrPos(0x104, 56400, 1000, 50200, 45)
    Jump("loc_6D7")

    label("loc_6B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x33)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D7")
    SetChrPos(0x134, 56400, 1000, 50200, 45)

    label("loc_6D7")

    TurnDirection(0x103, 0x8, 0)
    OP_69(0x103, 0x7D0)

    ChrTalk(
        0x103,
        (
            "#020F教区长，\x01",
            "可以打扰您一下吗？\x02",
        )
    )

    CloseMessageWindow()
    TalkBegin(0x8)

    ChrTalk(
        0x8,
        "嗯？\x02",
    )

    CloseMessageWindow()
    Jump("loc_80F")

    label("loc_72F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80F")
    Fade(1000)
    SetChrPos(0x104, 57400, 1000, 52500, 90)
    SetChrPos(0x101, 57400, 1000, 51300, 45)
    SetChrPos(0x103, 56400, 1000, 50200, 45)
    SetChrPos(0x102, 56400, 1000, 51500, 90)
    TurnDirection(0x104, 0x8, 0)
    OP_69(0x104, 0x7D0)

    ChrTalk(
        0x104,
        (
            "#030F哟，亲爱的教区长您好啊。\x02\x03",
            "不好意思，\x01",
            "不知道能不能和你聊几句呢。 \x02",
        )
    )

    CloseMessageWindow()
    TalkBegin(0x8)

    ChrTalk(
        0x8,
        "嗯？\x02",
    )

    CloseMessageWindow()

    label("loc_80F")


    ChrTalk(
        0x101,
        (
            "#000F请收下这个。\x02\x03",
            "这是洛连特的迪拜恩教区长\x01",
            "要我转交给您的一封信。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "教区长的亲笔信\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C0")
    OP_28(0xD, 0x1, 0x4000)

    label("loc_8C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_931")
    OP_28(0xD, 0x1, 0x2000)
    OP_28(0xD, 0x1, 0x2)

    ChrTalk(
        0x101,
        (
            "#000F抱歉，因为有一些事情，\x01",
            "送来的时间稍微晚了一些。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_937")

    label("loc_931")

    OP_28(0xD, 0x1, 0x4)

    label("loc_937")

    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "呵～呵～呵。\x01",
            "哎呀，真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "那么我就收下了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我先看看\x01",
            "这封信到底写了些什么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "迪拜恩教区长又在\x01",
            "设计一种新的配药方法了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F…………嗯？\x02\x03",
            "配药方法……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 0)

    ChrTalk(
        0x8,
        (
            "呵～呵～呵。\x01",
            "难道你不知道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "迪拜恩教区长可以说是利贝尔无人不知、\x01",
            "无人不晓的药学大师哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在进入大圣堂之前\x01",
            "就已经声名远扬了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#004F啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "迪拜恩教区长到洛连特任职之后，\x01",
            "研究还是从未间断过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "一旦发现了疗效颇佳的药材，\x01",
            "总会像这样来通知我们。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CBA")

    ChrTalk(
        0x103,
        (
            "#020F教区长调制出的新药，\x01",
            "对我们这些游击士来说\x01",
            "的确是非常有用。\x02\x03",
            "总是在我们忙于工作的时候\x01",
            "默默保护着我们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CBA")


    ChrTalk(
        0x101,
        (
            "#004F……这样的事情我居然不知道。\x01",
            "　\x02\x03",
            "真是的……\x01",
            "为什么我从来都没听他说过呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F教区长一直都是如此。\x02\x03",
            "他很少和别人说起\x01",
            "关于他自己的事情。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，原来是这样啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E8D")
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(
        0x101,
        (
            "#509F和某个口出狂言\x01",
            "尽说些不着边际的话的人完全不一样。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(
        0x104,
        (
            "#035F……呼，艾丝蒂尔君。\x02\x03",
            "不要这么看待我嘛。\x01",
            "我会很困扰的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#007F……真是不知反省呢……\x02",
    )

    CloseMessageWindow()

    label("loc_E8D")


    ChrTalk(
        0x8,
        (
            "迪拜恩教区长是一位\x01",
            "严于律己的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在劝诫他人的同时，\x01",
            "也不断地反省自己。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "现在的年轻人\x01",
            "都应该以他为榜样啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我这样说是不是要求太高了呢。\x01",
            "呵～呵～呵。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FB2():
        TurnDirection(0x104, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FB2)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        "#506F……呵～呵～呵。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过嘛， \x01",
            "人们首先要严格要求自己，\x01",
            "才能不断地进步。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 0)

    ChrTalk(
        0x8,
        (
            "你们从洛连特一路赶来，\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "空之女神爱德丝啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "请赐予他们护佑……\x01",
            "并且给予他们指引……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【送亲笔信】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_8C(0x8, 180, 0)
    EventEnd(0x0)
    TalkEnd(0x8)
    Return()

    # Function_0_66 end

    SaveToFile()

Try(main)
