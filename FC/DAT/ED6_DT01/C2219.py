import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C2219_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2219   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '弗科特老人'),
    TXT(0x02, '照相机'),
    TXT(0x03, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'C2219.x'
    header.mapIndex       = 84
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/C2219._SN', 'ED6_DT01/C2219_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2DB
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
            word_3A         = 84,
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
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT09/CH11200._CH', 'ED6_DT09/CH11200P._CP'),
        ('ED6_DT09/CH11201._CH', 'ED6_DT09/CH11201P._CP'),
    ]

# id: 0x10002 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -2140,
            z                   = 0,
            y                   = 201500,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0000,
        ),
        ScenaNpcData(
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

# id: 0x10003 offset: 0x102
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -250,
            z           = 0,
            y           = -890,
            word_0C     = 0x00B4,
            word_0E     = 0x0001,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F2,
            word_18     = 0x04A0,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 99940,
            z           = 0,
            y           = 20,
            word_0C     = 0x010E,
            word_0E     = 0x0001,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F2,
            word_18     = 0x04A1,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 1790,
            z           = 0,
            y           = 102020,
            word_0C     = 0x005A,
            word_0E     = 0x0001,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F2,
            word_18     = 0x04A3,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -1430,
            z           = 0,
            y           = 95940,
            word_0C     = 0x0000,
            word_0E     = 0x0001,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F2,
            word_18     = 0x04A4,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x172
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x172
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x172
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x40)"),
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x10)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_19A',
    )

    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)

    Jump('loc_1CF')

    def _loc_19A(): pass

    label('loc_19A')

    SetChrFlags(0x0008, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0094, 0, 0x4A0)),
            Expr.Return,
        ),
        'loc_1AB',
    )

    SetChrFlags(0x000A, 0x0080)

    def _loc_1AB(): pass

    label('loc_1AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0094, 1, 0x4A1)),
            Expr.Return,
        ),
        'loc_1B7',
    )

    SetChrFlags(0x000B, 0x0080)

    def _loc_1B7(): pass

    label('loc_1B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0094, 3, 0x4A3)),
            Expr.Return,
        ),
        'loc_1C3',
    )

    SetChrFlags(0x000C, 0x0080)

    def _loc_1C3(): pass

    label('loc_1C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0094, 4, 0x4A4)),
            Expr.Return,
        ),
        'loc_1CF',
    )

    SetChrFlags(0x000D, 0x0080)

    def _loc_1CF(): pass

    label('loc_1CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_1DD',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(1, 0x0001)

    def _loc_1DD(): pass

    label('loc_1DD')

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1F8',
    )

    SetChrPos(0x0008, 3340, 1000, 193310, 178)

    def _loc_1F8(): pass

    label('loc_1F8')

    Return()

# id: 0x0001 offset: 0x1F9
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x40)"),
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x10)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_20D',
    )

    Jump('loc_216')

    def _loc_20D(): pass

    label('loc_20D')

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1F),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_216(): pass

    label('loc_216')

    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0006, 0x0004)
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_71(0x000A, 0x0004)
    OP_71(0x000B, 0x0004)
    OP_71(0x000C, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)
    OP_71(0x000F, 0x0004)
    OP_B0(0x0000, 0x78)
    OP_1C(0x00, 0x00, 0x0003)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0094, 0, 0x4A0)),
            Expr.Return,
        ),
        'loc_2B5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0094, 1, 0x4A1)),
            Expr.Return,
        ),
        'loc_2B5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0094, 3, 0x4A3)),
            Expr.Return,
        ),
        'loc_2B5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0094, 4, 0x4A4)),
            Expr.Return,
        ),
        'loc_2B5',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x001C, 0x01, 0x0008)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x001D, 0x01, 0x0010)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B5',
    )

    OP_28(0x001C, 0x01, 0x0008)

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_2B1',
    )

    OP_28(0x001D, 0x01, 0x0010)

    def _loc_2B1(): pass

    label('loc_2B1')

    Event(1, 0x0005)

    def _loc_2B5(): pass

    label('loc_2B5')

    Return()

# id: 0x0002 offset: 0x2B6
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2CB',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_2CB(): pass

    label('loc_2CB')

    Return()

# id: 0x0003 offset: 0x2CC
@scena.Code('func_03_2CC')
def func_03_2CC():
    TalkBegin(0x00FF)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
