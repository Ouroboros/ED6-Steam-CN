import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C2302_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2302   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, '守护者'),
    TXT(0x03, '守护者'),
    TXT(0x04, '守护者'),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
    TXT(0x09, ''),
    TXT(0x0A, ''),
    TXT(0x0B, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'C2302.x'
    header.mapIndex       = 1
    header.bgm            = 60
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x220D
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
        ('ED6_DT29/CH12730._CH', 'ED6_DT29/CH12730P._CP'),
        ('ED6_DT29/CH12731._CH', 'ED6_DT29/CH12731P._CP'),
        ('ED6_DT29/CH12740._CH', 'ED6_DT29/CH12740P._CP'),
        ('ED6_DT29/CH12741._CH', 'ED6_DT29/CH12741P._CP'),
        ('ED6_DT29/CH12750._CH', 'ED6_DT29/CH12750P._CP'),
        ('ED6_DT29/CH12751._CH', 'ED6_DT29/CH12751P._CP'),
        ('ED6_DT29/CH12760._CH', 'ED6_DT29/CH12760P._CP'),
        ('ED6_DT29/CH12761._CH', 'ED6_DT29/CH12761P._CP'),
        ('ED6_DT29/CH12770._CH', 'ED6_DT29/CH12770P._CP'),
        ('ED6_DT29/CH12771._CH', 'ED6_DT29/CH12771P._CP'),
        ('ED6_DT29/CH12780._CH', 'ED6_DT29/CH12780P._CP'),
        ('ED6_DT29/CH12781._CH', 'ED6_DT29/CH12781P._CP'),
        ('ED6_DT29/CH12790._CH', 'ED6_DT29/CH12790P._CP'),
        ('ED6_DT29/CH12791._CH', 'ED6_DT29/CH12791P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP'),
    ]

# id: 0x10002 offset: 0x15A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 20,
            z                   = 1000,
            y                   = -40050,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
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
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
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
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1DA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -5500,
            z           = 400,
            y           = -45890,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0400,
            word_18     = 0x1EA3,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 5600,
            z           = 400,
            y           = -45590,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0401,
            word_18     = 0x1EA4,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 5440,
            z           = 400,
            y           = -34850,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0400,
            word_18     = 0x1EA5,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -5500,
            z           = 400,
            y           = -35460,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0401,
            word_18     = 0x1EA6,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 0,
            z           = 0,
            y           = -6170,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0404,
            word_18     = 0x1EA7,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 0,
            z           = 0,
            y           = 7630,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0404,
            word_18     = 0x1EA8,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x282
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -4000,
            y           = 0,
            z           = 29000,
            range       = 4000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00007EFD,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000008,
        ),
    )

# id: 0x10005 offset: 0x2A2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = 0,
            triggerY            = -40000,
            triggerRange        = 1000,
            actorX              = 20,
            actorZ              = 0,
            actorY              = -40050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -5380,
            triggerZ            = 400,
            triggerY            = -9620,
            triggerRange        = 1000,
            actorX              = -5850,
            actorZ              = 400,
            actorY              = -10080,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -5470,
            triggerZ            = 400,
            triggerY            = 11520,
            triggerRange        = 1000,
            actorX              = -5880,
            actorZ              = 400,
            actorY              = 11930,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 5580,
            triggerZ            = 400,
            triggerY            = 11420,
            triggerRange        = 1000,
            actorX              = 6050,
            actorZ              = 400,
            actorY              = 11880,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 5470,
            triggerZ            = 400,
            triggerY            = -9530,
            triggerRange        = 1000,
            actorX              = 6030,
            actorZ              = 400,
            actorY              = -10090,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = 0,
            triggerY            = 38890,
            triggerRange        = 1000,
            actorX              = 0,
            actorZ              = 0,
            actorY              = 38890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x37A
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_38A'),
        (0x00000065, 'loc_391'),
        (-1, 'loc_398'),
    )

    def _loc_38A(): pass

    label('loc_38A')

    Event(0, 0x000C)

    Jump('loc_398')

    def _loc_391(): pass

    label('loc_391')

    Event(0, 0x000E)

    Jump('loc_398')

    def _loc_398(): pass

    label('loc_398')

    Return()

# id: 0x0001 offset: 0x399
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EE, 6, 0x1F76)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3AB',
    )

    OP_6F(0x0008, 0)

    Jump('loc_3B2')

    def _loc_3AB(): pass

    label('loc_3AB')

    OP_6F(0x0008, 60)

    def _loc_3B2(): pass

    label('loc_3B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EF, 0, 0x1F78)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C4',
    )

    OP_6F(0x0009, 0)

    Jump('loc_3CB')

    def _loc_3C4(): pass

    label('loc_3C4')

    OP_6F(0x0009, 60)

    def _loc_3CB(): pass

    label('loc_3CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EF, 1, 0x1F79)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DD',
    )

    OP_6F(0x000A, 0)

    Jump('loc_3E4')

    def _loc_3DD(): pass

    label('loc_3DD')

    OP_6F(0x000A, 60)

    def _loc_3E4(): pass

    label('loc_3E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EF, 2, 0x1F7A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F6',
    )

    OP_6F(0x000B, 0)

    Jump('loc_3FD')

    def _loc_3F6(): pass

    label('loc_3F6')

    OP_6F(0x000B, 60)

    def _loc_3FD(): pass

    label('loc_3FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EF, 3, 0x1F7B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_40F',
    )

    OP_6F(0x000C, 0)

    Jump('loc_416')

    def _loc_40F(): pass

    label('loc_40F')

    OP_6F(0x000C, 60)

    def _loc_416(): pass

    label('loc_416')

    LoadEffect(0x00, 'map\\\\mp049_21.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D4, 3, 0x1EA3)),
            Expr.Return,
        ),
        'loc_44A',
    )

    SetChrFlags(0x000C, 0x0080)

    def _loc_44A(): pass

    label('loc_44A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D4, 4, 0x1EA4)),
            Expr.Return,
        ),
        'loc_456',
    )

    SetChrFlags(0x000D, 0x0080)

    def _loc_456(): pass

    label('loc_456')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D4, 5, 0x1EA5)),
            Expr.Return,
        ),
        'loc_462',
    )

    SetChrFlags(0x000E, 0x0080)

    def _loc_462(): pass

    label('loc_462')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D4, 6, 0x1EA6)),
            Expr.Return,
        ),
        'loc_46E',
    )

    SetChrFlags(0x000F, 0x0080)

    def _loc_46E(): pass

    label('loc_46E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D4, 7, 0x1EA7)),
            Expr.Return,
        ),
        'loc_47A',
    )

    SetChrFlags(0x0010, 0x0080)

    def _loc_47A(): pass

    label('loc_47A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D5, 0, 0x1EA8)),
            Expr.Return,
        ),
        'loc_486',
    )

    SetChrFlags(0x0011, 0x0080)

    def _loc_486(): pass

    label('loc_486')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 4, 0x1E1C)),
            Expr.Return,
        ),
        'loc_518',
    )

    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_72(0x0004, 0x0020)
    OP_72(0x0005, 0x0020)
    OP_72(0x0006, 0x0020)
    OP_72(0x0007, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0008)
    OP_72(0x0005, 0x0008)
    OP_72(0x0006, 0x0008)
    OP_72(0x0007, 0x0008)
    OP_6F(0x0000, 360)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0007, 0)

    Jump('loc_5A0')

    def _loc_518(): pass

    label('loc_518')

    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_72(0x0004, 0x0020)
    OP_72(0x0005, 0x0020)
    OP_72(0x0006, 0x0020)
    OP_72(0x0007, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0008)
    OP_72(0x0005, 0x0008)
    OP_72(0x0006, 0x0008)
    OP_72(0x0007, 0x0008)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0007, 0)

    def _loc_5A0(): pass

    label('loc_5A0')

    OP_1B(0x00, 0x00, 0x000D)
    OP_1B(0x01, 0x00, 0x000F)

    Return()

# id: 0x0002 offset: 0x5AB
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5C0',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_5C0(): pass

    label('loc_5C0')

    Return()

# id: 0x0003 offset: 0x5C1
@scena.Code('func_03_5C1')
def func_03_5C1():
    UnlockAchievement(0x02, 0x0B, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EE, 6, 0x1F76)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_759',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0008, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EE, 7, 0x1F77)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6A5',
    )

    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ChrTurnDirection(0x0008, 0x0000, 0)
    OP_91(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_0618')
    def lambda_0618():
        OP_91(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0618)

    @scena.Lambda('lambda_0633')
    def lambda_0633():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000258)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0633)

    ClearChrFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x00000408, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_680'),
        (0x00000002, 'loc_692'),
        (0x00000001, 'loc_6A2'),
        (-1, 'loc_6A5'),
    )

    def _loc_680(): pass

    label('loc_680')

    OP_A2(0x1F77)
    OP_6F(0x0008, 60)
    Sleep(500)

    Jump('loc_6A5')

    def _loc_692(): pass

    label('loc_692')

    OP_6F(0x0008, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_6A2(): pass

    label('loc_6A2')

    OP_B4(0x00)

    Return()

    def _loc_6A5(): pass

    label('loc_6A5')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['漆黑之刃'], 1)"),
            Expr.Return,
        ),
        'loc_6F4',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['漆黑之刃']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F76)

    Jump('loc_756')

    def _loc_6F4(): pass

    label('loc_6F4')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['漆黑之刃']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['漆黑之刃']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0008, 60)
    OP_70(0x0008, 0x00000000)

    def _loc_756(): pass

    label('loc_756')

    Jump('loc_788')

    def _loc_759(): pass

    label('loc_759')

    FadeOut(300, 0, 100)

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
    def _loc_788(): pass

    label('loc_788')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x796
@scena.Code('func_04_796')
def func_04_796():
    UnlockAchievement(0x02, 0x94, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EF, 0, 0x1F78)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_873',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0009, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_80A',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1F78)

    Jump('loc_870')

    def _loc_80A(): pass

    label('loc_80A')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0009, 60)
    OP_70(0x0009, 0x00000000)

    def _loc_870(): pass

    label('loc_870')

    Jump('loc_8A4')

    def _loc_873(): pass

    label('loc_873')

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
    def _loc_8A4(): pass

    label('loc_8A4')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x8B2
@scena.Code('func_05_8B2')
def func_05_8B2():
    UnlockAchievement(0x02, 0x95, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EF, 1, 0x1F79)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_98F',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000A, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['痊愈之药'], 1)"),
            Expr.Return,
        ),
        'loc_926',
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
    OP_A2(0x1F79)

    Jump('loc_98C')

    def _loc_926(): pass

    label('loc_926')

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
    OP_6F(0x000A, 60)
    OP_70(0x000A, 0x00000000)

    def _loc_98C(): pass

    label('loc_98C')

    Jump('loc_9C0')

    def _loc_98F(): pass

    label('loc_98F')

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
    def _loc_9C0(): pass

    label('loc_9C0')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x9CE
@scena.Code('func_06_9CE')
def func_06_9CE():
    UnlockAchievement(0x02, 0x96, 0x00, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EF, 2, 0x1F7A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AA3',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000B, 0x0000001E)
    OP_73(0x000B)
    OP_6F(0x000B, 30)
    AddSepith(0x01, 0x012C)
    AddSepith(0x04, 0x0064)
    AddSepith(0x05, 0x0064)
    AddSepith(0x06, 0x0064)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×３００\n',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×１００\n',
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
    OP_A2(0x1F7A)

    Jump('loc_ABD')

    def _loc_AA3(): pass

    label('loc_AA3')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_ABD(): pass

    label('loc_ABD')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xACF
@scena.Code('func_07_ACF')
def func_07_ACF():
    UnlockAchievement(0x02, 0x97, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EF, 3, 0x1F7B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BAC',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000C, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_B43',
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
    OP_A2(0x1F7B)

    Jump('loc_BA9')

    def _loc_B43(): pass

    label('loc_B43')

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
    OP_6F(0x000C, 60)
    OP_70(0x000C, 0x00000000)

    def _loc_BA9(): pass

    label('loc_BA9')

    Jump('loc_BDD')

    def _loc_BAC(): pass

    label('loc_BAC')

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
    def _loc_BDD(): pass

    label('loc_BDD')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xBEB
@scena.Code('func_08_BEB')
def func_08_BEB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 7, 0x1E17)),
            Expr.Return,
        ),
        'loc_BF3',
    )

    Return()

    def _loc_BF3(): pass

    label('loc_BF3')

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
        'loc_C18',
    )

    Call(0, 0x000A)
    Call(0, 0x000B)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_C18(): pass

    label('loc_C18')

    Fade(1000)
    OP_6D(-130, 400, 28900, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(2350, 0)
    OP_6C(219000, 0)
    OP_6E(404, 0)
    SetChrPos(0x0101, 900, 400, 29590, 0)
    SetChrPos(0x0102, -620, 400, 29500, 0)
    SetChrPos(0x0103, 1050, 400, 28150, 0)
    SetChrPos(0x00F9, -780, 400, 28040, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 6, 0x1E16)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1207',
    )

    OP_A2(0x1E16)
    OP_22(0x0118, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D25',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_D63')

    def _loc_D25(): pass

    label('loc_D25')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D4C',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_D63')

    def _loc_D4C(): pass

    label('loc_D4C')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_D63(): pass

    label('loc_D63')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010341310V#1020F#5P又是了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030341311V#024F#5P……来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0009, 0x0004)
    SetChrPos(0x0009, 180, 2500, 37290, 180)
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x0009, 0x0080)
    SetChrChipByIndex(0x0009, 10)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)
    SetChrFlags(0x000A, 0x0004)
    SetChrPos(0x000A, -4960, 2500, 35560, 135)
    OP_9F(0x000A, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x000A, 8)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    SetChrFlags(0x000B, 0x0004)
    SetChrPos(0x000B, 4840, 2500, 35260, 225)
    OP_9F(0x000B, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x000B, 0x0080)
    SetChrChipByIndex(0x000B, 8)
    CreateThread(0x000B, 0x00, 0x00, 0x0002)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x0099, 0x00, 0x64)

    @scena.Lambda('lambda_0E5B')
    def lambda_0E5B():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0E5B)

    @scena.Lambda('lambda_0E6D')
    def lambda_0E6D():
        OP_8F(0x00FE, 180, 500, 37290, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0E6D)

    @scena.Lambda('lambda_0E88')
    def lambda_0E88():
        OP_6D(-180, 400, 32420, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0E88)

    @scena.Lambda('lambda_0EA0')
    def lambda_0EA0():
        OP_6B(2490, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0EA0)

    Sleep(100)

    OP_22(0x0099, 0x00, 0x64)

    @scena.Lambda('lambda_0EBA')
    def lambda_0EBA():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0EBA)

    @scena.Lambda('lambda_0ECC')
    def lambda_0ECC():
        OP_8F(0x00FE, -4960, 500, 35560, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0ECC)

    Sleep(100)

    OP_22(0x0099, 0x00, 0x64)

    @scena.Lambda('lambda_0EF1')
    def lambda_0EF1():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0EF1)

    @scena.Lambda('lambda_0F03')
    def lambda_0F03():
        OP_8F(0x00FE, 4840, 500, 35260, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0F03)

    Sleep(300)

    WaitForThreadExit(0x000B, 0x0001)
    WaitForThreadExit(0x000B, 0x0002)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0101, 14)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0102, 15)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x0103, 16)
    SetChrSubChip(0x0103, 0)
    SetChrSubChip(0x00F9, 0)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_F7B'),
        (0x00000004, 'loc_F83'),
        (0x00000006, 'loc_F8B'),
        (0x00000007, 'loc_F93'),
        (0x00000008, 'loc_F9B'),
        (-1, 'loc_FA3'),
    )

    def _loc_F7B(): pass

    label('loc_F7B')

    SetChrChipByIndex(0x00F9, 17)

    Jump('loc_FA3')

    def _loc_F83(): pass

    label('loc_F83')

    SetChrChipByIndex(0x00F9, 18)

    Jump('loc_FA3')

    def _loc_F8B(): pass

    label('loc_F8B')

    SetChrChipByIndex(0x00F9, 19)

    Jump('loc_FA3')

    def _loc_F93(): pass

    label('loc_F93')

    SetChrChipByIndex(0x00F9, 20)

    Jump('loc_FA3')

    def _loc_F9B(): pass

    label('loc_F9B')

    SetChrChipByIndex(0x00F9, 21)

    Jump('loc_FA3')

    def _loc_FA3(): pass

    label('loc_FA3')

    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_0FAF')
    def lambda_0FAF():
        OP_6D(100, 400, 29000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0FAF)

    @scena.Lambda('lambda_0FC7')
    def lambda_0FC7():
        OP_6B(2000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0FC7)

    SetChrChipByIndex(0x000A, 9)
    SetChrChipByIndex(0x000B, 9)

    @scena.Lambda('lambda_0FE1')
    def lambda_0FE1():
        OP_8F(0x00FE, -1140, 400, 31150, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0FE1)

    @scena.Lambda('lambda_0FFC')
    def lambda_0FFC():
        OP_8F(0x00FE, 2470, 400, 31700, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0FFC)

    Sleep(50)

    SetChrChipByIndex(0x0009, 11)

    @scena.Lambda('lambda_1021')
    def lambda_1021():
        OP_8F(0x00FE, 480, 400, 31320, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1021)

    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    Battle(0x0000040A, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_1068'),
        (0x00000002, 'loc_113B'),
        (0x00000001, 'loc_11FF'),
        (-1, 'loc_1204'),
    )

    def _loc_1068(): pass

    label('loc_1068')

    EventBegin(0x00)
    TerminateThread(0x0009, 0x02)
    SetChrFlags(0x0009, 0x0080)
    TerminateThread(0x000A, 0x02)
    SetChrFlags(0x000A, 0x0080)
    TerminateThread(0x000B, 0x02)
    SetChrFlags(0x000B, 0x0080)
    OP_6D(460, 400, 30560, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 460, 400, 30560, 0)
    SetChrPos(0x0001, 460, 400, 30560, 0)
    SetChrPos(0x0002, 460, 400, 30560, 0)
    SetChrPos(0x0003, 460, 400, 30560, 0)
    OP_69(0x0000, 0x00000000)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0103, 65535)
    SetChrChipByIndex(0x00F9, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x0103, 0)
    SetChrSubChip(0x00F9, 0)
    OP_A2(0x1E17)

    Jump('loc_1204')

    def _loc_113B(): pass

    label('loc_113B')

    EventBegin(0x00)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    OP_6D(190, 400, 25640, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 0, 400, 25640, 0)
    SetChrPos(0x0001, 0, 400, 25640, 0)
    SetChrPos(0x0002, 0, 400, 25640, 0)
    SetChrPos(0x0003, 0, 400, 25640, 0)
    OP_69(0x0000, 0x00000000)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0103, 65535)
    SetChrChipByIndex(0x00F9, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x0103, 0)
    SetChrSubChip(0x00F9, 0)

    Jump('loc_1204')

    def _loc_11FF(): pass

    label('loc_11FF')

    OP_B4(0x00)

    Jump('loc_1204')

    def _loc_1204(): pass

    label('loc_1204')

    Jump('loc_1664')

    def _loc_1207(): pass

    label('loc_1207')

    OP_22(0x0118, 0x00, 0x64)
    Sleep(1000)

    SetChrFlags(0x0009, 0x0004)
    SetChrPos(0x0009, 180, 2500, 37290, 180)
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x0009, 0x0080)
    SetChrChipByIndex(0x0009, 10)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)
    SetChrFlags(0x000A, 0x0004)
    SetChrPos(0x000A, -4960, 2500, 35560, 135)
    OP_9F(0x000A, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x000A, 8)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    SetChrFlags(0x000B, 0x0004)
    SetChrPos(0x000B, 4840, 2500, 35260, 225)
    OP_9F(0x000B, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x000B, 0x0080)
    SetChrChipByIndex(0x000B, 8)
    CreateThread(0x000B, 0x00, 0x00, 0x0002)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x0099, 0x00, 0x64)

    @scena.Lambda('lambda_12BB')
    def lambda_12BB():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_12BB)

    @scena.Lambda('lambda_12CD')
    def lambda_12CD():
        OP_8F(0x00FE, 180, 500, 37290, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_12CD)

    @scena.Lambda('lambda_12E8')
    def lambda_12E8():
        OP_6D(-180, 400, 32420, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_12E8)

    @scena.Lambda('lambda_1300')
    def lambda_1300():
        OP_6B(2490, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1300)

    Sleep(100)

    OP_22(0x0099, 0x00, 0x64)

    @scena.Lambda('lambda_131A')
    def lambda_131A():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_131A)

    @scena.Lambda('lambda_132C')
    def lambda_132C():
        OP_8F(0x00FE, -4960, 500, 35560, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_132C)

    Sleep(100)

    OP_22(0x0099, 0x00, 0x64)

    @scena.Lambda('lambda_1351')
    def lambda_1351():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1351)

    @scena.Lambda('lambda_1363')
    def lambda_1363():
        OP_8F(0x00FE, 4840, 500, 35260, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1363)

    Sleep(300)

    WaitForThreadExit(0x000B, 0x0001)
    WaitForThreadExit(0x000B, 0x0002)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0101, 14)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0102, 15)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x0103, 16)
    SetChrSubChip(0x0103, 0)
    SetChrSubChip(0x00F9, 0)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_13DB'),
        (0x00000004, 'loc_13E3'),
        (0x00000006, 'loc_13EB'),
        (0x00000007, 'loc_13F3'),
        (0x00000008, 'loc_13FB'),
        (-1, 'loc_1403'),
    )

    def _loc_13DB(): pass

    label('loc_13DB')

    SetChrChipByIndex(0x00F9, 17)

    Jump('loc_1403')

    def _loc_13E3(): pass

    label('loc_13E3')

    SetChrChipByIndex(0x00F9, 18)

    Jump('loc_1403')

    def _loc_13EB(): pass

    label('loc_13EB')

    SetChrChipByIndex(0x00F9, 19)

    Jump('loc_1403')

    def _loc_13F3(): pass

    label('loc_13F3')

    SetChrChipByIndex(0x00F9, 20)

    Jump('loc_1403')

    def _loc_13FB(): pass

    label('loc_13FB')

    SetChrChipByIndex(0x00F9, 21)

    Jump('loc_1403')

    def _loc_1403(): pass

    label('loc_1403')

    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_140F')
    def lambda_140F():
        OP_6D(100, 400, 29000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_140F)

    @scena.Lambda('lambda_1427')
    def lambda_1427():
        OP_6B(2000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1427)

    SetChrChipByIndex(0x000A, 9)
    SetChrChipByIndex(0x000B, 9)

    @scena.Lambda('lambda_1441')
    def lambda_1441():
        OP_8F(0x00FE, -1140, 400, 31150, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1441)

    @scena.Lambda('lambda_145C')
    def lambda_145C():
        OP_8F(0x00FE, 2470, 400, 31700, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_145C)

    Sleep(50)

    SetChrChipByIndex(0x0009, 11)

    @scena.Lambda('lambda_1481')
    def lambda_1481():
        OP_8F(0x00FE, 480, 400, 31320, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1481)

    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    Battle(0x0000040A, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_14C8'),
        (0x00000002, 'loc_159B'),
        (0x00000001, 'loc_165F'),
        (-1, 'loc_1664'),
    )

    def _loc_14C8(): pass

    label('loc_14C8')

    EventBegin(0x00)
    TerminateThread(0x0009, 0x02)
    SetChrFlags(0x0009, 0x0080)
    TerminateThread(0x000A, 0x02)
    SetChrFlags(0x000A, 0x0080)
    TerminateThread(0x000B, 0x02)
    SetChrFlags(0x000B, 0x0080)
    OP_6D(460, 400, 30560, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 460, 400, 30560, 0)
    SetChrPos(0x0001, 460, 400, 30560, 0)
    SetChrPos(0x0002, 460, 400, 30560, 0)
    SetChrPos(0x0003, 460, 400, 30560, 0)
    OP_69(0x0000, 0x00000000)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0103, 65535)
    SetChrChipByIndex(0x00F9, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x0103, 0)
    SetChrSubChip(0x00F9, 0)
    OP_A2(0x1E17)

    Jump('loc_1664')

    def _loc_159B(): pass

    label('loc_159B')

    EventBegin(0x00)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    OP_6D(190, 400, 25640, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 0, 400, 25640, 0)
    SetChrPos(0x0001, 0, 400, 25640, 0)
    SetChrPos(0x0002, 0, 400, 25640, 0)
    SetChrPos(0x0003, 0, 400, 25640, 0)
    OP_69(0x0000, 0x00000000)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0103, 65535)
    SetChrChipByIndex(0x00F9, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x0103, 0)
    SetChrSubChip(0x00F9, 0)

    Jump('loc_1664')

    def _loc_165F(): pass

    label('loc_165F')

    OP_B4(0x00)

    Jump('loc_1664')

    def _loc_1664(): pass

    label('loc_1664')

    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x1668
@scena.Code('func_09_1668')
def func_09_1668():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 4, 0x1E1C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19BB',
    )

    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x009C, 0x00, 0x64)
    OP_B0(0x0000, 0x78)
    OP_70(0x0000, 0x00000168)
    Sleep(2500)

    OP_22(0x009D, 0x00, 0x64)
    OP_B0(0x0004, 0x64)
    OP_B0(0x0005, 0x64)
    OP_B0(0x0006, 0x64)
    OP_B0(0x0007, 0x64)
    OP_70(0x0004, 0x000000F0)
    Sleep(100)

    OP_70(0x0005, 0x000000F0)
    Sleep(100)

    OP_70(0x0006, 0x000000F0)
    Sleep(100)

    OP_70(0x0007, 0x000000F0)
    Sleep(100)

    OP_22(0x00B9, 0x00, 0x64)
    OP_B0(0x0001, 0x64)
    OP_B0(0x0002, 0x64)
    OP_B0(0x0003, 0x64)
    OP_70(0x0001, 0x00000168)
    OP_70(0x0002, 0x00000168)
    OP_70(0x0003, 0x00000168)
    OP_73(0x0001)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于‘环’的封印（２／４）』\n',
            '　\n',
            '得知■■■划的■环■\n',
            '■取了■制手段。\n',
            '　\n',
            '『■』生出■■■\n',
            '被称为『■洛伊■■』\n',
            '的自■■护者\n',
            '向躲在■■中的我们■■\n',
            '　\n',
            '──不■，■■的■\n',
            '设施■建造■■下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■■地上设施相连\n',
            '■■■■■一■。\n',
            '■■洛伊■■的攻■\n',
            '■法■达\n',
            '■■500■■。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■■，■特洛伊■■的攻■\n',
            '却日■不■。躲在里面■我们\n',
            '那道坚固■防■线也■近了■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['数据水晶９']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['数据水晶９'], 1)
    OP_A2(0x1E1C)
    Sleep(100)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6F(0x0000, 360)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0007, 0)
    OP_6D(280, 200, 36690, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 280, 200, 36690, 0)
    SetChrPos(0x0001, 280, 200, 36690, 0)
    SetChrPos(0x0002, 280, 200, 36690, 0)
    SetChrPos(0x0003, 280, 200, 36690, 0)
    OP_69(0x0000, 0x00000000)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Jump('loc_1B72')

    def _loc_19BB(): pass

    label('loc_19BB')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x009C, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于‘环’的封印（２／４）』\n',
            '　\n',
            '得知■■■划的■环■\n',
            '■取了■制手段。\n',
            '　\n',
            '『■』生出■■■\n',
            '被称为『■洛伊■■』\n',
            '的自■■护者\n',
            '向躲在■■中的我们■■\n',
            '　\n',
            '──不■，■■的■\n',
            '设施■建造■■下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■■地上设施相连\n',
            '■■■■■一■。\n',
            '■■洛伊■■的攻■\n',
            '■法■达\n',
            '■■500■■。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■■，■特洛伊■■的攻■\n',
            '却日■不■。躲在里面■我们\n',
            '那道坚固■防■线也■近了■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_0D()

    def _loc_1B72(): pass

    label('loc_1B72')

    TalkEnd(0x00FF)

    Return()

# id: 0x000A offset: 0x1B76
@scena.Code('func_0A_1B76')
def func_0A_1B76():
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
        (0x00000000, 'loc_1BF0'),
        (0x00000001, 'loc_1BF6'),
        (-1, 'loc_1BFC'),
    )

    def _loc_1BF0(): pass

    label('loc_1BF0')

    OP_A2(0x1200)

    Jump('loc_1BFC')

    def _loc_1BF6(): pass

    label('loc_1BF6')

    OP_A2(0x1201)

    Jump('loc_1BFC')

    def _loc_1BFC(): pass

    label('loc_1BFC')

    Return()

# id: 0x000B offset: 0x1BFD
@scena.Code('func_0B_1BFD')
def func_0B_1BFD():
    FadeOut(0, 0, -1)
    OP_6D(-48940, 490, -13310, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
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
            0x0002,
            0x00FF,
        ),
        (
            0x0005,
            0x0006,
            0x0004,
            0x0008,
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

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x000C offset: 0x1C8A
@scena.Code('func_0C_1C8A')
def func_0C_1C8A():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(0, 200, -66500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x0101, -500, 200, -66000, 0)
    SetChrPos(0x0102, 500, 200, -66000, 0)
    SetChrPos(0x00F8, -500, 200, -67000, 0)
    SetChrPos(0x00F9, 500, 200, -67000, 0)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0010)
    Call(0, 0x0012)
    Fade(500)
    OP_6D(-80, 200, -64580, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0000, -80, 200, -64580, 0)
    SetChrPos(0x0001, -80, 200, -64580, 0)
    SetChrPos(0x0002, -80, 200, -64580, 0)
    SetChrPos(0x0003, -80, 200, -64580, 0)
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x1D97
@scena.Code('func_0D_1D97')
def func_0D_1D97():
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
    OP_6D(0, 200, -66500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x0101, 500, 200, -66000, 180)
    SetChrPos(0x0102, -500, 200, -66000, 180)
    SetChrPos(0x00F8, 500, 200, -67000, 180)
    SetChrPos(0x00F9, -500, 200, -67000, 180)
    OP_0D()
    Call(0, 0x0010)
    Call(0, 0x0013)
    NewScene('ED6_DT21/C2301._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x1E18
@scena.Code('func_0E_1E18')
def func_0E_1E18():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(0, 200, 66500, 0)
    SetChrPos(0x0101, 500, 200, 66000, 180)
    SetChrPos(0x0102, -500, 200, 66000, 180)
    SetChrPos(0x00F8, 500, 200, 67000, 180)
    SetChrPos(0x00F9, -500, 200, 67000, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0011)
    Call(0, 0x0012)
    Fade(500)
    OP_6D(70, 200, 64580, 0)
    SetChrPos(0x0000, 70, 200, 64580, 180)
    SetChrPos(0x0001, 70, 200, 64580, 180)
    SetChrPos(0x0002, 70, 200, 64580, 180)
    SetChrPos(0x0003, 70, 200, 64580, 180)
    EventEnd(0x00)

    Return()

# id: 0x000F offset: 0x1F13
@scena.Code('func_0F_1F13')
def func_0F_1F13():
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
    OP_6D(0, 200, 66500, 0)
    SetChrPos(0x0101, -500, 200, 67000, 0)
    SetChrPos(0x0102, 500, 200, 67000, 0)
    SetChrPos(0x00F8, -500, 200, 66000, 0)
    SetChrPos(0x00F9, 500, 200, 66000, 0)
    OP_0D()
    Call(0, 0x0011)
    Call(0, 0x0013)
    NewScene('ED6_DT21/C2303._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x1F8B
@scena.Code('func_10_1F8B')
def func_10_1F8B():
    PlayEffect(0x00, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x0011 offset: 0x206A
@scena.Code('func_11_206A')
def func_11_206A():
    PlayEffect(0x01, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x0012 offset: 0x2149
@scena.Code('func_12_2149')
def func_12_2149():
    @scena.Lambda('lambda_214F')
    def lambda_214F():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_214F)

    @scena.Lambda('lambda_2161')
    def lambda_2161():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_2161)

    @scena.Lambda('lambda_2173')
    def lambda_2173():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_2173)

    @scena.Lambda('lambda_2185')
    def lambda_2185():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_2185)

    Sleep(2500)

    Return()

# id: 0x0013 offset: 0x2197
@scena.Code('func_13_2197')
def func_13_2197():
    @scena.Lambda('lambda_219D')
    def lambda_219D():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_219D)

    @scena.Lambda('lambda_21AF')
    def lambda_21AF():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_21AF)

    @scena.Lambda('lambda_21C1')
    def lambda_21C1():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_21C1)

    @scena.Lambda('lambda_21D3')
    def lambda_21D3():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_21D3)

    Sleep(2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
