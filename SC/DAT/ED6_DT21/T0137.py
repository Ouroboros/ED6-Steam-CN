import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0137_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0137   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0137.x'
    header.mapIndex       = 10
    header.bgm            = 84
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
        ('ED6_DT07/CH01730._CH', 'ED6_DT07/CH01730P._CP'),
        ('ED6_DT07/CH01731._CH', 'ED6_DT07/CH01731P._CP'),
    ]

# id: 0x10001 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '鸽子',
            x                   = 54080,
            z                   = 11330,
            y                   = 43400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '鸽子',
            x                   = 54640,
            z                   = 11330,
            y                   = 43420,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '鸽子',
            x                   = 55240,
            z                   = 11330,
            y                   = 43310,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '鸽子',
            x                   = 55740,
            z                   = 10630,
            y                   = 43210,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '鸽子',
            x                   = 55640,
            z                   = 11330,
            y                   = 43400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
    )

# id: 0x10002 offset: 0x15A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x15A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x15A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -300,
            triggerZ            = 0,
            triggerY            = 4140,
            triggerRange        = 800,
            actorX              = -300,
            actorZ              = 1000,
            actorY              = 4140,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 53450,
            triggerZ            = 10300,
            triggerY            = 47970,
            triggerRange        = 800,
            actorX              = 53450,
            actorZ              = 10000,
            actorY              = 47970,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1A2
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x1A3
@scena.Code('func_01_1A3')
def func_01_1A3():
    StopEffect(0x86, 0x02)
    StopEffect(0x87, 0x02)
    StopEffect(0x88, 0x02)

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x67),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1E1',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1DE',
    )

    MapSetFlags(0x00000010)
    OP_11(0x4B, 0x4B, 0x96, 0, 60000, 0)
    OP_E8(0xD0, 0x07, 0x00, 0x00)

    def _loc_1DE(): pass

    label('loc_1DE')

    Jump('loc_1EB')

    def _loc_1E1(): pass

    label('loc_1E1')

    MapClearFlags(0x00000010)
    OP_E8(0xE8, 0x03, 0x00, 0x00)
    def _loc_1EB(): pass

    label('loc_1EB')

    Return()

# id: 0x0002 offset: 0x1EC
@scena.Code('func_02_1EC')
def func_02_1EC():
    ExecExpressionWithValue(
        0x00FE,
        0x28,
        (
            (Expr.PushLong, 0x8),
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x07,
        (
            (Expr.PushLong, 0x190),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x00FE, 0x0040)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_22E',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            Expr.Rand,
            (Expr.PushLong, 0x5A),
            Expr.Mod,
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_23B')

    def _loc_22E(): pass

    label('loc_22E')

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            Expr.Rand,
            (Expr.PushLong, 0x5A),
            Expr.Mod,
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_23B(): pass

    label('loc_23B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3D4',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x708),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x708),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x708),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x708),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_391',
    )

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_30B',
    )

    Sleep(250)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_30B',
    )

    Sleep(500)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_30B',
    )

    Sleep(500)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_30B',
    )

    Sleep(500)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_30B',
    )

    Sleep(500)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_30B',
    )

    Sleep(500)

    def _loc_30B(): pass

    label('loc_30B')

    TerminateThread(0x00FE, 0x01)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    @scena.Lambda('lambda_031C')
    def lambda_031C():
        OP_94(0x00, 0x00FE, 0x00B4, 0x00007530, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_031C)

    ExecExpressionWithValue(
        0x00FE,
        0x28,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x00FE, 0x02, 0x00, func_03_3D5)
    ChrSetChipByIndex(0x00FE, 0)
    ChrClearFlags(0x00FE, 0x0400)
    ChrSetFlags(0x00FE, 0x0004)

    ExecExpressionWithValue(
        0x00FE,
        0x02,
        (
            (Expr.PushLong, 0xC8),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_358(): pass

    label('loc_358')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_385',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x02,
        (
            (Expr.PushLong, 0x1F4),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x2),
            (Expr.PushLong, 0x2328),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_37D',
    )

    Jump('loc_385')

    def _loc_37D(): pass

    label('loc_37D')

    Sleep(15)

    Jump('loc_358')

    def _loc_385(): pass

    label('loc_385')

    TerminateThread(0x00FE, 0x01)
    ChrSetFlags(0x00FE, 0x0080)

    Jump('loc_3D1')

    def _loc_391(): pass

    label('loc_391')

    Sleep(100)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x14),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B5',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x2D),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_3D1')

    def _loc_3B5(): pass

    label('loc_3B5')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x14),
            Expr.Mod,
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D1',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x2D),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_3D1(): pass

    label('loc_3D1')

    Jump('loc_23B')

    def _loc_3D4(): pass

    label('loc_3D4')

    Return()

# id: 0x0003 offset: 0x3D5
@scena.Code('func_03_3D5')
def func_03_3D5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3EA',
    )

    OP_99(0x00FE, 0x00, 0x07, 6000)

    Jump('func_03_3D5')

    def _loc_3EA(): pass

    label('loc_3EA')

    Return()

# id: 0x0004 offset: 0x3EB
@scena.Code('func_04_3EB')
def func_04_3EB():
    OP_4A(0x00FE, 255)
    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '*chirp chirp chirp chirp chirp...*',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)
    OP_4B(0x00FE, 255)

    Return()

# id: 0x0005 offset: 0x440
@scena.Code('func_05_440')
def func_05_440():
    OP_4A(0x00FE, 255)
    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '*chirr...*',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)
    OP_4B(0x00FE, 255)

    Return()

# id: 0x0006 offset: 0x47D
@scena.Code('func_06_47D')
def func_06_47D():
    OP_4A(0x00FE, 255)
    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x0000012C, 1600, 0x36, 0x39, 0x000000FA, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    UnlockAchievement(0x00, 0x0001, 0x00)

    ChrTalk(
        0x00FE,
        (
            '*chirp chirp!*',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)
    OP_4B(0x00FE, 255)

    Return()

# id: 0x0007 offset: 0x4C3
@scena.Code('func_07_4C3')
def func_07_4C3():
    OP_4A(0x00FE, 255)
    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '*CHIRP!!*',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)
    OP_4B(0x00FE, 255)

    Return()

# id: 0x0008 offset: 0x504
@scena.Code('func_08_504')
def func_08_504():
    OP_4A(0x00FE, 255)
    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '*chirp chirp chirrrr*',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)
    OP_4B(0x00FE, 255)

    Return()

# id: 0x0009 offset: 0x551
@scena.Code('func_09_551')
def func_09_551():
    NewScene('ED6_DT21/T0137._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x55B
@scena.Code('func_0A_55B')
def func_0A_55B():
    NewScene('ED6_DT21/T0137._SN', 102, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
