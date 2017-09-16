from ED6ScenarioHelper import *

def main():
    # 安塞尔新街

    CreateScenaFile(
        FileName            = 'R1403   ._SN',
        MapName             = 'Bose',
        Location            = 'R1403.x',
        MapIndex            = 58,
        MapDefaultBGM       = "ed60086",
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
        '吉尔',                                 # 9
        '乔丝特',                               # 10
        '空贼阿伦',                             # 11
        '空贼雷古',                             # 12
        '空贼蒂诺',                             # 13
        '空贼莱尔',                             # 14
        '空贼洛西',                             # 15
        '空贼罗尔',                             # 16
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
        Unknown_3A              = 58,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02120 ._CH',             # 00
        'ED6_DT07/CH02130 ._CH',             # 01
        'ED6_DT07/CH01380 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH02120P._CP',             # 00
        'ED6_DT07/CH02130P._CP',             # 01
        'ED6_DT07/CH01380P._CP',             # 02
    )

    DeclNpc(
        X                   = 26500,
        Z                   = 0,
        Y                   = 12600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x141,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 26500,
        Z                   = 0,
        Y                   = 12600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x141,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 800,
        Z                   = 500,
        Y                   = 500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 500,
        Y                   = 900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 500,
        Y                   = -700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2300,
        Z                   = 500,
        Y                   = -2700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1000,
        Z                   = 500,
        Y                   = -2800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1000,
        Z                   = 500,
        Y                   = -1900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1C2",          # 00, 0
        "Function_1_1ED",          # 01, 1
        "Function_2_200",          # 02, 2
        "Function_3_216",          # 03, 3
        "Function_4_144A",         # 04, 4
    )


    def Function_0_1C2(): pass

    label("Function_0_1C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_1DE")
    OP_A3(0x3FB)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)

    label("loc_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_1EC")
    OP_A3(0x3FA)
    Event(0, 3)

    label("loc_1EC")

    Return()

    # Function_0_1C2 end

    def Function_1_1ED(): pass

    label("Function_1_1ED")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE0C00, 0x3001E)
    Return()

    # Function_1_1ED end

    def Function_2_200(): pass

    label("Function_2_200")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_215")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_200")

    label("loc_215")

    Return()

    # Function_2_200 end

    def Function_3_216(): pass

    label("Function_3_216")

    AddParty(0x3, 0xFF)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(12760, -10, 9570, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(4600, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x64)
    SetChrPos(0x101, 6340, -210, -12440, 315)
    SetChrPos(0x102, 7380, -380, -12200, 315)
    SetChrPos(0x103, 5970, -290, -13400, 315)
    SetChrPos(0x104, 12230, 1020, -21130, 319)
    OP_8B(0xA, 0xFFFFFBB4, 0xFFFFFD30, 0x0)
    OP_8B(0xB, 0xFFFFFBB4, 0xFFFFFD30, 0x0)
    OP_8B(0xC, 0xFFFFFBB4, 0xFFFFFD30, 0x0)
    OP_8B(0xD, 0xFFFFFBB4, 0xFFFFFD30, 0x0)
    OP_8B(0xE, 0xFFFFFBB4, 0xFFFFFD30, 0x0)
    OP_8B(0xF, 0xFFFFFBB4, 0xFFFFFD30, 0x0)
    FadeToBright(2000, 0)
    OP_6D(1960, -10, 2560, 5000)
    Fade(1000)
    OP_6D(3800, 120, -9560, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#020F#6P原来停在了『琥珀之塔』前面。\x02\x03",
            "这里的确是\x01",
            "街道外面最好的停降场所。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D6")

    ChrTalk(
        0x101,
        (
            "#002F#5P『琥珀之塔』？\x01",
            "是和洛连特的『翡翠之塔』\x01",
            "一样的塔吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#2P嗯，它们同样都是\x01",
            "被称为『四轮之塔』的古代遗迹。\x02\x03",
            "那么雪拉姐姐……\x01",
            "我们要马上将他们制服吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51D")

    label("loc_4D6")


    ChrTalk(
        0x102,
        (
            "#012F#2P那么雪拉姐姐……\x01",
            "我们要马上将他们制服吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51D")


    ChrTalk(
        0x103,
        (
            "#522F#6P这个嘛……\x02\x03",
            "和之前交手时相比，\x01",
            "他们的人手增加了好几倍……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#5P没关系啦。\x01",
            "反正也还没到无法对付的数量。\x02\x03",
            "只要我们一口气解决的话……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x104,
        "青年的声音",
        (
            "#1P呵呵……\x01",
            "我想还是不要这样比较好哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_67E():
        OP_6D(6810, -410, -12820, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_67E)

    def lambda_696():

        label("loc_696")

        TurnDirection(0xFE, 0x104, 400)
        OP_48()
        Jump("loc_696")

    QueueWorkItem2(0x101, 1, lambda_696)

    def lambda_6A7():

        label("loc_6A7")

        TurnDirection(0xFE, 0x104, 400)
        OP_48()
        Jump("loc_6A7")

    QueueWorkItem2(0x102, 1, lambda_6A7)

    def lambda_6B8():

        label("loc_6B8")

        TurnDirection(0xFE, 0x104, 400)
        OP_48()
        Jump("loc_6B8")

    QueueWorkItem2(0x103, 1, lambda_6B8)
    SetChrFlags(0x104, 0x4)
    OP_8E(0x104, 0x2850, 0x398, 0xFFFFB5F0, 0x1388, 0x0)
    OP_96(0x104, 0x23E6, 0xFFFFFF92, 0xFFFFC068, 0x3E8, 0x1388)
    ClearChrFlags(0x104, 0x4)
    OP_8E(0x104, 0x1D24, 0xFFFFFE0C, 0xFFFFC8CE, 0x1388, 0x0)
    OP_8C(0x104, 315, 400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#031F呀，让大家久等了㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#3S#5P奥、奥利维\x02",
    )

    CloseMessageWindow()
    OP_44(0x102, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x103, 0x1)

    ChrTalk(
        0x102,
        (
            "#012F小声一点……\x01",
            "会被他们发现的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#5P………（紧张紧张）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)
    TurnDirection(0x102, 0x104, 0)

    ChrTalk(
        0x103,
        (
            "#023F真让人吃惊……\x02\x03",
            "想不到你能这么快\x01",
            "从那种醉死的状态恢复过来。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 400)

    ChrTalk(
        0x104,
        (
            "#035F呵呵，小菜一碟。\x02\x03",
            "我只不过把胃里的东西都吐光，\x01",
            "顺便用冷水淋头罢了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#007F#5P难、难以置信……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F或者说是可怕的执著……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F如此有趣的事情，\x01",
            "本人怎么能错过呢。\x02\x03",
            "离开旅馆的时候，\x01",
            "正好看到你们向街道外面跑出去，\x01",
            "所以我就紧跟着过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F我还是太大意了……\x02\x03",
            "一下子用上那么多烈酒，\x01",
            "竟然还是没能把你灌醉。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x104,
        (
            "#034F刚刚确实是差点要了我的小命啊，\x01",
            "雪拉君你还是饶了我吧……\x02\x03",
            "#030F话说回来，你们……\x02\x03",
            "你们难道不觉得\x01",
            "在这里和空贼战斗很无聊吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F#5P什么无聊！我们又不是来玩的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#032F等一下，我可是认真的。\x02\x03",
            "在这里战斗的话，\x01",
            "就算抓到那对兄妹好了。\x02\x03",
            "接下来要是无法保证\x01",
            "能从他们口中问出空贼的据点……\x02\x03",
            "到那时候，可能连释放人质\x01",
            "之类的要求也都变得难以实现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F任何事都要带点风险吧。\x02\x03",
            "难道说，\x01",
            "你有不冒风险的好办法吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F呵·呵·呵……\x01",
            "各位，把耳朵凑过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F#5P好吧，不过我事先声明……\x02\x03",
            "如果你敢在我耳边吹气，\x01",
            "我真的会揍你哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrPos(0x8, -340, -40, -16430, 0)
    SetChrPos(0x9, 700, -10, -16580, 0)
    OP_6D(-1120, 520, -1770, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3730, 0)
    OP_6C(224000, 0)
    OP_6E(261, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_F8D():
        OP_8E(0xFE, 0xFFFFFAA6, 0x10E, 0xFFFFEC32, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F8D)

    def lambda_FA8():

        label("loc_FA8")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_FA8")

    QueueWorkItem2(0xA, 1, lambda_FA8)

    def lambda_FB9():

        label("loc_FB9")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_FB9")

    QueueWorkItem2(0xB, 1, lambda_FB9)

    def lambda_FCA():

        label("loc_FCA")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_FCA")

    QueueWorkItem2(0xC, 1, lambda_FCA)

    def lambda_FDB():

        label("loc_FDB")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_FDB")

    QueueWorkItem2(0xD, 1, lambda_FDB)

    def lambda_FEC():

        label("loc_FEC")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_FEC")

    QueueWorkItem2(0xE, 1, lambda_FEC)

    def lambda_FFD():

        label("loc_FFD")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_FFD")

    QueueWorkItem2(0xF, 1, lambda_FFD)
    Sleep(800)

    def lambda_1013():
        OP_8E(0xFE, 0xFFFFFE0C, 0x96, 0xFFFFE976, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1013)
    OP_6D(-1870, 520, -4370, 3000)

    ChrTalk(
        0xA,
        "吉尔大哥，大小姐！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "欢迎回来！\x01",
            "我们等了很久呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "谈话的内容很多吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#200F#5P啊啊……\x01",
            "终于要上演压轴戏了。\x02\x03",
            "包括王国军的动向，\x01",
            "这次我们得到了很多情报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "那么，终于……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#210F#5P嗯，\x01",
            "最近几天应该就可以拿到赎金了。\x02\x03",
            "可以说，\x01",
            "现在正朝我们的梦想一步步迈进呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xE,
        "呀嗬——！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "太棒了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#200F#5P喂喂，\x01",
            "现在高兴还太早了。\x02\x03",
            "总之先回据点\x01",
            "向多伦大哥报告吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#211F#5P大家，快点撤退吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5A#3P#1K收到！\x02",
    )


    ChrTalk(
        0xB,
        "#5A#4P#1K收到！\x02",
    )


    ChrTalk(
        0xC,
        "#5A#2P#1K收到！\x02",
    )


    ChrTalk(
        0xD,
        "#5A#2P#1K收到！\x02",
    )


    ChrTalk(
        0xE,
        "#5A#1P#1K收到！\x02",
    )


    ChrTalk(
        0xF,
        "#5A#3P#1K收到！\x02",
    )

    OP_56(0x1)
    OP_59()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    Sleep(1000)
    NewScene("ED6_DT01/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_216 end

    def Function_4_144A(): pass

    label("Function_4_144A")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_6D(16867, 6300, -3100, 0)
    OP_6B(4400, 0)
    OP_67(0, 2500, -10000, 0)
    OP_6C(324000, 0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x2710)

    def lambda_14C1():
        OP_6D(14820, 6300, -3700, 15000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14C1)

    def lambda_14D9():
        OP_6B(5500, 15000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14D9)

    def lambda_14E9():
        OP_6C(135000, 15000)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14E9)

    def lambda_14F9():
        OP_67(0, 10600, -10000, 15000)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_14F9)
    OP_22(0x79, 0x0, 0x64)
    Sleep(6500)
    OP_22(0xCD, 0x0, 0x64)
    Sleep(8500)
    OP_A2(0x3FB)
    SetMapFlags(0x2000000)
    ClearMapFlags(0x10000000)
    NewScene("ED6_DT01/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_144A end

    SaveToFile()

Try(main)
