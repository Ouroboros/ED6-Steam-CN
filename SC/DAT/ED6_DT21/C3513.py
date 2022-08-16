import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3513_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3513   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3513.x'
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
            x           = 13970,
            z           = 0,
            y           = -14160,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F8,
            word_18     = 0x1580,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -14060,
            z           = 0,
            y           = -14180,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F8,
            word_18     = 0x1581,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -10,
            z           = 0,
            y           = -3340,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F7,
            word_18     = 0x1582,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 3070,
            z           = 0,
            y           = -30,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F7,
            word_18     = 0x1583,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -100,
            z           = 0,
            y           = 3100,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F7,
            word_18     = 0x1584,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -3090,
            z           = 0,
            y           = 40,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F7,
            word_18     = 0x1585,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -1110,
            z           = 0,
            y           = -1180,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F7,
            word_18     = 0x1586,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 1000,
            z           = 0,
            y           = -1130,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F7,
            word_18     = 0x1587,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 1090,
            z           = 0,
            y           = 1010,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F7,
            word_18     = 0x1588,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -1130,
            z           = 0,
            y           = 1030,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F7,
            word_18     = 0x1589,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -70,
            z           = 0,
            y           = -40,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F7,
            word_18     = 0x158A,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 12560,
            z           = 0,
            y           = 17070,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F6,
            word_18     = 0x158B,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -13140,
            z           = 0,
            y           = 17140,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F6,
            word_18     = 0x158C,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x256
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x256
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 12560,
            triggerZ            = 0,
            triggerY            = -18130,
            triggerRange        = 1000,
            actorX              = 12660,
            actorZ              = 0,
            actorY              = -18840,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -12820,
            triggerZ            = 0,
            triggerY            = -17830,
            triggerRange        = 1000,
            actorX              = -12820,
            actorZ              = 0,
            actorY              = -18490,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x29E
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x29F
@scena.Code('func_01_29F')
def func_01_29F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A8, 7, 0x1547)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B1',
    )

    OP_6F(0x0000, 0)

    Jump('loc_2B8')

    def _loc_2B1(): pass

    label('loc_2B1')

    OP_6F(0x0000, 60)

    def _loc_2B8(): pass

    label('loc_2B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A9, 0, 0x1548)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CA',
    )

    OP_6F(0x0001, 0)

    Jump('loc_2D1')

    def _loc_2CA(): pass

    label('loc_2CA')

    OP_6F(0x0001, 60)

    def _loc_2D1(): pass

    label('loc_2D1')

    OP_E0(0x00, 0x3C, 0x32, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0xBA, 0xFF, 0xFF)
    OP_E0(0x01, 0x28, 0xCE, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x40, 0xBB, 0xFF, 0xFF)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B0, 0, 0x1580)),
            Expr.Return,
        ),
        'loc_2F9',
    )

    ChrSetFlags(0x0008, 0x0080)

    def _loc_2F9(): pass

    label('loc_2F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B0, 1, 0x1581)),
            Expr.Return,
        ),
        'loc_305',
    )

    ChrSetFlags(0x0009, 0x0080)

    def _loc_305(): pass

    label('loc_305')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B0, 2, 0x1582)),
            Expr.Return,
        ),
        'loc_311',
    )

    ChrSetFlags(0x000A, 0x0080)

    def _loc_311(): pass

    label('loc_311')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B0, 3, 0x1583)),
            Expr.Return,
        ),
        'loc_31D',
    )

    ChrSetFlags(0x000B, 0x0080)

    def _loc_31D(): pass

    label('loc_31D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B0, 4, 0x1584)),
            Expr.Return,
        ),
        'loc_329',
    )

    ChrSetFlags(0x000C, 0x0080)

    def _loc_329(): pass

    label('loc_329')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B0, 5, 0x1585)),
            Expr.Return,
        ),
        'loc_335',
    )

    ChrSetFlags(0x000D, 0x0080)

    def _loc_335(): pass

    label('loc_335')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B0, 6, 0x1586)),
            Expr.Return,
        ),
        'loc_341',
    )

    ChrSetFlags(0x000E, 0x0080)

    def _loc_341(): pass

    label('loc_341')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B0, 7, 0x1587)),
            Expr.Return,
        ),
        'loc_34D',
    )

    ChrSetFlags(0x000F, 0x0080)

    def _loc_34D(): pass

    label('loc_34D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B1, 0, 0x1588)),
            Expr.Return,
        ),
        'loc_359',
    )

    ChrSetFlags(0x0010, 0x0080)

    def _loc_359(): pass

    label('loc_359')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B1, 1, 0x1589)),
            Expr.Return,
        ),
        'loc_365',
    )

    ChrSetFlags(0x0011, 0x0080)

    def _loc_365(): pass

    label('loc_365')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B1, 2, 0x158A)),
            Expr.Return,
        ),
        'loc_371',
    )

    ChrSetFlags(0x0012, 0x0080)

    def _loc_371(): pass

    label('loc_371')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B1, 3, 0x158B)),
            Expr.Return,
        ),
        'loc_37D',
    )

    ChrSetFlags(0x0013, 0x0080)

    def _loc_37D(): pass

    label('loc_37D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B1, 4, 0x158C)),
            Expr.Return,
        ),
        'loc_389',
    )

    ChrSetFlags(0x0014, 0x0080)

    def _loc_389(): pass

    label('loc_389')

    Return()

# id: 0x0002 offset: 0x38A
@scena.Code('func_02_38A')
def func_02_38A():
    UnlockAchievement(0x02, 0x00CB, 0x00)
    UnlockAchievement(0x02, 0x020B, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A8, 7, 0x1547)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_46C',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['海鲜果冻'], 1)"),
            Expr.Return,
        ),
        'loc_403',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['海鲜果冻']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x02A8, 7, 0x1547))

    Jump('loc_469')

    def _loc_403(): pass

    label('loc_403')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['海鲜果冻']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['海鲜果冻']),
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

    def _loc_469(): pass

    label('loc_469')

    Jump('loc_49D')

    def _loc_46C(): pass

    label('loc_46C')

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
    def _loc_49D(): pass

    label('loc_49D')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x4AB
@scena.Code('func_03_4AB')
def func_03_4AB():
    UnlockAchievement(0x02, 0x00CC, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A9, 0, 0x1548)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_588',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_51F',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x02A9, 0, 0x1548))

    Jump('loc_585')

    def _loc_51F(): pass

    label('loc_51F')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['中回复药']),
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

    def _loc_585(): pass

    label('loc_585')

    Jump('loc_5B9')

    def _loc_588(): pass

    label('loc_588')

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
    def _loc_5B9(): pass

    label('loc_5B9')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
