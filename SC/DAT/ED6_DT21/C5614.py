import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5614_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5614   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5614.x'
    header.mapIndex       = 1
    header.bgm            = 61
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
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
    Event(0, func_02_AE)

    Return()

# id: 0x0001 offset: 0xAD
@scena.Code('func_01_AD')
def func_01_AD():
    Return()

# id: 0x0002 offset: 0xAE
@scena.Code('func_02_AE')
def func_02_AE():
    EventBegin(0x00)
    CameraMove(1120, 0, 4019, 0)
    OP_67(0, 8620, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 650, 0, 2620, 90)
    ChrSetPos(0x0001, 650, 0, 3800, 90)
    ChrSetPos(0x0002, -930, 0, 2620, 90)
    ChrSetPos(0x0003, -930, 0, 3800, 90)
    FadeIn(1000, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0393, 2, 0x1C9A)),
            Expr.Return,
        ),
        'loc_152',
    )

    Call(0, 0x0003)
    NewScene('ED6_DT21/C5611._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1C2')

    def _loc_152(): pass

    label('loc_152')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0393, 3, 0x1C9B)),
            Expr.Return,
        ),
        'loc_169',
    )

    Call(0, 0x0004)
    NewScene('ED6_DT21/C5610._SN', 132, 0, 0)
    IdleLoop()

    Jump('loc_1C2')

    def _loc_169(): pass

    label('loc_169')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0393, 4, 0x1C9C)),
            Expr.Return,
        ),
        'loc_180',
    )

    Call(0, 0x0003)
    NewScene('ED6_DT21/C5612._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1C2')

    def _loc_180(): pass

    label('loc_180')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0393, 5, 0x1C9D)),
            Expr.Return,
        ),
        'loc_197',
    )

    Call(0, 0x0004)
    NewScene('ED6_DT21/C5611._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_1C2')

    def _loc_197(): pass

    label('loc_197')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0393, 6, 0x1C9E)),
            Expr.Return,
        ),
        'loc_1AE',
    )

    Call(0, 0x0003)
    NewScene('ED6_DT21/C5613._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1C2')

    def _loc_1AE(): pass

    label('loc_1AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0393, 7, 0x1C9F)),
            Expr.Return,
        ),
        'loc_1C2',
    )

    Call(0, 0x0004)
    NewScene('ED6_DT21/C5612._SN', 101, 0, 0)
    IdleLoop()

    def _loc_1C2(): pass

    label('loc_1C2')

    Return()

# id: 0x0003 offset: 0x1C3
@scena.Code('func_03_1C3')
def func_03_1C3():
    FadeOut(2000, 0, -1)
    PlaySE(103, 0x00, 0x64)
    CameraMove(1120, -12000, 4019, 2000)
    Sleep(2000)

    Return()

# id: 0x0004 offset: 0x1E9
@scena.Code('func_04_1E9')
def func_04_1E9():
    FadeOut(2000, 0, -1)
    PlaySE(103, 0x00, 0x64)
    CameraMove(1120, 12000, 4019, 2000)
    Sleep(2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
