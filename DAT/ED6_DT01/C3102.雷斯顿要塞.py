from ED6ScenarioHelper import *

def main():
    # 雷斯顿要塞

    CreateScenaFile(
        FileName            = 'C3102   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        '希德少校',                             # 9
        '格斯塔夫维修长',                       # 10
        '士兵',                                 # 11
        '士兵',                                 # 12
        '士兵',                                 # 13
        '士兵',                                 # 14
        '安东尼',                               # 15
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
        'ED6_DT07/CH02450 ._CH',             # 00
        'ED6_DT07/CH02440 ._CH',             # 01
        'ED6_DT07/CH01640 ._CH',             # 02
        'ED6_DT07/CH01700 ._CH',             # 03
        'ED6_DT07/CH01650 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH02450P._CP',             # 00
        'ED6_DT07/CH02440P._CP',             # 01
        'ED6_DT07/CH01640P._CP',             # 02
        'ED6_DT07/CH01700P._CP',             # 03
        'ED6_DT07/CH01650P._CP',             # 04
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1B2",          # 00, 0
        "Function_1_1BA",          # 01, 1
        "Function_2_218",          # 02, 2
        "Function_3_22E",          # 03, 3
        "Function_4_1411",         # 04, 4
        "Function_5_1545",         # 05, 5
    )


    def Function_0_1B2(): pass

    label("Function_0_1B2")

    OP_A3(0x3FA)
    Event(0, 3)
    Return()

    # Function_0_1B2 end

    def Function_1_1BA(): pass

    label("Function_1_1BA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x11C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE")
    OP_28(0x2A, 0x1, 0x4000)

    label("loc_1CE")

    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -12960, 1000, 34480, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_1BA end

    def Function_2_218(): pass

    label("Function_2_218")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_218")

    label("loc_22D")

    Return()

    # Function_2_218 end

    def Function_3_22E(): pass

    label("Function_3_22E")

    OP_A2(0x564)
    OP_28(0x44, 0x1, 0x2)
    EventBegin(0x0)
    SetChrPos(0x8, -15700, 0, 24380, 90)
    SetChrPos(0xA, -14780, 0, 25510, 90)
    SetChrPos(0xB, -16670, 0, 25510, 90)
    SetChrPos(0xC, -14880, 0, 26880, 90)
    SetChrPos(0xD, -16680, 0, 27080, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    StopSound(0xAFC8, 0x3D090, 0x0)
    SetPlaceName(0x8C) # 雷斯顿要塞
    OP_6D(-950, 0, 52320, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4460, 0)
    OP_6C(80000, 0)
    OP_6E(262, 0)

    def lambda_2FA():
        OP_6C(50000, 8000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2FA)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6D(-6420, 0, 24580, 6000)
    Fade(1000)
    OP_6D(-4770, 0, 24600, 0)
    OP_6B(3250, 0)
    OP_6C(54000, 0)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0x106, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, 0, 0, 0, 0)
    SetChrPos(0x102, 0, 0, 0, 0)
    SetChrPos(0x107, 0, 0, 0, 0)
    SetChrPos(0x106, 0, 0, 0, 0)
    SetChrBattleFlags(0x9, 0x20)
    OP_89(0x9, -2180, 2300, 22900, 270)
    OP_4A(0x8, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)

    def lambda_3CF():

        label("loc_3CF")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_3CF")

    QueueWorkItem2(0x8, 1, lambda_3CF)

    def lambda_3E0():

        label("loc_3E0")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_3E0")

    QueueWorkItem2(0xA, 1, lambda_3E0)

    def lambda_3F1():

        label("loc_3F1")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_3F1")

    QueueWorkItem2(0xB, 1, lambda_3F1)

    def lambda_402():

        label("loc_402")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_402")

    QueueWorkItem2(0xC, 1, lambda_402)

    def lambda_413():

        label("loc_413")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_413")

    QueueWorkItem2(0xD, 1, lambda_413)
    StopSound(0xAFC8, 0x1FBD0, 0x0)
    Sleep(500)

    def lambda_436():
        OP_6D(-15630, 0, 24380, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_436)
    OP_8E(0x9, 0xFFFFC59A, 0x0, 0x59F6, 0xBB8, 0x0)
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        (
            "#691F哟，希德少校。\x01",
            "你们订的货物到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#701F啊，格斯塔夫维修长。\x01",
            "要你特地来一趟真不好意思。\x02\x03",
            "不过，\x01",
            "真没想到这么快就能送到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#691F王国军是老主顾嘛，\x01",
            "服务质量当然要做好点。\x02\x03",
            "话说回来，\x01",
            "这次你们要得还真是急哦。\x02\x03",
            "还有之前警备飞艇的维修，\x01",
            "难道发生什么事件了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#702F不，没有……\x01",
            "不过军队里也有各种事嘛。\x02\x03",
            "对了……\x01",
            "关于中央工房的袭击事件……\x02\x03",
            "我们刚刚得到了重要的线索，\x01",
            "估计近期内就会解决的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#690F哦哦……那真是太好了。\x02\x03",
            "被绑架的拉赛尔老爷子\x01",
            "可是我的大恩人啊。\x02\x03",
            "希望他不要受什么伤就好了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#701F嗯，那倒不至于……\x01",
            "总之请你们中央工房放心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#692F哦，知道些什么了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#703F据说袭击犯把博士挟为人质，\x01",
            "想必他们打算要求赎金……\x02\x03",
            "我们已经确认他现在平安无事，\x01",
            "你们就先安心等着吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#691F原来如此啦……\x02\x03",
            "嗯，好的。\x01",
            "交给王国军就没什么好担心的了。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_8C(0x9, 45, 400)

    ChrTalk(
        0x9,
        (
            "#691F那么这次也要检查集装箱吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#701F虽然很信得过你们，\x01",
            "但我们也必须例行公事。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)

    ChrTalk(
        0x8,
        "#702F你们快点开始检查！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "明白！\x02",
    )

    CloseMessageWindow()

    def lambda_9D3():
        OP_8E(0xFE, 0xFFFFCA04, 0x0, 0x7846, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_9D3)

    ChrTalk(
        0xC,
        "明白了！\x02",
    )

    CloseMessageWindow()

    def lambda_9FD():

        label("loc_9FD")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_9FD")

    QueueWorkItem2(0x8, 1, lambda_9FD)

    def lambda_A0E():

        label("loc_A0E")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_A0E")

    QueueWorkItem2(0xA, 1, lambda_A0E)

    def lambda_A1F():

        label("loc_A1F")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_A1F")

    QueueWorkItem2(0xB, 1, lambda_A1F)

    def lambda_A30():

        label("loc_A30")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_A30")

    QueueWorkItem2(0x9, 1, lambda_A30)

    def lambda_A41():
        OP_6D(-9060, 0, 23330, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A41)

    def lambda_A59():
        OP_6B(4710, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A59)

    def lambda_A69():
        OP_6C(90000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A69)
    OP_8E(0xC, 0xFFFFC91E, 0x0, 0x64DC, 0xFA0, 0x0)

    def lambda_A8D():
        OP_8E(0xFE, 0xFFFFCB62, 0x0, 0x40D8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A8D)
    WaitChrThread(0xD, 0x1)
    OP_8C(0xD, 90, 0)
    Sleep(500)
    OP_22(0xAA, 0x0, 0x64)

    ChrTalk(
        0xD,
        "无异常。下一个……\x02",
    )

    CloseMessageWindow()
    OP_43(0xD, 0x1, 0x0, 0x4)
    OP_8C(0xC, 90, 0)
    Sleep(500)
    OP_22(0xAA, 0x0, 0x64)

    ChrTalk(
        0xC,
        "……ＯＫ。\x02",
    )

    CloseMessageWindow()
    OP_43(0xC, 0x1, 0x0, 0x5)
    WaitChrThread(0xD, 0x1)
    OP_22(0xAB, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)

    def lambda_B47():
        OP_6D(-12400, 0, 26810, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B47)

    def lambda_B5F():
        OP_6B(3250, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B5F)

    def lambda_B6F():
        OP_6C(62000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B6F)

    ChrTalk(
        0xD,
        "感应器有动静！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "是生命反应！\x02",
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)

    ChrTalk(
        0x8,
        (
            "#702F什么……！？\x02\x03",
            "维修长……这是？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#692F喂，喂喂。\x01",
            "我可什么都不知道哦。\x02\x03",
            "是不是装置出了故障啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#703F这怎么可能……\x02\x03",
            "这可是为王国军特制的生命感应器，\x01",
            "中央工房发明的东西应该不会出问题的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#691F也许是是老鼠什么的吧。\x01",
            "　\x02\x03",
            "用不着那么紧张啦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#703F……我们也是例行公事。\x02\x03",
            "#704F你们几个！\x01",
            "把集装箱包围起来！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xC, -9980, 0, 18170, 0)
    SetChrPos(0xE, -12260, 0, 26290, 180)

    def lambda_D9D():

        label("loc_D9D")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_D9D")

    QueueWorkItem2(0xA, 1, lambda_D9D)

    def lambda_DAE():

        label("loc_DAE")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_DAE")

    QueueWorkItem2(0xB, 1, lambda_DAE)

    def lambda_DBF():

        label("loc_DBF")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_DBF")

    QueueWorkItem2(0xC, 1, lambda_DBF)

    def lambda_DD0():

        label("loc_DD0")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_DD0")

    QueueWorkItem2(0xD, 1, lambda_DD0)

    def lambda_DE1():

        label("loc_DE1")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_DE1")

    QueueWorkItem2(0x8, 1, lambda_DE1)

    def lambda_DF2():

        label("loc_DF2")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_DF2")

    QueueWorkItem2(0x9, 1, lambda_DF2)
    SetChrChipByIndex(0xA, 4)
    SetChrChipByIndex(0xB, 4)
    SetChrChipByIndex(0xC, 4)
    SetChrChipByIndex(0xD, 4)

    def lambda_E17():
        OP_8E(0xC, 0xFFFFD71A, 0x0, 0x5F64, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_E17)

    def lambda_E32():
        OP_8E(0xA, 0xFFFFD1FC, 0x0, 0x5924, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_E32)

    def lambda_E4D():
        OP_8E(0xB, 0xFFFFC748, 0x0, 0x5D7A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_E4D)

    def lambda_E68():
        OP_8E(0x8, 0xFFFFCD42, 0x0, 0x56EA, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_E68)

    def lambda_E83():
        OP_8F(0x9, 0xFFFFC270, 0x0, 0x56D6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_E83)
    OP_8E(0xD, 0xFFFFC928, 0x0, 0x721A, 0xFA0, 0x0)
    OP_8E(0xD, 0xFFFFC810, 0x0, 0x6126, 0xFA0, 0x0)
    TurnDirection(0xD, 0xE, 400)

    ChrTalk(
        0x8,
        "#700F好……打开。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x80)
    OP_72(0x2, 0x10)
    OP_22(0xA8, 0x0, 0x64)
    OP_B0(0x2, 0x78)
    OP_70(0x2, 0x78)
    OP_6D(-12850, 0, 23990, 1000)
    OP_73(0x2)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#702F啊……？\x02",
    )

    CloseMessageWindow()
    OP_8E(0xE, 0xFFFFCF40, 0x0, 0x5ED8, 0x3E8, 0x0)
    TurnDirection(0xE, 0xD, 600)
    TurnDirection(0xE, 0xC, 600)
    TurnDirection(0xE, 0x8, 600)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    Sleep(500)
    OP_8E(0x9, 0xFFFFCA2C, 0x0, 0x5A1E, 0x7D0, 0x0)

    ChrTalk(
        0x9,
        (
            "#692F怎么，是安东尼啊。\x01",
            "　\x02\x03",
            "你什么时候躲到这里面来了？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xE,
        "喵～呵。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#702F这、这只猫是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#691F这家伙叫安东尼，\x01",
            "是中央工房养的小猫咪。\x02\x03",
            "看来这家伙不小心跑到\x01",
            "『莱普尼兹号』上来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#703F真是吓了我们一跳。\x02\x03",
            "#701F喂，你啊。\x01",
            "还真会引起骚动。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x8, 400)

    ChrTalk(
        0xE,
        "喵呵？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#701F算了，猫本来就喜怒无常的，\x01",
            "跟它说道理也听不懂的……\x02\x03",
            "你要是喜欢的话，\x01",
            "以后就干脆住在这里算了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#692F喂喂。\x01",
            "请不要诱惑安东尼哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "呜咪～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "……喵呜。\x02",
    )

    CloseMessageWindow()
    SetChrBattleFlags(0xE, 0x20)
    OP_8E(0xE, 0xFFFFDD28, 0x0, 0x59F6, 0x1388, 0x0)
    OP_8E(0xE, 0xFFFFF77C, 0x8FC, 0x5974, 0x1388, 0x0)
    SetChrFlags(0xE, 0x80)
    OP_44(0x8, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0x9, 0xFF)

    ChrTalk(
        0x8,
        "#703F唔唔……看来我被甩了。\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 2)
    SetChrChipByIndex(0xB, 2)
    SetChrChipByIndex(0xC, 2)
    SetChrChipByIndex(0xD, 2)

    def lambda_1296():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1296)

    def lambda_12A4():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12A4)

    def lambda_12B2():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12B2)

    def lambda_12C0():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_12C0)
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        (
            "#693F哈哈，真可惜啊。\x02\x03",
            "#691F不过话说回来，\x01",
            "这个生命感应器还真是厉害的东西。\x02\x03",
            "安东尼差点就这样一直被关着了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x8,
        (
            "#701F啊，的确是啊。\x01",
            "真不愧是中央工房发明的机器。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xC, 400)

    ChrTalk(
        0x8,
        (
            "#700F……你们几个。\x01",
            "把剩下的集装箱也检查一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "明白！\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_A2(0x3FA)
    SetMapFlags(0x40000000)
    NewScene("ED6_DT01/C3106   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_22E end

    def Function_4_1411(): pass

    label("Function_4_1411")

    OP_8E(0xD, 0xFFFFC914, 0x0, 0x7350, 0xBB8, 0x0)
    OP_8E(0xD, 0xFFFFD076, 0x0, 0x731E, 0xBB8, 0x0)
    OP_8E(0xD, 0xFFFFD08A, 0x0, 0x744A, 0xBB8, 0x0)
    Sleep(500)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(500)
    OP_8F(0xD, 0xFFFFD076, 0x0, 0x731E, 0x7D0, 0x0)
    OP_8E(0xD, 0xFFFFD940, 0x0, 0x736E, 0xBB8, 0x0)
    OP_8E(0xD, 0xFFFFD940, 0x0, 0x744A, 0xBB8, 0x0)
    Sleep(500)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(500)
    OP_8F(0xD, 0xFFFFD940, 0x0, 0x736E, 0x7D0, 0x0)
    OP_8E(0xD, 0xFFFFDFF8, 0x0, 0x736E, 0xBB8, 0x0)
    OP_8E(0xD, 0xFFFFDFF8, 0x0, 0x8368, 0xBB8, 0x0)
    OP_8C(0xD, 270, 400)
    Sleep(500)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(500)
    OP_8E(0xD, 0xFFFFDFF8, 0x0, 0x733C, 0xBB8, 0x0)
    OP_8E(0xD, 0xFFFFCF04, 0x0, 0x733C, 0xBB8, 0x0)
    OP_8E(0xD, 0xFFFFCF04, 0x0, 0x71CA, 0xBB8, 0x0)
    Sleep(500)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(1000)
    Return()

    # Function_4_1411 end

    def Function_5_1545(): pass

    label("Function_5_1545")

    OP_8E(0xC, 0xFFFFCB76, 0x0, 0x4150, 0xBB8, 0x0)
    OP_8C(0xC, 90, 400)
    Sleep(400)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(400)
    OP_8E(0xC, 0xFFFFCB76, 0x0, 0x37DC, 0xBB8, 0x0)
    OP_8C(0xC, 90, 400)
    Sleep(400)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(400)
    OP_8E(0xC, 0xFFFFCB76, 0x0, 0x2ECC, 0xBB8, 0x0)
    OP_8C(0xC, 90, 400)
    Sleep(400)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(400)
    OP_8E(0xC, 0xFFFFCB76, 0x0, 0x26FC, 0xFA0, 0x0)
    OP_8E(0xC, 0xFFFFD530, 0x0, 0x1D38, 0x1770, 0x0)
    OP_8E(0xC, 0xFFFFDDDC, 0x0, 0x1D38, 0x1770, 0x0)
    OP_8E(0xC, 0xFFFFE570, 0x0, 0x25C6, 0x1770, 0x0)
    OP_8E(0xC, 0xFFFFE570, 0x0, 0x2E68, 0xFA0, 0x0)
    OP_8C(0xC, 270, 400)
    Sleep(400)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(400)
    OP_8E(0xC, 0xFFFFE570, 0x0, 0x3ACA, 0xFA0, 0x0)
    OP_8C(0xC, 270, 400)
    Sleep(400)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(400)
    OP_8E(0xC, 0xFFFFE570, 0x0, 0x46A0, 0xFA0, 0x0)
    OP_8C(0xC, 270, 400)
    Sleep(400)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(400)
    Return()

    # Function_5_1545 end

    SaveToFile()

Try(main)
