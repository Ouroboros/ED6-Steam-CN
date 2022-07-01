import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3301   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3301.x'
    header.mapIndex       = 1
    header.bgm            = 32
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x791
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
        ('ED6_DT09/CH10630._CH', 'ED6_DT09/CH10630P._CP'),
        ('ED6_DT09/CH10631._CH', 'ED6_DT09/CH10631P._CP'),
        ('ED6_DT09/CH10640._CH', 'ED6_DT09/CH10640P._CP'),
        ('ED6_DT09/CH10641._CH', 'ED6_DT09/CH10641P._CP'),
        ('ED6_DT09/CH10650._CH', 'ED6_DT09/CH10650P._CP'),
        ('ED6_DT09/CH10651._CH', 'ED6_DT09/CH10651P._CP'),
        ('ED6_DT09/CH10660._CH', 'ED6_DT09/CH10660P._CP'),
        ('ED6_DT09/CH10661._CH', 'ED6_DT09/CH10661P._CP'),
        ('ED6_DT09/CH10670._CH', 'ED6_DT09/CH10670P._CP'),
        ('ED6_DT09/CH10671._CH', 'ED6_DT09/CH10671P._CP'),
        ('ED6_DT09/CH10680._CH', 'ED6_DT09/CH10680P._CP'),
        ('ED6_DT09/CH10681._CH', 'ED6_DT09/CH10681P._CP'),
        ('ED6_DT09/CH10690._CH', 'ED6_DT09/CH10690P._CP'),
        ('ED6_DT09/CH10691._CH', 'ED6_DT09/CH10691P._CP'),
        ('ED6_DT09/CH10700._CH', 'ED6_DT09/CH10700P._CP'),
        ('ED6_DT09/CH10701._CH', 'ED6_DT09/CH10701P._CP'),
        ('ED6_DT29/CH12420._CH', 'ED6_DT29/CH12420P._CP'),
        ('ED6_DT29/CH12421._CH', 'ED6_DT29/CH12421P._CP'),
    ]

# id: 0x10002 offset: 0x13A
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 151480,
            z           = 10,
            y           = -36090,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E2,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 173520,
            z           = -30,
            y           = -9860,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E4,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 145980,
            z           = 0,
            y           = -16110,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 133740,
            z           = -10,
            y           = -17360,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E3,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 100000,
            z           = 40,
            y           = -11970,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 103250,
            z           = 60,
            y           = -23320,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 86210,
            z           = -10,
            y           = -27450,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E1,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 68170,
            z           = 20,
            y           = -25410,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E3,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x21A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x21A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 158010,
            triggerZ            = 30,
            triggerY            = -64629,
            triggerRange        = 1000,
            actorX              = 157660,
            actorZ              = 1530,
            actorY              = -65230,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 140470,
            triggerZ            = -30,
            triggerY            = -11410,
            triggerRange        = 1000,
            actorX              = 140500,
            actorZ              = 1470,
            actorY              = -10700,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 90610,
            triggerZ            = 50,
            triggerY            = -19930,
            triggerRange        = 1000,
            actorX              = 91210,
            actorZ              = 1550,
            actorY              = -19850,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 97500,
            triggerZ            = -20,
            triggerY            = -18130,
            triggerRange        = 1000,
            actorX              = 96830,
            actorZ              = 1480,
            actorY              = -18060,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2AA
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x2AB
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A6, 1, 0x1531)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BD',
    )

    OP_6F(0x0000, 0)

    Jump('loc_2C4')

    def _loc_2BD(): pass

    label('loc_2BD')

    OP_6F(0x0000, 60)

    def _loc_2C4(): pass

    label('loc_2C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A6, 2, 0x1532)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D6',
    )

    OP_6F(0x0001, 0)

    Jump('loc_2DD')

    def _loc_2D6(): pass

    label('loc_2D6')

    OP_6F(0x0001, 60)

    def _loc_2DD(): pass

    label('loc_2DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A6, 4, 0x1534)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2EF',
    )

    OP_6F(0x0002, 0)

    Jump('loc_2F6')

    def _loc_2EF(): pass

    label('loc_2EF')

    OP_6F(0x0002, 60)

    def _loc_2F6(): pass

    label('loc_2F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A6, 6, 0x1536)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_308',
    )

    OP_6F(0x0003, 0)

    Jump('loc_30F')

    def _loc_308(): pass

    label('loc_308')

    OP_6F(0x0003, 60)

    def _loc_30F(): pass

    label('loc_30F')

    OP_22(0x01CD, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x315
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0xB8, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A6, 1, 0x1531)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F2',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_389',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1531)

    Jump('loc_3EF')

    def _loc_389(): pass

    label('loc_389')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)

    def _loc_3EF(): pass

    label('loc_3EF')

    Jump('loc_423')

    def _loc_3F2(): pass

    label('loc_3F2')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_423(): pass

    label('loc_423')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x431
@scena.Code('func_03_431')
def func_03_431():
    UnlockAchievement(0x02, 0xB9, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A6, 2, 0x1532)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_50E',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['百合项链'], 1)"),
            Expr.Return,
        ),
        'loc_4A5',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1532)

    Jump('loc_50B')

    def _loc_4A5(): pass

    label('loc_4A5')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_50B(): pass

    label('loc_50B')

    Jump('loc_53F')

    def _loc_50E(): pass

    label('loc_50E')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_53F(): pass

    label('loc_53F')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x54D
@scena.Code('func_04_54D')
def func_04_54D():
    UnlockAchievement(0x02, 0xBA, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A6, 4, 0x1534)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_62A',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['长桶'], 1)"),
            Expr.Return,
        ),
        'loc_5C1',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['长桶']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1534)

    Jump('loc_627')

    def _loc_5C1(): pass

    label('loc_5C1')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['长桶']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['长桶']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)

    def _loc_627(): pass

    label('loc_627')

    Jump('loc_65B')

    def _loc_62A(): pass

    label('loc_62A')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_65B(): pass

    label('loc_65B')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x669
@scena.Code('func_05_669')
def func_05_669():
    UnlockAchievement(0x02, 0xBB, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A6, 6, 0x1536)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_746',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0003, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_6DD',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1536)

    Jump('loc_743')

    def _loc_6DD(): pass

    label('loc_6DD')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0x00000000)

    def _loc_743(): pass

    label('loc_743')

    Jump('loc_777')

    def _loc_746(): pass

    label('loc_746')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_777(): pass

    label('loc_777')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
