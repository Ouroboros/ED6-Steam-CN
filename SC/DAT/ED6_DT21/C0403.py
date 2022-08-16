import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0403_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0403   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 16
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/C0403_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH02390._CH', 'ED6_DT07/CH02390P._CP'),
        ('ED6_DT07/CH02550._CH', 'ED6_DT07/CH02550P._CP'),
        ('ED6_DT06/CH20100._CH', 'ED6_DT06/CH20100P._CP'),
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT27/CH03520._CH', 'ED6_DT27/CH03520P._CP'),
        ('ED6_DT27/CH03500._CH', 'ED6_DT27/CH03500P._CP'),
        ('ED6_DT27/CH03600._CH', 'ED6_DT27/CH03600P._CP'),
        ('ED6_DT27/CH03530._CH', 'ED6_DT27/CH03530P._CP'),
        ('ED6_DT26/CH20280._CH', 'ED6_DT26/CH20280P._CP'),
        ('ED6_DT27/CH03500._CH', 'ED6_DT27/CH03500P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT27/CH03870._CH', 'ED6_DT27/CH03870P._CP'),
        ('ED6_DT27/CH03871._CH', 'ED6_DT27/CH03871P._CP'),
        ('ED6_DT27/CH03005._CH', 'ED6_DT27/CH03005P._CP'),
        ('ED6_DT29/CH12140._CH', 'ED6_DT29/CH12140P._CP'),
        ('ED6_DT29/CH12141._CH', 'ED6_DT29/CH12141P._CP'),
    ]

# id: 0x10001 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = 'Crow',
            x                   = -5140,
            z                   = 250,
            y                   = 1000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x14A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -9470,
            z           = 250,
            y           = 3200,
            word_0C     = 0x0000,
            word_0E     = 0x000E,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0031,
            word_18     = 0x2101,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x166
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x166
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -5140,
            triggerZ            = 250,
            triggerY            = 1000,
            triggerRange        = 1000,
            actorX              = -5140,
            actorZ              = 250,
            actorY              = 1000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x18A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0420, 1, 0x2101)),
            Expr.Return,
        ),
        'loc_196',
    )

    ChrSetFlags(0x0009, 0x0080)

    def _loc_196(): pass

    label('loc_196')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BC',
    )

    OP_B5(0x00)

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B8',
    )

    ChrClearFlags(0x0008, 0x0080)

    Jump('loc_1BC')

    def _loc_1B8(): pass

    label('loc_1B8')

    TerminateThread(0x0008, 0x00)

    def _loc_1BC(): pass

    label('loc_1BC')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1CC',
    )

    TerminateThread(0x0008, 0x00)

    def _loc_1CC(): pass

    label('loc_1CC')

    Return()

# id: 0x0001 offset: 0x1CD
@scena.Code('func_01_1CD')
def func_01_1CD():
    ExecExpressionWithValue(
        0x0009,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_247',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_247',
    )

    OP_65(0x00, 0x0001)
    OP_26(347)
    OP_26(140)
    LoadEffect(0x00, 'map\\\\mp022_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -5140, 450, 1000, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)

    def _loc_247(): pass

    label('loc_247')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_259',
    )

    StopEffect(0x81, 0x00)
    StopEffect(0x82, 0x00)

    def _loc_259(): pass

    label('loc_259')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_263',
    )

    StopEffect(0x80, 0x00)

    def _loc_263(): pass

    label('loc_263')

    PlaySE(451, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x269
@scena.Code('func_02_269')
def func_02_269():
    ExecExpressionWithValue(
        0x00FE,
        0x28,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x00FE, 0x0040)
    OP_8D(0x00FE, -5140, -470, -7400, 2650, 0)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            Expr.Rand,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_29D(): pass

    label('loc_29D')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_492',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x960),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x960),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x960),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x960),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_45B',
    )

    TerminateThread(0x00FE, 0x01)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_324',
    )

    @scena.Lambda('lambda_0308')
    def lambda_0308():
        OP_97(0x00FE, -4000, 1000, 360000, 7000, 0x0001)
        Yield()

        Jump('lambda_0308')

    DispatchAsync2(0x00FE, 0x0001, lambda_0308)

    Jump('loc_343')

    def _loc_324(): pass

    label('loc_324')

    @scena.Lambda('lambda_032A')
    def lambda_032A():
        OP_97(0x00FE, -4000, 1000, -360000, 7000, 0x0001)
        Yield()

        Jump('lambda_032A')

    DispatchAsync2(0x00FE, 0x0001, lambda_032A)

    def _loc_343(): pass

    label('loc_343')

    ChrSetChipByIndex(0x00FE, 11)
    ChrClearFlags(0x00FE, 0x0400)
    ChrSetFlags(0x00FE, 0x0004)
    PlaySE(347, 0x00, 0x64)
    PlaySE(140, 0x00, 0x64)
    def _loc_35C(): pass

    label('loc_35C')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_394',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x02,
        (
            (Expr.PushLong, 0xC8),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x2),
            (Expr.PushLong, 0x2328),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_38C',
    )

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 2000)

    Jump('loc_394')

    def _loc_38C(): pass

    label('loc_38C')

    Sleep(15)

    Jump('loc_35C')

    def _loc_394(): pass

    label('loc_394')

    TerminateThread(0x00FE, 0x01)
    ChrSetFlags(0x00FE, 0x0080)
    ChrClearFlags(0x00FE, 0x0004)
    ChrSetPos(0x00FE, -5140, 251, 1000, 270)
    def _loc_3B3(): pass

    label('loc_3B3')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_458',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x3A98),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x3A98),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            Expr.Or,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x3A98),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Or,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x3A98),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Or,
            Expr.Return,
        ),
        'loc_450',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_450',
    )

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 12)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 0)
    ChrClearFlags(0x00FE, 0x0004)
    ChrSetPos(0x00FE, -5140, 250, 1000, 270)
    OP_8D(0x00FE, -5140, -470, -7400, 2650, 0)

    Jump('loc_458')

    def _loc_450(): pass

    label('loc_450')

    Sleep(500)

    Jump('loc_3B3')

    def _loc_458(): pass

    label('loc_458')

    Jump('loc_48F')

    def _loc_45B(): pass

    label('loc_45B')

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
        'loc_48F',
    )

    @scena.Lambda('lambda_0477')
    def lambda_0477():
        OP_8D(0x00FE, -5140, -470, -7400, 2650, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0477)

    def _loc_48F(): pass

    label('loc_48F')

    Jump('loc_29D')

    def _loc_492(): pass

    label('loc_492')

    Return()

# id: 0x0003 offset: 0x493
@scena.Code('func_03_493')
def func_03_493():
    Call(1, 0x0000)
    OP_64(0x00, 0x0001)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
