import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C0413_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0413   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0413.x'
    header.mapIndex       = 1
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2BF
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
        ('ED6_DT09/CH10070._CH', 'ED6_DT09/CH10070P._CP'),
        ('ED6_DT09/CH10071._CH', 'ED6_DT09/CH10071P._CP'),
        ('ED6_DT09/CH10040._CH', 'ED6_DT09/CH10040P._CP'),
        ('ED6_DT09/CH10041._CH', 'ED6_DT09/CH10041P._CP'),
        ('ED6_DT09/CH10150._CH', 'ED6_DT09/CH10150P._CP'),
        ('ED6_DT09/CH10151._CH', 'ED6_DT09/CH10151P._CP'),
    ]

# id: 0x10002 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xDA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 17840,
            z           = 0,
            y           = 190,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0032,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 6290,
            z           = 0,
            y           = -20690,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0035,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 170,
            z           = 0,
            y           = 7010,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0033,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -19420,
            z           = 0,
            y           = 2050,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0039,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x14A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x14A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -16700,
            triggerZ            = 0,
            triggerY            = -13650,
            triggerRange        = 1000,
            actorX              = -16700,
            actorZ              = 1500,
            actorY              = -13650,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x16E
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x16F
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0051, 5, 0x28D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_181',
    )

    OP_6F(0x0000, 0)

    Jump('loc_188')

    def _loc_181(): pass

    label('loc_181')

    OP_6F(0x0000, 60)

    def _loc_188(): pass

    label('loc_188')

    Return()

# id: 0x0002 offset: 0x189
@scena.Code('ReInit')
def ReInit():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0051, 5, 0x28D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_273',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F5, 1)"),
            Expr.Return,
        ),
        'loc_1FD',
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
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0051, 5, 0x28D))

    Jump('loc_270')

    def _loc_1FD(): pass

    label('loc_1FD')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_270(): pass

    label('loc_270')

    Jump('loc_2AB')

    def _loc_273(): pass

    label('loc_273')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    WaitEffect(0x0F, 0x03)
    def _loc_2AB(): pass

    label('loc_2AB')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
