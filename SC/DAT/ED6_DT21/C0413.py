import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0413_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0413   ._SN')

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
        ('ED6_DT09/CH10040._CH', 'ED6_DT09/CH10040P._CP'),
        ('ED6_DT09/CH10041._CH', 'ED6_DT09/CH10041P._CP'),
        ('ED6_DT09/CH10070._CH', 'ED6_DT09/CH10070P._CP'),
        ('ED6_DT09/CH10071._CH', 'ED6_DT09/CH10071P._CP'),
        ('ED6_DT09/CH10150._CH', 'ED6_DT09/CH10150P._CP'),
        ('ED6_DT09/CH10151._CH', 'ED6_DT09/CH10151P._CP'),
        ('ED6_DT09/CH10190._CH', 'ED6_DT09/CH10190P._CP'),
        ('ED6_DT09/CH10191._CH', 'ED6_DT09/CH10191P._CP'),
        ('ED6_DT29/CH12140._CH', 'ED6_DT29/CH12140P._CP'),
        ('ED6_DT29/CH12141._CH', 'ED6_DT29/CH12141P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xFA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 17840,
            z           = 0,
            y           = 190,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0034,
            word_18     = 0x1973,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 170,
            z           = 0,
            y           = 7010,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0032,
            word_18     = 0x1974,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -19420,
            z           = 0,
            y           = 2050,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0033,
            word_18     = 0x1975,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x14E
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x14E
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

# id: 0x0000 offset: 0x172
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x173
@scena.Code('func_01_173')
def func_01_173():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032A, 5, 0x1955)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_185',
    )

    OP_6F(0x0000, 0)

    Jump('loc_18C')

    def _loc_185(): pass

    label('loc_185')

    OP_6F(0x0000, 60)

    def _loc_18C(): pass

    label('loc_18C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032E, 3, 0x1973)),
            Expr.Return,
        ),
        'loc_198',
    )

    ChrSetFlags(0x0008, 0x0080)

    def _loc_198(): pass

    label('loc_198')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032E, 4, 0x1974)),
            Expr.Return,
        ),
        'loc_1A4',
    )

    ChrSetFlags(0x0009, 0x0080)

    def _loc_1A4(): pass

    label('loc_1A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032E, 5, 0x1975)),
            Expr.Return,
        ),
        'loc_1B0',
    )

    ChrSetFlags(0x000A, 0x0080)

    def _loc_1B0(): pass

    label('loc_1B0')

    Return()

# id: 0x0002 offset: 0x1B1
@scena.Code('func_02_1B1')
def func_02_1B1():
    UnlockAchievement(0x02, 0x000F, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032A, 5, 0x1955)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_28E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['强力果汁'], 1)"),
            Expr.Return,
        ),
        'loc_225',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['强力果汁']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x032A, 5, 0x1955))

    Jump('loc_28B')

    def _loc_225(): pass

    label('loc_225')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['强力果汁']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['强力果汁']),
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

    def _loc_28B(): pass

    label('loc_28B')

    Jump('loc_2BF')

    def _loc_28E(): pass

    label('loc_28E')

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
    def _loc_2BF(): pass

    label('loc_2BF')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
