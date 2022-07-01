import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C2102_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2102   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, 'Targeting Camera'),
    TXT(0x02, '左の柱覆域判定用'),
    TXT(0x03, '右の柱覆域判定用'),
    TXT(0x04, '中央の台座判定'),
    TXT(0x05, ''),
    TXT(0x06, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'C2102.x'
    header.mapIndex       = 98
    header.bgm            = 33
    header.flags          = 0x0001
    header.entryFunction  = 0x000A
    header.importTable    = ['ED6_DT21/C2102._SN', 'ED6_DT21/C2102_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x274
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
        ('ED6_DT09/CH10160._CH', 'ED6_DT09/CH10160P._CP'),
        ('ED6_DT09/CH10161._CH', 'ED6_DT09/CH10161P._CP'),
        ('ED6_DT09/CH10450._CH', 'ED6_DT09/CH10450P._CP'),
        ('ED6_DT09/CH10451._CH', 'ED6_DT09/CH10451P._CP'),
        ('ED6_DT09/CH10220._CH', 'ED6_DT09/CH10220P._CP'),
        ('ED6_DT09/CH10221._CH', 'ED6_DT09/CH10221P._CP'),
        ('ED6_DT09/CH10470._CH', 'ED6_DT09/CH10470P._CP'),
        ('ED6_DT09/CH10471._CH', 'ED6_DT09/CH10471P._CP'),
        ('ED6_DT09/CH10480._CH', 'ED6_DT09/CH10480P._CP'),
        ('ED6_DT09/CH10481._CH', 'ED6_DT09/CH10481P._CP'),
        ('ED6_DT09/CH11060._CH', 'ED6_DT09/CH11060P._CP'),
        ('ED6_DT09/CH11061._CH', 'ED6_DT09/CH11061P._CP'),
        ('ED6_DT09/CH10460._CH', 'ED6_DT09/CH10460P._CP'),
        ('ED6_DT09/CH10461._CH', 'ED6_DT09/CH10461P._CP'),
        ('ED6_DT27/CH03520._CH', 'ED6_DT27/CH03520P._CP'),
        ('ED6_DT26/CH20279._CH', 'ED6_DT26/CH20279P._CP'),
        ('ED6_DT06/CH20064._CH', 'ED6_DT06/CH20064P._CP'),
        ('ED6_DT27/CH03523._CH', 'ED6_DT27/CH03523P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT29/CH12140._CH', 'ED6_DT29/CH12140P._CP'),
        ('ED6_DT29/CH12141._CH', 'ED6_DT29/CH12141P._CP'),
    ]

# id: 0x10002 offset: 0x152
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
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -3200,
            z                   = 250,
            y                   = 8710,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 3200,
            z                   = 250,
            y                   = 8710,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 950,
            y                   = 13850,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
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
        ScenaMonsterData(
            x           = -9050,
            z           = 250,
            y           = 12430,
            word_0C     = 0x00B4,
            word_0E     = 0x0013,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01BD,
            word_18     = 0x2103,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1EE
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1EE
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1EE
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0420, 3, 0x2103)),
            Expr.Return,
        ),
        'loc_1FA',
    )

    SetChrFlags(0x000C, 0x0080)

    def _loc_1FA(): pass

    label('loc_1FA')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24C',
    )

    OP_B5(0x00)

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0066, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x1000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_22F',
    )

    SetMapFlags(0x10000000)
    Event(1, 0x0001)

    Jump('loc_24C')

    def _loc_22F(): pass

    label('loc_22F')

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x2000)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0066, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_24C',
    )

    SetMapFlags(0x10000000)
    Event(1, 0x0000)

    def _loc_24C(): pass

    label('loc_24C')

    Return()

# id: 0x0001 offset: 0x24D
@scena.Code('Init')
def Init():
    ExecExpressionWithValue(
        0x000C,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_26A',
    )

    OP_82(0x80, 0x00)
    OP_82(0x81, 0x00)

    def _loc_26A(): pass

    label('loc_26A')

    OP_22(0x01C3, 0x01, 0x64)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
