import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C2307_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2307   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '幻惑之铃露茜奥拉'),
    TXT(0x02, '福音'),
    TXT(0x03, '残像'),
    TXT(0x04, '残像'),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'C2307.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xE18
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT27/CH04520._CH', 'ED6_DT27/CH04520P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00024._CH', 'ED6_DT07/CH00024P._CP'),
        ('ED6_DT27/CH04525._CH', 'ED6_DT27/CH04525P._CP'),
        ('ED6_DT27/CH04526._CH', 'ED6_DT27/CH04526P._CP'),
    ]

# id: 0x10002 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 458753,
            chipIndex           = 1,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65543,
            chipIndex           = 7,
            npcIndex            = 0x01E1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65543,
            chipIndex           = 7,
            npcIndex            = 0x01E1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x16A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x16A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x16A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x16A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_186',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x53),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0002)

    def _loc_186(): pass

    label('loc_186')

    Return()

# id: 0x0001 offset: 0x187
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x188
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_19F',
    )

    Call(0, 0x0005)
    Call(0, 0x0006)

    def _loc_19F(): pass

    label('loc_19F')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_1BC'),
        (0x00000004, 'loc_1C9'),
        (0x00000006, 'loc_1D6'),
        (0x00000007, 'loc_1E3'),
        (0x00000008, 'loc_1F0'),
        (-1, 'loc_1FD'),
    )

    def _loc_1BC(): pass

    label('loc_1BC')

    OP_D2(0x00070218, 0x00070224, 0x08)

    Jump('loc_1FD')

    def _loc_1C9(): pass

    label('loc_1C9')

    OP_D2(0x00070200, 0x0007020C, 0x08)

    Jump('loc_1FD')

    def _loc_1D6(): pass

    label('loc_1D6')

    OP_D2(0x00070230, 0x0007023C, 0x08)

    Jump('loc_1FD')

    def _loc_1E3(): pass

    label('loc_1E3')

    OP_D2(0x00070248, 0x00070254, 0x08)

    Jump('loc_1FD')

    def _loc_1F0(): pass

    label('loc_1F0')

    OP_D2(0x00270176, 0x00270183, 0x08)

    Jump('loc_1FD')

    def _loc_1FD(): pass

    label('loc_1FD')

    OP_6D(34920, 250, 12030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3960, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x01C3, 0x00, 0x64)
    SetChrPos(0x0008, 900, 950, 12280, 90)
    ClearChrFlags(0x0008, 0x0080)
    OP_82(0x80, 0x00)
    OP_82(0x82, 0x00)
    OP_72(0x0006, 0x0004)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_79(0x00, 0x0002)
    OP_79(0x01, 0x0002)
    OP_79(0x02, 0x0002)
    OP_79(0x03, 0x0002)
    OP_79(0x04, 0x0002)
    OP_7B()
    SetChrPos(0x0103, 40, 0, 5100, 90)
    SetChrPos(0x0101, 1200, 0, 4000, 90)
    SetChrPos(0x0102, -1020, 0, 3400, 90)
    SetChrPos(0x00F9, 60, 0, 2300, 90)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 2)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x0102, 3)
    SetChrSubChip(0x0103, 0)
    SetChrChipByIndex(0x0103, 4)
    SetChrSubChip(0x00F9, 0)
    SetChrChipByIndex(0x00F9, 8)

    @scena.Lambda('lambda_0300')
    def lambda_0300():
        OP_6D(1840, 0, 7670, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0300)

    @scena.Lambda('lambda_0318')
    def lambda_0318():
        OP_67(0, 5560, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0318)

    @scena.Lambda('lambda_0330')
    def lambda_0330():
        OP_6B(4800, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0330)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0210341380V#241F#6P呵呵……\n',
            '看来到时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_6D(210, 950, 9870, 0)
    OP_67(0, 2820, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(4000, 0)
    OP_6E(343, 0)
    SetChrSubChip(0x0103, 0)
    SetChrChipByIndex(0x0103, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x00F9, 0)
    SetChrChipByIndex(0x00F9, 65535)
    OP_0D()

    @scena.Lambda('lambda_03FA')
    def lambda_03FA():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_03FA)

    Sleep(100)

    @scena.Lambda('lambda_040D')
    def lambda_040D():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_040D)

    Sleep(100)

    @scena.Lambda('lambda_0420')
    def lambda_0420():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0420)

    Sleep(100)

    @scena.Lambda('lambda_0433')
    def lambda_0433():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0433)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010341381V#1003F#4P对了、对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341382V#1002F这里的结界\n',
            '是为了什么而张开来的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341383V『结社』到底，\n',
            '打算作什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0210341384V#240F#5P很遗憾，我们\n',
            '也未被告知详情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210341385V我们只是按照\n',
            '教授的指示做事而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210341386V#244F仅仅，是在看了隐藏之塔的内部后\n',
            '察觉到了一些线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270406V#1004F#4P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 6)
    OP_0D()
    Sleep(500)

    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 7)
    Fade(500)

    @scena.Lambda('lambda_05C8')
    def lambda_05C8():
        OP_6B(3200, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05C8)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(240)

    OP_22(0x0118, 0x00, 0x64)
    CreateThread(0x000A, 0x01, 0x00, 0x0003)
    CreateThread(0x000B, 0x01, 0x00, 0x0004)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_685',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_6C3')

    def _loc_685(): pass

    label('loc_685')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6AC',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_6C3')

    def _loc_6AC(): pass

    label('loc_6AC')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_6C3(): pass

    label('loc_6C3')

    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030341388V#024F#6P等等姐姐！\n',
            '你还没有全部回答我！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030341389V为什么姐姐\n',
            '一定要杀死团长！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030341390V#527F……把那么温柔的一个人……\n',
            '如同大家的父亲一般的人……杀死！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210341391V#244F#5P呵呵……\n',
            '不好意思，今天就到此为止了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210341392V#241F如果以后还有机会相遇的话，\n',
            '我会把事情的全部后续告诉你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210341393V在此之前要乖乖听话哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x011E, 0x00, 0x64)

    @scena.Lambda('lambda_0832')
    def lambda_0832():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0832)

    @scena.Lambda('lambda_0844')
    def lambda_0844():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0844)

    @scena.Lambda('lambda_0856')
    def lambda_0856():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0856)

    WaitForThreadExit(0x0008, 0x0002)
    WaitForThreadExit(0x000A, 0x0002)
    WaitForThreadExit(0x000B, 0x0002)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030341394V#024F#6P姐姐……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_08B7')
    def lambda_08B7():
        ChrTurnDirection(0x00FE, 0x0103, 400)
        Yield()

        Jump('lambda_08B7')

    DispatchAsync2(0x0101, 0x0003, lambda_08B7)

    @scena.Lambda('lambda_08C8')
    def lambda_08C8():
        OP_6D(80, 500, 10820, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_08C8)

    @scena.Lambda('lambda_08E0')
    def lambda_08E0():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_08E0)

    OP_91(0x0103, 0, 0, 1500, 1000, 0x00)
    Sleep(500)

    OP_62(0x0103, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(1500)

    ChrTalk(
        0x0101,
        (
            '#0010341395V#1026F#4P那、那个，雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341396V#1043F#6P雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0103)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030341397V#522F#5P……我没事，别担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030341398V我已经离姐姐的真相\n',
            '更近一步了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030341399V#026F现在……这就足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A34',
    )

    ChrTalk(
        0x0108,
        (
            '#0080341400V#572F#6P雪拉扎德……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B12')

    def _loc_A34(): pass

    label('loc_A34')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A6B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050341401V#552F#6P雪拉扎德……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B12')

    def _loc_A6B(): pass

    label('loc_A6B')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AA2',
    )

    ChrTalk(
        0x0107,
        (
            '#0070341402V#063F#6P雪拉姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B12')

    def _loc_AA2(): pass

    label('loc_AA2')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ADD',
    )

    ChrTalk(
        0x0105,
        (
            '#0060341403V#043F#6P雪拉扎德小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B12')

    def _loc_ADD(): pass

    label('loc_ADD')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B12',
    )

    ChrTalk(
        0x0109,
        (
            '#0180341404V#1067F#6P雪拉小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B12(): pass

    label('loc_B12')

    OP_8C(0x0103, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030341405V#524F#5P『四轮之塔』已经解决三个了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030341406V返回『埃尔赛尤』，\n',
            '前往最后一座塔吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_20(0x000007D0)
    OP_21()
    OP_A2(0x10FF)
    OP_A2(0x10F3)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0xBAA
@scena.Code('func_03_BAA')
def func_03_BAA():
    SetChrPos(0x000A, 900, 950, 12280, 180)
    OP_9F(0x000A, 0xFF, 0xFF, 0xFF, 0x5A, 0x00000000)
    ClearChrFlags(0x000A, 0x0080)
    OP_91(0x000A, 50, 0, 0, 300, 0x00)
    OP_91(0x000A, -50, 0, 0, 300, 0x00)
    OP_91(0x000A, 100, 0, 0, 300, 0x00)
    OP_91(0x000A, -100, 0, 0, 300, 0x00)
    def _loc_C1B(): pass

    label('loc_C1B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C4F',
    )

    OP_91(0x000A, 150, 0, 0, 300, 0x00)
    OP_91(0x000A, -150, 0, 0, 300, 0x00)

    Jump('loc_C1B')

    def _loc_C4F(): pass

    label('loc_C4F')

    Return()

# id: 0x0004 offset: 0xC50
@scena.Code('func_04_C50')
def func_04_C50():
    SetChrPos(0x000B, 900, 950, 12280, 180)
    OP_9F(0x000B, 0xFF, 0xFF, 0xFF, 0x5A, 0x00000000)
    ClearChrFlags(0x000B, 0x0080)
    OP_91(0x000B, -50, 0, 0, 300, 0x00)
    OP_91(0x000B, 50, 0, 0, 300, 0x00)
    OP_91(0x000B, -100, 0, 0, 300, 0x00)
    OP_91(0x000B, 100, 0, 0, 300, 0x00)
    def _loc_CC1(): pass

    label('loc_CC1')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_CF5',
    )

    OP_91(0x000B, -150, 0, 0, 300, 0x00)
    OP_91(0x000B, 150, 0, 0, 300, 0x00)

    Jump('loc_CC1')

    def _loc_CF5(): pass

    label('loc_CF5')

    Return()

# id: 0x0005 offset: 0xCF6
@scena.Code('func_05_CF6')
def func_05_CF6():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_D70'),
        (0x00000001, 'loc_D76'),
        (-1, 'loc_D7C'),
    )

    def _loc_D70(): pass

    label('loc_D70')

    OP_A2(0x1200)

    Jump('loc_D7C')

    def _loc_D76(): pass

    label('loc_D76')

    OP_A2(0x1201)

    Jump('loc_D7C')

    def _loc_D7C(): pass

    label('loc_D7C')

    Return()

# id: 0x0006 offset: 0xD7D
@scena.Code('func_06_D7D')
def func_06_D7D():
    FadeOut(0, 0, -1)
    OP_6D(-66940, 250, 36210, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x0002,
            0x00FF,
        ),
        (
            0x0005,
            0x0006,
            0x0004,
            0x0008,
            0x0007,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
