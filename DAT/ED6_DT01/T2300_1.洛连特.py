from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T2300_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2300.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        "Function_1_DD4",          # 01, 1
    )


    def Function_0_66(): pass

    label("Function_0_66")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    Fade(1000)
    OP_6C(338000, 0)
    SetChrPos(0x0, -3200, 8000, 44000, 315)
    SetChrPos(0x1, -2000, 8000, 43900, 315)
    SetChrPos(0x2, -2800, 8000, 42500, 315)
    OP_69(0x0, 0x7D0)
    TalkBegin(0xE)
    OP_4A(0xFE, 255)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0xFE,
        "………………啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "请问……\x01",
            "你们是游击士协会的人吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_343")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F")

    ChrTalk(
        0x101,
        (
            "#501F…………嗯？\x02\x03",
            "#000F嗯，正是……\x02\x03",
            "难不成，\x01",
            "你就是阿梅莉娅小姐吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F")

    label("loc_16F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AD")

    ChrTalk(
        0x102,
        (
            "#014F嗯，是的……\x02\x03",
            "您就是阿梅莉娅小姐吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F")

    label("loc_1AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22F")

    ChrTalk(
        0x105,
        (
            "#044F啊，是的。\x02\x03",
            "虽然我不是，\x01",
            "不过这两位确实是游击士。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(
        0x101,
        (
            "#000F哎，难道……\x02\x03",
            "你就是阿梅莉娅小姐吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    label("loc_22F")


    ChrTalk(
        0xFE,
        (
            "啊，我就是。\x01",
            "终于等到你们了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(
        0x102,
        (
            "#010F那就开门见山吧，\x01",
            "您的委托内容是……\x02\x03",
            "护送的任务吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "嗯，是的。\x01",
            "希望你们能够护送我叔父。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "因为他要去古罗尼山道。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D6")

    label("loc_343")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A7")

    ChrTalk(
        0x101,
        (
            "#004F哎？\x02\x03",
            "嗯，然后呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(
        0x102,
        "#010F有什么事吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_463")

    label("loc_3A7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F8")

    ChrTalk(
        0x102,
        (
            "#014F嗯，是的……\x02\x03",
            "#010F有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_463")

    label("loc_3F8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_463")

    ChrTalk(
        0x105,
        (
            "#044F啊，是的。\x02\x03",
            "虽然我不是，\x01",
            "不过这两位确实是游击士。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(
        0x102,
        "#010F有什么事吗？\x02",
    )

    CloseMessageWindow()

    label("loc_463")

    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "嗯，其实……\x01",
            "希望你们能够护送我叔父。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为他要去\x01",
            "古罗尼山道办点事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D6")

    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(
        0x101,
        (
            "#000F古罗尼山道啊。\x02\x03",
            "#508F那么，\x01",
            "最终目的地是柏斯吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "不，不是这样的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他只是单纯地\x01",
            "想到古罗尼山道去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F咦？为什么？\x02\x03",
            "去古罗尼山道……\x01",
            "能有什么事做呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔……\x01",
            "他说是去寻找珍稀的野菜……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对不起，\x01",
            "我也不太明白\x01",
            "叔父所说的意思。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#007F哦…………\x01",
            "是这样啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(
        0x102,
        (
            "#010F那么就向他本人询问一下，\x01",
            "这样更直接。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "嗯，是啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(
        0xFE,
        (
            "请稍等片刻。\x01",
            "我这就去叫他。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xFE, 0xFFFFEA20, 0x2134, 0xB798, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    SetChrFlags(0xFE, 0x40)
    OP_94(0x1, 0xFE, 0x0, 0x9C4, 0xBB8, 0x0)
    OP_72(0x0, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x0, 30)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    SetChrFlags(0xFE, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_7ED")
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#003F看到公告板的时候，\x01",
            "我还以为这次任务比较简单……\x02\x03",
            "为什么突然感觉\x01",
            "事情变得这么怪了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83A")

    label("loc_7ED")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F嗯～\x01",
            "真是不明白呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83A")

    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#043F古罗尼山道是一个相当危险的地方。\x01",
            "　\x02\x03",
            "那样的地方，\x01",
            "为何还要专程前去呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(
        0x102,
        (
            "#010F是啊。\x02\x03",
            "总之还是向他本人\x01",
            "问清楚这件事吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_8C(0x101, 315, 400)

    ChrTalk(
        0x101,
        "#000F……啊，好像来了哦。\x02",
    )

    CloseMessageWindow()

    def lambda_947():
        OP_8C(0x102, 315, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_947)

    def lambda_955():
        OP_8C(0x105, 315, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_955)
    ClearChrFlags(0xFE, 0x8)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_8C(0xFE, 90, 0)
    OP_94(0x1, 0xFE, 0x0, 0x9C4, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_72(0x0, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x0, 30)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    OP_8E(0xFE, 0xFFFFEFFC, 0x1F40, 0xB02C, 0xBB8, 0x0)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(
        0x101,
        (
            "#000F咦？\x01",
            "您的叔父呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "是这样的………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他好像\x01",
            "早就已经出发了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        "#004F啊！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(
        0x102,
        (
            "#014F出发了…………\x02\x03",
            "去了古罗尼山道……是吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "嗯，应该是的。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)

    ChrTalk(
        0xFE,
        (
            "我告诉过他\x01",
            "要等你们一起的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "叔父真是的，\x01",
            "实在是太乱来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F嗯，真让人担心啊。\x02\x03",
            "竟然一个人就跑到\x01",
            "古罗尼山道去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F更何况现在天色越来越暗，\x01",
            "一个人实在很危险啊。\x02\x03",
            "希望他能在天黑之前\x01",
            "赶回来就好了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "唉…………\x01",
            "对不起啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "让你们专程赶来，\x01",
            "结果却白跑了一趟……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F没什么，不用介意。\x01",
            "对我们来说这没关系的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真的很抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "等叔父回来之后，\x01",
            "我会好好和他谈谈的。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x1F, 0x4, 0x4)
    OP_28(0x1F, 0x4, 0x2)
    OP_28(0x1F, 0x1, 0x1)
    OP_28(0x1F, 0x1, 0x2)
    OP_28(0x1F, 0x1, 0x4)
    OP_8E(0xFE, 0xFFFFEA20, 0x2134, 0xB798, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    SetChrFlags(0xFE, 0x40)
    OP_94(0x1, 0xFE, 0x0, 0x9C4, 0xBB8, 0x0)
    OP_72(0x0, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x0, 30)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    SetChrFlags(0xFE, 0x8)
    SetChrFlags(0xFE, 0x80)
    OP_4B(0xFE, 255)
    EventEnd(0x0)
    TalkEnd(0xE)
    Return()

    # Function_0_66 end

    def Function_1_DD4(): pass

    label("Function_1_DD4")

    FadeToBright(2000, 0)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetMapFlags(0x400000)
    OP_6C(270000, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -2780, 8000, 59500, 180)
    SetChrPos(0x101, -1780, 8000, 61500, 180)
    SetChrPos(0x102, -3780, 8000, 62500, 180)
    SetChrPos(0x105, -2780, 8000, 63500, 180)
    OP_6D(-2750, 7990, 58240, 0)

    def lambda_E52():
        OP_6C(315000, 5000)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E52)

    def lambda_E62():
        OP_94(0x1, 0x10, 0x0, 0x1CE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E62)
    Sleep(100)

    def lambda_E7D():
        OP_94(0x1, 0x101, 0x0, 0x2008, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E7D)
    Sleep(50)

    def lambda_E98():
        OP_94(0x1, 0x102, 0x0, 0x2260, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E98)
    Sleep(50)

    def lambda_EB3():
        OP_94(0x1, 0x105, 0x0, 0x21FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EB3)
    OP_0D()
    OP_6D(-2840, 7990, 52900, 4000)
    WaitChrThread(0x10, 0x1)
    TurnDirection(0x10, 0x105, 400)
    Sleep(800)

    ChrTalk(
        0x10,
        "唔，到这里就可以了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "今天真是\x01",
            "承蒙你们的照顾。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_116E")
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0x10,
        (
            "这样吧。\x01",
            "借此难得的机会，\x01",
            "以前的不愉快也都一笔勾销如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "怎么说我和你们\x01",
            "都还算有些缘分啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "如果可以的话，\x01",
            "今后我们\x01",
            "还是做朋友吧……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_102D():
        TurnDirection(0x105, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_102D)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F这样也好……\x01",
            "艾丝蒂尔你觉得呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        (
            "#505F唔…………\x02\x03",
            "既然奥维德先生都这么说了，\x01",
            "那我当然也没问题……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10A8():
        TurnDirection(0x105, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10A8)
    TurnDirection(0x102, 0x10, 400)

    ChrTalk(
        0x102,
        (
            "#019F和解成功……了呢。\x02\x03",
            "#010F那么从现在开始大家就是朋友了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(
        0x10,
        (
            "嗯，听你这么一说，\x01",
            "我也感到很高兴啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x105, 400)

    ChrTalk(
        0x10,
        (
            "那我们就在\x01",
            "下次的工作中再会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11F9")

    label("loc_116E")

    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        "#508F嗯，工作请加油哦。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10, 400)

    ChrTalk(
        0x102,
        (
            "#010F那么，\x01",
            "我们告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "唔，再见。\x01",
            "就在下次的工作中再会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F9")

    OP_8C(0x10, 180, 400)
    SetChrFlags(0x10, 0x40)

    def lambda_120B():

        label("loc_120B")

        TurnDirection(0x101, 0x10, 0)
        OP_48()
        Jump("loc_120B")

    QueueWorkItem2(0x101, 1, lambda_120B)

    def lambda_121C():

        label("loc_121C")

        TurnDirection(0x102, 0x10, 0)
        OP_48()
        Jump("loc_121C")

    QueueWorkItem2(0x102, 1, lambda_121C)

    def lambda_122D():

        label("loc_122D")

        TurnDirection(0x105, 0x10, 0)
        OP_48()
        Jump("loc_122D")

    QueueWorkItem2(0x105, 1, lambda_122D)
    OP_94(0x1, 0x10, 0x0, 0x2328, 0xBB8, 0x0)
    SetChrFlags(0x10, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x105, 0x1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【护送上山的叔父】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_1_DD4 end

    SaveToFile()

Try(main)
