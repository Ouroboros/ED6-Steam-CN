from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T2521_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2600.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60031",
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
        "Function_1_BF9",          # 01, 1
        "Function_2_1061",         # 02, 2
        "Function_3_10CE",         # 03, 3
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_169")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6")
    TalkBegin(0x15)
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "多亏你们，\x01",
            "我终于集齐了全部三本必要的资料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好了，\x01",
            "那么我就继续展开研究了，\x01",
            "时间已经不多了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_166")

    label("loc_F6")

    SetChrFlags(0x15, 0x10)
    TalkBegin(0x15)

    ChrTalk(
        0xFE,
        "唔～原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们的预测\x01",
            "还有可以修正的余地啊。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x10)

    label("loc_166")

    Jump("loc_BF5")

    label("loc_169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1D4")
    TalkBegin(0x15)

    ChrTalk(
        0xFE,
        (
            "如果找到了《卢安经济史》，\x01",
            "请务必告诉我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了学园祭，\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF5")

    label("loc_1D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x400)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x800)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B7")
    TalkBegin(0x15)
    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "作为研究根据的资料还不太够啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其余的《卢安经济史》\x01",
            "你们在哪里看到过吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x33E)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x33F)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_40C")
    EventBegin(0x0)

    ChrTalk(
        0x101,
        "#006F嘿嘿～已经找到了哦。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D)"), scpexpr(EXPR_END)), "loc_327")
    OP_3F(0x33D, 1)
    OP_28(0x27, 0x1, 0x200)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "卢安经济史·上\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_327")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33E)"), scpexpr(EXPR_END)), "loc_387")
    OP_3F(0x33E, 1)
    OP_28(0x27, 0x1, 0x400)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "卢安经济史·中\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_387")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33F)"), scpexpr(EXPR_END)), "loc_3E8")
    OP_3F(0x33F, 1)
    OP_28(0x27, 0x1, 0x800)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "卢安经济史·下\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3E8")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "哦，我就在等它呢。\x02",
    )

    CloseMessageWindow()
    Call(1, 1)
    Jump("loc_4B4")

    label("loc_40C")


    ChrTalk(
        0x101,
        (
            "#003F唔～\x01",
            "好像没有看见过呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F嗯，是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哦，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果看到了其余的书，\x01",
            "还请过来告诉我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B4")

    Jump("loc_BF5")

    label("loc_4B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_57E")
    TalkBegin(0x15)

    ChrTalk(
        0xFE,
        (
            "因为是用于研究成果展示的资料，\x01",
            "所以无论如何也要找到……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是名为《卢安经济史》的\x01",
            "三本一套的老书，\x01",
            "不知道被谁给拿走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果找到了的话，\x01",
            "请务必告诉我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF5")

    label("loc_57E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_8DB")
    TalkBegin(0x15)
    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "作为研究根据的资料还不太够啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "《卢安经济史》这套书\x01",
            "你们在哪里看到过吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x33E)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x33F)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_82A")
    EventBegin(0x0)

    ChrTalk(
        0x101,
        (
            "#000F嗯～你说的……\x02\x03",
            "应该就是这本书了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F嗯，我想也是。\x02\x03",
            "罗基克，\x01",
            "你要找的是这本书吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D)"), scpexpr(EXPR_END)), "loc_733")
    OP_3F(0x33D, 1)
    OP_28(0x27, 0x1, 0x200)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "卢安经济史·上\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_733")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33E)"), scpexpr(EXPR_END)), "loc_793")
    OP_3F(0x33E, 1)
    OP_28(0x27, 0x1, 0x400)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "卢安经济史·中\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_793")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33F)"), scpexpr(EXPR_END)), "loc_7F4")
    OP_3F(0x33F, 1)
    OP_28(0x27, 0x1, 0x800)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "卢安经济史·下\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7F4")

    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(
        0xFE,
        (
            "哦，没错。\x01",
            "我要找的就是它。\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 1)
    Jump("loc_8D8")

    label("loc_82A")


    ChrTalk(
        0x101,
        (
            "#002F唔～\x01",
            "好像没有看见过呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F抱歉，罗基克。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀～又不是你们的错，\x01",
            "不用道歉啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果看到的话，\x01",
            "还请过来告诉我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D8")

    Jump("loc_BF5")

    label("loc_8DB")

    OP_A2(0xA)
    OP_28(0x27, 0x1, 0x20)
    ClearChrFlags(0x15, 0x10)
    TalkBegin(0x15)
    EventBegin(0x0)
    TurnDirection(0x15, 0x105, 0)
    OP_4A(0x15, 255)

    ChrTalk(
        0xFE,
        "唔，是科洛丝啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#044F啊，罗基克。\x02\x03",
            "你还在做成果展览的资料收集吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，是啊。\x01",
            "再加把劲就可以了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是作为研究最终根据的\x01",
            "必要资料还没有找到呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F啊……\x01",
            "这可就麻烦了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是名为《卢安经济史》的\x01",
            "三本一套的老书。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "资料室里没有，\x01",
            "应该是被人拿出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们有没有在学院里\x01",
            "看到过那几本书呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F唔……\x01",
            "没有注意到哪里有呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "这样啊……不过，\x01",
            "肯定是在校园的某个地方的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(
        0xFE,
        (
            "如果找到了的话，\x01",
            "请务必告诉我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F嗯，我知道了。\x02\x03",
            "如果找到了，\x01",
            "我们会立刻来告诉你的。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x10)
    EventEnd(0x1)
    OP_4B(0x15, 255)

    label("loc_BF5")

    TalkEnd(0x15)
    Return()

    # Function_0_66 end

    def Function_1_BF9(): pass

    label("Function_1_BF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x400)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EDE")
    OP_28(0x27, 0x1, 0x1000)
    OP_28(0x3D, 0x1, 0x400)
    OP_2C(0x3D, 0x1F4)
    OP_2B(0x3D, 0x1)

    ChrTalk(
        0xFE,
        (
            "好，这样一来，\x01",
            "三本必要的资料终于都到手了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xFE, 400)

    ChrTalk(
        0x105,
        (
            "#040F呵呵，罗基克，\x01",
            "我期待着你的研究成果哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(
        0xFE,
        "嗯，敬请期待。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "能够得到科洛丝你们\x01",
            "这样尽力的帮助，\x01",
            "我一定会做到最好的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好了，\x01",
            "那么我就继续展开研究了，\x01",
            "时间已经不多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "科洛丝你们的\x01",
            "舞台剧也要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F嗯，我们是不会被比下去的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#040F……是吧，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(
        0x101,
        "#001F嘿嘿，你就好好期待吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "嗯，我们一起加油吧。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "学园祭的校园任务\x01",
            "【收集研究资料】\x07\x00",
            "完成！\x02",
        )
    )

    OP_83(0x2, 0x3)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(100)
    Jump("loc_105B")

    label("loc_EDE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x400)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x400)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F8A")

    ChrTalk(
        0xFE,
        (
            "最后一本肯定\x01",
            "也在学院里面的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了学园祭，\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_105B")

    label("loc_F8A")


    ChrTalk(
        0xFE,
        (
            "应该还有\x01",
            "另外两本的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有了这上面的资料，\x01",
            "我的研究成果展览\x01",
            "就会很充实了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了学园祭，\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_105B")

    EventEnd(0x1)
    TalkEnd(0x15)
    Return()

    # Function_1_BF9 end

    def Function_2_1061(): pass

    label("Function_2_1061")

    OP_A3(0xA)
    OP_A3(0xB)
    OP_22(0x11, 0x0, 0x64)
    SetChrFlags(0x16, 0x80)
    OP_64(0x1, 0x1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "卢安经济史·上\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x33D, 1)
    OP_28(0x27, 0x1, 0x40)
    TalkEnd(0xFF)
    Return()

    # Function_2_1061 end

    def Function_3_10CE(): pass

    label("Function_3_10CE")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架大部分地方都空着。\x01",
            "看起来资料都被拿走了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x33E)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x33F)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_130C")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【归还卢安经济史】\x01",      # 0
            "【不归还】\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_11EF"),
        (1, "loc_1309"),
        (SWITCH_DEFAULT, "loc_130C"),
    )


    label("loc_11EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D)"), scpexpr(EXPR_END)), "loc_124B")
    OP_3F(0x33D, 1)
    OP_28(0x27, 0x1, 0x200)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了\x07\x02",
            "卢安经济史·上\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_124B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33E)"), scpexpr(EXPR_END)), "loc_12A8")
    OP_3F(0x33E, 1)
    OP_28(0x27, 0x1, 0x400)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了\x07\x02",
            "卢安经济史·中\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_12A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33F)"), scpexpr(EXPR_END)), "loc_1306")
    OP_3F(0x33F, 1)
    OP_28(0x27, 0x1, 0x800)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了\x07\x02",
            "卢安经济史·下\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1306")

    Jump("loc_130C")

    label("loc_1309")

    Jump("loc_130C")

    label("loc_130C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x400)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_132B")
    OP_64(0x3, 0x1)

    label("loc_132B")

    TalkEnd(0xFF)
    Return()

    # Function_3_10CE end

    SaveToFile()

Try(main)
