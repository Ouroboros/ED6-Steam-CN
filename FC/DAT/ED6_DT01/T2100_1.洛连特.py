from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T2100_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2100.x',
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
    )


    def Function_0_66(): pass

    label("Function_0_66")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_51(0x12, 0x1, (scpexpr(EXPR_PUSH_LONG, 0x32C8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x11EB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_28(0x20, 0x1, 0x4)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8B(0x0, 0x34BC, 0x11EB8, 0x190)
    Fade(1000)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_PUSH_LONG, 0x11EB8), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_PUSH_LONG, 0x11EB8), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B")
    OP_51(0x1, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x1, 180, 0)
    OP_8C(0x2, 180, 0)
    Jump("loc_2B2")

    label("loc_13B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_PUSH_LONG, 0x11EB8), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_PUSH_LONG, 0x11EB8), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B9")
    OP_51(0x1, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x1, 180, 0)
    OP_8C(0x2, 180, 0)
    Jump("loc_2B2")

    label("loc_1B9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_PUSH_LONG, 0x11EB8), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_PUSH_LONG, 0x11EB8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_237")
    OP_51(0x1, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x1, 0, 0)
    OP_8C(0x2, 0, 0)
    Jump("loc_2B2")

    label("loc_237")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_PUSH_LONG, 0x11EB8), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_PUSH_LONG, 0x11EB8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B2")
    OP_51(0x1, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x1, 0, 0)
    OP_8C(0x2, 0, 0)

    label("loc_2B2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EB")

    def lambda_2CD():
        OP_6D(13500, 1500, 73400, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2CD)
    OP_6C(135000, 3000)
    Jump("loc_3CC")

    label("loc_2EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_324")

    def lambda_306():
        OP_6D(13500, 1500, 73400, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_306)
    OP_6C(45000, 3000)
    Jump("loc_3CC")

    label("loc_324")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35D")

    def lambda_33F():
        OP_6D(13500, 1500, 73400, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_33F)
    OP_6C(45000, 3000)
    Jump("loc_3CC")

    label("loc_35D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_396")

    def lambda_378():
        OP_6D(13500, 1500, 73400, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_378)
    OP_6C(45000, 3000)
    Jump("loc_3CC")

    label("loc_396")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CC")

    def lambda_3B1():
        OP_6D(13500, 1500, 73400, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3B1)
    OP_6C(135000, 3000)

    label("loc_3CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45A")

    ChrTalk(
        0x101,
        "#002F#1P…………嗯？\x02",
    )

    CloseMessageWindow()

    def lambda_3F0():
        TurnDirection(0x102, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F0)
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x102,
        "#014F怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F#1P……那、那个。\x01",
            "不是卡片吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_448():
        TurnDirection(0x102, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_448)
    TurnDirection(0x105, 0x12, 400)
    Jump("loc_609")

    label("loc_45A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54B")

    ChrTalk(
        0x102,
        "#014F#1P嗯…………？\x02",
    )

    CloseMessageWindow()

    def lambda_47B():
        TurnDirection(0x101, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47B)
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(
        0x101,
        "#501F怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#1P…………是卡片。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F……啊！？\x02\x03",
            "在、在哪里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F#1P在那块金属板上面。\x02",
    )

    CloseMessageWindow()

    def lambda_51D():
        TurnDirection(0x101, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51D)
    TurnDirection(0x105, 0x12, 400)

    ChrTalk(
        0x101,
        "#004F啊，果然！\x02",
    )

    CloseMessageWindow()
    Jump("loc_609")

    label("loc_54B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_609")

    ChrTalk(
        0x105,
        "#044F#1P咦…………\x02",
    )

    CloseMessageWindow()

    def lambda_56D():
        TurnDirection(0x102, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_56D)
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#501F怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#044F#1P那里有一张卡片……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_5D3():
        TurnDirection(0x101, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D3)
    TurnDirection(0x102, 0x12, 400)

    ChrTalk(
        0x101,
        (
            "#004F啊…………！？\x02\x03",
            "啊，果然！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_609")


    ChrTalk(
        0x102,
        "#012F#2P……我来确认一下。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x102, 0x40)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_686")

    def lambda_63D():
        OP_92(0x1, 0x12, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_63D)

    def lambda_652():
        OP_92(0x2, 0x12, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_652)
    OP_8E(0x102, 0x3138, 0x0, 0x11EB8, 0x7D0, 0x0)
    TurnDirection(0x1, 0x12, 0)
    TurnDirection(0x2, 0x12, 0)
    Jump("loc_773")

    label("loc_686")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FB")

    def lambda_698():
        OP_91(0x0, 0xFFFFFCE0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_698)
    OP_91(0x102, 0x258, 0x0, 0x0, 0x7D0, 0x0)

    def lambda_6C7():
        OP_92(0x2, 0x12, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_6C7)
    OP_8E(0x102, 0x3138, 0x0, 0x11EB8, 0x7D0, 0x0)
    TurnDirection(0x0, 0x12, 0)
    TurnDirection(0x2, 0x12, 0)
    Jump("loc_773")

    label("loc_6FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_773")

    def lambda_70D():
        OP_91(0x0, 0xFFFFFCE0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_70D)

    def lambda_728():
        OP_91(0x1, 0xFFFFFF38, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_728)
    OP_91(0x102, 0x2BC, 0x0, 0x0, 0x7D0, 0x0)
    TurnDirection(0x0, 0x12, 0)
    TurnDirection(0x1, 0x12, 0)
    OP_8E(0x102, 0x3138, 0x0, 0x11EB8, 0x7D0, 0x0)

    label("loc_773")

    ClearChrFlags(0x102, 0x40)
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_7BD():
        OP_69(0x12, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7BD)
    OP_8C(0x102, 90, 400)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#012F…………果然没错。\x02\x03",
            "这上面贴的卡片\x01",
            "和在市长官邸里看到的一样。\x02\x03",
            "原来如此…………\x01",
            "所谓的『三只眼』\x01",
            "指的就是这个东西……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(800)
    Fade(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A1")
    OP_67(0, 4875, -10000, 0)
    OP_6D(21130, 1900, 79750, 3000)
    Jump("loc_8C3")

    label("loc_8A1")

    OP_67(0, 4875, -10000, 0)
    OP_6D(21130, 1900, 66830, 3000)

    label("loc_8C3")

    OP_0D()

    ChrTalk(
        0x101,
        (
            "#501F啊，原来是这样啊。\x01",
            "这样看来的确是三只眼睛呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(800)
    Fade(1000)
    OP_69(0x12, 0x0)
    OP_67(0, 9500, -10000, 0)
    OP_0D()
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#002F…………\x01",
            "卡片上面写的又是什么呢？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F嗯，来看看吧。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "『啊，探寻者们。\x01",
            "　如女神一般直视真实，\x01",
            "　抛弃虚伪的人啊。\x01",
            "　\x01",
            "　前往红与黑交织的\x01",
            "　无尽圆舞曲所在之处吧。\x01",
            "　如是，探寻者们，\x01",
            "　汝等将至苍之光所在。\x01",
            "　　　　　　　　　　　怪盗Ｂ』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#006F记录下来了，\x01",
            "这样就可以确定地点了。\x02\x03",
            "『红与黑交织的无尽\x01",
            "　圆舞曲所在之处』\x01",
            "…………就是这个地方。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#040F是红与黑……啊。\x02\x03",
            "我没猜错的话，\x01",
            "这也应该在卢安市内的某个地方吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B5F():
        TurnDirection(0x101, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5F)
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(
        0x102,
        (
            "#010F大概是这样吧。\x02\x03",
            "犯人似乎以让别人\x01",
            "去解自己设下的谜题为乐……\x02\x03",
            "所以应该不会破坏\x01",
            "自己所定下的规则。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BE1():
        TurnDirection(0x105, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BE1)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#009F真是个喜欢捉弄人的讨厌鬼。\x01",
            "　\x02\x03",
            "#006F总而言之，\x01",
            "我们现在就继续展开搜索吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x0, 0x1)
    EventEnd(0x0)
    Return()

    # Function_0_66 end

    SaveToFile()

Try(main)
