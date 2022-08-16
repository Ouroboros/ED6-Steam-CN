import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5206_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5206   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5206.x'
    header.mapIndex       = 1
    header.bgm            = 35
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
        ('ED6_DT29/CH12950._CH', 'ED6_DT29/CH12950P._CP'),
    ]

# id: 0x10001 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '地震制御用ダミーキャラ',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0xD2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xD2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xD2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xD2
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0xD3
@scena.Code('func_01_D3')
def func_01_D3():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 6, 0x223E)),
            Expr.Return,
        ),
        'loc_F9',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x42),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x0008, 0x03, 0x00, func_02_FA)
    PlaySE(133, 0x01, 0x46)
    MapSetFlags(0x02000000)
    MapSetFlags(0x00100000)

    def _loc_F9(): pass

    label('loc_F9')

    Return()

# id: 0x0002 offset: 0xFA
@scena.Code('func_02_FA')
def func_02_FA():
    OP_C4(0x00, 0x00000020)
    def _loc_100(): pass

    label('loc_100')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_122',
    )

    OP_7C(60, 60, 1000, 900)
    Sleep(1000)

    Jump('loc_100')

    def _loc_122(): pass

    label('loc_122')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
