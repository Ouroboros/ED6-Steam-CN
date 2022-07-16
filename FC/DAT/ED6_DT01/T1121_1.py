import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1121_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1121_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T1121.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1CA
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10001 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('PreInit')
def PreInit():
    Sleep(400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_A9',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x000D, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_93',
    )

    OP_2A(0x000E, 0x0010, 0x0011, 0x0012, 0x0013, 0x0015, 0x0016, 0x0017, 0x0018, 0xFFFF)

    Jump('loc_A6')

    def _loc_93(): pass

    label('loc_93')

    OP_2A(0x000E, 0x0010, 0x0012, 0x0013, 0x0015, 0x0016, 0x0017, 0x0018, 0xFFFF)

    def _loc_A6(): pass

    label('loc_A6')

    Jump('loc_1BF')

    def _loc_A9(): pass

    label('loc_A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_E9',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x000D, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_D3',
    )

    OP_2A(0x000E, 0x0010, 0x0011, 0x0012, 0x0013, 0x0015, 0x0016, 0x0017, 0x0018, 0xFFFF)

    Jump('loc_E6')

    def _loc_D3(): pass

    label('loc_D3')

    OP_2A(0x000E, 0x0010, 0x0012, 0x0013, 0x0015, 0x0016, 0x0017, 0x0018, 0xFFFF)

    def _loc_E6(): pass

    label('loc_E6')

    Jump('loc_1BF')

    def _loc_E9(): pass

    label('loc_E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_125',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x000D, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_111',
    )

    OP_2A(0x000E, 0x0010, 0x0011, 0x0012, 0x0015, 0x0016, 0x0017, 0x0018, 0xFFFF)

    Jump('loc_122')

    def _loc_111(): pass

    label('loc_111')

    OP_2A(0x000E, 0x0010, 0x0012, 0x0015, 0x0016, 0x0017, 0x0018, 0xFFFF)

    def _loc_122(): pass

    label('loc_122')

    Jump('loc_1BF')

    def _loc_125(): pass

    label('loc_125')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_159',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x000D, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_149',
    )

    OP_2A(0x000E, 0x0011, 0x0012, 0x0015, 0x0016, 0x0017, 0xFFFF)

    Jump('loc_156')

    def _loc_149(): pass

    label('loc_149')

    OP_2A(0x000E, 0x0012, 0x0015, 0x0016, 0x0017, 0xFFFF)

    def _loc_156(): pass

    label('loc_156')

    Jump('loc_1BF')

    def _loc_159(): pass

    label('loc_159')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 5, 0x30D)),
            Expr.Return,
        ),
        'loc_16E',
    )

    OP_2A(0x000E, 0x0012, 0x0015, 0x0016, 0xFFFF)

    Jump('loc_1BF')

    def _loc_16E(): pass

    label('loc_16E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_181',
    )

    OP_2A(0x000E, 0x0012, 0x0015, 0xFFFF)

    Jump('loc_1BF')

    def _loc_181(): pass

    label('loc_181')

    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '现在没有什么特别的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_1BF(): pass

    label('loc_1BF')

    TalkEnd(0x00FF)
    Sleep(400)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
