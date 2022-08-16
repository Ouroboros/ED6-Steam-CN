import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4301   ._SN')

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

# id: 0xFFFF offset: 0x64
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

# id: 0x10000 offset: 0xA8
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

# id: 0x10001 offset: 0x112
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '军用犬',
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
            name                = '军用犬',
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
            name                = '军用犬',
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

# id: 0x10002 offset: 0x1D2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1D2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1D2
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
@scena.Code('Init')
def Init():
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
    Event(0, func_03_51C)

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
    Event(0, func_04_A20)

    def _loc_253(): pass

    label('loc_253')

    Jump('loc_295')

    def _loc_256(): pass

    label('loc_256')

    Event(0, func_0D_1B5F)

    Jump('loc_295')

    def _loc_25D(): pass

    label('loc_25D')

    Event(0, func_0C_19DE)

    Jump('loc_295')

    def _loc_264(): pass

    label('loc_264')

    Event(0, func_0B_185D)

    Jump('loc_295')

    def _loc_26B(): pass

    label('loc_26B')

    Event(0, func_0A_16DC)

    Jump('loc_295')

    def _loc_272(): pass

    label('loc_272')

    Event(0, func_09_155B)

    Jump('loc_295')

    def _loc_279(): pass

    label('loc_279')

    Event(0, func_08_13DA)

    Jump('loc_295')

    def _loc_280(): pass

    label('loc_280')

    Event(0, func_07_1259)

    Jump('loc_295')

    def _loc_287(): pass

    label('loc_287')

    Event(0, func_06_10D8)

    Jump('loc_295')

    def _loc_28E(): pass

    label('loc_28E')

    Event(0, func_05_F57)

    Jump('loc_295')

    def _loc_295(): pass

    label('loc_295')

    Return()

# id: 0x0001 offset: 0x296
@scena.Code('func_01_296')
def func_01_296():
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
@scena.Code('func_02_2D9')
def func_02_2D9():
    MapSetFlags(0x00000080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 5, 0x655)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_442',
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
    TalkSetChrName('')

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
        'loc_403',
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

    Jump('loc_43D')

    def _loc_403(): pass

    label('loc_403')

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

    def _loc_43D(): pass

    label('loc_43D')

    EventEnd(0x01)

    Jump('loc_516')

    def _loc_442(): pass

    label('loc_442')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 7, 0x657)),
            Expr.Return,
        ),
        'loc_4BF',
    )

    EventBegin(0x00)
    CameraMove(-70, 1000, 41330, 1000)
    SetScenaFlags(ScenaFlag(0x00CB, 0, 0x658))
    OP_71(0x0000, 0x0010)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

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

    Jump('loc_516')

    def _loc_4BF(): pass

    label('loc_4BF')

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

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

    def _loc_516(): pass

    label('loc_516')

    MapClearFlags(0x00000080)

    Return()

# id: 0x0003 offset: 0x51C
@scena.Code('func_03_51C')
def func_03_51C():
    EventBegin(0x00)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0108, 4)
    ChrSetPos(0x0101, 16560, 1000, -8020, 87)
    ChrSetPos(0x0102, 15530, 1000, -8910, 135)
    ChrSetPos(0x0108, 15490, 1000, -6910, 45)
    CameraMove(15530, 1000, -7950, 0)
    ChrSetChipByIndex(0x0008, 6)
    ChrSetChipByIndex(0x0009, 11)
    ChrSetChipByIndex(0x000B, 8)
    ChrSetChipByIndex(0x000C, 8)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x0008, 18910, 1000, 720, 180)
    ChrSetPos(0x0009, 18910, 1000, 3690, 180)
    ChrSetPos(0x000B, 18130, 1000, 2540, 180)
    ChrSetPos(0x000C, 19750, 1000, 2310, 180)

    ChrTalk(
        0x0008,
        (
            '#2620130604V你……你们是什么人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_060B')
    def lambda_060B():
        CameraMove(18540, 1000, -4090, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_060B)

    @scena.Lambda('lambda_0623')
    def lambda_0623():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0623)

    ChrSetChipByIndex(0x0008, 7)

    @scena.Lambda('lambda_0638')
    def lambda_0638():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0638)

    Sleep(50)

    ChrSetChipByIndex(0x0009, 12)

    @scena.Lambda('lambda_065D')
    def lambda_065D():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_065D)

    Sleep(50)

    ChrSetChipByIndex(0x000B, 9)

    @scena.Lambda('lambda_0682')
    def lambda_0682():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0682)

    Sleep(50)

    ChrSetChipByIndex(0x000C, 9)

    @scena.Lambda('lambda_06A7')
    def lambda_06A7():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_06A7)

    @scena.Lambda('lambda_06C2')
    def lambda_06C2():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_06C2)

    @scena.Lambda('lambda_06D0')
    def lambda_06D0():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_06D0)

    @scena.Lambda('lambda_06DE')
    def lambda_06DE():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_06DE)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0108, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)
    ChrSetChipByIndex(0x0008, 6)
    ChrSetSubChip(0x0008, 0)
    WaitForThreadExit(0x0009, 0x0001)
    ChrSetChipByIndex(0x0009, 11)
    ChrSetSubChip(0x0009, 0)
    WaitForThreadExit(0x000B, 0x0001)
    ChrSetChipByIndex(0x000B, 8)
    ChrSetSubChip(0x000B, 0)

    @scena.Lambda('lambda_075E')
    def lambda_075E():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_075E')

    DispatchAsync2(0x000B, 0x0000, lambda_075E)

    WaitForThreadExit(0x000C, 0x0001)
    ChrSetChipByIndex(0x000C, 8)
    ChrSetSubChip(0x000C, 0)

    @scena.Lambda('lambda_0780')
    def lambda_0780():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0780')

    DispatchAsync2(0x000C, 0x0000, lambda_0780)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#2620130605V可疑的人，在那儿不许动！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0008, 7)

    @scena.Lambda('lambda_07C7')
    def lambda_07C7():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_07C7)

    Sleep(50)

    ChrSetChipByIndex(0x0009, 12)

    @scena.Lambda('lambda_07E6')
    def lambda_07E6():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_07E6)

    Sleep(50)

    ChrSetChipByIndex(0x000B, 9)

    @scena.Lambda('lambda_0805')
    def lambda_0805():
        OP_92(0x00FE, 0x0108, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0805)

    Sleep(50)

    ChrSetChipByIndex(0x000C, 9)

    @scena.Lambda('lambda_0824')
    def lambda_0824():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0824)

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
        (0x00000001, 'loc_861'),
        (-1, 'loc_864'),
    )

    def _loc_861(): pass

    label('loc_861')

    OP_B4(0x00)

    Return()

    def _loc_864(): pass

    label('loc_864')

    EventBegin(0x00)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    ChrSetPos(0x0101, 17530, 1000, -6110, 45)
    ChrSetPos(0x0102, 18110, 1000, -4380, 180)
    ChrSetPos(0x0108, 19360, 1000, -6190, 330)

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

    ChrSetChipByIndex(0x0008, 10)
    ChrSetChipByIndex(0x0009, 10)
    ChrClearFlags(0x0008, 0x0001)
    ChrClearFlags(0x0009, 0x0001)
    ChrSetFlags(0x0008, 0x0800)
    ChrSetFlags(0x0009, 0x0800)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetPos(0x0008, 18460, 1000, -2860, 180)
    ChrSetPos(0x0009, 19820, 1000, -3010, 135)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
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

# id: 0x0004 offset: 0xA20
@scena.Code('func_04_A20')
def func_04_A20():
    EventBegin(0x00)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0108, 4)
    ChrSetPos(0x0101, -16350, 1000, -7540, 301)
    ChrSetPos(0x0102, -16410, 1000, -8720, 243)
    ChrSetPos(0x0108, -15040, 1000, -8100, 302)
    CameraMove(-15730, 1000, -8020, 0)
    ChrSetChipByIndex(0x0008, 6)
    ChrSetChipByIndex(0x0009, 11)
    ChrSetChipByIndex(0x000B, 8)
    ChrSetChipByIndex(0x000C, 8)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x0008, -19240, 1000, -50, 188)
    ChrSetPos(0x0009, -19280, 1000, 2470, 180)
    ChrSetPos(0x000B, -20160, 1000, 960, 180)
    ChrSetPos(0x000C, -18110, 1000, 970, 180)

    ChrTalk(
        0x0008,
        (
            '#2620130604V你……你们是什么人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0B0F')
    def lambda_0B0F():
        CameraMove(-19130, 1000, -4630, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0B0F)

    @scena.Lambda('lambda_0B27')
    def lambda_0B27():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0B27)

    ChrSetChipByIndex(0x0008, 7)

    @scena.Lambda('lambda_0B3C')
    def lambda_0B3C():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0B3C)

    Sleep(50)

    ChrSetChipByIndex(0x0009, 12)

    @scena.Lambda('lambda_0B61')
    def lambda_0B61():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0B61)

    Sleep(50)

    ChrSetChipByIndex(0x000B, 9)

    @scena.Lambda('lambda_0B86')
    def lambda_0B86():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0B86)

    Sleep(50)

    ChrSetChipByIndex(0x000C, 9)

    @scena.Lambda('lambda_0BAB')
    def lambda_0BAB():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0BAB)

    @scena.Lambda('lambda_0BC6')
    def lambda_0BC6():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0BC6)

    @scena.Lambda('lambda_0BD4')
    def lambda_0BD4():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0BD4)

    @scena.Lambda('lambda_0BE2')
    def lambda_0BE2():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0BE2)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0108, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)
    ChrSetChipByIndex(0x0008, 6)
    ChrSetSubChip(0x0008, 0)
    WaitForThreadExit(0x0009, 0x0001)
    ChrSetChipByIndex(0x0009, 11)
    ChrSetSubChip(0x0009, 0)
    WaitForThreadExit(0x000B, 0x0001)
    ChrSetChipByIndex(0x000B, 8)
    ChrSetSubChip(0x000B, 0)

    @scena.Lambda('lambda_0C62')
    def lambda_0C62():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0C62')

    DispatchAsync2(0x000B, 0x0000, lambda_0C62)

    WaitForThreadExit(0x000C, 0x0001)
    ChrSetChipByIndex(0x000C, 8)
    ChrSetSubChip(0x000C, 0)

    @scena.Lambda('lambda_0C84')
    def lambda_0C84():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0C84')

    DispatchAsync2(0x000C, 0x0000, lambda_0C84)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#2620130605V可疑的人，在那儿不许动！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0008, 7)

    @scena.Lambda('lambda_0CCB')
    def lambda_0CCB():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0CCB)

    Sleep(50)

    ChrSetChipByIndex(0x0009, 12)

    @scena.Lambda('lambda_0CEA')
    def lambda_0CEA():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0CEA)

    Sleep(50)

    ChrSetChipByIndex(0x000B, 9)

    @scena.Lambda('lambda_0D09')
    def lambda_0D09():
        OP_92(0x00FE, 0x0102, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0D09)

    Sleep(50)

    ChrSetChipByIndex(0x000C, 9)

    @scena.Lambda('lambda_0D28')
    def lambda_0D28():
        OP_92(0x00FE, 0x0108, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0D28)

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
        (0x00000001, 'loc_D65'),
        (-1, 'loc_D68'),
    )

    def _loc_D65(): pass

    label('loc_D65')

    OP_B4(0x00)

    Return()

    def _loc_D68(): pass

    label('loc_D68')

    EventBegin(0x00)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    ChrSetPos(0x0101, -18900, 1000, -6950, 14)
    ChrSetPos(0x0102, -17970, 1000, -6160, 345)
    ChrSetPos(0x0108, -20110, 1000, -5730, 45)
    ChrSetPos(0x0101, -18900, 1000, -6950, 339)
    ChrSetPos(0x0102, -18280, 1000, -5200, 225)
    ChrSetPos(0x0108, -20110, 1000, -5730, 105)

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

    ChrSetChipByIndex(0x0008, 10)
    ChrSetChipByIndex(0x0009, 10)
    ChrClearFlags(0x0008, 0x0001)
    ChrClearFlags(0x0009, 0x0001)
    ChrSetFlags(0x0008, 0x0800)
    ChrSetFlags(0x0009, 0x0800)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetPos(0x0008, -17200, 1000, -3390, 180)
    ChrSetPos(0x0009, -18660, 1000, -3640, 225)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
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

# id: 0x0005 offset: 0xF57
@scena.Code('func_05_F57')
def func_05_F57():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F69',
    )

    Return()

    def _loc_F69(): pass

    label('loc_F69')

    EventBegin(0x00)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0108, 4)
    ChrSetPos(0x0101, 19940, 1000, 6790, 294)
    ChrSetPos(0x0102, 21170, 1000, 6410, 326)
    ChrSetPos(0x0108, 21290, 1000, 7450, 303)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0008, 19310, 1000, 13490, 173)
    ChrSetPos(0x0009, 20360, 1000, 15020, 170)
    ChrSetPos(0x000A, 18980, 1000, 14690, 186)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(19290, 1000, 10760, 1000)

    @scena.Lambda('lambda_104B')
    def lambda_104B():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_104B)

    @scena.Lambda('lambda_1060')
    def lambda_1060():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1060)

    @scena.Lambda('lambda_1075')
    def lambda_1075():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1075)

    @scena.Lambda('lambda_108A')
    def lambda_108A():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_108A)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x10D8
@scena.Code('func_06_10D8')
def func_06_10D8():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10EA',
    )

    Return()

    def _loc_10EA(): pass

    label('loc_10EA')

    EventBegin(0x00)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0108, 4)
    ChrSetPos(0x0101, 20250, 1000, 21120, 295)
    ChrSetPos(0x0102, 20800, 1000, 20430, 2)
    ChrSetPos(0x0108, 20970, 1000, 21870, 149)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0008, 19240, 1000, 31840, 174)
    ChrSetPos(0x0009, 20580, 1000, 32970, 194)
    ChrSetPos(0x000A, 18940, 1000, 32770, 160)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(19670, 1000, 32770, 1000)

    @scena.Lambda('lambda_11CC')
    def lambda_11CC():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_11CC)

    @scena.Lambda('lambda_11E1')
    def lambda_11E1():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_11E1)

    @scena.Lambda('lambda_11F6')
    def lambda_11F6():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_11F6)

    @scena.Lambda('lambda_120B')
    def lambda_120B():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_120B)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x1259
@scena.Code('func_07_1259')
def func_07_1259():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_126B',
    )

    Return()

    def _loc_126B(): pass

    label('loc_126B')

    EventBegin(0x00)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0108, 4)
    ChrSetPos(0x0101, 20270, 1000, 32830, 270)
    ChrSetPos(0x0102, 21030, 1000, 32090, 267)
    ChrSetPos(0x0108, 21160, 1000, 33550, 274)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0008, 12630, 1000, 35570, 101)
    ChrSetPos(0x0009, 11450, 1000, 36350, 97)
    ChrSetPos(0x000A, 11530, 1000, 34890, 88)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(12350, 1000, 35970, 1000)

    @scena.Lambda('lambda_134D')
    def lambda_134D():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_134D)

    @scena.Lambda('lambda_1362')
    def lambda_1362():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1362)

    @scena.Lambda('lambda_1377')
    def lambda_1377():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1377)

    @scena.Lambda('lambda_138C')
    def lambda_138C():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_138C)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x13DA
@scena.Code('func_08_13DA')
def func_08_13DA():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13EC',
    )

    Return()

    def _loc_13EC(): pass

    label('loc_13EC')

    EventBegin(0x00)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0108, 4)
    ChrSetPos(0x0101, 9090, 1000, 36810, 270)
    ChrSetPos(0x0102, 9630, 1000, 37440, 270)
    ChrSetPos(0x0108, 8380, 1000, 36730, 270)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0008, 400, 1000, 35050, 88)
    ChrSetPos(0x0009, -330, 1000, 36110, 103)
    ChrSetPos(0x000A, -640, 1000, 34500, 78)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(490, 1000, 35070, 1000)

    @scena.Lambda('lambda_14CE')
    def lambda_14CE():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_14CE)

    @scena.Lambda('lambda_14E3')
    def lambda_14E3():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_14E3)

    @scena.Lambda('lambda_14F8')
    def lambda_14F8():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_14F8)

    @scena.Lambda('lambda_150D')
    def lambda_150D():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_150D)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x155B
@scena.Code('func_09_155B')
def func_09_155B():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_156D',
    )

    Return()

    def _loc_156D(): pass

    label('loc_156D')

    EventBegin(0x00)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0108, 4)
    ChrSetPos(0x0101, -180, 1000, 40300, 186)
    ChrSetPos(0x0102, 840, 1000, 40700, 166)
    ChrSetPos(0x0108, -890, 1000, 40810, 198)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0008, 150, 250, 29590, 351)
    ChrSetPos(0x0009, -440, 500, 30500, 356)
    ChrSetPos(0x000A, 940, 500, 30620, 341)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(150, 250, 29590, 1000)

    @scena.Lambda('lambda_164F')
    def lambda_164F():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_164F)

    @scena.Lambda('lambda_1664')
    def lambda_1664():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1664)

    @scena.Lambda('lambda_1679')
    def lambda_1679():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1679)

    @scena.Lambda('lambda_168E')
    def lambda_168E():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_168E)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x16DC
@scena.Code('func_0A_16DC')
def func_0A_16DC():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16EE',
    )

    Return()

    def _loc_16EE(): pass

    label('loc_16EE')

    EventBegin(0x00)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0108, 4)
    ChrSetPos(0x0101, -8960, 1000, 36360, 83)
    ChrSetPos(0x0102, -9650, 1000, 36960, 83)
    ChrSetPos(0x0108, -7870, 1000, 36840, 87)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0008, 1650, 1000, 34820, 248)
    ChrSetPos(0x0009, 2640, 1000, 35540, 277)
    ChrSetPos(0x000A, 2540, 1000, 34230, 260)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(1650, 1000, 34820, 1000)

    @scena.Lambda('lambda_17D0')
    def lambda_17D0():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_17D0)

    @scena.Lambda('lambda_17E5')
    def lambda_17E5():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_17E5)

    @scena.Lambda('lambda_17FA')
    def lambda_17FA():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_17FA)

    @scena.Lambda('lambda_180F')
    def lambda_180F():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_180F)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x185D
@scena.Code('func_0B_185D')
def func_0B_185D():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_186F',
    )

    Return()

    def _loc_186F(): pass

    label('loc_186F')

    EventBegin(0x00)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0108, 4)
    ChrSetPos(0x0101, -20560, 1000, 29250, 23)
    ChrSetPos(0x0102, -21000, 1000, 28080, 60)
    ChrSetPos(0x0108, -21470, 1000, 29440, 52)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0008, -16129, 1000, 34890, 224)
    ChrSetPos(0x0009, -16560, 1000, 36340, 211)
    ChrSetPos(0x000A, -17730, 1000, 36360, 209)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(-16560, 1000, 36340, 1000)

    @scena.Lambda('lambda_1951')
    def lambda_1951():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1951)

    @scena.Lambda('lambda_1966')
    def lambda_1966():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1966)

    @scena.Lambda('lambda_197B')
    def lambda_197B():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_197B)

    @scena.Lambda('lambda_1990')
    def lambda_1990():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1990)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x19DE
@scena.Code('func_0C_19DE')
def func_0C_19DE():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19F0',
    )

    Return()

    def _loc_19F0(): pass

    label('loc_19F0')

    EventBegin(0x00)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0108, 4)
    ChrSetPos(0x0101, -20250, 1000, 20460, 144)
    ChrSetPos(0x0102, -21290, 1000, 20210, 133)
    ChrSetPos(0x0108, -20770, 1000, 21590, 119)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0008, -16300, 1000, 16040, 316)
    ChrSetPos(0x0009, -15870, 750, 15030, 297)
    ChrSetPos(0x000A, -15260, 750, 16170, 306)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(-16300, 1000, 16040, 1000)

    @scena.Lambda('lambda_1AD2')
    def lambda_1AD2():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1AD2)

    @scena.Lambda('lambda_1AE7')
    def lambda_1AE7():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1AE7)

    @scena.Lambda('lambda_1AFC')
    def lambda_1AFC():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1AFC)

    @scena.Lambda('lambda_1B11')
    def lambda_1B11():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1B11)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x1B5F
@scena.Code('func_0D_1B5F')
def func_0D_1B5F():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B71',
    )

    Return()

    def _loc_1B71(): pass

    label('loc_1B71')

    EventBegin(0x00)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0108, 4)
    ChrSetPos(0x0101, -20590, 1000, 3380, 29)
    ChrSetPos(0x0102, -21500, 1000, 3480, 55)
    ChrSetPos(0x0108, -21000, 1000, 2080, 29)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0008, -19300, 1000, 10370, 167)
    ChrSetPos(0x0009, -20480, 1000, 11180, 175)
    ChrSetPos(0x000A, -18330, 1000, 10260, 167)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(-19300, 1000, 10370, 1000)

    @scena.Lambda('lambda_1C53')
    def lambda_1C53():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1C53)

    @scena.Lambda('lambda_1C68')
    def lambda_1C68():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1C68)

    @scena.Lambda('lambda_1C7D')
    def lambda_1C7D():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1C7D)

    @scena.Lambda('lambda_1C92')
    def lambda_1C92():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1C92)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
