import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3514_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3514   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3514.x'
    header.mapIndex       = 1
    header.bgm            = 33
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
        ('ED6_DT09/CH10710._CH', 'ED6_DT09/CH10710P._CP'),
        ('ED6_DT09/CH10711._CH', 'ED6_DT09/CH10711P._CP'),
        ('ED6_DT09/CH10720._CH', 'ED6_DT09/CH10720P._CP'),
        ('ED6_DT09/CH10721._CH', 'ED6_DT09/CH10721P._CP'),
        ('ED6_DT09/CH10730._CH', 'ED6_DT09/CH10730P._CP'),
        ('ED6_DT09/CH10731._CH', 'ED6_DT09/CH10731P._CP'),
        ('ED6_DT09/CH10740._CH', 'ED6_DT09/CH10740P._CP'),
        ('ED6_DT09/CH10741._CH', 'ED6_DT09/CH10741P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xEA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 2040,
            z           = 0,
            y           = 3920,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F6,
            word_18     = 0x158D,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 3970,
            z           = 0,
            y           = -1960,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F6,
            word_18     = 0x158E,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -1920,
            z           = 0,
            y           = -4010,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F6,
            word_18     = 0x158F,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -4080,
            z           = 0,
            y           = 1890,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F6,
            word_18     = 0x1590,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -120,
            z           = 0,
            y           = -17970,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F8,
            word_18     = 0x1591,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x176
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x176
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -4690,
            triggerZ            = 0,
            triggerY            = -22750,
            triggerRange        = 1000,
            actorX              = -4690,
            actorZ              = 0,
            actorY              = -23410,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4740,
            triggerZ            = 0,
            triggerY            = -22710,
            triggerRange        = 1000,
            actorX              = 4800,
            actorZ              = 0,
            actorY              = -23330,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1BE
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x1BF
@scena.Code('func_01_1BF')
def func_01_1BF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A9, 1, 0x1549)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D1',
    )

    OP_6F(0x0000, 0)

    Jump('loc_1D8')

    def _loc_1D1(): pass

    label('loc_1D1')

    OP_6F(0x0000, 60)

    def _loc_1D8(): pass

    label('loc_1D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A9, 2, 0x154A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1EA',
    )

    OP_6F(0x0001, 0)

    Jump('loc_1F1')

    def _loc_1EA(): pass

    label('loc_1EA')

    OP_6F(0x0001, 60)

    def _loc_1F1(): pass

    label('loc_1F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B1, 5, 0x158D)),
            Expr.Return,
        ),
        'loc_1FD',
    )

    ChrSetFlags(0x0008, 0x0080)

    def _loc_1FD(): pass

    label('loc_1FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B1, 6, 0x158E)),
            Expr.Return,
        ),
        'loc_209',
    )

    ChrSetFlags(0x0009, 0x0080)

    def _loc_209(): pass

    label('loc_209')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B1, 7, 0x158F)),
            Expr.Return,
        ),
        'loc_215',
    )

    ChrSetFlags(0x000A, 0x0080)

    def _loc_215(): pass

    label('loc_215')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B2, 0, 0x1590)),
            Expr.Return,
        ),
        'loc_221',
    )

    ChrSetFlags(0x000B, 0x0080)

    def _loc_221(): pass

    label('loc_221')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B2, 1, 0x1591)),
            Expr.Return,
        ),
        'loc_22D',
    )

    ChrSetFlags(0x000C, 0x0080)

    def _loc_22D(): pass

    label('loc_22D')

    Return()

# id: 0x0002 offset: 0x22E
@scena.Code('func_02_22E')
def func_02_22E():
    UnlockAchievement(0x02, 0x00CD, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A9, 1, 0x1549)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_30B',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['行动力２'], 1)"),
            Expr.Return,
        ),
        'loc_2A2',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['行动力２']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x02A9, 1, 0x1549))

    Jump('loc_308')

    def _loc_2A2(): pass

    label('loc_2A2')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['行动力２']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['行动力２']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_308(): pass

    label('loc_308')

    Jump('loc_33C')

    def _loc_30B(): pass

    label('loc_30B')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_33C(): pass

    label('loc_33C')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x34A
@scena.Code('func_03_34A')
def func_03_34A():
    UnlockAchievement(0x02, 0x00CE, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A9, 2, 0x154A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_427',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_3BE',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x02A9, 2, 0x154A))

    Jump('loc_424')

    def _loc_3BE(): pass

    label('loc_3BE')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_424(): pass

    label('loc_424')

    Jump('loc_458')

    def _loc_427(): pass

    label('loc_427')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_458(): pass

    label('loc_458')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
