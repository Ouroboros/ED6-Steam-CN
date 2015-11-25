from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3111_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T3111   ._SN',
            'ED6_DT01/T3111_1 ._SN',
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
        "Function_1_7E6",          # 01, 1
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_239")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_135")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_A1")

    label("loc_9A")

    TurnDirection(0x102, 0x0, 400)

    label("loc_A1")


    ChrTalk(
        0x102,
        (
            "#010F（刚才已经问过话了，\x01",
            "　安东尼一点反应也没有。）\x02\x03",
            "#010F（那么，我们就去\x01",
            "　二楼工房长的房间调查看看吧。）\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E")

    label("loc_135")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F（刚才调查过了，\x01",
            "　一点反应也没有。）\x02\x03",
            "#010F（我们再到工房里面调查一下吧。）\x01",
            "　\x02\x03",
            "#010F（照米妮亚姆医生说的，\x01",
            "　在某个地方也许会有线索的。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#003F（唔……也只有这样了。）\x02",
    )

    CloseMessageWindow()

    label("loc_22E")

    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_7E5")

    label("loc_239")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DE")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(-10040, 0, -1620, 0)
    SetChrPos(0x101, -8960, 0, -1680, 228)
    SetChrPos(0x102, -8920, 0, -530, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A0")
    SetChrPos(0x107, -7480, 0, -1290, 224)

    label("loc_2A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BF")
    SetChrPos(0x106, -7720, 0, -160, 225)

    label("loc_2BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DE")
    SetChrPos(0x13C, -8770, 0, -2870, 290)

    label("loc_2DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F8")

    def lambda_2F0():
        TurnDirection(0x0, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2F0)

    label("loc_2F8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_312")

    def lambda_30A():
        TurnDirection(0x1, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_30A)

    label("loc_312")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32C")

    def lambda_324():
        TurnDirection(0x2, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_324)

    label("loc_32C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_346")

    def lambda_33E():
        TurnDirection(0x3, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_33E)

    label("loc_346")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_360")

    def lambda_358():
        TurnDirection(0x4, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_358)

    label("loc_360")

    OP_0D()
    Sleep(400)
    OP_4A(0xA, 255)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x0, 400)
    Sleep(800)

    ChrTalk(
        0xA,
        "怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不好意思，\x01",
            "我现在正在谈重要的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "有事的话请等一会儿。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 0, 400)
    OP_4B(0xA, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_71B")
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#003F（唔～\x01",
            "　没机会向他提问啊～）\x02\x03",
            "#004F（啊，对了，\x01",
            "　安东尼有什么反应吗？）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4BD():
        TurnDirection(0x102, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4BD)

    def lambda_4CB():
        TurnDirection(0x107, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4CB)
    TurnDirection(0x101, 0x13C, 400)

    ChrTalk(
        0x13C,
        "…………………………\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    TurnDirection(0x13C, 0x101, 400)

    ChrTalk(
        0x13C,
        "………………喵噢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#063F（没有反应呢～）\x02",
    )

    CloseMessageWindow()
    OP_28(0x2C, 0x1, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_711")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_603")

    ChrTalk(
        0x101,
        (
            "#505F唔～对两个人都没有反应呢。\x02\x03",
            "果然还是去刚才\x01",
            "安东尼有反应的地方调查一下吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是二楼工房长的房间对吧。\x02\x03",
            "我们赶快去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_711")

    label("loc_603")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#004F（咦，\x01",
            "　这么说对这两人都没有反应了？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F（也就是说没有线索了。）\x02\x03",
            "#010F（我们再到工房里面调查一下吧。）\x01",
            "　\x02\x03",
            "#010F（照米妮亚姆医生说的，\x01",
            "　在某个地方也许会有线索的。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F（唔……也只有这样了。）\x02",
    )

    CloseMessageWindow()
    OP_28(0x2C, 0x1, 0x80)

    label("loc_711")

    Sleep(50)
    EventEnd(0x4)
    Jump("loc_7E5")

    label("loc_71B")

    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#003F（完、完全插不上嘴……）\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#017F（好像在商谈重要事情。）\x02\x03",
            "（现在还是不要问他了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x2C, 0x1, 0x8)
    ClearMapFlags(0x80)

    label("loc_7E5")

    Return()

    # Function_0_66 end

    def Function_1_7E6(): pass

    label("Function_1_7E6")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -115940, -4000, -111340, 180)
    SetChrPos(0x102, -116620, -4000, -110300, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_82E")
    SetChrPos(0x107, -115430, -4000, -109960, 180)

    label("loc_82E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_84D")
    SetChrPos(0x106, -116050, -4000, -109140, 180)

    label("loc_84D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86C")
    SetChrPos(0x108, -116050, -4000, -109140, 180)

    label("loc_86C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88B")
    SetChrPos(0x110, -116740, -4000, -108860, 180)

    label("loc_88B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8AA")
    SetChrPos(0x13C, -116740, -4000, -108860, 180)

    label("loc_8AA")

    OP_6D(-116920, -4000, -112310, 2000)
    OP_0D()

    ChrTalk(
        0x101,
        "#000F菲小姐，打扰一下好吗？\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xE, 0x10)
    TalkBegin(0xE)
    OP_4A(0xE, 255)
    ClearChrFlags(0xE, 0x10)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "嗯？什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F这是某人托我们带给您的东西。\x01",
            "　\x02\x03",
            "这个，请您收下。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "给菲的情书\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_3F(0x35E, 1)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "这封信……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…………难道说，\x01",
            "是沃尔费堡垒的布拉姆写的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，是的。\x02\x03",
            "#002F（好！\x01",
            "　这就把礼物拿给她。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF0")
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#008F（……哎呀，虽然心里一直惦记着，\x01",
            "　最后还是忘记买礼物了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_F30")

    label("loc_AF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B7B")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【工作手套】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B6C"),
        (1, "loc_B72"),
        (SWITCH_DEFAULT, "loc_B78"),
    )


    label("loc_B6C")

    OP_A2(0xB)
    Jump("loc_B78")

    label("loc_B72")

    OP_A2(0xE)
    Jump("loc_B78")

    label("loc_B78")

    Jump("loc_F30")

    label("loc_B7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C08")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【果馅饼】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BF9"),
        (1, "loc_BFF"),
        (SWITCH_DEFAULT, "loc_C05"),
    )


    label("loc_BF9")

    OP_A2(0xC)
    Jump("loc_C05")

    label("loc_BFF")

    OP_A2(0xE)
    Jump("loc_C05")

    label("loc_C05")

    Jump("loc_F30")

    label("loc_C08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C97")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【绒毛编织帽】\x01",      # 0
            "【放弃】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C88"),
        (1, "loc_C8E"),
        (SWITCH_DEFAULT, "loc_C94"),
    )


    label("loc_C88")

    OP_A2(0xD)
    Jump("loc_C94")

    label("loc_C8E")

    OP_A2(0xE)
    Jump("loc_C94")

    label("loc_C94")

    Jump("loc_F30")

    label("loc_C97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D3B")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【工作手套】\x01",      # 0
            "【果馅饼】\x01",        # 1
            "【放弃】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D26"),
        (1, "loc_D2C"),
        (2, "loc_D32"),
        (SWITCH_DEFAULT, "loc_D38"),
    )


    label("loc_D26")

    OP_A2(0xB)
    Jump("loc_D38")

    label("loc_D2C")

    OP_A2(0xC)
    Jump("loc_D38")

    label("loc_D32")

    OP_A2(0xE)
    Jump("loc_D38")

    label("loc_D38")

    Jump("loc_F30")

    label("loc_D3B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE1")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【工作手套】\x01",        # 0
            "【绒毛编织帽】\x01",      # 1
            "【放弃】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DCC"),
        (1, "loc_DD2"),
        (2, "loc_DD8"),
        (SWITCH_DEFAULT, "loc_DDE"),
    )


    label("loc_DCC")

    OP_A2(0xB)
    Jump("loc_DDE")

    label("loc_DD2")

    OP_A2(0xD)
    Jump("loc_DDE")

    label("loc_DD8")

    OP_A2(0xE)
    Jump("loc_DDE")

    label("loc_DDE")

    Jump("loc_F30")

    label("loc_DE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E89")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【果馅饼】\x01",          # 0
            "【绒毛编织帽】\x01",      # 1
            "【放弃】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E74"),
        (1, "loc_E7A"),
        (2, "loc_E80"),
        (SWITCH_DEFAULT, "loc_E86"),
    )


    label("loc_E74")

    OP_A2(0xC)
    Jump("loc_E86")

    label("loc_E7A")

    OP_A2(0xD)
    Jump("loc_E86")

    label("loc_E80")

    OP_A2(0xE)
    Jump("loc_E86")

    label("loc_E86")

    Jump("loc_F30")

    label("loc_E89")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【工作手套】\x01",        # 0
            "【果馅饼】\x01",          # 1
            "【绒毛编织帽】\x01",      # 2
            "【放弃】\x01",            # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F1B"),
        (1, "loc_F1E"),
        (2, "loc_F24"),
        (3, "loc_F2A"),
        (SWITCH_DEFAULT, "loc_F30"),
    )


    label("loc_F1B")

    OP_A2(0xB)

    label("loc_F1E")

    OP_A2(0xC)
    Jump("loc_F30")

    label("loc_F24")

    OP_A2(0xD)
    Jump("loc_F30")

    label("loc_F2A")

    OP_A2(0xE)
    Jump("loc_F30")

    label("loc_F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_11B5")

    ChrTalk(
        0x101,
        (
            "#000F对了，\x01",
            "这是他送你的礼物。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "工作手套\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0xFE,
        (
            "……礼物？\x01",
            "工作手套？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好、好吧，\x01",
            "我收下了……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 200)

    ChrTalk(
        0xFE,
        (
            "哼，真是的，\x01",
            "那个家伙到底在想什么，\x01",
            "我一点都不明白……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……………………………\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#509F（唔…………………）\x02\x03",
            "（这、这个礼物\x01",
            "　好像失败了……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0xFE, 0, 400)

    ChrTalk(
        0xFE,
        "……哎呀，对、对不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "谢谢你们\x01",
            "特地给我送过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那…………\x01",
            "我要继续工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F啊、嗯，再见。\x02",
    )

    CloseMessageWindow()
    OP_3F(0x14D, 1)
    OP_28(0x31, 0x1, 0x40)
    OP_2B(0x31, 0x2)
    Jump("loc_1895")

    label("loc_11B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_1475")

    ChrTalk(
        0x101,
        (
            "#000F对了，\x01",
            "这是他送你的礼物。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "果馅饼\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_62(0xFE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0xFE,
        (
            "谢、谢谢了。\x01",
            "我很高兴…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过我最近要\x01",
            "控制甜食的数量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "尽管这样，\x01",
            "却送这样的礼物给我……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 200)

    ChrTalk(
        0xFE,
        (
            "哼！看来他不懂得体贴别人这点\x01",
            "还是完全没变。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……………………………\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#509F（唔…………………）\x02\x03",
            "（这、这个礼物\x01",
            "　好像失败了……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0xFE, 0, 400)

    ChrTalk(
        0xFE,
        "……哎呀，对、对不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "谢谢你们\x01",
            "特地给我送过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那…………\x01",
            "我要继续工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F啊、嗯，再见。\x02",
    )

    CloseMessageWindow()
    OP_3F(0x1B2, 1)
    OP_28(0x31, 0x1, 0x80)
    OP_2B(0x31, 0x2)
    Jump("loc_1895")

    label("loc_1475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_166F")

    ChrTalk(
        0x101,
        (
            "#000F对了，\x01",
            "这是他送你的礼物。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "绒毛编织帽\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(
        0xFE,
        "哇，好可爱呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "他总算是稍微……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……开始为我着想了呢。\x01",
            "呵呵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过既然知道该这样，\x01",
            "为什么不早点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……………………………\x02",
    )

    CloseMessageWindow()
    Sleep(800)

    ChrTalk(
        0xFE,
        "……哎呀，对、对不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "谢谢你们\x01",
            "特地给我送过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那…………\x01",
            "我要继续工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F啊、嗯，再见。\x02",
    )

    CloseMessageWindow()
    OP_3F(0x14A, 1)
    OP_28(0x31, 0x1, 0x20)
    OP_2B(0x31, 0x4)
    Jump("loc_1895")

    label("loc_166F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_16B1")

    ChrTalk(
        0x101,
        (
            "#505F（……唔～\x01",
            "　没有看到合适的礼物。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B1")

    Sleep(400)

    ChrTalk(
        0xFE,
        "呼～这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那家伙啊，\x01",
            "肯定是已经反省过了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 200)

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "就算他现在想到要写封信给我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……………………………\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#509F（唔…………………）\x02\x03",
            "（果然还是应该送点礼物才行……）\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0xFE, 0, 400)

    ChrTalk(
        0xFE,
        "……哎呀，对、对不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "谢谢你们\x01",
            "特地给我送过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那…………\x01",
            "我要继续工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F啊、嗯，再见。\x02",
    )

    CloseMessageWindow()
    OP_28(0x31, 0x1, 0x100)

    label("loc_1895")

    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【爱之使者】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x31, 0x4, 0x10)
    OP_28(0x31, 0x1, 0x10)
    OP_A2(0xA)
    EventEnd(0x0)
    OP_4B(0xE, 255)
    Return()

    # Function_1_7E6 end

    SaveToFile()

Try(main)
