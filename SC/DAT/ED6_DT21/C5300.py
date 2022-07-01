import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5300   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '怀斯曼教授'),
    TXT(0x02, '小丑肯帕雷拉'),
    TXT(0x03, '凯文神父'),
    TXT(0x04, '升降梯'),
    TXT(0x05, '怀斯曼之杖'),
    TXT(0x06, '地震控制用假人'),
    TXT(0x07, ''),
    TXT(0x08, ''),
    TXT(0x09, ''),
    TXT(0x0A, ''),
    TXT(0x0B, ''),
    TXT(0x0C, ''),
    TXT(0x0D, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5300.x'
    header.mapIndex       = 1
    header.bgm            = 64
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x34BA
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
        ('ED6_DT29/CH12280._CH', 'ED6_DT29/CH12280P._CP'),
        ('ED6_DT29/CH12281._CH', 'ED6_DT29/CH12281P._CP'),
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
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
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
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1CA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -76830,
            z           = 0,
            y           = -90660,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x052D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -94910,
            z           = 0,
            y           = -72500,
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
            x           = -100110,
            z           = 0,
            y           = 15090,
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
            x           = -87500,
            z           = 0,
            y           = 96820,
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
            x           = 81290,
            z           = 0,
            y           = 102460,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x052D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 99160,
            z           = 0,
            y           = 84400,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x052A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x272
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 102030,
            y           = -2000,
            z           = 1000,
            range       = 3000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000000D,
        ),
    )

# id: 0x10005 offset: 0x292
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 20,
            triggerZ            = 0,
            triggerY            = -83640,
            triggerRange        = 1000,
            actorX              = 50,
            actorZ              = 0,
            actorY              = -82980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -2550,
            triggerZ            = 0,
            triggerY            = -83650,
            triggerRange        = 1000,
            actorX              = -2520,
            actorZ              = 0,
            actorY              = -83030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 2450,
            triggerZ            = 0,
            triggerY            = -83650,
            triggerRange        = 1000,
            actorX              = 2480,
            actorZ              = 0,
            actorY              = -82990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 10350,
            triggerZ            = 0,
            triggerY            = -94070,
            triggerRange        = 1000,
            actorX              = 11050,
            actorZ              = 0,
            actorY              = -94030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 10350,
            triggerZ            = 0,
            triggerY            = -96660,
            triggerRange        = 1000,
            actorX              = 10970,
            actorZ              = 0,
            actorY              = -96630,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 10350,
            triggerZ            = 0,
            triggerY            = -91550,
            triggerRange        = 1000,
            actorX              = 11060,
            actorZ              = 0,
            actorY              = -91560,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x36A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_384',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x5A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F0)
    Event(0, 0x0009)

    Jump('loc_3C7')

    def _loc_384(): pass

    label('loc_384')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x77),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_397',
    )

    Event(0, 0x000E)

    Jump('loc_3C7')

    def _loc_397(): pass

    label('loc_397')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 4, 0x223C)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3B4',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0008)

    Jump('loc_3C7')

    def _loc_3B4(): pass

    label('loc_3B4')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000007A, 'loc_3C0'),
        (-1, 'loc_3C7'),
    )

    def _loc_3C0(): pass

    label('loc_3C0')

    Event(0, 0x000F)

    Jump('loc_3C7')

    def _loc_3C7(): pass

    label('loc_3C7')

    Return()

# id: 0x0001 offset: 0x3C8
@scena.Code('Init')
def Init():
    ExecExpressionWithValue(
        0x000E,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x24,
        (
            (Expr.PushLong, 0xD7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046C, 4, 0x2364)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_406',
    )

    OP_6F(0x0001, 0)

    Jump('loc_40D')

    def _loc_406(): pass

    label('loc_406')

    OP_6F(0x0001, 60)

    def _loc_40D(): pass

    label('loc_40D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046C, 6, 0x2366)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_41F',
    )

    OP_6F(0x0002, 0)

    Jump('loc_426')

    def _loc_41F(): pass

    label('loc_41F')

    OP_6F(0x0002, 60)

    def _loc_426(): pass

    label('loc_426')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046C, 7, 0x2367)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_438',
    )

    OP_6F(0x0003, 0)

    Jump('loc_43F')

    def _loc_438(): pass

    label('loc_438')

    OP_6F(0x0003, 60)

    def _loc_43F(): pass

    label('loc_43F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046D, 0, 0x2368)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_451',
    )

    OP_6F(0x0004, 0)

    Jump('loc_458')

    def _loc_451(): pass

    label('loc_451')

    OP_6F(0x0004, 60)

    def _loc_458(): pass

    label('loc_458')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046D, 1, 0x2369)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_46A',
    )

    OP_6F(0x0005, 0)

    Jump('loc_471')

    def _loc_46A(): pass

    label('loc_46A')

    OP_6F(0x0005, 60)

    def _loc_471(): pass

    label('loc_471')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046D, 2, 0x236A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_483',
    )

    OP_6F(0x0006, 0)

    Jump('loc_48A')

    def _loc_483(): pass

    label('loc_483')

    OP_6F(0x0006, 60)

    def _loc_48A(): pass

    label('loc_48A')

    OP_E0(0x01, 0x14, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1C, 0xB8, 0xFE, 0xFF)
    OP_E0(0x02, 0x0A, 0xF6, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x1C, 0xB8, 0xFE, 0xFF)
    OP_E0(0x03, 0x92, 0x09, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x12, 0xB8, 0xFE, 0xFF)
    OP_E0(0x04, 0x04, 0x29, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x8A, 0x90, 0xFE, 0xFF)
    OP_E0(0x05, 0x04, 0x29, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x6C, 0x86, 0xFE, 0xFF)
    OP_E0(0x06, 0x04, 0x29, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x62, 0x9A, 0xFE, 0xFF)
    OP_10(0x13, 0x00)
    OP_82(0x84, 0x00)
    OP_82(0x85, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 3, 0x223B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 1, 0x2239)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 6, 0x2236)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 3, 0x2233)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_505',
    )

    OP_10(0x16, 0x01)
    OP_1B(0x16, 0x00, 0x0010)

    Jump('loc_50B')

    def _loc_505(): pass

    label('loc_505')

    OP_10(0x16, 0x00)
    OP_82(0x83, 0x00)

    def _loc_50B(): pass

    label('loc_50B')

    OP_22(0x0140, 0x00, 0x64)

    Return()

# id: 0x0002 offset: 0x511
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0x2A, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046C, 4, 0x2364)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5EE',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['长桶Ⅲ'], 1)"),
            Expr.Return,
        ),
        'loc_585',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['长桶Ⅲ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x2364)

    Jump('loc_5EB')

    def _loc_585(): pass

    label('loc_585')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['长桶Ⅲ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['长桶Ⅲ']),
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

    def _loc_5EB(): pass

    label('loc_5EB')

    Jump('loc_61F')

    def _loc_5EE(): pass

    label('loc_5EE')

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
    def _loc_61F(): pass

    label('loc_61F')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x62D
@scena.Code('func_03_62D')
def func_03_62D():
    UnlockAchievement(0x02, 0x2B, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046C, 6, 0x2366)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_70A',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['全回复药'], 1)"),
            Expr.Return,
        ),
        'loc_6A1',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x2366)

    Jump('loc_707')

    def _loc_6A1(): pass

    label('loc_6A1')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)

    def _loc_707(): pass

    label('loc_707')

    Jump('loc_73B')

    def _loc_70A(): pass

    label('loc_70A')

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
    def _loc_73B(): pass

    label('loc_73B')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x749
@scena.Code('func_04_749')
def func_04_749():
    UnlockAchievement(0x02, 0x2C, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046C, 7, 0x2367)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_826',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0003, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['全回复药'], 1)"),
            Expr.Return,
        ),
        'loc_7BD',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x2367)

    Jump('loc_823')

    def _loc_7BD(): pass

    label('loc_7BD')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0x00000000)

    def _loc_823(): pass

    label('loc_823')

    Jump('loc_857')

    def _loc_826(): pass

    label('loc_826')

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
    def _loc_857(): pass

    label('loc_857')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x865
@scena.Code('func_05_865')
def func_05_865():
    UnlockAchievement(0x02, 0x2D, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046D, 0, 0x2368)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_942',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0004, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['还魂胶囊'], 1)"),
            Expr.Return,
        ),
        'loc_8D9',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['还魂胶囊']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x2368)

    Jump('loc_93F')

    def _loc_8D9(): pass

    label('loc_8D9')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['还魂胶囊']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['还魂胶囊']),
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

    def _loc_93F(): pass

    label('loc_93F')

    Jump('loc_973')

    def _loc_942(): pass

    label('loc_942')

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
    def _loc_973(): pass

    label('loc_973')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x981
@scena.Code('func_06_981')
def func_06_981():
    UnlockAchievement(0x02, 0x2E, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046D, 1, 0x2369)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A5E',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0005, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_9F5',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x2369)

    Jump('loc_A5B')

    def _loc_9F5(): pass

    label('loc_9F5')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['复苏药']),
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

    def _loc_A5B(): pass

    label('loc_A5B')

    Jump('loc_A8F')

    def _loc_A5E(): pass

    label('loc_A5E')

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
    def _loc_A8F(): pass

    label('loc_A8F')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xA9D
@scena.Code('func_07_A9D')
def func_07_A9D():
    UnlockAchievement(0x02, 0x2F, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046D, 2, 0x236A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B7A',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0006, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['土人偶'], 1)"),
            Expr.Return,
        ),
        'loc_B11',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['土人偶']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x236A)

    Jump('loc_B77')

    def _loc_B11(): pass

    label('loc_B11')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['土人偶']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['土人偶']),
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

    def _loc_B77(): pass

    label('loc_B77')

    Jump('loc_BAB')

    def _loc_B7A(): pass

    label('loc_B7A')

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
    def _loc_BAB(): pass

    label('loc_BAB')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xBB9
@scena.Code('func_08_BB9')
def func_08_BB9():
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
        'loc_BD0',
    )

    Call(0, 0x0011)
    Call(0, 0x0012)

    def _loc_BD0(): pass

    label('loc_BD0')

    OP_6D(-1440, 0, -89110, 0)
    OP_67(0, 10010, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(171000, 0)
    OP_6E(500, 0)
    SetChrPos(0x0101, 450, 0, -129370, 0)
    SetChrPos(0x0102, -740, 0, -129490, 0)
    SetChrPos(0x00F8, 450, 0, -130590, 0)
    SetChrPos(0x00F9, -760, 0, -130850, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_0C60')
    def lambda_0C60():
        OP_6D(80, 0, -129160, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0C60)

    @scena.Lambda('lambda_0C78')
    def lambda_0C78():
        OP_67(0, 6290, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0C78)

    @scena.Lambda('lambda_0C90')
    def lambda_0C90():
        OP_6C(159000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0C90)

    @scena.Lambda('lambda_0CA0')
    def lambda_0CA0():
        OP_6B(1980, 7000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0CA0)

    OP_C8(0x0080, 0x0046, 'C_PLAC27._CH', 0x01, 0x03E8)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D12',
    )

    ChrTalk(
        0x010B,
        (
            '#0090401297V#212F#5P这、这就是『中枢塔』的内部……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F55')

    def _loc_D12(): pass

    label('loc_D12')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D59',
    )

    ChrTalk(
        0x0108,
        (
            '#0080401298V#072F#5P这就是『中枢塔』的内部吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F55')

    def _loc_D59(): pass

    label('loc_D59')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DA0',
    )

    ChrTalk(
        0x0106,
        (
            '#0050401299V#057F#5P这就是『中枢塔』的内部啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F55')

    def _loc_DA0(): pass

    label('loc_DA0')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DEA',
    )

    ChrTalk(
        0x0104,
        (
            '#0040401300V#032F#5P喔……\n',
            '这就是『中枢塔』内部吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F55')

    def _loc_DEA(): pass

    label('loc_DEA')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E35',
    )

    ChrTalk(
        0x0110,
        (
            '#0110401301V<FIXME>#270Fこれが《中枢塔》の内部か……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F55')

    def _loc_E35(): pass

    label('loc_E35')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E84',
    )

    ChrTalk(
        0x0109,
        (
            '#0180401302V#1063F#5P啊～……\n',
            '这就是『中枢塔』的内部吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F55')

    def _loc_E84(): pass

    label('loc_E84')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EC9',
    )

    ChrTalk(
        0x0103,
        (
            '#0030401303V#022F#5P这就是『中枢塔』的内部……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F55')

    def _loc_EC9(): pass

    label('loc_EC9')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F0F',
    )

    ChrTalk(
        0x0105,
        (
            '#0060401304V#1163F#5P这就是『中枢塔』的内部……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F55')

    def _loc_F0F(): pass

    label('loc_F0F')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F55',
    )

    ChrTalk(
        0x010F,
        (
            '#0100401305V<FIXME>#172Fこれが《中枢塔》の内部……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F55(): pass

    label('loc_F55')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FA3',
    )

    ChrTalk(
        0x0107,
        (
            '#0070401306V#065F#5P简、简直是在巨大装置\n',
            '的内部一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1214')

    def _loc_FA3(): pass

    label('loc_FA3')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FF9',
    )

    ChrTalk(
        0x010F,
        (
            '#0100401307V<FIXME>#178Fまるで大きな装置の\n',
            '中にいるようだが……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1214')

    def _loc_FF9(): pass

    label('loc_FF9')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1046',
    )

    ChrTalk(
        0x0105,
        (
            '#0060401308V#1163F#5P简直是在巨大装置\n',
            '的内部一样呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1214')

    def _loc_1046(): pass

    label('loc_1046')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1092',
    )

    ChrTalk(
        0x0103,
        (
            '#0030401309V#022F#5P简直是在巨大装置\n',
            '的内部一样呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1214')

    def _loc_1092(): pass

    label('loc_1092')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10DF',
    )

    ChrTalk(
        0x0109,
        (
            '#0180401310V#1063F#5P简直是在巨大装置\n',
            '的内部一样呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1214')

    def _loc_10DF(): pass

    label('loc_10DF')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1133',
    )

    ChrTalk(
        0x0110,
        (
            '#0110401311V<FIXME>#270Fまるで大きな装置の\n',
            '内部のようだが……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1214')

    def _loc_1133(): pass

    label('loc_1133')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_117F',
    )

    ChrTalk(
        0x0104,
        (
            '#0040401312V#034F#5P简直是在巨大装置\n',
            '的内部一样呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1214')

    def _loc_117F(): pass

    label('loc_117F')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11CB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050401313V#555F#5P简直是在巨大装置\n',
            '的内部一样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1214')

    def _loc_11CB(): pass

    label('loc_11CB')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1214',
    )

    ChrTalk(
        0x0108,
        (
            '#0080401314V#072F#5P简直是在巨大装置\n',
            '的内部一样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1214(): pass

    label('loc_1214')

    ChrTalk(
        0x0101,
        (
            '#0010401315V#1002F#5P还有，那发光的液体\n',
            '到底是什么呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010401316V感觉正体不明的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020401317V#1035F#5P……或许是充满\n',
            '高压导力的液体……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020401318V#1042F看来最好不要\n',
            '用手直接触碰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_6D(10, 0, -131270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 10, 0, -131270, 0)
    SetChrPos(0x0001, 10, 0, -131270, 0)
    SetChrPos(0x0002, 10, 0, -131270, 0)
    SetChrPos(0x0003, 10, 0, -131270, 0)
    OP_A2(0x223C)
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x1372
@scena.Code('func_09_1372')
def func_09_1372():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_D2(0x002601EF, 0x002601F4, 0x0C)
    OP_D2(0x0027028E, 0x00270298, 0x0D)
    OP_D2(0x00270296, 0x002702A0, 0x0E)
    OP_D2(0x002601F0, 0x002601F5, 0x0F)
    OP_D2(0x002601F6, 0x002601FB, 0x10)
    OP_D2(0x00270080, 0x00270084, 0x11)
    OP_D2(0x00270176, 0x00270183, 0x12)
    OP_D2(0x00270178, 0x00270185, 0x13)
    OP_D2(0x002701DA, 0x002701DF, 0x14)
    OP_D2(0x002600C1, 0x002600C6, 0x15)
    OP_D2(0x00260157, 0x0026015C, 0x16)
    OP_D2(0x002701D0, 0x002701D5, 0x17)
    LoadEffect(0x00, 'battle\\\\mgaria0.eff')
    LoadEffect(0x01, 'monster\\\\msc0647a.eff')
    LoadEffect(0x02, 'monster\\\\msc0647b.eff')
    LoadEffect(0x03, 'scraft\\\\sc008_02.eff')
    LoadEffect(0x03, 'scraft\\\\sc008_02.eff')
    LoadEffect(0x04, 'monster\\\\ms31004a.eff')
    OP_6D(-101510, 30, -14160, 0)
    OP_67(0, 9190, -10000, 0)
    OP_6B(2190, 0)
    OP_6C(315000, 0)
    OP_6E(336, 0)
    SetChrFlags(0x0008, 0x0002)
    SetChrChipByIndex(0x0008, 12)
    SetChrChipByIndex(0x000A, 17)
    SetChrChipByIndex(0x0009, 20)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -99780, 110, -11120, 0)
    CreateThread(0x000D, 0x03, 0x00, 0x000C)
    OP_22(0x0085, 0x01, 0x46)
    FadeIn(1500, 0)

    @scena.Lambda('lambda_150E')
    def lambda_150E():
        OP_6D(-100630, 0, -4610, 6800)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_150E)

    @scena.Lambda('lambda_1526')
    def lambda_1526():
        OP_6B(2080, 6800)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1526)

    @scena.Lambda('lambda_1536')
    def lambda_1536():
        OP_9E(0x00FE, 0x00000032, 0x00000000, 0x00001388, 0x000001F4)
        Yield()

        Jump('lambda_1536')

    DispatchAsync2(0x0008, 0x0003, lambda_1536)

    OP_8E(0x0008, -99940, 0, -5160, 1000, 0x00)
    TerminateThread(0x0008, 0x03)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#0150420970V#1157F#6P……不可能……这不可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420971V如此事态……\n',
            '『盟主』的预言里并没有……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420972V#1156F……等……等一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420973V难、难道说…\n',
            '我也只是一枚试验用的棋子吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420974V#1157F哼……\n',
            '回去之后一定要问明白才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x000A, -99790, 0, 7790, 180)
    ClearChrFlags(0x000A, 0x0080)

    NpcTalk(
        0x000A,
        '青年的声音',
        (
            '#0180420975V#3P很抱歉，你已经没机会那么做了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_16E2')
    def lambda_16E2():
        OP_6D(-100880, 0, -790, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_16E2)

    @scena.Lambda('lambda_16FA')
    def lambda_16FA():
        OP_67(0, 5400, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_16FA)

    @scena.Lambda('lambda_1712')
    def lambda_1712():
        OP_6B(1660, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1712)

    @scena.Lambda('lambda_1722')
    def lambda_1722():
        OP_6E(534, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1722)

    OP_8E(0x000A, -99860, 0, 2410, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#0150420976V#1157F#6P凯文·格拉汉姆……\n',
            '你是什么时候来到这种地方的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420977V滚开……我可没时间\n',
            '理会你这种杂鱼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    ClearChrFlags(0x0008, 0x0002)
    SetChrFlags(0x0008, 0x0800)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 14)
    OP_0D()
    Sleep(300)

    SetChrChipByIndex(0x0008, 14)
    OP_99(0x0008, 0x00, 0x03, 0x000005DC)
    OP_22(0x00D8, 0x00, 0x64)
    OP_99(0x0008, 0x04, 0x09, 0x000005DC)
    PlayEffect(0x00, 0x00, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    Fade(500)
    SetChrChipByIndex(0x000A, 22)
    SetChrSubChip(0x000A, 0)
    Sleep(500)

    OP_22(0x00D8, 0x00, 0x64)
    SetChrSubChip(0x000A, 1)
    Sleep(1000)

    PlayEffect(0x01, 0x01, 0x000A, 0, 2800, 3000, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    OP_82(0x00, 0x02)
    PlayEffect(0x03, 0x02, 0x000A, 300, 1000, 550, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(700)

    PlayEffect(0x02, 0x03, 0x000A, 0, 0, 0, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0390, 0x00, 0x64)
    PlayEffect(0x04, 0x04, 0x000A, 0, 0, 0, 0, 0, 0, 2000, 4000, 2000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_82(0x01, 0x02)
    OP_82(0x03, 0x02)
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    ClearChrFlags(0x0008, 0x0800)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 13)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0150420978V#1156F……你……\n',
            '『魔眼』竟然对你无效！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420979V就算是星杯骑士，\n',
            '也不是你这种新手可以抵挡的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0099, 0x00, 0x64)
    OP_82(0x04, 0x02)
    Sleep(1000)

    Sleep(100)

    Fade(250)
    OP_22(0x00D8, 0x00, 0x64)
    SetChrChipByIndex(0x000A, 17)
    SetChrSubChip(0x000A, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0180420980V#1066F#2P啊～抱歉。\n',
            '之前说了个小小的谎。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180420981V#1060F我在骑士团排名第五位。\n',
            '所以像这类的场面早已见怪不怪了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180420982V#1075F不过，就算如此，\n',
            '也很难赢得了正常状态下的你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180420983V#1073F不过，出现『可乘之机』的话就另当别论了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420984V#1153F什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x03, 'map\\\\mp104_00.eff')
    Sleep(100)

    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrSubChip(0x000A, 0)
    SetChrChipByIndex(0x000A, 18)
    OP_0D()
    Sleep(500)

    SetChrChipByIndex(0x000A, 19)
    OP_99(0x000A, 0x00, 0x07, 0x00000BB8)

    @scena.Lambda('lambda_1BA3')
    def lambda_1BA3():
        OP_99(0x00FE, 0x07, 0x0D, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1BA3)

    Sleep(300)

    PlayEffect(0x03, 0x03, 0x000A, 0, 1050, 1550, 0, 0, 0, 500, 500, 500, 0x0008, 0, 500, 0, 0)
    OP_22(0x01F6, 0x00, 0x64)
    Sleep(200)

    OP_22(0x0151, 0x00, 0x64)
    SetChrFlags(0x0008, 0x0002)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 15)
    OP_99(0x0008, 0x00, 0x04, 0x000005DC)
    OP_9E(0x0008, 0x0000000F, 0x00000000, 0x0000012C, 0x00000FA0)
    OP_83(0x03, 0x02)
    OP_82(0x03, 0x00)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0150420985V#1157F唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0180420986V#1075F#2P……我真正的任务\n',
            '并不是调查什么『辉之环』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180420987V#1072F最恶的破戒僧，\n',
            '盖鲁格·怀斯曼——',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180420988V我是前来了结你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420989V#1151F呼呼……原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420990V不过，如果你以为这种程度的攻击，\n',
            '就能消灭我『白面』的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_9E(0x0008, 0x00000028, 0x00000000, 0x0000012C, 0x00001388)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 15)
    Sleep(500)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(250)

    OP_22(0x020C, 0x00, 0x64)

    @scena.Lambda('lambda_1DB3')
    def lambda_1DB3():
        OP_99(0x00FE, 0x05, 0x08, 0x000005DC)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1DB3)

    Sleep(150)

    CreateThread(0x000C, 0x00, 0x00, 0x000A)
    WaitForThreadExit(0x0008, 0x0000)
    Sleep(1000)

    OP_99(0x0008, 0x08, 0x0A, 0x00000320)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0150420991V#1153F#5P什……什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_22(0x0152, 0x01, 0x5A)
    OP_99(0x0008, 0x0B, 0x0F, 0x000001F4)
    OP_62(0x0008, 0x000000C8, 1800, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0150420992V#1156F#5P盐、『盐之桩』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420993V曾经将诺桑普里亚北部地区\n',
            '化为盐之海的禁断咒具……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420994V#1157F为了杀死我一个人，\n',
            '竟要会动用到这种东西……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrSubChip(0x000A, 0)
    SetChrChipByIndex(0x000A, 17)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0180420995V#1072F你的做法太过分了，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180420996V即使是中立的教会\n',
            '也已无法再继续坐视下去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180420997V老老实实地消失吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1F90')
    def lambda_1F90():
        OP_99(0x00FE, 0x10, 0x18, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1F90)

    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0150420998V#1158F#5P#3S#22A你……你这条可恨的走狗！！！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    WaitForThreadExit(0x0008, 0x0002)
    OP_23(0x0152)
    Sleep(1500)

    OP_62(0x000A, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x000A)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0180420999V#1072F#2P走狗吗……\n',
            '嗯，这话倒也说得没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180421000V#1076F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180421001V#1065F#2P约修亚，真羡慕你的运气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180421002V和我这种人不同，\n',
            '至少…你还有回头的机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    LoadEffect(0x01, 'map\\\\mp055_00.eff')
    LoadEffect(0x02, 'map\\\\mp105_00.eff')
    SetChrPos(0x0009, -102410, 0, -5240, 0)
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x0009, 0x0080)
    SetMessageWindowPos(70, 100, -1, -1)
    SetChrName('少年的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0190421003V#5P呼呼呼……\n',
            '这算是嫉妒吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_219F')
    def lambda_219F():
        OP_6D(-102500, 0, -550, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_219F)

    @scena.Lambda('lambda_21B7')
    def lambda_21B7():
        OP_67(0, 5200, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_21B7)

    @scena.Lambda('lambda_21CF')
    def lambda_21CF():
        OP_6B(1740, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_21CF)

    @scena.Lambda('lambda_21DF')
    def lambda_21DF():
        OP_6E(542, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_21DF)

    PlayEffect(0x01, 0x00, 0x0009, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x010A, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_222E')
    def lambda_222E():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_222E)

    WaitForThreadExit(0x0009, 0x0001)
    OP_82(0x00, 0x02)
    CreateThread(0x0009, 0x03, 0x00, 0x000B)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0190421004V#853F#5P星杯骑士第五位──\n',
            '『法外制裁者』凯文·格拉汉姆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190421005V#854F呵呵呵……\n',
            '果然如传闻中一般冷酷无情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0180421006V#1074F#2P你是……\n',
            '小丑吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180421007V#1072F不好意思……\n',
            '你来晚一步，他已经没救了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0190421008V#854F#5P呵呵……\n',
            '或许你已经听说了，\n',
            '我的任务仅仅是『观察』而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190421009V掌握计划的全过程，\n',
            '滴水不漏地向『盟主』报告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190421010V#853F教授的自毁灭亡也只是单纯的结果，\n',
            '并非能够防范的事态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0180421011V#1075F#2P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180421012V#1073F『噬身之蛇』……\n',
            '看来这组织里还充满许多的谜团啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0190421013V#854F#5P呵呵……\n',
            '你们骑士团不也是一样吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190421014V#853F好了……\n',
            '这下我的任务也结束了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190421015V失物也已经回收完毕，\n',
            '差不多是该回去的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0180421016V#1074F#2P什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2555')
    def lambda_2555():
        OP_6D(-101170, 0, -3010, 1200)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2555)

    @scena.Lambda('lambda_256D')
    def lambda_256D():
        OP_67(0, 4800, -10000, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_256D)

    OP_8C(0x0009, 90, 400)
    SetChrFlags(0x0009, 0x0002)
    SetChrChipByIndex(0x0009, 21)
    SetChrSubChip(0x0009, 0)
    OP_0D()
    WaitForThreadExit(0x0009, 0x0001)
    Sleep(500)

    Fade(500)

    @scena.Lambda('lambda_25AB')
    def lambda_25AB():
        OP_6B(1540, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_25AB)

    OP_99(0x0009, 0x01, 0x02, 0x000003E8)
    OP_22(0x00BC, 0x00, 0x64)
    OP_0D()
    Sleep(500)

    OP_22(0x0153, 0x00, 0x64)
    SetChrSubChip(0x0008, 25)
    Sleep(500)

    PlayEffect(0x02, 0x02, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x000007D0)

    @scena.Lambda('lambda_261E')
    def lambda_261E():
        OP_99(0x00FE, 0x08, 0x0F, 0x000005DC)
        Yield()

        Jump('lambda_261E')

    DispatchAsync2(0x000C, 0x0001, lambda_261E)

    Sleep(500)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_2652')
    def lambda_2652():
        OP_6B(1640, 5000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2652)

    PlayEffect(0x01, 0x00, 0x0009, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x010A, 0x00, 0x64)
    Sleep(200)

    PlayEffect(0x01, 0x01, 0x000C, 0, 0, 0, 0, 0, 0, 1300, 1000, 1300, 0x00FF, 0, 0, 0, 0)
    ClearChrFlags(0x0009, 0x0002)
    SetChrChipByIndex(0x0009, 20)
    SetChrSubChip(0x0009, 0)
    Sleep(500)

    OP_8C(0x0009, 0, 300)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0190421017V#851F啊哈哈！\n',
            '那么祝一切顺利！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190421018V希望以后\n',
            '有机会再见！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2749')
    def lambda_2749():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2749)

    Sleep(200)

    @scena.Lambda('lambda_2760')
    def lambda_2760():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2760)

    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x000C, 0x0001)
    OP_82(0x00, 0x02)
    OP_82(0x01, 0x02)
    CreateThread(0x0009, 0x03, 0x00, 0x000B)
    SetChrFlags(0x0009, 0x0080)
    Sleep(1500)

    @scena.Lambda('lambda_2793')
    def lambda_2793():
        OP_67(0, 5300, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2793)

    OP_8E(0x000A, -99850, 0, -3540, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0180421019V#1074F#5P失物……难道是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180421020V#1072F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180421021V#1065F算了……\n',
            '这已经超出我的任务权限了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180421022V#1067F得赶快和艾丝蒂尔\n',
            '他们会合才行啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x00000BB8)
    FadeOut(1500, 0, -1)
    OP_24(0x0085, 0x3C)
    Sleep(200)

    OP_24(0x0085, 0x32)
    Sleep(200)

    OP_24(0x0085, 0x28)
    Sleep(200)

    OP_24(0x0085, 0x1E)
    Sleep(200)

    OP_24(0x0085, 0x14)
    Sleep(200)

    OP_24(0x0085, 0x0A)
    Sleep(200)

    OP_23(0x0085)
    OP_0D()
    OP_21()
    Sleep(500)

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '……就这样，艾丝蒂尔等人\n',
            '在断断续续发生的摇晃中逃出了『中枢塔』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '或许是因为导力急剧下降的缘故，\n',
            '『光环轨道』变得完全无法使用……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔等人便通过地下道\n',
            '前往停泊在公园区域的埃尔赛尤号。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMapFlags(0x02000000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5208._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x29D6
@scena.Code('func_0A_29D6')
def func_0A_29D6():
    SetChrPos(0x00FE, -99300, 0, -4800, 0)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0002)
    SetChrFlags(0x00FE, 0x0800)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x000C, 16)
    OP_22(0x00D5, 0x00, 0x64)
    OP_99(0x00FE, 0x00, 0x05, 0x000003E8)

    Return()

# id: 0x000B offset: 0x2A0F
@scena.Code('func_0B_2A0F')
def func_0B_2A0F():
    Sleep(250)

    OP_24(0x010A, 0x5A)
    Sleep(250)

    OP_24(0x010A, 0x50)
    Sleep(250)

    OP_24(0x010A, 0x46)
    Sleep(250)

    OP_24(0x010A, 0x3C)
    Sleep(250)

    OP_24(0x010A, 0x32)
    Sleep(250)

    OP_24(0x010A, 0x28)
    Sleep(250)

    OP_24(0x010A, 0x1E)
    Sleep(250)

    OP_23(0x010A)

    Return()

# id: 0x000C offset: 0x2A57
@scena.Code('func_0C_2A57')
def func_0C_2A57():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2AA5',
    )

    OP_7C(0x00000028, 0x00000028, 0x000003E8, 0x00000320)
    Sleep(1800)

    OP_7C(0x00000014, 0x00000014, 0x000003E8, 0x00000514)
    Sleep(1600)

    OP_7C(0x0000001E, 0x0000001E, 0x000003E8, 0x000005DC)
    Sleep(2000)

    Jump('func_0C_2A57')

    def _loc_2AA5(): pass

    label('loc_2AA5')

    Return()

# id: 0x000D offset: 0x2AA6
@scena.Code('func_0D_2AA6')
def func_0D_2AA6():
    EventBegin(0x00)
    OP_A1(0x000B, 0x0000)
    SetChrPos(0x000B, 101980, -1750, 850, 0)
    Yield()
    Fade(1000)
    OP_6D(101980, 0, 850, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 102000, 0, 2000, 0)
    OP_89(0x0001, 103000, 0, 1000, 90)
    OP_89(0x0002, 101000, 0, 1000, 270)
    OP_89(0x0003, 102000, 0, 0, 180)
    OP_0D()
    SetMapFlags(0x00100000)
    OP_22(0x00EB, 0x00, 0x64)

    @scena.Lambda('lambda_2B56')
    def lambda_2B56():
        OP_8F(0x00FE, 101980, 65000, 850, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2B56)

    Sleep(500)

    @scena.Lambda('lambda_2B76')
    def lambda_2B76():
        OP_6D(101980, 35000, 850, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2B76)

    @scena.Lambda('lambda_2B8E')
    def lambda_2B8E():
        OP_67(0, 14000, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2B8E)

    @scena.Lambda('lambda_2BA6')
    def lambda_2BA6():
        OP_6C(335000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2BA6)

    Sleep(500)

    @scena.Lambda('lambda_2BBB')
    def lambda_2BBB():
        OP_8F(0x00FE, 101980, 65000, 850, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2BBB)

    Sleep(500)

    @scena.Lambda('lambda_2BDB')
    def lambda_2BDB():
        OP_8F(0x00FE, 101980, 65000, 850, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2BDB)

    Sleep(400)

    @scena.Lambda('lambda_2BFB')
    def lambda_2BFB():
        OP_8F(0x00FE, 101980, 65000, 850, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2BFB)

    Sleep(200)

    @scena.Lambda('lambda_2C1B')
    def lambda_2C1B():
        OP_8F(0x00FE, 101980, 65000, 850, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2C1B)

    Sleep(100)

    @scena.Lambda('lambda_2C3B')
    def lambda_2C3B():
        OP_8F(0x00FE, 101980, 65000, 850, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2C3B)

    Sleep(2000)

    Sleep(2000)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x228C)
    OP_A3(0x228D)
    OP_A3(0x228E)
    OP_A3(0x228F)
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

# id: 0x000E offset: 0x2C95
@scena.Code('func_0E_2C95')
def func_0E_2C95():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_A1(0x000B, 0x0000)
    SetChrPos(0x000B, 101980, 66000, 850, 0)
    Yield()
    OP_6D(101980, 48000, 850, 0)
    OP_67(0, 16000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(335000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 102000, 67000, 2000, 0)
    OP_89(0x0001, 103000, 67000, 1000, 90)
    OP_89(0x0002, 101000, 67000, 1000, 270)
    OP_89(0x0003, 102000, 67000, 0, 180)
    OP_22(0x00EB, 0x00, 0x64)

    @scena.Lambda('lambda_2D44')
    def lambda_2D44():
        OP_6D(101980, 0, 850, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2D44)

    @scena.Lambda('lambda_2D5C')
    def lambda_2D5C():
        OP_67(0, 9500, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2D5C)

    @scena.Lambda('lambda_2D74')
    def lambda_2D74():
        OP_6C(315000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2D74)

    FadeIn(1000, 0)
    SetPlaceName(0x011C)

    @scena.Lambda('lambda_2D90')
    def lambda_2D90():
        OP_8F(0x00FE, 101980, -1750, 850, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2D90)

    Sleep(3800)

    Sleep(4000)

    @scena.Lambda('lambda_2DB5')
    def lambda_2DB5():
        OP_8F(0x00FE, 101980, -1750, 850, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2DB5)

    Sleep(700)

    @scena.Lambda('lambda_2DD5')
    def lambda_2DD5():
        OP_8F(0x00FE, 101980, -1750, 850, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2DD5)

    Sleep(600)

    @scena.Lambda('lambda_2DF5')
    def lambda_2DF5():
        OP_8F(0x00FE, 101980, -1750, 850, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2DF5)

    Sleep(100)

    @scena.Lambda('lambda_2E15')
    def lambda_2E15():
        OP_8F(0x00FE, 101980, -1750, 850, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2E15)

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
    WaitForThreadExit(0x000B, 0x0001)
    Sleep(500)

    Fade(1000)
    SetChrPos(0x0000, 102080, 0, 5330, 0)
    SetChrPos(0x0001, 102080, 0, 5330, 0)
    SetChrPos(0x0002, 102080, 0, 5330, 0)
    SetChrPos(0x0003, 102080, 0, 5330, 0)
    OP_69(0x0000, 0x00000000)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x000F offset: 0x2EE6
@scena.Code('func_0F_2EE6')
def func_0F_2EE6():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(0, 1100, -94000, 0)
    SetChrPos(0x0101, 500, 1100, -94500, 180)
    SetChrPos(0x0102, -500, 1100, -94500, 180)
    SetChrPos(0x00F8, 500, 1100, -93500, 180)
    SetChrPos(0x00F9, -500, 1100, -93500, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    @scena.Lambda('lambda_2FC1')
    def lambda_2FC1():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2FC1)

    @scena.Lambda('lambda_2FD3')
    def lambda_2FD3():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_2FD3)

    @scena.Lambda('lambda_2FE5')
    def lambda_2FE5():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_2FE5)

    @scena.Lambda('lambda_2FF7')
    def lambda_2FF7():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_2FF7)

    Sleep(2500)

    Fade(500)
    OP_6D(0, 0, -97620, 0)
    SetChrPos(0x0000, 0, 0, -97620, 180)
    SetChrPos(0x0001, 0, 0, -97620, 180)
    SetChrPos(0x0002, 0, 0, -97620, 180)
    SetChrPos(0x0003, 0, 0, -97620, 180)
    EventEnd(0x00)

    Return()

# id: 0x0010 offset: 0x3065
@scena.Code('func_10_3065')
def func_10_3065():
    EventBegin(0x01)
    Fade(500)
    OP_6D(0, 1100, -94000, 0)
    SetChrPos(0x0101, -500, 1100, -93500, 0)
    SetChrPos(0x0102, 500, 1100, -93500, 0)
    SetChrPos(0x00F8, -500, 1100, -94500, 0)
    SetChrPos(0x00F9, 500, 1100, -94500, 0)
    OP_0D()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 3, 0x223B)),
            Expr.Return,
        ),
        'loc_3107',
    )

    OP_CC(0x01, 0x00, '【第５层】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_3107(): pass

    label('loc_3107')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 1, 0x2239)),
            Expr.Return,
        ),
        'loc_3126',
    )

    OP_CC(0x01, 0x00, '【第４层】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_3126(): pass

    label('loc_3126')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 6, 0x2236)),
            Expr.Return,
        ),
        'loc_3145',
    )

    OP_CC(0x01, 0x00, '【第３层】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_3145(): pass

    label('loc_3145')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 3, 0x2233)),
            Expr.Return,
        ),
        'loc_3164',
    )

    OP_CC(0x01, 0x00, '【第２层】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_3164(): pass

    label('loc_3164')

    OP_CC(0x01, 0x00, '【放弃】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    OP_CC(0x02, 0x00)
    MenuEnd(0x0000)
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_31AF',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3231')

    def _loc_31AF(): pass

    label('loc_31AF')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_31B9(): pass

    label('loc_31B9')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3231',
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31D3',
    )

    Jump('loc_3231')

    def _loc_31D3(): pass

    label('loc_31D3')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3224',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_320D',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Div2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_320A',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_320A(): pass

    label('loc_320A')

    Jump('loc_3224')

    def _loc_320D(): pass

    label('loc_320D')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Div2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_31D3')

    def _loc_3224(): pass

    label('loc_3224')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_31B9')

    def _loc_3231(): pass

    label('loc_3231')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x3),
            Expr.Leq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_32D4',
    )

    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    @scena.Lambda('lambda_328D')
    def lambda_328D():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_328D)

    @scena.Lambda('lambda_329F')
    def lambda_329F():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_329F)

    @scena.Lambda('lambda_32B1')
    def lambda_32B1():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_32B1)

    @scena.Lambda('lambda_32C3')
    def lambda_32C3():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_32C3)

    Sleep(2000)

    def _loc_32D4(): pass

    label('loc_32D4')

    Switch(
        (
            (Expr.PushReg, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_32ED'),
        (0x00000001, 'loc_32F9'),
        (0x00000002, 'loc_3305'),
        (0x00000003, 'loc_3311'),
        (-1, 'loc_331D'),
    )

    def _loc_32ED(): pass

    label('loc_32ED')

    NewScene('ED6_DT21/C5306._SN', 111, 0, 0)
    IdleLoop()

    Jump('loc_331D')

    def _loc_32F9(): pass

    label('loc_32F9')

    NewScene('ED6_DT21/C5305._SN', 116, 0, 0)
    IdleLoop()

    Jump('loc_331D')

    def _loc_3305(): pass

    label('loc_3305')

    NewScene('ED6_DT21/C5303._SN', 116, 0, 0)
    IdleLoop()

    Jump('loc_331D')

    def _loc_3311(): pass

    label('loc_3311')

    NewScene('ED6_DT21/C5301._SN', 115, 0, 0)
    IdleLoop()

    Jump('loc_331D')

    def _loc_331D(): pass

    label('loc_331D')

    Fade(500)
    OP_6D(0, 0, -97620, 0)
    SetChrPos(0x0000, 0, 0, -97620, 180)
    SetChrPos(0x0001, 0, 0, -97620, 180)
    SetChrPos(0x0002, 0, 0, -97620, 180)
    SetChrPos(0x0003, 0, 0, -97620, 180)
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x337A
@scena.Code('func_11_337A')
def func_11_337A():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
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
        (0x00000000, 'loc_33F4'),
        (0x00000001, 'loc_33FA'),
        (-1, 'loc_3400'),
    )

    def _loc_33F4(): pass

    label('loc_33F4')

    OP_A2(0x1200)

    Jump('loc_3400')

    def _loc_33FA(): pass

    label('loc_33FA')

    OP_A2(0x1201)

    Jump('loc_3400')

    def _loc_3400(): pass

    label('loc_3400')

    Return()

# id: 0x0012 offset: 0x3401
@scena.Code('func_12_3401')
def func_12_3401():
    FadeOut(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0x000A,
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
    OP_69(0x0000, 0x00000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
