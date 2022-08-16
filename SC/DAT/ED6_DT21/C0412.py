import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0412_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0412   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0412.x'
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
            x           = 0,
            z           = 0,
            y           = -4950,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0032,
            word_18     = 0x1970,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -17930,
            z           = 0,
            y           = 30,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0033,
            word_18     = 0x1971,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 18010,
            z           = 0,
            y           = 50,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0034,
            word_18     = 0x1972,
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
            triggerX            = 0,
            triggerZ            = 0,
            triggerY            = 700,
            triggerRange        = 1000,
            actorX              = 0,
            actorZ              = 0,
            actorY              = 0,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4570,
            triggerZ            = 0,
            triggerY            = 22600,
            triggerRange        = 1000,
            actorX              = 4570,
            actorZ              = 0,
            actorY              = 23200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4510,
            triggerZ            = 0,
            triggerY            = 22600,
            triggerRange        = 1000,
            actorX              = -4600,
            actorZ              = 0,
            actorY              = 23220,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1BA
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x1BB
@scena.Code('func_01_1BB')
def func_01_1BB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032A, 0, 0x1950)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CD',
    )

    OP_6F(0x0000, 0)

    Jump('loc_1D4')

    def _loc_1CD(): pass

    label('loc_1CD')

    OP_6F(0x0000, 60)

    def _loc_1D4(): pass

    label('loc_1D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032A, 2, 0x1952)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E6',
    )

    OP_6F(0x0001, 0)

    Jump('loc_1ED')

    def _loc_1E6(): pass

    label('loc_1E6')

    OP_6F(0x0001, 60)

    def _loc_1ED(): pass

    label('loc_1ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032A, 4, 0x1954)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FF',
    )

    OP_6F(0x0002, 0)

    Jump('loc_206')

    def _loc_1FF(): pass

    label('loc_1FF')

    OP_6F(0x0002, 60)

    def _loc_206(): pass

    label('loc_206')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032E, 0, 0x1970)),
            Expr.Return,
        ),
        'loc_212',
    )

    ChrSetFlags(0x0008, 0x0080)

    def _loc_212(): pass

    label('loc_212')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032E, 1, 0x1971)),
            Expr.Return,
        ),
        'loc_21E',
    )

    ChrSetFlags(0x0009, 0x0080)

    def _loc_21E(): pass

    label('loc_21E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032E, 2, 0x1972)),
            Expr.Return,
        ),
        'loc_22A',
    )

    ChrSetFlags(0x000A, 0x0080)

    def _loc_22A(): pass

    label('loc_22A')

    Return()

# id: 0x0002 offset: 0x22B
@scena.Code('func_02_22B')
def func_02_22B():
    UnlockAchievement(0x02, 0x000C, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032A, 0, 0x1950)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_308',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['翠耀石护符'], 1)"),
            Expr.Return,
        ),
        'loc_29F',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['翠耀石护符']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x032A, 0, 0x1950))

    Jump('loc_305')

    def _loc_29F(): pass

    label('loc_29F')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['翠耀石护符']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['翠耀石护符']),
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

    def _loc_305(): pass

    label('loc_305')

    Jump('loc_339')

    def _loc_308(): pass

    label('loc_308')

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
    def _loc_339(): pass

    label('loc_339')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x347
@scena.Code('func_03_347')
def func_03_347():
    UnlockAchievement(0x02, 0x000D, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032A, 2, 0x1952)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C5',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 30)
    OP_73(0x0001)
    OP_6F(0x0001, 30)
    AddSepith(0x01, 200)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×２００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x032A, 2, 0x1952))

    Jump('loc_3DF')

    def _loc_3C5(): pass

    label('loc_3C5')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_3DF(): pass

    label('loc_3DF')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x3F1
@scena.Code('func_04_3F1')
def func_04_3F1():
    UnlockAchievement(0x02, 0x000E, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032A, 4, 0x1954)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4CE',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_465',
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
    SetScenaFlags(ScenaFlag(0x032A, 4, 0x1954))

    Jump('loc_4CB')

    def _loc_465(): pass

    label('loc_465')

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
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_4CB(): pass

    label('loc_4CB')

    Jump('loc_4FF')

    def _loc_4CE(): pass

    label('loc_4CE')

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
    def _loc_4FF(): pass

    label('loc_4FF')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
