from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T0120_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0120.x',
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
        "Function_1_6CC",          # 01, 1
        "Function_2_112D",         # 02, 2
        "Function_3_157D",         # 03, 3
    )


    def Function_0_66(): pass

    label("Function_0_66")

    OP_A2(0x228)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_305")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_266")

    ChrTalk(
        0x8,
        (
            "哟，这不是\x01",
            "近来很活跃的两位游击士新人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "最近到处都能听到\x01",
            "你们努力工作的事迹哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F是吗，不过我们还只是新手啦。\x01",
            "还需要拼命加油呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哈哈，有前途啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过你们来得\x01",
            "还真是时候，\x01",
            "我有急事要拜托你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在米尔西街道上的\x01",
            "导力灯需要找人去更换，\x01",
            "怎么样，你们愿意接受这工作吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 1)
    Jump("loc_302")

    label("loc_266")


    def lambda_26C():
        TurnDirection(0x0, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_26C)
    TurnDirection(0x1, 0x8, 400)

    ChrTalk(
        0x8,
        (
            "哟，\x01",
            "艾丝蒂尔、约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "更换导力灯的工作\x01",
            "你们要接受吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_2FE")
    Call(1, 2)
    Jump("loc_302")

    label("loc_2FE")

    Call(1, 1)

    label("loc_302")

    Jump("loc_6C1")

    label("loc_305")


    ChrTalk(
        0x8,
        "有什么事吗？\x02",
    )

    CloseMessageWindow()

    label("loc_32E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BE")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【确认路灯的解锁密码】\x01",      # 0
            "【取消委托任务】\x01",            # 1
            "【没什么事】\x01",                # 2
        )
    )

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_3BC"),
        (1, "loc_4FA"),
        (2, "loc_692"),
        (SWITCH_DEFAULT, "loc_692"),
    )


    label("loc_3BC")


    ChrTalk(
        0x8,
        (
            "需要交换的是城西\x01",
            "米尔西街道的第六号路灯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是从靠洛连特这边街道\x01",
            "开始数的第六个路灯哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "控电盘的解锁密码是\x01",
            "『５４４８１８』。\x01",
            "……不要忘记了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "那么就拜托你们了。\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_6BB")

    label("loc_4FA")

    OP_28(0x6, 0x3, 0x8)
    OP_28(0x6, 0x1, 0x8000)

    ChrTalk(
        0x101,
        (
            "#003F实在是对不起，佛莱迪叔叔，\x01",
            "我们突然有很急的事情要办……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是这样啊。\x01",
            "那就没办法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "既然如此，那就把用于\x01",
            "更换的导力灯还给我好了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了\x07\x02",
            "导力灯\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x327, 1)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "办完事情后，\x01",
            "请马上通知我一声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "我这边的事情也很急啊。\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_6BB")

    label("loc_692")


    ChrTalk(
        0x8,
        "那么就拜托你们了。\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_6BB")

    label("loc_6BB")

    Jump("loc_32E")

    label("loc_6BE")

    OP_5F(0x0)

    label("loc_6C1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_66 end

    def Function_1_6CC(): pass

    label("Function_1_6CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1122")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_731"),
        (1, "loc_1024"),
        (SWITCH_DEFAULT, "loc_1024"),
    )


    label("loc_731")

    OP_28(0x6, 0x4, 0x8)
    OP_28(0x6, 0x4, 0x4)
    OP_28(0x6, 0x4, 0x2)
    OP_28(0x6, 0x1, 0x1)
    OP_28(0x6, 0x1, 0x2)

    ChrTalk(
        0x101,
        "#006F嗯，就交给我们吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F很高兴您能\x01",
            "把这个任务交给我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "谢谢了，真是帮大忙了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "差点忘了说，\x01",
            "今天就是任务的最后期限哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那么，\x01",
            "先把这个重要的东西交给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "导力灯\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x327, 1)
    Sleep(100)

    ChrTalk(
        0x101,
        "#000F这就是用作更换的导力灯吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "啊，对呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "需要交换的是城西\x01",
            "米尔西街道的第六号路灯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是从靠洛连特这边街道\x01",
            "开始数的第六个路灯哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "不要弄错了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，没问题。\x02\x03",
            "城西米尔西街道，\x01",
            "从洛连特方向开始数的第六个路灯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "找到那个路灯后，\x01",
            "就把灯上配备的控电盘打开。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "控电盘打开后，\x01",
            "还需要输入六位数的解锁密码。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是啊，六号路灯的密码是\x01",
            "『５４４８１８』哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#008F对，对不起佛莱迪叔叔。\x01",
            "再说一遍好吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F『５４４８１８』对吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "完全一致，\x01",
            "不愧是约修亚啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#009F哼。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x8,
        (
            "输入数字之后控电盘就能打开了，\x01",
            "之后更换掉里面的导力器就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "可能你们觉得这很简单，\x01",
            "但是千万不能太大意了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "路灯有可能\x01",
            "很早之前就已经坏掉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此。\x02\x03",
            "#010F导力灯发出的光，\x01",
            "具有能驱赶\x01",
            "大型魔兽的效果。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "不过也只能达到\x01",
            "让人稍感安心的程度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "因此，如果坏掉了，\x01",
            "说不定会发生什么意外。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "把这件事委托给\x01",
            "游击士去解决，\x01",
            "是基于以防万一的考虑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "说起来路灯就是设置在\x01",
            "魔兽频繁出现的道路旁啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F哎呀，魔兽来的话，\x01",
            "我啪啪几下就收拾得干干净净了……\x02\x03",
            "那个密码什么的不用纸记下来\x01",
            "倒是很容易忘记。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F这样的话，\x01",
            "输入密码的工作可以交给我来办。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x8,
        "具体分工就由你们自己决定吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "好了，我已经把相关的注意事项都说明了，\x01",
            "那么就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果还有什么需要确认的，\x01",
            "或者想取消任务，\x01",
            "就再到这里来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_111C")

    label("loc_1024")

    OP_28(0x6, 0x1, 0x8000)

    ChrTalk(
        0x101,
        (
            "#505F抱歉啊，佛莱迪叔叔，\x01",
            "我们还有其他事情要做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是这样啊。\x01",
            "那就没办法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "办完事情后，\x01",
            "请马上通知我一声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "我这边的事情也很急啊。\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_111C")

    label("loc_111C")

    OP_5F(0x0)
    Jump("Function_1_6CC")

    label("loc_1122")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_6CC end

    def Function_2_112D(): pass

    label("Function_2_112D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156F")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_1192"),
        (1, "loc_145B"),
        (SWITCH_DEFAULT, "loc_145B"),
    )


    label("loc_1192")

    OP_28(0x6, 0x4, 0x8)

    ChrTalk(
        0x101,
        (
            "#006F嗯，刚才的事情已经办完了，\x01",
            "这件工作就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我再次说明一下，\x01",
            "先把这个交给你们。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "导力灯\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x327, 1)
    Sleep(100)

    ChrTalk(
        0x8,
        "再次确认这次任务的要点……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "需要交换的是城西\x01",
            "米尔西街道的第六号路灯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是从靠洛连特这边街道\x01",
            "开始数的第六个路灯哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "控电盘的解锁密码是\x01",
            "『５４４８１８』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "……嗯，基本上就这么多了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "好了，那么\x01",
            "接下来就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果还有什么需要确认的，\x01",
            "或者想取消任务，\x01",
            "就再到这里来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_156C")

    label("loc_145B")

    OP_28(0x6, 0x1, 0x8000)

    ChrTalk(
        0x101,
        (
            "#003F实在是对不起，佛莱迪叔叔，\x01",
            "我们还有一些事情要办。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是这样啊。\x01",
            "那就没办法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "办完事情后，\x01",
            "请马上通知我一声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "我这边的事情也很急啊。\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_156C")

    label("loc_156C")

    Jump("Function_2_112D")

    label("loc_156F")

    OP_5F(0x0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_112D end

    def Function_3_157D(): pass

    label("Function_3_157D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1593")
    Jump("loc_15BB")

    label("loc_1593")


    ChrTalk(
        0x8,
        "看到这句话就表示有Ｂｕｇ发生。\x02",
    )

    CloseMessageWindow()

    label("loc_15BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B39")
    EventBegin(0x0)
    OP_28(0x6, 0x4, 0x10)
    OP_28(0x6, 0x1, 0x10)

    ChrTalk(
        0x101,
        "#001F呀嗬～佛莱迪叔叔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哟，是艾丝蒂尔啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "从你的表情来看，\x01",
            "事情已经顺利完成了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#006F嗯⊙\x01",
            "还算顺利。\x02\x03",
            "……虽然还是发生了一些小事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F为了慎重起见，\x01",
            "先向佛莱迪先生汇报吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "米尔西街道的事件汇报完毕。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "哦……果然是出故障了啊。\x01",
            "一定是因为更换日期太迟了的缘故。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "实在是抱歉。\x01",
            "因为我的疏忽让你们遇到了危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F没关系的，\x01",
            "不用道歉啦。\x02\x03",
            "#000F这是我们份内的事情嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F工作中的危险\x01",
            "也是我们游击士应该承担的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "谢谢啊。\x01",
            "有你这句话我就放心了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "……对了，请收下这个，\x01",
            "以表我的歉意。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了\x07\x02",
            "妨害２\x07\x00",
            "的结晶回路。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x2C2, 1)
    Sleep(100)

    ChrTalk(
        0x101,
        "#004F这是，结晶回路？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "没错，妨害２的结晶回路。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "它可以在对方\x01",
            "准备发出魔法时中止其发动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果能熟练使用的话，\x01",
            "这东西可是很有用的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F劳您费心了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        "哪里哪里，是我感谢你们两个才对啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "有什么关于导力器的问题的话\x01",
            "就随时找我来谈好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "以后我们工房的生意\x01",
            "还要请你们多多关照啦。\x02",
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
            "任务【更换路灯】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x1)
    Jump("loc_1BC8")

    label("loc_1B39")


    ChrTalk(
        0x8,
        (
            "有什么关于导力器的问题的话\x01",
            "就随时找我来谈好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "以后我们工房的生意\x01",
            "还要请你们多多关照啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC8")

    Return()

    # Function_3_157D end

    SaveToFile()

Try(main)
