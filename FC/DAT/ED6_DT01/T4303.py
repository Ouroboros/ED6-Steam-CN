import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4303_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4303   ._SN')

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
    header.mapModel       = 'T4303.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1910
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
    ]

# id: 0x10002 offset: 0x102
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

# id: 0x10003 offset: 0x1C2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1C2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1C2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1C2
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_1F6'),
        (0x00000064, 'loc_20C'),
        (0x00000066, 'loc_222'),
        (0x00000067, 'loc_229'),
        (0x00000068, 'loc_230'),
        (0x00000069, 'loc_237'),
        (0x0000006A, 'loc_23E'),
        (0x0000006B, 'loc_245'),
        (0x0000006C, 'loc_24C'),
        (0x0000006D, 'loc_253'),
        (0x0000006E, 'loc_25A'),
        (-1, 'loc_261'),
    )

    def _loc_1F6(): pass

    label('loc_1F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 3, 0x653)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 2, 0x652)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_209',
    )

    SetScenaFlags(ScenaFlag(0x00CA, 3, 0x653))
    Event(0, 0x0002)

    def _loc_209(): pass

    label('loc_209')

    Jump('loc_261')

    def _loc_20C(): pass

    label('loc_20C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 3, 0x653)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 2, 0x652)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_21F',
    )

    SetScenaFlags(ScenaFlag(0x00CA, 3, 0x653))
    Event(0, 0x0003)

    def _loc_21F(): pass

    label('loc_21F')

    Jump('loc_261')

    def _loc_222(): pass

    label('loc_222')

    Event(0, 0x000C)

    Jump('loc_261')

    def _loc_229(): pass

    label('loc_229')

    Event(0, 0x000B)

    Jump('loc_261')

    def _loc_230(): pass

    label('loc_230')

    Event(0, 0x000A)

    Jump('loc_261')

    def _loc_237(): pass

    label('loc_237')

    Event(0, 0x0009)

    Jump('loc_261')

    def _loc_23E(): pass

    label('loc_23E')

    Event(0, 0x0008)

    Jump('loc_261')

    def _loc_245(): pass

    label('loc_245')

    Event(0, 0x0007)

    Jump('loc_261')

    def _loc_24C(): pass

    label('loc_24C')

    Event(0, 0x0006)

    Jump('loc_261')

    def _loc_253(): pass

    label('loc_253')

    Event(0, 0x0005)

    Jump('loc_261')

    def _loc_25A(): pass

    label('loc_25A')

    Event(0, 0x0004)

    Jump('loc_261')

    def _loc_261(): pass

    label('loc_261')

    Return()

# id: 0x0001 offset: 0x262
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -128000, -112000, 196706)

    Return()

# id: 0x0002 offset: 0x275
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0102, 2)
    SetChrChipByIndex(0x0108, 4)
    SetChrPos(0x0101, 16560, 1000, -8020, 87)
    SetChrPos(0x0102, 15530, 1000, -8910, 135)
    SetChrPos(0x0108, 15490, 1000, -6910, 45)
    CameraMove(15530, 1000, -7950, 0)
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

    @scena.Lambda('lambda_034B')
    def lambda_034B():
        CameraMove(18540, 1000, -4090, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_034B)

    @scena.Lambda('lambda_0363')
    def lambda_0363():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0363)

    @scena.Lambda('lambda_0373')
    def lambda_0373():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0373)

    @scena.Lambda('lambda_038E')
    def lambda_038E():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_038E)

    @scena.Lambda('lambda_03A9')
    def lambda_03A9():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_03A9)

    @scena.Lambda('lambda_03C4')
    def lambda_03C4():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_03C4)

    @scena.Lambda('lambda_03DF')
    def lambda_03DF():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_03DF)

    @scena.Lambda('lambda_03ED')
    def lambda_03ED():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_03ED)

    @scena.Lambda('lambda_03FB')
    def lambda_03FB():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_03FB)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0108, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0009,
        (
            '可疑的人，在那儿不许动！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0471')
    def lambda_0471():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0471)

    @scena.Lambda('lambda_0486')
    def lambda_0486():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0486)

    @scena.Lambda('lambda_049B')
    def lambda_049B():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_049B)

    @scena.Lambda('lambda_04B0')
    def lambda_04B0():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_04B0)

    Sleep(500)

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
        (0x00000001, 'loc_4ED'),
        (-1, 'loc_4F0'),
    )

    def _loc_4ED(): pass

    label('loc_4ED')

    OP_B4(0x00)

    Return()

    def _loc_4F0(): pass

    label('loc_4F0')

    EventBegin(0x00)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    SetChrPos(0x0101, 17040, 1000, -5470, 19)
    SetChrPos(0x0102, 16580, 1000, -3860, 45)
    SetChrPos(0x0108, 18690, 1000, -6040, 11)

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

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 10)
    SetChrChipByIndex(0x0009, 10)
    SetChrChipByIndex(0x000A, 10)
    SetChrPos(0x0008, 19930, 1000, -3920, 190)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    CameraMove(17470, 1000, -4720, 0)
    OP_6C(315000, 1000)

    ChrTalk(
        0x0101,
        (
            '#000F呼～解决了。\n',
            '冷不妨就跳出几个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F还有相当数量的特务兵\n',
            '残留在离宫里面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130610V好像定期在中庭\n',
            '的走廊巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F没办法，若是被发现了\n',
            '就只有让他们保持沉默了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x654
@scena.Code('func_03_654')
def func_03_654():
    EventBegin(0x00)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0102, 2)
    SetChrChipByIndex(0x0108, 4)
    SetChrPos(0x0101, -16350, 1000, -7540, 301)
    SetChrPos(0x0102, -16410, 1000, -8720, 243)
    SetChrPos(0x0108, -15040, 1000, -8100, 302)
    CameraMove(-15730, 1000, -8020, 0)
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

    @scena.Lambda('lambda_072A')
    def lambda_072A():
        CameraMove(-19130, 1000, -4630, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_072A)

    @scena.Lambda('lambda_0742')
    def lambda_0742():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0742)

    @scena.Lambda('lambda_0752')
    def lambda_0752():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0752)

    @scena.Lambda('lambda_076D')
    def lambda_076D():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_076D)

    @scena.Lambda('lambda_0788')
    def lambda_0788():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0788)

    @scena.Lambda('lambda_07A3')
    def lambda_07A3():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_07A3)

    @scena.Lambda('lambda_07BE')
    def lambda_07BE():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07BE)

    @scena.Lambda('lambda_07CC')
    def lambda_07CC():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_07CC)

    @scena.Lambda('lambda_07DA')
    def lambda_07DA():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_07DA)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0108, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0009,
        (
            '可疑的人，在那儿不许动！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0850')
    def lambda_0850():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0850)

    @scena.Lambda('lambda_0865')
    def lambda_0865():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0865)

    @scena.Lambda('lambda_087A')
    def lambda_087A():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_087A)

    @scena.Lambda('lambda_088F')
    def lambda_088F():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_088F)

    Sleep(500)

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
        (0x00000001, 'loc_8CC'),
        (-1, 'loc_8CF'),
    )

    def _loc_8CC(): pass

    label('loc_8CC')

    OP_B4(0x00)

    Return()

    def _loc_8CF(): pass

    label('loc_8CF')

    EventBegin(0x00)

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

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 10)
    SetChrChipByIndex(0x0009, 10)
    SetChrChipByIndex(0x000A, 10)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    SetChrPos(0x0101, -18900, 1000, -6950, 14)
    SetChrPos(0x0102, -17970, 1000, -6160, 345)
    SetChrPos(0x0108, -20110, 1000, -5730, 45)
    SetChrPos(0x0008, -17200, 1000, -3390, 270)
    SetChrPos(0x0009, -18660, 1000, -3640, 270)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    CameraMove(-18490, 1000, -4850, 0)
    OP_6C(45000, 0)

    ChrTalk(
        0x0101,
        (
            '#000F呼～解决了。\n',
            '冷不妨就跳出几个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F还有相当数量的特务兵\n',
            '残留在离宫里面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130610V好像定期在中庭\n',
            '的走廊巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F没办法，若是被发现了\n',
            '就只有让他们保持沉默了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0xA44
@scena.Code('func_04_A44')
def func_04_A44():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A56',
    )

    Return()

    def _loc_A56(): pass

    label('loc_A56')

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

    @scena.Lambda('lambda_0B38')
    def lambda_0B38():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0B38)

    @scena.Lambda('lambda_0B4D')
    def lambda_0B4D():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0B4D)

    @scena.Lambda('lambda_0B62')
    def lambda_0B62():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0B62)

    @scena.Lambda('lambda_0B77')
    def lambda_0B77():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0B77)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)

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

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 10)
    SetChrChipByIndex(0x0009, 10)
    SetChrChipByIndex(0x000A, 10)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0xBE6
@scena.Code('func_05_BE6')
def func_05_BE6():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BF8',
    )

    Return()

    def _loc_BF8(): pass

    label('loc_BF8')

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

    @scena.Lambda('lambda_0CDA')
    def lambda_0CDA():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0CDA)

    @scena.Lambda('lambda_0CEF')
    def lambda_0CEF():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0CEF)

    @scena.Lambda('lambda_0D04')
    def lambda_0D04():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0D04)

    @scena.Lambda('lambda_0D19')
    def lambda_0D19():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0D19)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)

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

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 10)
    SetChrChipByIndex(0x0009, 10)
    SetChrChipByIndex(0x000A, 10)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0xD88
@scena.Code('func_06_D88')
def func_06_D88():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D9A',
    )

    Return()

    def _loc_D9A(): pass

    label('loc_D9A')

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

    @scena.Lambda('lambda_0E7C')
    def lambda_0E7C():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0E7C)

    @scena.Lambda('lambda_0E91')
    def lambda_0E91():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0E91)

    @scena.Lambda('lambda_0EA6')
    def lambda_0EA6():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0EA6)

    @scena.Lambda('lambda_0EBB')
    def lambda_0EBB():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0EBB)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)

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

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 10)
    SetChrChipByIndex(0x0009, 10)
    SetChrChipByIndex(0x000A, 10)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0xF2A
@scena.Code('func_07_F2A')
def func_07_F2A():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F3C',
    )

    Return()

    def _loc_F3C(): pass

    label('loc_F3C')

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

    @scena.Lambda('lambda_101E')
    def lambda_101E():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_101E)

    @scena.Lambda('lambda_1033')
    def lambda_1033():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1033)

    @scena.Lambda('lambda_1048')
    def lambda_1048():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1048)

    @scena.Lambda('lambda_105D')
    def lambda_105D():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_105D)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)

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

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 10)
    SetChrChipByIndex(0x0009, 10)
    SetChrChipByIndex(0x000A, 10)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x10CC
@scena.Code('func_08_10CC')
def func_08_10CC():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10DE',
    )

    Return()

    def _loc_10DE(): pass

    label('loc_10DE')

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

    @scena.Lambda('lambda_11C0')
    def lambda_11C0():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_11C0)

    @scena.Lambda('lambda_11D5')
    def lambda_11D5():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_11D5)

    @scena.Lambda('lambda_11EA')
    def lambda_11EA():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_11EA)

    @scena.Lambda('lambda_11FF')
    def lambda_11FF():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_11FF)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)

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

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 10)
    SetChrChipByIndex(0x0009, 10)
    SetChrChipByIndex(0x000A, 10)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x126E
@scena.Code('func_09_126E')
def func_09_126E():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1280',
    )

    Return()

    def _loc_1280(): pass

    label('loc_1280')

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

    @scena.Lambda('lambda_1362')
    def lambda_1362():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1362)

    @scena.Lambda('lambda_1377')
    def lambda_1377():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1377)

    @scena.Lambda('lambda_138C')
    def lambda_138C():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_138C)

    @scena.Lambda('lambda_13A1')
    def lambda_13A1():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_13A1)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)

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

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 10)
    SetChrChipByIndex(0x0009, 10)
    SetChrChipByIndex(0x000A, 10)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x1410
@scena.Code('func_0A_1410')
def func_0A_1410():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1422',
    )

    Return()

    def _loc_1422(): pass

    label('loc_1422')

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

    @scena.Lambda('lambda_1504')
    def lambda_1504():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1504)

    @scena.Lambda('lambda_1519')
    def lambda_1519():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1519)

    @scena.Lambda('lambda_152E')
    def lambda_152E():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_152E)

    @scena.Lambda('lambda_1543')
    def lambda_1543():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1543)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)

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

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 10)
    SetChrChipByIndex(0x0009, 10)
    SetChrChipByIndex(0x000A, 10)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x15B2
@scena.Code('func_0B_15B2')
def func_0B_15B2():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15C4',
    )

    Return()

    def _loc_15C4(): pass

    label('loc_15C4')

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

    @scena.Lambda('lambda_16A6')
    def lambda_16A6():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_16A6)

    @scena.Lambda('lambda_16BB')
    def lambda_16BB():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_16BB)

    @scena.Lambda('lambda_16D0')
    def lambda_16D0():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_16D0)

    @scena.Lambda('lambda_16E5')
    def lambda_16E5():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_16E5)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)

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

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 10)
    SetChrChipByIndex(0x0009, 10)
    SetChrChipByIndex(0x000A, 10)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x1754
@scena.Code('func_0C_1754')
def func_0C_1754():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1766',
    )

    Return()

    def _loc_1766(): pass

    label('loc_1766')

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

    @scena.Lambda('lambda_1848')
    def lambda_1848():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1848)

    @scena.Lambda('lambda_185D')
    def lambda_185D():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_185D)

    @scena.Lambda('lambda_1872')
    def lambda_1872():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1872)

    @scena.Lambda('lambda_1887')
    def lambda_1887():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1887)

    Sleep(800)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)

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

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 10)
    SetChrChipByIndex(0x0009, 10)
    SetChrChipByIndex(0x000A, 10)
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
