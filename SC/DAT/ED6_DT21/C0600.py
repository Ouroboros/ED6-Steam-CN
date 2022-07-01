import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0600_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0600   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '霉菌雾'),
    TXT(0x02, '霉菌雾'),
    TXT(0x03, '霉菌雾'),
    TXT(0x04, '目标用照相机'),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0600.x'
    header.mapIndex       = 20
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/C0600_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x694
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
        ('ED6_DT29/CH12120._CH', 'ED6_DT29/CH12120P._CP'),
        ('ED6_DT29/CH12121._CH', 'ED6_DT29/CH12121P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT27/CH03005._CH', 'ED6_DT27/CH03005P._CP'),
    ]

# id: 0x10002 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 6000,
            y                   = -4059,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -1100,
            z                   = 6000,
            y                   = -3020,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 1100,
            z                   = 6000,
            y                   = -3020,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
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
    )

# id: 0x10003 offset: 0x17A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x17A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x17A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -32900,
            triggerZ            = 0,
            triggerY            = 84900,
            triggerRange        = 1700,
            actorX              = -32900,
            actorZ              = 2500,
            actorY              = 84900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -13900,
            triggerZ            = 0,
            triggerY            = 73100,
            triggerRange        = 1700,
            actorX              = -13900,
            actorZ              = 2500,
            actorY              = 73100,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 2320,
            triggerZ            = 0,
            triggerY            = -360,
            triggerRange        = 600,
            actorX              = 2320,
            actorZ              = 800,
            actorY              = -360,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0001,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1E6
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.Eval, "OP_29(0x0077, 0x01, 0x0080)"),
            (Expr.Eval, "OP_29(0x0077, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0077, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_206',
    )

    Event(1, 0x0000)

    def _loc_206(): pass

    label('loc_206')

    Return()

# id: 0x0001 offset: 0x207
@scena.Code('Init')
def Init():
    OP_72(0x0000, 0x0028)
    OP_72(0x0001, 0x0028)
    OP_72(0x0002, 0x0028)
    OP_72(0x0003, 0x0028)
    OP_72(0x0004, 0x0028)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_235',
    )

    OP_6F(0x0000, 120)
    OP_6F(0x0001, 60)

    def _loc_235(): pass

    label('loc_235')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_24A',
    )

    OP_6F(0x0000, 120)
    OP_6F(0x0001, 160)

    def _loc_24A(): pass

    label('loc_24A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_25F',
    )

    OP_6F(0x0003, 120)
    OP_6F(0x0004, 60)

    def _loc_25F(): pass

    label('loc_25F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_274',
    )

    OP_6F(0x0002, 120)
    OP_6F(0x0004, 160)

    def _loc_274(): pass

    label('loc_274')

    OP_64(0x02, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x0077, 0x01, 0x4000)"),
            (Expr.Eval, "OP_29(0x0077, 0x01, 0x0100)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0077, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_298',
    )

    OP_65(0x02, 0x0001)

    def _loc_298(): pass

    label('loc_298')

    OP_22(0x01CD, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x29E
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
        'loc_2C3',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_405')

    def _loc_2C3(): pass

    label('loc_2C3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2DC',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_405')

    def _loc_2DC(): pass

    label('loc_2DC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F5',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_405')

    def _loc_2F5(): pass

    label('loc_2F5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_30E',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_405')

    def _loc_30E(): pass

    label('loc_30E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_327',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_405')

    def _loc_327(): pass

    label('loc_327')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_340',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_405')

    def _loc_340(): pass

    label('loc_340')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_359',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_405')

    def _loc_359(): pass

    label('loc_359')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_372',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_405')

    def _loc_372(): pass

    label('loc_372')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_38B',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_405')

    def _loc_38B(): pass

    label('loc_38B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A4',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_405')

    def _loc_3A4(): pass

    label('loc_3A4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3BD',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_405')

    def _loc_3BD(): pass

    label('loc_3BD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D6',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_405')

    def _loc_3D6(): pass

    label('loc_3D6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3EF',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_405')

    def _loc_3EF(): pass

    label('loc_3EF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_405',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_405(): pass

    label('loc_405')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_41A',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_405')

    def _loc_41A(): pass

    label('loc_41A')

    Return()

# id: 0x0003 offset: 0x41B
@scena.Code('func_03_41B')
def func_03_41B():
    TalkBegin(0x00FF)
    ClearMapFlags(0x00000001)

    Talk(
        (
            '有扳手。是否扳动？',
            TxtCtl.Enter,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4DE',
    )

    Menu(
        0,
        260,
        200,
        0,
        (
            TXT(0x00, '拉到右边\n'),
            TXT(0x01, '拉到左边\n'),
            TXT(0x02, '不动\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_491',
    )

    OP_6F(0x0001, 0)
    OP_70(0x0001, 0x0000003C)
    OP_73(0x0001)
    OP_A2(0x0001)

    Jump('loc_4B2')

    def _loc_491(): pass

    label('loc_491')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4B2',
    )

    OP_6F(0x0001, 100)
    OP_70(0x0001, 0x000000A0)
    OP_73(0x0001)
    OP_A2(0x0000)

    def _loc_4B2(): pass

    label('loc_4B2')

    OP_6D(-32340, -60, 91590, 500)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 0x00000078)
    OP_73(0x0000)
    OP_69(0x0000, 0x00000258)

    Jump('loc_546')

    def _loc_4DE(): pass

    label('loc_4DE')

    Menu(
        0,
        260,
        200,
        0,
        (
            TXT(0x00, '回复原状\n'),
            TXT(0x01, '不动\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_546',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_521',
    )

    OP_6F(0x0001, 0)
    OP_73(0x0001)
    OP_A3(0x0001)

    Jump('loc_535')

    def _loc_521(): pass

    label('loc_521')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_535',
    )

    OP_6F(0x0001, 0)
    OP_73(0x0001)
    OP_A3(0x0000)

    def _loc_535(): pass

    label('loc_535')

    OP_6F(0x0000, 120)
    OP_70(0x0000, 0x00000000)
    OP_73(0x0000)

    def _loc_546(): pass

    label('loc_546')

    SetMapFlags(0x00000001)
    TalkEnd(0x00FF)

    Return()

# id: 0x0004 offset: 0x54F
@scena.Code('func_04_54F')
def func_04_54F():
    TalkBegin(0x00FF)

    Talk(
        (
            '有扳手。是否扳动？',
            TxtCtl.Enter,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_60D',
    )

    Menu(
        0,
        260,
        200,
        0,
        (
            TXT(0x00, '拉到右边\n'),
            TXT(0x01, '拉到左边\n'),
            TXT(0x02, '不动\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5D1',
    )

    OP_6F(0x0004, 0)
    OP_70(0x0004, 0x0000003C)
    OP_73(0x0004)
    OP_A2(0x0003)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 0x00000078)
    OP_73(0x0003)

    Jump('loc_603')

    def _loc_5D1(): pass

    label('loc_5D1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_603',
    )

    OP_6F(0x0004, 100)
    OP_70(0x0004, 0x000000A0)
    OP_73(0x0004)
    OP_A2(0x0002)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 0x00000078)
    OP_73(0x0002)

    def _loc_603(): pass

    label('loc_603')

    OP_69(0x0000, 0x00000258)

    Jump('loc_686')

    def _loc_60D(): pass

    label('loc_60D')

    Menu(
        0,
        260,
        200,
        0,
        (
            TXT(0x00, '回复原状\n'),
            TXT(0x01, '不动\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_686',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_661',
    )

    OP_6F(0x0004, 0)
    OP_73(0x0004)
    OP_6F(0x0003, 120)
    OP_70(0x0003, 0x00000000)
    OP_73(0x0003)
    OP_A3(0x0003)

    Jump('loc_686')

    def _loc_661(): pass

    label('loc_661')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_686',
    )

    OP_6F(0x0004, 0)
    OP_73(0x0004)
    OP_6F(0x0002, 120)
    OP_70(0x0002, 0x00000000)
    OP_73(0x0002)
    OP_A3(0x0002)

    def _loc_686(): pass

    label('loc_686')

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
