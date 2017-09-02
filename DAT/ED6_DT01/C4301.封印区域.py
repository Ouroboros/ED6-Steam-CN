from ED6ScenarioHelper import *

def main():
    # 封印区域

    CreateScenaFile(
        FileName            = 'C4301   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4301.x',
        MapIndex            = 216,
        MapDefaultBGM       = "ed60035",
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
        '凯诺娜上尉',                           # 9
        '拉赛尔博士',                           # 10
        '基库',                                 # 11
        '机器',                                 # 12
        '机器',                                 # 13
        '雪拉扎德',                             # 14
        '奥利维尔',                             # 15
        '科洛丝',                               # 16
        '阿加特',                               # 17
        '提妲',                                 # 18
        '金',                                   # 19
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
        'ED6_DT07/CH00280 ._CH',             # 00
        'ED6_DT09/CH10990 ._CH',             # 01
        'ED6_DT07/CH02020 ._CH',             # 02
        'ED6_DT07/CH02320 ._CH',             # 03
        'ED6_DT07/CH00100 ._CH',             # 04
        'ED6_DT07/CH00101 ._CH',             # 05
        'ED6_DT07/CH00110 ._CH',             # 06
        'ED6_DT07/CH00111 ._CH',             # 07
        'ED6_DT07/CH00120 ._CH',             # 08
        'ED6_DT07/CH00121 ._CH',             # 09
        'ED6_DT07/CH00130 ._CH',             # 0A
        'ED6_DT07/CH00131 ._CH',             # 0B
        'ED6_DT07/CH00140 ._CH',             # 0C
        'ED6_DT07/CH00141 ._CH',             # 0D
        'ED6_DT07/CH00150 ._CH',             # 0E
        'ED6_DT07/CH00151 ._CH',             # 0F
        'ED6_DT07/CH00160 ._CH',             # 10
        'ED6_DT07/CH00161 ._CH',             # 11
        'ED6_DT07/CH00170 ._CH',             # 12
        'ED6_DT07/CH00171 ._CH',             # 13
        'ED6_DT09/CH10991 ._CH',             # 14
        'ED6_DT06/CH20040 ._CH',             # 15
        'ED6_DT07/CH00020 ._CH',             # 16
        'ED6_DT07/CH00030 ._CH',             # 17
        'ED6_DT07/CH00040 ._CH',             # 18
        'ED6_DT06/CH20053 ._CH',             # 19
        'ED6_DT07/CH00060 ._CH',             # 1A
        'ED6_DT07/CH00070 ._CH',             # 1B
    )

    AddCharChipPat(
        'ED6_DT07/CH00280P._CP',             # 00
        'ED6_DT09/CH10990P._CP',             # 01
        'ED6_DT07/CH02020P._CP',             # 02
        'ED6_DT07/CH02320P._CP',             # 03
        'ED6_DT07/CH00100P._CP',             # 04
        'ED6_DT07/CH00101P._CP',             # 05
        'ED6_DT07/CH00110P._CP',             # 06
        'ED6_DT07/CH00111P._CP',             # 07
        'ED6_DT07/CH00120P._CP',             # 08
        'ED6_DT07/CH00121P._CP',             # 09
        'ED6_DT07/CH00130P._CP',             # 0A
        'ED6_DT07/CH00131P._CP',             # 0B
        'ED6_DT07/CH00140P._CP',             # 0C
        'ED6_DT07/CH00141P._CP',             # 0D
        'ED6_DT07/CH00150P._CP',             # 0E
        'ED6_DT07/CH00151P._CP',             # 0F
        'ED6_DT07/CH00160P._CP',             # 10
        'ED6_DT07/CH00161P._CP',             # 11
        'ED6_DT07/CH00170P._CP',             # 12
        'ED6_DT07/CH00171P._CP',             # 13
        'ED6_DT09/CH10991P._CP',             # 14
        'ED6_DT06/CH20040P._CP',             # 15
        'ED6_DT07/CH00020P._CP',             # 16
        'ED6_DT07/CH00030P._CP',             # 17
        'ED6_DT07/CH00040P._CP',             # 18
        'ED6_DT06/CH20053P._CP',             # 19
        'ED6_DT07/CH00060P._CP',             # 1A
        'ED6_DT07/CH00070P._CP',             # 1B
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    DeclEvent(
        X                   = 46000,
        Y                   = -1000,
        Z                   = -10460,
        Range               = 49420,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFFFFB884,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )


    DeclActor(
        TriggerX            = 62990,
        TriggerZ            = 0,
        TriggerY            = -2920,
        TriggerRange        = 1000,
        ActorX              = 62990,
        ActorZ              = 1200,
        ActorY              = -2920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_32E",          # 00, 0
        "Function_1_362",          # 01, 1
        "Function_2_3AC",          # 02, 2
        "Function_3_3C2",          # 03, 3
        "Function_4_42C",          # 04, 4
        "Function_5_51D",          # 05, 5
        "Function_6_59A",          # 06, 6
        "Function_7_637",          # 07, 7
        "Function_8_6A5",          # 08, 8
        "Function_9_702",          # 09, 9
        "Function_10_8A8",         # 0A, 10
        "Function_11_8EE",         # 0B, 11
        "Function_12_911",         # 0C, 12
        "Function_13_2130",        # 0D, 13
        "Function_14_2764",        # 0E, 14
        "Function_15_28A8",        # 0F, 15
        "Function_16_2CE0",        # 10, 16
        "Function_17_2DB5",        # 11, 17
    )


    def Function_0_32E(): pass

    label("Function_0_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_345")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 15)

    label("loc_345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 0)), scpexpr(EXPR_END)), "loc_350")
    Call(0, 14)

    label("loc_350")

    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_32E end

    def Function_1_362(): pass

    label("Function_1_362")

    LoadEffect(0x5, "map\\\\mp027_00.eff")
    PlayEffect(0x5, 0x6, 0xFF, 62990, 1200, -2920, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_362 end

    def Function_2_3AC(): pass

    label("Function_2_3AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3AC")

    label("loc_3C1")

    Return()

    # Function_2_3AC end

    def Function_3_3C2(): pass

    label("Function_3_3C2")

    TalkBegin(0xD)

    ChrTalk(
        0xD,
        (
            "#020F艾丝蒂尔，\x01",
            "不要太过蛮干哦。\x02\x03",
            "前面的路还长，切忌焦躁。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xD)
    Return()

    # Function_3_3C2 end

    def Function_4_42C(): pass

    label("Function_4_42C")

    TalkBegin(0xE)

    ChrTalk(
        0xE,
        (
            "#030F王城的地下还有\x01",
            "如此巨大的上古遗迹啊。\x02\x03",
            "呵呵，这真是一个\x01",
            "让我的灵感爆发的时刻啊……\x02\x03",
            "不过还要再等等，\x01",
            "因为那些军人和机械魔兽\x01",
            "让人有些扫兴。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    # Function_4_42C end

    def Function_5_51D(): pass

    label("Function_5_51D")

    TalkBegin(0xF)

    ChrTalk(
        0xF,
        (
            "#042F『辉之环』……\x01",
            "既然被封印在这里，\x01",
            "就肯定有什么原因。\x02\x03",
            "理查德上校究竟\x01",
            "知道了些什么……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xF)
    Return()

    # Function_5_51D end

    def Function_6_59A(): pass

    label("Function_6_59A")

    TalkBegin(0x10)

    ChrTalk(
        0x10,
        (
            "#050F往下走了那么久，\x01",
            "竟然只赶了一半的路。\x02\x03",
            "真是的……\x01",
            "#057F到最后也要这么麻烦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x10)
    Return()

    # Function_6_59A end

    def Function_7_637(): pass

    label("Function_7_637")

    TalkBegin(0x11)

    ChrTalk(
        0x11,
        (
            "#062F那些魔兽难道也是\x01",
            "用导力来驱动的吗。\x02\x03",
            "这么说来的话，\x01",
            "这个遗迹果然是……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x11)
    Return()

    # Function_7_637 end

    def Function_8_6A5(): pass

    label("Function_8_6A5")

    TalkBegin(0x12)

    ChrTalk(
        0x12,
        (
            "#070F这里的魔兽\x01",
            "很有挑战性。\x02\x03",
            "我已经跃跃欲试了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_8_6A5 end

    def Function_9_702(): pass

    label("Function_9_702")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",            # 0
            "改造·换钱\x01",      # 1
            "购买道具\x01",        # 2
            "更换队员\x01",        # 3
            "取消\x01",            # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_781")
    Call(0, 10)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_781")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79B")
    Call(0, 11)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_79B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EF")
    EventBegin(0x0)
    OP_4A(0x9, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    Call(0, 13)
    OP_4B(0x9, 255)
    OP_4B(0xD, 255)
    OP_4B(0xE, 255)
    OP_4B(0xF, 255)
    OP_4B(0x10, 255)
    OP_4B(0x11, 255)
    OP_4B(0x12, 255)
    EventEnd(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_7EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_800")
    TalkEnd(0x9)
    Return()

    label("loc_800")


    ChrTalk(
        0x9,
        (
            "#104F一定要坚持下去啊。\x02\x03",
            "#102F随时可能会和上校开战，\x01",
            "做好万全的准备再前进吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_9_702 end

    def Function_10_8A8(): pass

    label("Function_10_8A8")


    ChrTalk(
        0x9,
        (
            "#100F来吧，我会给你们\x01",
            "比这边的工房更好的服务。\x02",
        )
    )

    CloseMessageWindow()
    OP_0D()
    OP_A9(0x6A)
    Return()

    # Function_10_8A8 end

    def Function_11_8EE(): pass

    label("Function_11_8EE")


    ChrTalk(
        0x9,
        "#100F有什么需要的吗？\x02",
    )

    CloseMessageWindow()
    OP_0D()
    OP_A9(0x6B)
    Return()

    # Function_11_8EE end

    def Function_12_911(): pass

    label("Function_12_911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_91E")
    Return()

    label("loc_91E")

    OP_A2(0x668)
    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    OP_9F(0xB, 0xFF, 0x0, 0x0, 0x0, 0x0)
    OP_9F(0xC, 0xFF, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x8, 61000, 0, -13970, 270)
    SetChrPos(0xB, 59250, 6000, -11650, 270)
    SetChrPos(0xC, 59250, 6000, -16329, 270)

    NpcTalk(
        0x8,
        "女人的声音",
        (
            "你们这些捣乱分子，\x01",
            "果然还是不自量力地追来了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_A17():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A17)

    def lambda_A25():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A25)

    def lambda_A33():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_A33)

    def lambda_A41():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_A41)

    def lambda_A4F():
        OP_67(0, 8170, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A4F)

    def lambda_A67():
        OP_6C(37000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A67)
    OP_6D(57560, 0, -13380, 2000)
    SetChrChipByIndex(0x101, 4)
    SetChrChipByIndex(0x102, 6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A9F")
    SetChrChipByIndex(0x103, 8)

    label("loc_A9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB2")
    SetChrChipByIndex(0x104, 10)

    label("loc_AB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC5")
    SetChrChipByIndex(0x106, 14)

    label("loc_AC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD8")
    SetChrChipByIndex(0x105, 12)

    label("loc_AD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AEB")
    SetChrChipByIndex(0x107, 16)

    label("loc_AEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AFE")
    SetChrChipByIndex(0x108, 18)

    label("loc_AFE")

    SetChrPos(0x0, 45670, 0, -14030, 90)
    SetChrPos(0x1, 45670, 0, -14030, 90)
    SetChrPos(0x2, 45670, 0, -14030, 90)
    SetChrPos(0x3, 45670, 0, -14030, 90)

    def lambda_B48():
        OP_8E(0xFE, 0xD110, 0x0, 0xFFFFCBA8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B48)
    Sleep(500)

    def lambda_B68():
        OP_8E(0xFE, 0xD110, 0x0, 0xFFFFC68A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B68)
    Sleep(500)
    OP_A3(0x6)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_BC4")
    Sleep(500)

    def lambda_BAC():
        OP_8E(0xFE, 0xCE9A, 0x0, 0xFFFFC145, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_BAC)
    Jump("loc_BDF")

    label("loc_BC4")


    def lambda_BCA():
        OP_8E(0xFE, 0xCE7C, 0x0, 0xFFFFD080, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_BCA)

    label("loc_BDF")

    OP_A2(0x6)

    label("loc_BE2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_C21")
    Sleep(500)

    def lambda_C09():
        OP_8E(0xFE, 0xCE9A, 0x0, 0xFFFFC145, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_C09)
    Jump("loc_C3C")

    label("loc_C21")


    def lambda_C27():
        OP_8E(0xFE, 0xCE7C, 0x0, 0xFFFFD080, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_C27)

    label("loc_C3C")

    OP_A2(0x6)

    label("loc_C3F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_C7E")
    Sleep(500)

    def lambda_C66():
        OP_8E(0xFE, 0xCE9A, 0x0, 0xFFFFC145, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_C66)
    Jump("loc_C99")

    label("loc_C7E")


    def lambda_C84():
        OP_8E(0xFE, 0xCE7C, 0x0, 0xFFFFD080, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_C84)

    label("loc_C99")

    OP_A2(0x6)

    label("loc_C9C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_CDB")
    Sleep(500)

    def lambda_CC3():
        OP_8E(0xFE, 0xCE9A, 0x0, 0xFFFFC145, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_CC3)
    Jump("loc_CF6")

    label("loc_CDB")


    def lambda_CE1():
        OP_8E(0xFE, 0xCE7C, 0x0, 0xFFFFD080, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_CE1)

    label("loc_CF6")

    OP_A2(0x6)

    label("loc_CF9")

    WaitChrThread(0x0, 0x0)
    OP_8C(0x0, 90, 0)
    WaitChrThread(0x1, 0x0)
    OP_8C(0x1, 90, 0)
    WaitChrThread(0x2, 0x0)
    OP_8C(0x2, 90, 0)
    WaitChrThread(0x3, 0x0)
    OP_8C(0x3, 90, 0)

    ChrTalk(
        0x102,
        "#012F凯诺娜上尉……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#004F怎、怎么她还会出现在这里！？\x01",
            "　\x02\x03",
            "不是已经在空中庭园被打昏了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#180F哼，你们太小看我了。\x01",
            "我才不会被那种程度的攻击所打倒。\x02\x03",
            "#181F虽然我已经拼尽全力守护，\x01",
            "格兰赛尔城最后还是被夺走了……\x02\x03",
            "#188F不过，只要上校得到了『辉之环』，\x01",
            "必定可以随时将王城夺回来。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F0F")

    ChrTalk(
        0x103,
        (
            "#025F#5P该怎么说好呢……\x01",
            "真是不知悔改的性格啊。\x02\x03",
            "#027F与其说是母狐狸，\x01",
            "倒不如说她是蛇更加贴切呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_11E1")

    label("loc_F0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FC0")

    ChrTalk(
        0x104,
        (
            "#035F#5P哼，被逼到走投无路的人\x01",
            "还沉醉在泡沫般的美梦里……\x02\x03",
            "#030F真是可悲啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_11E1")

    label("loc_FC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1030")

    ChrTalk(
        0x106,
        (
            "#053F#5P母狐狸……\x01",
            "这绰号的确和你很相配……\x02\x03",
            "#057F做你的千秋大梦去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_11E1")

    label("loc_1030")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1087")

    ChrTalk(
        0x107,
        (
            "#065F#5P做、做这样的事情，\x01",
            "到底是为了什么啊？\x02\x03",
            "我……实在不明白。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_11E1")

    label("loc_1087")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1122")

    ChrTalk(
        0x108,
        (
            "#075F#5P哎呀哎呀，我说。\x01",
            "你这女人也太过嚣张了吧。\x02\x03",
            "#070F真是和你的美貌不相配呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_11E1")

    label("loc_1122")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11E1")

    ChrTalk(
        0x105,
        (
            "#043F#5P『辉之环』……\x01",
            "真的是人类可以控制住的东西吗？\x02\x03",
            "况且我们还不知道\x01",
            "为什么它会被封印在这里啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_11E1")


    ChrTalk(
        0x8,
        (
            "#186F可恶，给我闭嘴！\x02\x03",
            "我是绝对不会让你们去干扰上校的！\x01",
            "　\x02\x03",
            "#185F出来吧，人形机器！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1258():
        OP_96(0xFE, 0xE772, 0x0, 0xFFFFD27E, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1258)
    OP_9F(0xB, 0x64, 0x64, 0xFF, 0xFF, 0x64)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    WaitChrThread(0xB, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)

    def lambda_12A7():

        label("loc_12A7")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_12A7")

    QueueWorkItem2(0xB, 1, lambda_12A7)

    def lambda_12BA():
        OP_96(0xFE, 0xE772, 0x0, 0xFFFFC037, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12BA)
    OP_9F(0xC, 0x64, 0x64, 0xFF, 0xFF, 0x64)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    WaitChrThread(0xC, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)

    def lambda_1309():

        label("loc_1309")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_1309")

    QueueWorkItem2(0xC, 1, lambda_1309)

    ChrTalk(
        0x101,
        "#580F哇啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F可以操纵古代的机械……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#188F哼哼，见识到我们的实力，\x01",
            "你们已经感到气馁了吧。\x02\x03",
            "在对这里展开调查之前\x01",
            "我们就已经收集了足够的资料。\x02\x03",
            "通过那些资料来看，\x01",
            "操纵这些强大的人形兵器也并非不可能。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1474")

    ChrTalk(
        0x103,
        (
            "#025F#5P呼……\x01",
            "我就讨厌这种固执的女人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1636")

    label("loc_1474")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14CA")

    ChrTalk(
        0x104,
        (
            "#035F#5P呵……\x01",
            "真是可歌可泣的努力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1636")

    label("loc_14CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_151E")

    ChrTalk(
        0x106,
        "#057F#5P嘁……不要开玩笑了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1636")

    label("loc_151E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1595")

    ChrTalk(
        0x107,
        (
            "#063F#5P既、既然存在这样的技术，\x01",
            "就应该将它用于正途才合适啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1636")

    label("loc_1595")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15EA")

    ChrTalk(
        0x108,
        "#075F#5P喂喂，你不要命了吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1636")

    label("loc_15EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1636")

    ChrTalk(
        0x105,
        "#043F#5P这、这太危险了……\x02",
    )

    CloseMessageWindow()

    label("loc_1636")


    ChrTalk(
        0x8,
        (
            "#183F哼，什么也不用说了。\x02\x03",
            "#185F准备……开始进攻！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1678():
        OP_92(0xFE, 0x8, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1678)
    Sleep(10)

    def lambda_1692():
        OP_92(0xFE, 0x8, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1692)
    Sleep(10)
    OP_A3(0x6)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_16E2")
    Sleep(10)

    def lambda_16D0():
        OP_92(0xFE, 0xC, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_16D0)
    Jump("loc_16F7")

    label("loc_16E2")


    def lambda_16E8():
        OP_92(0xFE, 0xB, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_16E8)

    label("loc_16F7")

    OP_A2(0x6)

    label("loc_16FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_174B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1733")
    Sleep(10)

    def lambda_1721():
        OP_92(0xFE, 0xC, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_1721)
    Jump("loc_1748")

    label("loc_1733")


    def lambda_1739():
        OP_92(0xFE, 0xB, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_1739)

    label("loc_1748")

    OP_A2(0x6)

    label("loc_174B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_179C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1784")
    Sleep(10)

    def lambda_1772():
        OP_92(0xFE, 0xC, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_1772)
    Jump("loc_1799")

    label("loc_1784")


    def lambda_178A():
        OP_92(0xFE, 0xB, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_178A)

    label("loc_1799")

    OP_A2(0x6)

    label("loc_179C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_17D5")
    Sleep(10)

    def lambda_17C3():
        OP_92(0xFE, 0xC, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_17C3)
    Jump("loc_17EA")

    label("loc_17D5")


    def lambda_17DB():
        OP_92(0xFE, 0xB, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_17DB)

    label("loc_17EA")

    OP_A2(0x6)

    label("loc_17ED")

    Sleep(50)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 20)

    def lambda_1808():
        OP_8E(0xFE, 0xCC1A, 0x0, 0xFFFFD27E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1808)
    Sleep(10)
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 20)

    def lambda_1838():
        OP_8E(0xFE, 0xCC1A, 0x0, 0xFFFFC037, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1838)
    Sleep(10)

    def lambda_1858():
        OP_92(0xFE, 0x0, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1858)
    Sleep(200)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x39B, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_18A1"),
        (SWITCH_DEFAULT, "loc_18A4"),
    )


    label("loc_18A1")

    OP_B4(0x0)
    Return()

    label("loc_18A4")

    EventBegin(0x0)
    SetChrPos(0x101, 57050, 0, -12660, 132)
    SetChrPos(0x102, 56160, 0, -14450, 88)
    OP_A3(0x6)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_190F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_18FB")
    SetChrPos(0x0, 57840, 0, -15280, 27)
    Jump("loc_190C")

    label("loc_18FB")

    SetChrPos(0x0, 56200, 0, -11470, 112)

    label("loc_190C")

    OP_A2(0x6)

    label("loc_190F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1953")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_193F")
    SetChrPos(0x1, 57840, 0, -15280, 27)
    Jump("loc_1950")

    label("loc_193F")

    SetChrPos(0x1, 56200, 0, -11470, 112)

    label("loc_1950")

    OP_A2(0x6)

    label("loc_1953")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1997")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1983")
    SetChrPos(0x2, 57840, 0, -15280, 27)
    Jump("loc_1994")

    label("loc_1983")

    SetChrPos(0x2, 56200, 0, -11470, 112)

    label("loc_1994")

    OP_A2(0x6)

    label("loc_1997")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_19C7")
    SetChrPos(0x3, 57840, 0, -15280, 27)
    Jump("loc_19D8")

    label("loc_19C7")

    SetChrPos(0x3, 56200, 0, -11470, 112)

    label("loc_19D8")

    OP_A2(0x6)

    label("loc_19DB")

    SetChrPos(0x8, 59690, 0, -13480, 0)
    SetChrChipByIndex(0x8, 21)
    SetChrSubChip(0x8, 0)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_6D(57980, 0, -13040, 0)
    OP_67(0, 9150, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#007F这、这回总算是完全昏迷了吧……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯……\x01",
            "短时间内应该不能行动了。\x02\x03",
            "多亏了她的出现……\x01",
            "从她守卫在这里的举动来判断，\x01",
            "通过这条路线应该就能找到上校。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C15")

    ChrTalk(
        0x101,
        "#004F的、的确……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F那么，\x01",
            "我就叫基库将他们带过来吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_8C(0x105, 270, 400)

    def lambda_1BB4():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1BB4)

    def lambda_1BC2():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1BC2)

    def lambda_1BD0():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1BD0)

    def lambda_1BDE():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1BDE)
    Sleep(400)

    ChrTalk(
        0x105,
        "#040F#2P基库，过来！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2P啾～⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CE3")

    label("loc_1C15")


    ChrTalk(
        0x101,
        (
            "#004F的、的确……\x02\x03",
            "#006F这么说来的话，\x01",
            "就可以叫基库将他们带过来了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_8C(0x101, 270, 400)

    def lambda_1C84():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1C84)

    def lambda_1C92():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1C92)

    def lambda_1CA0():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1CA0)

    def lambda_1CAE():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1CAE)
    Sleep(400)

    ChrTalk(
        0x101,
        "#508F#2P喂～基库！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2P啾！\x02",
    )

    CloseMessageWindow()

    label("loc_1CE3")

    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, 37300, 5000, -13990, 0)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_1D09():
        OP_6D(52800, 0, -14030, 2000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1D09)

    def lambda_1D21():
        OP_8E(0xFE, 0xD8B8, 0x3E8, 0xFFFFCAF4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1D21)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x101, 54150, 0, -5010, 45)
    SetChrPos(0x102, 55010, 0, -6060, 45)
    SetChrFlags(0xA, 0x80)
    OP_A3(0x6)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1DA5")
    SetChrPos(0x0, 53820, 0, -7240, 45)
    Jump("loc_1DB6")

    label("loc_1DA5")

    SetChrPos(0x0, 52900, 0, -6250, 45)

    label("loc_1DB6")

    OP_A2(0x6)

    label("loc_1DB9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1DE9")
    SetChrPos(0x1, 53820, 0, -7240, 45)
    Jump("loc_1DFA")

    label("loc_1DE9")

    SetChrPos(0x1, 52900, 0, -6250, 45)

    label("loc_1DFA")

    OP_A2(0x6)

    label("loc_1DFD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1E2D")
    SetChrPos(0x2, 53820, 0, -7240, 45)
    Jump("loc_1E3E")

    label("loc_1E2D")

    SetChrPos(0x2, 52900, 0, -6250, 45)

    label("loc_1E3E")

    OP_A2(0x6)

    label("loc_1E41")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1E71")
    SetChrPos(0x3, 53820, 0, -7240, 45)
    Jump("loc_1E82")

    label("loc_1E71")

    SetChrPos(0x3, 52900, 0, -6250, 45)

    label("loc_1E82")

    OP_A2(0x6)

    label("loc_1E85")

    OP_4A(0x9, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    Call(0, 14)
    SetChrFlags(0x8, 0x800)
    ClearChrFlags(0x8, 0x1)
    OP_6D(56230, 0, -3780, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#102F#5P从刚才检测出的导力反应的程度来看，\x01",
            "基本上已经可以确定这个遗迹的规模了……\x02\x03",
            "这个地方应该是在遗迹的中间位置。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F呼，只走了一半啊。\x02\x03",
            "#003F再不快一点的话恐怕上校会……\x01",
            "哎呀，总觉得好着急呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F可是，如果现在就着急，\x01",
            "反而有可能会迷路的。\x02\x03",
            "放松一些，认真地走下去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#104F#5P唔……\x01",
            "一定要坚持下去啊。\x02\x03",
            "#102F随时可能会和上校开战，\x01",
            "做好充分的准备再前进吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 255)
    OP_4B(0xD, 255)
    OP_4B(0xE, 255)
    OP_4B(0xF, 255)
    OP_4B(0x10, 255)
    OP_4B(0x11, 255)
    OP_4B(0x12, 255)
    EventEnd(0x0)
    Return()

    # Function_12_911 end

    def Function_13_2130(): pass

    label("Function_13_2130")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2141")
    RemoveParty(0x2, 0xFF)

    label("loc_2141")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2152")
    RemoveParty(0x3, 0xFF)

    label("loc_2152")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2163")
    RemoveParty(0x5, 0xFF)

    label("loc_2163")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2174")
    RemoveParty(0x4, 0xFF)

    label("loc_2174")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2185")
    RemoveParty(0x6, 0xFF)

    label("loc_2185")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2196")
    RemoveParty(0x7, 0xFF)

    label("loc_2196")

    Fade(1000)
    SetChrPos(0x101, 54150, 0, -5010, 45)
    SetChrPos(0x102, 55010, 0, -6060, 45)
    Call(0, 14)
    OP_6D(56230, 0, -3780, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请选择除了约修亚和艾丝蒂尔以外的两名成员。\x01",
            "　\x02",
        )
    )


    label("loc_2252")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26B8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22B5")

    Menu(
        0,
        10,
        106,
        1,
        (
            "★【　雪拉扎德　】\x01",      # 0
            "　【　奥利维尔　】\x01",      # 1
            "　【　 阿加特 　】\x01",      # 2
            "　【　　提妲　　】\x01",      # 3
            "　【　　 金 　　】\x01",      # 4
            "　【　 科洛丝 　】\x01",      # 5
        )
    )

    Jump("loc_24A9")

    label("loc_22B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_230B")

    Menu(
        0,
        10,
        106,
        1,
        (
            "　【　雪拉扎德　】\x01",      # 0
            "★【　奥利维尔　】\x01",      # 1
            "　【　 阿加特 　】\x01",      # 2
            "　【　　提妲　　】\x01",      # 3
            "　【　　 金 　　】\x01",      # 4
            "　【　 科洛丝 　】\x01",      # 5
        )
    )

    Jump("loc_24A9")

    label("loc_230B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2361")

    Menu(
        0,
        10,
        106,
        1,
        (
            "　【　雪拉扎德　】\x01",      # 0
            "　【　奥利维尔　】\x01",      # 1
            "★【　 阿加特 　】\x01",      # 2
            "　【　　提妲　　】\x01",      # 3
            "　【　　 金 　　】\x01",      # 4
            "　【　 科洛丝 　】\x01",      # 5
        )
    )

    Jump("loc_24A9")

    label("loc_2361")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23B7")

    Menu(
        0,
        10,
        106,
        1,
        (
            "　【　雪拉扎德　】\x01",      # 0
            "　【　奥利维尔　】\x01",      # 1
            "　【　 阿加特 　】\x01",      # 2
            "★【　　提妲　　】\x01",      # 3
            "　【　　 金 　　】\x01",      # 4
            "　【　 科洛丝 　】\x01",      # 5
        )
    )

    Jump("loc_24A9")

    label("loc_23B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_240D")

    Menu(
        0,
        10,
        106,
        1,
        (
            "　【　雪拉扎德　】\x01",      # 0
            "　【　奥利维尔　】\x01",      # 1
            "　【　 阿加特 　】\x01",      # 2
            "　【　　提妲　　】\x01",      # 3
            "★【　　 金 　　】\x01",      # 4
            "　【　 科洛丝 　】\x01",      # 5
        )
    )

    Jump("loc_24A9")

    label("loc_240D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2464")

    Menu(
        0,
        10,
        106,
        1,
        (
            "　【　雪拉扎德　】\x01",      # 0
            "　【　奥利维尔　】\x01",      # 1
            "　【　 阿加特 　】\x01",      # 2
            "　【　　提妲　　】\x01",      # 3
            "　【　　 金 　　】\x01",      # 4
            "★【　 科洛丝 　】\x01",      # 5
        )
    )

    Jump("loc_24A9")

    label("loc_2464")


    Menu(
        0,
        10,
        106,
        0,
        (
            "　【　雪拉扎德　】\x01",      # 0
            "　【　奥利维尔　】\x01",      # 1
            "　【　 阿加特 　】\x01",      # 2
            "　【　　提妲　　】\x01",      # 3
            "　【　　 金 　　】\x01",      # 4
            "　【　 科洛丝 　】\x01",      # 5
        )
    )


    label("loc_24A9")

    MenuEnd(0x0)
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_24D0"),
        (1, "loc_24EA"),
        (2, "loc_2504"),
        (3, "loc_251E"),
        (4, "loc_2538"),
        (5, "loc_2552"),
        (SWITCH_DEFAULT, "loc_256C"),
    )


    label("loc_24D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24E4")
    AddParty(0x2, 0xFF)
    Jump("loc_24E7")

    label("loc_24E4")

    RemoveParty(0x2, 0xFF)

    label("loc_24E7")

    Jump("loc_25E4")

    label("loc_24EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24FE")
    AddParty(0x3, 0xFF)
    Jump("loc_2501")

    label("loc_24FE")

    RemoveParty(0x3, 0xFF)

    label("loc_2501")

    Jump("loc_25E4")

    label("loc_2504")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2518")
    AddParty(0x5, 0xFF)
    Jump("loc_251B")

    label("loc_2518")

    RemoveParty(0x5, 0xFF)

    label("loc_251B")

    Jump("loc_25E4")

    label("loc_251E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2532")
    AddParty(0x6, 0xFF)
    Jump("loc_2535")

    label("loc_2532")

    RemoveParty(0x6, 0xFF)

    label("loc_2535")

    Jump("loc_25E4")

    label("loc_2538")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_254C")
    AddParty(0x7, 0xFF)
    Jump("loc_254F")

    label("loc_254C")

    RemoveParty(0x7, 0xFF)

    label("loc_254F")

    Jump("loc_25E4")

    label("loc_2552")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2566")
    AddParty(0x4, 0xFF)
    Jump("loc_2569")

    label("loc_2566")

    RemoveParty(0x4, 0xFF)

    label("loc_2569")

    Jump("loc_25E4")

    label("loc_256C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2580")
    RemoveParty(0x2, 0xFF)
    Jump("loc_25E1")

    label("loc_2580")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2594")
    RemoveParty(0x3, 0xFF)
    Jump("loc_25E1")

    label("loc_2594")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25A8")
    RemoveParty(0x5, 0xFF)
    Jump("loc_25E1")

    label("loc_25A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25BC")
    RemoveParty(0x4, 0xFF)
    Jump("loc_25E1")

    label("loc_25BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25D0")
    RemoveParty(0x6, 0xFF)
    Jump("loc_25E1")

    label("loc_25D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25E1")
    RemoveParty(0x7, 0xFF)

    label("loc_25E1")

    Jump("loc_25E4")

    label("loc_25E4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2607")
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x2, 0x80)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2693")

    label("loc_2607")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_264C")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请选择除了约修亚和艾丝蒂尔以外的两名成员。\x01",
            "　\x02",
        )
    )

    Jump("loc_2693")

    label("loc_264C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2693")
    SetChrFlags(0x2, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请选择除了约修亚和艾丝蒂尔以外的两名成员。\x01",
            "　\x02",
        )
    )


    label("loc_2693")

    SetChrPos(0x101, 54150, 0, -5010, 45)
    SetChrPos(0x102, 55010, 0, -6060, 45)
    Jump("loc_2252")

    label("loc_26B8")

    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(300, 0)
    Fade(1000)
    SetChrPos(0x101, 54150, 0, -5010, 45)
    SetChrPos(0x102, 55010, 0, -6060, 45)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x2, 54470, 0, -7820, 27)
    SetChrPos(0x3, 56010, 0, -8590, 27)
    Call(0, 14)
    OP_6D(56230, 0, -3780, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Return()

    # Function_13_2130 end

    def Function_14_2764(): pass

    label("Function_14_2764")

    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 55790, 0, -4250, 225)
    SetChrFlags(0x8, 0x800)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 60460, 0, 480, 90)
    SetChrChipByIndex(0x8, 21)
    ClearChrFlags(0x8, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27C6")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 55690, 0, 1000, 180)
    Jump("loc_27CB")

    label("loc_27C6")

    SetChrFlags(0x10, 0x80)

    label("loc_27CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27F2")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 54740, 0, -1560, 180)
    Jump("loc_27F7")

    label("loc_27F2")

    SetChrFlags(0x11, 0x80)

    label("loc_27F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_281E")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 57870, 0, -2040, 225)
    Jump("loc_2823")

    label("loc_281E")

    SetChrFlags(0xE, 0x80)

    label("loc_2823")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_284A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 57210, 0, -860, 225)
    Jump("loc_284F")

    label("loc_284A")

    SetChrFlags(0xD, 0x80)

    label("loc_284F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2876")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 59350, 0, -3220, 225)
    Jump("loc_287B")

    label("loc_2876")

    SetChrFlags(0x12, 0x80)

    label("loc_287B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28A2")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 56420, 0, -2530, 225)
    Jump("loc_28A7")

    label("loc_28A2")

    SetChrFlags(0xF, 0x80)

    label("loc_28A7")

    Return()

    # Function_14_2764 end

    def Function_15_28A8(): pass

    label("Function_15_28A8")

    EventBegin(0x0)
    OP_4A(0x9, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)

    def lambda_28E0():

        label("loc_28E0")

        OP_7C(0x0, 0x64, 0x7D0, 0xBB8)
        OP_48()
        Jump("loc_28E0")

    QueueWorkItem2(0x9, 3, lambda_28E0)
    OP_22(0x85, 0x1, 0x64)
    LoadEffect(0x1, "map\\\\mp015_00.eff")
    OP_43(0x101, 0x0, 0x0, 0x10)
    OP_6D(55710, 0, -7780, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(134000, 0)
    OP_6E(513, 0)
    FadeToBright(2000, 0)
    Sleep(600)
    OP_77(0xC8, 0xC8, 0xC8, 0xBB800, 0x0)

    def lambda_296F():
        OP_6D(-130, 0, -14000, 3500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_296F)

    def lambda_2987():
        OP_6C(45000, 5500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_2987)
    Sleep(400)
    OP_B0(0x3, 0xA)
    OP_B0(0x4, 0xA)
    OP_B0(0x5, 0xA)
    OP_B0(0x6, 0xA)
    OP_B0(0x7, 0xA)
    OP_B0(0x8, 0xA)
    OP_B0(0x9, 0xA)
    OP_B0(0xA, 0xA)
    OP_B0(0xB, 0xA)
    OP_B0(0xC, 0xA)
    OP_B0(0xD, 0xA)
    OP_B0(0xE, 0xA)
    OP_B0(0xF, 0xA)
    OP_B0(0x10, 0xA)
    OP_B0(0x11, 0xA)
    OP_B0(0x12, 0xA)
    OP_B0(0x13, 0xA)
    OP_B0(0x14, 0xA)
    OP_B0(0x15, 0xA)
    OP_B0(0x16, 0xA)
    OP_6F(0x3, 18)
    OP_6F(0x4, 18)
    OP_6F(0x5, 18)
    OP_6F(0x6, 18)
    OP_6F(0x7, 18)
    OP_6F(0x8, 18)
    OP_6F(0x9, 18)
    OP_6F(0xA, 18)
    OP_6F(0xB, 18)
    OP_6F(0xC, 18)
    OP_6F(0xD, 18)
    OP_6F(0xE, 18)
    OP_6F(0xF, 18)
    OP_6F(0x10, 18)
    OP_6F(0x11, 18)
    OP_6F(0x12, 18)
    OP_6F(0x13, 18)
    OP_6F(0x14, 18)
    OP_6F(0x15, 18)
    OP_6F(0x16, 18)
    Sleep(250)
    OP_70(0xF, 0x14)
    OP_70(0x10, 0x14)
    Sleep(250)
    Sleep(250)
    OP_70(0x4, 0x14)
    OP_70(0x3, 0x14)
    Sleep(250)
    OP_70(0x13, 0x14)
    OP_70(0x14, 0x14)
    Sleep(250)
    Sleep(250)
    OP_70(0x16, 0x14)
    OP_70(0x15, 0x14)
    Sleep(250)
    Sleep(250)
    OP_70(0x7, 0x14)
    OP_70(0x5, 0x14)

    def lambda_2AE6():
        OP_6E(665, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2AE6)
    Sleep(250)
    Sleep(500)
    OP_22(0x91, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 67290, 1000, -13940, 0, 0, 0, 4500, 4500, 4500, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x0, 0x1)
    OP_77(0x8C, 0x8C, 0x8C, 0x7D000, 0x0)
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_6F(0x0, 4000)
    OP_6F(0x1, 4000)
    OP_6F(0x2, 4000)
    OP_70(0x0, 0xFDC)
    OP_70(0x1, 0xFDC)
    OP_70(0x2, 0xFDC)

    def lambda_2B81():
        OP_6D(280, 0, 25240, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2B81)
    Sleep(200)
    OP_70(0xE, 0x14)
    OP_70(0x6, 0x14)
    Sleep(200)
    OP_70(0x8, 0x14)
    OP_70(0xD, 0x14)
    Sleep(200)
    OP_70(0xC, 0x14)
    OP_70(0x9, 0x14)
    Sleep(100)
    OP_70(0xB, 0x14)
    OP_70(0x11, 0x14)
    Sleep(100)
    OP_70(0xA, 0x14)
    Sleep(100)
    OP_70(0x12, 0x14)
    Sleep(500)
    Sleep(1000)
    Fade(1000)
    OP_6D(57500, 0, -2650, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#105F#5P糟了！\x01",
            "是『导力停止现象』！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_24(0x85, 0x5A)
    Sleep(200)
    OP_24(0x85, 0x50)
    Sleep(200)
    OP_24(0x85, 0x46)
    Sleep(200)
    OP_24(0x85, 0x3C)
    Sleep(200)
    OP_24(0x85, 0x32)
    Sleep(200)
    OP_24(0x85, 0x28)
    Sleep(200)
    OP_24(0x85, 0x1E)
    Sleep(200)
    OP_24(0x85, 0x14)
    Sleep(200)
    OP_24(0x85, 0xA)
    Sleep(200)
    OP_23(0x85)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C4303   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_28A8 end

    def Function_16_2CE0(): pass

    label("Function_16_2CE0")

    OP_22(0x91, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 67290, 1000, -13940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    OP_82(0x6, 0x2)
    OP_22(0x91, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 67290, 1000, -13940, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(1100)
    OP_22(0x91, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 67290, 1000, -13940, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sleep(800)
    Sleep(800)
    Sleep(800)
    Sleep(500)
    Return()

    # Function_16_2CE0 end

    def Function_17_2DB5(): pass

    label("Function_17_2DB5")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在此休息\x01",      # 0
            "离开\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F73")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_72(0x19, 0x20)
    OP_6F(0x19, 300)
    OP_70(0x19, 0x1F4)
    OP_73(0x19)
    OP_6F(0x19, 500)
    OP_70(0x19, 0x2BC)
    OP_71(0x19, 0x20)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x6, 0x2)
    LoadEffect(0x5, "map\\\\mp027_01.eff")
    PlayEffect(0x5, 0x6, 0xFF, 62990, 1200, -2920, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1500, 0, -1)
    Sleep(1500)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Sleep(3500)
    OP_82(0x6, 0x0)
    LoadEffect(0x5, "map\\\\mp027_00.eff")
    PlayEffect(0x5, 0x0, 0xFF, 62990, 1200, -2920, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x19, 0)
    OP_70(0x19, 0xFA)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2F73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F8D")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2F8D")

    Return()

    # Function_17_2DB5 end

    SaveToFile()

Try(main)
