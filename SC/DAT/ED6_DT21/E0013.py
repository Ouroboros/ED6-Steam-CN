import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0013_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0013   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'event'
    header.mapModel       = 'E0013.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/E0013_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
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
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT27/CH03880._CH', 'ED6_DT27/CH03880P._CP'),
        ('ED6_DT27/CH03005._CH', 'ED6_DT27/CH03005P._CP'),
        ('ED6_DT27/CH03881._CH', 'ED6_DT27/CH03881P._CP'),
        ('ED6_DT27/CH03882._CH', 'ED6_DT27/CH03882P._CP'),
    ]

# id: 0x10001 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = 'Aryll',
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
            name                = 'Kitten',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = 'Kitten',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = 'Kitten',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x152
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x152
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 31660,
            y           = -1000,
            z           = 7810,
            range       = 28340,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00002206,
            dword_18    = 0x00010000,
            dword_1C    = 0x00000009,
        ),
    )

# id: 0x10004 offset: 0x172
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x172
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6E),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_191',
    )

    OP_89(0x0000, 84860, 130, 5970, 0)
    OP_30(0x01)

    def _loc_191(): pass

    label('loc_191')

    ExecExpressionWithValue(
        0x0009,
        0x2D,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x2E,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x2F,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x07,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x29,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x2D,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x2E,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x2F,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x07,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x29,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x2D,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x2E,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x2F,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x07,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x29,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_246',
    )

    Event(1, 0x0000)

    def _loc_246(): pass

    label('loc_246')

    Return()

# id: 0x0001 offset: 0x247
@scena.Code('func_01_247')
def func_01_247():
    Return()

# id: 0x0002 offset: 0x248
@scena.Code('func_02_248')
def func_02_248():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_25D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_248')

    def _loc_25D(): pass

    label('loc_25D')

    Return()

# id: 0x0003 offset: 0x25E
@scena.Code('func_03_25E')
def func_03_25E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_281',
    )

    OP_8D(0x00FE, 29250, 9730, 30560, 8740, 1000)

    Jump('func_03_25E')

    def _loc_281(): pass

    label('loc_281')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
