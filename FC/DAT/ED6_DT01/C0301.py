import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C0301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0301   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0301.x'
    header.mapIndex       = 19
    header.bgm            = 21
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x428
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x000088B8,
            dword_04        = 0x00000000,
            dword_08        = 0x00003E80,
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
            word_3A         = 19,
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
        ('ED6_DT09/CH10010._CH', 'ED6_DT09/CH10010P._CP'),
        ('ED6_DT09/CH10011._CH', 'ED6_DT09/CH10011P._CP'),
        ('ED6_DT09/CH10280._CH', 'ED6_DT09/CH10280P._CP'),
        ('ED6_DT09/CH10281._CH', 'ED6_DT09/CH10281P._CP'),
        ('ED6_DT09/CH10230._CH', 'ED6_DT09/CH10230P._CP'),
        ('ED6_DT09/CH10231._CH', 'ED6_DT09/CH10231P._CP'),
        ('ED6_DT09/CH10240._CH', 'ED6_DT09/CH10240P._CP'),
        ('ED6_DT09/CH10241._CH', 'ED6_DT09/CH10241P._CP'),
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
            x           = -5000,
            z           = 0,
            y           = -28000,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0048,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -13000,
            z           = -300,
            y           = -11000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x004E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 17000,
            z           = -300,
            y           = -5000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0043,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -23000,
            z           = 0,
            y           = 32000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0043,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 7000,
            z           = -100,
            y           = -27000,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x004F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 2000,
            z           = 0,
            y           = -4000,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0046,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 21000,
            z           = -300,
            y           = 11000,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0049,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -16000,
            z           = -300,
            y           = -3000,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0047,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 5000,
            z           = 0,
            y           = 14000,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x004D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 1000,
            z           = 0,
            y           = 26000,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0046,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x202
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x202
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -7330,
            triggerZ            = 0,
            triggerY            = 800,
            triggerRange        = 1500,
            actorX              = -7330,
            actorZ              = 1500,
            actorY              = 800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 10760,
            triggerZ            = 0,
            triggerY            = 21620,
            triggerRange        = 1500,
            actorX              = 10760,
            actorZ              = 1500,
            actorY              = 21620,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x24A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x24B
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 4, 0x284)),
            Expr.Return,
        ),
        'loc_260',
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_64(0x00, 0x0001)

    def _loc_260(): pass

    label('loc_260')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 5, 0x285)),
            Expr.Return,
        ),
        'loc_275',
    )

    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_64(0x01, 0x0001)

    def _loc_275(): pass

    label('loc_275')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 5, 0x265)),
            Expr.Return,
        ),
        'loc_285',
    )

    OP_10(0x01, 0x00)
    OP_10(0x03, 0x01)

    Jump('loc_28B')

    def _loc_285(): pass

    label('loc_285')

    OP_10(0x01, 0x01)
    OP_10(0x03, 0x00)

    def _loc_28B(): pass

    label('loc_28B')

    Return()

# id: 0x0002 offset: 0x28C
@scena.Code('ReInit')
def ReInit():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 4, 0x284)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_34D',
    )

    If(
        (
            (Expr.Eval, "AddItem(0x0386, 1)"),
            Expr.Return,
        ),
        'loc_2FB',
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '熊刺草',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_64(0x00, 0x0001)
    SetScenaFlags(ScenaFlag(0x0050, 4, 0x284))

    Jump('loc_34D')

    def _loc_2FB(): pass

    label('loc_2FB')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '熊刺草',
            (TxtCtl.SetColor, 0x0),
            '发现了，\n',
            (TxtCtl.SetColor, 0x0),
            '不过现有的数量太多，不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_34D(): pass

    label('loc_34D')

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x356
@scena.Code('func_03_356')
def func_03_356():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 5, 0x285)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_417',
    )

    If(
        (
            (Expr.Eval, "AddItem(0x0386, 1)"),
            Expr.Return,
        ),
        'loc_3C5',
    )

    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '熊刺草',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_64(0x01, 0x0001)
    SetScenaFlags(ScenaFlag(0x0050, 5, 0x285))

    Jump('loc_417')

    def _loc_3C5(): pass

    label('loc_3C5')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '熊刺草',
            (TxtCtl.SetColor, 0x0),
            '发现了，\n',
            (TxtCtl.SetColor, 0x0),
            '不过现有的数量太多，不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_417(): pass

    label('loc_417')

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
