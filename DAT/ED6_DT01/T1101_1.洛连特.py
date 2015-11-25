from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T1101_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
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
        "Function_1_309",          # 01, 1
        "Function_2_321",          # 02, 2
    )


    def Function_0_66(): pass

    label("Function_0_66")

    TalkBegin(0x14)

    ChrTalk(
        0xFE,
        "准备好了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FB")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        10,
        100,
        0,
        (
            "【好了】\x01",                # 0
            "【对不起，还没有】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_100"),
        (1, "loc_256"),
        (SWITCH_DEFAULT, "loc_2F8"),
    )


    label("loc_100")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_28(0x10, 0x4, 0x8)
    OP_28(0x10, 0x1, 0x4)

    ChrTalk(
        0x101,
        "#006F好了，已经万事俱备了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "我也准备好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么，接下来就靠你们了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#020F古罗尼山顶，\x01",
            "从这里一直向西就可以到达了。\x02\x03",
            "路途比较远，\x01",
            "要打起精神来哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(
        0x102,
        "#010F嗯。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F好了，出发吧！\x02",
    )

    CloseMessageWindow()
    Call(1, 1)
    Jump("loc_2F8")

    label("loc_256")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)

    ChrTalk(
        0x101,
        (
            "#000F对不起，\x01",
            "还要再准备一下。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "请你们快点回来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我有很重要的一笔生意要谈。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F8")

    label("loc_2F8")

    Jump("loc_83")

    label("loc_2FB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0x14)
    Return()

    # Function_0_66 end

    def Function_1_309(): pass

    label("Function_1_309")

    FadeToDark(1000, 0, -1)
    OP_0D()
    AddParty(0x34, 0x3)
    NewScene("ED6_DT01/R1200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_1_309 end

    def Function_2_321(): pass

    label("Function_2_321")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, 24400, 0, 46300, 270)
    SetChrPos(0x102, 25400, 0, 45300, 270)
    SetChrPos(0x103, 24500, 0, 44300, 270)
    OP_69(0x14, 0x0)
    TalkBegin(0x14)
    FadeToBright(1000, 0)
    OP_0D()
    TurnDirection(0x101, 0x14, 400)

    ChrTalk(
        0x101,
        (
            "#501F对不起啊，哈尔德先生。\x01",
            "我们还要再补充一下装备。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x101, 400)

    ChrTalk(
        0x14,
        (
            "我会在这里等着的，\x01",
            "请尽量快一点。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    TalkEnd(0x14)
    Return()

    # Function_2_321 end

    SaveToFile()

Try(main)
