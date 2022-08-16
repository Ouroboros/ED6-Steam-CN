import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0601_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0601   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0601.x'
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
            triggerX            = 16750,
            triggerZ            = 0,
            triggerY            = 57710,
            triggerRange        = 1700,
            actorX              = 16750,
            actorZ              = 2500,
            actorY              = 57710,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 46510,
            triggerZ            = 0,
            triggerY            = 67900,
            triggerRange        = 1700,
            actorX              = 46510,
            actorZ              = 2500,
            actorY              = 67900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 53050,
            triggerZ            = 0,
            triggerY            = 92420,
            triggerRange        = 1700,
            actorX              = 53050,
            actorZ              = 2500,
            actorY              = 92420,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x114
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x115
@scena.Code('func_01_115')
def func_01_115():
    OP_72(0x0000, 0x0028)
    OP_72(0x0001, 0x0028)
    OP_72(0x0002, 0x0028)
    OP_72(0x0003, 0x0028)
    OP_72(0x0004, 0x0028)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_143',
    )

    OP_6F(0x0007, 60)
    OP_6F(0x0000, 260)

    def _loc_143(): pass

    label('loc_143')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_158',
    )

    OP_6F(0x0007, 60)
    OP_6F(0x0000, 260)

    def _loc_158(): pass

    label('loc_158')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_16D',
    )

    OP_6F(0x0000, 60)
    OP_6F(0x0004, 260)

    def _loc_16D(): pass

    label('loc_16D')

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

# id: 0x0002 offset: 0x178
@scena.Code('func_02_178')
def func_02_178():
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
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_23B',
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
        'loc_1EE',
    )

    OP_6F(0x0002, 0)
    OP_70(0x0002, 60)
    OP_73(0x0002)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_20F')

    def _loc_1EE(): pass

    label('loc_1EE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_20F',
    )

    OP_6F(0x0002, 100)
    OP_70(0x0002, 160)
    OP_73(0x0002)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_20F(): pass

    label('loc_20F')

    CameraMove(52660, -60, 67850, 500)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 120)
    OP_73(0x0001)
    OP_69(0x0000, 600)

    Jump('loc_2C9')

    def _loc_23B(): pass

    label('loc_23B')

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
        'loc_2C9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_285',
    )

    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)
    OP_73(0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_2A0')

    def _loc_285(): pass

    label('loc_285')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2A0',
    )

    OP_6F(0x0002, 160)
    OP_70(0x0002, 100)
    OP_73(0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_2A0(): pass

    label('loc_2A0')

    CameraMove(52660, -60, 67850, 500)
    OP_6F(0x0001, 120)
    OP_70(0x0001, 0)
    OP_73(0x0001)
    OP_69(0x0000, 600)

    def _loc_2C9(): pass

    label('loc_2C9')

    MapSetFlags(0x00000001)
    TalkEnd(0x00FF)

    Return()

# id: 0x0003 offset: 0x2D2
@scena.Code('func_03_2D2')
def func_03_2D2():
    TalkBegin(0x00FF)

    Talk(
        (
            '魔兽下来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FF)

    Return()

# id: 0x0004 offset: 0x2E9
@scena.Code('func_04_2E9')
def func_04_2E9():
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
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_35A',
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
    OP_6F(0x0000, 0)
    OP_70(0x0000, 60)
    OP_73(0x0000)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 250)
    OP_73(0x0004)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    MapSetFlags(0x00000001)
    EventEnd(0x03)

    Return()

    def _loc_35A(): pass

    label('loc_35A')

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
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)
    OP_73(0x0000)
    OP_6F(0x0004, 250)
    OP_70(0x0004, 0)
    OP_73(0x0004)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    MapSetFlags(0x00000001)
    EventEnd(0x03)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
