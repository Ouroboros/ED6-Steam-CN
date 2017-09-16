from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T2101_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2101.x',
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
        "Function_1_10CD",         # 01, 1
        "Function_2_29D5",         # 02, 2
        "Function_3_2A03",         # 03, 3
        "Function_4_2A33",         # 04, 4
        "Function_5_2A4F",         # 05, 5
        "Function_6_2A6B",         # 06, 6
        "Function_7_2A87",         # 07, 7
        "Function_8_3000",         # 08, 8
        "Function_9_36F0",         # 09, 9
        "Function_10_42E7",        # 0A, 10
    )


    def Function_0_66(): pass

    label("Function_0_66")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_222")
    OP_28(0x21, 0x1, 0x2000)

    ChrTalk(
        0xFE,
        "哟，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "关于委托的事情有点不好意思，\x01",
            "因为钥匙我已经找到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊，是这样啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "果然就掉在\x01",
            "『亚克罗萨』附近。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样的话，\x01",
            "我就把委托撤销了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真的很抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，没关系的。\x01",
            "反正钥匙找到就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是啊，现在我就放心了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(
        0xFE,
        (
            "那如果以后钥匙又丢掉的话，\x01",
            "我会和你们再联络的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F……拜托你保管好吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_10C9")

    label("loc_222")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x200)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x8000)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_362")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_293")

    ChrTalk(
        0x101,
        (
            "#000F您好啊，哈古先生。\x02\x03",
            "我们有件事想问问您……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35B")

    label("loc_293")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FF")

    ChrTalk(
        0x102,
        (
            "#010F您正在工作啊，打扰了。\x02\x03",
            "有件事情想请教您。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35B")

    label("loc_2FF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35B")

    ChrTalk(
        0x105,
        (
            "#040F对不起，哈古先生。\x02\x03",
            "有件事情想向您打听一下……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35B")

    Call(1, 1)
    Jump("loc_10C9")

    label("loc_362")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B7C")
    EventBegin(0x0)
    OP_28(0x21, 0x4, 0x4)
    OP_28(0x21, 0x4, 0x8)
    OP_28(0x21, 0x1, 0x1)
    OP_28(0x21, 0x1, 0x2)
    LoadEffect(0x0, "map\\\\mp022_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 41040, -6550, 32140, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_414")

    ChrTalk(
        0x101,
        (
            "#000F打扰一下。\x02\x03",
            "叔叔您是叫哈古吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49D")

    label("loc_414")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_466")

    ChrTalk(
        0x102,
        (
            "#010F对不起，打扰了。\x02\x03",
            "请问您是哈古先生吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49D")

    label("loc_466")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49D")

    ChrTalk(
        0x105,
        (
            "#040F对不起，\x01",
            "请问您是哈古先生吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49D")

    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "我就是哈古没错……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0xFE,
        (
            "啊！\x01",
            "难道你们是游击士！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(
        0x101,
        "#006F嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F您好像把仓库的钥匙弄丢了吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "嗯，是呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不久之前，\x01",
            "我把起重机周围的\x01",
            "那些木桶都搬进了仓库……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "似乎在搬完折返的途中，\x01",
            "钥匙就不见了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_6DD")
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F……嗯？\x01",
            "起重机周围的木桶？\x02\x03",
            "#002F喂，约修亚。\x01",
            "那个该不会是……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F嗯，对啊。\x02\x03",
            "是那个卡片上所写的可疑的木桶吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(
        0x102,
        (
            "#010F…………对不起，\x01",
            "请继续说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哦，好的。\x02",
    )

    CloseMessageWindow()

    label("loc_6DD")


    ChrTalk(
        0xFE,
        (
            "我记得\x01",
            "在『亚克罗萨』里喝酒的时候，\x01",
            "钥匙还好好地带在身上的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想很可能\x01",
            "就掉在这附近。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_801")

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "我知道的线索差不多就是这些了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们会作为参考的。\x02\x03",
            "那么，如果有什么新的发现，\x01",
            "我们会再与您联络的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哦，拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "回头见。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    TalkEnd(0xF)
    Jump("loc_B79")

    label("loc_801")


    ChrTalk(
        0xFE,
        (
            "因为刚才心情很愉快，\x01",
            "就在这儿周围散步，\x01",
            "可能就是那个时候弄丢了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0xFE, 0)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F！？\x02\x03",
            "喝醉酒之后\x01",
            "还在海港这里走来走去？\x02\x03",
            "如果掉进海里那可怎么办啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "没办法啊，\x01",
            "海风吹得我心情很好嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        "#007F唉，真是无话可说。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9C3")

    ChrTalk(
        0x105,
        "#045F……说的是呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9EF")

    label("loc_9C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9EF")

    ChrTalk(
        0x136,
        "#045F……说的是呢。\x02",
    )

    CloseMessageWindow()

    label("loc_9EF")


    ChrTalk(
        0xFE,
        (
            "因为这样的原因，\x01",
            "应该就是掉在这个海港的某处了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯，那就只有在这附近转转，\x01",
            "看看能不能找到了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F说得没错。\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "我不能再在这儿偷懒了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(
        0xFE,
        (
            "那么我就去继续工作了。\x01",
            "如果找到了就通知我一声！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F如果有什么新的发现，\x01",
            "我们会再与您联络的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "哦，拜托了。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    TalkEnd(0xF)

    label("loc_B79")

    Jump("loc_10C9")

    label("loc_B7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C2")
    EventBegin(0x0)
    OP_4A(0xF, 255)
    OP_28(0x21, 0x4, 0x10)
    OP_28(0x21, 0x1, 0x20)
    OP_3F(0x334, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE8")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C12")

    ChrTalk(
        0x101,
        (
            "#000F哈古先生，\x01",
            "打扰一下可以吗？\x02\x03",
            "是关于钥匙的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "对了，怎么样了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE5")

    label("loc_C12")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7D")

    ChrTalk(
        0x102,
        "#010F您正在工作啊，打扰了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哦，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "对了，那件事怎么样了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE5")

    label("loc_C7D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE5")

    ChrTalk(
        0x105,
        (
            "#040F对不起，哈古先生。\x01",
            "打扰一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哦，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "对了，那件事怎么样了……\x02",
    )

    CloseMessageWindow()

    label("loc_CE5")

    Jump("loc_E6B")

    label("loc_CE8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA0")

    ChrTalk(
        0x101,
        "#508F呀嗬～哈古先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "喂、喂！         \x01",
            "你太大声了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "会被我的同事听到的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊……对、对不起。\x02\x03",
            "可是，钥匙那件事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哦，对了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_E6B")

    label("loc_DA0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E07")

    ChrTalk(
        0x102,
        "#010F您正在工作啊，打扰了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哦，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "对了，那件事怎么样了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_E6B")

    label("loc_E07")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6B")

    ChrTalk(
        0x105,
        (
            "#040F对不起，哈古先生。\x01",
            "打扰一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哦，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "对了，那件事怎么样了……\x02",
    )

    CloseMessageWindow()

    label("loc_E6B")


    ChrTalk(
        0x101,
        (
            "#006F嗯，已经找到了。\x02\x03",
            "是这把钥匙吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "仓库的钥匙\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "哦，\x01",
            "就是它就是它。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀～辛苦你们了。\x01",
            "真是帮了我大忙啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……可是这钥匙\x01",
            "怎么会被钓鱼线缠住的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F啊哈哈，\x01",
            "这个的原因嘛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯……算了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好了，那就这样吧。\x01",
            "谢谢了哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【仓库的钥匙】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x8000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10BD")

    ChrTalk(
        0x102,
        (
            "#014F啊，对不起。\x02\x03",
            "我们有件事想问问您。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)
    Call(1, 1)

    label("loc_10BD")

    EventEnd(0x1)
    Jump("loc_10C9")

    label("loc_10C2")

    TalkEnd(0xF)
    Call(0, 6)

    label("loc_10C9")

    TalkEnd(0xF)
    Return()

    # Function_0_66 end

    def Function_1_10CD(): pass

    label("Function_1_10CD")

    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(
        0xFE,
        "问我？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们想问问您\x01",
            "刚才钥匙掉了的时候您所说的那件事。\x02\x03",
            "『把起重机周围的那些木桶\x01",
            "　都搬进了仓库』……\x02\x03",
            "……是这样的吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "啊，对呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "起重机附近的\x01",
            "木桶很碍事的，\x01",
            "所以我就把它们搬进仓库里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "之后没多久\x01",
            "钥匙就丢失了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对不起，\x01",
            "能不能让我们进一下仓库呢？\x02\x03",
            "我们有点事情，\x01",
            "想调查一下里面的木桶。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔……使用中的仓库\x01",
            "在出入管理方面是很严格的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为那是一个\x01",
            "放置着很多商品的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以外部人员\x01",
            "是不能随意进出的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F哎呀…………\x01",
            "这可就不好办了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "既然你们刚才帮过我，\x01",
            "我就稍微通融一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就只是调查一下\x01",
            "相关的木桶对吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F嗯，就是这样的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "那么我就把它\x01",
            "搬到仓库外来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样既不用进入仓库，\x01",
            "又可以调查木桶了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#508F啊，对啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F真是给您添麻烦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们不用这么客气。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好了，那么我们就去吧。\x02",
    )

    CloseMessageWindow()
    Fade(2000)
    OP_6C(135000, 0)

    def lambda_15A6():
        OP_6D(23520, 1000, 4150, 4000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_15A6)
    SetChrPos(0xFE, 23520, 1000, 4150, 180)
    OP_51(0x10, 0x1, (scpexpr(EXPR_PUSH_LONG, 0x5BE0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x1036), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x102, 180, 0)
    OP_51(0x101, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x101, 180, 0)
    OP_51(0x105, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12C), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x105, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x105, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC80), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x105, 180, 0)
    OP_0D()
    Sleep(2000)
    OP_6F(0x15, 0)
    OP_70(0x15, 0x3C)
    OP_73(0x15)
    OP_6F(0x15, 60)
    Sleep(1000)

    def lambda_16A9():
        OP_6D(22780, 0, 5890, 2000)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_16A9)
    OP_8C(0xFE, 0, 400)
    Sleep(400)
    OP_90(0xFE, 0x0, 0x0, 0x3E8, 0x3E8, 0x0)
    WaitChrThread(0x18, 0x1)

    ChrTalk(
        0xFE,
        "#1P好，打开了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1P你们就先在这里\x01",
            "等我一下吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_171E():
        OP_6D(23920, 500, 4380, 2000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_171E)
    ClearChrFlags(0x18, 0x80)
    OP_8E(0x18, 0x5BF4, 0x3E8, 0xFA0, 0x3E8, 0x0)
    ClearChrFlags(0x18, 0x4)
    OP_4A(0x18, 255)
    WaitChrThread(0x10, 0x1)
    OP_8C(0xFE, 180, 400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0xFE,
        "#1P咦？波尔多斯主任。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1P您在这里面\x01",
            "做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#2P唔，我只是有点不放心，\x01",
            "所以来看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#2P我用备用钥匙进去的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1P啊？备用钥匙？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1P奇怪了，\x01",
            "有这样的东西吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#2P……对了，\x01",
            "那边的几位是？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)

    ChrTalk(
        0xFE,
        "#1P啊，他们是游击士协会的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1P因为要调查一件事，\x01",
            "所以要看看仓库里面的木桶。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#2P哦，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#2P不过，保管中的仓库\x01",
            "是不允许外部人员进入的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 180, 400)

    ChrTalk(
        0xFE,
        (
            "#1P嗯，所以我才来\x01",
            "帮他们把木桶取出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1P只是把木桶搬出来\x01",
            "应该可以吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#2P啊，那就没问题了。\x01",
            "要协助调查嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#2P唔，\x01",
            "竟然可以找到这个地方来啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#2P虽然还很年轻，\x01",
            "不过你们都是很优秀的游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1P#001F嘿嘿⊙\x01",
            "您过奖了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#2P如果有什么不明白的，\x01",
            "尽管问哈古就是了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#2P那么我就先告辞了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1P辛苦您了。\x02",
    )

    CloseMessageWindow()

    def lambda_1BC7():

        label("loc_1BC7")

        TurnDirection(0xFE, 0x18, 0)
        OP_48()
        Jump("loc_1BC7")

    QueueWorkItem2(0xFE, 1, lambda_1BC7)

    def lambda_1BD8():

        label("loc_1BD8")

        TurnDirection(0x101, 0x18, 0)
        OP_48()
        Jump("loc_1BD8")

    QueueWorkItem2(0x101, 1, lambda_1BD8)

    def lambda_1BE9():

        label("loc_1BE9")

        TurnDirection(0x102, 0x18, 0)
        OP_48()
        Jump("loc_1BE9")

    QueueWorkItem2(0x102, 1, lambda_1BE9)

    def lambda_1BFA():

        label("loc_1BFA")

        TurnDirection(0x105, 0x18, 0)
        OP_48()
        Jump("loc_1BFA")

    QueueWorkItem2(0x105, 1, lambda_1BFA)
    SetChrFlags(0x18, 0x40)
    OP_8E(0x18, 0x6E0A, 0x0, 0x215C, 0x7D0, 0x0)
    OP_8E(0x18, 0x73B4, 0x3E8, 0x3840, 0x7D0, 0x0)
    SetChrFlags(0x18, 0x80)
    OP_44(0xFE, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x105, 0x1)

    def lambda_1C4D():
        OP_8C(0x0, 180, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1C4D)

    def lambda_1C5B():
        OP_8C(0x1, 180, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1C5B)

    def lambda_1C69():
        OP_8C(0x2, 180, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1C69)
    OP_8C(0xFE, 0, 400)
    Sleep(400)

    def lambda_1C83():
        OP_8C(0x0, 180, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1C83)

    def lambda_1C91():
        OP_8C(0x1, 180, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1C91)
    OP_8C(0x2, 180, 400)

    ChrTalk(
        0xFE,
        (
            "#1P好了，\x01",
            "我这就帮你们把木桶拿出来吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(23740, 0, 5560, 0)
    OP_72(0x1D, 0x4)
    OP_71(0x1D, 0x2)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, 23550, 500, 4740, 180)
    OP_8C(0x101, 180, 0)
    OP_8C(0x102, 180, 0)
    OP_8C(0x105, 180, 0)
    OP_8C(0xFE, 180, 0)
    Sleep(800)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(800)
    OP_94(0x1, 0xFE, 0xB4, 0x12C, 0x3E8, 0x0)
    OP_4A(0xFE, 255)
    ClearChrFlags(0xFE, 0x40)
    Sleep(400)
    OP_8C(0xFE, 0, 400)

    ChrTalk(
        0xFE,
        "#1P呼～～久等了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1P你们要的木桶已经拿来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哇～～\x01",
            "还真不小呢～\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1DD5():
        OP_6D(24500, 1000, 3980, 2000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1DD5)
    OP_43(0x102, 0x1, 0x1, 0x2)
    OP_43(0x105, 0x1, 0x1, 0x3)
    OP_43(0xFE, 0x1, 0x1, 0x4)
    OP_8E(0x101, 0x5FDC, 0x1F4, 0x1266, 0x3E8, 0x0)
    OP_8C(0x101, 270, 400)
    WaitChrThread(0x10, 0x1)
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(
        0x101,
        (
            "#000F#1P您一个人就能把它搬出来啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "#1P呵呵，对我们这些海港男儿来说，\x01",
            "这都是些家常便饭啦。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)
    OP_63(0x102)
    Sleep(800)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#014F#2P艾丝蒂尔，\x01",
            "这里又有一张卡片。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_1F1A():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1F1A)

    def lambda_1F28():
        TurnDirection(0x105, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1F28)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#004F#1P啊，真的吗！？\x02",
    )

    CloseMessageWindow()

    def lambda_1F59():
        OP_6D(23220, 500, 4740, 1000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1F59)
    OP_43(0x101, 0x1, 0x1, 0x6)
    OP_8C(0x102, 45, 400)
    OP_8C(0x105, 180, 400)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x10, 0x1)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "『唔，十分抱歉。\x01",
            "　木桶被运走是我的失误。\x01",
            "　\x01",
            "　不过，一旦找到仓库的钥匙，\x01",
            "　就可以顺藤摸瓜找到这里。\x01",
            "　看来你们已经揭示出了真相。\x01",
            "　\x01",
            "　作为奖赏，寻找的物品将完璧归赵。\x01",
            "　你们调查这个木桶之中即可。\x01",
            "　如果可以的话，\x01",
            "　务必将烛台归还给其真正的主人。\x01",
            "　\x01",
            "　……嗯，时间已到。\x01",
            "　期待我们的再次相会。\x01",
            "　　　　　　　　　　　　　　怪盗Ｂ』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#003F#1P真、真是讨厌啊……\x02\x03",
            "就好像是从很近的地方\x01",
            "一直观察着我们的行动一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#043F的确是这样呢…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#014F#2P咦，这张卡片……\x02\x03",
            "……上面的墨迹还没有干。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x105,
        "#044F#4P#1K…………！？\x02",
    )


    ChrTalk(
        0x101,
        "#004F#1P#1K哎！？\x02",
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()
    SetChrPos(0x18, 31010, 0, 9300, 119)
    ClearChrFlags(0x18, 0x80)

    def lambda_22D7():
        OP_6D(25540, 0, 5950, 2000)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_22D7)
    OP_8E(0x18, 0x7170, 0x0, 0x196E, 0x7D0, 0x0)
    OP_8C(0x18, 270, 0)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8E(0x18, 0x672A, 0x0, 0x1932, 0xBB8, 0x0)
    Sleep(400)

    ChrTalk(
        0x18,
        (
            "喂，\x01",
            "你们在这里做什么！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2385():
        TurnDirection(0x0, 0x18, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2385)

    def lambda_2393():
        TurnDirection(0x1, 0x18, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2393)

    def lambda_23A1():
        TurnDirection(0x2, 0x18, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_23A1)
    TurnDirection(0xFE, 0x18, 400)

    ChrTalk(
        0xFE,
        (
            "啊！？\x01",
            "波、波尔多斯主任。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "刚才您不是\x01",
            "已经同意了吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x18,
        "？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "你在说什么？\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x102,
        "#012F#2P糟糕，被骗了。\x02",
    )

    CloseMessageWindow()

    def lambda_248A():
        OP_6D(24290, 500, 4740, 1000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_248A)

    def lambda_24A2():
        TurnDirection(0x105, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_24A2)

    def lambda_24B0():
        TurnDirection(0x18, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_24B0)

    def lambda_24BE():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_24BE)
    TurnDirection(0x101, 0x102, 400)
    WaitChrThread(0x10, 0x1)

    ChrTalk(
        0x101,
        (
            "#004F#1P难、难道是！\x02\x03",
            "刚才在这里的波尔多斯主任……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F#2P是假扮的…………\x01",
            "虽然相貌非常相似。\x02\x03",
            "犯人变装之后把卡片的内容更换了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#043F#4P怎么会…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#1P赶、赶快追上去啊！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_25FB():

        label("loc_25FB")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_25FB")

    QueueWorkItem2(0xFE, 1, lambda_25FB)

    def lambda_260C():

        label("loc_260C")

        TurnDirection(0x18, 0x101, 0)
        OP_48()
        Jump("loc_260C")

    QueueWorkItem2(0x18, 1, lambda_260C)

    def lambda_261D():

        label("loc_261D")

        TurnDirection(0x105, 0x101, 0)
        OP_48()
        Jump("loc_261D")

    QueueWorkItem2(0x105, 1, lambda_261D)

    def lambda_262E():

        label("loc_262E")

        TurnDirection(0x102, 0x101, 0)
        OP_48()
        Jump("loc_262E")

    QueueWorkItem2(0x102, 1, lambda_262E)

    def lambda_263F():
        OP_8E(0x101, 0x745E, 0x208, 0x32F0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_263F)
    OP_62(0x18, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    ChrTalk(
        0x105,
        (
            "#044F#4P啊！\x01",
            "艾丝蒂尔！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0xFE, 0x1)
    OP_44(0x18, 0x1)

    ChrTalk(
        0x102,
        "#014F#2P竟然就这样追上去了……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(
        0x105,
        (
            "#042F#4P约修亚，\x01",
            "我们怎么办！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(
        0x102,
        (
            "#013F#2P虽然很遗憾，\x01",
            "不过已经太迟了。\x02\x03",
            "那个伪装者离开的时候\x01",
            "我们就已经输了。\x02\x03",
            "#015F#2P大概艾丝蒂尔\x01",
            "连犯人的影子也看不到吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#043F是……这样啊…………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(
        0x102,
        (
            "#012F#2P更重要的是，\x01",
            "要先确认一下烛台是否还完好。\x01",
            "　\x02\x03",
            "与逮捕犯人相比，\x01",
            "委托人更希望能够找回烛台。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#042F嗯，是啊。\x02\x03",
            "按照卡片写的，\x01",
            "应该就在这个木桶里面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P嗯，\x01",
            "但愿真是如此。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28A4():
        OP_8E(0x18, 0x6144, 0x0, 0x1AF4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_28A4)

    def lambda_28BF():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28BF)
    Sleep(400)

    def lambda_28D2():
        OP_8C(0x102, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_28D2)
    OP_8E(0x105, 0x5B9A, 0x1F4, 0x12A2, 0x3E8, 0x0)
    OP_8C(0x105, 180, 400)
    Sleep(800)
    OP_62(0x18, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x18, 0x1)
    Sleep(800)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#018F#2P唉，真是的……\x02\x03",
            "艾丝蒂尔赶快回来吧……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0xFE, 4620, -1800, 22750, 270)
    OP_4B(0xF, 255)
    SetChrFlags(0x18, 0x80)
    OP_71(0x1D, 0x4)
    OP_28(0x20, 0x1, 0x200)
    NewScene("ED6_DT01/T2210   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    TalkEnd(0xF)
    Return()

    # Function_1_10CD end

    def Function_2_29D5(): pass

    label("Function_2_29D5")

    OP_8E(0x102, 0x57E4, 0x3E8, 0xF96, 0x3E8, 0x0)
    OP_8C(0x102, 90, 400)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Return()

    # Function_2_29D5 end

    def Function_3_2A03(): pass

    label("Function_3_2A03")

    OP_8E(0x105, 0x582A, 0x0, 0x14D2, 0x3E8, 0x0)
    OP_8E(0x105, 0x587A, 0xFA, 0x1342, 0x3E8, 0x0)
    OP_8C(0x105, 135, 400)
    Return()

    # Function_3_2A03 end

    def Function_4_2A33(): pass

    label("Function_4_2A33")

    OP_8E(0xFE, 0x5C08, 0x0, 0x19FA, 0x3E8, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_4_2A33 end

    def Function_5_2A4F(): pass

    label("Function_5_2A4F")

    OP_8E(0x102, 0x588E, 0x2EE, 0x11BC, 0x7D0, 0x0)
    OP_8C(0x102, 90, 400)
    Return()

    # Function_5_2A4F end

    def Function_6_2A6B(): pass

    label("Function_6_2A6B")

    OP_8E(0x101, 0x5D3E, 0x1F4, 0x1266, 0x7D0, 0x0)
    OP_8C(0x101, 225, 400)
    Return()

    # Function_6_2A6B end

    def Function_7_2A87(): pass

    label("Function_7_2A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B76")
    OP_8B(0x0, 0xA06E, 0x86A6, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AFC")

    ChrTalk(
        0x101,
        (
            "#002F（虽然很在意，\x01",
            "　不过现在不赶快去仓库的话……！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B70")

    label("loc_2AFC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B70")

    ChrTalk(
        0x102,
        (
            "#012F（没有时间再去别的地方了。）\x01",
            "　\x02\x03",
            "（……赶快去最深处的仓库吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B70")

    TalkEnd(0xFF)
    Jump("loc_2FFF")

    label("loc_2B76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_2C33")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x332)"), scpexpr(EXPR_END)), "loc_2B90")
    Call(1, 8)
    Jump("loc_2C30")

    label("loc_2B90")


    ChrTalk(
        0x101,
        "#003F唔～掉进水里的到底是什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F如果可以的话最好调查一下，\x01",
            "可是不知道该从何做起啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F如果有什么带钩的工具，\x01",
            "就可以把它捞出来了吧……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_2C30")

    Jump("loc_2FFF")

    label("loc_2C33")

    EventBegin(0x0)
    OP_28(0x21, 0x1, 0x4)
    OP_62(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_8B(0x0, 0xA050, 0x420351EC, 0x190)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C9F")

    ChrTalk(
        0x101,
        (
            "#004F…………咦？\x02\x03",
            "刚才那里好像有什么东西在发光……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D13")

    label("loc_2C9F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CE0")

    ChrTalk(
        0x102,
        (
            "#014F…………嗯？\x02\x03",
            "好像有什么东西在发光……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D13")

    label("loc_2CE0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D13")

    ChrTalk(
        0x105,
        (
            "#044F啊…………\x02\x03",
            "刚才好像有什么东西在发光？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D13")

    Fade(1000)
    SetChrPos(0x101, 41040, -1650, 31310, 0)
    SetChrPos(0x102, 42040, -1650, 31230, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2D5B")
    SetChrPos(0x105, 40040, -1650, 31130, 0)
    Jump("loc_2D79")

    label("loc_2D5B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2D79")
    SetChrPos(0x136, 40040, -1650, 31130, 0)

    label("loc_2D79")

    OP_6D(41040, -1650, 31830, 0)
    OP_6C(135000, 0)
    OP_0D()
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F哎呀，果然，\x01",
            "水里面好像有东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F亮闪闪的东西，是什么呢。\x02\x03",
            "有可能是哈古先生想找的东西，\x01",
            "如果可以的话最好调查一下……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2ED1")

    ChrTalk(
        0x105,
        (
            "#043F可是，该怎么做呢？\x02\x03",
            "虽说跳下去看可能太夸张了点，\x01",
            "但如果不确认一下的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯～是啊。\x02\x03",
            "如果有什么带钩的工具就好了……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FEE")

    label("loc_2ED1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2F71")

    ChrTalk(
        0x136,
        (
            "#043F可是，该怎么做呢？\x02\x03",
            "虽说跳下去看可能太夸张了点，\x01",
            "但如果不确认一下的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯～是啊。\x02\x03",
            "如果有什么带钩的工具就好了……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FEE")

    label("loc_2F71")


    ChrTalk(
        0x101,
        (
            "#505F可是，该怎么做呢？\x02\x03",
            "虽说跳下去看可能太夸张了点，\x01",
            "不确认一下的话……\x02\x03",
            "如果有什么带钩的工具就好了……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x332)"), scpexpr(EXPR_END)), "loc_2FFD")
    Call(1, 8)
    Jump("loc_2FFF")

    label("loc_2FFD")

    EventEnd(0x0)

    label("loc_2FFF")

    Return()

    # Function_7_2A87 end

    def Function_8_3000(): pass

    label("Function_8_3000")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 41040, -1650, 31430, 0)
    SetChrPos(0x102, 42040, -1650, 31230, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_304A")
    SetChrPos(0x105, 40040, -1650, 31130, 0)
    Jump("loc_3068")

    label("loc_304A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3068")
    SetChrPos(0x136, 40040, -1650, 31130, 0)

    label("loc_3068")

    OP_6D(41040, -1650, 31830, 0)
    OP_6C(135000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x101,
        "#003F唔～掉进水里的到底是什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F如果可以的话最好调查一下，\x01",
            "可是不知道该从何做起啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F如果有什么带钩的工具，\x01",
            "就可以把它捞出来了吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F啊，对了！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    Fade(1000)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(25000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 41040, -2000, 31900, 0)
    SetChrChipByIndex(0x101, 15)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x101,
        "#001F怎～么样？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014F原来如此。\x01",
            "是用钓钩把它钩上来吗？\x02\x03",
            "可是很不容易做到啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F嘿嘿嘿，\x01",
            "现在就让你识一下\x01",
            "艾丝蒂尔姐姐华丽的技巧吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F好吧好吧。\x01",
            "我就等着你的表演。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_32F6")
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#040F艾丝蒂尔，加油！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#508F哦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3342")

    label("loc_32F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3342")
    TurnDirection(0x136, 0x101, 400)

    ChrTalk(
        0x136,
        "#040F艾丝蒂尔，加油！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#508F哦！\x02",
    )

    CloseMessageWindow()

    label("loc_3342")

    Sleep(100)
    Fade(1000)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    SetChrSubChip(0x101, 0)
    OP_0D()
    OP_22(0x84, 0x0, 0x64)
    OP_99(0x101, 0x0, 0x6, 0x5DC)
    Sleep(400)
    OP_22(0x19, 0x0, 0x64)
    Sleep(1200)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x101)
    Sleep(700)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_44(0x101, 0xFF)
    OP_99(0x101, 0x6, 0x3, 0x5DC)
    OP_82(0x0, 0x0)
    OP_84(0x0)
    OP_22(0x18, 0x0, 0x64)
    OP_99(0x101, 0x3, 0x1, 0x5DC)
    Sleep(1000)
    OP_99(0x101, 0x10, 0x12, 0x5DC)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "仓库的钥匙\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_96(0x101, 0xA050, 0xFFFFF98E, 0x7AC6, 0x258, 0xBB8)
    ClearChrFlags(0x101, 0x4)
    Sleep(400)

    def lambda_3469():
        OP_94(0x1, 0x101, 0x0, 0xFFFFFED4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3469)
    Fade(1000)
    OP_6D(41040, -1650, 31830, 0)
    OP_6C(135000, 0)
    OP_0D()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#508F你看你看！钓到了哦！\x02",
    )

    CloseMessageWindow()
    OP_3E(0x334, 1)
    OP_28(0x21, 0x1, 0x10)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014F艾丝蒂尔，你好厉害。\x02\x03",
            "真没想到你居然对这个也如此在行。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#009F哼，\x01",
            "听你的语气好像不是在称赞我吧。\x02\x03",
            "#000F不过，运气不错呢。\x01",
            "这个好像就是哈古\x01",
            "先生所说的仓库的钥匙。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 0, 400)

    ChrTalk(
        0x102,
        (
            "#010F呵呵，\x01",
            "竟然掉到这里来了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_365B")

    ChrTalk(
        0x105,
        (
            "#040F呵呵，\x01",
            "这样子哈古先生也可以安心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36AC")

    label("loc_365B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_36AC")

    ChrTalk(
        0x136,
        (
            "#040F呵呵，\x01",
            "这样子哈古先生也可以安心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36AC")


    ChrTalk(
        0x101,
        (
            "#000F我们把它交给哈古先生吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F嗯，对啊。\x02",
    )

    CloseMessageWindow()
    OP_64(0x0, 0x1)
    EventEnd(0x0)
    Return()

    # Function_8_3000 end

    def Function_9_36F0(): pass

    label("Function_9_36F0")

    OP_28(0x20, 0x1, 0x8000)
    OP_28(0x20, 0x1, 0x20)
    OP_64(0x1, 0x1)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 20100, 0, 28900, 270)
    SetChrPos(0x102, 21200, 0, 29300, 270)
    SetChrPos(0x105, 22300, 0, 27900, 270)
    OP_6C(315000, 0)
    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x10, 0x7D0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#002F唔……\x02\x03",
            "真奇怪啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F#2P所谓『钢铁之鹤』应该\x01",
            "就是指这个起重机吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F不过却没看到最重要的『木桶』啊……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F可恶，\x01",
            "到底怎么回事嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x101, 0x15, 400)

    ChrTalk(
        0x101,
        "#501F啊，那边那位大哥！\x02",
    )

    CloseMessageWindow()

    def lambda_3898():
        TurnDirection(0x102, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3898)

    def lambda_38A6():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_38A6)
    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x10, 0x7D0)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x15, 0x101, 400)
    OP_4A(0x15, 255)

    ChrTalk(
        0x15,
        "哦，有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F你在这附近看到过木桶吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "木桶？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "那种东西\x01",
            "我也记不太清楚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "不过每一个仓库里面都有木桶。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x15, 255)
    OP_8C(0x15, 270, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3CE2")
    OP_28(0x20, 0x1, 0x100)

    ChrTalk(
        0x101,
        (
            "#505F#1P唔，这样啊……\x02\x03",
            "…………嗯？仓库？\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x10, 0x7D0)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x105, 0x101, 400)

    def lambda_3A81():
        TurnDirection(0x102, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A81)

    ChrTalk(
        0x105,
        "#044F有什么发现吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#505F#1P嗯…………\x01",
            "等一下。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#002F喂，\x01",
            "我们之前不是找到过仓库的钥匙吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F#2P嗯…………\x01",
            "哈古先生曾经委托过我们帮他找钥匙。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F#1P那个人不是说过的吗？\x02\x03",
            "起重机周围的那些木桶\x01",
            "都被搬进仓库里面去了…………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x102,
        (
            "#014F#2P对啊…………\x02\x03",
            "原来这里的木桶\x01",
            "都被搬运到仓库里面去了。\x02\x03",
            "#010F一定是这样没错。\x01",
            "头脑很灵敏嘛，艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#001F#1P嘿嘿，偶尔啦。\x02\x03",
            "好，\x01",
            "我们这就去问问哈古先生吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42E4")

    label("loc_3CE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_406A")
    OP_28(0x20, 0x1, 0x80)

    ChrTalk(
        0x101,
        (
            "#505F#1P唔，这样啊……\x02\x03",
            "……嗯？仓库？\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x10, 0x7D0)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x105, 0x101, 400)

    def lambda_3DA3():
        TurnDirection(0x102, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3DA3)

    ChrTalk(
        0x105,
        "#044F有什么发现吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#505F#1P嗯…………\x01",
            "等一下。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#002F#1P我说，\x01",
            "之前我们不是听说过吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P嗯……\x01",
            "哈古先生曾经委托过我们帮他找钥匙。\x01",
            "　\x02\x03",
            "仓库的钥匙丢失了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F#1P是啊是啊。\x01",
            "那个人不是说过吗？\x02\x03",
            "起重机周围的那些木桶\x01",
            "都被搬进仓库里面去了…………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x102,
        (
            "#014F#2P对啊…………\x02\x03",
            "原来这里的木桶\x01",
            "都被搬运到仓库里面去了。\x02\x03",
            "#010F一定是这样没错。\x01",
            "头脑很灵敏嘛，艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#001F#1P嘿嘿，偶尔啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P好，\x01",
            "那么我们先把哈古先生的委托解决掉吧。\x02\x03",
            "这样的话，\x01",
            "事情就应该有所进展了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#508F哦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_42E4")

    label("loc_406A")

    OP_28(0x20, 0x1, 0x40)

    ChrTalk(
        0x101,
        (
            "#505F#1P是吗……\x02\x03",
            "唉，真是不好办啊。\x01",
            "线索就这样中断了。\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x10, 0x7D0)

    def lambda_410E():
        TurnDirection(0x105, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_410E)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#013F#2P如果有关于木桶的消息就好了。\x01",
            "　\x02\x03",
            "可是我们目前\x01",
            "也没有这方面的线索呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#003F#1P可是，\x01",
            "在这种地方发愁也没有用……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P不如我们先去接受其他的任务吧？\x01",
            "　\x02\x03",
            "说不定会得到什么线索呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#1P嗯，就这样办吧。\x02\x03",
            "当然，这件事也不能放弃，\x01",
            "要继续调查下去啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P是啊。\x02\x03",
            "好，我们走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42E4")

    EventEnd(0x0)
    Return()

    # Function_9_36F0 end

    def Function_10_42E7(): pass

    label("Function_10_42E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x334)"), scpexpr(EXPR_END)), "loc_4950")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47E3")
    OP_A2(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4498")
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x332)"), scpexpr(EXPR_END)), "loc_439F")

    ChrTalk(
        0x102,
        (
            "#014F我说，艾丝蒂尔。\x02\x03",
            "说起来，\x01",
            "还没有把仓库的钥匙交给哈古先生吧。\x02\x03",
            "#010F而且钓鱼竿也还没有还回去呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43F2")

    label("loc_439F")


    ChrTalk(
        0x102,
        (
            "#014F我说，艾丝蒂尔。\x02\x03",
            "说起来，\x01",
            "还没有把仓库的钥匙交给哈古先生吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43F2")

    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        "#008F啊，忘得一干二净了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F出发之前去还了吧。\x01",
            "哈古先生肯定正在港口工作吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，好啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_47E0")

    label("loc_4498")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4634")
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x332)"), scpexpr(EXPR_END)), "loc_453B")

    ChrTalk(
        0x102,
        (
            "#014F啊，说起来……\x02\x03",
            "还没有把仓库的钥匙交给哈古先生吧。\x01",
            "　\x02\x03",
            "#010F而且钓鱼竿也还没有还回去呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_458E")

    label("loc_453B")


    ChrTalk(
        0x102,
        (
            "#014F啊，说起来……\x02\x03",
            "还没有把仓库的钥匙交给哈古先生吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_458E")

    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        "#008F啊，忘得一干二净了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F出发之前去还了吧。\x01",
            "哈古先生应该在港口那里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，好啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_47E0")

    label("loc_4634")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47E0")
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x332)"), scpexpr(EXPR_END)), "loc_46D7")

    ChrTalk(
        0x102,
        (
            "#014F啊，说起来……\x02\x03",
            "还没有把仓库的钥匙交给哈古先生吧。\x01",
            "　\x02\x03",
            "#010F而且钓鱼竿也还没有还回去呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_472A")

    label("loc_46D7")


    ChrTalk(
        0x102,
        (
            "#014F啊，说起来……\x02\x03",
            "还没有把仓库的钥匙交给哈古先生吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_472A")

    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        "#008F啊，忘得一干二净了……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#044F那么就先去哈古先生那里吧……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(
        0x102,
        (
            "#010F嗯，对啊。\x01",
            "哈古先生应该正在港口。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47E0")

    Jump("loc_4932")

    label("loc_47E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4860")
    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#010F出发之前，\x01",
            "把仓库的钥匙交给哈古先生把。\x02\x03",
            "哈古先生应该在港口那里的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4932")

    label("loc_4860")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48B8")

    ChrTalk(
        0x102,
        (
            "#010F先把仓库的钥匙交给哈古先生，\x01",
            "然后再出发吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4932")

    label("loc_48B8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4932")
    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#010F先把仓库的钥匙交给哈古先生，\x01",
            "然后再出发吧。\x02\x03",
            "哈古先生应该在港口那里的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4932")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_4AC3")

    label("loc_4950")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x332)"), scpexpr(EXPR_END)), "loc_4AC3")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A45")
    OP_A2(0x0)

    ChrTalk(
        0x102,
        (
            "#010F对了，\x01",
            "从酒吧借的钓鱼竿还没还，\x02\x03",
            "出发之前去还了吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F嗯～\x01",
            "是在港口的酒吧借来的吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(
        0x105,
        "#040F嗯，是『亚克罗萨』啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4AA8")

    label("loc_4A45")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#010F从港口的酒吧借来的钓鱼竿还没还。\x01",
            "　\x02\x03",
            "出发之前去还了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AA8")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_4AC3")

    Return()

    # Function_10_42E7 end

    SaveToFile()

Try(main)
