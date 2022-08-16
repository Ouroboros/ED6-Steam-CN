import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0602_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0602   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0602.x'
    header.mapIndex       = 1
    header.bgm            = 10
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
        ScenaActorData(
            triggerX            = -1160,
            triggerZ            = 0,
            triggerY            = 144370,
            triggerRange        = 1700,
            actorX              = -1160,
            actorZ              = 2500,
            actorY              = 144370,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -13210,
            triggerZ            = 0,
            triggerY            = 169110,
            triggerRange        = 1700,
            actorX              = -13210,
            actorZ              = 2500,
            actorY              = 169110,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4340,
            triggerZ            = 0,
            triggerY            = 181980,
            triggerRange        = 1700,
            actorX              = 4340,
            actorZ              = 2500,
            actorY              = 181980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -30880,
            triggerZ            = 0,
            triggerY            = 150510,
            triggerRange        = 1700,
            actorX              = -30880,
            actorZ              = 2500,
            actorY              = 150510,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x138
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x139
@scena.Code('func_01_139')
def func_01_139():
    OP_72(0x0000, 0x0028)
    OP_72(0x0001, 0x0028)
    OP_72(0x0002, 0x0028)
    OP_72(0x0003, 0x0028)
    OP_72(0x0004, 0x0028)
    OP_72(0x0005, 0x0028)
    OP_72(0x0006, 0x0028)
    OP_72(0x0007, 0x0028)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_176',
    )

    OP_6F(0x0001, 120)
    OP_6F(0x0006, 60)

    def _loc_176(): pass

    label('loc_176')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_18B',
    )

    OP_6F(0x0001, 120)
    OP_6F(0x0006, 160)

    def _loc_18B(): pass

    label('loc_18B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1A0',
    )

    OP_6F(0x0003, 120)
    OP_6F(0x0002, 60)

    def _loc_1A0(): pass

    label('loc_1A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1B5',
    )

    OP_6F(0x0003, 120)
    OP_6F(0x0002, 160)

    def _loc_1B5(): pass

    label('loc_1B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1CA',
    )

    OP_6F(0x0004, 120)
    OP_6F(0x0005, 60)

    def _loc_1CA(): pass

    label('loc_1CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1DF',
    )

    OP_6F(0x0004, 120)
    OP_6F(0x0005, 160)

    def _loc_1DF(): pass

    label('loc_1DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1F4',
    )

    OP_6F(0x0007, 60)
    OP_6F(0x0000, 260)

    def _loc_1F4(): pass

    label('loc_1F4')

    ExecExpressionWithVar(
        0x2A,
        (
            (Expr.PushLong, 0x6D6),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x1FF
@scena.Code('func_02_1FF')
def func_02_1FF():
    TalkBegin(0x00FF)
    MapClearFlags(0x00000001)

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
        'loc_2C2',
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
        'loc_275',
    )

    OP_6F(0x0006, 0)
    OP_70(0x0006, 60)
    OP_73(0x0006)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_296')

    def _loc_275(): pass

    label('loc_275')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_296',
    )

    OP_6F(0x0006, 100)
    OP_70(0x0006, 160)
    OP_73(0x0006)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_296(): pass

    label('loc_296')

    CameraMove(3880, 0, 135860, 500)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 120)
    OP_73(0x0001)
    OP_69(0x0000, 600)

    Jump('loc_350')

    def _loc_2C2(): pass

    label('loc_2C2')

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
        'loc_350',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_30C',
    )

    OP_6F(0x0006, 60)
    OP_70(0x0006, 0)
    OP_73(0x0006)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_327')

    def _loc_30C(): pass

    label('loc_30C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_327',
    )

    OP_6F(0x0006, 160)
    OP_70(0x0006, 100)
    OP_73(0x0006)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_327(): pass

    label('loc_327')

    CameraMove(3880, 0, 135860, 500)
    OP_6F(0x0001, 120)
    OP_70(0x0001, 0)
    OP_73(0x0001)
    OP_69(0x0000, 600)

    def _loc_350(): pass

    label('loc_350')

    MapSetFlags(0x00000001)
    TalkEnd(0x00FF)

    Return()

# id: 0x0003 offset: 0x359
@scena.Code('func_03_359')
def func_03_359():
    TalkBegin(0x00FF)
    MapClearFlags(0x00000001)

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
        'loc_41C',
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
        'loc_3CF',
    )

    OP_6F(0x0002, 0)
    OP_70(0x0002, 60)
    OP_73(0x0002)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_3F0')

    def _loc_3CF(): pass

    label('loc_3CF')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F0',
    )

    OP_6F(0x0002, 100)
    OP_70(0x0002, 160)
    OP_73(0x0002)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_3F0(): pass

    label('loc_3F0')

    CameraMove(-12270, 0, 174500, 500)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 120)
    OP_73(0x0003)
    OP_69(0x0000, 600)

    Jump('loc_4AA')

    def _loc_41C(): pass

    label('loc_41C')

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
        'loc_4AA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_466',
    )

    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)
    OP_73(0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_481')

    def _loc_466(): pass

    label('loc_466')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_481',
    )

    OP_6F(0x0002, 160)
    OP_70(0x0002, 100)
    OP_73(0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_481(): pass

    label('loc_481')

    CameraMove(-12270, 0, 174500, 500)
    OP_6F(0x0003, 120)
    OP_70(0x0003, 0)
    OP_73(0x0003)
    OP_69(0x0000, 600)

    def _loc_4AA(): pass

    label('loc_4AA')

    MapSetFlags(0x00000001)
    TalkEnd(0x00FF)

    Return()

# id: 0x0004 offset: 0x4B3
@scena.Code('func_04_4B3')
def func_04_4B3():
    TalkBegin(0x00FF)
    MapClearFlags(0x00000001)

    Talk(
        (
            '有扳手。是否扳动？',
            TxtCtl.Enter,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_576',
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
        'loc_529',
    )

    OP_6F(0x0005, 0)
    OP_70(0x0005, 60)
    OP_73(0x0005)
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_54A')

    def _loc_529(): pass

    label('loc_529')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_54A',
    )

    OP_6F(0x0005, 100)
    OP_70(0x0005, 160)
    OP_73(0x0005)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_54A(): pass

    label('loc_54A')

    CameraMove(-8090, -60, 183030, 500)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 120)
    OP_73(0x0004)
    OP_69(0x0000, 600)

    Jump('loc_604')

    def _loc_576(): pass

    label('loc_576')

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
        'loc_604',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_5C0',
    )

    OP_6F(0x0005, 60)
    OP_70(0x0005, 0)
    OP_73(0x0005)
    ClearScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_5DB')

    def _loc_5C0(): pass

    label('loc_5C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_5DB',
    )

    OP_6F(0x0005, 160)
    OP_70(0x0005, 100)
    OP_73(0x0005)
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_5DB(): pass

    label('loc_5DB')

    CameraMove(-8090, -60, 183030, 500)
    OP_6F(0x0004, 120)
    OP_70(0x0004, 0)
    OP_73(0x0004)
    OP_69(0x0000, 600)

    def _loc_604(): pass

    label('loc_604')

    MapSetFlags(0x00000001)
    TalkEnd(0x00FF)

    Return()

# id: 0x0005 offset: 0x60D
@scena.Code('func_05_60D')
def func_05_60D():
    MapSetFlags(0x00000080)
    MapClearFlags(0x00000001)

    Talk(
        (
            '有扳手。是否扳动？',
            TxtCtl.Enter,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_67E',
    )

    Menu(
        0,
        260,
        200,
        0,
        (
            TXT(0x00, '降下\n'),
            TXT(0x01, '不动\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)
    EventBegin(0x00)
    OP_6F(0x0007, 0)
    OP_70(0x0007, 60)
    OP_73(0x0007)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 250)
    OP_73(0x0000)
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    MapSetFlags(0x00000001)
    EventEnd(0x03)

    Return()

    def _loc_67E(): pass

    label('loc_67E')

    Menu(
        0,
        260,
        200,
        0,
        (
            TXT(0x00, '升高\n'),
            TXT(0x01, '不动\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)
    EventBegin(0x00)
    OP_6F(0x0007, 60)
    OP_70(0x0007, 0)
    OP_73(0x0007)
    OP_6F(0x0000, 250)
    OP_70(0x0000, 0)
    OP_73(0x0000)
    ClearScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    MapSetFlags(0x00000001)
    EventEnd(0x03)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
