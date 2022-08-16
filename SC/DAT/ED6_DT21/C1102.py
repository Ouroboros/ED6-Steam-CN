import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1102_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1102   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1102.x'
    header.mapIndex       = 1
    header.bgm            = 30
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/C1102_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH00162._CH', 'ED6_DT07/CH00162P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT09/CH10300._CH', 'ED6_DT09/CH10300P._CP'),
        ('ED6_DT09/CH10301._CH', 'ED6_DT09/CH10301P._CP'),
        ('ED6_DT27/CH03610._CH', 'ED6_DT27/CH03610P._CP'),
        ('ED6_DT27/CH03750._CH', 'ED6_DT27/CH03750P._CP'),
        ('ED6_DT29/CH12350._CH', 'ED6_DT29/CH12350P._CP'),
        ('ED6_DT29/CH12351._CH', 'ED6_DT29/CH12351P._CP'),
        ('ED6_DT29/CH12570._CH', 'ED6_DT29/CH12570P._CP'),
        ('ED6_DT29/CH12571._CH', 'ED6_DT29/CH12571P._CP'),
        ('ED6_DT29/CH12574._CH', 'ED6_DT29/CH12574P._CP'),
    ]

# id: 0x10001 offset: 0x102
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '哨兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x162
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -29330,
            z           = -500,
            y           = 36850,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0xC1,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0DAC,
            word_18     = 0x1A2A,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -84750,
            z           = -410,
            y           = 68560,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0xC1,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0DAC,
            word_18     = 0x1A2B,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 50700,
            z           = 0,
            y           = 57550,
            word_0C     = 0x00E1,
            word_0E     = 0x0006,
            byte_10     = 0xC1,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0DAC,
            word_18     = 0x1A2C,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 49810,
            z           = 0,
            y           = 10380,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0xC1,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0DAC,
            word_18     = 0x1A2D,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 75930,
            z           = -500,
            y           = 185910,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0xC1,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0DAD,
            word_18     = 0x1A2E,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1EE
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -46900,
            y           = -2000,
            z           = 26000,
            range       = -46100,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00007530,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000B,
        ),
    )

# id: 0x10004 offset: 0x20E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 7410,
            triggerZ            = 0,
            triggerY            = 43900,
            triggerRange        = 1000,
            actorX              = 6750,
            actorZ              = 0,
            actorY              = 43900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -75700,
            triggerZ            = 0,
            triggerY            = 30920,
            triggerRange        = 1000,
            actorX              = -75080,
            actorZ              = 0,
            actorY              = 30400,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -89670,
            triggerZ            = -250,
            triggerY            = 78010,
            triggerRange        = 1000,
            actorX              = -90330,
            actorZ              = -250,
            actorY              = 78140,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -80220,
            triggerZ            = -250,
            triggerY            = 76890,
            triggerRange        = 1000,
            actorX              = -79560,
            actorZ              = -250,
            actorY              = 76890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -41820,
            triggerZ            = -250,
            triggerY            = 99770,
            triggerRange        = 1000,
            actorX              = -41820,
            actorZ              = -250,
            actorY              = 99110,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -28930,
            triggerZ            = -130,
            triggerY            = 47490,
            triggerRange        = 1000,
            actorX              = -28930,
            actorZ              = 1500,
            actorY              = 47490,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -69290,
            triggerZ            = 0,
            triggerY            = 170530,
            triggerRange        = 1000,
            actorX              = -69860,
            actorZ              = 0,
            actorY              = 170530,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x30A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 7, 0x1A17)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_327',
    )

    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_08_BAC)

    Jump('loc_362')

    def _loc_327(): pass

    label('loc_327')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_346',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_09_BB8)

    Jump('loc_362')

    def _loc_346(): pass

    label('loc_346')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_362',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x10000000)
    Event(1, 0x0001)

    def _loc_362(): pass

    label('loc_362')

    If(
        (
            (Expr.Eval, "OP_29(0x007D, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x007D, 0x01, 0x0008)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x007D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x007D, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3C6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0345, 2, 0x1A2A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_392',
    )

    ChrClearFlags(0x000B, 0x0080)

    def _loc_392(): pass

    label('loc_392')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0345, 3, 0x1A2B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_39F',
    )

    ChrClearFlags(0x000C, 0x0080)

    def _loc_39F(): pass

    label('loc_39F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0345, 4, 0x1A2C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3AC',
    )

    ChrClearFlags(0x000D, 0x0080)

    def _loc_3AC(): pass

    label('loc_3AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0345, 5, 0x1A2D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3B9',
    )

    ChrClearFlags(0x000E, 0x0080)

    def _loc_3B9(): pass

    label('loc_3B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0345, 6, 0x1A2E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C6',
    )

    ChrClearFlags(0x000F, 0x0080)

    def _loc_3C6(): pass

    label('loc_3C6')

    Return()

# id: 0x0001 offset: 0x3C7
@scena.Code('func_01_3C7')
def func_01_3C7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0366, 3, 0x1B33)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D9',
    )

    OP_6F(0x0000, 0)

    Jump('loc_3E0')

    def _loc_3D9(): pass

    label('loc_3D9')

    OP_6F(0x0000, 60)

    def _loc_3E0(): pass

    label('loc_3E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0366, 4, 0x1B34)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F2',
    )

    OP_6F(0x0001, 0)

    Jump('loc_3F9')

    def _loc_3F2(): pass

    label('loc_3F2')

    OP_6F(0x0001, 60)

    def _loc_3F9(): pass

    label('loc_3F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0366, 5, 0x1B35)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_40B',
    )

    OP_6F(0x0002, 0)

    Jump('loc_412')

    def _loc_40B(): pass

    label('loc_40B')

    OP_6F(0x0002, 60)

    def _loc_412(): pass

    label('loc_412')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0366, 6, 0x1B36)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_424',
    )

    OP_6F(0x0003, 0)

    Jump('loc_42B')

    def _loc_424(): pass

    label('loc_424')

    OP_6F(0x0003, 60)

    def _loc_42B(): pass

    label('loc_42B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0366, 7, 0x1B37)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_43D',
    )

    OP_6F(0x0004, 0)

    Jump('loc_444')

    def _loc_43D(): pass

    label('loc_43D')

    OP_6F(0x0004, 60)

    def _loc_444(): pass

    label('loc_444')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0367, 0, 0x1B38)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_456',
    )

    OP_6F(0x0006, 0)

    Jump('loc_45D')

    def _loc_456(): pass

    label('loc_456')

    OP_6F(0x0006, 60)

    def _loc_45D(): pass

    label('loc_45D')

    OP_E0(0x03, 0x10, 0xC9, 0xFE, 0xFF, 0x38, 0xFF, 0xFF, 0xFF, 0x5A, 0x2C, 0x01, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_476',
    )

    OP_64(0x05, 0x0001)

    def _loc_476(): pass

    label('loc_476')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 7, 0x1A17)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_48A',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4C2')

    def _loc_48A(): pass

    label('loc_48A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 7, 0x1A17)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4AC',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x02000000)
    OP_1B(0x04, 0x00, 0x000D)

    Jump('loc_4C2')

    def _loc_4AC(): pass

    label('loc_4AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C2',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x56),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x02000000)

    def _loc_4C2(): pass

    label('loc_4C2')

    OP_10(0x00, 0x00)

    If(
        (
            (Expr.Eval, "OP_29(0x007D, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x007D, 0x01, 0x0008)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x007D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x007D, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_503',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0345, 2, 0x1A2A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0345, 3, 0x1A2B)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0345, 4, 0x1A2C)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0345, 5, 0x1A2D)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0345, 6, 0x1A2E)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_503',
    )

    Event(1, 0x0000)

    def _loc_503(): pass

    label('loc_503')

    Return()

# id: 0x0002 offset: 0x504
@scena.Code('func_02_504')
def func_02_504():
    UnlockAchievement(0x02, 0x002B, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0366, 3, 0x1B33)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5E1',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_578',
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
    SetScenaFlags(ScenaFlag(0x0366, 3, 0x1B33))

    Jump('loc_5DE')

    def _loc_578(): pass

    label('loc_578')

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

    def _loc_5DE(): pass

    label('loc_5DE')

    Jump('loc_612')

    def _loc_5E1(): pass

    label('loc_5E1')

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
    def _loc_612(): pass

    label('loc_612')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x620
@scena.Code('func_03_620')
def func_03_620():
    UnlockAchievement(0x02, 0x002C, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0366, 4, 0x1B34)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6FD',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_694',
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
    SetScenaFlags(ScenaFlag(0x0366, 4, 0x1B34))

    Jump('loc_6FA')

    def _loc_694(): pass

    label('loc_694')

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

    def _loc_6FA(): pass

    label('loc_6FA')

    Jump('loc_72E')

    def _loc_6FD(): pass

    label('loc_6FD')

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
    def _loc_72E(): pass

    label('loc_72E')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x73C
@scena.Code('func_04_73C')
def func_04_73C():
    UnlockAchievement(0x02, 0x002D, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0366, 5, 0x1B35)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_819',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['鲑鱼卵'], 1)"),
            Expr.Return,
        ),
        'loc_7B0',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['鲑鱼卵']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0366, 5, 0x1B35))

    Jump('loc_816')

    def _loc_7B0(): pass

    label('loc_7B0')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['鲑鱼卵']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['鲑鱼卵']),
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

    def _loc_816(): pass

    label('loc_816')

    Jump('loc_84A')

    def _loc_819(): pass

    label('loc_819')

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
    def _loc_84A(): pass

    label('loc_84A')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x858
@scena.Code('func_05_858')
def func_05_858():
    UnlockAchievement(0x02, 0x002E, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0366, 6, 0x1B36)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_935',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_8CC',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

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
    SetScenaFlags(ScenaFlag(0x0366, 6, 0x1B36))

    Jump('loc_932')

    def _loc_8CC(): pass

    label('loc_8CC')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_932(): pass

    label('loc_932')

    Jump('loc_966')

    def _loc_935(): pass

    label('loc_935')

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
    def _loc_966(): pass

    label('loc_966')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x974
@scena.Code('func_06_974')
def func_06_974():
    UnlockAchievement(0x02, 0x002F, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0366, 7, 0x1B37)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A51',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['百战百胜牛排'], 1)"),
            Expr.Return,
        ),
        'loc_9E8',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['百战百胜牛排']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0366, 7, 0x1B37))

    Jump('loc_A4E')

    def _loc_9E8(): pass

    label('loc_9E8')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['百战百胜牛排']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['百战百胜牛排']),
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

    def _loc_A4E(): pass

    label('loc_A4E')

    Jump('loc_A82')

    def _loc_A51(): pass

    label('loc_A51')

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
    def _loc_A82(): pass

    label('loc_A82')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xA90
@scena.Code('func_07_A90')
def func_07_A90():
    UnlockAchievement(0x02, 0x0030, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0367, 0, 0x1B38)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B6D',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0006, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['深红眼眸'], 1)"),
            Expr.Return,
        ),
        'loc_B04',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['深红眼眸']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0367, 0, 0x1B38))

    Jump('loc_B6A')

    def _loc_B04(): pass

    label('loc_B04')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['深红眼眸']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['深红眼眸']),
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

    def _loc_B6A(): pass

    label('loc_B6A')

    Jump('loc_B9E')

    def _loc_B6D(): pass

    label('loc_B6D')

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
    def _loc_B9E(): pass

    label('loc_B9E')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xBAC
@scena.Code('func_08_BAC')
def func_08_BAC():
    EventBegin(0x00)
    NewScene('ED6_DT21/C1103._SN', 107, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0xBB8
@scena.Code('func_09_BB8')
def func_09_BB8():
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
        'loc_BCB',
    )

    Call(0, 0x000C)

    def _loc_BCB(): pass

    label('loc_BCB')

    CameraMove(1020, 0, 6630, 0)
    OP_67(0, 8740, -10000, 0)
    CameraSetDistance(2670, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 430, 0, 6420, 0)
    ChrSetPos(0x0107, 1480, 0, 6290, 0)
    ChrSetPos(0x00F8, -160, 0, 5280, 0)
    ChrSetPos(0x00F9, 1570, 0, 5060, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070301131V#065F#5P阿、阿加特哥哥的声音！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301132V#1002F这个响声的方向\n',
            '似乎来自露天采掘场。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301133V#1005F总之赶快去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x000A offset: 0xCF2
@scena.Code('func_0A_CF2')
def func_0A_CF2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 0, 0x1A18)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_11F1',
    )

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
        'loc_D20',
    )

    Call(0, 0x000C)
    FadeIn(0, 0)
    Sleep(200)

    def _loc_D20(): pass

    label('loc_D20')

    Fade(1000)
    CameraMove(-29880, -430, 46640, 0)
    OP_67(0, 10510, -10000, 0)
    CameraSetDistance(2660, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -29170, -500, 45850, 0)
    ChrSetPos(0x0107, -30200, -500, 45730, 0)
    ChrSetPos(0x00F8, -30290, -500, 44420, 0)
    ChrSetPos(0x00F9, -29090, -500, 44350, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010301134V#1020F咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070301135V#065F#6P怎、怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301136V#1020F这里原本可以通往\n',
            '外面的露天采掘场才对……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301137V怎么被岩石堵住了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EA2',
    )

    ChrTalk(
        0x0105,
        (
            '#0060301138V#043F#6P搞不好，是龙发飙\n',
            '造成崩塌也不一定……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F3F')

    def _loc_EA2(): pass

    label('loc_EA2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EF2',
    )

    ChrTalk(
        0x0103,
        (
            '#0030301139V#022F#6P搞不好，是龙发飙\n',
            '造成崩塌也不一定呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F3F')

    def _loc_EF2(): pass

    label('loc_EF2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F3F',
    )

    ChrTalk(
        0x0104,
        (
            '#0040301140V#035F#6P搞不好，是龙发飙\n',
            '造成崩塌也不一定啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F3F(): pass

    label('loc_F3F')

    ChrTalk(
        0x0107,
        (
            '#0070301141V#062F#6P那，那就\n',
            '用我的导力炮！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(216, 0x00, 0x64)
    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0107, 0)
    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_0F90')
    def lambda_0F90():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F90)

    Sleep(100)

    @scena.Lambda('lambda_0FA3')
    def lambda_0FA3():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0FA3)

    Sleep(10)

    ChrTurnDirection(0x00F8, 0x0107, 400)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_101F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080301142V#072F#6P不，最好不要。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080301143V随便使其振动\n',
            '搞不好会塌得更厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10F6')

    def _loc_101F(): pass

    label('loc_101F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_108B',
    )

    ChrTalk(
        0x0104,
        (
            '#0040301144V#032F#6P不，最好不要吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040301145V随便使其振动\n',
            '搞不好会坍塌得更厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10F6')

    def _loc_108B(): pass

    label('loc_108B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10F6',
    )

    ChrTalk(
        0x0103,
        (
            '#0030301146V#022F#6P不，最好不要哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030301147V随便使其振动\n',
            '搞不好会坍塌得更厉害吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10F6(): pass

    label('loc_10F6')

    OP_62(0x0107, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070301148V#561F#6P啊、啊呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(216, 0x00, 0x64)
    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0107, 65535)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010301149V#1002F#4P提妲……\n',
            '我明白你的心情，不过镇定点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301150V总之先寻找别的途径吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070301151V#062F#5P嗯、嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0343, 0, 0x1A18))
    OP_28(0x0094, 0x01, 0x0020)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Jump('loc_1235')

    def _loc_11F1(): pass

    label('loc_11F1')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '出口被岩石堵住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)
    def _loc_1235(): pass

    label('loc_1235')

    Return()

# id: 0x000B offset: 0x1236
@scena.Code('func_0B_1236')
def func_0B_1236():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 1, 0x1A19)),
            Expr.Return,
        ),
        'loc_123E',
    )

    Return()

    def _loc_123E(): pass

    label('loc_123E')

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
        'loc_125F',
    )

    Call(0, 0x000C)
    FadeIn(0, 0)
    Sleep(200)

    def _loc_125F(): pass

    label('loc_125F')

    Fade(1000)
    CameraMove(-48350, 50, 28560, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -47490, 50, 28410, 270)
    ChrSetPos(0x0107, -47470, 50, 27380, 270)
    ChrSetPos(0x00F8, -46180, 50, 28740, 270)
    ChrSetPos(0x00F9, -45960, 0, 27320, 270)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010301152V#1004F#6P咦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301153V这里的桥，之前来的时候\n',
            '好像是坏掉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13B3',
    )

    ChrTalk(
        0x0103,
        (
            '#0030301154V#022F#6P记得听说空贼事件以后，\n',
            '军方把它修复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301155V#1015F#6P这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1491')

    def _loc_13B3(): pass

    label('loc_13B3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1424',
    )

    ChrTalk(
        0x0105,
        (
            '#0060301156V#042F#6P搞不好是王国军\n',
            '修复了也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301157V#1015F#6P原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1491')

    def _loc_1424(): pass

    label('loc_1424')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1491',
    )

    ChrTalk(
        0x0104,
        (
            '#0040301158V#035F#6P唔，搞不好\n',
            '是军队修复了也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301159V#1015F原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1491(): pass

    label('loc_1491')

    SetScenaFlags(ScenaFlag(0x0343, 1, 0x1A19))
    OP_28(0x0094, 0x01, 0x0040)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x000C offset: 0x14A2
@scena.Code('func_0C_14A2')
def func_0C_14A2():
    FadeOut(0, 0, -1)
    CameraMove(-41010, -360, 62470, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(32000, 0)
    OP_6E(262, 0)
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
        (0x00000000, 'loc_1559'),
        (0x00000001, 'loc_155F'),
        (-1, 'loc_1565'),
    )

    def _loc_1559(): pass

    label('loc_1559')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_1565')

    def _loc_155F(): pass

    label('loc_155F')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_1565')

    def _loc_1565(): pass

    label('loc_1565')

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['提妲'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
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

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

# id: 0x000D offset: 0x159F
@scena.Code('func_0D_159F')
def func_0D_159F():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15EB',
    )

    ChrTalk(
        0x0101,
        (
            '#0010301160V#1002F阿加特就在里面……\n',
            '总之现在赶快吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_173F')

    def _loc_15EB(): pass

    label('loc_15EB')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_162C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030301161V#022F阿加特就在里面。\n',
            '赶快去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_173F')

    def _loc_162C(): pass

    label('loc_162C')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_166D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060301162V#042F阿加特就在里面。\n',
            '赶快去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_173F')

    def _loc_166D(): pass

    label('loc_166D')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16AE',
    )

    ChrTalk(
        0x0104,
        (
            '#0040301163V#032F阿加特就在里面。\n',
            '赶快去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_173F')

    def _loc_16AE(): pass

    label('loc_16AE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16F7',
    )

    ChrTalk(
        0x0107,
        (
            '#0070301164V#065F阿加特就在里面……\n',
            '要、要赶快才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_173F')

    def _loc_16F7(): pass

    label('loc_16F7')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_173F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080301165V#072F阿加特就在里面。\n',
            '总之这就赶快前进吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_173F(): pass

    label('loc_173F')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
