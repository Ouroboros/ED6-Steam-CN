import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1212_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1212   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1212.x'
    header.mapIndex       = 1
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2C8
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
        ('ED6_DT09/CH10410._CH', 'ED6_DT09/CH10410P._CP'),
        ('ED6_DT09/CH10411._CH', 'ED6_DT09/CH10411P._CP'),
        ('ED6_DT09/CH10420._CH', 'ED6_DT09/CH10420P._CP'),
        ('ED6_DT09/CH10421._CH', 'ED6_DT09/CH10421P._CP'),
        ('ED6_DT09/CH10430._CH', 'ED6_DT09/CH10430P._CP'),
        ('ED6_DT09/CH10431._CH', 'ED6_DT09/CH10431P._CP'),
        ('ED6_DT09/CH10440._CH', 'ED6_DT09/CH10440P._CP'),
        ('ED6_DT09/CH10441._CH', 'ED6_DT09/CH10441P._CP'),
    ]

# id: 0x10002 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xEA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -13760,
            z           = 0,
            y           = 16490,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0091,
            word_18     = 0x1BA0,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 14080,
            z           = 0,
            y           = -14300,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0091,
            word_18     = 0x1BA1,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -60,
            z           = 0,
            y           = 40,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0091,
            word_18     = 0x1BA2,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -14040,
            z           = 0,
            y           = -14060,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0091,
            word_18     = 0x1BA3,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x15A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x15A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -17190,
            triggerZ            = 0,
            triggerY            = 12850,
            triggerRange        = 1000,
            actorX              = -16720,
            actorZ              = 1500,
            actorY              = 13450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x17E
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x17F
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036A, 3, 0x1B53)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_191',
    )

    OP_6F(0x0000, 0)

    Jump('loc_198')

    def _loc_191(): pass

    label('loc_191')

    OP_6F(0x0000, 60)

    def _loc_198(): pass

    label('loc_198')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0374, 0, 0x1BA0)),
            Expr.Return,
        ),
        'loc_1A4',
    )

    SetChrFlags(0x0008, 0x0080)

    def _loc_1A4(): pass

    label('loc_1A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0374, 1, 0x1BA1)),
            Expr.Return,
        ),
        'loc_1B0',
    )

    SetChrFlags(0x0009, 0x0080)

    def _loc_1B0(): pass

    label('loc_1B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0374, 2, 0x1BA2)),
            Expr.Return,
        ),
        'loc_1BC',
    )

    SetChrFlags(0x000A, 0x0080)

    def _loc_1BC(): pass

    label('loc_1BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0374, 3, 0x1BA3)),
            Expr.Return,
        ),
        'loc_1C8',
    )

    SetChrFlags(0x000B, 0x0080)

    def _loc_1C8(): pass

    label('loc_1C8')

    Return()

# id: 0x0002 offset: 0x1C9
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0x33, 0x00, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036A, 3, 0x1B53)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_296',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000001E)
    OP_73(0x0000)
    OP_6F(0x0000, 30)
    AddSepith(0x00, 0x0032)
    AddSepith(0x01, 0x0032)
    AddSepith(0x02, 0x0032)
    AddSepith(0x03, 0x0032)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×５０\n',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×５０\n',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×５０\n',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×５０\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1B53)

    Jump('loc_2B0')

    def _loc_296(): pass

    label('loc_296')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_2B0(): pass

    label('loc_2B0')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
