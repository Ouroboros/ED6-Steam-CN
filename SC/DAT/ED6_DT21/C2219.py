import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C2219_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2219   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '弗科特老人'),
    TXT(0x02, '扎古'),
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
    header.importTable    = ['ED6_DT21/C2219._SN', 'ED6_DT21/C2219_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x669
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
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
    ]

# id: 0x10002 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -2870,
            z                   = 0,
            y                   = 202000,
            direction           = 270,
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
            x                   = 1430,
            z                   = 0,
            y                   = 200430,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10003 offset: 0xFA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xFA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xFA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -6600,
            triggerZ            = 0,
            triggerY            = 204290,
            triggerRange        = 800,
            actorX              = -6600,
            actorZ              = 1200,
            actorY              = 204290,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0001,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 2000,
            triggerZ            = 1000,
            triggerY            = 192960,
            triggerRange        = 600,
            actorX              = 2000,
            actorZ              = 1800,
            actorY              = 192960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3030,
            triggerZ            = 1000,
            triggerY            = 192700,
            triggerRange        = 600,
            actorX              = 3230,
            actorZ              = 1600,
            actorY              = 192420,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 5240,
            triggerZ            = 1000,
            triggerY            = 194630,
            triggerRange        = 600,
            actorX              = 5350,
            actorZ              = 1600,
            actorY              = 194210,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 7110,
            triggerZ            = 1000,
            triggerY            = 196770,
            triggerRange        = 800,
            actorX              = 7110,
            actorZ              = 2500,
            actorY              = 196770,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1AE
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1CB',
    )

    SetChrPos(0x0008, 3410, 1000, 193340, 183)
    ClearChrFlags(0x0009, 0x0080)

    def _loc_1CB(): pass

    label('loc_1CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_1DE',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(1, 0x0007)

    def _loc_1DE(): pass

    label('loc_1DE')

    Return()

# id: 0x0001 offset: 0x1DF
@scena.Code('Init')
def Init():
    OP_B0(0x0000, 0x78)
    OP_1C(0x00, 0x00, 0x0004)

    If(
        (
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x08)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x40)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x10)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_218',
    )

    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)

    Jump('loc_23B')

    def _loc_218(): pass

    label('loc_218')

    If(
        (
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x006B, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_23B',
    )

    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)

    def _loc_23B(): pass

    label('loc_23B')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C4',
    )

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
    OP_72(0x000F, 0x0004)

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6C),
            Expr.Equ,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6D),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2AE',
    )

    OP_78(0xC8, 0xC8, 0xC8)

    Jump('loc_2B2')

    def _loc_2AE(): pass

    label('loc_2AE')

    OP_78(0x96, 0x96, 0x96)

    def _loc_2B2(): pass

    label('loc_2B2')

    OP_79(0xFF, 0x0002)
    OP_7A(0x1C, 0x0002)
    OP_7B()
    OP_77(0xFF, 0xFF, 0xFF, 0x01, 0x00000000)

    def _loc_2C4(): pass

    label('loc_2C4')

    Return()

# id: 0x0002 offset: 0x2C5
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EA',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_42C')

    def _loc_2EA(): pass

    label('loc_2EA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_303',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_42C')

    def _loc_303(): pass

    label('loc_303')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31C',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_42C')

    def _loc_31C(): pass

    label('loc_31C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_335',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_42C')

    def _loc_335(): pass

    label('loc_335')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34E',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_42C')

    def _loc_34E(): pass

    label('loc_34E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_367',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_42C')

    def _loc_367(): pass

    label('loc_367')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_380',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_42C')

    def _loc_380(): pass

    label('loc_380')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_399',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_42C')

    def _loc_399(): pass

    label('loc_399')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B2',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_42C')

    def _loc_3B2(): pass

    label('loc_3B2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3CB',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_42C')

    def _loc_3CB(): pass

    label('loc_3CB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E4',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_42C')

    def _loc_3E4(): pass

    label('loc_3E4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3FD',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_42C')

    def _loc_3FD(): pass

    label('loc_3FD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_416',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_42C')

    def _loc_416(): pass

    label('loc_416')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42C',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_42C(): pass

    label('loc_42C')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_441',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_42C')

    def _loc_441(): pass

    label('loc_441')

    Return()

# id: 0x0003 offset: 0x442
@scena.Code('func_03_442')
def func_03_442():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_55A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_512',
    )

    ChrTalk(
        0x00FE,
        (
            '爷爷似乎总算是能够\n',
            '明白目前的状况了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实我很希望他去村里避难的，\n',
            '不过，看来这是不可能办到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，没办法\n',
            '我就留在这里陪他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟不能把爷爷一个人\n',
            '丢在这里不管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_557')

    def _loc_512(): pass

    label('loc_512')

    ChrTalk(
        0x00FE,
        (
            '爷爷似乎总算是能够\n',
            '明白目前的状况了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是个倔强无比的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_557(): pass

    label('loc_557')

    Jump('loc_654')

    def _loc_55A(): pass

    label('loc_55A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_654',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5FC',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，真伤脑筋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '关于导力器无法运行的事情\n',
            '都已经说过好几次了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爷爷他完全\n',
            '都听不进去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话，只好暂时\n',
            '不管他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_654')

    def _loc_5FC(): pass

    label('loc_5FC')

    ChrTalk(
        0x00FE,
        (
            '爷爷他根本就不相信\n',
            '导力器无法运行的事实啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，这样的话，\n',
            '只好暂时不管他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_654(): pass

    label('loc_654')

    TalkEnd(0x0009)

    Return()

# id: 0x0004 offset: 0x658
@scena.Code('func_04_658')
def func_04_658():
    TalkBegin(0x00FF)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
