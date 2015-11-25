from ED6ScenarioHelper import *

def main():
    # 威尔特桥　关所

    CreateScenaFile(
        FileName            = 'T0500_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0500.x',
        MapIndex            = 18,
        MapDefaultBGM       = "ed60016",
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
        "Function_1_C5C",          # 01, 1
        "Function_2_C66",          # 02, 2
        "Function_3_C78",          # 03, 3
        "Function_4_CF6",          # 04, 4
        "Function_5_D74",          # 05, 5
        "Function_6_DF2",          # 06, 6
    )


    def Function_0_66(): pass

    label("Function_0_66")

    EventBegin(0x0)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    SetChrPos(0x101, -4900, 0, -22400, 90)
    SetChrPos(0x102, -4900, 0, -24400, 90)
    SetChrPos(0x8, 3000, 0, -22400, 270)
    SetChrPos(0x9, 3000, 0, -24400, 270)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -1000, 0, -20400, 180)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_6C(45000, 0)
    OP_6B(2500, 0)
    OP_6D(-20400, 0, -18400, 0)
    FadeToBright(3000, 0)
    OP_43(0xA, 0x1, 0x1, 0x1)
    OP_43(0xA, 0x2, 0x1, 0x2)
    OP_6C(315000, 6000)
    Sleep(1500)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)

    ChrTalk(
        0xA,
        "那么，训练现在开始。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "全体，向前五步走！\x02",
    )

    CloseMessageWindow()
    OP_43(0x8, 0x2, 0x1, 0x3)
    OP_43(0x9, 0x2, 0x1, 0x4)
    OP_43(0x102, 0x2, 0x1, 0x5)
    OP_43(0x101, 0x2, 0x1, 0x6)
    Sleep(5000)

    ChrTalk(
        0xA,
        "预备！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    SetChrPos(0x11, -1900, 0, -22400, 90)
    ClearChrFlags(0x11, 0x8)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x101, 0x40)
    SetChrPos(0x12, -1900, 0, -24400, 90)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x102, 0x40)
    SetChrPos(0xF, 0, 0, -22400, 270)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x10, 0, 0, -24400, 270)
    ClearChrFlags(0x10, 0x8)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0x9, 0x40)
    OP_0D()

    ChrTalk(
        0xF,
        "我好紧张……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "虽然明知道是训练……\x01",
            "可是感觉好害怕啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 135, 400)

    ChrTalk(
        0xA,
        (
            "现在是在训练中。\x01",
            "不许窃窃私语。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "要把它当作真正的战斗一样全神贯注！\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)

    ChrTalk(
        0xA,
        (
            "艾丝蒂尔、约修亚，\x01",
            "你们二位不必手下留情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#006F嗯，我一开始就没打算留情☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#012F知道了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(
        0x10,
        "怕怕～\x02",
    )

    CloseMessageWindow()
    Sleep(700)

    ChrTalk(
        0xA,
        "开战！\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x3ED, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_1D(0x10)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_497"),
        (2, "loc_8A5"),
        (1, "loc_8A5"),
        (SWITCH_DEFAULT, "loc_BE5"),
    )


    label("loc_497")

    FadeToBright(2000, 0)
    SetChrPos(0x13, 0, 0, -22400, 270)
    SetChrPos(0x14, 0, 0, -24400, 270)
    SetChrSubChip(0x13, 3)
    SetChrSubChip(0x14, 3)
    ClearChrFlags(0x13, 0x8)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x8)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x10, 0x40)
    SetChrPos(0x101, -1900, 0, -22400, 90)
    SetChrPos(0x102, -1900, 0, -24400, 90)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x102, 0x40)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    OP_0D()
    Sleep(700)
    OP_28(0x8, 0x1, 0x2)
    OP_2C(0x8, 0xC8)
    OP_2B(0x8, 0x2)

    ChrTalk(
        0xA,
        "好，到此为止。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "训练结束。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "疼死我了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "终于、终于结束了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F辛苦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F唉，真是可悲啊。\x02\x03",
            "你们这样还算是士兵吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x13, 0x3, 0x0, 0x7D0)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x8, 5)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x40)

    ChrTalk(
        0x8,
        "真、真是烦啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不要把我和\x01",
            "你这样的疯丫头相提并论！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#005F什么，疯、疯丫头～～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "够了，斯科特。\x01",
            "训练已经结束了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#017F艾丝蒂尔你也要冷静啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F哼～～～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(
        0xA,
        "……斯科特、哈罗德。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "刚才艾丝蒂尔的话\x01",
            "可是普通市民的心声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "你们觉得现在的自己能够保护市民的安全吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "自己好好地\x01",
            "思考一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "…………好、好的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE5")

    label("loc_8A5")

    FadeToBright(2000, 0)
    SetChrPos(0x15, -1900, 0, -22400, 90)
    OP_99(0x15, 0x3, 0x3, 0x0)
    ClearChrFlags(0x15, 0x8)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x11, 0x8)
    SetChrPos(0x102, -1900, 0, -24400, 90)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x102, 0x40)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x12, 0x40)
    SetChrChipByIndex(0x8, 5)
    SetChrChipByIndex(0x9, 5)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x10, 0x40)
    OP_0D()
    Sleep(700)
    OP_28(0x8, 0x1, 0x4)

    ChrTalk(
        0xA,
        "好，到此为止。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "训练结束。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#007F好疼啊…………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x15, 400)

    ChrTalk(
        0x102,
        (
            "#017F我们输了。\x02\x03",
            "太大意了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "呼～呼～呼……\x01",
            "终、终于结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "我已经一步都走不动了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(
        0xA,
        "斯科特，你怎么能这么说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "假如这是真正的战斗，\x01",
            "现在下一批敌人就已经出现了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 0)
    TurnDirection(0x9, 0xA, 400)

    ChrTalk(
        0x8,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "…………是，队长说的是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "……斯科特、哈罗德。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "你们觉得现在的自己\x01",
            "能够保护市民的安全吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "你们需要\x01",
            "好好地反省自己。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0)
    TurnDirection(0x8, 0xA, 400)

    ChrTalk(
        0x8,
        "对、对不起。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE5")

    label("loc_BE5")


    ChrTalk(
        0xA,
        (
            "嗯，今天的事就不要放在心上了，\x01",
            "以后努力完成任务吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    FadeToDark(3000, 0, -1)
    OP_28(0x8, 0x1, 0x4000)
    NewScene("ED6_DT01/T0510   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_0_66 end

    def Function_1_C5C(): pass

    label("Function_1_C5C")

    OP_6B(2800, 6000)
    Return()

    # Function_1_C5C end

    def Function_2_C66(): pass

    label("Function_2_C66")

    OP_6D(-1600, 0, -22400, 6000)
    Return()

    # Function_2_C66 end

    def Function_3_C78(): pass

    label("Function_3_C78")

    Sleep(500)
    OP_90(0x8, 0xFFFFFDA8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(340)
    OP_90(0x8, 0xFFFFFDA8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(330)
    OP_90(0x8, 0xFFFFFDA8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(340)
    OP_90(0x8, 0xFFFFFDA8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(335)
    OP_90(0x8, 0xFFFFFDA8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_3_C78 end

    def Function_4_CF6(): pass

    label("Function_4_CF6")

    Sleep(700)
    OP_90(0x9, 0xFFFFFDA8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x9, 0xFFFFFDA8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x9, 0xFFFFFDA8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x9, 0xFFFFFDA8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x9, 0xFFFFFDA8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_4_CF6 end

    def Function_5_D74(): pass

    label("Function_5_D74")

    Sleep(550)
    OP_90(0x102, 0x258, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x102, 0x258, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x102, 0x258, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x102, 0x258, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x102, 0x258, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_5_D74 end

    def Function_6_DF2(): pass

    label("Function_6_DF2")

    Sleep(550)
    OP_90(0x101, 0x258, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x101, 0x258, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x101, 0x258, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x101, 0x258, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x101, 0x258, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_6_DF2 end

    SaveToFile()

Try(main)
