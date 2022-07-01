import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5303_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5303   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '升降梯'),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5303.x'
    header.mapIndex       = 1
    header.bgm            = 64
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x136D
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
        ('ED6_DT29/CH12010._CH', 'ED6_DT29/CH12010P._CP'),
        ('ED6_DT29/CH12010._CH', 'ED6_DT29/CH12010P._CP'),
        ('ED6_DT29/CH12080._CH', 'ED6_DT29/CH12080P._CP'),
        ('ED6_DT29/CH12081._CH', 'ED6_DT29/CH12081P._CP'),
        ('ED6_DT29/CH12050._CH', 'ED6_DT29/CH12050P._CP'),
        ('ED6_DT29/CH12051._CH', 'ED6_DT29/CH12051P._CP'),
        ('ED6_DT29/CH12140._CH', 'ED6_DT29/CH12140P._CP'),
        ('ED6_DT29/CH12141._CH', 'ED6_DT29/CH12141P._CP'),
        ('ED6_DT29/CH12420._CH', 'ED6_DT29/CH12420P._CP'),
        ('ED6_DT29/CH12421._CH', 'ED6_DT29/CH12421P._CP'),
        ('ED6_DT29/CH12340._CH', 'ED6_DT29/CH12340P._CP'),
        ('ED6_DT29/CH12341._CH', 'ED6_DT29/CH12341P._CP'),
    ]

# id: 0x10002 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x12A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 91440,
            z           = 0,
            y           = -73190,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x052C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 73490,
            z           = 0,
            y           = -91400,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0528,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -76640,
            z           = 0,
            y           = -90640,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x052B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -94840,
            z           = 0,
            y           = -72560,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0530,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -97730,
            z           = 0,
            y           = 87090,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0529,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -79380,
            z           = 0,
            y           = 104930,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x052C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1D2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 100010,
            y           = -2000,
            z           = 9030,
            range       = 3000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000007,
        ),
        ScenaEventData(
            x           = 5130,
            y           = -2000,
            z           = 110010,
            range       = 3000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000009,
        ),
    )

# id: 0x10005 offset: 0x212
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -10540,
            triggerZ            = 0,
            triggerY            = -90650,
            triggerRange        = 1000,
            actorX              = -10500,
            actorZ              = 0,
            actorY              = -90040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 9500,
            triggerZ            = 0,
            triggerY            = -90660,
            triggerRange        = 1000,
            actorX              = 9520,
            actorZ              = 0,
            actorY              = -89950,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 9500,
            triggerZ            = 0,
            triggerY            = -95340,
            triggerRange        = 1000,
            actorX              = 9520,
            actorZ              = 0,
            actorY              = -96050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -10460,
            triggerZ            = 0,
            triggerY            = -95340,
            triggerRange        = 1000,
            actorX              = -10500,
            actorZ              = 0,
            actorY              = -96000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2A2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_2B3',
    )

    OP_A3(0x10F0)
    Event(0, 0x0006)

    Jump('loc_2DC')

    def _loc_2B3(): pass

    label('loc_2B3')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_2C7'),
        (0x00000072, 'loc_2CE'),
        (0x00000074, 'loc_2D5'),
        (-1, 'loc_2DC'),
    )

    def _loc_2C7(): pass

    label('loc_2C7')

    Event(0, 0x0008)

    Jump('loc_2DC')

    def _loc_2CE(): pass

    label('loc_2CE')

    Event(0, 0x000A)

    Jump('loc_2DC')

    def _loc_2D5(): pass

    label('loc_2D5')

    Event(0, 0x000C)

    Jump('loc_2DC')

    def _loc_2DC(): pass

    label('loc_2DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 6, 0x2236)),
            Expr.Return,
        ),
        'loc_323',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_323',
    )

    OP_A2(0x0000)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_323(): pass

    label('loc_323')

    Return()

# id: 0x0001 offset: 0x324
@scena.Code('Init')
def Init():
    ExecExpressionWithValue(
        0x000A,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x24,
        (
            (Expr.PushLong, 0xD7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046E, 6, 0x2376)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_357',
    )

    OP_6F(0x0003, 0)

    Jump('loc_35E')

    def _loc_357(): pass

    label('loc_357')

    OP_6F(0x0003, 60)

    def _loc_35E(): pass

    label('loc_35E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046F, 0, 0x2378)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_370',
    )

    OP_6F(0x0004, 0)

    Jump('loc_377')

    def _loc_370(): pass

    label('loc_370')

    OP_6F(0x0004, 60)

    def _loc_377(): pass

    label('loc_377')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046F, 1, 0x2379)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_389',
    )

    OP_6F(0x0005, 0)

    Jump('loc_390')

    def _loc_389(): pass

    label('loc_389')

    OP_6F(0x0005, 60)

    def _loc_390(): pass

    label('loc_390')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046F, 2, 0x237A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A2',
    )

    OP_6F(0x0006, 0)

    Jump('loc_3A9')

    def _loc_3A2(): pass

    label('loc_3A2')

    OP_6F(0x0006, 60)

    def _loc_3A9(): pass

    label('loc_3A9')

    OP_10(0x00, 0x00)
    OP_10(0x0E, 0x00)
    OP_82(0x84, 0x00)
    OP_82(0x88, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 6, 0x2236)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D4',
    )

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 0)
    OP_10(0x10, 0x00)

    Jump('loc_425')

    def _loc_3D4(): pass

    label('loc_3D4')

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 600)
    OP_10(0x10, 0x01)
    OP_82(0x83, 0x00)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_1B(0x10, 0x00, 0x000B)

    def _loc_425(): pass

    label('loc_425')

    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_6F(0x0001, 0)
    OP_72(0x0002, 0x0020)
    OP_72(0x0002, 0x0008)
    OP_6F(0x0002, 0)
    OP_22(0x0140, 0x00, 0x64)

    Return()

# id: 0x0002 offset: 0x44D
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0x38, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046E, 6, 0x2376)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_52A',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0003, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['Ｓ－药片'], 1)"),
            Expr.Return,
        ),
        'loc_4C1',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x2376)

    Jump('loc_527')

    def _loc_4C1(): pass

    label('loc_4C1')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0x00000000)

    def _loc_527(): pass

    label('loc_527')

    Jump('loc_55B')

    def _loc_52A(): pass

    label('loc_52A')

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
    def _loc_55B(): pass

    label('loc_55B')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x569
@scena.Code('func_03_569')
def func_03_569():
    UnlockAchievement(0x02, 0x39, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046F, 0, 0x2378)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_646',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0004, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_5DD',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x2378)

    Jump('loc_643')

    def _loc_5DD(): pass

    label('loc_5DD')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0x00000000)

    def _loc_643(): pass

    label('loc_643')

    Jump('loc_677')

    def _loc_646(): pass

    label('loc_646')

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
    def _loc_677(): pass

    label('loc_677')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x685
@scena.Code('func_04_685')
def func_04_685():
    UnlockAchievement(0x02, 0x3A, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046F, 1, 0x2379)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_762',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0005, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_6F9',
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
    OP_A2(0x2379)

    Jump('loc_75F')

    def _loc_6F9(): pass

    label('loc_6F9')

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
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0x00000000)

    def _loc_75F(): pass

    label('loc_75F')

    Jump('loc_793')

    def _loc_762(): pass

    label('loc_762')

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
    def _loc_793(): pass

    label('loc_793')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x7A1
@scena.Code('func_05_7A1')
def func_05_7A1():
    UnlockAchievement(0x02, 0x3B, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046F, 2, 0x237A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_87E',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0006, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['痊愈之药'], 1)"),
            Expr.Return,
        ),
        'loc_815',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x237A)

    Jump('loc_87B')

    def _loc_815(): pass

    label('loc_815')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0x00000000)

    def _loc_87B(): pass

    label('loc_87B')

    Jump('loc_8AF')

    def _loc_87E(): pass

    label('loc_87E')

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
    def _loc_8AF(): pass

    label('loc_8AF')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x8BD
@scena.Code('func_06_8BD')
def func_06_8BD():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6D(-97890, 0, 32369, 0)
    OP_67(0, 7020, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(345000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_6F(0x0000, 0)
    OP_70(0x0000, 0x00000258)
    Sleep(1500)

    OP_22(0x00E1, 0x00, 0x64)
    Sleep(3000)

    OP_22(0x0070, 0x00, 0x64)
    OP_73(0x0000)

    @scena.Lambda('lambda_0945')
    def lambda_0945():
        OP_6D(-88930, 1090, 4140, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0945)

    @scena.Lambda('lambda_095D')
    def lambda_095D():
        OP_67(0, 9500, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_095D)

    OP_6C(315000, 5000)
    Fade(1000)
    OP_22(0x00D7, 0x00, 0x64)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(3000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5309._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x9D4
@scena.Code('func_07_9D4')
def func_07_9D4():
    EventBegin(0x00)
    OP_A1(0x0008, 0x0001)
    SetChrPos(0x0008, 100010, -1750, 9030, 0)
    Yield()
    Fade(1000)
    OP_6D(100010, 0, 9030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 100000, 0, 10000, 0)
    OP_89(0x0001, 101000, 0, 9000, 90)
    OP_89(0x0002, 99000, 0, 9000, 270)
    OP_89(0x0003, 100000, 0, 8000, 180)
    OP_0D()
    Sleep(300)

    SetMapFlags(0x00100000)
    OP_22(0x00EB, 0x00, 0x64)

    @scena.Lambda('lambda_0A89')
    def lambda_0A89():
        OP_67(0, 6500, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A89)

    @scena.Lambda('lambda_0AA1')
    def lambda_0AA1():
        OP_6B(3700, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0AA1)

    @scena.Lambda('lambda_0AB1')
    def lambda_0AB1():
        OP_91(0x00FE, 0, -10000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0AB1)

    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A3(0x228C)
    OP_A3(0x228D)
    OP_A3(0x228E)
    OP_A2(0x228F)
    OP_A3(0x2290)
    OP_A3(0x2291)
    OP_A3(0x2292)
    OP_A3(0x2293)
    OP_A3(0x2294)
    OP_A3(0x2295)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5316._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0xB01
@scena.Code('func_08_B01')
def func_08_B01():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_A1(0x0008, 0x0001)
    SetChrPos(0x0008, 100010, -11750, 9030, 0)
    Yield()
    OP_6D(100010, 0, 9030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 100000, 0, 10000, 0)
    OP_89(0x0001, 101000, 0, 9000, 90)
    OP_89(0x0002, 99000, 0, 9000, 270)
    OP_89(0x0003, 100000, 0, 8000, 180)
    OP_22(0x00EB, 0x00, 0x64)

    @scena.Lambda('lambda_0BB0')
    def lambda_0BB0():
        OP_6B(3500, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0BB0)

    FadeIn(1000, 0)
    SetPlaceName(0x011E)

    @scena.Lambda('lambda_0BCC')
    def lambda_0BCC():
        OP_91(0x00FE, 0, 10000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0BCC)

    Sleep(2200)

    OP_24(0x00EB, 0x5A)
    Sleep(50)

    OP_24(0x00EB, 0x50)
    Sleep(50)

    OP_24(0x00EB, 0x46)
    Sleep(50)

    OP_24(0x00EB, 0x3C)
    Sleep(50)

    OP_24(0x00EB, 0x32)
    Sleep(50)

    OP_24(0x00EB, 0x28)
    Sleep(50)

    OP_24(0x00EB, 0x1E)
    Sleep(50)

    OP_24(0x00EB, 0x14)
    Sleep(50)

    OP_24(0x00EB, 0x0A)
    Sleep(50)

    OP_23(0x00EB)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0008, 0x0001)
    Sleep(500)

    Fade(1000)
    SetChrPos(0x0000, 100220, 0, 4340, 180)
    SetChrPos(0x0001, 100220, 0, 4340, 180)
    SetChrPos(0x0002, 100220, 0, 4340, 180)
    SetChrPos(0x0003, 100220, 0, 4340, 180)
    OP_69(0x0000, 0x00000000)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0xC9D
@scena.Code('func_09_C9D')
def func_09_C9D():
    EventBegin(0x00)
    OP_A1(0x0008, 0x0002)
    SetChrPos(0x0008, 5130, -1750, 110010, 90)
    Yield()
    Fade(1000)
    OP_6D(5130, 0, 110010, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 5000, 0, 111000, 0)
    OP_89(0x0001, 6000, 0, 110000, 90)
    OP_89(0x0002, 4000, 0, 110000, 270)
    OP_89(0x0003, 5000, 0, 109000, 180)
    OP_0D()
    SetMapFlags(0x00100000)
    OP_22(0x00EB, 0x01, 0x64)

    @scena.Lambda('lambda_0D4D')
    def lambda_0D4D():
        OP_8F(0x00FE, 5130, 65000, 110010, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0D4D)

    Sleep(500)

    @scena.Lambda('lambda_0D6D')
    def lambda_0D6D():
        OP_6D(5130, 35000, 110010, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D6D)

    @scena.Lambda('lambda_0D85')
    def lambda_0D85():
        OP_67(0, 14000, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D85)

    @scena.Lambda('lambda_0D9D')
    def lambda_0D9D():
        OP_6C(295000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0D9D)

    Sleep(500)

    @scena.Lambda('lambda_0DB2')
    def lambda_0DB2():
        OP_8F(0x00FE, 5130, 65000, 110010, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0DB2)

    Sleep(500)

    @scena.Lambda('lambda_0DD2')
    def lambda_0DD2():
        OP_8F(0x00FE, 5130, 65000, 110010, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0DD2)

    Sleep(400)

    @scena.Lambda('lambda_0DF2')
    def lambda_0DF2():
        OP_8F(0x00FE, 5130, 65000, 110010, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0DF2)

    Sleep(200)

    @scena.Lambda('lambda_0E12')
    def lambda_0E12():
        OP_8F(0x00FE, 5130, 65000, 110010, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0E12)

    Sleep(100)

    @scena.Lambda('lambda_0E32')
    def lambda_0E32():
        OP_8F(0x00FE, 5130, 65000, 110010, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0E32)

    Sleep(2000)

    Sleep(2000)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A3(0x228C)
    OP_A3(0x228D)
    OP_A3(0x228E)
    OP_A3(0x228F)
    OP_A2(0x2290)
    OP_A3(0x2291)
    OP_A3(0x2292)
    OP_A3(0x2293)
    OP_A3(0x2294)
    OP_A3(0x2295)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5316._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0xE8C
@scena.Code('func_0A_E8C')
def func_0A_E8C():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_A1(0x0008, 0x0002)
    SetChrPos(0x0008, 5130, 66000, 110010, 90)
    Yield()
    OP_6D(5130, 48000, 110010, 0)
    OP_67(0, 16000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(295000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 5000, 67000, 111000, 0)
    OP_89(0x0001, 6000, 67000, 110000, 90)
    OP_89(0x0002, 4000, 67000, 110000, 270)
    OP_89(0x0003, 5000, 67000, 109000, 180)
    OP_22(0x00EB, 0x01, 0x64)

    @scena.Lambda('lambda_0F3B')
    def lambda_0F3B():
        OP_6D(5130, 0, 110010, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F3B)

    @scena.Lambda('lambda_0F53')
    def lambda_0F53():
        OP_67(0, 9500, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0F53)

    @scena.Lambda('lambda_0F6B')
    def lambda_0F6B():
        OP_6C(315000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0F6B)

    FadeIn(1000, 0)
    SetPlaceName(0x011E)

    @scena.Lambda('lambda_0F87')
    def lambda_0F87():
        OP_8F(0x00FE, 5130, -1750, 110010, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0F87)

    Sleep(7800)

    @scena.Lambda('lambda_0FA7')
    def lambda_0FA7():
        OP_8F(0x00FE, 5130, -1750, 110010, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0FA7)

    Sleep(700)

    @scena.Lambda('lambda_0FC7')
    def lambda_0FC7():
        OP_8F(0x00FE, 5130, -1750, 110010, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0FC7)

    Sleep(600)

    @scena.Lambda('lambda_0FE7')
    def lambda_0FE7():
        OP_8F(0x00FE, 5130, -1750, 110010, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0FE7)

    Sleep(100)

    @scena.Lambda('lambda_1007')
    def lambda_1007():
        OP_8F(0x00FE, 5130, -1750, 110010, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1007)

    Sleep(500)

    OP_24(0x00EB, 0x5A)
    Sleep(50)

    OP_24(0x00EB, 0x50)
    Sleep(50)

    OP_24(0x00EB, 0x46)
    Sleep(50)

    OP_24(0x00EB, 0x3C)
    Sleep(50)

    OP_24(0x00EB, 0x32)
    Sleep(50)

    OP_24(0x00EB, 0x28)
    Sleep(50)

    OP_24(0x00EB, 0x1E)
    Sleep(50)

    OP_24(0x00EB, 0x14)
    Sleep(50)

    OP_24(0x00EB, 0x0A)
    Sleep(50)

    OP_23(0x00EB)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0008, 0x0001)
    Sleep(500)

    Fade(1000)
    SetChrPos(0x0000, 190, 0, 109990, 270)
    SetChrPos(0x0001, 190, 0, 109990, 270)
    SetChrPos(0x0002, 190, 0, 109990, 270)
    SetChrPos(0x0003, 190, 0, 109990, 270)
    OP_69(0x0000, 0x00000000)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x10D8
@scena.Code('func_0B_10D8')
def func_0B_10D8():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    OP_6D(-89000, 1050, 4000, 0)
    SetChrPos(0x0101, -88500, 1050, 4500, 90)
    SetChrPos(0x0102, -88500, 1050, 3500, 90)
    SetChrPos(0x00F8, -89500, 1050, 4500, 90)
    SetChrPos(0x00F9, -89500, 1050, 3500, 90)
    OP_0D()
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    @scena.Lambda('lambda_1183')
    def lambda_1183():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1183)

    @scena.Lambda('lambda_1195')
    def lambda_1195():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1195)

    @scena.Lambda('lambda_11A7')
    def lambda_11A7():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_11A7)

    @scena.Lambda('lambda_11B9')
    def lambda_11B9():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_11B9)

    Sleep(2000)

    NewScene('ED6_DT21/C5300._SN', 122, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x11D4
@scena.Code('func_0C_11D4')
def func_0C_11D4():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(-89000, 1050, 4000, 0)
    SetChrPos(0x0101, -89500, 1050, 3500, 270)
    SetChrPos(0x0102, -89500, 1050, 4500, 270)
    SetChrPos(0x00F8, -88500, 1050, 3500, 270)
    SetChrPos(0x00F9, -88500, 1050, 4500, 270)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    @scena.Lambda('lambda_12AF')
    def lambda_12AF():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_12AF)

    @scena.Lambda('lambda_12C1')
    def lambda_12C1():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_12C1)

    @scena.Lambda('lambda_12D3')
    def lambda_12D3():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_12D3)

    @scena.Lambda('lambda_12E5')
    def lambda_12E5():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_12E5)

    Sleep(2500)

    Fade(500)
    OP_6D(-92500, 0, 4000, 0)
    SetChrPos(0x0000, -92500, 0, 4000, 270)
    SetChrPos(0x0001, -92500, 0, 4000, 270)
    SetChrPos(0x0002, -92500, 0, 4000, 270)
    SetChrPos(0x0003, -92500, 0, 4000, 270)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
