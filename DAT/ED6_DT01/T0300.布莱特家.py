from ED6ScenarioHelper import *

def main():
    # 布莱特家

    CreateScenaFile(
        FileName            = 'T0300   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0300.x',
        MapIndex            = 15,
        MapDefaultBGM       = "ed60088",
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
        '约修亚',                               # 9
        '卡西乌斯',                             # 10
        '器皿',                                 # 11
        '艾利兹街道方向',                       # 12
    )

    DeclEntryPoint(
        Unknown_00              = 2000,
        Unknown_04              = 0,
        Unknown_08              = -6000,
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
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00010 ._CH',             # 00
        'ED6_DT07/CH02000 ._CH',             # 01
        'ED6_DT06/CH20030 ._CH',             # 02
        'ED6_DT06/CH20011 ._CH',             # 03
        'ED6_DT06/CH20021 ._CH',             # 04
        'ED6_DT06/CH20132 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH00010P._CP',             # 00
        'ED6_DT07/CH02000P._CP',             # 01
        'ED6_DT06/CH20030P._CP',             # 02
        'ED6_DT06/CH20011P._CP',             # 03
        'ED6_DT06/CH20021P._CP',             # 04
        'ED6_DT06/CH20132P._CP',             # 05
    )

    DeclNpc(
        X                   = 11500,
        Z                   = 0,
        Y                   = -3400,
        Direction           = 135,
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
        X                   = 2000,
        Z                   = 450,
        Y                   = -1200,
        Direction           = 90,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262148,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4110,
        Z                   = -1000,
        Y                   = -46140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 21670,
        TriggerZ            = 0,
        TriggerY            = -2000,
        TriggerRange        = 800,
        ActorX              = 21670,
        ActorZ              = 1500,
        ActorY              = -1980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 21670,
        TriggerZ            = 0,
        TriggerY            = 0,
        TriggerRange        = 800,
        ActorX              = 21670,
        ActorZ              = 1500,
        ActorY              = 20,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 21670,
        TriggerZ            = 0,
        TriggerY            = 2000,
        TriggerRange        = 800,
        ActorX              = 21670,
        ActorZ              = 1500,
        ActorY              = 2020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_292",          # 00, 0
        "Function_1_437",          # 01, 1
        "Function_2_491",          # 02, 2
        "Function_3_49C",          # 03, 3
        "Function_4_502",          # 04, 4
        "Function_5_5C8",          # 05, 5
        "Function_6_1106",         # 06, 6
        "Function_7_114F",         # 07, 7
        "Function_8_1168",         # 08, 8
        "Function_9_1169",         # 09, 9
        "Function_10_1BD6",        # 0A, 10
        "Function_11_1C19",        # 0B, 11
        "Function_12_1C2F",        # 0C, 12
        "Function_13_1D11",        # 0D, 13
        "Function_14_1D68",        # 0E, 14
    )


    def Function_0_292(): pass

    label("Function_0_292")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_2A6"),
        (2, "loc_311"),
        (3, "loc_3B2"),
        (SWITCH_DEFAULT, "loc_436"),
    )


    label("loc_2A6")

    ClearMapFlags(0x1)
    SetChrChipByIndex(0x8, 2)
    SetChrPos(0x8, -6220, 3450, 4390, 180)
    SetChrFlags(0x8, 0x4)

    def lambda_2CC():

        label("loc_2CC")

        OP_99(0xFE, 0x0, 0x7, 0x320)
        OP_48()
        Jump("loc_2CC")

    QueueWorkItem2(0x8, 1, lambda_2CC)
    ClearChrFlags(0x8, 0x80)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(7170, 3450, -16520, 0)
    OP_6C(308000, 0)
    FadeToBright(2000, 0)
    Event(0, 5)
    Jump("loc_436")

    label("loc_311")

    ClearMapFlags(0x1)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x9, 0x8)
    SetChrPos(0x102, 6021, 450, 3014, 90)
    SetChrPos(0x9, 9600, 500, -2310, 90)
    SetChrChipByIndex(0x9, 10)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0xA, 10000, 1100, -3300, 0)
    ClearChrFlags(0xA, 0x80)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-2924, 0, -6598, 0)
    OP_6C(48000, 0)
    OP_77(0x7, 0x45, 0x91, 0x0, 0x0)
    FadeToBright(500, 0)
    Event(0, 9)
    Jump("loc_436")

    label("loc_3B2")

    OP_A2(0x219)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x6, 0xFF)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x7, 0xFF)
    AddParty(0x0, 0xFF)
    OP_31(0x0, 0x0, 0x3)
    OP_37(0x0, 0x0)
    OP_41(0x0, 0xF1)
    OP_41(0x0, 0x1)
    OP_35(0x0, 0x96)
    OP_36(0x0, 0xE6)
    OP_31(0x1, 0x0, 0x3)
    OP_37(0x1, 0x0)
    OP_41(0x1, 0x1F)
    OP_41(0x1, 0xF1)
    OP_35(0x1, 0xA0)
    OP_36(0x1, 0xEB)
    SetMapFlags(0x1000000)
    SetMapFlags(0x800000)
    OP_16(0x0)
    SetChrChipByIndex(0x8, 0)
    SetChrPos(0x8, -6220, 3450, 4390, 180)
    SetChrFlags(0x8, 0x4)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)
    Jump("loc_436")

    label("loc_436")

    Return()

    # Function_0_292 end

    def Function_1_437(): pass

    label("Function_1_437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44F")
    OP_B1("t0300_y")
    Jump("loc_458")

    label("loc_44F")

    OP_B1("t0300_n")

    label("loc_458")

    OP_16(0x2, 0xFA0, 0xFFFE17B8, 0xFFFDF878, 0x30003)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_490")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_482")
    SetMapFlags(0x800)

    label("loc_482")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1B(0x0, 0x0, 0x2)

    label("loc_490")

    Return()

    # Function_1_437 end

    def Function_2_491(): pass

    label("Function_2_491")

    ClearMapFlags(0x800)
    OP_1B(0x0, 0x0, 0xFFFF)
    Return()

    # Function_2_491 end

    def Function_3_49C(): pass

    label("Function_3_49C")

    EventBegin(0x0)
    OP_6D(-186290, 0, -48440, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    PlayMovie(0x0, "ed6_op.avi")
    OP_56(0x2)
    FadeToDark(2000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "")
    Sleep(2000)
    Call(0, 4)
    Return()

    # Function_3_49C end

    def Function_4_502(): pass

    label("Function_4_502")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    OP_22(0x1C2, 0x1, 0x64)
    OP_6D(800, -1000, -24180, 0)
    OP_67(0, 5600, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(350000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)

    def lambda_55A():
        OP_6D(4000, 0, -1000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55A)

    def lambda_572():
        OP_67(0, 8000, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_572)

    def lambda_58A():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_58A)
    Sleep(8000)

    def lambda_59F():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_59F)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x100000)
    NewScene("ED6_DT01/T0310   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_4_502 end

    def Function_5_5C8(): pass

    label("Function_5_5C8")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_1F(0x64, 0x3E8)
    SetChrPos(0x101, -1860, 3450, 930, 270)
    SetChrFlags(0x101, 0x40)
    OP_43(0x101, 0x0, 0x0, 0x6)
    OP_43(0x8, 0x0, 0x0, 0x7)
    OP_43(0x9, 0x0, 0x0, 0x8)
    OP_6D(-5250, 3450, 3230, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4380, 0)
    OP_6C(226000, 0)
    OP_6E(262, 0)

    def lambda_643():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_643)

    def lambda_653():
        OP_67(0, 5000, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_653)
    Sleep(5000)

    def lambda_670():
        OP_67(0, 6200, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_670)
    OP_6B(3000, 10000)
    Sleep(4000)
    OP_70(0x2, 0x3C)
    Sleep(500)
    OP_A2(0x0)
    OP_A5(0x0)
    OP_21()
    OP_44(0x8, 0x1)
    OP_22(0x7B, 0x0, 0x64)
    SetChrChipByIndex(0x101, 5)

    def lambda_6B7():

        label("loc_6B7")

        OP_99(0xFE, 0x0, 0x2, 0x5DC)
        OP_48()
        Jump("loc_6B7")

    QueueWorkItem2(0x101, 1, lambda_6B7)
    SetChrFlags(0x101, 0x2)
    Sleep(2000)
    OP_44(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#001F咻——咻——！\x02\x03",
            "不错嘛，约修亚。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    OP_1D(0x58)
    Fade(250)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(400)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#010F早上好，艾丝蒂尔。\x02\x03",
            "抱歉。\x01",
            "是不是把你吵醒了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F没有啊，\x01",
            "我已经睡饱了，自然要起床嘛。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7A1():
        OP_6D(-5850, 3450, 4410, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A1)
    OP_8E(0x101, 0xFFFFE7B4, 0xD7A, 0xB2C, 0x7D0, 0x0)
    TurnDirection(0x101, 0x8, 400)
    Sleep(100)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x101,
        (
            "#001F#2P不过，约修亚也真是的。\x01",
            "一大早就这么认真地吹口琴～\x02\x03",
            "呵呵～姐姐我啊，\x01",
            "都听得入神了呢㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#017F#5P什么姐姐啊……\x01",
            "明明和我一样大。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F#2P啧啧啧，你太天真了。\x02\x03",
            "虽然我和你同龄，\x01",
            "不过在这个家里我可算是前辈哦。\x02\x03",
            "也可以说是你的师姐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#010F#5P是是，我完全明白。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#2P呀～你这态度也太敷衍了吧……\x02\x03",
            "#501F话说回来，这首曲子真的很好听呢。\x01",
            "旋律明快，却又有点悲伤的意境……\x02\x03",
            "虽然其它的曲子也都不错，\x01",
            "不过我最喜欢的还要数这首了。\x02\x03",
            "#505F对了……曲名叫什么来着？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#010F#5P『星之所在』。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P啊对对，叫『星之所在』。\x02\x03",
            "#007F啊～\x01",
            "要是我也能把口琴吹得这么棒就好了。\x02\x03",
            "看起来挺简单的，\x01",
            "不过真的做起来却很难啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#010F#5P比起你擅长的棒术，\x01",
            "我倒觉得这个简单多了……\x02\x03",
            "#010F关键还是集中力的问题哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F#2P那也是，要是让我一动不动地做事情，\x01",
            "肯定一会儿就睡着了～\x02\x03",
            "#006F倒是约修亚你不能光喜欢吹口琴，\x01",
            "有时候也该表现活跃一点才行啊。\x02\x03",
            "约修亚的兴趣除了吹口琴，\x01",
            "就是读书和修理武器什么的吧？\x02\x03",
            "#502F在这种时代，\x01",
            "老呆在屋里可是不能打动女孩子的心哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#017F#5P那也没办法，我向来都没什么人缘。\x02\x03",
            "#010F而且我觉得\x01",
            "你的兴趣才真是特别呢。\x02\x03",
            "比如钓鱼呢，捉虫子呢，\x01",
            "还有收集运动鞋什么的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#2P唔……\x01",
            "不行吗？我就是喜欢。\x02\x03",
            "#509F不过话说回来，\x01",
            "那个捉虫子什么的我早就不玩了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#019F#5P哦～真的吗？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x9, -6050, 0, -2610, 0)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(
        0x9,
        "男人的声音",
        (
            "#1P……喂。\x01",
            "艾丝蒂尔、约修亚。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_A2(0x0)
    OP_A2(0x1)
    OP_6D(-6400, 3450, -400, 1500)

    ChrTalk(
        0x101,
        "#501F啊～老爸，早啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#010F早上好，爸爸。\x01",
            "早饭已经准备好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#080F啊啊，大功告成了。\x02\x03",
            "你们俩，趁饭菜还没凉，\x01",
            "赶快下来吃吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F明白～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#010F马上就去。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    NewScene("ED6_DT01/T0310   ._SN", 2, 0, 0)
    IdleLoop()
    Return()

    # Function_5_5C8 end

    def Function_6_1106(): pass

    label("Function_6_1106")

    OP_A6(0x0)
    SetChrPos(0x101, -1860, 3450, 930, 270)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFFF3D0, 0xD7A, 0x3DE, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x40)
    OP_A3(0x0)
    OP_A6(0x0)
    TurnDirection(0xFE, 0x9, 400)
    OP_A3(0x0)
    OP_A6(0x0)
    OP_A3(0x0)
    Return()

    # Function_6_1106 end

    def Function_7_114F(): pass

    label("Function_7_114F")

    OP_A6(0x1)
    Sleep(400)
    TurnDirection(0xFE, 0x9, 400)
    OP_A3(0x1)
    OP_A6(0x1)
    OP_A3(0x1)
    Return()

    # Function_7_114F end

    def Function_8_1168(): pass

    label("Function_8_1168")

    Return()

    # Function_8_1168 end

    def Function_9_1169(): pass

    label("Function_9_1169")

    EventBegin(0x0)
    OP_77(0x7, 0x45, 0x91, 0x0, 0x0)
    OP_6B(3000, 0)
    OP_43(0x102, 0x0, 0x0, 0xA)
    OP_43(0x9, 0x0, 0x0, 0xB)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, 0, 0, 0, 0)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8)
    OP_A2(0x2)
    OP_6D(7500, 450, 1022, 8000)
    OP_A5(0x2)
    OP_6B(2800, 2000)
    OP_0D()
    OP_70(0x1, 0x3C)
    OP_73(0x1)
    OP_A2(0x1)
    OP_A5(0x1)

    ChrTalk(
        0x102,
        "#010F……爸爸。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 1)
    Sleep(300)

    ChrTalk(
        0x9,
        "#080F是约修亚啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_6D(10020, 450, -790, 2000)
    OP_A5(0x1)

    ChrTalk(
        0x102,
        (
            "#010F喝这么多酒，\x01",
            "又会被艾丝蒂尔骂的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#080F出发前提提神嘛。\x01",
            "要不，你也来一杯吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F还是免了。\x01",
            "还有，请不要劝未成年人喝酒。\x02\x03",
            "#018F况且我又不是雪拉姐姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#080F哈哈……\x01",
            "那个大酒鬼，比我能喝多了。\x02\x03",
            "#080F…………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F…………………………\x02\x03",
            "#012F……看来任务很棘手吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#085F现在还没有确实的证据……\x01",
            "不过帝国那边似乎已经有动静了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F埃雷波尼亚帝国……\x02\x03",
            "#012F就是说很可疑吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#082F虽然还没有明显的行动……\x01",
            "不过这却反而让人更加怀疑。\x02\x03",
            "所以我打算先\x01",
            "到帝国大使馆那里打听一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我知道了。\x01",
            "艾丝蒂尔就交给我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#080F可别太娇惯她哦。\x02\x03",
            "#080F她已经是游击士了，\x01",
            "不好好学会照顾自己怎么行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#011F艾丝蒂尔能行的。\x02\x03",
            "#011F她有天生的直觉。虽然平常有点粗枝大叶，\x01",
            "但在武术方面也算是个天才。\x02\x03",
            "#011F所以一定能成为一流的游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#085F现在还是不谙世事的小孩子呢。\x02\x03",
            "#085F总有一天她也要\x01",
            "依自身的意志来选择前进的道路。\x02\x03",
            "#082F……约修亚。\x01",
            "这话也同样是对你说的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#085F已经过了５年了啊……\x02\x03",
            "#085F时间真是转瞬即逝啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F嗯……\x02\x03",
            "#015F真的是转瞬即逝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#082F那时候的话……\x01",
            "你还不打算收回吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F…………………………\x02\x03",
            "#013F对我来说，那已经是最后的底线了。\x02\x03",
            "#013F如果连那都不能守护，\x01",
            "我……绝对不会原谅自己的。\x02\x03",
            "#013F所以我……\x01",
            "爸爸……再一次抱歉了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#080F……你没必要道歉啊。\x02\x03",
            "#080F但是，你要记住一件事。\x02\x03",
            "#080F不管你选择什么样的道路，\x01",
            "都无法抹消这五年的时光。\x02\x03",
            "#080F我和艾丝蒂尔，都是你的家人。\x02\x03",
            "#080F无论发生什么事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F……嗯……\x02\x03",
            "#013F…………………………\x02\x03",
            "#019F谢谢您……爸爸……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x9, 0xFF)
    OP_20(0x9C4)
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT01/T0700   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1169 end

    def Function_10_1BD6(): pass

    label("Function_10_1BD6")

    OP_A6(0x1)
    OP_8E(0xFE, 0x212C, 0x1C2, 0xAB5, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 400)
    OP_A3(0x1)
    OP_A6(0x1)
    OP_8E(0xFE, 0x2710, 0x1C2, 0xFFFFFF56, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 400)
    OP_A3(0x1)
    Return()

    # Function_10_1BD6 end

    def Function_11_1C19(): pass

    label("Function_11_1C19")

    OP_A6(0x2)
    OP_6C(315000, 8000)
    OP_A3(0x2)
    OP_A6(0x2)
    OP_A3(0x2)
    Return()

    # Function_11_1C19 end

    def Function_12_1C2F(): pass

    label("Function_12_1C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CBA")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "仔细看能看到上面写着什么。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『约修亚大笨蛋』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_1D0D")

    label("loc_1CBA")

    OP_A2(0x3)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "竖立着棒术练习用的木桩。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_1D0D")

    TalkEnd(0xFF)
    Return()

    # Function_12_1C2F end

    def Function_13_1D11(): pass

    label("Function_13_1D11")

    OP_A2(0x4)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "竖立着棒术练习用的木桩。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_1D11 end

    def Function_14_1D68(): pass

    label("Function_14_1D68")

    OP_A2(0x5)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "竖立着棒术练习用的木桩。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_1D68 end

    SaveToFile()

Try(main)
