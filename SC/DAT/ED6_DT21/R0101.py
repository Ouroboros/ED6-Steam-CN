import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R0101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R0101   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '雾调整'),
    TXT(0x02, '洛连特方向'),
    TXT(0x03, '格鲁纳门方向'),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
    TXT(0x09, ''),
    TXT(0x0A, ''),
    TXT(0x0B, ''),
    TXT(0x0C, ''),
    TXT(0x0D, ''),
    TXT(0x0E, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'R0101.x'
    header.mapIndex       = 23
    header.bgm            = 29
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1934
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
        ('ED6_DT09/CH10240._CH', 'ED6_DT09/CH10240P._CP'),
        ('ED6_DT09/CH10241._CH', 'ED6_DT09/CH10241P._CP'),
        ('ED6_DT09/CH10230._CH', 'ED6_DT09/CH10230P._CP'),
        ('ED6_DT09/CH10231._CH', 'ED6_DT09/CH10231P._CP'),
    ]

# id: 0x10002 offset: 0xCA
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
            npcIndex            = 0x0189,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -35110,
            z                   = 1000,
            y                   = 185500,
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
            x                   = -122810,
            z                   = 1000,
            y                   = -720,
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

# id: 0x10003 offset: 0x12A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -32000,
            z           = 1000,
            y           = 154000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0016,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -42000,
            z           = 1400,
            y           = 142000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0017,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -28000,
            z           = 2000,
            y           = 120000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0018,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -47000,
            z           = 1000,
            y           = 122000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0014,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -55000,
            z           = 1000,
            y           = 106000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0015,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -33000,
            z           = 1000,
            y           = 109000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0016,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -83000,
            z           = 2000,
            y           = 84900,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0017,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -94000,
            z           = 1000,
            y           = 62000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0018,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -106000,
            z           = 1000,
            y           = 42000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0014,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -125000,
            z           = 1000,
            y           = 34000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0015,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x242
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x242
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -126160,
            triggerZ            = 1030,
            triggerY            = 32310,
            triggerRange        = 1000,
            actorX              = -126630,
            actorZ              = 1030,
            actorY              = 32530,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -24690,
            triggerZ            = 2009,
            triggerY            = 123260,
            triggerRange        = 1000,
            actorX              = -24030,
            actorZ              = 2000,
            actorY              = 123440,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -91280,
            triggerZ            = 970,
            triggerY            = 78610,
            triggerRange        = 1000,
            actorX              = -96410,
            actorZ              = -500,
            actorY              = 77750,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2AE
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 6, 0x180E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 7, 0x180F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 0, 0x1810)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2C8',
    )

    Event(0, 0x0007)

    Jump('loc_2DE')

    def _loc_2C8(): pass

    label('loc_2C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 7, 0x180F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 0, 0x1810)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2DA',
    )

    Event(0, 0x0006)

    Jump('loc_2DE')

    def _loc_2DA(): pass

    label('loc_2DA')

    Event(0, 0x0005)

    def _loc_2DE(): pass

    label('loc_2DE')

    Return()

# id: 0x0001 offset: 0x2DF
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFD0260, 0xFFFF63C0, 0x00230009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0322, 0, 0x1910)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_303',
    )

    OP_6F(0x0000, 0)

    Jump('loc_30A')

    def _loc_303(): pass

    label('loc_303')

    OP_6F(0x0000, 60)

    def _loc_30A(): pass

    label('loc_30A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0322, 1, 0x1911)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31C',
    )

    OP_6F(0x0001, 0)

    Jump('loc_323')

    def _loc_31C(): pass

    label('loc_31C')

    OP_6F(0x0001, 60)

    def _loc_323(): pass

    label('loc_323')

    OP_82(0x80, 0x00)
    OP_82(0x81, 0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_35A',
    )

    SetMapFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0x00000000, 0x0000EA60, 0x00000000)
    OP_C4(0x00, 0x00000004)

    Jump('loc_3DB')

    def _loc_35A(): pass

    label('loc_35A')

    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_11(0xE6, 0xF0, 0xFF, 0x00000000, 0x00013880, 0x00000000)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)

    def _loc_3DB(): pass

    label('loc_3DB')

    Return()

# id: 0x0002 offset: 0x3DC
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_471',
    )

    ExecExpressionWithVar(
        0x37,
        (
            (Expr.PushLong, 0x28C58),
            (Expr.PushValueByIndex, 0x67),
            Expr.Sub,
            (Expr.PushLong, 0x5),
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x37),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_40F',
    )

    ExecExpressionWithVar(
        0x37,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_424')

    def _loc_40F(): pass

    label('loc_40F')

    If(
        (
            (Expr.PushValueByIndex, 0x37),
            (Expr.PushLong, 0x7D00),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_424',
    )

    ExecExpressionWithVar(
        0x37,
        (
            (Expr.PushLong, 0x7D00),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_424(): pass

    label('loc_424')

    ExecExpressionWithVar(
        0x38,
        (
            (Expr.PushLong, 0x28C58),
            (Expr.PushValueByIndex, 0x67),
            Expr.Sub,
            (Expr.PushLong, 0x5),
            Expr.Mul,
            (Expr.PushLong, 0x13880),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x38),
            (Expr.PushLong, 0x13880),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_454',
    )

    ExecExpressionWithVar(
        0x38,
        (
            (Expr.PushLong, 0x13880),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_469')

    def _loc_454(): pass

    label('loc_454')

    If(
        (
            (Expr.PushValueByIndex, 0x38),
            (Expr.PushLong, 0x222E0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_469',
    )

    ExecExpressionWithVar(
        0x38,
        (
            (Expr.PushLong, 0x222E0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_469(): pass

    label('loc_469')

    Sleep(10)

    Jump('ReInit')

    def _loc_471(): pass

    label('loc_471')

    Return()

# id: 0x0003 offset: 0x472
@scena.Code('func_03_472')
def func_03_472():
    UnlockAchievement(0x02, 0xBD, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0322, 0, 0x1910)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_54F',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['清醒之药'], 1)"),
            Expr.Return,
        ),
        'loc_4E6',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1910)

    Jump('loc_54C')

    def _loc_4E6(): pass

    label('loc_4E6')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['清醒之药']),
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

    def _loc_54C(): pass

    label('loc_54C')

    Jump('loc_580')

    def _loc_54F(): pass

    label('loc_54F')

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
    def _loc_580(): pass

    label('loc_580')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x58E
@scena.Code('func_04_58E')
def func_04_58E():
    UnlockAchievement(0x02, 0xBE, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0322, 1, 0x1911)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_66B',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['封魔之刃'], 1)"),
            Expr.Return,
        ),
        'loc_602',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['封魔之刃']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1911)

    Jump('loc_668')

    def _loc_602(): pass

    label('loc_602')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['封魔之刃']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['封魔之刃']),
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

    def _loc_668(): pass

    label('loc_668')

    Jump('loc_69C')

    def _loc_66B(): pass

    label('loc_66B')

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
    def _loc_69C(): pass

    label('loc_69C')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x6AA
@scena.Code('func_05_6AA')
def func_05_6AA():
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
        'loc_6D4',
    )

    Call(0, 0x0009)
    FadeIn(0, 0)
    Call(0, 0x000A)

    def _loc_6D4(): pass

    label('loc_6D4')

    OP_6D(-34830, 1000, 170380, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x000B, 0x0080)
    SetChrPos(0x0101, -35500, 1000, 180520, 180)
    SetChrPos(0x0103, -34500, 1000, 180520, 180)
    SetChrPos(0x00F8, -35750, 1000, 181520, 180)
    SetChrPos(0x00F9, -34250, 1000, 181520, 180)

    @scena.Lambda('lambda_0760')
    def lambda_0760():
        OP_90(0x00FE, 0, 0, -10000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0760)

    Sleep(100)

    @scena.Lambda('lambda_0780')
    def lambda_0780():
        OP_90(0x00FE, 0, 0, -10000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0780)

    Sleep(200)

    @scena.Lambda('lambda_07A0')
    def lambda_07A0():
        OP_90(0x00FE, 0, 0, -9500, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_07A0)

    Sleep(100)

    @scena.Lambda('lambda_07C0')
    def lambda_07C0():
        OP_90(0x00FE, 0, 0, -9500, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_07C0)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x00F9, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010281243V#1004F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_080B')
    def lambda_080B():
        OP_8E(0x00FE, -35810, 1000, 162970, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_080B)

    Sleep(100)

    @scena.Lambda('lambda_082B')
    def lambda_082B():
        OP_8E(0x00FE, -34540, 1000, 162830, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_082B)

    Sleep(200)

    @scena.Lambda('lambda_084B')
    def lambda_084B():
        OP_8E(0x00FE, -35850, 1000, 164520, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_084B)

    Sleep(100)

    @scena.Lambda('lambda_086B')
    def lambda_086B():
        OP_8E(0x00FE, -34380, 1000, 164570, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_086B)

    @scena.Lambda('lambda_0886')
    def lambda_0886():
        OP_6D(-34940, 1000, 163860, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0886)

    @scena.Lambda('lambda_089E')
    def lambda_089E():
        OP_6B(3370, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_089E)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0103, 0x0001)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    OP_8C(0x0101, 180, 400)
    Sleep(50)

    OP_8C(0x0103, 245, 400)
    Sleep(30)

    OP_8C(0x00F8, 155, 400)
    Sleep(50)

    OP_8C(0x00F9, 180, 400)
    Sleep(300)

    OP_8C(0x0101, 180, 400)
    Sleep(50)

    OP_8C(0x0103, 245, 400)
    Sleep(30)

    OP_8C(0x00F8, 245, 400)
    Sleep(50)

    OP_8C(0x00F9, 155, 400)
    Sleep(300)

    OP_8C(0x0101, 245, 400)
    Sleep(50)

    OP_8C(0x0103, 180, 400)
    Sleep(30)

    OP_8C(0x00F8, 270, 400)
    Sleep(50)

    OP_8C(0x00F9, 0, 400)
    Sleep(300)

    OP_8C(0x0101, 0, 400)
    Sleep(50)

    OP_8C(0x0103, 0, 400)
    Sleep(30)

    OP_8C(0x00F8, 180, 400)
    Sleep(50)

    OP_8C(0x00F9, 180, 400)
    Sleep(300)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x00F9, 0x0001)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9C6',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281162V#560F哇……\n',
            '一下子就明朗了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ABF')

    def _loc_9C6(): pass

    label('loc_9C6')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A04',
    )

    ChrTalk(
        0x0106,
        (
            '#0050281163V#051F嘿……\n',
            '突然就明朗了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ABF')

    def _loc_A04(): pass

    label('loc_A04')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A44',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281164V#030F嗯……\n',
            '一下子就明朗了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ABF')

    def _loc_A44(): pass

    label('loc_A44')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A84',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281165V#048F呵呵……\n',
            '忽然就明朗了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ABF')

    def _loc_A84(): pass

    label('loc_A84')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ABF',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281166V#070F呼……\n',
            '突然就明朗了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ABF(): pass

    label('loc_ABF')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B07',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281167V#061F雾的覆盖范围\n',
            '似乎就到这里为止呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C24')

    def _loc_B07(): pass

    label('loc_B07')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B4F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050281168V#051F雾的覆盖范围\n',
            '似乎就到这里为止啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C24')

    def _loc_B4F(): pass

    label('loc_B4F')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B97',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281169V#030F雾的覆盖范围\n',
            '似乎就到这里为止啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C24')

    def _loc_B97(): pass

    label('loc_B97')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BDF',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281170V#048F雾的覆盖范围\n',
            '似乎就到这里为止呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C24')

    def _loc_BDF(): pass

    label('loc_BDF')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C24',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281171V#070F雾的覆盖范围\n',
            '似乎就到这里为止啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C24(): pass

    label('loc_C24')

    ChrTalk(
        0x0103,
        (
            '#0030281254V#026F艾利兹街道，距离洛连特\n',
            '大约６０塞尔矩的地点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281255V#020F雾的范围内也没有魔兽，\n',
            '应该可以确保安全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281256V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281257V接下来去调查\n',
            '其他地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x180E)
    OP_28(0x008F, 0x02, 0x0004)
    OP_28(0x008F, 0x01, 0x0008)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0xD01
@scena.Code('func_06_D01')
def func_06_D01():
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
        'loc_D2B',
    )

    Call(0, 0x0009)
    FadeIn(0, 0)
    Call(0, 0x000A)

    def _loc_D2B(): pass

    label('loc_D2B')

    OP_6D(-35370, 1000, 172190, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -35500, 1000, 172520, 180)
    SetChrPos(0x0103, -34500, 1000, 172520, 180)
    SetChrPos(0x00F8, -35750, 1000, 173520, 180)
    SetChrPos(0x00F9, -34250, 1000, 173520, 180)

    @scena.Lambda('lambda_0DB2')
    def lambda_0DB2():
        OP_8E(0x00FE, -35810, 1000, 162970, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0DB2)

    Sleep(100)

    @scena.Lambda('lambda_0DD2')
    def lambda_0DD2():
        OP_8E(0x00FE, -34540, 1000, 162830, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0DD2)

    Sleep(200)

    @scena.Lambda('lambda_0DF2')
    def lambda_0DF2():
        OP_8E(0x00FE, -35850, 1000, 164520, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0DF2)

    Sleep(100)

    @scena.Lambda('lambda_0E12')
    def lambda_0E12():
        OP_8E(0x00FE, -34380, 1000, 164570, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0E12)

    @scena.Lambda('lambda_0E2D')
    def lambda_0E2D():
        OP_6D(-34940, 1000, 163860, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0E2D)

    FadeIn(1000, 0)
    OP_6B(3370, 3000)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x00F9, 0x0001)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E93',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281176V#061F嘿嘿，已经晴了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F7A')

    def _loc_E93(): pass

    label('loc_E93')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ECA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050281177V#051F嘿，已经晴了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F7A')

    def _loc_ECA(): pass

    label('loc_ECA')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F05',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281178V#030F嗯，好像已经晴了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F7A')

    def _loc_F05(): pass

    label('loc_F05')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F40',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281179V#048F……似乎已经晴了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F7A')

    def _loc_F40(): pass

    label('loc_F40')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F7A',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281180V#070F嗯……已经没有雾了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F7A(): pass

    label('loc_F7A')

    ChrTalk(
        0x0103,
        (
            '#0030281263V#026F艾利兹街道，距离洛连特\n',
            '大约６０塞尔矩的地点吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281255V#020F在有雾的范围内没有魔兽，\n',
            '应该可以确保安全。',
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
        'loc_109C',
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
            TXT(0x00, '【◇调查过玛鲁加山道】\n'),
            TXT(0x01, '【◇调查过米尔西街道】\n'),
            TXT(0x02, '【◇不变更】\n'),
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
        (0x00000000, 'loc_108A'),
        (0x00000001, 'loc_1093'),
        (-1, 'loc_109C'),
    )

    def _loc_108A(): pass

    label('loc_108A')

    OP_A3(0x180F)
    OP_A2(0x1810)

    Jump('loc_109C')

    def _loc_1093(): pass

    label('loc_1093')

    OP_A2(0x180F)
    OP_A3(0x1810)

    Jump('loc_109C')

    def _loc_109C(): pass

    label('loc_109C')

    ChrTurnDirection(0x0101, 0x0103, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 0, 0x1810)),
            Expr.Return,
        ),
        'loc_10FE',
    )

    ChrTalk(
        0x0101,
        (
            '#0010281256V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281266V这样的话，\n',
            '只剩下米尔西街道了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_114F')

    def _loc_10FE(): pass

    label('loc_10FE')

    ChrTalk(
        0x0101,
        (
            '#0010281256V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281268V这样的话，\n',
            '只剩下玛鲁加山道了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_114F(): pass

    label('loc_114F')

    OP_A2(0x180E)
    OP_28(0x008F, 0x02, 0x0004)
    OP_28(0x008F, 0x01, 0x0008)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x1161
@scena.Code('func_07_1161')
def func_07_1161():
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
        'loc_118B',
    )

    Call(0, 0x0009)
    FadeIn(0, 0)
    Call(0, 0x000A)

    def _loc_118B(): pass

    label('loc_118B')

    OP_6D(-35370, 1000, 172190, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -35500, 1000, 172520, 180)
    SetChrPos(0x0103, -34500, 1000, 172520, 180)
    SetChrPos(0x00F8, -35750, 1000, 173520, 180)
    SetChrPos(0x00F9, -34250, 1000, 173520, 180)

    @scena.Lambda('lambda_1212')
    def lambda_1212():
        OP_8E(0x00FE, -35810, 1000, 162970, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1212)

    Sleep(100)

    @scena.Lambda('lambda_1232')
    def lambda_1232():
        OP_8E(0x00FE, -34540, 1000, 162830, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_1232)

    Sleep(200)

    @scena.Lambda('lambda_1252')
    def lambda_1252():
        OP_8E(0x00FE, -35850, 1000, 164520, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_1252)

    Sleep(100)

    @scena.Lambda('lambda_1272')
    def lambda_1272():
        OP_8E(0x00FE, -34380, 1000, 164570, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1272)

    @scena.Lambda('lambda_128D')
    def lambda_128D():
        OP_6D(-34940, 1000, 163860, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_128D)

    FadeIn(1000, 0)
    OP_6B(3370, 3000)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x00F9, 0x0001)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12F3',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281176V#061F嘿嘿，已经晴了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13DA')

    def _loc_12F3(): pass

    label('loc_12F3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_132A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050281177V#051F嘿，已经晴了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13DA')

    def _loc_132A(): pass

    label('loc_132A')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1365',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281178V#030F嗯，好像已经晴了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13DA')

    def _loc_1365(): pass

    label('loc_1365')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13A0',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281179V#048F……似乎已经晴了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13DA')

    def _loc_13A0(): pass

    label('loc_13A0')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13DA',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281180V#070F嗯……已经没有雾了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13DA(): pass

    label('loc_13DA')

    ChrTalk(
        0x0103,
        (
            '#0030281263V#026F艾利兹街道、从洛连特出发\n',
            '大概６０塞尔矩的地点吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281255V#020F雾的范围内也没有魔兽，\n',
            '应该可以确保安全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281256V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281195V这样的话，三个地方\n',
            '都调查过了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010281278V#1006F我们应该回协会\n',
            '向爱娜姐报告了吧？',
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
        'loc_157F',
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
            TXT(0x00, '【◇没去过布莱特家】\n'),
            TXT(0x01, '【◇去过布莱特家】\n'),
            TXT(0x02, '【◇不变更】\n'),
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
        (0x00000000, 'loc_1573'),
        (0x00000001, 'loc_1579'),
        (-1, 'loc_157F'),
    )

    def _loc_1573(): pass

    label('loc_1573')

    OP_A3(0x180D)

    Jump('loc_157F')

    def _loc_1579(): pass

    label('loc_1579')

    OP_A2(0x180D)

    Jump('loc_157F')

    def _loc_157F(): pass

    label('loc_157F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 5, 0x180D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1653',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030281279V#023F#2P那样也好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281198V不过你好像\n',
            '还没回家看看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281281V#1004F啊……都给忘了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281200V#1008F回协会报告之前\n',
            '先回去看一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x008F, 0x02, 0x0004)
    OP_28(0x008F, 0x01, 0x0008)
    OP_28(0x008F, 0x01, 0x0800)
    OP_28(0x008F, 0x01, 0x1000)

    Jump('loc_169B')

    def _loc_1653(): pass

    label('loc_1653')

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030281283V#021F#2P嗯。\n',
            '那样也好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x008F, 0x02, 0x0004)
    OP_28(0x008F, 0x01, 0x0008)
    OP_28(0x008F, 0x01, 0x0200)
    OP_28(0x008F, 0x01, 0x0400)

    def _loc_169B(): pass

    label('loc_169B')

    OP_A2(0x180E)
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x16A1
@scena.Code('func_08_16A1')
def func_08_16A1():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_16D9')
    def lambda_16D9():
        OP_6D(-93210, 980, 76900, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_16D9)

    @scena.Lambda('lambda_16F1')
    def lambda_16F1():
        OP_6C(0, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_16F1)

    Sleep(1000)

    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
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

    Menu(
        0,
        10,
        32,
        1,
        (
            TXT(0x00, '钓鱼\n'),
            TXT(0x01, '离开\n'),
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
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1820',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x0E, 0x00000006, 0xFFFE9B70, 0x000003CA, 0x00013312, 0x000000E1, 0xFFFE8BF8, 0x0000041A, 0x000128E0)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_181A',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1814',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x01, 0x0010)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1811',
    )

    OP_28(0x0073, 0x01, 0x0002)
    OP_28(0x0073, 0x01, 0x0010)
    Sleep(400)

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '将在艾利兹街道发现钓鱼场的事情\n',
            '记录在游击士手册上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_1811(): pass

    label('loc_1811')

    Jump('loc_181A')

    def _loc_1814(): pass

    label('loc_1814')

    OP_28(0x0073, 0x01, 0x1000)

    def _loc_181A(): pass

    label('loc_181A')

    OP_0D()
    EventEnd(0x01)

    Jump('loc_182F')

    def _loc_1820(): pass

    label('loc_1820')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_182F',
    )

    EventEnd(0x01)

    def _loc_182F(): pass

    label('loc_182F')

    Return()

# id: 0x0009 offset: 0x1830
@scena.Code('func_09_1830')
def func_09_1830():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
        (0x00000000, 'loc_18AD'),
        (0x00000001, 'loc_18B3'),
        (-1, 'loc_18B9'),
    )

    def _loc_18AD(): pass

    label('loc_18AD')

    OP_A2(0x1200)

    Jump('loc_18B9')

    def _loc_18B3(): pass

    label('loc_18B3')

    OP_A2(0x1201)

    Jump('loc_18B9')

    def _loc_18B9(): pass

    label('loc_18B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_18C7',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_18CB')

    def _loc_18C7(): pass

    label('loc_18C7')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_18CB(): pass

    label('loc_18CB')

    Return()

# id: 0x000A offset: 0x18CC
@scena.Code('func_0A_18CC')
def func_0A_18CC():
    ClearMapFlags(0x00000001)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0002,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0003,
            0x0004,
            0x0006,
            0x0007,
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
    OP_69(0x0000, 0x00000000)
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
