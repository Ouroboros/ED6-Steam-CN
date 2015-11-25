from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4134   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4134.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        '修女艾伦',                             # 9
        '尤莉亚中尉',                           # 10
        '男人的声音',                           # 11
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01410 ._CH',             # 00
        'ED6_DT06/CH20112 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01410P._CP',             # 00
        'ED6_DT06/CH20112P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_12E",          # 01, 1
        "Function_2_12F",          # 02, 2
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_12D")
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_12D")

    Return()

    # Function_0_11A end

    def Function_1_12E(): pass

    label("Function_1_12E")

    Return()

    # Function_1_12E end

    def Function_2_12F(): pass

    label("Function_2_12F")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_6D(80, 0, -470, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -30, 1000, 17550, 180)
    SetChrPos(0x9, -30, 1000, 17550, 0)
    SetChrPos(0x102, 10, 0, 450, 0)
    SetChrPos(0x101, -360, -250, -3700, 0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(500, 0)
    OP_8E(0x101, 0xFFFFFDF8, 0x0, 0xFFFFFACE, 0x7D0, 0x0)
    Sleep(500)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#012F……不好意思，艾丝蒂尔。\x02\x03",
            "好像是我搞错了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎……？\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "女性的声音",
        (
            "#3P……呵呵。\x01",
            "你们果然来了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_295():
        OP_6D(-290, 1000, 16930, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_295)
    WaitChrThread(0x101, 0x2)
    Fade(1000)
    OP_6D(10, 8100, 16470, 0)
    OP_6C(0, 0)
    OP_6E(582, 0)
    OP_67(0, 3500, -10000, 0)
    OP_6B(1490, 0)
    SetChrPos(0x101, -510, 0, 9550, 0)
    SetChrPos(0x102, 500, 0, 9640, 0)
    OP_6D(0, 500, 16500, 3000)

    ChrTalk(
        0x102,
        "#012F您是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F你难道是……\x01",
            "在周游道遇到过的修女小姐！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那个时候\x01",
            "真是谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "凭那封信的内容就来到这里，\x01",
            "你们俩的胆量和智慧真值得嘉许。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F那封信，是修女小姐写的啊……\x01",
            "　\x02\x03",
            "可是，你到底为什么要\x01",
            "做出这么耐人寻味的事情呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F原来如此……终于明白了。\x01",
            "　\x02\x03",
            "#010F原来是您啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "呵呵……\x01",
            "约修亚真是敏锐啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那么，不好意思……\x01",
            "我要把这件闷热的衣服脱掉。\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)

    def lambda_50B():
        OP_6D(10, 500, 19000, 1000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_50B)
    OP_8C(0x8, 90, 400)
    OP_8C(0x8, 0, 400)
    OP_22(0xCB, 0x0, 0x64)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_8C(0x9, 270, 400)
    OP_8C(0x9, 180, 400)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#004F#5S啊啊！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_579():
        OP_8E(0xFE, 0xFFFFFFEC, 0x0, 0x3232, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_579)

    def lambda_594():
        OP_67(0, 5010, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_594)
    OP_6D(-10, 0, 12730, 3000)
    WaitChrThread(0x9, 0x1)

    ChrTalk(
        0x9,
        (
            "#460F我是王室亲卫队独立中队长，\x01",
            "尤莉亚·舒华兹中尉。\x02\x03",
            "很久不见了。\x01",
            "艾丝蒂尔、约修亚。\x02\x03",
            "我相信你们一定会来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F很久不见了，尤莉亚中尉。\x02\x03",
            "自从在卢安的飞艇坪分别之后\x01",
            "就没有再见过面呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#461F嗯……是啊。\x02\x03",
            "呵呵，明明没过多长时间，\x01",
            "感觉却像很久之前的事情了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F等、等一下……\x02\x03",
            "为什么尤莉亚小姐\x01",
            "会装扮成这个样子呢？\x02\x03",
            "而且……\x01",
            "为什么要把我们叫到这个地方来呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#460F我一个一个回答好了。\x02\x03",
            "首先，这个装扮……\x01",
            "七耀教会和利贝尔王家\x01",
            "很久以前就有很深厚的关系了。\x02\x03",
            "由于理查德上校的阴谋，\x01",
            "我们亲卫队不得不过着逃亡的生活，\x01",
            "幸亏得到了教会的诸多帮助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#460F另外一个问题……\x01",
            "叫你们来其实是想拜托你们一件事。\x02\x03",
            "如果你们在明天的决赛中获胜，\x01",
            "就能被款待入王城参加晚餐会对吧？\x02\x03",
            "那个时候，我希望你们能和\x01",
            "在格兰赛尔城里的女王陛下会面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#464F我知道这个请求可能有些自私。\x02\x03",
            "但我们现在被王国军通缉中，\x01",
            "所以是不可能潜入王城里去的。\x02\x03",
            "只能拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F……那个。\x01",
            "还真是巧合啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们就是为了与女王陛下见面\x01",
            "才参加这次武术大会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#463F哎……？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔和约修亚向尤莉亚说明了\x01",
            "雷斯顿要塞的事情和接受拉赛尔博士的委托\x01",
            "要向女王传言的情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x9,
        (
            "#463F原来有这样的事啊……\x02\x03",
            "#465F啊啊～女神啊。\x01",
            "感谢您伟大的慈悲……\x02\x03",
            "这样的话，\x01",
            "我要拜托你们的事情就只有一件了。\x02\x03",
            "#460F希望你们能和深陷困境的陛下好好谈谈。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，本来就打算这么做啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F虽然协会有不干涉国家内政的规约，\x01",
            "但对目前的事态也是不能袖手旁观的。\x02\x03",
            "我们会在允许的范围内\x01",
            "尽自己所能去完成您的委托的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#461F实在是太感谢你们了……\x02\x03",
            "那么，你们拿上这个吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x9, 0xFFFFFF7E, 0x0, 0x2972, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "尤莉亚的介绍信\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x36C, 1)
    OP_8F(0x9, 0xFFFFFFD8, 0x0, 0x2EA4, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        "#505F这是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#460F#5P这是给城里的女官长\x01",
            "希尔丹夫人的介绍信。\x02\x03",
            "#465F陛下现在大概还在\x01",
            "那些特务兵的严密监视之下……\x02\x03",
            "贴身服侍的希尔丹夫人\x01",
            "应该能想出办法让你们见到陛下的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F哎～还有这样的人啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我知道了。\x01",
            "进城后我们就去找她商量一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#460F#5P拜托你们了。\x02\x03",
            "#465F呼呼……真是羞愧啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#464F#5P被那些人设下的无耻奸计陷害，\x01",
            "无法守护身边重要的人，这种屈辱……\x02\x03",
            "明明向上天发过誓就算拼上性命也要\x01",
            "讨伐奸贼、救出陛下……\x01",
            "　\x02\x03",
            "可这次不得不借用你们的力量，\x01",
            "这个没用的我还真是可悲啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F不、不要这样责备自己啊……\x01",
            "　\x02\x03",
            "#007F而且，明天的比赛\x01",
            "我们也有输掉的可能性呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#461F#5P呵呵……\x01",
            "你们一定没有问题的。\x02\x03",
            "那个来自东方的武术家\x01",
            "也拥有相当厉害的身手……\x02\x03",
            "而且不管怎么说，\x01",
            "你们毕竟是卡西乌斯上校的孩子啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004F哎～？\x01",
            "尤莉亚小姐也认识老爸吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#465F#5P卡西乌斯上校作为王国军的智囊，\x01",
            "同时又是被称为『剑圣』的最强剑士……\x02\x03",
            "#460F从王国军退役之前，\x01",
            "受邀担当了士官学校的武术教官。\x02\x03",
            "所以，他可以说是我的剑术老师。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F真、真是难以置信……\x01",
            "老爸明明只使用棒术的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#465F#5P我听说，他退伍成为游击士的时候，\x01",
            "就放弃了用剑。\x02\x03",
            "这样做不是单单为了杀敌，\x01",
            "更是为了坚守自己的信念去惩强扶弱……\x02\x03",
            "#460F正因为抱着这样一种精神，\x01",
            "所以他选择了棒术作为守护别人的武器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F原来是这样啊……\x02\x03",
            "棒术原来有这样的含义啊……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F而且，\x01",
            "这种精神已经被你完全地继承下来了呢。\x02\x03",
            "我觉得这是你应该引以为荣的东西。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#008F约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#460F#5P你们是上校培养和锻炼出来的。\x02\x03",
            "我相信你们一定会取得胜利的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15D0():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15D0)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x101,
        (
            "#506F嘿嘿……\x01",
            "尤莉亚小姐也这么说了，\x01",
            "我也感觉自信更强了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们会全力以赴的。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xA, 0, 0, 1870, 0)
    OP_22(0x72, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_16C8():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16C8)

    def lambda_16D6():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16D6)

    def lambda_16E4():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_16E4)
    OP_6D(0, 0, 9920, 1000)

    NpcTalk(
        0xA,
        "男人的声音",
        "#5P……对不起，我们是王都警卫队！\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "男人的声音",
        (
            "#5P作为恐怖活动的应付对策之一，\x01",
            "我们正在进行主要设施的巡视工作。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "男人的声音",
        (
            "#5P很抱歉，这么晚了还来打扰，\x01",
            "不过能不能让我们进去呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F（糟了……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#461F啊……真是辛苦你们了。\x02\x03",
            "请稍等一下，\x01",
            "我这就去开门。\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)

    def lambda_187B():
        OP_6D(-10, 0, 12730, 1000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_187B)

    def lambda_1893():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1893)
    TurnDirection(0x101, 0x9, 400)
    OP_8C(0x9, 90, 600)
    OP_8C(0x9, 0, 600)
    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0x9, 0)
    OP_8C(0x9, 270, 600)
    OP_8C(0x9, 180, 600)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#5P（祭坛房间那边有通往外面的后门。）\x01",
            "　\x02\x03",
            "（你们从那里离开吧。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F（知、知道了！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F（尤莉亚中尉，您也要小心啊。）\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_197F")
    Jump("loc_19BA")

    label("loc_197F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x2000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_199A")
    OP_2B(0x45, 0x1)
    Jump("loc_19BA")

    label("loc_199A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x1000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x800)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_19B5")
    OP_2B(0x45, 0x3)
    Jump("loc_19BA")

    label("loc_19B5")

    OP_2B(0x45, 0x5)

    label("loc_19BA")

    OP_A2(0x3FD)
    NewScene("ED6_DT01/T4151   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_12F end

    SaveToFile()

Try(main)
