import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import SUB000_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('SUB000  ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'a'
    header.mapModel       = 'a.x'
    header.mapIndex       = 0
    header.bgm            = 0
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
    Return()

# id: 0x0001 offset: 0xA9
@scena.Code('func_01_A9')
def func_01_A9():
    Return()

# id: 0x0002 offset: 0xAA
@scena.Code('func_02_AA')
def func_02_AA():
    ExecExpressionWithReg(
        0x0065,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x65),
            Expr.Return,
        ),
        (0x00000000, 'loc_DB'),
        (0x00000001, 'loc_E7'),
        (0x00000002, 'loc_F3'),
        (0x00000003, 'loc_FF'),
        (0x00000004, 'loc_10B'),
        (0x00000005, 'loc_117'),
        (0x00000006, 'loc_123'),
        (-1, 'loc_12F'),
    )

    def _loc_DB(): pass

    label('loc_DB')

    OP_99(0x00FE, 0x00, 0x07, 1450)

    Jump('loc_13B')

    def _loc_E7(): pass

    label('loc_E7')

    OP_99(0x00FE, 0x00, 0x07, 1550)

    Jump('loc_13B')

    def _loc_F3(): pass

    label('loc_F3')

    OP_99(0x00FE, 0x00, 0x07, 1600)

    Jump('loc_13B')

    def _loc_FF(): pass

    label('loc_FF')

    OP_99(0x00FE, 0x00, 0x07, 1400)

    Jump('loc_13B')

    def _loc_10B(): pass

    label('loc_10B')

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_13B')

    def _loc_117(): pass

    label('loc_117')

    OP_99(0x00FE, 0x00, 0x07, 1350)

    Jump('loc_13B')

    def _loc_123(): pass

    label('loc_123')

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_13B')

    def _loc_12F(): pass

    label('loc_12F')

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_13B')

    def _loc_13B(): pass

    label('loc_13B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_150',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_13B')

    def _loc_150(): pass

    label('loc_150')

    Return()

# id: 0x0003 offset: 0x151
@scena.Code('func_03_151')
def func_03_151():
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '改造·换钱\n'),
            TXT(0x02, '离开\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A8',
    )

    OP_0D()

    def _loc_1A8(): pass

    label('loc_1A8')

    Return()

# id: 0x0004 offset: 0x1A9
@scena.Code('func_04_1A9')
def func_04_1A9():
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1FC',
    )

    OP_0D()

    def _loc_1FC(): pass

    label('loc_1FC')

    Return()

# id: 0x0005 offset: 0x1FD
@scena.Code('func_05_1FD')
def func_05_1FD():
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '报告\n'),
            TXT(0x02, '离开\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    FadeIn(300, 0)

    Return()

# id: 0x0006 offset: 0x241
@scena.Code('func_06_241')
def func_06_241():
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '休息\n'),
            TXT(0x02, '离开\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_292',
    )

    OP_0D()

    def _loc_292(): pass

    label('loc_292')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
