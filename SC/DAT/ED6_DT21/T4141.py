import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4141_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4141   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '莉莉'),
    TXT(0x02, '丹顿'),
    TXT(0x03, '蜜蒂'),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4141.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x28D
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
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01770._CH', 'ED6_DT07/CH01770P._CP'),
    ]

# id: 0x10002 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 8790,
            z                   = 0,
            y                   = 10500,
            direction           = 196,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 12170,
            z                   = 0,
            y                   = -4050,
            direction           = 163,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -4540,
            z                   = 0,
            y                   = 9850,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
    )

# id: 0x10003 offset: 0x132
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x132
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x132
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 8450,
            triggerZ            = 0,
            triggerY            = 8650,
            triggerRange        = 800,
            actorX              = 8790,
            actorZ              = 1500,
            actorY              = 10500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 11970,
            triggerZ            = 0,
            triggerY            = -5950,
            triggerRange        = 800,
            actorX              = 12170,
            actorZ              = 1500,
            actorY              = -4050,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -6400,
            triggerZ            = 0,
            triggerY            = 9620,
            triggerRange        = 800,
            actorX              = -4540,
            actorZ              = 1500,
            actorY              = 9850,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x19E
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x19F
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x1A0
@scena.Code('ReInit')
def ReInit():
    Call(0, 0x0003)

    Return()

# id: 0x0003 offset: 0x1A5
@scena.Code('func_03_1A5')
def func_03_1A5():
    TalkBegin(0x0008)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1DC',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CA',
    )

    OP_A9(0xD8)

    Jump('loc_1D8')

    def _loc_1CA(): pass

    label('loc_1CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1D6',
    )

    OP_A9(0xD7)

    Jump('loc_1D8')

    def _loc_1D6(): pass

    label('loc_1D6')

    OP_A9(0xD2)

    def _loc_1D8(): pass

    label('loc_1D8')

    TalkEnd(0x0008)

    Return()

    def _loc_1DC(): pass

    label('loc_1DC')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1ED',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_1ED(): pass

    label('loc_1ED')

    ChrTalk(
        0x0008,
        (
            '◆你好',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x1FD
@scena.Code('func_04_1FD')
def func_04_1FD():
    Call(0, 0x0005)

    Return()

# id: 0x0005 offset: 0x202
@scena.Code('func_05_202')
def func_05_202():
    TalkBegin(0x0009)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_21C',
    )

    OP_A9(0xD3)
    TalkEnd(0x0009)

    Return()

    def _loc_21C(): pass

    label('loc_21C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22D',
    )

    TalkEnd(0x0009)

    Return()

    def _loc_22D(): pass

    label('loc_22D')

    ChrTalk(
        0x0009,
        (
            '◆你好',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0x23D
@scena.Code('func_06_23D')
def func_06_23D():
    Call(0, 0x0007)

    Return()

# id: 0x0007 offset: 0x242
@scena.Code('func_07_242')
def func_07_242():
    TalkBegin(0x000A)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25C',
    )

    OP_A9(0xD4)
    TalkEnd(0x000A)

    Return()

    def _loc_25C(): pass

    label('loc_25C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26D',
    )

    TalkEnd(0x000A)

    Return()

    def _loc_26D(): pass

    label('loc_26D')

    ChrTalk(
        0x000A,
        (
            '◆你好',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
