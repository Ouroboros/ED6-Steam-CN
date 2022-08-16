import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5810_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5810   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5810.x'
    header.mapIndex       = 1
    header.bgm            = 62
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
        ('ED6_DT26/CH20425._CH', 'ED6_DT26/CH20425P._CP'),
        ('ED6_DT26/CH20425._CH', 'ED6_DT26/CH20425P._CP'),
        ('ED6_DT26/CH20425._CH', 'ED6_DT26/CH20425P._CP'),
        ('ED6_DT26/CH20425._CH', 'ED6_DT26/CH20425P._CP'),
        ('ED6_DT26/CH20425._CH', 'ED6_DT26/CH20425P._CP'),
        ('ED6_DT26/CH20425._CH', 'ED6_DT26/CH20425P._CP'),
        ('ED6_DT26/CH20425._CH', 'ED6_DT26/CH20425P._CP'),
        ('ED6_DT26/CH20425._CH', 'ED6_DT26/CH20425P._CP'),
        ('ED6_DT07/CH02110._CH', 'ED6_DT07/CH02110P._CP'),
        ('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '福音',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65536,
            chipIndex           = 0,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '多伦',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '吉尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x15A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
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
            triggerX            = -2800,
            triggerZ            = 500,
            triggerY            = -67080,
            triggerRange        = 1500,
            actorX              = -2810,
            actorZ              = 1500,
            actorY              = -67700,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -2800,
            triggerZ            = 500,
            triggerY            = -67080,
            triggerRange        = 1500,
            actorX              = -2810,
            actorZ              = 1500,
            actorY              = -67700,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -5970,
            triggerZ            = 0,
            triggerY            = 11030,
            triggerRange        = 1500,
            actorX              = -5970,
            actorZ              = 1000,
            actorY              = 11030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 67040,
            triggerZ            = 0,
            triggerY            = 9980,
            triggerRange        = 1500,
            actorX              = 67040,
            actorZ              = 1000,
            actorY              = 9980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 120000,
            triggerZ            = 0,
            triggerY            = -1980,
            triggerRange        = 1500,
            actorX              = 120000,
            actorZ              = 1000,
            actorY              = -1980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 8600,
            triggerZ            = 0,
            triggerY            = 4940,
            triggerRange        = 1000,
            actorX              = 9260,
            actorZ              = 0,
            actorY              = 4980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 8620,
            triggerZ            = 0,
            triggerY            = 1030,
            triggerRange        = 1000,
            actorX              = 9240,
            actorZ              = 0,
            actorY              = 980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 54100,
            triggerZ            = 0,
            triggerY            = 9100,
            triggerRange        = 1000,
            actorX              = 54100,
            actorZ              = 0,
            actorY              = 9710,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 120470,
            triggerZ            = 0,
            triggerY            = 2140,
            triggerRange        = 1000,
            actorX              = 119850,
            actorZ              = 0,
            actorY              = 2140,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -18540,
            triggerZ            = 0,
            triggerY            = -75000,
            triggerRange        = 1000,
            actorX              = -19160,
            actorZ              = 0,
            actorY              = -75000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -11080,
            triggerZ            = 0,
            triggerY            = -69510,
            triggerRange        = 1000,
            actorX              = -11080,
            actorZ              = 0,
            actorY              = -68940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -18390,
            triggerZ            = 0,
            triggerY            = -85010,
            triggerRange        = 1500,
            actorX              = -18390,
            actorZ              = 1000,
            actorY              = -85010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x30A
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x30B
@scena.Code('func_01_30B')
def func_01_30B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0461, 5, 0x230D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31D',
    )

    OP_6F(0x0000, 0)

    Jump('loc_324')

    def _loc_31D(): pass

    label('loc_31D')

    OP_6F(0x0000, 60)

    def _loc_324(): pass

    label('loc_324')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0461, 6, 0x230E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_336',
    )

    OP_6F(0x0001, 0)

    Jump('loc_33D')

    def _loc_336(): pass

    label('loc_336')

    OP_6F(0x0001, 60)

    def _loc_33D(): pass

    label('loc_33D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0461, 7, 0x230F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_34F',
    )

    OP_6F(0x0002, 0)

    Jump('loc_356')

    def _loc_34F(): pass

    label('loc_34F')

    OP_6F(0x0002, 60)

    def _loc_356(): pass

    label('loc_356')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0462, 0, 0x2310)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_368',
    )

    OP_6F(0x0003, 0)

    Jump('loc_36F')

    def _loc_368(): pass

    label('loc_368')

    OP_6F(0x0003, 60)

    def _loc_36F(): pass

    label('loc_36F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0462, 1, 0x2311)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_381',
    )

    OP_6F(0x0004, 0)

    Jump('loc_388')

    def _loc_381(): pass

    label('loc_381')

    OP_6F(0x0004, 60)

    def _loc_388(): pass

    label('loc_388')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0462, 2, 0x2312)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_39A',
    )

    OP_6F(0x0005, 0)

    Jump('loc_3A1')

    def _loc_39A(): pass

    label('loc_39A')

    OP_6F(0x0005, 60)

    def _loc_3A1(): pass

    label('loc_3A1')

    OP_64(0x07, 0x0001)
    OP_71(0x0002, 0x0000)
    OP_71(0x0002, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 3, 0x221B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3BE',
    )

    OP_64(0x01, 0x0001)

    Jump('loc_3C2')

    def _loc_3BE(): pass

    label('loc_3BE')

    OP_64(0x00, 0x0001)

    def _loc_3C2(): pass

    label('loc_3C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_3D3',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_10_43FE)

    Jump('loc_3E1')

    def _loc_3D3(): pass

    label('loc_3D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_3E1',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    Event(0, func_11_5E37)

    def _loc_3E1(): pass

    label('loc_3E1')

    Return()

# id: 0x0002 offset: 0x3E2
@scena.Code('func_02_3E2')
def func_02_3E2():
    UnlockAchievement(0x02, 0x01B4, 0x00)
    UnlockAchievement(0x02, 0x020C, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0461, 5, 0x230D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C4',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_45B',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0461, 5, 0x230D))

    Jump('loc_4C1')

    def _loc_45B(): pass

    label('loc_45B')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
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

    def _loc_4C1(): pass

    label('loc_4C1')

    Jump('loc_4F5')

    def _loc_4C4(): pass

    label('loc_4C4')

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
    def _loc_4F5(): pass

    label('loc_4F5')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x503
@scena.Code('func_03_503')
def func_03_503():
    UnlockAchievement(0x02, 0x01B5, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0461, 6, 0x230E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5BB',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 30)
    OP_73(0x0001)
    OP_6F(0x0001, 30)
    AddSepith(0x01, 100)
    AddSepith(0x03, 100)
    AddSepith(0x05, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x0461, 6, 0x230E))

    Jump('loc_5D5')

    def _loc_5BB(): pass

    label('loc_5BB')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_5D5(): pass

    label('loc_5D5')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x5E7
@scena.Code('func_04_5E7')
def func_04_5E7():
    UnlockAchievement(0x02, 0x01B6, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0461, 7, 0x230F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6BC',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 30)
    OP_73(0x0002)
    OP_6F(0x0002, 30)
    AddSepith(0x00, 100)
    AddSepith(0x02, 100)
    AddSepith(0x04, 100)
    AddSepith(0x06, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x0461, 7, 0x230F))

    Jump('loc_6D6')

    def _loc_6BC(): pass

    label('loc_6BC')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_6D6(): pass

    label('loc_6D6')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x6E8
@scena.Code('func_05_6E8')
def func_05_6E8():
    UnlockAchievement(0x02, 0x01B7, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0462, 0, 0x2310)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7C5',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['全回复药'], 1)"),
            Expr.Return,
        ),
        'loc_75C',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0462, 0, 0x2310))

    Jump('loc_7C2')

    def _loc_75C(): pass

    label('loc_75C')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_7C2(): pass

    label('loc_7C2')

    Jump('loc_7F6')

    def _loc_7C5(): pass

    label('loc_7C5')

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
    def _loc_7F6(): pass

    label('loc_7F6')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x804
@scena.Code('func_06_804')
def func_06_804():
    UnlockAchievement(0x02, 0x01B8, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0462, 1, 0x2311)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8E1',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['金耀珠'], 1)"),
            Expr.Return,
        ),
        'loc_878',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['金耀珠']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0462, 1, 0x2311))

    Jump('loc_8DE')

    def _loc_878(): pass

    label('loc_878')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['金耀珠']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['金耀珠']),
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

    def _loc_8DE(): pass

    label('loc_8DE')

    Jump('loc_912')

    def _loc_8E1(): pass

    label('loc_8E1')

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
    def _loc_912(): pass

    label('loc_912')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x920
@scena.Code('func_07_920')
def func_07_920():
    UnlockAchievement(0x02, 0x01B9, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0462, 2, 0x2312)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9FD',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['Ｓ－药片'], 1)"),
            Expr.Return,
        ),
        'loc_994',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0462, 2, 0x2312))

    Jump('loc_9FA')

    def _loc_994(): pass

    label('loc_994')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
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

    def _loc_9FA(): pass

    label('loc_9FA')

    Jump('loc_A2E')

    def _loc_9FD(): pass

    label('loc_9FD')

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
    def _loc_A2E(): pass

    label('loc_A2E')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xA3C
@scena.Code('func_08_A3C')
def func_08_A3C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A5F',
    )

    Call(0, 0x000A)
    Call(0, 0x000B)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_A5F(): pass

    label('loc_A5F')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S第３５克雷德尔·市政厅窗口\n',
            '\n',
            '※除了登记在册的利贝尔·方舟市民之外，\n',
            '  无法利用各项服务。\n',
            '\n',
            '※现在，由于和『中枢塔』之间的通讯\n',
            '  发生异常，因此可以利用的服务种类\n',
            '  受到了一定的限制。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_B3A(): pass

    label('loc_B3A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2957',
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CC(0x00, 0x00, 0x0028, 0x005A, 0x01)
    OP_CC(0x01, 0x00, '【使用数据库】')
    OP_CC(0x01, 0x00, '【福音的再发行申请】')
    OP_CC(0x01, 0x00, '【放弃使用】')
    OP_CC(0x02, 0x00)
    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_BB3'),
        (0x00000001, 'loc_10E3'),
        (-1, 'loc_2935'),
    )

    def _loc_BB3(): pass

    label('loc_BB3')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10D3',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S现在可以参阅的项目受到了一定的限制。\n',
            '丂\n',
            '请选择项目。',
            TxtCtl.Enter,
        ),
    )

    OP_CC(0x00, 0x01, 0x0028, 0x00BE, 0x01)
    OP_CC(0x01, 0x01, '【光环轨道】')
    OP_CC(0x02, 0x01)
    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_C3A'),
        (-1, 'loc_10C3'),
    )

    def _loc_C3A(): pass

    label('loc_C3A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10B3',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CC(0x00, 0x02, 0x0028, 0x00FA, 0x01)
    OP_CC(0x01, 0x02, '【关于光环轨道】')
    OP_CC(0x01, 0x02, '【关于各站的终端】')
    OP_CC(0x01, 0x02, '【关于紧急运行模式】')
    OP_CC(0x02, 0x02)
    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_CBF'),
        (0x00000001, 'loc_E4B'),
        (0x00000002, 'loc_F7B'),
        (-1, 'loc_10A3'),
    )

    def _loc_CBF(): pass

    label('loc_CBF')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『光环轨道』是一种独一无二，\n',
            '本都市特有的跨时代移动手段。\n',
            '\n',
            '#1S在本都市建立起的空间干涉技术，\n',
            '让借由特殊力场对空间展开轨道成为了可能，\n',
            '传统的实体轨道因此走向废除的命运。\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S这种特殊力场最大的特点，\n',
            '就是它的发生场所完全不受限制。\n',
            '也就是说，它可以让散布在都市各处\n',
            '的无数车站灵活地直接连结在一起。\n',
            '\n',
            '#1S『光环轨道』保障了市民们\n',
            '便利而舒适的都市生活。\n',
            '当您有事要到其它地区时请多利用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10B0')

    def _loc_E4B(): pass

    label('loc_E4B')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S各地区『光环轨道』的终端\n',
            '#1S除发售车票之外，\n',
            '还受理其它各项服务。\n',
            '\n',
            '#1S在其中的【网络商店】里，\n',
            '市民可以进行日用品的采购，\n',
            '同时也贩卖各种票券等等，\n',
            '欢迎多加利用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S此外，当『光环轨道』\n',
            '由于各种原因而无法使用时，\n',
            '可以利用车站终端来启动\n',
            '紧急运行模式，或是解除\n',
            '通往车站周边的地下通路锁定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10B0')

    def _loc_F7B(): pass

    label('loc_F7B')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S紧急运行模式正如其名，\n',
            '是指紧急时的启动的模式。\n',
            '\n',
            '#1S当某些原因导致来自『中枢塔』\n',
            '的能量供给陷入困难的情况下时，\n',
            '可借由启动这个模式\n',
            '来切换到备用能量。\n',
            '如此一来便可让『光环轨道』\n',
            '暂时能够运行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S此外，由于该模式\n',
            '是由各车站所个别控制，\n',
            '因此无法移动至尚未启动\n',
            '紧急运行模式的车站。\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10B0')

    def _loc_10A3(): pass

    label('loc_10A3')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_10B0')

    def _loc_10B0(): pass

    label('loc_10B0')

    Jump('loc_C3A')

    def _loc_10B3(): pass

    label('loc_10B3')

    OP_5F(0x0002)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_10D0')

    def _loc_10C3(): pass

    label('loc_10C3')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_10D0')

    def _loc_10D0(): pass

    label('loc_10D0')

    Jump('loc_BB3')

    def _loc_10D3(): pass

    label('loc_10D3')

    OP_5F(0x0001)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2954')

    def _loc_10E3(): pass

    label('loc_10E3')

    SetScenaFlags(ScenaFlag(0x045A, 1, 0x22D1))

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S现在由于和『中枢塔』之间\n',
            '的通讯发生异常，因此\n',
            '再发行的福音纯属临时性质。\n',
            '\n',
            '为了与本终端的数据库进行核对，\n',
            '请输入申请者本人的姓名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_5F(0x0000)
    OP_57(0x003C, 0x00AA, 0x0009, '#2C输入谁的姓名呢？')

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CC(0x00, 0x01, 0x0055, 0x0104, 0x00)
    OP_CC(0x01, 0x01, '【艾丝蒂尔】')
    OP_CC(0x01, 0x01, '【约修亚】')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_120F'),
        (0x00000003, 'loc_1222'),
        (0x00000004, 'loc_1235'),
        (0x00000005, 'loc_1246'),
        (0x00000006, 'loc_1257'),
        (0x00000007, 'loc_1266'),
        (0x00000008, 'loc_1273'),
        (0x0000000A, 'loc_1282'),
        (-1, 'loc_1293'),
    )

    def _loc_120F(): pass

    label('loc_120F')

    OP_CC(0x01, 0x01, '【雪拉扎德】')

    Jump('loc_1293')

    def _loc_1222(): pass

    label('loc_1222')

    OP_CC(0x01, 0x01, '【奥利维尔】')

    Jump('loc_1293')

    def _loc_1235(): pass

    label('loc_1235')

    OP_CC(0x01, 0x01, '【科洛丝】')

    Jump('loc_1293')

    def _loc_1246(): pass

    label('loc_1246')

    OP_CC(0x01, 0x01, '【阿加特】')

    Jump('loc_1293')

    def _loc_1257(): pass

    label('loc_1257')

    OP_CC(0x01, 0x01, '【提妲】')

    Jump('loc_1293')

    def _loc_1266(): pass

    label('loc_1266')

    OP_CC(0x01, 0x01, '【金】')

    Jump('loc_1293')

    def _loc_1273(): pass

    label('loc_1273')

    OP_CC(0x01, 0x01, '【凯文】')

    Jump('loc_1293')

    def _loc_1282(): pass

    label('loc_1282')

    OP_CC(0x01, 0x01, '【乔丝特】')

    Jump('loc_1293')

    def _loc_1293(): pass

    label('loc_1293')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_12BC'),
        (0x00000003, 'loc_12CF'),
        (0x00000004, 'loc_12E2'),
        (0x00000005, 'loc_12F3'),
        (0x00000006, 'loc_1304'),
        (0x00000007, 'loc_1313'),
        (0x00000008, 'loc_1320'),
        (0x0000000A, 'loc_132F'),
        (-1, 'loc_1340'),
    )

    def _loc_12BC(): pass

    label('loc_12BC')

    OP_CC(0x01, 0x01, '【雪拉扎德】')

    Jump('loc_1340')

    def _loc_12CF(): pass

    label('loc_12CF')

    OP_CC(0x01, 0x01, '【奥利维尔】')

    Jump('loc_1340')

    def _loc_12E2(): pass

    label('loc_12E2')

    OP_CC(0x01, 0x01, '【科洛丝】')

    Jump('loc_1340')

    def _loc_12F3(): pass

    label('loc_12F3')

    OP_CC(0x01, 0x01, '【阿加特】')

    Jump('loc_1340')

    def _loc_1304(): pass

    label('loc_1304')

    OP_CC(0x01, 0x01, '【提妲】')

    Jump('loc_1340')

    def _loc_1313(): pass

    label('loc_1313')

    OP_CC(0x01, 0x01, '【金】')

    Jump('loc_1340')

    def _loc_1320(): pass

    label('loc_1320')

    OP_CC(0x01, 0x01, '【凯文】')

    Jump('loc_1340')

    def _loc_132F(): pass

    label('loc_132F')

    OP_CC(0x01, 0x01, '【乔丝特】')

    Jump('loc_1340')

    def _loc_1340(): pass

    label('loc_1340')

    OP_CC(0x02, 0x01)
    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_135F'),
        (0x00000001, 'loc_136C'),
        (0x00000002, 'loc_1379'),
        (0x00000003, 'loc_139D'),
        (-1, 'loc_13C1'),
    )

    def _loc_135F(): pass

    label('loc_135F')

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_13C1')

    def _loc_136C(): pass

    label('loc_136C')

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_13C1')

    def _loc_1379(): pass

    label('loc_1379')

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_139A',
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_139A(): pass

    label('loc_139A')

    Jump('loc_13C1')

    def _loc_139D(): pass

    label('loc_139D')

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13BE',
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_13BE(): pass

    label('loc_13BE')

    Jump('loc_13C1')

    def _loc_13C1(): pass

    label('loc_13C1')

    OP_5F(0x0001)
    OP_5F(0x0002)
    OP_57(0x0028, 0x00AA, 0x000B, '#2C请输入姓名。')

    Menu(
        1,
        70,
        260,
        0,
        (
            TXT(0x00, '【乌路里希】\n'),
            TXT(0x01, '【盖鲁格】\n'),
            TXT(0x02, '【亚奥伊斯】\n'),
            TXT(0x03, '【赛雷斯托】\n'),
            TXT(0x04, '【爱德路霍富】\n'),
        ),
    )

    MenuEnd(0x0000)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1442',
    )

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1442(): pass

    label('loc_1442')

    OP_5F(0x0001)

    Menu(
        1,
        110,
        260,
        0,
        (
            TXT(0x00, '【Ａ】\n'),
            TXT(0x01, '【Ｂ】\n'),
            TXT(0x02, '【Ｃ】\n'),
            TXT(0x03, '【Ｄ】\n'),
            TXT(0x04, '【Ｅ】\n'),
        ),
    )

    MenuEnd(0x0000)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_148B',
    )

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_148B(): pass

    label('loc_148B')

    OP_5F(0x0001)

    Menu(
        1,
        65,
        260,
        0,
        (
            TXT(0x00, '【阿斯特雷】\n'),
            TXT(0x01, '【怀斯曼】\n'),
            TXT(0x02, '【爱普斯泰恩】\n'),
            TXT(0x03, '【奥赛雷丝】\n'),
            TXT(0x04, '【莱恩福尔特】\n'),
        ),
    )

    MenuEnd(0x0000)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14F4',
    )

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_14F4(): pass

    label('loc_14F4')

    OP_5F(0x0001)
    OP_DA()
    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)
    Sleep(300)

    Fade(500)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(72, 320, 56, 3)
    EventBegin(0x00)
    CameraMove(-3670, 230, -66890, 0)
    OP_67(0, 5740, -10000, 0)
    CameraSetDistance(3400, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Switch(
        (
            (Expr.PushReg, 0x4),
            Expr.Return,
        ),
        (0x00000000, 'loc_157D'),
        (0x00000001, 'loc_15C4'),
        (0x00000002, 'loc_160B'),
        (0x00000003, 'loc_1652'),
        (-1, 'loc_1699'),
    )

    def _loc_157D(): pass

    label('loc_157D')

    ChrSetPos(0x0101, -2790, 500, -68180, 0)
    ChrSetPos(0x0102, -2680, 220, -69410, 0)
    ChrSetPos(0x00F8, -1230, 0, -69950, 315)
    ChrSetPos(0x00F9, -3450, 220, -69930, 0)

    Jump('loc_1699')

    def _loc_15C4(): pass

    label('loc_15C4')

    ChrSetPos(0x0102, -2790, 500, -68180, 0)
    ChrSetPos(0x0101, -2680, 220, -69410, 0)
    ChrSetPos(0x00F8, -1230, 0, -69950, 315)
    ChrSetPos(0x00F9, -3450, 220, -69930, 0)

    Jump('loc_1699')

    def _loc_160B(): pass

    label('loc_160B')

    ChrSetPos(0x00F8, -2790, 500, -68180, 0)
    ChrSetPos(0x0101, -2680, 220, -69410, 0)
    ChrSetPos(0x0102, -1230, 0, -69950, 315)
    ChrSetPos(0x00F9, -3450, 220, -69930, 0)

    Jump('loc_1699')

    def _loc_1652(): pass

    label('loc_1652')

    ChrSetPos(0x00F9, -2790, 500, -68180, 0)
    ChrSetPos(0x0101, -2680, 220, -69410, 0)
    ChrSetPos(0x0102, -1230, 0, -69950, 315)
    ChrSetPos(0x00F8, -3450, 220, -69930, 0)

    Jump('loc_1699')

    def _loc_1699(): pass

    label('loc_1699')

    OP_0D()
    Sleep(200)

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1CF0',
    )

    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '姓名………………………赛雷斯托·Ｄ·奥赛雷丝\n',
            '基因验证…………………７３％吻合',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '暂时认定\n',
            '申请者为\n',
            '【赛雷斯托·Ｄ·奥赛雷丝】',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '现在进行『福音』的再发行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    LoadEffect(0x00, 'map\\\\mp027_01.eff')
    PlayEffect(0x00, 0x00, 0x0008, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetPos(0x0008, -2810, 2500, -67130, 0)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0008, 0x0080)
    PlaySE(153, 0x00, 0x64)

    @scena.Lambda('lambda_17DE')
    def lambda_17DE():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_17DE)

    ChrMoveToRelativeAsync(0x0008, 0, -1000, 0, 1000, 0x00)
    WaitForThreadExit(0x0008, 0x0001)
    StopEffect(0x00, 0x02)
    Sleep(500)

    ChrTalk(
        0x0105,
        (
            '#0060391356V#1164F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340743V#1004F哇哇……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391358V#1042F是空间转换吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 500)
    ChrSetFlags(0x0008, 0x0080)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['原福音']),
            (TxtCtl.SetColor, 0x0),
            '收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['原福音'], 1)
    ChrSetDirection(0x0105, 180, 400)

    ChrTalk(
        0x0105,
        (
            '#0060391359V#1160F#2P……好像是远古时代\n',
            '曾经使用过的真正『福音』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391360V#1002F嗯……感觉和『结社』\n',
            '制造的复制品很相似。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391361V#1040F果然，在四轮之塔终端的\n',
            '那位『赛雷斯托·Ｄ·奥赛雷丝』\n',
            '似乎就是科洛丝的祖先呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060391362V#1160F#2P是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060391363V#1167F或许就是让市民们\n',
            '从这座都市里逃出的负责人吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060391364V#1382F至于基因验证和我相似，\n',
            '我想大概是偶然凑巧吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B1E',
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇在车站终端查阅『福音』的信息】\n'),
            TXT(0x01, '【◇不在车站的终端查阅『福音』的信息】\n'),
            TXT(0x02, '【◇什么也没有变更】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1B12'),
        (0x00000001, 'loc_1B18'),
        (-1, 'loc_1B1E'),
    )

    def _loc_1B12(): pass

    label('loc_1B12')

    SetScenaFlags(ScenaFlag(0x0443, 2, 0x221A))

    Jump('loc_1B1E')

    def _loc_1B18(): pass

    label('loc_1B18')

    ClearScenaFlags(ScenaFlag(0x0443, 2, 0x221A))

    Jump('loc_1B1E')

    def _loc_1B1E(): pass

    label('loc_1B1E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 2, 0x221A)),
            Expr.Return,
        ),
        'loc_1C08',
    )

    ChrTalk(
        0x0101,
        (
            '#0010391365V#1001F嘿嘿，也许不是偶然，\n',
            '而是女神的指引呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391366V#1006F总之，在车站的终端使用这个，\n',
            '似乎就可以打开通往地下的大门了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391367V我们马上去试试吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060391368V#1161F#2P嗯，说得也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CD2')

    def _loc_1C08(): pass

    label('loc_1C08')

    ChrTalk(
        0x0101,
        (
            '#0010391365V#1001F嘿嘿，也许不是偶然，\n',
            '而是女神的指引呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391370V#1006F总之，带着它\n',
            '说不定会有什么帮助……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391371V就心怀感激地收下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060391372V#1168F#2P呵呵，说得也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CD2(): pass

    label('loc_1CD2')

    SetScenaFlags(ScenaFlag(0x0443, 3, 0x221B))
    OP_64(0x00, 0x0001)
    OP_65(0x01, 0x0001)
    OP_28(0x009D, 0x01, 0x0800)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2954')

    def _loc_1CF0(): pass

    label('loc_1CF0')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x3),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_21CA',
    )

    TalkSetChrName('合成音')
    SetMessageWindowPos(-1, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '姓名………………………无此者\n',
            '基因验证…………………无此者\n',
            '请输入正确的姓名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2101',
    )

    ChrTalk(
        0x0101,
        (
            '#0010391348V#1004F怎、怎么了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391349V#1035F看来会将当时的市民姓名\n',
            '与基因验证彼此进行相互核对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391375V#1040F但是，基因验证吻合\n',
            '也就是说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0105, 180, 400)

    ChrTalk(
        0x0105,
        (
            '#0060391376V#1167F#2P是的，或许是我的基因验证\n',
            '与哪位祖先相似也说不定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060391377V#1162F接下来只要知道姓名的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391378V#1002F科洛丝的祖先姓名吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391379V#1015F（咦……？\n',
            '好像有点印象……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045A, 2, 0x22D2)),
            Expr.Return,
        ),
        'loc_1FAA',
    )

    ChrTalk(
        0x0102,
        (
            '#0020391352V#1040F无论如何，正像博士所说的，\n',
            '看来我们需要了解一下过去的事情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391353V我们暂时先返回埃尔赛尤号，\n',
            '看看『卡佩尔』从数据水晶解读出来的信息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_202E')

    def _loc_1FAA(): pass

    label('loc_1FAA')

    ChrTalk(
        0x0102,
        (
            '#0020391354V#1040F不管怎么说，\n',
            '这似乎是个相当精密的系统。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391355V还是暂时先返回埃尔赛尤号，\n',
            '与拉赛尔博士商量一下比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_202E(): pass

    label('loc_202E')

    ChrSetDirection(0x0105, 0, 400)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetMessageWindowPos(330, 68, 34, 12)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S第３５克雷德尔·市政厅窗口\n',
            '\n',
            '※除了登记在册的利贝尔·方舟市民之外，\n',
            '  无法利用各种服务。\n',
            '\n',
            '※现在，由于和『中枢塔』之间的通讯\n',
            '  发生异常，因此可以利用的服务种类\n',
            '  受到了一定的限制。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2954')

    def _loc_2101(): pass

    label('loc_2101')

    SetMessageWindowPos(330, 68, 34, 12)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S第３５克雷德尔·市政厅窗口\n',
            '\n',
            '※除了登记在册的利贝尔·方舟市民之外，\n',
            '  无法利用各种服务。\n',
            '\n',
            '※现在，由于和『中枢塔』之间的通讯\n',
            '  发生异常，因此可以利用的服务种类\n',
            '  受到了一定的限制。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2932')

    def _loc_21CA(): pass

    label('loc_21CA')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2665',
    )

    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '姓名………………………赛雷斯托·Ｄ·奥赛雷丝\n',
            '基因验证…………………不一致',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '中断再发行手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_259C',
    )

    Switch(
        (
            (Expr.PushReg, 0x4),
            Expr.Return,
        ),
        (0x00000000, 'loc_2274'),
        (0x00000001, 'loc_2277'),
        (0x00000002, 'loc_227A'),
        (0x00000003, 'loc_227D'),
        (-1, 'loc_2280'),
    )

    def _loc_2274(): pass

    label('loc_2274')

    Jump('loc_2280')

    def _loc_2277(): pass

    label('loc_2277')

    Jump('loc_2280')

    def _loc_227A(): pass

    label('loc_227A')

    Jump('loc_2280')

    def _loc_227D(): pass

    label('loc_227D')

    Jump('loc_2280')

    def _loc_2280(): pass

    label('loc_2280')

    ChrTalk(
        0x0101,
        (
            '#0010391348V#1004F怎、怎么了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391349V#1035F看来会将当时的市民姓名\n',
            '与基因验证彼此进行相互核对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391386V#1043F虽然有符合的姓名，\n',
            '但基因验证不吻合……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391387V#1007F嗯……\n',
            '看来真的一点办法也没有了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391388V#1015F（咦……？\n',
            '不过说到奥赛雷丝……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045A, 2, 0x22D2)),
            Expr.Return,
        ),
        'loc_244C',
    )

    ChrTalk(
        0x0102,
        (
            '#0020391352V#1040F无论如何，正像博士所说的，\n',
            '看来我们需要了解一下过去的事情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391353V我们暂时先返回埃尔赛尤号，\n',
            '看看『卡佩尔』从数据水晶解读出来的信息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24D0')

    def _loc_244C(): pass

    label('loc_244C')

    ChrTalk(
        0x0102,
        (
            '#0020391354V#1040F不管怎么说，\n',
            '这似乎是个相当精密的系统。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391355V还是暂时先返回埃尔赛尤号，\n',
            '与拉赛尔博士商量一下比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24D0(): pass

    label('loc_24D0')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetMessageWindowPos(330, 68, 34, 12)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S第３５克雷德尔·市政厅窗口\n',
            '\n',
            '※除了登记在册的利贝尔·方舟市民之外，\n',
            '  无法利用各种服务。\n',
            '\n',
            '※现在，由于和『中枢塔』之间的通讯\n',
            '  发生异常，因此可以利用的服务种类\n',
            '  受到了一定的限制。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2954')

    def _loc_259C(): pass

    label('loc_259C')

    SetMessageWindowPos(330, 68, 34, 12)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S第３５克雷德尔·市政厅窗口\n',
            '\n',
            '※除了登记在册的利贝尔·方舟市民之外，\n',
            '  无法利用各种服务。\n',
            '\n',
            '※现在，由于和『中枢塔』之间的通讯\n',
            '  发生异常，因此可以利用的服务种类\n',
            '  受到了一定的限制。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2932')

    def _loc_2665(): pass

    label('loc_2665')

    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '姓名………………………无此者\n',
            '基因验证…………………无此者',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '中断再发行手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2922',
    )

    Switch(
        (
            (Expr.PushReg, 0x4),
            Expr.Return,
        ),
        (0x00000000, 'loc_26E7'),
        (0x00000001, 'loc_26EA'),
        (0x00000002, 'loc_26ED'),
        (0x00000003, 'loc_26F0'),
        (-1, 'loc_26F3'),
    )

    def _loc_26E7(): pass

    label('loc_26E7')

    Jump('loc_26F3')

    def _loc_26EA(): pass

    label('loc_26EA')

    Jump('loc_26F3')

    def _loc_26ED(): pass

    label('loc_26ED')

    Jump('loc_26F3')

    def _loc_26F0(): pass

    label('loc_26F0')

    Jump('loc_26F3')

    def _loc_26F3(): pass

    label('loc_26F3')

    ChrTalk(
        0x0101,
        (
            '#0010391348V#1004F怎、怎么了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391349V#1035F看来会将当时的市民姓名\n',
            '与基因验证彼此进行相互核对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391350V#1042F如果二者不能吻合，\n',
            '就无法继续办理手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391351V#1019F嗯……\n',
            '老实说，有束手无策的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045A, 2, 0x22D2)),
            Expr.Return,
        ),
        'loc_288A',
    )

    ChrTalk(
        0x0102,
        (
            '#0020391352V#1040F无论如何，正像博士所说的，\n',
            '看来我们需要了解一下过去的事情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391353V我们暂时先返回埃尔赛尤号，\n',
            '看看『卡佩尔』从数据水晶解读出来的信息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_290C')

    def _loc_288A(): pass

    label('loc_288A')

    ChrTalk(
        0x0102,
        (
            '#0020391354V#1040F不管怎么说\n',
            '这似乎是个相当精密的系统。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391355V还是暂时先返回埃尔赛尤号，\n',
            '与拉赛尔博士商量一下比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_290C(): pass

    label('loc_290C')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    SetMessageWindowPos(330, 68, 34, 12)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2954')

    def _loc_2922(): pass

    label('loc_2922')

    SetMessageWindowPos(330, 68, 34, 12)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            TxtCtl.Enter,
        ),
    )

    def _loc_2932(): pass

    label('loc_2932')

    Jump('loc_2954')

    def _loc_2935(): pass

    label('loc_2935')

    FadeIn(300, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2954')

    def _loc_2954(): pass

    label('loc_2954')

    Jump('loc_B3A')

    def _loc_2957(): pass

    label('loc_2957')

    FadeIn(300, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2985',
    )

    EventEnd(0x00)

    def _loc_2985(): pass

    label('loc_2985')

    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0x298C
@scena.Code('func_09_298C')
def func_09_298C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_29AF',
    )

    Call(0, 0x000A)
    Call(0, 0x000B)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_29AF(): pass

    label('loc_29AF')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S第３５克雷德尔·市政厅窗口\n',
            '\n',
            '※除了登记在册的利贝尔·方舟市民之外，\n',
            '  无法利用各种服务。\n',
            '\n',
            '※现在，由于和『中枢塔』之间的通讯\n',
            '  发生异常，因此可以利用的服务种类\n',
            '  受到了一定的限制。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2A88(): pass

    label('loc_2A88')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3032',
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CC(0x00, 0x00, 0x0028, 0x0064, 0x01)
    OP_CC(0x01, 0x00, '【使用数据库】')
    OP_CC(0x01, 0x00, '【放弃使用】')
    OP_CC(0x02, 0x00)
    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2ADF'),
        (0x00000000, 'loc_2ADF'),
        (-1, 'loc_3010'),
    )

    def _loc_2ADF(): pass

    label('loc_2ADF')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3000',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S现在可以参阅的项目受到了一定的限制。\n',
            '丂\n',
            '请选择项目。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_CC(0x00, 0x01, 0x0028, 0x00B4, 0x01)
    OP_CC(0x01, 0x01, '【光环轨道】')
    OP_CC(0x02, 0x01)
    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2B67'),
        (-1, 'loc_2FF0'),
    )

    def _loc_2B67(): pass

    label('loc_2B67')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2FE0',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CC(0x00, 0x02, 0x0028, 0x00F0, 0x01)
    OP_CC(0x01, 0x02, '【关于光环轨道】')
    OP_CC(0x01, 0x02, '【关于各站的终端】')
    OP_CC(0x01, 0x02, '【关于紧急运行模式】')
    OP_CC(0x02, 0x02)
    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2BEC'),
        (0x00000001, 'loc_2D78'),
        (0x00000002, 'loc_2EA8'),
        (-1, 'loc_2FD0'),
    )

    def _loc_2BEC(): pass

    label('loc_2BEC')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『光环轨道』是一种独一无二，\n',
            '本都市特有的跨时代移动手段。\n',
            '\n',
            '#1S在本都市建立起的空间干涉技术，\n',
            '让借由特殊力场对空间展开轨道成为了可能，\n',
            '传统的实体轨道因此走向废除的命运。\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S这种特殊力场最大的特点，\n',
            '就是它的发生场所完全不受限制。\n',
            '也就是说，它可以让散布在都市各处\n',
            '的无数车站灵活地直接连结在一起。\n',
            '\n',
            '#1S『光环轨道』保障了市民们\n',
            '便利而舒适的都市生活。\n',
            '当您有事要到其它地区时请多利用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FDD')

    def _loc_2D78(): pass

    label('loc_2D78')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S各地区『光环轨道』的终端\n',
            '#1S除发售车票之外，\n',
            '还受理其它各项服务。\n',
            '\n',
            '#1S在其中的【网络商店】里，\n',
            '市民可以进行日用品的采购，\n',
            '同时也贩卖各种票券等等，\n',
            '欢迎多加利用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S此外，当『光环轨道』\n',
            '由于各种原因而无法使用时，\n',
            '可以利用车站终端来启动\n',
            '紧急运行模式，或是解除\n',
            '通往车站周边的地下通路锁定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FDD')

    def _loc_2EA8(): pass

    label('loc_2EA8')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S紧急运行模式正如其名，\n',
            '是指紧急时的启动的模式。\n',
            '\n',
            '#1S当某些原因导致来自『中枢塔』\n',
            '的能量供给陷入困难的情况下时，\n',
            '可借由启动这个模式\n',
            '来切换到备用能量。\n',
            '如此一来便可让『光环轨道』\n',
            '暂时能够运行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S此外，由于该模式\n',
            '是由各车站所个别控制，\n',
            '因此无法移动至尚未启动\n',
            '紧急运行模式的车站。\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FDD')

    def _loc_2FD0(): pass

    label('loc_2FD0')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2FDD')

    def _loc_2FDD(): pass

    label('loc_2FDD')

    Jump('loc_2B67')

    def _loc_2FE0(): pass

    label('loc_2FE0')

    OP_5F(0x0002)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2FFD')

    def _loc_2FF0(): pass

    label('loc_2FF0')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2FFD')

    def _loc_2FFD(): pass

    label('loc_2FFD')

    Jump('loc_2ADF')

    def _loc_3000(): pass

    label('loc_3000')

    OP_5F(0x0001)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_302F')

    def _loc_3010(): pass

    label('loc_3010')

    FadeIn(300, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_302F')

    def _loc_302F(): pass

    label('loc_302F')

    Jump('loc_2A88')

    def _loc_3032(): pass

    label('loc_3032')

    FadeIn(300, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    TalkEnd(0x00FF)

    Return()

# id: 0x000A offset: 0x305B
@scena.Code('func_0A_305B')
def func_0A_305B():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_30D5'),
        (0x00000001, 'loc_30DB'),
        (-1, 'loc_30E1'),
    )

    def _loc_30D5(): pass

    label('loc_30D5')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_30E1')

    def _loc_30DB(): pass

    label('loc_30DB')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_30E1')

    def _loc_30E1(): pass

    label('loc_30E1')

    Return()

# id: 0x000B offset: 0x30E2
@scena.Code('func_0B_30E2')
def func_0B_30E2():
    FadeOut(0, 0, -1)
    CameraMove(-545830, 30000, 755590, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['科洛丝'],
            ChrTable['奥利维尔'],
            ChrTable['提妲'],
            ChrTable['金'],
            ChrTable['凯文神父'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

# id: 0x000C offset: 0x3175
@scena.Code('func_0C_3175')
def func_0C_3175():
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S第３５克雷德尔·居住者用终端\n',
            '　　　　　　　　　　　＃C035-556800015073\n',
            '丂\n',
            '#1SＩＤ确认中#100W……………………………#20W不符合。\n',
            '丂\n',
            '※无法确认终端所有者的ＩＤ。\n',
            '　允许阅览的项目受到了一定的限制。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3265(): pass

    label('loc_3265')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_39C1',
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CC(0x00, 0x00, 0x0028, 0x005A, 0x01)
    OP_CC(0x01, 0x00, '【确认新食谱】')
    OP_CC(0x01, 0x00, '<FIXME>【クリスタルの照合】')
    OP_CC(0x01, 0x00, '【放弃使用】')
    OP_CC(0x02, 0x00)
    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_32E5'),
        (0x00000001, 'loc_35C9'),
        (-1, 'loc_399F'),
    )

    def _loc_32E5(): pass

    label('loc_32E5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_35B9',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S===============料理＃W-6894===============\n',
            '==============大麦奶酪果冻==============',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_57(0x0032, 0x009B, 0x0009, '#2C要转录资料吗？')
    OP_CC(0x00, 0x01, 0x0028, 0x00F0, 0x00)
    OP_CC(0x01, 0x01, '【是】')
    OP_CC(0x01, 0x01, '【否】')
    OP_CC(0x02, 0x01)
    MenuEnd(0x0000)
    OP_5F(0x0001)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_33B9'),
        (0x00000001, 'loc_35A8'),
        (-1, 'loc_35A8'),
    )

    def _loc_33B9(): pass

    label('loc_33B9')

    OP_DA()

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3588',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x004B)"),
            Expr.Return,
        ),
        'loc_33FD',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S食谱数据已经开始转录。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3585')

    def _loc_33FD(): pass

    label('loc_33FD')

    OP_AC(0x004B)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S数据转录中#100W……………………#20W完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_5F(0x0001)
    FadeIn(300, 0)
    Sleep(100)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['大麦奶酪果冻']),
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0101,
        (
            '#0010391393V#1004F哇，料理手册上\n',
            '被写进了新资料！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_34F8',
    )

    ChrTalk(
        0x0107,
        (
            '#0020391394V#065F……究、究竟\n',
            '是怎么做到的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3525')

    def _loc_34F8(): pass

    label('loc_34F8')

    ChrTalk(
        0x0102,
        (
            '#0020391395V#1044F……究竟\n',
            '是什么原理？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3525(): pass

    label('loc_3525')

    ChrTalk(
        0x0101,
        (
            '#0010391396V#1015F嗯，虽然不太了解，\n',
            '不过真是了不起的技术啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3585(): pass

    label('loc_3585')

    Jump('loc_35A5')

    def _loc_3588(): pass

    label('loc_3588')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S找不到数据转录对象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_35A5(): pass

    label('loc_35A5')

    Jump('loc_35B6')

    def _loc_35A8(): pass

    label('loc_35A8')

    OP_DA()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_35B6')

    def _loc_35B6(): pass

    label('loc_35B6')

    Jump('loc_32E5')

    def _loc_35B9(): pass

    label('loc_35B9')

    OP_5F(0x0001)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_39BE')

    def _loc_35C9(): pass

    label('loc_35C9')

    If(
        (
            (Expr.Eval, "OP_40(0x0418, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x045B, 1, 0x22D9)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_38E4',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S<FIXME>照合を開始します…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S………………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S<FIXME>………特定の周波パターンを確認。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S<FIXME>登録のあった受託者と認めます。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S<FIXME>保管物＃W-8834-0034の転送を開始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S<FIXME>データ受信中…………２０％………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S……４０％……………６０％………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S……８０％……………転送完了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_5F(0x0000)
    Sleep(200)

    OP_5F(0x0000)
    Sleep(200)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '<FIXME>#1047iを手に入れた。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['塞姆里亚石'], 1)

    ChrTalk(
        0x0101,
        (
            '#0010391397V#1004F<FIXME>こ、これって\n',
            'あたしたちが持ってるのと\n',
            '同じ鉱石よね？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391398V#1015Fさっきのクリスタルと同じで\n',
            'またどこかから\n',
            '送られてきたみたいだけど……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391399V#1035F<FIXME>うん……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391400V#1040F詳しいことは判らないけど\n',
            'どうやら、このクリスタルが鍵になっていたようだね。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x045B, 1, 0x22D9))

    Jump('loc_399F')

    def _loc_38E4(): pass

    label('loc_38E4')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S<FIXME>照合を開始します………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S………………データ検知できず。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S<FIXME>クリスタルを確認して、\n',
            '再試行してください。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_399F(): pass

    label('loc_399F')

    FadeIn(300, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_39BE')

    def _loc_39BE(): pass

    label('loc_39BE')

    Jump('loc_3265')

    def _loc_39C1(): pass

    label('loc_39C1')

    FadeIn(300, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    TalkEnd(0x00FF)

    Return()

# id: 0x000D offset: 0x39EA
@scena.Code('func_0D_39EA')
def func_0D_39EA():
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S第３５克雷德尔·居住者用终端\n',
            '　　　　　　　　　　　＃C035-556800014096\n',
            '　\n',
            '#1SＩＤ确认中#100W……………………………#20W不符合。\n',
            '丂\n',
            '※无法确认终端所有者的ＩＤ。\n',
            '　允许阅览的项目受到了一定的限制。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3ADA(): pass

    label('loc_3ADA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3E26',
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CC(0x00, 0x00, 0x0028, 0x005A, 0x01)
    OP_CC(0x01, 0x00, '【留言板】')
    OP_CC(0x01, 0x00, '【放弃使用】')
    OP_CC(0x02, 0x00)
    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3B33'),
        (-1, 'loc_3E04'),
    )

    def _loc_3B33(): pass

    label('loc_3B33')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于强化都市警备的通知』\n',
            '　\n',
            '近年来，在法克特里亚等\n',
            '人烟稀少的地区里，\n',
            '犯罪数目明显增加。\n',
            '迄今为止，我们竭尽所能地\n',
            '在确保市民自由的基础上，\n',
            '不断地进行警备力量的强化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S然而，犯罪率\n',
            '依旧一路向上攀升。\n',
            '讨论后的结果是，没有市民的配合，\n',
            '就无法达成万全的警备，\n',
            '因此希望大家能够提供协助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S为此，我们衷心希望\n',
            '各位市民能够理解以下事项。\n',
            '丂\n',
            '·在使用终端时，\n',
            '　将全面进行各位的『福音』ＩＤ认证。\n',
            '·在『利贝尔·方舟』市的所有地区\n',
            '　将实施定期性的盘查活动。\n',
            '·在没有许可的情况下，\n',
            '　将限制普通住户前往『中枢塔』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S这次的警备强化\n',
            '多少干涉了市民的行动自由，\n',
            '也许会因此为您带来些许的不愉快。\n',
            '但这也是优先考虑都市与各位市民安全\n',
            '所得到的结果。\n',
            '期望各位的理解与合作。\n',
            '丂\n',
            '『利贝尔·方舟』市·警备局',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E23')

    def _loc_3E04(): pass

    label('loc_3E04')

    FadeIn(300, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3E23')

    def _loc_3E23(): pass

    label('loc_3E23')

    Jump('loc_3ADA')

    def _loc_3E26(): pass

    label('loc_3E26')

    FadeIn(300, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    TalkEnd(0x00FF)

    Return()

# id: 0x000E offset: 0x3E4F
@scena.Code('func_0E_3E4F')
def func_0E_3E4F():
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkSetChrName('合成音')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '欢迎来到克雷德尔·市政厅！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '现在为非受理时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有事请在里面的窗口\n',
            '选择直接服务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000F offset: 0x3EEA
@scena.Code('func_0F_3EEA')
def func_0F_3EEA():
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S第３５克雷德尔·居住者用终端\n',
            '　　　　　　　　　　　＃C035-556800014096\n',
            '丂\n',
            '#1SＩＤ确认中#100W……………………………#20W不符合。\n',
            '　\n',
            '※无法确认终端所有者的ＩＤ。\n',
            '　允许阅览的项目受到了一定的限制。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3FDA(): pass

    label('loc_3FDA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_43D5',
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CC(0x00, 0x00, 0x0028, 0x005A, 0x01)
    OP_CC(0x01, 0x00, '【留言板】')
    OP_CC(0x01, 0x00, '【放弃使用】')
    OP_CC(0x02, 0x00)
    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_4033'),
        (-1, 'loc_43B3'),
    )

    def _loc_4033(): pass

    label('loc_4033')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『【重要】关于强化个人播送服务和\n',
            '　　　　　更新『福音』的通知』\n',
            '丂\n',
            '『利贝尔·方舟』市，\n',
            '为了给市民们营造\n',
            '舒适而充实的都市生活，\n',
            '我们实施了以『治愈』为主题\n',
            '的各种音乐和影像的播送服务。\n',
            '此一服务除了一般的大众之外，\n',
            '也受到了因精神疾病而困扰的患者\n',
            '一致的热烈好评。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S然而，目前这类服务\n',
            '尽管有一定的可选择性，\n',
            '但总体来说是统一且单方面的，\n',
            '因此近来不断听到要求广泛对应\n',
            '每一个人兴趣爱好的声音。\n',
            '丂\n',
            '我们接受了这种意见，并且为了提供\n',
            '拥有不同嗜好的所有市民充实的服务，\n',
            '我们正在加强播送服务方面的多样性\n',
            '和独创性，同时一步步考虑要如何\n',
            '提供大家更便捷、更适合的服务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S为此，首先必须对全体市民的\n',
            '『福音』进行更新。\n',
            '基于上述理由，\n',
            '请大家前往附近的市政厅询问之后，\n',
            '同时办理更新手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S此外，本次更新以全体市民为实施对象，\n',
            '未经更新的『福音』\n',
            '在经过一段的期间之后\n',
            '将无法继续使用。\n',
            '这或许多少会给大家带来一些麻烦，\n',
            '但衷心期望您能够与我们配合。\n',
            '丂\n',
            '『利贝尔·方舟』市·系统管理局',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43D2')

    def _loc_43B3(): pass

    label('loc_43B3')

    FadeIn(300, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_43D2')

    def _loc_43D2(): pass

    label('loc_43D2')

    Jump('loc_3FDA')

    def _loc_43D5(): pass

    label('loc_43D5')

    FadeIn(300, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    TalkEnd(0x00FF)

    Return()

# id: 0x0010 offset: 0x43FE
@scena.Code('func_10_43FE')
def func_10_43FE():
    EventBegin(0x00)
    FadeOut(0, 0, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4423',
    )

    Call(0, 0x000A)
    Call(0, 0x0015)
    FormationAddMember(ChrTable['乔丝特2'], 0xFA, 0xFF)

    def _loc_4423(): pass

    label('loc_4423')

    LoadChip('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP', 10)
    LoadChip('ED6_DT27/CH03013._CH', 'ED6_DT27/CH03013P._CP', 11)
    LoadChip('ED6_DT27/CH03103._CH', 'ED6_DT27/CH03103P._CP', 12)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_4466'),
        (0x00000003, 'loc_4473'),
        (0x00000004, 'loc_4480'),
        (0x00000005, 'loc_448D'),
        (0x00000006, 'loc_449A'),
        (0x00000007, 'loc_44A7'),
        (0x00000008, 'loc_44B4'),
        (-1, 'loc_44C1'),
    )

    def _loc_4466(): pass

    label('loc_4466')

    LoadChip('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP', 13)

    Jump('loc_44C1')

    def _loc_4473(): pass

    label('loc_4473')

    LoadChip('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP', 13)

    Jump('loc_44C1')

    def _loc_4480(): pass

    label('loc_4480')

    LoadChip('ED6_DT27/CH03213._CH', 'ED6_DT27/CH03213P._CP', 13)

    Jump('loc_44C1')

    def _loc_448D(): pass

    label('loc_448D')

    LoadChip('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP', 13)

    Jump('loc_44C1')

    def _loc_449A(): pass

    label('loc_449A')

    LoadChip('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP', 13)

    Jump('loc_44C1')

    def _loc_44A7(): pass

    label('loc_44A7')

    LoadChip('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP', 13)

    Jump('loc_44C1')

    def _loc_44B4(): pass

    label('loc_44B4')

    LoadChip('ED6_DT27/CH03083._CH', 'ED6_DT27/CH03083P._CP', 13)

    Jump('loc_44C1')

    def _loc_44C1(): pass

    label('loc_44C1')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_44E6'),
        (0x00000003, 'loc_44F3'),
        (0x00000004, 'loc_4500'),
        (0x00000005, 'loc_450D'),
        (0x00000006, 'loc_451A'),
        (0x00000007, 'loc_4527'),
        (0x00000008, 'loc_4534'),
        (-1, 'loc_4541'),
    )

    def _loc_44E6(): pass

    label('loc_44E6')

    LoadChip('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP', 14)

    Jump('loc_4541')

    def _loc_44F3(): pass

    label('loc_44F3')

    LoadChip('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP', 14)

    Jump('loc_4541')

    def _loc_4500(): pass

    label('loc_4500')

    LoadChip('ED6_DT27/CH03213._CH', 'ED6_DT27/CH03213P._CP', 14)

    Jump('loc_4541')

    def _loc_450D(): pass

    label('loc_450D')

    LoadChip('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP', 14)

    Jump('loc_4541')

    def _loc_451A(): pass

    label('loc_451A')

    LoadChip('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP', 14)

    Jump('loc_4541')

    def _loc_4527(): pass

    label('loc_4527')

    LoadChip('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP', 14)

    Jump('loc_4541')

    def _loc_4534(): pass

    label('loc_4534')

    LoadChip('ED6_DT27/CH03083._CH', 'ED6_DT27/CH03083P._CP', 14)

    Jump('loc_4541')

    def _loc_4541(): pass

    label('loc_4541')

    CameraMove(59810, 0, -1090, 0)
    OP_67(0, 5780, -10000, 0)
    CameraSetDistance(4450, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetChipByIndex(0x0101, 10)
    ChrSetChipByIndex(0x0102, 11)
    ChrSetChipByIndex(0x0146, 12)
    ChrSetChipByIndex(0x00F8, 13)
    ChrSetChipByIndex(0x00F9, 14)
    ChrSetSubChip(0x00F9, 1)
    ChrSetFlags(0x0146, 0x0004)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x00F8, 0x0004)
    ChrSetFlags(0x00F9, 0x0004)
    ChrSetPos(0x0146, 59020, 200, 3010, 90)
    ChrSetPos(0x0101, 60220, 200, 4430, 180)
    ChrSetPos(0x0102, 60040, 200, 1600, 0)
    ChrSetPos(0x00F8, 61850, 200, 4460, 180)
    ChrSetPos(0x00F9, 61850, 200, 1520, 0)

    @scena.Lambda('lambda_4610')
    def lambda_4610():
        CameraMove(59860, 0, 4019, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4610)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    Fade(500)
    CameraMove(59860, 0, 4019, 0)
    OP_67(0, 5780, -10000, 0)
    CameraSetDistance(3510, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0146,
        (
            '#0090391224V#413F#5P……对不起……\n',
            '好像吓到你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391225V#210F我没事，已经平静下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391226V#1019F真是的……\n',
            '害我吓了一大跳呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391227V#1035F#6P那么，乔丝特……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391228V#1042F能将其它人被捕时的情况\n',
            '详细地告诉我们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x0146, 2)
    Sleep(300)

    ChrTalk(
        0x0146,
        (
            '#0090391229V#215F#5P……嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391230V#212F我们坠落到这里之后，\n',
            '马上就开始着手修理『山猫号』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391231V虽然引擎平安无事，\n',
            '可是其它装置全部都损坏了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391232V所以我们试着在这附近进行探索，\n',
            '看看有没有可以用来修理的材料……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_48C2',
    )

    ChrTalk(
        0x0106,
        (
            '#0050391233V#555F嗯……\n',
            '和我们的情况差不多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A07')

    def _loc_48C2(): pass

    label('loc_48C2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4900',
    )

    ChrTalk(
        0x0108,
        (
            '#0080391234V#070F和我们的情况差不多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A07')

    def _loc_4900(): pass

    label('loc_4900')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4949',
    )

    ChrTalk(
        0x0103,
        (
            '#0030391235V#020F原来如此。\n',
            '和我们的情况差不多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A07')

    def _loc_4949(): pass

    label('loc_4949')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4988',
    )

    ChrTalk(
        0x0109,
        (
            '#0180391236V#1063F和我们的情况差不多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A07')

    def _loc_4988(): pass

    label('loc_4988')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_49CD',
    )

    ChrTalk(
        0x0104,
        (
            '#0040391237V#030F嗯……\n',
            '和我们的情况差不多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A07')

    def _loc_49CD(): pass

    label('loc_49CD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4A07',
    )

    ChrTalk(
        0x0105,
        (
            '#0060391238V#1162F和我们的情况差不多呢',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A07(): pass

    label('loc_4A07')

    ChrTalk(
        0x0146,
        (
            '#0090391239V#215F#5P……大约三天之后吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391240V当我们找齐了原先不足的材料，\n',
            '正准备进行正式的修复工作时，\n',
            '像章鱼的那种人形兵器出现了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391241V#413F当我击中它之后，\n',
            '红色飞艇就飞了过来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391242V一着陆，那些猎兵们\n',
            '就三三两两地跑下来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391243V#1043F#6P把正在警戒行动中的\n',
            '『哨兵』打倒了吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391244V#1035F大概是被破坏时所发出的\n',
            '紧急信号传送到敌人那里了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090391245V#216F#5P果然是这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391246V#215F怎、怎么办……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391247V都怪我做了多余的事情。\n',
            '害得大哥他们和大家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391248V#1043F#6P乔丝特……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391249V#1022F啊～真是的！\n',
            '别摆出那种表情嘛！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391250V#1005F被抓住的话，\n',
            '去救出来不就行了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0146, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetSubChip(0x0146, 0)

    ChrTalk(
        0x0146,
        (
            '#0090391251V#213F#5P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391252V#1006F即使是罪犯，\n',
            '只要遭到了不当监禁，\n',
            '就是游击士的保护对象。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391253V反正也必须和『结社』\n',
            '做个了结才行……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391254V就顺便帮你救出\n',
            '你哥哥他们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391255V#1040F#6P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0146, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0146,
        (
            '#0090391256V#212F#5P等、等一下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391257V#214F为什么我们\n',
            '非要接受什么游击士的\n',
            '帮助不可啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391258V#1007F哦～『什么游击士』吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391259V#1028F这么说的话，\n',
            '你一个人能救得了他们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090391260V#216F#5P唔唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391261V#1006F而且我们在逃出\n',
            '『古罗力亚斯』的时候\n',
            '不是也受过你们的帮助吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391262V就在这个地方\n',
            '让我还你们一个人情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090391263V#214F#5P～～～～～！～～～～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391264V#1035F#6P乔丝特……\n',
            '正如艾丝蒂尔所言。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391265V#1040F你一个人待在这里\n',
            '也解决不了任何问题的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391266V这点你应该明白吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090391267V#215F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391268V#1040F#6P如果你愿意的话，\n',
            '就暂时在埃尔赛尤等候好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391269V#1035F吉尔他们\n',
            '应该是被抓到『古罗力亚斯』去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391270V照这样子搜索下去的话，\n',
            '或许可以找到前往\n',
            '停泊场所的道路也说不定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391271V#1040F到那时候一定会通知你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090391272V#215F#5P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391273V#413F……我明白了。\n',
            '既然约修亚这么说的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391274V#214F不过，平白接受别人的帮助\n',
            '会有损我们卡普亚一家的名声的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391275V搜索也好、修理飞船也好，\n',
            '请让我也帮忙做点什么吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391276V#1016F啊～好的好的，\n',
            '真是不坦率啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090391277V#210F#5P哼、哼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391278V总比某个喜欢扮好人的\n',
            '笨女人强吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391279V#1019F你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391280V#1052F#6P唉，真是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391281V#1048F……虽然不知道是什么原因，\n',
            '不过你们就不能和睦相处吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(50)

    OP_62(0x0146, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0101)
    OP_63(0x0146)
    Sleep(500)

    ChrSetSubChip(0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010391282V#1007F我说啊，约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x0146, 2)

    ChrTalk(
        0x0146,
        (
            '#0090391283V#212F#5P……你怎么能说这种话？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361226V#1044F#6P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_545F',
    )

    ChrTalk(
        0x0109,
        (
            '#0180391285V#1068F（不好……\n',
            '  踩到地雷了吗）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_559B')

    def _loc_545F(): pass

    label('loc_545F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_54AA',
    )

    ChrTalk(
        0x0104,
        (
            '#0040391286V#035F（哎呀呀……\n',
            '  好像是踩到地雷了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_559B')

    def _loc_54AA(): pass

    label('loc_54AA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_54E4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050391287V#551F（踩到地雷了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_559B')

    def _loc_54E4(): pass

    label('loc_54E4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5522',
    )

    ChrTalk(
        0x0108,
        (
            '#0080391288V#075F（这下踩到地雷了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_559B')

    def _loc_5522(): pass

    label('loc_5522')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5562',
    )

    ChrTalk(
        0x0103,
        (
            '#0030391289V#025F（哈……踩到地雷了吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_559B')

    def _loc_5562(): pass

    label('loc_5562')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_559B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070391290V#065F（我、我说哥哥……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_559B(): pass

    label('loc_559B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_55DC',
    )

    ChrTalk(
        0x0105,
        (
            '#0060391291V#1167F（…………………迟钝。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5730')

    def _loc_55DC(): pass

    label('loc_55DC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5618',
    )

    ChrTalk(
        0x0107,
        (
            '#0070391290V#065F（我、我说哥哥……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5730')

    def _loc_5618(): pass

    label('loc_5618')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5654',
    )

    ChrTalk(
        0x0103,
        (
            '#0030391293V#025F（修行远远不够呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5730')

    def _loc_5654(): pass

    label('loc_5654')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5695',
    )

    ChrTalk(
        0x0108,
        (
            '#0080391294V#071F（哎～……\n',
            '  年轻真好。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5730')

    def _loc_5695(): pass

    label('loc_5695')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_56E6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050391295V#555F（该怎么说呢……\n',
            '  初生牛犊不畏虎啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5730')

    def _loc_56E6(): pass

    label('loc_56E6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5730',
    )

    ChrTalk(
        0x0104,
        (
            '#0040391296V#031F（哈哈哈。\n',
            '  真是初生牛犊不畏虎啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5730(): pass

    label('loc_5730')

    ChrTalk(
        0x0101,
        (
            '#0010391297V#1019F喂，乔丝特……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391298V我们现在要不要暂时休战？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090391299V#413F#5P……说得也是，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391300V毕竟当前的敌人\n',
            '并不是彼此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391301V#1048F#6P嗯，那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391302V能融洽相处自然是最好\n',
            '……我说了什么不该说的话了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391303V#1001F不，完全没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090391304V#211F#5P大概是心理作用吧～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391305V#1052F#6P是、是吗……\n',
            '（眼神中看不出笑意……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_58E5',
    )

    SetScenaFlags(ScenaFlag(0x0454, 4, 0x22A4))

    def _loc_58E5(): pass

    label('loc_58E5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_58F6',
    )

    SetScenaFlags(ScenaFlag(0x0453, 5, 0x229D))

    def _loc_58F6(): pass

    label('loc_58F6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5904',
    )

    def _loc_5904(): pass

    label('loc_5904')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5915',
    )

    SetScenaFlags(ScenaFlag(0x0454, 7, 0x22A7))

    def _loc_5915(): pass

    label('loc_5915')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5926',
    )

    SetScenaFlags(ScenaFlag(0x0454, 0, 0x22A0))

    def _loc_5926(): pass

    label('loc_5926')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5937',
    )

    SetScenaFlags(ScenaFlag(0x0454, 2, 0x22A2))

    def _loc_5937(): pass

    label('loc_5937')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5945',
    )

    def _loc_5945(): pass

    label('loc_5945')

    ChrSetStatus(ChrTable['乔丝特'], 0x00, 72)
    ChrSetStatus(ChrTable['乔丝特'], 0xFE, 0)
    EquipCmd(ChrTable['乔丝特'], ItemTable['独眼巨人'], 0xFF)
    EquipCmd(ChrTable['乔丝特'], ItemTable['树脂装甲'], 0xFF)
    EquipCmd(ChrTable['乔丝特'], ItemTable['斯托雷加Ｇ'], 0xFF)
    EquipCmd(ChrTable['乔丝特'], ItemTable['光明背带'], 0xFF)
    OP_37(0x0A, 0x7F, 0x02)
    EquipCmd(ChrTable['乔丝特'], ItemTable['防御４'], 0x00)
    EquipCmd(ChrTable['乔丝特'], ItemTable['省ＥＰ４'], 0x04)
    EquipCmd(ChrTable['乔丝特'], ItemTable['攻击４'], 0x06)
    AddCraft(ChrTable['乔丝特'], 0x0000)
    CameraMove(-25340, 0, 52840, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　请选择２名固定成员以外的同行者。\n',
            '　（离开的人会自动返回埃尔赛尤号。）',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    FadeIn(0, 0)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5A68',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    Jump('loc_5E11')

    def _loc_5A68(): pass

    label('loc_5A68')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5A97',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['科洛丝'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    Jump('loc_5E11')

    def _loc_5A97(): pass

    label('loc_5A97')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5AC6',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['奥利维尔'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    Jump('loc_5E11')

    def _loc_5AC6(): pass

    label('loc_5AC6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5AF5',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['提妲'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    Jump('loc_5E11')

    def _loc_5AF5(): pass

    label('loc_5AF5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5B24',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['金'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    Jump('loc_5E11')

    def _loc_5B24(): pass

    label('loc_5B24')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5B53',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['凯文神父'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    Jump('loc_5E11')

    def _loc_5B53(): pass

    label('loc_5B53')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5B82',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['科洛丝'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    Jump('loc_5E11')

    def _loc_5B82(): pass

    label('loc_5B82')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5BB1',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['奥利维尔'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    Jump('loc_5E11')

    def _loc_5BB1(): pass

    label('loc_5BB1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5BE0',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    Jump('loc_5E11')

    def _loc_5BE0(): pass

    label('loc_5BE0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5C0F',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['金'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    Jump('loc_5E11')

    def _loc_5C0F(): pass

    label('loc_5C0F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5C3E',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['凯文神父'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    Jump('loc_5E11')

    def _loc_5C3E(): pass

    label('loc_5C3E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5C6D',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['科洛丝'],
            ChrTable['奥利维尔'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    Jump('loc_5E11')

    def _loc_5C6D(): pass

    label('loc_5C6D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5C9C',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['科洛丝'],
            ChrTable['提妲'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    Jump('loc_5E11')

    def _loc_5C9C(): pass

    label('loc_5C9C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5CCB',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['科洛丝'],
            ChrTable['金'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    Jump('loc_5E11')

    def _loc_5CCB(): pass

    label('loc_5CCB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5CFA',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['科洛丝'],
            ChrTable['凯文神父'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    Jump('loc_5E11')

    def _loc_5CFA(): pass

    label('loc_5CFA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5D29',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['提妲'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    Jump('loc_5E11')

    def _loc_5D29(): pass

    label('loc_5D29')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5D58',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['金'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    Jump('loc_5E11')

    def _loc_5D58(): pass

    label('loc_5D58')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5D87',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['凯文神父'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    Jump('loc_5E11')

    def _loc_5D87(): pass

    label('loc_5D87')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5DB6',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['提妲'],
            ChrTable['金'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    Jump('loc_5E11')

    def _loc_5DB6(): pass

    label('loc_5DB6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5DE5',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['提妲'],
            ChrTable['凯文神父'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    Jump('loc_5E11')

    def _loc_5DE5(): pass

    label('loc_5DE5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5E11',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['金'],
            ChrTable['凯文神父'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    def _loc_5E11(): pass

    label('loc_5E11')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_0D()
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/C5801._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0011 offset: 0x5E37
@scena.Code('func_11_5E37')
def func_11_5E37():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5E4E',
    )

    Call(0, 0x0014)
    Call(0, 0x0016)

    def _loc_5E4E(): pass

    label('loc_5E4E')

    LoadChip('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP', 10)
    LoadChip('ED6_DT27/CH03013._CH', 'ED6_DT27/CH03013P._CP', 11)
    LoadChip('ED6_DT27/CH03103._CH', 'ED6_DT27/CH03103P._CP', 12)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_5E91'),
        (0x00000003, 'loc_5E9E'),
        (0x00000004, 'loc_5EAB'),
        (0x00000005, 'loc_5EB8'),
        (0x00000006, 'loc_5EC5'),
        (0x00000007, 'loc_5ED2'),
        (0x00000008, 'loc_5EDF'),
        (-1, 'loc_5EEC'),
    )

    def _loc_5E91(): pass

    label('loc_5E91')

    LoadChip('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP', 13)

    Jump('loc_5EEC')

    def _loc_5E9E(): pass

    label('loc_5E9E')

    LoadChip('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP', 13)

    Jump('loc_5EEC')

    def _loc_5EAB(): pass

    label('loc_5EAB')

    LoadChip('ED6_DT27/CH03213._CH', 'ED6_DT27/CH03213P._CP', 13)

    Jump('loc_5EEC')

    def _loc_5EB8(): pass

    label('loc_5EB8')

    LoadChip('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP', 13)

    Jump('loc_5EEC')

    def _loc_5EC5(): pass

    label('loc_5EC5')

    LoadChip('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP', 13)

    Jump('loc_5EEC')

    def _loc_5ED2(): pass

    label('loc_5ED2')

    LoadChip('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP', 13)

    Jump('loc_5EEC')

    def _loc_5EDF(): pass

    label('loc_5EDF')

    LoadChip('ED6_DT27/CH03083._CH', 'ED6_DT27/CH03083P._CP', 13)

    Jump('loc_5EEC')

    def _loc_5EEC(): pass

    label('loc_5EEC')

    LoadChip('ED6_DT27/CH03763._CH', 'ED6_DT27/CH03763P._CP', 14)
    LoadChip('ED6_DT27/CH03773._CH', 'ED6_DT27/CH03773P._CP', 15)
    CameraMove(59860, 0, 4019, 0)
    OP_67(0, 5780, -10000, 0)
    CameraSetDistance(3510, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetChipByIndex(0x0101, 10)
    ChrSetChipByIndex(0x0102, 11)
    ChrSetChipByIndex(0x010B, 12)
    ChrSetChipByIndex(0x00F9, 13)
    ChrSetChipByIndex(0x0009, 14)
    ChrSetChipByIndex(0x000A, 15)
    ChrSetFlags(0x010B, 0x0004)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x00F9, 0x0004)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetPos(0x010B, 59020, 200, 3010, 90)
    ChrSetPos(0x0009, 60220, 200, 4430, 180)
    ChrSetPos(0x000A, 61850, 200, 4460, 180)
    ChrSetPos(0x0102, 60040, 200, 1600, 0)
    ChrSetPos(0x0101, 61850, 200, 1520, 0)
    ChrSetPos(0x00F9, 62840, 200, 3040, 270)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0300400527V#198F#2P──所以说，\n',
            '我们打算马上着手进行\n',
            '『山猫号』的修理工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400528V#197F所幸已经找齐了材料，\n',
            '我想应该会有办法的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290400529V#203F#2P机身方面暂且不提，\n',
            '问题是那个『导力停止现象』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400530V#206F总之，即使勉强起飞，\n',
            '也会在离开都市的瞬间坠落吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400531V#1015F#6P嗯……\n',
            '如果没有大型的『零力场发生器』，\n',
            '我想的确会变成那样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400532V#1044F#6P要请埃尔赛尤号的\n',
            '拉赛尔博士帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290400533V#200F#2P嗯，只要在都市里，\n',
            '导力通讯似乎也可以使用，\n',
            '必要时我们会联络博士的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400534V话说回来，你们打算\n',
            '继续寻找『辉之环』吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400535V#1040F#6P嗯，就是这么打算的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400536V#1006F#6P那也正是我们\n',
            '来到这座浮游都市的真正目的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x010B, 2)
    Sleep(300)

    ChrTalk(
        0x010B,
        (
            '#0090400537V#213F#5P啊，说到这个，\n',
            '你们好像曾经提过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400538V不是要来寻宝什么的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x0101, 1)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010400539V#1019F#6P我说啊……\n',
            '别把我们和你们混为一谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0009)
    OP_63(0x000A)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0290400540V#200F#2P……那么，乔丝特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400541V你就继续和约修亚他们\n',
            '一起行动如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x010B, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Sleep(100)

    ChrSetSubChip(0x010B, 0)
    Sleep(100)

    ChrSetSubChip(0x0101, 0)
    Sleep(300)

    ChrTalk(
        0x010B,
        (
            '#0090400542V#213F#5P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0300400543V#490F#2P修理『山猫号』\n',
            '有我们几个就足够了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400544V要说让你负责什么工作的话，\n',
            '我们还是希望你去收集情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400545V#210F#5P啊，原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400546V#1035F#6P的确，在这种形势下，\n',
            '埃尔赛尤和山猫号之间\n',
            '也需要有一个联络人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400547V#1040F听起来好像不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400548V#1006F#6P嗯，我也有同感。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400549V为了对抗『结社』，\n',
            '伙伴当然是越多越好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400550V让乔丝特来进行辅助的话，\n',
            '完全值得信赖，\n',
            '这样可就帮我们一个大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x010B, 2)
    Sleep(300)

    ChrTalk(
        0x010B,
        (
            '#0090400551V#213F#5P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x0101, 1)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010400552V#1004F#6P咦，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400553V#216F#5P不，这个，怎么说呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400554V#215F（……喂，约修亚。\n',
            '  她说这话是认真的吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400555V#1049F#6P（哈哈……她就是那种女孩啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400556V#413F#5P（真让人头疼呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400557V#1009F#6P什、什么嘛。\n',
            '干嘛摆出那副诧异的表情？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400558V#210F#5P不，不是诧异的表情，\n',
            '而是完全的吃了一惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400559V#1019F#6P什、什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0300400560V#191F#2P哈哈哈。\n',
            '似乎已经决定了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290400561V#200F#2P那么我们就\n',
            '返回『山猫号』啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400562V乔丝特。\n',
            '要多加小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x010B, 0)
    Sleep(100)

    ChrSetSubChip(0x0101, 0)
    Sleep(300)

    ChrTalk(
        0x010B,
        (
            '#0090400563V#210F#5P啊，嗯……\n',
            '大哥你们也要当心哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400564V说不定『结社』那些家伙\n',
            '还会过来袭击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0300400565V#191F#2P哈哈哈，别担心啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290400566V#200F#2P好了，我们会尽量小心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)

    @scena.Lambda('lambda_69B7')
    def lambda_69B7():
        CameraMove(59950, 0, 5310, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_69B7)

    ChrSetChipByIndex(0x0009, 8)
    ChrSetChipByIndex(0x000A, 9)
    ChrClearFlags(0x0009, 0x0004)
    ChrClearFlags(0x000A, 0x0004)
    ChrSetPos(0x0009, 59170, 0, 4380, 270)
    ChrSetPos(0x000A, 62820, 0, 4390, 90)
    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_6A0B')
    def lambda_6A0B():
        CameraMove(59480, 0, -310, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6A0B)

    CreateThread(0x0009, 0x01, 0x00, func_12_6BBA)
    Sleep(100)

    CreateThread(0x000A, 0x01, 0x00, func_13_6C13)
    ChrSetSubChip(0x010B, 1)
    Sleep(50)

    ChrSetSubChip(0x00F9, 2)
    Sleep(500)

    ChrSetSubChip(0x0102, 1)
    Sleep(50)

    ChrSetSubChip(0x0101, 2)
    Sleep(1000)

    ChrSetSubChip(0x010B, 0)
    Sleep(50)

    ChrSetSubChip(0x00F9, 0)
    Sleep(1000)

    ChrSetSubChip(0x010B, 2)
    Sleep(50)

    ChrSetSubChip(0x00F9, 1)
    SetScenaFlags(ScenaFlag(0x0445, 4, 0x222C))
    OP_28(0x009E, 0x01, 0x0100)
    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x000A, 0x0001)
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '乔丝特学会了',
            (TxtCtl.SetColor, 0x2),
            '山猫号',
            (TxtCtl.SetColor, 0x5),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    AddSCraft(ChrTable['乔丝特'], CraftTable['山猫号'])
    OP_BB(0x0A, 0x06, 0x00000112)
    PlaySE(542, 0x00, 0x64)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrClearFlags(0x010B, 0x0004)
    ChrClearFlags(0x0101, 0x0004)
    ChrClearFlags(0x0102, 0x0004)
    ChrClearFlags(0x00F9, 0x0004)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x010B, 65535)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 0)
    ChrSetSubChip(0x010B, 0)
    ChrSetSubChip(0x00F9, 0)
    CameraMove(58080, 0, 600, 0)
    OP_67(0, 5500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 58080, 0, 600, 180)
    ChrSetPos(0x0001, 58080, 0, 600, 180)
    ChrSetPos(0x0002, 58080, 0, 600, 180)
    ChrSetPos(0x0003, 58080, 0, 600, 180)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0012 offset: 0x6BBA
@scena.Code('func_12_6BBA')
def func_12_6BBA():
    ChrWalkTo(0x00FE, 57440, 0, 3000, 3000, 0x00)
    ChrWalkTo(0x00FE, 60080, 0, -7830, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_6BED')
    def lambda_6BED():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_6BED)

    ChrWalkTo(0x00FE, 60130, 0, -9010, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0013 offset: 0x6C13
@scena.Code('func_13_6C13')
def func_13_6C13():
    ChrWalkTo(0x00FE, 64769, 0, 3420, 3000, 0x00)
    ChrWalkTo(0x00FE, 61930, 0, -7870, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_6C46')
    def lambda_6C46():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_6C46)

    ChrWalkTo(0x00FE, 61890, 0, -9140, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0014 offset: 0x6C6C
@scena.Code('func_14_6C6C')
def func_14_6C6C():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_6CE6'),
        (0x00000001, 'loc_6CEC'),
        (-1, 'loc_6CF2'),
    )

    def _loc_6CE6(): pass

    label('loc_6CE6')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_6CF2')

    def _loc_6CEC(): pass

    label('loc_6CEC')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_6CF2')

    def _loc_6CF2(): pass

    label('loc_6CF2')

    Return()

# id: 0x0015 offset: 0x6CF3
@scena.Code('func_15_6CF3')
def func_15_6CF3():
    FadeOut(0, 0, -1)
    CameraMove(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['科洛丝'],
            ChrTable['奥利维尔'],
            ChrTable['提妲'],
            ChrTable['金'],
            ChrTable['凯文神父'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

# id: 0x0016 offset: 0x6D84
@scena.Code('func_16_6D84')
def func_16_6D84():
    FadeOut(0, 0, -1)
    CameraMove(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            ChrTable['乔丝特'],
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['科洛丝'],
            ChrTable['奥利维尔'],
            ChrTable['提妲'],
            ChrTable['金'],
            ChrTable['凯文神父'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
