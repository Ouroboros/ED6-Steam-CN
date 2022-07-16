import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2610_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2610   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2610.x'
    header.mapIndex       = 1
    header.bgm            = 32
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T2610._SN', 'ED6_DT01/T2610_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x376
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
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT09/CH10530._CH', 'ED6_DT09/CH10530P._CP'),
        ('ED6_DT09/CH10531._CH', 'ED6_DT09/CH10531P._CP'),
    ]

# id: 0x10002 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xC2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 510,
            z           = 0,
            y           = 10520,
            word_0C     = 0x0000,
            word_0E     = 0x0001,
            byte_10     = 0x81,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F5,
            word_18     = 0x04A5,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -33210,
            z           = 250,
            y           = 28100,
            word_0C     = 0x0000,
            word_0E     = 0x0001,
            byte_10     = 0x81,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F5,
            word_18     = 0x04A6,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 8140,
            z           = 0,
            y           = 20000,
            word_0C     = 0x0000,
            word_0E     = 0x0001,
            byte_10     = 0x81,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F5,
            word_18     = 0x04A7,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -93270,
            z           = 0,
            y           = 1680,
            word_0C     = 0x0000,
            word_0E     = 0x0001,
            byte_10     = 0x81,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F5,
            word_18     = 0x04A8,
            word_1A     = 0x0000,
        ),
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
            triggerX            = -80260,
            triggerZ            = 250,
            triggerY            = 31430,
            triggerRange        = 1000,
            actorX              = -80210,
            actorZ              = 250,
            actorY              = 32080,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x156
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x157
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_178',
    )

    OP_B1('t2610_y')

    Jump('loc_181')

    def _loc_178(): pass

    label('loc_178')

    OP_B1('t2610_n')

    def _loc_181(): pass

    label('loc_181')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x2000)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1D2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0094, 5, 0x4A5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AB',
    )

    ClearChrFlags(0x0008, 0x0080)

    def _loc_1AB(): pass

    label('loc_1AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0094, 6, 0x4A6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B8',
    )

    ClearChrFlags(0x0009, 0x0080)

    def _loc_1B8(): pass

    label('loc_1B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0094, 7, 0x4A7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C5',
    )

    ClearChrFlags(0x000A, 0x0080)

    def _loc_1C5(): pass

    label('loc_1C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0095, 0, 0x4A8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D2',
    )

    ClearChrFlags(0x000B, 0x0080)

    def _loc_1D2(): pass

    label('loc_1D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x2000)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_228',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_228',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0094, 5, 0x4A5)),
            Expr.Return,
        ),
        'loc_228',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0094, 6, 0x4A6)),
            Expr.Return,
        ),
        'loc_228',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0094, 7, 0x4A7)),
            Expr.Return,
        ),
        'loc_228',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0095, 0, 0x4A8)),
            Expr.Return,
        ),
        'loc_228',
    )

    OP_28(0x0027, 0x01, 0x4000)
    OP_28(0x003D, 0x01, 0x0100)
    OP_2C(0x003D, 0x03E8)
    OP_2B(0x003D, 0x0003)
    Event(1, 0x0000)

    def _loc_228(): pass

    label('loc_228')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0099, 2, 0x4CA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_23A',
    )

    OP_6F(0x000B, 0)

    Jump('loc_241')

    def _loc_23A(): pass

    label('loc_23A')

    OP_6F(0x000B, 60)

    def _loc_241(): pass

    label('loc_241')

    Return()

# id: 0x0002 offset: 0x242
@scena.Code('ReInit')
def ReInit():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0099, 2, 0x4CA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_32C',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000B, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FC, 1)"),
            Expr.Return,
        ),
        'loc_2B6',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '复苏药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0099, 2, 0x4CA))

    Jump('loc_329')

    def _loc_2B6(): pass

    label('loc_2B6')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '复苏药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '复苏药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000B, 60)
    OP_70(0x000B, 0)

    def _loc_329(): pass

    label('loc_329')

    Jump('loc_362')

    def _loc_32C(): pass

    label('loc_32C')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0xA3)
    def _loc_362(): pass

    label('loc_362')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
