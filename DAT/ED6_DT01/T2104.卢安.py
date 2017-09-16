from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2104   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2104.x',
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
        '戴尔蒙市长',                           # 9
        '尤莉亚中尉',                           # 10
        '亲卫队',                               # 11
        '亲卫队',                               # 12
        '亲卫队',                               # 13
        '亲卫队',                               # 14
        ' ',                                    # 15
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
        'ED6_DT07/CH02410 ._CH',             # 00
        'ED6_DT07/CH02090 ._CH',             # 01
        'ED6_DT07/CH01320 ._CH',             # 02
        'ED6_DT07/CH00005 ._CH',             # 03
        'ED6_DT07/CH00015 ._CH',             # 04
        'ED6_DT07/CH00045 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH02410P._CP',             # 00
        'ED6_DT07/CH02090P._CP',             # 01
        'ED6_DT07/CH01320P._CP',             # 02
        'ED6_DT07/CH00005P._CP',             # 03
        'ED6_DT07/CH00015P._CP',             # 04
        'ED6_DT07/CH00045P._CP',             # 05
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1BA",          # 00, 0
        "Function_1_1C9",          # 01, 1
        "Function_2_1E1",          # 02, 2
    )


    def Function_0_1BA(): pass

    label("Function_0_1BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_1C8")
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_1C8")

    Return()

    # Function_0_1BA end

    def Function_1_1C9(): pass

    label("Function_1_1C9")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_72(0x3, 0x4)
    Event(0, 2)
    OP_22(0x1C4, 0x1, 0x64)
    Return()

    # Function_1_1C9 end

    def Function_2_1E1(): pass

    label("Function_2_1E1")

    OP_22(0x75, 0x0, 0x64)
    EventBegin(0x0)
    FadeToBright(2000, 0)
    OP_B0(0x2, 0xF)
    OP_6D(-15160, -2990, -35260, 0)
    OP_67(0, 4070, -10000, 0)
    OP_6B(1530, 0)
    OP_6C(0, 0)
    OP_6E(581, 0)
    OP_72(0x1, 0x2)
    OP_71(0x1, 0x40)
    OP_72(0x0, 0x2)
    OP_71(0x0, 0x40)
    OP_89(0x101, 59410, -2000, -3710, 270)
    OP_89(0x102, 61470, -2000, -4030, 270)
    OP_89(0x105, 60400, -2000, -3500, 270)

    def lambda_27F():
        OP_6D(-14060, 2029, -15000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27F)

    def lambda_297():
        OP_6C(314000, 11000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_297)
    Sleep(3000)

    def lambda_2AC():
        OP_6B(2620, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2AC)

    def lambda_2BC():
        OP_67(0, 8750, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2BC)
    OP_6E(904, 8000)
    OP_44(0x101, 0xFF)
    Fade(1000)
    OP_6D(-6160, -2990, -12620, 0)
    OP_67(0, 4470, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(314000, 0)
    OP_6E(388, 0)
    SetChrBattleFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x80)
    OP_89(0x8, 1090, -2890, -16110, 270)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#668F这、这飞艇是什么东西！\x02\x03",
            "是王国军的……\x01",
            "不对，这个徽章是……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrBattleFlags(0x9, 0x20)
    SetChrBattleFlags(0xA, 0x20)
    SetChrBattleFlags(0xB, 0x20)
    SetChrBattleFlags(0xC, 0x20)
    SetChrBattleFlags(0xD, 0x20)
    OP_89(0x9, -13380, 10050, -12580, 90)
    OP_89(0xA, -15510, 10050, -11720, 90)
    OP_89(0xB, -15520, 10050, -13390, 90)
    OP_89(0xC, -15520, 10050, -13390, 90)
    OP_89(0xD, -14360, 10050, -10980, 90)

    NpcTalk(
        0x9,
        "女性的声音",
        (
            "#4P……王室亲卫队所属。\x01",
            "高速巡洋舰『埃尔赛尤号』。\x02\x03",
            "这就是本舰的名字。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_489():
        OP_6D(-6340, -540, -14100, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_489)

    def lambda_4A1():
        OP_67(0, 5660, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A1)

    def lambda_4B9():
        OP_6B(2680, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4B9)

    def lambda_4C9():
        OP_6E(435, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4C9)

    def lambda_4D9():
        OP_6C(329000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4D9)
    Sleep(3000)

    NpcTalk(
        0x9,
        "女性军官",
        (
            "#170F咳咳……\x01",
            "看来总算是赶上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#668F蓝白色军服……\x01",
            "难道是女王陛下的亲卫队！？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "女性军官",
        (
            "#176F正是如此。\x02\x03",
            "本人就是任职亲卫队中队长的\x01",
            "尤莉亚·舒华兹。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x9,
        (
            "#172F卢安市长，\x01",
            "莫里斯·戴尔蒙先生。\x02\x03",
            "你涉嫌纵火、抢劫、强占等多项罪行，\x01",
            "现在，我要将你拘捕归案。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#668F这是梦……\x01",
            "一定是梦……\x02\x03",
            "#664F啊……怎么搞的……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 370, -2300, -16090, 180)
    OP_51(0x8, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0xFFFEA070), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x8, 0, 300)
    OP_22(0x20C, 0x0, 0x64)
    OP_A1(0xE, 0x1)
    SetChrPos(0xE, 25470, -2990, -32360, 114)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0x0, 0x20)
    SetChrFlags(0x1, 0x20)
    SetChrFlags(0x2, 0x20)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrChipByIndex(0x105, 5)

    def lambda_74F():
        OP_8F(0xFE, 0xFFFFDF12, 0xFFFFF452, 0xFFFFBC80, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_74F)
    Sleep(1700)
    OP_22(0xD4, 0x0, 0x64)

    def lambda_774():
        OP_8F(0xFE, 0xFFFFDF12, 0xFFFFF452, 0xFFFFBC80, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_774)
    Sleep(700)

    def lambda_794():
        OP_8F(0xFE, 0xFFFFDF12, 0xFFFFF452, 0xFFFFBC80, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_794)
    Sleep(600)

    def lambda_7B4():
        OP_8F(0xFE, 0xFFFFDF12, 0xFFFFF452, 0xFFFFBC80, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7B4)

    def lambda_7CF():
        OP_6D(-10020, 100, -16530, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7CF)
    Sleep(400)

    def lambda_7EC():
        OP_8F(0xFE, 0xFFFFDF12, 0xFFFFF452, 0xFFFFBC80, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7EC)
    Sleep(300)

    def lambda_80C():
        OP_8F(0xFE, 0xFFFFDF12, 0xFFFFF452, 0xFFFFBC80, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_80C)
    Sleep(200)

    def lambda_82C():
        OP_8F(0xFE, 0xFFFFDF12, 0xFFFFF452, 0xFFFFBC80, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_82C)
    Sleep(200)

    def lambda_84C():
        OP_8F(0xFE, 0xFFFFDF12, 0xFFFFF452, 0xFFFFBC80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_84C)
    Sleep(200)

    def lambda_86C():
        OP_8F(0xFE, 0xFFFFDF12, 0xFFFFF452, 0xFFFFBC80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_86C)
    Sleep(200)

    def lambda_88C():
        OP_8F(0xFE, 0xFFFFDF12, 0xFFFFF452, 0xFFFFBC80, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_88C)
    WaitChrThread(0x101, 0x0)
    Fade(1000)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x105, 65535)
    OP_0D()
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004F这、这是……\x01",
            "到底是怎么回事啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F我刚在想嘉恩先生请求支援的\x01",
            "王国军能不能及时赶到……\x02\x03",
            "即使是这样，\x01",
            "军队也似乎来得太快了吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#048F……呵呵………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 135, 400)
    Sleep(400)

    ChrTalk(
        0x9,
        (
            "#171F啊，诸位游击士。\x02\x03",
            "很感谢诸位的帮忙。\x01",
            "接下来的事就请交给我们吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    ClearMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1E1 end

    SaveToFile()

Try(main)
