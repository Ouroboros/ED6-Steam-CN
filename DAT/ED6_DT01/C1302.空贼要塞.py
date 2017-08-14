from ED6ScenarioHelper import *

def main():
    # 空贼要塞

    CreateScenaFile(
        FileName            = 'C1302   ._SN',
        MapName             = 'Bose',
        Location            = 'C1302.x',
        MapIndex            = 52,
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
        '乔丝特',                               # 9
        '吉尔',                                 # 10
        '多伦',                                 # 11
        '王国军士兵',                           # 12
        '王国军士兵',                           # 13
        '王国军士兵',                           # 14
        '王国军士兵',                           # 15
        '王国军军官',                           # 16
        '理查德上校',                           # 17
        '凯诺娜上尉',                           # 18
        '摩尔根将军',                           # 19
        '奈尔',                                 # 20
        '朵洛希',                               # 21
        '王国军士兵',                           # 22
        '王国军士兵',                           # 23
        '王国军士兵',                           # 24
        '王国军士兵',                           # 25
        '王国军士兵',                           # 26
        '王国军士兵',                           # 27
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
        Unknown_3A              = 52,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02130 ._CH',             # 00
        'ED6_DT07/CH02120 ._CH',             # 01
        'ED6_DT07/CH02110 ._CH',             # 02
        'ED6_DT07/CH01650 ._CH',             # 03
        'ED6_DT07/CH01310 ._CH',             # 04
        'ED6_DT07/CH02030 ._CH',             # 05
        'ED6_DT07/CH02100 ._CH',             # 06
        'ED6_DT07/CH02060 ._CH',             # 07
        'ED6_DT06/CH20063 ._CH',             # 08
        'ED6_DT07/CH02080 ._CH',             # 09
        'ED6_DT07/CH01640 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH02130P._CP',             # 00
        'ED6_DT07/CH02120P._CP',             # 01
        'ED6_DT07/CH02110P._CP',             # 02
        'ED6_DT07/CH01650P._CP',             # 03
        'ED6_DT07/CH01310P._CP',             # 04
        'ED6_DT07/CH02030P._CP',             # 05
        'ED6_DT07/CH02100P._CP',             # 06
        'ED6_DT07/CH02060P._CP',             # 07
        'ED6_DT06/CH20063P._CP',             # 08
        'ED6_DT07/CH02080P._CP',             # 09
        'ED6_DT07/CH01640P._CP',             # 0A
    )

    DeclNpc(
        X                   = -35700,
        Z                   = 0,
        Y                   = -85400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -36200,
        Z                   = 0,
        Y                   = -84300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -34100,
        Z                   = 0,
        Y                   = -82100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 52155,
        Z                   = -3000,
        Y                   = 17688,
        Direction           = 270,
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
        X                   = 48810,
        Z                   = -3000,
        Y                   = 27604,
        Direction           = 270,
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
        X                   = 72117,
        Z                   = 3000,
        Y                   = 28437,
        Direction           = 270,
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
        X                   = 36188,
        Z                   = 0,
        Y                   = 16750,
        Direction           = 270,
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
        X                   = 48683,
        Z                   = -3000,
        Y                   = 29357,
        Direction           = 270,
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
        X                   = 47780,
        Z                   = 0,
        Y                   = 39390,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 47780,
        Z                   = 0,
        Y                   = 39390,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 209710,
        Z                   = 0,
        Y                   = 11740,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 52155,
        Z                   = -3000,
        Y                   = 17688,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 48810,
        Z                   = -3000,
        Y                   = 27604,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 72117,
        Z                   = 3000,
        Y                   = 28437,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 36188,
        Z                   = 0,
        Y                   = 16750,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 36188,
        Z                   = 0,
        Y                   = 16750,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 36188,
        Z                   = 0,
        Y                   = 16750,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_362",          # 00, 0
        "Function_1_381",          # 01, 1
        "Function_2_382",          # 02, 2
        "Function_3_398",          # 03, 3
        "Function_4_1E4F",         # 04, 4
        "Function_5_1EAA",         # 05, 5
    )


    def Function_0_362(): pass

    label("Function_0_362")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_36E"),
        (SWITCH_DEFAULT, "loc_380"),
    )


    label("loc_36E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37D")
    OP_A2(0x35C)
    Event(0, 3)

    label("loc_37D")

    Jump("loc_380")

    label("loc_380")

    Return()

    # Function_0_362 end

    def Function_1_381(): pass

    label("Function_1_381")

    Return()

    # Function_1_381 end

    def Function_2_382(): pass

    label("Function_2_382")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_397")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_382")

    label("loc_397")

    Return()

    # Function_2_382 end

    def Function_3_398(): pass

    label("Function_3_398")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-17060, 3750, -15530, 0)
    OP_67(0, 5310, -10000, 0)
    OP_6B(3740, 0)
    OP_6C(102000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x101, -16500, 2000, -14000, 180)
    SetChrPos(0x103, -17120, 2000, -13840, 180)
    SetChrPos(0x102, -16600, 2000, -12660, 180)
    SetChrPos(0x104, -17460, 2000, -12310, 180)
    SetChrPos(0xB, -13140, 4000, -23900, 180)
    SetChrPos(0xA, -13220, 4000, -22610, 180)
    SetChrPos(0xD, -11860, 4000, -22360, 180)
    SetChrPos(0x8, -13031, 4000, -21770, 233)
    SetChrPos(0xC, -13750, 4000, -21750, 180)
    SetChrPos(0x9, -12600, 4000, -21120, 64)
    SetChrPos(0xF, -12300, 4000, -20010, 180)
    TurnDirection(0xB, 0xA, 0)
    TurnDirection(0xC, 0xA, 0)
    TurnDirection(0xD, 0xA, 0)
    TurnDirection(0xF, 0xA, 0)
    SetChrPos(0x13, -17040, 4000, -24290, 0)
    SetChrPos(0x14, -16980, 4000, -25880, 0)

    def lambda_508():

        label("loc_508")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_508")

    QueueWorkItem2(0x14, 1, lambda_508)

    def lambda_519():

        label("loc_519")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_519")

    QueueWorkItem2(0x13, 1, lambda_519)
    FadeToBright(1000, 0)
    OP_20(0x5DC)

    def lambda_538():
        OP_6D(-15280, 4000, -18760, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_538)

    def lambda_550():
        OP_8E(0xFE, 0xFFFFBBC2, 0xFA0, 0xFFFFC126, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_550)
    Sleep(100)

    def lambda_570():
        OP_8E(0xFE, 0xFFFFBC4E, 0xFA0, 0xFFFFB9B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_570)
    Sleep(100)

    def lambda_590():
        OP_8E(0xFE, 0xFFFFBED8, 0xFA0, 0xFFFFC180, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_590)

    def lambda_5AB():
        OP_8E(0xFE, 0xFFFFC0CC, 0xFA0, 0xFFFFBC08, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5AB)
    Sleep(100)

    def lambda_5CB():
        OP_8E(0xFE, 0xFFFFBBA4, 0xFA0, 0xFFFFBF28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5CB)
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x102, 0x1)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_61E():
        OP_8C(0xFE, 134, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_61E)
    WaitChrThread(0x103, 0x1)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_648():
        OP_8C(0xFE, 134, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_648)
    WaitChrThread(0x104, 0x1)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_672():
        OP_8C(0xFE, 134, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_672)
    Sleep(1000)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x101,
        "#004F#1P哎……\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x102,
        "#014F这是……\x02",
    )

    CloseMessageWindow()
    OP_21()

    def lambda_721():

        label("loc_721")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_721")

    QueueWorkItem2(0x101, 0, lambda_721)

    def lambda_732():

        label("loc_732")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_732")

    QueueWorkItem2(0x102, 0, lambda_732)

    def lambda_743():

        label("loc_743")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_743")

    QueueWorkItem2(0x103, 0, lambda_743)

    def lambda_754():

        label("loc_754")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_754")

    QueueWorkItem2(0x104, 0, lambda_754)
    OP_1D(0x65)

    def lambda_767():
        OP_6D(-8410, 4000, -22720, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_767)

    def lambda_77F():
        OP_6E(437, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_77F)

    def lambda_78F():
        OP_6C(125000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_78F)
    Sleep(2000)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x9,
        (
            "#201F#2P混、混帐。\x01",
            "军队怎么会知道这地方的！？\x02\x03",
            "那个混蛋，给出的消息又有误！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#214F#5P喂、喂！\x01",
            "不要随便碰我！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#192F喂喂……\x01",
            "这到底是怎么回事！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8AF():
        OP_6D(-14680, 4000, -20970, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8AF)

    def lambda_8C7():
        OP_67(0, 7970, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8C7)

    def lambda_8DF():
        OP_6C(137000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8DF)

    def lambda_8EF():
        OP_6E(244, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8EF)
    OP_43(0xB, 0x1, 0x0, 0x4)
    Sleep(100)
    OP_43(0xA, 0x1, 0x0, 0x4)
    Sleep(200)
    OP_43(0xD, 0x1, 0x0, 0x4)
    Sleep(300)
    OP_43(0x8, 0x1, 0x0, 0x4)
    Sleep(300)
    OP_43(0xC, 0x1, 0x0, 0x4)
    Sleep(300)
    OP_43(0x9, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_43(0xF, 0x1, 0x0, 0x4)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)
    Sleep(600)

    ChrTalk(
        0x14,
        (
            "#153F#6P哇～这些人\x01",
            "就是空贼团的首领啊～\x02\x03",
            "还有女孩子在里面，\x01",
            "真是不可思议呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#144F#6P别站着动口不动手，\x01",
            "快点拍照啦！\x02\x03",
            "这样的爆炸性新闻\x01",
            "可不是经常能遇到的！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    SetChrPos(0x10, -11930, 4000, -33160, 0)
    SetChrPos(0x12, -11930, 4000, -33160, 0)
    SetChrPos(0x11, -11930, 4000, -33160, 0)
    SetChrPos(0x15, -11450, 4050, -36300, 0)
    SetChrPos(0x16, -11450, 4050, -36300, 0)
    SetChrPos(0x17, -11450, 4050, -36300, 0)
    SetChrPos(0x18, -11450, 4050, -36300, 0)
    SetChrPos(0x19, -11450, 4050, -36300, 0)
    SetChrPos(0x1A, -11450, 4050, -36300, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x1A, 0x40)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x11, 0x4)

    def lambda_B60():

        label("loc_B60")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_B60")

    QueueWorkItem2(0x14, 1, lambda_B60)

    def lambda_B71():

        label("loc_B71")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_B71")

    QueueWorkItem2(0x13, 1, lambda_B71)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)

    def lambda_B92():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B92)

    def lambda_BA0():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BA0)

    def lambda_BAE():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BAE)

    def lambda_BBC():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BBC)

    def lambda_BCA():
        OP_6D(-15270, 4000, -25300, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BCA)

    def lambda_BE2():
        OP_8E(0xFE, 0xFFFFC7AC, 0xFA0, 0xFFFFA060, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_BE2)
    Sleep(400)

    def lambda_C02():
        OP_8E(0xFE, 0xFFFFCB76, 0xFA0, 0xFFFF9AFC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_C02)
    Sleep(400)

    def lambda_C22():
        OP_8E(0xFE, 0xFFFFC8C4, 0xFA0, 0xFFFF9674, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C22)

    def lambda_C3D():

        label("loc_C3D")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_C3D")

    QueueWorkItem2(0x15, 1, lambda_C3D)

    def lambda_C4E():

        label("loc_C4E")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_C4E")

    QueueWorkItem2(0x16, 1, lambda_C4E)

    def lambda_C5F():

        label("loc_C5F")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_C5F")

    QueueWorkItem2(0x17, 1, lambda_C5F)

    def lambda_C70():

        label("loc_C70")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_C70")

    QueueWorkItem2(0x18, 1, lambda_C70)

    def lambda_C81():

        label("loc_C81")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_C81")

    QueueWorkItem2(0x19, 1, lambda_C81)

    def lambda_C92():

        label("loc_C92")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_C92")

    QueueWorkItem2(0x1A, 1, lambda_C92)

    def lambda_CA3():
        OP_8E(0xFE, 0xFFFFD058, 0xFA0, 0xFFFFA0A6, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_CA3)
    Sleep(400)

    def lambda_CC3():
        OP_8E(0xFE, 0xFFFFD472, 0xFA0, 0xFFFFA0BA, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_CC3)
    Sleep(400)

    def lambda_CE3():
        OP_8E(0xFE, 0xFFFFD472, 0xFA0, 0xFFFF9C5A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_CE3)
    Sleep(400)

    def lambda_D03():
        OP_8E(0xFE, 0xFFFFD012, 0xFA0, 0xFFFF9C5A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_D03)
    Sleep(400)

    def lambda_D23():
        OP_8E(0xFE, 0xFFFFD472, 0xFA0, 0xFFFF9782, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_D23)
    Sleep(400)

    def lambda_D43():
        OP_8E(0xFE, 0xFFFFCFEA, 0xFA0, 0xFFFF9782, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_D43)
    WaitChrThread(0x10, 0x1)

    def lambda_D63():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_D63)
    WaitChrThread(0x11, 0x1)

    def lambda_D76():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_D76)
    WaitChrThread(0x10, 0x1)

    def lambda_D89():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_D89)

    ChrTalk(
        0x10,
        (
            "#110F怎么样，奈尔先生。\x01",
            "这下可以写出很好的报道吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#141F这是当然的啦！\x02\x03",
            "您能带我们一起来现场，\x01",
            "真是感激不尽啊！\x02\x03",
            "#147F啊，等一下能否\x01",
            "也让我们为上校拍张照呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x14, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    TurnDirection(0x10, 0x12, 400)

    ChrTalk(
        0x10,
        (
            "#113F#6P唔……\x01",
            "将军，请问这可以吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x10, 400)

    ChrTalk(
        0x12,
        (
            "#163F#2P随你的意思吧，\x01",
            "这次的作战方案全是你制定的。\x02\x03",
            "#160F能获得成功的确是你的功劳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#115F#6P将军您言重了，\x01",
            "其实这应归功于情报部各位的正确分析。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0x10,
        (
            "#110F而且，还要感谢\x01",
            "那边几位的鼎力相助。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_101F():

        label("loc_101F")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_101F")

    QueueWorkItem2(0x10, 2, lambda_101F)

    def lambda_1030():

        label("loc_1030")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_1030")

    QueueWorkItem2(0x14, 2, lambda_1030)

    def lambda_1041():

        label("loc_1041")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_1041")

    QueueWorkItem2(0x13, 2, lambda_1041)

    def lambda_1052():

        label("loc_1052")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_1052")

    QueueWorkItem2(0x11, 2, lambda_1052)

    def lambda_1063():

        label("loc_1063")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_1063")

    QueueWorkItem2(0x12, 2, lambda_1063)
    Sleep(500)

    ChrTalk(
        0x12,
        "#161F#2P什么……？\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)

    def lambda_10B3():
        OP_6D(-14680, 4000, -23970, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_10B3)

    def lambda_10CB():

        label("loc_10CB")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_10CB")

    QueueWorkItem2(0x101, 2, lambda_10CB)

    def lambda_10DC():

        label("loc_10DC")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_10DC")

    QueueWorkItem2(0x102, 2, lambda_10DC)

    def lambda_10ED():

        label("loc_10ED")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_10ED")

    QueueWorkItem2(0x103, 2, lambda_10ED)

    def lambda_10FE():

        label("loc_10FE")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_10FE")

    QueueWorkItem2(0x104, 2, lambda_10FE)

    def lambda_110F():
        OP_8E(0xFE, 0xFFFFCAA4, 0xFA0, 0xFFFFB0AA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_110F)
    Sleep(100)

    def lambda_112F():
        OP_8E(0xFE, 0xFFFFC4AA, 0xFA0, 0xFFFFAEFC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_112F)
    Sleep(100)
    SetChrFlags(0x102, 0x4)

    def lambda_1154():
        OP_8E(0xFE, 0xFFFFC7B6, 0xFA0, 0xFFFFB514, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1154)
    Sleep(100)

    def lambda_1174():
        OP_8E(0xFE, 0xFFFFC2FC, 0xFA0, 0xFFFFB3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1174)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x101,
        (
            "#505F唔……\x01",
            "我还是搞不清状况。\x02\x03",
            "到底发生了什么事呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#143F是、是你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#151F哇～是小艾他们呢！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#162F游、游击士！\x01",
            "为什么你们会在这里！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F为了慎重起见，\x01",
            "我们早一步潜进来了。\x02\x03",
            "这个据点已经被压制住了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们是追着逃跑的\x01",
            "空贼首领到这里来的……\x02\x03",
            "真没想到\x01",
            "王国军的警备飞艇也会来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#162F唔唔唔……\x01",
            "又擅自做出这种越权的行动。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x12, 400)

    ChrTalk(
        0x10,
        (
            "#115F#6P虽说如此，不过……\x02\x03",
            "多亏了他们，\x01",
            "我们才能如此顺利地进行突击。\x02\x03",
            "#110F我们应当承认他们这份功劳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#163F……唔。\x02\x03",
            "#160F算了，\x01",
            "接下来就交给你指挥吧。\x02\x03",
            "我先回到飞艇上，\x01",
            "空贼一伙也一并押上来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#110F#6P遵命。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x4)
    OP_8C(0x12, 180, 400)
    OP_43(0x12, 0x1, 0x0, 0x4)
    Sleep(400)
    OP_8C(0x1A, 180, 400)
    OP_43(0x1A, 0x1, 0x0, 0x4)
    Sleep(300)
    OP_8C(0x19, 180, 400)
    OP_43(0x19, 0x1, 0x0, 0x4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#007F还真是个顽固的老爷爷～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0x10,
        (
            "#115F他并不是个不讲理的人，\x01",
            "只是有时候缺乏变通而已。\x02\x03",
            "#112F对了，\x01",
            "其他空贼还有人质在什么地方呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F那些空贼\x01",
            "应该还倒在那边。\x02\x03",
            "而人质都在\x01",
            "被囚禁的房间待命。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#110F这样啊……\x02\x03",
            "嗯，真是辛苦你们了。\x02\x03",
            "包括人质和货物的遣返，\x01",
            "后续工作就交由我们处理吧。\x02\x03",
            "走吧，凯诺娜上尉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#182F遵命。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x4)
    OP_43(0x10, 0x1, 0x0, 0x5)
    Sleep(100)
    OP_43(0x11, 0x1, 0x0, 0x5)

    def lambda_17DA():

        label("loc_17DA")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_17DA")

    QueueWorkItem2(0x14, 1, lambda_17DA)

    def lambda_17EB():

        label("loc_17EB")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_17EB")

    QueueWorkItem2(0x13, 1, lambda_17EB)

    def lambda_17FC():

        label("loc_17FC")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_17FC")

    QueueWorkItem2(0x101, 2, lambda_17FC)

    def lambda_180D():

        label("loc_180D")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_180D")

    QueueWorkItem2(0x102, 2, lambda_180D)

    def lambda_181E():

        label("loc_181E")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_181E")

    QueueWorkItem2(0x103, 2, lambda_181E)

    def lambda_182F():

        label("loc_182F")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_182F")

    QueueWorkItem2(0x104, 2, lambda_182F)
    Sleep(500)
    OP_43(0x15, 0x1, 0x0, 0x5)
    Sleep(200)
    OP_43(0x16, 0x1, 0x0, 0x5)
    Sleep(400)
    OP_43(0x18, 0x1, 0x0, 0x5)
    Sleep(200)
    OP_43(0x17, 0x1, 0x0, 0x5)
    Sleep(300)

    ChrTalk(
        0x13,
        "#143F啊，请等等上校。\x02",
    )

    CloseMessageWindow()

    def lambda_1899():

        label("loc_1899")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_1899")

    QueueWorkItem2(0x101, 2, lambda_1899)

    def lambda_18AA():

        label("loc_18AA")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_18AA")

    QueueWorkItem2(0x102, 2, lambda_18AA)

    def lambda_18BB():

        label("loc_18BB")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_18BB")

    QueueWorkItem2(0x103, 2, lambda_18BB)

    def lambda_18CC():

        label("loc_18CC")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_18CC")

    QueueWorkItem2(0x104, 2, lambda_18CC)
    Sleep(1000)

    ChrTalk(
        0x13,
        (
            "#141F我们本来也想\x01",
            "给你们做个采访的，\x01",
            "不过这次你们就先忙吧。\x02\x03",
            "下次有机会的话，可要拜托你们了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#151F再见了～！\x01",
            "小艾，小约。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    OP_43(0x13, 0x1, 0x0, 0x5)
    Sleep(700)
    OP_43(0x14, 0x1, 0x0, 0x5)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    def lambda_1A1A():
        OP_6D(-15060, 4000, -19760, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A1A)

    def lambda_1A32():
        OP_6E(232, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A32)
    Sleep(3000)
    OP_63(0x101)
    OP_63(0x102)
    OP_63(0x103)
    OP_63(0x104)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)
    OP_20(0x5DC)
    Sleep(1000)
    Fade(1000)
    OP_6B(3010, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#035F哎呀呀～\x01",
            "感觉最后什么好处都被他们得到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F#5P嗯，确实是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F呵呵，其实这样已经够了呢。\x02\x03",
            "游击士的本分就是\x01",
            "默默奉献自己的力量。\x02\x03",
            "被忽视也是没办法的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F的确是这样。\x02\x03",
            "其实父亲也一直在\x01",
            "坚持着这点而默默地工作啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F#5P咦，是这样吗？\x02\x03",
            "…………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x101,
        "#004F#3S#5P啊啊，老爸！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_1C66():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C66)

    def lambda_1C74():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C74)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#015F嗯……\x01",
            "必须认真想想这个问题了。\x02\x03",
            "#013F父亲他究竟在哪里，\x01",
            "现在又在做些什么呢……\x02\x03",
            "为什么不联络我们呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F#5P唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026F这里已经没什么\x01",
            "需要我们帮忙的事情了。\x02\x03",
            "总之先回柏斯\x01",
            "把这次的事件报告一下。\x02\x03",
            "#020F然后再仔细考虑老师的事情吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14E)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E26")
    OP_28(0x13, 0x4, 0x40)

    label("loc_1E26")

    OP_28(0x37, 0x4, 0x10)
    OP_28(0x39, 0x1, 0x100)
    OP_28(0x39, 0x1, 0x200)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_398 end

    def Function_4_1E4F(): pass

    label("Function_4_1E4F")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFFD54E, 0xFD2, 0xFFFF71EE, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFE053, 0xFA0, 0xFFFF7162, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFE003, 0x7D0, 0xFFFF809E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFAA, 0x0, 0xFFFF813E, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_4_1E4F end

    def Function_5_1EAA(): pass

    label("Function_5_1EAA")

    OP_8E(0xFE, 0xFFFFBE38, 0xFA0, 0xFFFFAFB0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFBCC6, 0xFA0, 0xFFFFC22A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFBD52, 0x2EE, 0xFFFFD634, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_5_1EAA end

    SaveToFile()

Try(main)
