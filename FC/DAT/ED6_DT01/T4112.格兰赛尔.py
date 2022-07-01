from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4112   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4112.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60081",
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
        '奥利维尔',                             # 9
        '穆拉',                                 # 10
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
        'ED6_DT07/CH00030 ._CH',             # 00
        'ED6_DT07/CH02190 ._CH',             # 01
        'ED6_DT07/CH00133 ._CH',             # 02
        'ED6_DT07/CH00035 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH00030P._CP',             # 00
        'ED6_DT07/CH02190P._CP',             # 01
        'ED6_DT07/CH00133P._CP',             # 02
        'ED6_DT07/CH00035P._CP',             # 03
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


    ScpFunction(
        "Function_0_10A",          # 00, 0
        "Function_1_11A",          # 01, 1
        "Function_2_12B",          # 02, 2
    )


    def Function_0_10A(): pass

    label("Function_0_10A")

    SoundLoad(137)
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    Event(0, 2)
    Return()

    # Function_0_10A end

    def Function_1_11A(): pass

    label("Function_1_11A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_12A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12A")

    Return()

    # Function_1_11A end

    def Function_2_12B(): pass

    label("Function_2_12B")

    ClearMapFlags(0x10000000)
    ClearMapFlags(0x2000000)
    EventBegin(0x0)
    OP_24(0x1C9, 0x4B)
    OP_77(0xC9, 0xC9, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, -940, 0, 4500, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x4, 0x80)
    OP_6D(370, 0, 5650, 0)
    OP_67(0, 5170, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(273, 0)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#035F美丽的王都笼罩着乌云，\x01",
            "昏暗的热情序曲正在奏响……\x02\x03",
            "#030F嘻嘻……\x01",
            "这不是很有趣吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x0, 0x10)
    OP_6F(0x0, 30)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    SetChrPos(0x9, 6430, 0, -20, 270)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(
        0x9,
        "男人的声音",
        "……还是老样子，真是悠闲啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2DC():

        label("loc_2DC")

        TurnDirection(0x8, 0x9, 400)
        OP_48()
        Jump("loc_2DC")

    QueueWorkItem2(0x8, 3, lambda_2DC)

    def lambda_2ED():
        OP_6D(2800, 0, 3250, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2ED)

    def lambda_305():
        OP_6E(318, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_305)
    OP_8E(0x9, 0xFE6, 0x0, 0x5A, 0x7D0, 0x0)
    OP_8C(0x9, 270, 400)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#033F#5P哦哦……\x01",
            "你能领略到我的梦中情景吗？\x02\x03",
            "#031F穆拉，我亲爱的朋友！\x02\x03",
            "一向那么繁忙的你，\x01",
            "竟然特地从帝都来到这里。\x02\x03",
            "今天到底是吹的什么风啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x0, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_71(0x0, 0x10)
    OP_70(0x0, 0x0)

    def lambda_421():
        OP_6D(490, 0, 4019, 1500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_421)
    OP_8E(0x9, 0xFFFFFD94, 0x0, 0xA3C, 0xBB8, 0x0)
    OP_8C(0x9, 0, 400)
    OP_44(0x8, 0x3)

    ChrTalk(
        0x9,
        (
            "#270F你在装什么傻……\x02\x03",
            "还不是因为你一直不和我联络，\x01",
            "到处闲逛吗？\x02\x03",
            "这不是给我添麻烦嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#035F#5P哼哼，不用害羞了。\x02\x03",
            "虽然嘴上说得如此无情，\x01",
            "其实还不是因为担心我，\x01",
            "才像飞艇那般迅速地赶过来吗？\x02\x03",
            "人们不是常说，恋爱是盲目的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#273F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#031F#5P好了，不要再考虑了，\x01",
            "赶快飞奔过来扑到我的怀里吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#272F我特地带过来的，\x01",
            "是你拜托我调查的情报……\x02\x03",
            "看样子，你是不想知道了？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#036F#5P讨厌～\x01",
            "不要说这么过分的话嘛～\x02\x03",
            "#035F我明白了。\x01",
            "你是要我拿出诚意对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#270F这应该是理所当然的吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F#5P这种小事就请看好了。\x02\x03",
            "#035F咳咳……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x8, 1)
    OP_99(0x8, 0x1, 0x2, 0x3E8)
    OP_62(0x8, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    OP_22(0x89, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#031F#5P拜托您了，我的主人☆\x02\x03",
            "#031F#5P请务必告诉人家㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1600)
    OP_63(0x9)
    Sleep(500)
    OP_63(0x8)

    ChrTalk(
        0x8,
        (
            "#033F#5P啊，不对是吗？\x02\x03",
            "#035F那么，下一个是这样。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#039F#3S#5P大哥！\x01",
            "这是我一生的心愿啊啊啊啊！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x8,
        "#039F#3S#5P请一定告诉我啊啊啊啊！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x9,
        (
            "#274F够了……\x01",
            "我头都要晕了……\x02\x03",
            "你快给我闭嘴，我这就告诉你。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    OP_0D()
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#031F#5P哇～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#270F『那个人』的……\x01",
            "行踪终于被我们发现了。\x02\x03",
            "大概一个月之前，\x01",
            "在帝国的游击士协会里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#033F#5P哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#270F在这几个月里，\x01",
            "帝国各地的协会支部陆续受到了袭击。\x02\x03",
            "他好像在调查这件事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F#5P袭击啊……\x02\x03",
            "虽然觉得有点不大可能，\x01",
            "但会不会是哪里的部队干的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#272F这确实不大可能……\x01",
            "现在毕竟已经和十年前不一样了。\x02\x03",
            "据我所知，\x01",
            "所有的部队都没有接到出动的命令。\x02\x03",
            "很有可能是某人雇佣了猎兵团\x01",
            "犯下这些案件的。\x02\x03",
            "#270F而且到了最后，事件得到解决的同时，\x01",
            "又失去了那个人的行踪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#034F#5P呼……被耍了呢。\x02\x03",
            "虽然来到了利贝尔王国，\x01",
            "但是这个结果并不是我想要的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#270F没错，就是这样。\x02\x03",
            "目标人物已经不在了，\x01",
            "你还有留在这里的必要吗？\x02\x03",
            "好像有一场比想象中\x01",
            "更加激烈的暴风雨就要临近了。\x02\x03",
            "被卷进去之前，还是赶快回帝都吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#031F#5P哈·哈·哈，别开玩笑了。\x02\x03",
            "好戏正要上演，\x01",
            "本人没理由中途退席的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#273F……什么。\x02\x03",
            "#271F喂，难道你……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F8E():
        OP_8C(0x8, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F8E)

    def lambda_F9C():
        OP_6E(290, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_F9C)
    OP_6D(-250, 0, 5610, 1500)

    ChrTalk(
        0x8,
        (
            "#035F#6P演员已经到齐了。\x02\x03",
            "虽然主演不在，不过替补演员嘛……\x01",
            "本人心中已经有数了。\x02\x03",
            "#030F那两个人，肯定会凭借自己的力量，\x01",
            "在这广大的舞台上有所作为的。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearMapFlags(0x100000)
    Sleep(1000)
    OP_AD(0x40040, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T3120   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_12B end

    SaveToFile()

Try(main)
