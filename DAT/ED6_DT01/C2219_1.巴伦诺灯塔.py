from ED6ScenarioHelper import *

def main():
    # 巴伦诺灯塔

    CreateScenaFile(
        FileName            = 'C2219_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C2210.x',
        MapIndex            = 84,
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
        "Function_1_2014",         # 01, 1
        "Function_2_3966",         # 02, 2
        "Function_3_398E",         # 03, 3
        "Function_4_39B6",         # 04, 4
        "Function_5_39DE",         # 05, 5
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1308")
    OP_28(0x1D, 0x4, 0x10)
    OP_28(0x1D, 0x1, 0x80)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    Fade(1000)
    SetChrPos(0x101, -970, 0, 201500, 270)
    SetChrPos(0x102, -120, 0, 201000, 270)
    SetChrPos(0x105, 330, 0, 202500, 270)
    OP_69(0x8, 0x3E8)
    TalkBegin(0x8)

    ChrTalk(
        0x101,
        (
            "#001F谢谢惠顾～\x01",
            "这是给您送来的东西～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯？\x01",
            "你们不是前些时候的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿，好久不见了。\x02\x03",
            "#006F今天我们是为了任务而来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F从游击士协会接到的委托，\x01",
            "把维修工具箱给您送来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F没错，请收下。\x01",
            "啊，要小心，比较重。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
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
        0x8,
        "唔，没错，就是这个。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那么大老远的跑来，\x01",
            "真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x19A)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6E2")

    ChrTalk(
        0x101,
        (
            "#000F没有啦，小事一桩。\x02\x03",
            "比起这个，\x01",
            "城里的人们也都很关心老人家您呢。\x02\x03",
            "工作这么辛苦，\x01",
            "一定要保重身体才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "唔～真是谢谢他们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……你们现在也总算明白了\x01",
            "这种为某人某事操心的艰难了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嗯，怎么说好呢。\x02\x03",
            "虽然明白这些道理，\x01",
            "不过要做好果然还是挺难的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没关系，慢慢来，\x01",
            "总有一天可以做到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "当然，\x01",
            "现在还是差得很远呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……就这样吧。\x01",
            "今天真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也该继续工作了。\x01",
            "还要进行定期检查呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F好吧。\x01",
            "多多保重了，老爷爷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F打扰了。\x02",
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
            "任务【运送维修工具箱】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    EventEnd(0x0)
    TalkEnd(0x8)
    Jump("loc_1305")

    label("loc_6E2")


    ChrTalk(
        0x101,
        (
            "#000F没有啦，小事一桩。\x02\x03",
            "而且我们今天\x01",
            "还带了其他的东西来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哦？\x02",
    )

    CloseMessageWindow()
    OP_90(0x105, 0xFFFFFCE0, 0x0, 0x0, 0x7D0, 0x0)
    OP_92(0x105, 0x8, 0x3E8, 0x7D0, 0x0)

    ChrTalk(
        0x105,
        (
            "#040F弗科特老爷爷，请收下。\x02\x03",
            "这是『拉旺塔尔』的\x01",
            "普莱米奥老板捎给您的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 400)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "亚瑟利亚葡萄酒\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x19A, 1)
    OP_28(0x1D, 0x1, 0x20)
    OP_91(0x105, 0x190, 0x0, 0x190, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        (
            "哦哦！\x01",
            "这不是『亚瑟利亚葡萄酒』吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "让我回忆起了\x01",
            "以前用辣鳀鱼作为下酒菜，\x01",
            "通宵痛饮的时代啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x391)"), scpexpr(EXPR_END)), "loc_B0A")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【交出辣鳀鱼】\x01",      # 0
            "【什么也不做】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_936"),
        (1, "loc_AAC"),
        (SWITCH_DEFAULT, "loc_B07"),
    )


    label("loc_936")


    ChrTalk(
        0x101,
        (
            "#001F嘿嘿嘿⊙\x01",
            "事实上我们一起带来了的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "辣鳀鱼\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x391, 1)
    OP_28(0x1D, 0x1, 0x40)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x8,
        "哦哦！哦哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "还专门弄来了下酒菜，\x01",
            "真是准备得很周全啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "唉～\x01",
            "真让人怀念啊。\x01",
            "普莱米奥他们还好吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B07")

    label("loc_AAC")

    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "唉，真让人怀念啊，\x01",
            "普莱米奥他们还好吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B07")

    label("loc_B07")

    Jump("loc_B62")

    label("loc_B0A")

    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "唉，真让人怀念啊，\x01",
            "普莱米奥他们还好吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B62")


    ChrTalk(
        0x101,
        (
            "#000F很好的，\x01",
            "大家也都很关心老人家您呢。\x02\x03",
            "工作这么辛苦，\x01",
            "一定要保重身体才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "嗯，你们捎来东西我就已经很感激了，\x01",
            "这么说让我更加感激啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……你们现在\x01",
            "也总算明白了这种\x01",
            "为某人某事操心的艰难了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嗯，怎么说好呢。\x02\x03",
            "虽然明白这些道理，\x01",
            "不过要做好果然还是挺难的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没关系，慢慢来，\x01",
            "你们很快就能做到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "当然，\x01",
            "现在还是差得很远呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……哦，对了。\x01",
            "稍等片刻。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DCB():

        label("loc_DCB")

        TurnDirection(0x102, 0x8, 400)
        OP_48()
        Jump("loc_DCB")

    QueueWorkItem2(0x102, 1, lambda_DCB)

    def lambda_DDC():

        label("loc_DDC")

        TurnDirection(0x101, 0x8, 400)
        OP_48()
        Jump("loc_DDC")

    QueueWorkItem2(0x101, 1, lambda_DDC)

    def lambda_DED():

        label("loc_DED")

        TurnDirection(0x105, 0x8, 400)
        OP_48()
        Jump("loc_DED")

    QueueWorkItem2(0x105, 1, lambda_DED)
    OP_8E(0x8, 0xFFFFF7E0, 0x0, 0x31A38, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFF20E, 0x0, 0x31DBC, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFE8D6, 0x0, 0x31C9A, 0x7D0, 0x0)
    OP_8C(0x8, 315, 0)
    Sleep(1000)
    OP_8E(0x8, 0xFFFFE8D6, 0x0, 0x31C9A, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFF20E, 0x0, 0x31DBC, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFF7E0, 0x0, 0x31A38, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFF7A4, 0x0, 0x3131C, 0x7D0, 0x0)
    TurnDirection(0x8, 0x101, 400)
    OP_44(0x102, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)

    ChrTalk(
        0x8,
        (
            "这是很久以前\x01",
            "我用过的东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "让你们那么辛苦地送东西来，\x01",
            "这就算我的一点心意。\x01",
            "你们就别客气，收下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "虽然有些旧了，\x01",
            "不过品质可是勿庸置疑的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_1048")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "工作安全帽\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "斗魂扎头巾\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x148, 1)
    OP_3E(0x146, 1)
    Jump("loc_1098")

    label("loc_1048")

    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "工作安全帽\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x148, 1)

    label("loc_1098")


    ChrTalk(
        0x101,
        "#001F哇啊，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F这样好吗？\x01",
            "那么珍贵的物品……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "没关系没关系，\x01",
            "反正我也不可能再次出海了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……就这样吧。\x01",
            "今天真是辛苦你们了。\x01",
            "我也该继续工作了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "拿到你们捎来的东西，\x01",
            "我真的非常高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F请您一定要注意身体哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F那么，\x01",
            "多多保重了，老爷爷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们告辞了。\x02",
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
            "任务【运送维修工具箱】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    EventEnd(0x0)
    TalkEnd(0x8)

    label("loc_1305")

    Jump("loc_2013")

    label("loc_1308")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_END)), "loc_17C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1629")
    OP_A2(0x458)
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "噢，是小姑娘你们啊。\x01",
            "昨晚真是谢谢你们了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F老爷爷您才是呢，\x01",
            "已经没事了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "不久前头还稍微有点晕……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "现在已经没事了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F看来麻醉药的作用已经过去了。\x01",
            "　\x02\x03",
            "药本身是无毒的，\x01",
            "这样的话就不用担心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F太好了，\x01",
            "那我就放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好，\x01",
            "那我这就恢复工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F不要太过勉强了。\x02\x03",
            "虽然已经恢复了，\x01",
            "但是毕竟遭遇了那样的惊吓啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔，说的有道理。\x02\x03",
            "那就比平时\x01",
            "多休息一会儿再工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C4")

    label("loc_1629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1720")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "噢，是小姑娘你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "药的效果终于已经过去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "头晕的感觉也已经消失了，\x01",
            "跟平常没什么两样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好吧，\x01",
            "我这就恢复工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C4")

    label("loc_1720")


    ChrTalk(
        0xFE,
        (
            "药的效果\x01",
            "终于已经过去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "跟平常没什么两样了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好吧，\x01",
            "我这就恢复工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C4")

    Jump("loc_2010")

    label("loc_17C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_1C96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9B")
    OP_A2(0x458)
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "噢，是小姑娘你们啊。\x01",
            "昨晚真是谢谢你们了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F老爷爷您才是呢，\x01",
            "已经没事了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，没什么了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "还是稍微有点头晕……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F看来麻醉药的作用\x01",
            "还没有完全消退。\x02\x03",
            "不过这药没有毒，\x01",
            "应该很快就可以恢复的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F太好了，\x01",
            "那我就放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，那么我稍微休息一会儿，\x01",
            "然后再去工作好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，\x01",
            "休息是最重要的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请您千万不要勉强自己。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好吧，\x01",
            "那我这就去休息了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C93")

    label("loc_1A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC7")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "昨天晚上\x01",
            "真是谢谢你们了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过我记不清楚\x01",
            "昨天晚上到底发生过什么事情了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "感觉真的就像\x01",
            "在一瞬间发生的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呜呜……\x01",
            "我的头好像又有点晕了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C93")

    label("loc_1BC7")


    ChrTalk(
        0xFE,
        (
            "昨晚的事情\x01",
            "我怎么也记不清楚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "感觉真的就像\x01",
            "在一瞬间发生的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "我的头好像又有点晕了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C93")

    Jump("loc_2010")

    label("loc_1C96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1ED3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1DAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D30")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "哦，是你们啊。\x01",
            "真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从今往后也要记得\x01",
            "把关心别人放在首位哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DAA")

    label("loc_1D30")


    ChrTalk(
        0xFE,
        (
            "呼，休息一下\x01",
            "就开始进行检查吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀哎呀，\x01",
            "这个工作对腰真是不好啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DAA")

    Jump("loc_1ED0")

    label("loc_1DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E5E")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "哦，是你们啊。\x01",
            "辛苦你们消灭魔兽了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不要忘记关心人的心，\x01",
            "从今往后也要加油啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED0")

    label("loc_1E5E")


    ChrTalk(
        0xFE,
        (
            "好了，\x01",
            "我差不多该去进行定期检查了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在货物运来之前\x01",
            "要去进行工作的准备才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ED0")

    Jump("loc_2010")

    label("loc_1ED3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2010")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F8E")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "哦，是你们啊。\x01",
            "辛苦你们消灭魔兽了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不要忘记关心人的心，\x01",
            "从今往后也要加油啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2010")

    label("loc_1F8E")


    ChrTalk(
        0xFE,
        (
            "好了，\x01",
            "我差不多该去进行定期检查了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在货物运来之前\x01",
            "要去进行工作的准备才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2010")

    TalkEnd(0x8)

    label("loc_2013")

    Return()

    # Function_0_66 end

    def Function_1_2014(): pass

    label("Function_1_2014")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    ClearChrFlags(0x8, 0x80)
    TalkBegin(0x8)
    SetChrPos(0x8, 300, 0, 202000, 180)
    SetChrPos(0x101, 1750, 0, 203500, 180)
    SetChrPos(0x102, 2650, 0, 203000, 180)
    SetChrPos(0x105, 2550, 0, 205000, 180)
    OP_69(0x101, 0x0)
    FadeToBright(2000, 0)

    def lambda_207D():
        OP_8E(0x8, 0xFFFFF7A4, 0x0, 0x3131C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_207D)

    def lambda_2098():
        OP_6D(-970, 0, 201500, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2098)
    OP_43(0x101, 0x1, 0x1, 0x2)
    Sleep(200)
    OP_43(0x102, 0x1, 0x1, 0x3)
    Sleep(200)
    OP_43(0x105, 0x1, 0x1, 0x4)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 270, 400)
    Sleep(400)
    OP_8C(0x8, 270, 400)

    ChrTalk(
        0x8,
        (
            "呼，我这是怎么了，\x01",
            "突然感觉自己\x01",
            "好像离开这里好久了啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，\x01",
            "先把任务完成了吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，说得对呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)
    OP_92(0x101, 0x8, 0x3E8, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        (
            "#001F谢谢惠顾～\x01",
            "这是给您送来的东西～\x02\x03",
            "有点重，要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
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
        0x8,
        "唔，没错，就是这个。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那么大老远的跑来，\x01",
            "真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x19A)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_29C3")

    ChrTalk(
        0x101,
        (
            "#000F没有啦，小事一桩。\x02\x03",
            "比起这个，\x01",
            "城里的人也都很关心老人家您呢。\x02\x03",
            "工作这么辛苦，\x01",
            "一定要保重身体才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "唔～真是谢谢他们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……你们现在也总算明白了这种\x01",
            "为某人某事操心的艰难了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嗯，怎么说好呢。\x02\x03",
            "虽然明白这些道理，\x01",
            "不过要做好果然还是挺难的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "没关系，慢慢来，\x01",
            "总有一天可以做到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "当然，\x01",
            "如果和那位游击士相比，\x01",
            "不足的地方还是很多的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F请问，您说的那位游击士\x01",
            "究竟是个什么样的人呢？\x02\x03",
            "听您刚才那么说，\x01",
            "他好像是个很了不起的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "七八年前，我承蒙过他的关照。\x01",
            "但是很遗憾，我并不知道他的名字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "他可真是一个了不起的男子汉啊。\x01",
            "现在的你们\x01",
            "还是无法和他相提并论的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "唔，但是小姑娘头发的颜色倒是和他很相似，\x01",
            "那个游击士的头发也恰好是\x01",
            "红色中带有一丝茶色。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "……怎么回事，仔细一看，\x01",
            "眼睛的颜色也挺相似的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F……红色的头发，\x01",
            "和艾丝蒂尔相同的眼睛颜色。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F那、那个游击士难道是…………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#044F？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "你们还远远没有\x01",
            "达到他那样的水平啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……把理想定得太高，\x01",
            "就容易忽视一些细小的方面。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 400)

    ChrTalk(
        0x8,
        (
            "哦，话说回来，\x01",
            "今天真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我也该继续工作了。\x01",
            "还要进行定期检查呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊……嗯，那么，\x01",
            "多多保重了，老爷爷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F打扰了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/C2209   ._SN", 101, 0, 0)
    IdleLoop()
    TalkEnd(0x8)
    Jump("loc_395E")

    label("loc_29C3")


    ChrTalk(
        0x101,
        (
            "#000F没有啦，小事一桩。\x02\x03",
            "而且我们今天还\x01",
            "带了其他的东西来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哦？\x02",
    )

    CloseMessageWindow()
    OP_90(0x105, 0xFFFFFCE0, 0x0, 0x0, 0x7D0, 0x0)
    OP_92(0x105, 0x8, 0x3E8, 0x7D0, 0x0)

    ChrTalk(
        0x105,
        (
            "#040F弗科特老爷爷，请收下。\x02\x03",
            "这是『拉旺塔尔』的\x01",
            "普莱米奥老板捎给您的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 400)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "亚瑟利亚葡萄酒\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x19A, 1)
    OP_28(0x1D, 0x1, 0x20)
    OP_91(0x105, 0x190, 0x0, 0x190, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        (
            "哦哦！\x01",
            "这不是『亚瑟利亚葡萄酒』吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "让我回忆起了\x01",
            "以前用辣鳀鱼作为下酒菜，\x01",
            "通宵痛饮的时代啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x391)"), scpexpr(EXPR_END)), "loc_2DF6")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【交出辣鳀鱼】\x01",      # 0
            "【什么也不做】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C22"),
        (1, "loc_2D98"),
        (SWITCH_DEFAULT, "loc_2DF3"),
    )


    label("loc_2C22")


    ChrTalk(
        0x101,
        (
            "#001F嘿嘿嘿⊙\x01",
            "事实上我们一起带来了的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "辣鳀鱼\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x391, 1)
    OP_28(0x1D, 0x1, 0x40)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x8,
        "哦哦！哦哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "还专门弄来了下酒菜，\x01",
            "真是准备得很周全啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "唉～\x01",
            "真让人怀念啊。\x01",
            "普莱米奥他们还好吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF3")

    label("loc_2D98")

    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "唉，真让人怀念啊，\x01",
            "普莱米奥他们还好吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF3")

    label("loc_2DF3")

    Jump("loc_2E4E")

    label("loc_2DF6")

    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "唉，真让人怀念啊，\x01",
            "普莱米奥他们还好吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E4E")


    ChrTalk(
        0x101,
        (
            "#000F很好的，\x01",
            "大家也都很关心老人家您呢。\x02\x03",
            "工作这么辛苦，\x01",
            "一定要保重身体才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "嗯，你们捎来东西我就已经很感激了，\x01",
            "这么说让我更加感激啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……你们现在\x01",
            "也总算明白了这种\x01",
            "为某人某事操心的艰难了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嗯，怎么说好呢。\x02\x03",
            "虽然明白这些道理，\x01",
            "不过要做好果然还是挺难的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "没关系，慢慢来，\x01",
            "总有一天可以做到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "当然，\x01",
            "如果和那位游击士相比，\x01",
            "不足的地方还是比较多的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F请问，您说的那位游击士\x01",
            "究竟是个什么样的人呢？\x02\x03",
            "听您刚才那么说，\x01",
            "他好像是个很了不起的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "七八年前，我承蒙过他的关照。\x01",
            "但是很遗憾，我并不知道他的名字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "他可真是一个了不起的男子汉啊。\x01",
            "现在的你们\x01",
            "还是无法和他相提并论的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "唔，但是小姑娘头发的颜色倒是和他很相似，\x01",
            "那个游击士的头发也恰好是\x01",
            "红色中带有一丝茶色。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "……怎么回事，仔细一看，\x01",
            "眼睛的颜色也挺相似的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F……红色的头发，\x01",
            "和艾丝蒂尔相同的眼睛颜色。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F那、那个游击士难道是…………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#044F？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "你们还远远没有\x01",
            "达到他那样的水平啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……把理想定得太高，\x01",
            "就容易忽视一些细小的方面。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 400)

    ChrTalk(
        0x8,
        (
            "哦，话说回来，\x01",
            "今天真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "除了工作用品，\x01",
            "你们还特地送了这些东西来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……哦，对了。\x01",
            "稍等片刻。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_34AE():

        label("loc_34AE")

        TurnDirection(0x102, 0x8, 400)
        OP_48()
        Jump("loc_34AE")

    QueueWorkItem2(0x102, 1, lambda_34AE)

    def lambda_34BF():

        label("loc_34BF")

        TurnDirection(0x101, 0x8, 400)
        OP_48()
        Jump("loc_34BF")

    QueueWorkItem2(0x101, 1, lambda_34BF)

    def lambda_34D0():

        label("loc_34D0")

        TurnDirection(0x105, 0x8, 400)
        OP_48()
        Jump("loc_34D0")

    QueueWorkItem2(0x105, 1, lambda_34D0)
    OP_8E(0x8, 0xFFFFF7E0, 0x0, 0x31A38, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFF20E, 0x0, 0x31DBC, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFE8D6, 0x0, 0x31C9A, 0x7D0, 0x0)
    OP_8C(0x8, 315, 0)
    Sleep(1000)
    OP_8E(0x8, 0xFFFFE8D6, 0x0, 0x31C9A, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFF20E, 0x0, 0x31DBC, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFF7E0, 0x0, 0x31A38, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFF7A4, 0x0, 0x3131C, 0x7D0, 0x0)
    TurnDirection(0x8, 0x101, 400)
    OP_44(0x102, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)

    ChrTalk(
        0x8,
        (
            "这是很久以前\x01",
            "我用过的东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这就算我的一点心意。\x01",
            "你们就别客气，收下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "虽然有些旧了，\x01",
            "不过品质可是勿庸置疑的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_3739")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "工作安全帽\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "斗魂扎头巾\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x148, 1)
    OP_3E(0x146, 1)
    Jump("loc_3789")

    label("loc_3739")

    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "工作安全帽\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x148, 1)

    label("loc_3789")


    ChrTalk(
        0x101,
        "#001F哇啊，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F这样好吗？\x01",
            "那么珍贵的物品……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "没关系没关系，\x01",
            "反正我也不可能再次出海了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……那么，\x01",
            "我也该继续工作了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "拿到你们捎来的东西，\x01",
            "我真的非常高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F请您一定要注意身体哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F那么，\x01",
            "多多保重了，老爷爷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们告辞了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/C2209   ._SN", 101, 0, 0)
    IdleLoop()
    TalkEnd(0x8)

    label("loc_395E")

    EventEnd(0x0)
    SetMapFlags(0x1)
    Return()

    # Function_1_2014 end

    def Function_2_3966(): pass

    label("Function_2_3966")


    def lambda_396C():
        OP_8E(0x101, 0xFFFFFC36, 0x0, 0x3131C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_396C)
    WaitChrThread(0x101, 0x2)
    OP_8C(0x101, 270, 400)
    Return()

    # Function_2_3966 end

    def Function_3_398E(): pass

    label("Function_3_398E")


    def lambda_3994():
        OP_8E(0x102, 0xFFFFFF88, 0x0, 0x31128, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3994)
    WaitChrThread(0x102, 0x2)
    OP_8C(0x102, 270, 400)
    Return()

    # Function_3_398E end

    def Function_4_39B6(): pass

    label("Function_4_39B6")


    def lambda_39BC():
        OP_8E(0x105, 0x14A, 0x0, 0x31830, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_39BC)
    WaitChrThread(0x105, 0x2)
    OP_8C(0x105, 270, 400)
    Return()

    # Function_4_39B6 end

    def Function_5_39DE(): pass

    label("Function_5_39DE")

    EventBegin(0x1)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽全部消灭干净了！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x1)
    Return()

    # Function_5_39DE end

    SaveToFile()

Try(main)
