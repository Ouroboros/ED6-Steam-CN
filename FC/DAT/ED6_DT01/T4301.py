import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4301   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '特务兵'),
    TXT(0x02, '特务兵'),
    TXT(0x03, '特务兵'),
    TXT(0x04, '军用犬'),
    TXT(0x05, '军用犬'),
    TXT(0x06, '军用犬'),
    TXT(0x07, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4301.x'
    header.mapIndex       = 1
    header.bgm            = 89
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1CAC
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
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT07/CH00340._CH', 'ED6_DT07/CH00340P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT09/CH10060._CH', 'ED6_DT09/CH10060P._CP'),
        ('ED6_DT09/CH10061._CH', 'ED6_DT09/CH10061P._CP'),
        ('ED6_DT06/CH20042._CH', 'ED6_DT06/CH20042P._CP'),
        ('ED6_DT07/CH00440._CH', 'ED6_DT07/CH00440P._CP'),
        ('ED6_DT07/CH00441._CH', 'ED6_DT07/CH00441P._CP'),
    ]

# id: 0x10002 offset: 0x112
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1D2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1D2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1D2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = 1000,
            triggerY            = 42050,
            triggerRange        = 800,
            actorX              = 0,
            actorZ              = 2000,
            actorY              = 42050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1F6
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_22A'),
        (0x00000064, 'loc_240'),
        (0x00000066, 'loc_256'),
        (0x00000067, 'loc_25D'),
        (0x00000068, 'loc_264'),
        (0x00000069, 'loc_26B'),
        (0x0000006A, 'loc_272'),
        (0x0000006B, 'loc_279'),
        (0x0000006C, 'loc_280'),
        (0x0000006D, 'loc_287'),
        (0x0000006E, 'loc_28E'),
        (-1, 'loc_295'),
    )

    def _loc_22A(): pass

    label('loc_22A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 3, 0x653)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 2, 0x652)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_23D',
    )

    SetScenaFlags(ScenaFlag(0x00CA, 3, 0x653))
    Event(0, 0x0003)

    def _loc_23D(): pass

    label('loc_23D')

    Jump('loc_295')

    def _loc_240(): pass

    label('loc_240')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 3, 0x653)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 2, 0x652)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_253',
    )

    SetScenaFlags(ScenaFlag(0x00CA, 3, 0x653))
    Event(0, 0x0004)

    def _loc_253(): pass

    label('loc_253')

    Jump('loc_295')

    def _loc_256(): pass

    label('loc_256')

    Event(0, 0x000D)

    Jump('loc_295')

    def _loc_25D(): pass

    label('loc_25D')

    Event(0, 0x000C)

    Jump('loc_295')

    def _loc_264(): pass

    label('loc_264')

    Event(0, 0x000B)

    Jump('loc_295')

    def _loc_26B(): pass

    label('loc_26B')

    Event(0, 0x000A)

    Jump('loc_295')

    def _loc_272(): pass

    label('loc_272')

    Event(0, 0x0009)

    Jump('loc_295')

    def _loc_279(): pass

    label('loc_279')

    Event(0, 0x0008)

    Jump('loc_295')

    def _loc_280(): pass

    label('loc_280')

    Event(0, 0x0007)

    Jump('loc_295')

    def _loc_287(): pass

    label('loc_287')

    Event(0, 0x0006)

    Jump('loc_295')

    def _loc_28E(): pass

    label('loc_28E')

    Event(0, 0x0005)

    Jump('loc_295')

    def _loc_295(): pass

    label('loc_295')

    Return()

# id: 0x0001 offset: 0x296
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -128000, -112000, 196706)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 0, 0x658)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B8',
    )

    OP_72(0x0000, 0x0010)

    Jump('loc_2BC')

    def _loc_2B8(): pass

    label('loc_2B8')

    OP_64(0x00, 0x0001)

    def _loc_2BC(): pass

    label('loc_2BC')

    OP_25(0x01CB, -130, 250, 15900, 2000, 25000, 0x64, 0x00000000)

    Return()

# id: 0x0002 offset: 0x2D9
@scena.Code('ReInit')
def ReInit():
    SetMapFlags(0x00000080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 5, 0x655)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_42E',
    )

    SetScenaFlags(ScenaFlag(0x00CA, 5, 0x655))
    EventBegin(0x00)
    CameraMove(-70, 1000, 41330, 1000)
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010130616V#009F唉～怎么会这样！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130617V#012F真是相当坚固的锁呢……\n',
            '得先找到钥匙才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 6, 0x656)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F4',
    )

    ChrTalk(
        0x0108,
        (
            '#0080130618V#072F唔，\n',
            '那就只能暂时先到别的地方看看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_429')

    def _loc_3F4(): pass

    label('loc_3F4')

    ChrTalk(
        0x0108,
        (
            '#0080130619V#070F唔，\n',
            '去问问那个年轻的管家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x004C, 0x01, 0x0008)

    def _loc_429(): pass

    label('loc_429')

    EventEnd(0x01)

    Jump('loc_502')

    def _loc_42E(): pass

    label('loc_42E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 7, 0x657)),
            Expr.Return,
        ),
        'loc_4AB',
    )

    EventBegin(0x00)
    CameraMove(-70, 1000, 41330, 1000)
    SetScenaFlags(ScenaFlag(0x00CB, 0, 0x658))
    OP_71(0x0000, 0x0010)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '使用了',
            (TxtCtl.SetColor, 0x2),
            '备用钥匙',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    RemoveItem(0x036F, 1)
    PlaySE(115, 0x00, 0x64)
    Sleep(800)

    OP_64(0x00, 0x0001)
    EventEnd(0x01)

    Jump('loc_502')

    def _loc_4AB(): pass

    label('loc_4AB')

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_502(): pass

    label('loc_502')

    ClearMapFlags(0x00000080)

    Return()

# id: 0x0003 offset: 0x508
@scena.Code('func_03_508')
def func_03_508():
    EventBegin(0x00)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0102, 2)
    SetChrChipByIndex(0x0108, 4)
    SetChrPos(0x0101, 16560, 1000, -8020, 87)
    SetChrPos(0x0102, 15530, 1000, -8910, 135)
    SetChrPos(0x0108, 15490, 1000, -6910, 45)
    CameraMove(15530, 1000, -7950, 0)
    SetChrChipByIndex(0x0008, 6)
    SetChrChipByIndex(0x0009, 11)
    SetChrChipByIndex(0x000B, 8)
    SetChrChipByIndex(0x000C, 8)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x0008, 18910, 1000, 720, 180)
    SetChrPos(0x0009, 18910, 1000, 3690, 180)
    SetChrPos(0x000B, 18130, 1000, 2540, 180)
    SetChrPos(0x000C, 19750, 1000, 2310, 180)

    ChrTalk(
        0x0008,
        (
            '#2620130604V你……你们是什么人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_05F2')
    def lambda_05F2():
        CameraMove(18540, 1000, -4090, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_05F2)

    @scena.Lambda('lambda_060A')
    def lambda_060A():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_060A)

    SetChrChipByIndex(0x0008, 7)

    @scena.Lambda('lambda_061F')
    def lambda_061F():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_061F)

    Sleep(50)

    SetChrChipByIndex(0x0009, 12)

    @scena.Lambda('lambda_0644')
    def lambda_0644():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0644)

    Sleep(50)

    SetChrChipByIndex(0x000B, 9)

    @scena.Lambda('lambda_0669')
    def lambda_0669():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0669)

    Sleep(50)

    SetChrChipByIndex(0x000C, 9)

    @scena.Lambda('lambda_068E')
    def lambda_068E():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_068E)

    @scena.Lambda('lambda_06A9')
    def lambda_06A9():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_06A9)

    @scena.Lambda('lambda_06B7')
    def lambda_06B7():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_06B7)

    @scena.Lambda('lambda_06C5')
    def lambda_06C5():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_06C5)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0108, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)
    SetChrChipByIndex(0x0008, 6)
    SetChrSubChip(0x0008, 0)
    WaitForThreadExit(0x0009, 0x0001)
    SetChrChipByIndex(0x0009, 11)
    SetChrSubChip(0x0009, 0)
    WaitForThreadExit(0x000B, 0x0001)
    SetChrChipByIndex(0x000B, 8)
    SetChrSubChip(0x000B, 0)

    @scena.Lambda('lambda_0745')
    def lambda_0745():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0745')

    DispatchAsync2(0x000B, 0x0000, lambda_0745)

    WaitForThreadExit(0x000C, 0x0001)
    SetChrChipByIndex(0x000C, 8)
    SetChrSubChip(0x000C, 0)

    @scena.Lambda('lambda_0767')
    def lambda_0767():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0767')

    DispatchAsync2(0x000C, 0x0000, lambda_0767)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#2620130605V可疑的人，在那儿不许动！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0008, 7)

    @scena.Lambda('lambda_07A9')
    def lambda_07A9():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_07A9)

    Sleep(50)

    SetChrChipByIndex(0x0009, 12)

    @scena.Lambda('lambda_07C8')
    def lambda_07C8():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_07C8)

    Sleep(50)

    SetChrChipByIndex(0x000B, 9)

    @scena.Lambda('lambda_07E7')
    def lambda_07E7():
        OP_92(0x00FE, 0x0108, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_07E7)

    Sleep(50)

    SetChrChipByIndex(0x000C, 9)

    @scena.Lambda('lambda_0806')
    def lambda_0806():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0806)

    Sleep(400)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    Battle(0x000003AB, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_843'),
        (-1, 'loc_846'),
    )

    def _loc_843(): pass

    label('loc_843')

    OP_B4(0x00)

    Return()

    def _loc_846(): pass

    label('loc_846')

    EventBegin(0x00)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    SetChrPos(0x0101, 17530, 1000, -6110, 45)
    SetChrPos(0x0102, 18110, 1000, -4380, 180)
    SetChrPos(0x0108, 19360, 1000, -6190, 330)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 10)
    SetChrChipByIndex(0x0009, 10)
    ClearChrFlags(0x0008, 0x0001)
    ClearChrFlags(0x0009, 0x0001)
    SetChrFlags(0x0008, 0x0800)
    SetChrFlags(0x0009, 0x0800)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrPos(0x0008, 18460, 1000, -2860, 180)
    SetChrPos(0x0009, 19820, 1000, -3010, 135)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    CameraMove(17470, 1000, -4720, 0)
    OP_6C(315000, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010130608V#007F呼～解决了。\n',
            '冷不妨就跳出几个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130609V#012F还有相当数量的特务兵残留在离宫里面。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130610V好像定期在中庭的走廊巡逻。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130611V#072F没办法，若是被发现了，\n',
            '就只有让他们保持沉默了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x9EE
@scena.Code('func_04_9EE')
def func_04_9EE():
    EventBegin(0x00)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0102, 2)
    SetChrChipByIndex(0x0108, 4)
    SetChrPos(0x0101, -16350, 1000, -7540, 301)
    SetChrPos(0x0102, -16410, 1000, -8720, 243)
    SetChrPos(0x0108, -15040, 1000, -8100, 302)
    CameraMove(-15730, 1000, -8020, 0)
    SetChrChipByIndex(0x0008, 6)
    SetChrChipByIndex(0x0009, 11)
    SetChrChipByIndex(0x000B, 8)
    SetChrChipByIndex(0x000C, 8)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x0008, -19240, 1000, -50, 188)
    SetChrPos(0x0009, -19280, 1000, 2470, 180)
    SetChrPos(0x000B, -20160, 1000, 960, 180)
    SetChrPos(0x000C, -18110, 1000, 970, 180)

    ChrTalk(
        0x0008,
        (
            '#2620130604V你……你们是什么人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0AD8')
    def lambda_0AD8():
        CameraMove(-19130, 1000, -4630, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0AD8)

    @scena.Lambda('lambda_0AF0')
    def lambda_0AF0():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0AF0)

    SetChrChipByIndex(0x0008, 7)

    @scena.Lambda('lambda_0B05')
    def lambda_0B05():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0B05)

    Sleep(50)

    SetChrChipByIndex(0x0009, 12)

    @scena.Lambda('lambda_0B2A')
    def lambda_0B2A():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0B2A)

    Sleep(50)

    SetChrChipByIndex(0x000B, 9)

    @scena.Lambda('lambda_0B4F')
    def lambda_0B4F():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0B4F)

    Sleep(50)

    SetChrChipByIndex(0x000C, 9)

    @scena.Lambda('lambda_0B74')
    def lambda_0B74():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0B74)

    @scena.Lambda('lambda_0B8F')
    def lambda_0B8F():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B8F)

    @scena.Lambda('lambda_0B9D')
    def lambda_0B9D():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0B9D)

    @scena.Lambda('lambda_0BAB')
    def lambda_0BAB():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0BAB)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0108, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)
    SetChrChipByIndex(0x0008, 6)
    SetChrSubChip(0x0008, 0)
    WaitForThreadExit(0x0009, 0x0001)
    SetChrChipByIndex(0x0009, 11)
    SetChrSubChip(0x0009, 0)
    WaitForThreadExit(0x000B, 0x0001)
    SetChrChipByIndex(0x000B, 8)
    SetChrSubChip(0x000B, 0)

    @scena.Lambda('lambda_0C2B')
    def lambda_0C2B():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0C2B')

    DispatchAsync2(0x000B, 0x0000, lambda_0C2B)

    WaitForThreadExit(0x000C, 0x0001)
    SetChrChipByIndex(0x000C, 8)
    SetChrSubChip(0x000C, 0)

    @scena.Lambda('lambda_0C4D')
    def lambda_0C4D():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0C4D')

    DispatchAsync2(0x000C, 0x0000, lambda_0C4D)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#2620130605V可疑的人，在那儿不许动！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0008, 7)

    @scena.Lambda('lambda_0C8F')
    def lambda_0C8F():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0C8F)

    Sleep(50)

    SetChrChipByIndex(0x0009, 12)

    @scena.Lambda('lambda_0CAE')
    def lambda_0CAE():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0CAE)

    Sleep(50)

    SetChrChipByIndex(0x000B, 9)

    @scena.Lambda('lambda_0CCD')
    def lambda_0CCD():
        OP_92(0x00FE, 0x0102, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0CCD)

    Sleep(50)

    SetChrChipByIndex(0x000C, 9)

    @scena.Lambda('lambda_0CEC')
    def lambda_0CEC():
        OP_92(0x00FE, 0x0108, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0CEC)

    Sleep(400)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    Battle(0x000003AC, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_D29'),
        (-1, 'loc_D2C'),
    )

    def _loc_D29(): pass

    label('loc_D29')

    OP_B4(0x00)

    Return()

    def _loc_D2C(): pass

    label('loc_D2C')

    EventBegin(0x00)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    SetChrPos(0x0101, -18900, 1000, -6950, 14)
    SetChrPos(0x0102, -17970, 1000, -6160, 345)
    SetChrPos(0x0108, -20110, 1000, -5730, 45)
    SetChrPos(0x0101, -18900, 1000, -6950, 339)
    SetChrPos(0x0102, -18280, 1000, -5200, 225)
    SetChrPos(0x0108, -20110, 1000, -5730, 105)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 10)
    SetChrChipByIndex(0x0009, 10)
    ClearChrFlags(0x0008, 0x0001)
    ClearChrFlags(0x0009, 0x0001)
    SetChrFlags(0x0008, 0x0800)
    SetChrFlags(0x0009, 0x0800)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrPos(0x0008, -17200, 1000, -3390, 180)
    SetChrPos(0x0009, -18660, 1000, -3640, 225)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    CameraMove(-18490, 1000, -4850, 0)
    OP_6C(45000, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010130608V#007F呼～解决了。\n',
            '冷不妨就跳出几个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130609V#012F还有相当数量的特务兵残留在离宫里面。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130610V好像定期在中庭的走廊巡逻。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130611V#072F没办法，若是被发现了，\n',
            '就只有让他们保持沉默了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0xF07
@scena.Code('func_05_F07')
def func_05_F07():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F19',
    )

    Return()

    def _loc_F19(): pass

    label('loc_F19')

    EventBegin(0x00)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0102, 2)
    SetChrChipByIndex(0x0108, 4)
    SetChrPos(0x0101, 19940, 1000, 6790, 294)
    SetChrPos(0x0102, 21170, 1000, 6410, 326)
    SetChrPos(0x0108, 21290, 1000, 7450, 303)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0008, 19310, 1000, 13490, 173)
    SetChrPos(0x0009, 20360, 1000, 15020, 170)
    SetChrPos(0x000A, 18980, 1000, 14690, 186)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(19290, 1000, 10760, 1000)

    @scena.Lambda('lambda_0FFB')
    def lambda_0FFB():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0FFB)

    @scena.Lambda('lambda_1010')
    def lambda_1010():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1010)

    @scena.Lambda('lambda_1025')
    def lambda_1025():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1025)

    @scena.Lambda('lambda_103A')
    def lambda_103A():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_103A)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x1088
@scena.Code('func_06_1088')
def func_06_1088():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_109A',
    )

    Return()

    def _loc_109A(): pass

    label('loc_109A')

    EventBegin(0x00)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0102, 2)
    SetChrChipByIndex(0x0108, 4)
    SetChrPos(0x0101, 20250, 1000, 21120, 295)
    SetChrPos(0x0102, 20800, 1000, 20430, 2)
    SetChrPos(0x0108, 20970, 1000, 21870, 149)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0008, 19240, 1000, 31840, 174)
    SetChrPos(0x0009, 20580, 1000, 32970, 194)
    SetChrPos(0x000A, 18940, 1000, 32770, 160)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(19670, 1000, 32770, 1000)

    @scena.Lambda('lambda_117C')
    def lambda_117C():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_117C)

    @scena.Lambda('lambda_1191')
    def lambda_1191():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1191)

    @scena.Lambda('lambda_11A6')
    def lambda_11A6():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_11A6)

    @scena.Lambda('lambda_11BB')
    def lambda_11BB():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_11BB)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x1209
@scena.Code('func_07_1209')
def func_07_1209():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_121B',
    )

    Return()

    def _loc_121B(): pass

    label('loc_121B')

    EventBegin(0x00)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0102, 2)
    SetChrChipByIndex(0x0108, 4)
    SetChrPos(0x0101, 20270, 1000, 32830, 270)
    SetChrPos(0x0102, 21030, 1000, 32090, 267)
    SetChrPos(0x0108, 21160, 1000, 33550, 274)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0008, 12630, 1000, 35570, 101)
    SetChrPos(0x0009, 11450, 1000, 36350, 97)
    SetChrPos(0x000A, 11530, 1000, 34890, 88)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(12350, 1000, 35970, 1000)

    @scena.Lambda('lambda_12FD')
    def lambda_12FD():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_12FD)

    @scena.Lambda('lambda_1312')
    def lambda_1312():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1312)

    @scena.Lambda('lambda_1327')
    def lambda_1327():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1327)

    @scena.Lambda('lambda_133C')
    def lambda_133C():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_133C)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x138A
@scena.Code('func_08_138A')
def func_08_138A():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_139C',
    )

    Return()

    def _loc_139C(): pass

    label('loc_139C')

    EventBegin(0x00)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0102, 2)
    SetChrChipByIndex(0x0108, 4)
    SetChrPos(0x0101, 9090, 1000, 36810, 270)
    SetChrPos(0x0102, 9630, 1000, 37440, 270)
    SetChrPos(0x0108, 8380, 1000, 36730, 270)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0008, 400, 1000, 35050, 88)
    SetChrPos(0x0009, -330, 1000, 36110, 103)
    SetChrPos(0x000A, -640, 1000, 34500, 78)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(490, 1000, 35070, 1000)

    @scena.Lambda('lambda_147E')
    def lambda_147E():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_147E)

    @scena.Lambda('lambda_1493')
    def lambda_1493():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1493)

    @scena.Lambda('lambda_14A8')
    def lambda_14A8():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_14A8)

    @scena.Lambda('lambda_14BD')
    def lambda_14BD():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_14BD)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x150B
@scena.Code('func_09_150B')
def func_09_150B():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_151D',
    )

    Return()

    def _loc_151D(): pass

    label('loc_151D')

    EventBegin(0x00)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0102, 2)
    SetChrChipByIndex(0x0108, 4)
    SetChrPos(0x0101, -180, 1000, 40300, 186)
    SetChrPos(0x0102, 840, 1000, 40700, 166)
    SetChrPos(0x0108, -890, 1000, 40810, 198)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0008, 150, 250, 29590, 351)
    SetChrPos(0x0009, -440, 500, 30500, 356)
    SetChrPos(0x000A, 940, 500, 30620, 341)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(150, 250, 29590, 1000)

    @scena.Lambda('lambda_15FF')
    def lambda_15FF():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_15FF)

    @scena.Lambda('lambda_1614')
    def lambda_1614():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1614)

    @scena.Lambda('lambda_1629')
    def lambda_1629():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1629)

    @scena.Lambda('lambda_163E')
    def lambda_163E():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_163E)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x168C
@scena.Code('func_0A_168C')
def func_0A_168C():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_169E',
    )

    Return()

    def _loc_169E(): pass

    label('loc_169E')

    EventBegin(0x00)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0102, 2)
    SetChrChipByIndex(0x0108, 4)
    SetChrPos(0x0101, -8960, 1000, 36360, 83)
    SetChrPos(0x0102, -9650, 1000, 36960, 83)
    SetChrPos(0x0108, -7870, 1000, 36840, 87)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0008, 1650, 1000, 34820, 248)
    SetChrPos(0x0009, 2640, 1000, 35540, 277)
    SetChrPos(0x000A, 2540, 1000, 34230, 260)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(1650, 1000, 34820, 1000)

    @scena.Lambda('lambda_1780')
    def lambda_1780():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1780)

    @scena.Lambda('lambda_1795')
    def lambda_1795():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1795)

    @scena.Lambda('lambda_17AA')
    def lambda_17AA():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_17AA)

    @scena.Lambda('lambda_17BF')
    def lambda_17BF():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_17BF)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x180D
@scena.Code('func_0B_180D')
def func_0B_180D():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_181F',
    )

    Return()

    def _loc_181F(): pass

    label('loc_181F')

    EventBegin(0x00)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0102, 2)
    SetChrChipByIndex(0x0108, 4)
    SetChrPos(0x0101, -20560, 1000, 29250, 23)
    SetChrPos(0x0102, -21000, 1000, 28080, 60)
    SetChrPos(0x0108, -21470, 1000, 29440, 52)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0008, -16129, 1000, 34890, 224)
    SetChrPos(0x0009, -16560, 1000, 36340, 211)
    SetChrPos(0x000A, -17730, 1000, 36360, 209)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(-16560, 1000, 36340, 1000)

    @scena.Lambda('lambda_1901')
    def lambda_1901():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1901)

    @scena.Lambda('lambda_1916')
    def lambda_1916():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1916)

    @scena.Lambda('lambda_192B')
    def lambda_192B():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_192B)

    @scena.Lambda('lambda_1940')
    def lambda_1940():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1940)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x198E
@scena.Code('func_0C_198E')
def func_0C_198E():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19A0',
    )

    Return()

    def _loc_19A0(): pass

    label('loc_19A0')

    EventBegin(0x00)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0102, 2)
    SetChrChipByIndex(0x0108, 4)
    SetChrPos(0x0101, -20250, 1000, 20460, 144)
    SetChrPos(0x0102, -21290, 1000, 20210, 133)
    SetChrPos(0x0108, -20770, 1000, 21590, 119)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0008, -16300, 1000, 16040, 316)
    SetChrPos(0x0009, -15870, 750, 15030, 297)
    SetChrPos(0x000A, -15260, 750, 16170, 306)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(-16300, 1000, 16040, 1000)

    @scena.Lambda('lambda_1A82')
    def lambda_1A82():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1A82)

    @scena.Lambda('lambda_1A97')
    def lambda_1A97():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1A97)

    @scena.Lambda('lambda_1AAC')
    def lambda_1AAC():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1AAC)

    @scena.Lambda('lambda_1AC1')
    def lambda_1AC1():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1AC1)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x1B0F
@scena.Code('func_0D_1B0F')
def func_0D_1B0F():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B21',
    )

    Return()

    def _loc_1B21(): pass

    label('loc_1B21')

    EventBegin(0x00)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0102, 2)
    SetChrChipByIndex(0x0108, 4)
    SetChrPos(0x0101, -20590, 1000, 3380, 29)
    SetChrPos(0x0102, -21500, 1000, 3480, 55)
    SetChrPos(0x0108, -21000, 1000, 2080, 29)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0008, -19300, 1000, 10370, 167)
    SetChrPos(0x0009, -20480, 1000, 11180, 175)
    SetChrPos(0x000A, -18330, 1000, 10260, 167)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(-19300, 1000, 10370, 1000)

    @scena.Lambda('lambda_1C03')
    def lambda_1C03():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1C03)

    @scena.Lambda('lambda_1C18')
    def lambda_1C18():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1C18)

    @scena.Lambda('lambda_1C2D')
    def lambda_1C2D():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1C2D)

    @scena.Lambda('lambda_1C42')
    def lambda_1C42():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1C42)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
