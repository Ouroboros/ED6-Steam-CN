import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4303_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4303   ._SN')

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
    ]

# id: 0x10001 offset: 0x102
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
            dword_10            = 7,
            chipIndex           = 7,
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

# id: 0x10002 offset: 0x1C2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1C2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1C2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1C2
@scena.Code('Init')
def Init():
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
    Event(0, func_02_275)

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
    Event(0, func_03_65E)

    def _loc_21F(): pass

    label('loc_21F')

    Jump('loc_261')

    def _loc_222(): pass

    label('loc_222')

    Event(0, func_0C_1768)

    Jump('loc_261')

    def _loc_229(): pass

    label('loc_229')

    Event(0, func_0B_15C6)

    Jump('loc_261')

    def _loc_230(): pass

    label('loc_230')

    Event(0, func_0A_1424)

    Jump('loc_261')

    def _loc_237(): pass

    label('loc_237')

    Event(0, func_09_1282)

    Jump('loc_261')

    def _loc_23E(): pass

    label('loc_23E')

    Event(0, func_08_10E0)

    Jump('loc_261')

    def _loc_245(): pass

    label('loc_245')

    Event(0, func_07_F3E)

    Jump('loc_261')

    def _loc_24C(): pass

    label('loc_24C')

    Event(0, func_06_D9C)

    Jump('loc_261')

    def _loc_253(): pass

    label('loc_253')

    Event(0, func_05_BFA)

    Jump('loc_261')

    def _loc_25A(): pass

    label('loc_25A')

    Event(0, func_04_A58)

    Jump('loc_261')

    def _loc_261(): pass

    label('loc_261')

    Return()

# id: 0x0001 offset: 0x262
@scena.Code('func_01_262')
def func_01_262():
    OP_16(0x02, 4000, -128000, -112000, 196706)

    Return()

# id: 0x0002 offset: 0x275
@scena.Code('func_02_275')
def func_02_275():
    EventBegin(0x00)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0108, 4)
    ChrSetPos(0x0101, 16560, 1000, -8020, 87)
    ChrSetPos(0x0102, 15530, 1000, -8910, 135)
    ChrSetPos(0x0108, 15490, 1000, -6910, 45)
    CameraMove(15530, 1000, -7950, 0)
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

    @scena.Lambda('lambda_0350')
    def lambda_0350():
        CameraMove(18540, 1000, -4090, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0350)

    @scena.Lambda('lambda_0368')
    def lambda_0368():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0368)

    @scena.Lambda('lambda_0378')
    def lambda_0378():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0378)

    @scena.Lambda('lambda_0393')
    def lambda_0393():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0393)

    @scena.Lambda('lambda_03AE')
    def lambda_03AE():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_03AE)

    @scena.Lambda('lambda_03C9')
    def lambda_03C9():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_03C9)

    @scena.Lambda('lambda_03E4')
    def lambda_03E4():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_03E4)

    @scena.Lambda('lambda_03F2')
    def lambda_03F2():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_03F2)

    @scena.Lambda('lambda_0400')
    def lambda_0400():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0400)

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

    @scena.Lambda('lambda_0476')
    def lambda_0476():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0476)

    @scena.Lambda('lambda_048B')
    def lambda_048B():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_048B)

    @scena.Lambda('lambda_04A0')
    def lambda_04A0():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_04A0)

    @scena.Lambda('lambda_04B5')
    def lambda_04B5():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_04B5)

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
        (0x00000001, 'loc_4F2'),
        (-1, 'loc_4F5'),
    )

    def _loc_4F2(): pass

    label('loc_4F2')

    OP_B4(0x00)

    Return()

    def _loc_4F5(): pass

    label('loc_4F5')

    EventBegin(0x00)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    ChrSetPos(0x0101, 17040, 1000, -5470, 19)
    ChrSetPos(0x0102, 16580, 1000, -3860, 45)
    ChrSetPos(0x0108, 18690, 1000, -6040, 11)

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

    ChrSetChipByIndex(0x0008, 10)
    ChrSetChipByIndex(0x0009, 10)
    ChrSetChipByIndex(0x000A, 10)
    ChrSetPos(0x0008, 19930, 1000, -3920, 190)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
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

# id: 0x0003 offset: 0x65E
@scena.Code('func_03_65E')
def func_03_65E():
    EventBegin(0x00)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0108, 4)
    ChrSetPos(0x0101, -16350, 1000, -7540, 301)
    ChrSetPos(0x0102, -16410, 1000, -8720, 243)
    ChrSetPos(0x0108, -15040, 1000, -8100, 302)
    CameraMove(-15730, 1000, -8020, 0)
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

    @scena.Lambda('lambda_0739')
    def lambda_0739():
        CameraMove(-19130, 1000, -4630, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0739)

    @scena.Lambda('lambda_0751')
    def lambda_0751():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0751)

    @scena.Lambda('lambda_0761')
    def lambda_0761():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0761)

    @scena.Lambda('lambda_077C')
    def lambda_077C():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_077C)

    @scena.Lambda('lambda_0797')
    def lambda_0797():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0797)

    @scena.Lambda('lambda_07B2')
    def lambda_07B2():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_07B2)

    @scena.Lambda('lambda_07CD')
    def lambda_07CD():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07CD)

    @scena.Lambda('lambda_07DB')
    def lambda_07DB():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_07DB)

    @scena.Lambda('lambda_07E9')
    def lambda_07E9():
        ChrTurnDirection(0x00FE, 0x0008, 800)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_07E9)

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

    @scena.Lambda('lambda_085F')
    def lambda_085F():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_085F)

    @scena.Lambda('lambda_0874')
    def lambda_0874():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0874)

    @scena.Lambda('lambda_0889')
    def lambda_0889():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0889)

    @scena.Lambda('lambda_089E')
    def lambda_089E():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_089E)

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
        (0x00000001, 'loc_8DB'),
        (-1, 'loc_8DE'),
    )

    def _loc_8DB(): pass

    label('loc_8DB')

    OP_B4(0x00)

    Return()

    def _loc_8DE(): pass

    label('loc_8DE')

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

    ChrSetChipByIndex(0x0008, 10)
    ChrSetChipByIndex(0x0009, 10)
    ChrSetChipByIndex(0x000A, 10)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    ChrSetPos(0x0101, -18900, 1000, -6950, 14)
    ChrSetPos(0x0102, -17970, 1000, -6160, 345)
    ChrSetPos(0x0108, -20110, 1000, -5730, 45)
    ChrSetPos(0x0008, -17200, 1000, -3390, 270)
    ChrSetPos(0x0009, -18660, 1000, -3640, 270)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
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

# id: 0x0004 offset: 0xA58
@scena.Code('func_04_A58')
def func_04_A58():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A6A',
    )

    Return()

    def _loc_A6A(): pass

    label('loc_A6A')

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

    @scena.Lambda('lambda_0B4C')
    def lambda_0B4C():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0B4C)

    @scena.Lambda('lambda_0B61')
    def lambda_0B61():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0B61)

    @scena.Lambda('lambda_0B76')
    def lambda_0B76():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0B76)

    @scena.Lambda('lambda_0B8B')
    def lambda_0B8B():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0B8B)

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

    ChrSetChipByIndex(0x0008, 10)
    ChrSetChipByIndex(0x0009, 10)
    ChrSetChipByIndex(0x000A, 10)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0xBFA
@scena.Code('func_05_BFA')
def func_05_BFA():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C0C',
    )

    Return()

    def _loc_C0C(): pass

    label('loc_C0C')

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

    @scena.Lambda('lambda_0CEE')
    def lambda_0CEE():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0CEE)

    @scena.Lambda('lambda_0D03')
    def lambda_0D03():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0D03)

    @scena.Lambda('lambda_0D18')
    def lambda_0D18():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0D18)

    @scena.Lambda('lambda_0D2D')
    def lambda_0D2D():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0D2D)

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

    ChrSetChipByIndex(0x0008, 10)
    ChrSetChipByIndex(0x0009, 10)
    ChrSetChipByIndex(0x000A, 10)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0xD9C
@scena.Code('func_06_D9C')
def func_06_D9C():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DAE',
    )

    Return()

    def _loc_DAE(): pass

    label('loc_DAE')

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

    @scena.Lambda('lambda_0E90')
    def lambda_0E90():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0E90)

    @scena.Lambda('lambda_0EA5')
    def lambda_0EA5():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0EA5)

    @scena.Lambda('lambda_0EBA')
    def lambda_0EBA():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0EBA)

    @scena.Lambda('lambda_0ECF')
    def lambda_0ECF():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0ECF)

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

    ChrSetChipByIndex(0x0008, 10)
    ChrSetChipByIndex(0x0009, 10)
    ChrSetChipByIndex(0x000A, 10)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0xF3E
@scena.Code('func_07_F3E')
def func_07_F3E():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F50',
    )

    Return()

    def _loc_F50(): pass

    label('loc_F50')

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

    @scena.Lambda('lambda_1032')
    def lambda_1032():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1032)

    @scena.Lambda('lambda_1047')
    def lambda_1047():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1047)

    @scena.Lambda('lambda_105C')
    def lambda_105C():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_105C)

    @scena.Lambda('lambda_1071')
    def lambda_1071():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1071)

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

    ChrSetChipByIndex(0x0008, 10)
    ChrSetChipByIndex(0x0009, 10)
    ChrSetChipByIndex(0x000A, 10)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x10E0
@scena.Code('func_08_10E0')
def func_08_10E0():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10F2',
    )

    Return()

    def _loc_10F2(): pass

    label('loc_10F2')

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

    @scena.Lambda('lambda_11D4')
    def lambda_11D4():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_11D4)

    @scena.Lambda('lambda_11E9')
    def lambda_11E9():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_11E9)

    @scena.Lambda('lambda_11FE')
    def lambda_11FE():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_11FE)

    @scena.Lambda('lambda_1213')
    def lambda_1213():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1213)

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

    ChrSetChipByIndex(0x0008, 10)
    ChrSetChipByIndex(0x0009, 10)
    ChrSetChipByIndex(0x000A, 10)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x1282
@scena.Code('func_09_1282')
def func_09_1282():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1294',
    )

    Return()

    def _loc_1294(): pass

    label('loc_1294')

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

    @scena.Lambda('lambda_1376')
    def lambda_1376():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1376)

    @scena.Lambda('lambda_138B')
    def lambda_138B():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_138B)

    @scena.Lambda('lambda_13A0')
    def lambda_13A0():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_13A0)

    @scena.Lambda('lambda_13B5')
    def lambda_13B5():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_13B5)

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

    ChrSetChipByIndex(0x0008, 10)
    ChrSetChipByIndex(0x0009, 10)
    ChrSetChipByIndex(0x000A, 10)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x1424
@scena.Code('func_0A_1424')
def func_0A_1424():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1436',
    )

    Return()

    def _loc_1436(): pass

    label('loc_1436')

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

    @scena.Lambda('lambda_1518')
    def lambda_1518():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1518)

    @scena.Lambda('lambda_152D')
    def lambda_152D():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_152D)

    @scena.Lambda('lambda_1542')
    def lambda_1542():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1542)

    @scena.Lambda('lambda_1557')
    def lambda_1557():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1557)

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

    ChrSetChipByIndex(0x0008, 10)
    ChrSetChipByIndex(0x0009, 10)
    ChrSetChipByIndex(0x000A, 10)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x15C6
@scena.Code('func_0B_15C6')
def func_0B_15C6():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15D8',
    )

    Return()

    def _loc_15D8(): pass

    label('loc_15D8')

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

    @scena.Lambda('lambda_16BA')
    def lambda_16BA():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_16BA)

    @scena.Lambda('lambda_16CF')
    def lambda_16CF():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_16CF)

    @scena.Lambda('lambda_16E4')
    def lambda_16E4():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_16E4)

    @scena.Lambda('lambda_16F9')
    def lambda_16F9():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_16F9)

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

    ChrSetChipByIndex(0x0008, 10)
    ChrSetChipByIndex(0x0009, 10)
    ChrSetChipByIndex(0x000A, 10)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x1768
@scena.Code('func_0C_1768')
def func_0C_1768():
    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_177A',
    )

    Return()

    def _loc_177A(): pass

    label('loc_177A')

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

    @scena.Lambda('lambda_185C')
    def lambda_185C():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_185C)

    @scena.Lambda('lambda_1871')
    def lambda_1871():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1871)

    @scena.Lambda('lambda_1886')
    def lambda_1886():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1886)

    @scena.Lambda('lambda_189B')
    def lambda_189B():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_189B)

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

    ChrSetChipByIndex(0x0008, 10)
    ChrSetChipByIndex(0x0009, 10)
    ChrSetChipByIndex(0x000A, 10)
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
