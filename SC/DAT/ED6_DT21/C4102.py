import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C4102_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4102   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '艾尔贝离宫方向'),
    TXT(0x02, '庭园大道方向'),
    TXT(0x03, '丘陵毒蜂'),
    TXT(0x04, '鳄鱼'),
    TXT(0x05, '鳄鱼'),
    TXT(0x06, '沼泽剑齿吸血魔'),
    TXT(0x07, '迅猛小鹫'),
    TXT(0x08, '丘陵毒蜂'),
    TXT(0x09, '地狱火爆麻雀'),
    TXT(0x0A, '地狱火爆麻雀'),
    TXT(0x0B, '好战蝙蝠'),
    TXT(0x0C, '凶暴巨鳄'),
    TXT(0x0D, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4102.x'
    header.mapIndex       = 1
    header.bgm            = 21
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x809
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
        ('ED6_DT09/CH10780._CH', 'ED6_DT09/CH10780P._CP'),
        ('ED6_DT09/CH10781._CH', 'ED6_DT09/CH10781P._CP'),
        ('ED6_DT09/CH10790._CH', 'ED6_DT09/CH10790P._CP'),
        ('ED6_DT09/CH10791._CH', 'ED6_DT09/CH10791P._CP'),
        ('ED6_DT09/CH10050._CH', 'ED6_DT09/CH10050P._CP'),
        ('ED6_DT09/CH10051._CH', 'ED6_DT09/CH10051P._CP'),
        ('ED6_DT09/CH10800._CH', 'ED6_DT09/CH10800P._CP'),
        ('ED6_DT09/CH10801._CH', 'ED6_DT09/CH10801P._CP'),
        ('ED6_DT09/CH10810._CH', 'ED6_DT09/CH10810P._CP'),
        ('ED6_DT09/CH10811._CH', 'ED6_DT09/CH10811P._CP'),
        ('ED6_DT09/CH10820._CH', 'ED6_DT09/CH10820P._CP'),
        ('ED6_DT09/CH10821._CH', 'ED6_DT09/CH10821P._CP'),
        ('ED6_DT09/CH11220._CH', 'ED6_DT09/CH11220P._CP'),
        ('ED6_DT09/CH11221._CH', 'ED6_DT09/CH11221P._CP'),
        ('ED6_DT09/CH11230._CH', 'ED6_DT09/CH11230P._CP'),
        ('ED6_DT09/CH11231._CH', 'ED6_DT09/CH11231P._CP'),
    ]

# id: 0x10002 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 77370,
            z                   = 0,
            y                   = -15080,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -79490,
            z                   = 0,
            y                   = 4930,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x16A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 29090,
            z           = 110,
            y           = -28620,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0259,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 35270,
            z           = 0,
            y           = -43590,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x025D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 34970,
            z           = 100,
            y           = -63310,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x025D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 4820,
            z           = 100,
            y           = -79050,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x025B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 5370,
            z           = 120,
            y           = -58670,
            word_0C     = 0x0000,
            word_0E     = 0x000E,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0260,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 12310,
            z           = 10,
            y           = 7720,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0259,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 34490,
            z           = 40,
            y           = 31600,
            word_0C     = 0x0000,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x025F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 21340,
            z           = 10,
            y           = 64120,
            word_0C     = 0x0000,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x025F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 32640,
            z           = 90,
            y           = 49450,
            word_0C     = 0x0000,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x025E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -6330,
            z           = 140,
            y           = 2330,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x025C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x282
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x282
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 480,
            triggerZ            = 0,
            triggerY            = -67940,
            triggerRange        = 1000,
            actorX              = 1140,
            actorZ              = 0,
            actorY              = -67940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 13310,
            triggerZ            = -30,
            triggerY            = 61150,
            triggerRange        = 1000,
            actorX              = 12570,
            actorZ              = -30,
            actorY              = 61290,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 7430,
            triggerZ            = 30,
            triggerY            = -17940,
            triggerRange        = 1000,
            actorX              = 7020,
            actorZ              = 30,
            actorY              = -18340,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 24020,
            triggerZ            = 500,
            triggerY            = 54480,
            triggerRange        = 1500,
            actorX              = 24020,
            actorZ              = 4000,
            actorY              = 54480,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3540,
            triggerZ            = 500,
            triggerY            = -67980,
            triggerRange        = 1500,
            actorX              = 3540,
            actorZ              = 4000,
            actorY              = -67980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x336
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_378',
    )

    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)

    def _loc_378(): pass

    label('loc_378')

    Return()

# id: 0x0001 offset: 0x379
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE17B8, 0xFFFDE8D8, 0x00230065)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 5, 0x1625)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3C9',
    )

    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)

    def _loc_3C9(): pass

    label('loc_3C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E0, 3, 0x1703)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DB',
    )

    OP_6F(0x0000, 0)

    Jump('loc_3E2')

    def _loc_3DB(): pass

    label('loc_3DB')

    OP_6F(0x0000, 60)

    def _loc_3E2(): pass

    label('loc_3E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E0, 5, 0x1705)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F4',
    )

    OP_6F(0x0001, 0)

    Jump('loc_3FB')

    def _loc_3F4(): pass

    label('loc_3F4')

    OP_6F(0x0001, 60)

    def _loc_3FB(): pass

    label('loc_3FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E0, 7, 0x1707)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_40D',
    )

    OP_6F(0x0002, 0)

    Jump('loc_414')

    def _loc_40D(): pass

    label('loc_40D')

    OP_6F(0x0002, 60)

    def _loc_414(): pass

    label('loc_414')

    OP_E0(0x00, 0xF4, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x9C, 0xF6, 0xFE, 0xFF)

    Return()

# id: 0x0002 offset: 0x423
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0xFA, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E0, 3, 0x1703)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_500',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['防御３'], 1)"),
            Expr.Return,
        ),
        'loc_497',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['防御３']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1703)

    Jump('loc_4FD')

    def _loc_497(): pass

    label('loc_497')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['防御３']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['防御３']),
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

    def _loc_4FD(): pass

    label('loc_4FD')

    Jump('loc_531')

    def _loc_500(): pass

    label('loc_500')

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
    def _loc_531(): pass

    label('loc_531')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x53F
@scena.Code('func_03_53F')
def func_03_53F():
    UnlockAchievement(0x02, 0xFB, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E0, 5, 0x1705)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_61C',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['死之刃２'], 1)"),
            Expr.Return,
        ),
        'loc_5B3',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['死之刃２']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1705)

    Jump('loc_619')

    def _loc_5B3(): pass

    label('loc_5B3')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['死之刃２']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['死之刃２']),
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

    def _loc_619(): pass

    label('loc_619')

    Jump('loc_64D')

    def _loc_61C(): pass

    label('loc_61C')

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
    def _loc_64D(): pass

    label('loc_64D')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x65B
@scena.Code('func_04_65B')
def func_04_65B():
    UnlockAchievement(0x02, 0xFC, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E0, 7, 0x1707)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_738',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_6CF',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1707)

    Jump('loc_735')

    def _loc_6CF(): pass

    label('loc_6CF')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)

    def _loc_735(): pass

    label('loc_735')

    Jump('loc_769')

    def _loc_738(): pass

    label('loc_738')

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
    def _loc_769(): pass

    label('loc_769')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x777
@scena.Code('func_05_777')
def func_05_777():
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '竖立着古老的苍耀石石碑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0006 offset: 0x7B9
@scena.Code('func_06_7B9')
def func_06_7B9():
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '竖立着古老的红耀石石碑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
