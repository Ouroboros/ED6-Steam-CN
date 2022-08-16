import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C2111_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2111   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'C2111.x'
    header.mapIndex       = 1
    header.bgm            = 33
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
        ('ED6_DT09/CH10560._CH', 'ED6_DT09/CH10560P._CP'),
        ('ED6_DT09/CH10561._CH', 'ED6_DT09/CH10561P._CP'),
        ('ED6_DT09/CH10570._CH', 'ED6_DT09/CH10570P._CP'),
        ('ED6_DT09/CH10571._CH', 'ED6_DT09/CH10571P._CP'),
        ('ED6_DT09/CH10580._CH', 'ED6_DT09/CH10580P._CP'),
        ('ED6_DT09/CH10581._CH', 'ED6_DT09/CH10581P._CP'),
        ('ED6_DT09/CH10590._CH', 'ED6_DT09/CH10590P._CP'),
        ('ED6_DT09/CH10591._CH', 'ED6_DT09/CH10591P._CP'),
        ('ED6_DT29/CH12140._CH', 'ED6_DT29/CH12140P._CP'),
        ('ED6_DT29/CH12141._CH', 'ED6_DT29/CH12141P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xFA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 6160,
            z           = 0,
            y           = 200,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01BA,
            word_18     = 0x1350,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x116
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x116
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x116
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x117
@scena.Code('func_01_117')
def func_01_117():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x026A, 0, 0x1350)),
            Expr.Return,
        ),
        'loc_123',
    )

    ChrSetFlags(0x0008, 0x0080)

    def _loc_123(): pass

    label('loc_123')

    OP_25(0x01CB, 90, 0, -12240, 2000, 25000, 0x64, 0x00000000)
    OP_25(0x01CB, -150, 0, 12290, 2000, 25000, 0x64, 0x00000000)
    PlaySE(461, 0x01, 0x64)
    OP_E8(0xDC, 0x05, 0x00, 0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
