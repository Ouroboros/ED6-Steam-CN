from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T1131_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T1131.x',
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


    ChrTalk(
        0xFE,
        "哎呀，有什么事吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB")

    ChrTalk(
        0x101,
        (
            "#508F谢谢惠顾～\x02\x03",
            "这是您委托游击士协会的东西～\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187")

    label("loc_DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F")

    ChrTalk(
        0x102,
        (
            "#010F您是格露娜小姐吧。\x02\x03",
            "我们给您送东西来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187")

    label("loc_12F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_187")

    ChrTalk(
        0x103,
        (
            "#020F您是格露娜小姐吧。\x02\x03",
            "我们给您送东西来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_187")

    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了５个\x07\x02",
            "魔兽鸟肉\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x3A7, 5)

    ChrTalk(
        0xFE,
        (
            "啊，真是太感谢了，\x01",
            "还让你们特地跑了一趟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们很忙吧，\x01",
            "给你们添麻烦了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F没有啦，完全没那回事。\x02\x03",
            "帮助有困难的人，\x01",
            "是我们游击士的工作嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F对，艾丝蒂尔说得没错。\x02\x03",
            "而且现在还正处于\x01",
            "定期船停航的非常时期。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(
        0xFE,
        (
            "谢谢你们，\x01",
            "这样说让我宽心了不少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "用金钱并不足以表达我的谢意……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0xFE,
        "………………对了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "请你们再接受\x01",
            "我的一份谢礼好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊？是什么？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "我把我们店里最受欢迎的一道菜——\x01",
            "『王国煎蛋卷』的制作方法教给你们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F我们店，\x01",
            "是指这个安特洛丝餐厅吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，当然了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F这样好吗？\x01",
            "把料理的菜谱告诉我们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不用担心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "即使知道菜谱，\x01",
            "也不一定能做出原汁原味的哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xFE, 400)

    ChrTalk(
        0x103,
        "#020F很有自信嘛。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(
        0xFE,
        (
            "呵呵，因为这不仅是\x01",
            "精不精通于做菜的问题哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "打个比方，\x01",
            "就好像乐谱和音乐家的关系一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "同样的乐谱也会因为演奏者的不同，\x01",
            "而产生不一样的效果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F呼～真是深奥啊～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "菜谱是最终制作出\x01",
            "美味菜肴的条件之一。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们可以保持原有的简单配料，\x01",
            "然后去尝试改变它的味道，\x01",
            "说不定会有意想不到的效果哦。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_822")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0xC)"), scpexpr(EXPR_END)), "loc_7F4")
    Jump("loc_822")

    label("loc_7F4")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "学会了\x07\x02",
            "王国煎蛋卷\x07\x00",
            "的做法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_822")

    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#001F哈哈㈱　太好了～\x02\x03",
            "好，\x01",
            "我马上就试着做做看吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#018F……………………\x02\x03",
            "……艾丝蒂尔，拜托，\x01",
            "你能不能把菜谱仔细研究之后再做？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#005F你、你这是什么话～\x02\x03",
            "岂有此理，\x01",
            "你好像在说我不会做饭一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F你这样说的话，\x01",
            "就更要好好注意调味料的量才行啊。\x02\x03",
            "因为艾丝蒂尔你\x01",
            "经常一放就是一大堆呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#009F哼。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "好啦好啦，制作方法固然重要，\x01",
            "不过最重要的还是能享受美味的料理吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说不定品尝之后\x01",
            "就能知道其中的诀窍了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(
        0x101,
        (
            "#001F嗯，的确是这样⊙\x02\x03",
            "谢谢你给我们这么多指点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "彼此彼此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "请你们有空也到本店\x01",
            "品尝其他美味的料理哦。\x02",
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
            "任务【收集食物材料】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x12, 0x4, 0x10)
    OP_A2(0xA)
    OP_28(0x12, 0x1, 0x1)
    TalkEnd(0x11)
    Return()

    # Function_0_66 end

    SaveToFile()

Try(main)
