import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0302_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0302   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0302.x'
    header.mapIndex       = 19
    header.bgm            = 21
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
        ('ED6_DT29/CH12430._CH', 'ED6_DT29/CH12430P._CP'),
        ('ED6_DT29/CH12431._CH', 'ED6_DT29/CH12431P._CP'),
        ('ED6_DT09/CH10010._CH', 'ED6_DT09/CH10010P._CP'),
        ('ED6_DT09/CH10011._CH', 'ED6_DT09/CH10011P._CP'),
        ('ED6_DT09/CH10280._CH', 'ED6_DT09/CH10280P._CP'),
        ('ED6_DT09/CH10281._CH', 'ED6_DT09/CH10281P._CP'),
        ('ED6_DT29/CH12400._CH', 'ED6_DT29/CH12400P._CP'),
        ('ED6_DT29/CH12401._CH', 'ED6_DT29/CH12401P._CP'),
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
            x           = 55300,
            z           = 160,
            y           = -13730,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 49420,
            z           = 40,
            y           = 7980,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 58410,
            z           = -10,
            y           = -820,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 69340,
            z           = -90,
            y           = 4080,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x15A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x15A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 48430,
            triggerZ            = -90,
            triggerY            = 16780,
            triggerRange        = 1000,
            actorX              = 48560,
            actorZ              = -90,
            actorY              = 17480,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 77150,
            triggerZ            = -50,
            triggerY            = 8730,
            triggerRange        = 1000,
            actorX              = 77860,
            actorZ              = -50,
            actorY              = 8730,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 65900,
            triggerZ            = 90,
            triggerY            = -5510,
            triggerRange        = 1000,
            actorX              = 65239,
            actorZ              = 90,
            actorY              = -5800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1C6
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x1C7
@scena.Code('func_01_1C7')
def func_01_1C7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032C, 5, 0x1965)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D9',
    )

    OP_6F(0x0004, 0)

    Jump('loc_1E0')

    def _loc_1D9(): pass

    label('loc_1D9')

    OP_6F(0x0004, 60)

    def _loc_1E0(): pass

    label('loc_1E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032C, 7, 0x1967)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F2',
    )

    OP_6F(0x0005, 0)

    Jump('loc_1F9')

    def _loc_1F2(): pass

    label('loc_1F2')

    OP_6F(0x0005, 60)

    def _loc_1F9(): pass

    label('loc_1F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032D, 1, 0x1969)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20B',
    )

    OP_6F(0x0006, 0)

    Jump('loc_212')

    def _loc_20B(): pass

    label('loc_20B')

    OP_6F(0x0006, 60)

    def _loc_212(): pass

    label('loc_212')

    ExecExpressionWithValue(
        0x0008,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_260',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_260',
    )

    MapSetFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0, 60000, 0)
    OP_C4(0x00, 0x00000004)

    def _loc_260(): pass

    label('loc_260')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_272',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x000B, 0x0080)

    def _loc_272(): pass

    label('loc_272')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 3, 0x1823)),
            Expr.Return,
        ),
        'loc_282',
    )

    OP_10(0x00, 0x01)
    OP_10(0x02, 0x00)

    Jump('loc_28F')

    def _loc_282(): pass

    label('loc_282')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 6, 0x1806)),
            Expr.Return,
        ),
        'loc_28F',
    )

    OP_10(0x00, 0x00)
    OP_10(0x02, 0x01)

    def _loc_28F(): pass

    label('loc_28F')

    Return()

# id: 0x0002 offset: 0x290
@scena.Code('func_02_290')
def func_02_290():
    UnlockAchievement(0x02, 0x0005, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032C, 5, 0x1965)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36D',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['野战军服'], 1)"),
            Expr.Return,
        ),
        'loc_304',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['野战军服']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x032C, 5, 0x1965))

    Jump('loc_36A')

    def _loc_304(): pass

    label('loc_304')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['野战军服']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['野战军服']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_36A(): pass

    label('loc_36A')

    Jump('loc_39E')

    def _loc_36D(): pass

    label('loc_36D')

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
    def _loc_39E(): pass

    label('loc_39E')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x3AC
@scena.Code('func_03_3AC')
def func_03_3AC():
    UnlockAchievement(0x02, 0x0006, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032C, 7, 0x1967)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_489',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['百合项链'], 1)"),
            Expr.Return,
        ),
        'loc_420',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['百合项链']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x032C, 7, 0x1967))

    Jump('loc_486')

    def _loc_420(): pass

    label('loc_420')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['百合项链']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['百合项链']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0)

    def _loc_486(): pass

    label('loc_486')

    Jump('loc_4BA')

    def _loc_489(): pass

    label('loc_489')

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
    def _loc_4BA(): pass

    label('loc_4BA')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x4C8
@scena.Code('func_04_4C8')
def func_04_4C8():
    UnlockAchievement(0x02, 0x0007, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032D, 1, 0x1969)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5A5',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0006, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['黑色手镯'], 1)"),
            Expr.Return,
        ),
        'loc_53C',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['黑色手镯']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x032D, 1, 0x1969))

    Jump('loc_5A2')

    def _loc_53C(): pass

    label('loc_53C')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['黑色手镯']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['黑色手镯']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0)

    def _loc_5A2(): pass

    label('loc_5A2')

    Jump('loc_5D6')

    def _loc_5A5(): pass

    label('loc_5A5')

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
    def _loc_5D6(): pass

    label('loc_5D6')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
