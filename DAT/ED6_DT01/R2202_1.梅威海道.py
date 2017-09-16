from ED6ScenarioHelper import *

def main():
    # 梅威海道

    CreateScenaFile(
        FileName            = 'R2202_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'R2202.x',
        MapIndex            = 101,
        MapDefaultBGM       = "ed60020",
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
        "Function_1_4B8",          # 01, 1
    )


    def Function_0_66(): pass

    label("Function_0_66")

    EventBegin(0x0)
    OP_64(0x0, 0x1)
    Fade(1000)
    OP_6C(90000, 0)
    OP_69(0x101, 0x0)
    OP_0D()
    Sleep(800)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "骷髅刀\x07\x00",
            "和\x07\x02",
            "古海图的残片\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x335, 1)
    OP_3E(0x2D, 1)
    Sleep(800)

    ChrTalk(
        0x101,
        "#501F咦～好酷的短剑啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F看上去是相当古老的东西呢。\x02\x03",
            "从使用的材质来看，\x01",
            "也许是导力革命以前的东西呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F对了，\x01",
            "那个像是碎纸片的东西是什么呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F好像是航海图的碎片。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_41D")
    OP_28(0x1E, 0x1, 0x10)
    OP_62(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F等一下…………\x02\x03",
            "吉米先生所说的财宝\x01",
            "难道就是指这个？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F很遗憾，\x01",
            "两者恐怕毫无联系。\x02\x03",
            "#010F这些应该都是从什么地方\x01",
            "飘流过来的东西。\x02\x03",
            "可能是遇难船只上面的货物吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3A1")
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(
        0x105,
        (
            "#040F嗯，我想也是。\x02\x03",
            "听说以前这类的\x01",
            "海上事故很多呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)
    Jump("loc_41A")

    label("loc_3A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_41A")
    TurnDirection(0x136, 0x102, 400)

    ChrTalk(
        0x136,
        (
            "#040F嗯，我想也是。\x02\x03",
            "听说以前这类的\x01",
            "海上事故很多呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x136, 400)

    label("loc_41A")

    Jump("loc_423")

    label("loc_41D")

    OP_28(0x1E, 0x1, 0x4000)

    label("loc_423")


    ChrTalk(
        0x101,
        (
            "#505F对啊，在还没有飞艇的时候，\x01",
            "大家都是用船运东西的呢。\x02\x03",
            "这里的海岸过去\x01",
            "也是货船途径的通道吧？\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_0_66 end

    def Function_1_4B8(): pass

    label("Function_1_4B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x326)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_638")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_581")
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#040F往这边走就到王立学院了……\x01",
            "　\x02\x03",
            "你们的工作不要紧吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#000F啊，对了。\x02\x03",
            "要赶快把工作先做完。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61A")

    label("loc_581")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F这边是通往王立学院的街景林道吧。\x01",
            "　\x02\x03",
            "在去学院之前\x01",
            "还是先把手头的工作做完吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F啊，没错。\x02",
    )

    CloseMessageWindow()

    label("loc_61A")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_70B")

    label("loc_638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70B")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65C")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_663")

    label("loc_65C")

    TurnDirection(0x102, 0x0, 400)

    label("loc_663")


    ChrTalk(
        0x102,
        (
            "#012F这边是王立学院。\x02\x03",
            "我们要赶快去市长官邸…………\x01",
            "在王国军来之前尽量拖延时间。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_70B")

    Return()

    # Function_1_4B8 end

    SaveToFile()

Try(main)
