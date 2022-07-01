import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C2303_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2303   ._SN')

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
    header.mapModel       = 'C2303.x'
    header.mapIndex       = 1
    header.bgm            = 60
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2224
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
            x                   = 60,
            z                   = 1000,
            y                   = 820,
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
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0404,
            word_18     = 0x1EA9,
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
            word_18     = 0x1EAA,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 5440,
            z           = 400,
            y           = -34850,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0404,
            word_18     = 0x1EAB,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -5500,
            z           = 400,
            y           = -35460,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0400,
            word_18     = 0x1EAC,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 0,
            z           = 0,
            y           = -6170,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0401,
            word_18     = 0x1EAD,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 0,
            z           = 0,
            y           = 7630,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0400,
            word_18     = 0x1EAE,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x282
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -7000,
            y           = -1000,
            z           = 32000,
            range       = 7000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x000084D0,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000007,
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
            triggerX            = 210,
            triggerZ            = 0,
            triggerY            = -4860,
            triggerRange        = 1000,
            actorX              = 40,
            actorZ              = 0,
            actorY              = -4050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 140,
            triggerZ            = 0,
            triggerY            = 190,
            triggerRange        = 1000,
            actorX              = 60,
            actorZ              = 0,
            actorY              = 820,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 100,
            triggerZ            = 0,
            triggerY            = 5280,
            triggerRange        = 1000,
            actorX              = 80,
            actorZ              = 0,
            actorY              = 5940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
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
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x356
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_366'),
        (0x00000065, 'loc_36D'),
        (-1, 'loc_374'),
    )

    def _loc_366(): pass

    label('loc_366')

    Event(0, 0x000B)

    Jump('loc_374')

    def _loc_36D(): pass

    label('loc_36D')

    Event(0, 0x000D)

    Jump('loc_374')

    def _loc_374(): pass

    label('loc_374')

    Return()

# id: 0x0001 offset: 0x375
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EF, 4, 0x1F7C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_387',
    )

    OP_6F(0x0009, 0)

    Jump('loc_38E')

    def _loc_387(): pass

    label('loc_387')

    OP_6F(0x0009, 60)

    def _loc_38E(): pass

    label('loc_38E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EF, 6, 0x1F7E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A0',
    )

    OP_6F(0x000A, 0)

    Jump('loc_3A7')

    def _loc_3A0(): pass

    label('loc_3A0')

    OP_6F(0x000A, 60)

    def _loc_3A7(): pass

    label('loc_3A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EF, 7, 0x1F7F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3B9',
    )

    OP_6F(0x000B, 0)

    Jump('loc_3C0')

    def _loc_3B9(): pass

    label('loc_3B9')

    OP_6F(0x000B, 60)

    def _loc_3C0(): pass

    label('loc_3C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F0, 1, 0x1F81)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D2',
    )

    OP_6F(0x000C, 0)

    Jump('loc_3D9')

    def _loc_3D2(): pass

    label('loc_3D2')

    OP_6F(0x000C, 60)

    def _loc_3D9(): pass

    label('loc_3D9')

    LoadEffect(0x00, 'map\\\\mp049_21.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D5, 1, 0x1EA9)),
            Expr.Return,
        ),
        'loc_40D',
    )

    SetChrFlags(0x000C, 0x0080)

    def _loc_40D(): pass

    label('loc_40D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D5, 2, 0x1EAA)),
            Expr.Return,
        ),
        'loc_419',
    )

    SetChrFlags(0x000D, 0x0080)

    def _loc_419(): pass

    label('loc_419')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D5, 3, 0x1EAB)),
            Expr.Return,
        ),
        'loc_425',
    )

    SetChrFlags(0x000E, 0x0080)

    def _loc_425(): pass

    label('loc_425')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D5, 4, 0x1EAC)),
            Expr.Return,
        ),
        'loc_431',
    )

    SetChrFlags(0x000F, 0x0080)

    def _loc_431(): pass

    label('loc_431')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D5, 5, 0x1EAD)),
            Expr.Return,
        ),
        'loc_43D',
    )

    SetChrFlags(0x0010, 0x0080)

    def _loc_43D(): pass

    label('loc_43D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D5, 6, 0x1EAE)),
            Expr.Return,
        ),
        'loc_449',
    )

    SetChrFlags(0x0011, 0x0080)

    def _loc_449(): pass

    label('loc_449')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C4, 1, 0x1E21)),
            Expr.Return,
        ),
        'loc_4EC',
    )

    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_72(0x0004, 0x0020)
    OP_72(0x0005, 0x0020)
    OP_72(0x0006, 0x0020)
    OP_72(0x0007, 0x0020)
    OP_72(0x0008, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0008)
    OP_72(0x0005, 0x0008)
    OP_72(0x0006, 0x0008)
    OP_72(0x0007, 0x0008)
    OP_72(0x0008, 0x0008)
    OP_6F(0x0000, 360)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0007, 0)
    OP_6F(0x0008, 0)

    Jump('loc_585')

    def _loc_4EC(): pass

    label('loc_4EC')

    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_72(0x0004, 0x0020)
    OP_72(0x0005, 0x0020)
    OP_72(0x0006, 0x0020)
    OP_72(0x0007, 0x0020)
    OP_72(0x0008, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0008)
    OP_72(0x0005, 0x0008)
    OP_72(0x0006, 0x0008)
    OP_72(0x0007, 0x0008)
    OP_72(0x0008, 0x0008)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0007, 0)
    OP_6F(0x0008, 0)

    def _loc_585(): pass

    label('loc_585')

    OP_1B(0x00, 0x00, 0x000C)
    OP_1B(0x01, 0x00, 0x000E)

    Return()

# id: 0x0002 offset: 0x590
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5A5',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_5A5(): pass

    label('loc_5A5')

    Return()

# id: 0x0003 offset: 0x5A6
@scena.Code('func_03_5A6')
def func_03_5A6():
    UnlockAchievement(0x02, 0x98, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EF, 4, 0x1F7C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_683',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0009, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['龙牙鞭'], 1)"),
            Expr.Return,
        ),
        'loc_61A',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['龙牙鞭']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F7C)

    Jump('loc_680')

    def _loc_61A(): pass

    label('loc_61A')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['龙牙鞭']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['龙牙鞭']),
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

    def _loc_680(): pass

    label('loc_680')

    Jump('loc_6B4')

    def _loc_683(): pass

    label('loc_683')

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
    def _loc_6B4(): pass

    label('loc_6B4')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x6C2
@scena.Code('func_04_6C2')
def func_04_6C2():
    UnlockAchievement(0x02, 0x99, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EF, 6, 0x1F7E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_79F',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000A, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_736',
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
    OP_A2(0x1F7E)

    Jump('loc_79C')

    def _loc_736(): pass

    label('loc_736')

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
    OP_6F(0x000A, 60)
    OP_70(0x000A, 0x00000000)

    def _loc_79C(): pass

    label('loc_79C')

    Jump('loc_7D0')

    def _loc_79F(): pass

    label('loc_79F')

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
    def _loc_7D0(): pass

    label('loc_7D0')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x7DE
@scena.Code('func_05_7DE')
def func_05_7DE():
    UnlockAchievement(0x02, 0x9A, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EF, 7, 0x1F7F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_976',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000B, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F0, 0, 0x1F80)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8C2',
    )

    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ChrTurnDirection(0x0008, 0x0000, 0)
    OP_91(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_0835')
    def lambda_0835():
        OP_91(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0835)

    @scena.Lambda('lambda_0850')
    def lambda_0850():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000258)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0850)

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
        (0x00000000, 'loc_89D'),
        (0x00000002, 'loc_8AF'),
        (0x00000001, 'loc_8BF'),
        (-1, 'loc_8C2'),
    )

    def _loc_89D(): pass

    label('loc_89D')

    OP_A2(0x1F80)
    OP_6F(0x000B, 60)
    Sleep(500)

    Jump('loc_8C2')

    def _loc_8AF(): pass

    label('loc_8AF')

    OP_6F(0x000B, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_8BF(): pass

    label('loc_8BF')

    OP_B4(0x00)

    Return()

    def _loc_8C2(): pass

    label('loc_8C2')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['八卦服'], 1)"),
            Expr.Return,
        ),
        'loc_911',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['八卦服']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F7F)

    Jump('loc_973')

    def _loc_911(): pass

    label('loc_911')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['八卦服']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['八卦服']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x000B, 60)
    OP_70(0x000B, 0x00000000)

    def _loc_973(): pass

    label('loc_973')

    Jump('loc_9A5')

    def _loc_976(): pass

    label('loc_976')

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
    def _loc_9A5(): pass

    label('loc_9A5')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x9B3
@scena.Code('func_06_9B3')
def func_06_9B3():
    UnlockAchievement(0x02, 0x9B, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F0, 1, 0x1F81)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A90',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000C, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_A27',
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
    OP_A2(0x1F81)

    Jump('loc_A8D')

    def _loc_A27(): pass

    label('loc_A27')

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
    OP_6F(0x000C, 60)
    OP_70(0x000C, 0x00000000)

    def _loc_A8D(): pass

    label('loc_A8D')

    Jump('loc_AC1')

    def _loc_A90(): pass

    label('loc_A90')

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
    def _loc_AC1(): pass

    label('loc_AC1')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xACF
@scena.Code('func_07_ACF')
def func_07_ACF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 1, 0x1E19)),
            Expr.Return,
        ),
        'loc_AD7',
    )

    Return()

    def _loc_AD7(): pass

    label('loc_AD7')

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
        'loc_AFC',
    )

    Call(0, 0x0009)
    Call(0, 0x000A)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_AFC(): pass

    label('loc_AFC')

    Fade(1000)
    OP_6D(60, 400, 34140, 0)
    OP_67(0, 6390, -10000, 0)
    OP_6B(2140, 0)
    OP_6C(134000, 0)
    OP_6E(383, 0)
    SetChrPos(0x0101, 540, 400, 35020, 0)
    SetChrPos(0x0102, -980, 400, 35070, 0)
    SetChrPos(0x0103, 580, 400, 33530, 0)
    SetChrPos(0x00F9, -1190, 400, 33740, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 0, 0x1E18)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1123',
    )

    OP_A2(0x1E18)
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
        'loc_C09',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_C47')

    def _loc_C09(): pass

    label('loc_C09')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C30',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_C47')

    def _loc_C30(): pass

    label('loc_C30')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_C47(): pass

    label('loc_C47')

    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020341312V#1042F#2P来了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030341313V#024F#5P统统收拾掉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0009, 0x0004)
    SetChrPos(0x0009, -240, 2500, 27760, 180)
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x0009, 0x0080)
    SetChrChipByIndex(0x0009, 10)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)
    SetChrFlags(0x000A, 0x0004)
    SetChrPos(0x000A, 3930, 2500, 38750, 225)
    OP_9F(0x000A, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x000A, 8)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    SetChrFlags(0x000B, 0x0004)
    SetChrPos(0x000B, -4940, 2500, 38780, 135)
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

    @scena.Lambda('lambda_0D41')
    def lambda_0D41():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0D41)

    @scena.Lambda('lambda_0D53')
    def lambda_0D53():
        OP_8F(0x00FE, -240, 500, 27760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0D53)

    @scena.Lambda('lambda_0D6E')
    def lambda_0D6E():
        OP_6D(160, 400, 34890, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0D6E)

    @scena.Lambda('lambda_0D86')
    def lambda_0D86():
        OP_6B(2390, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D86)

    Sleep(100)

    OP_22(0x0099, 0x00, 0x64)

    @scena.Lambda('lambda_0DA0')
    def lambda_0DA0():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0DA0)

    @scena.Lambda('lambda_0DB2')
    def lambda_0DB2():
        OP_8F(0x00FE, 3930, 500, 38750, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0DB2)

    Sleep(100)

    OP_22(0x0099, 0x00, 0x64)

    @scena.Lambda('lambda_0DD7')
    def lambda_0DD7():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0DD7)

    @scena.Lambda('lambda_0DE9')
    def lambda_0DE9():
        OP_8F(0x00FE, -4940, 500, 38780, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0DE9)

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
        (0x00000005, 'loc_E61'),
        (0x00000004, 'loc_E69'),
        (0x00000006, 'loc_E71'),
        (0x00000007, 'loc_E79'),
        (0x00000008, 'loc_E81'),
        (-1, 'loc_E89'),
    )

    def _loc_E61(): pass

    label('loc_E61')

    SetChrChipByIndex(0x00F9, 17)

    Jump('loc_E89')

    def _loc_E69(): pass

    label('loc_E69')

    SetChrChipByIndex(0x00F9, 18)

    Jump('loc_E89')

    def _loc_E71(): pass

    label('loc_E71')

    SetChrChipByIndex(0x00F9, 19)

    Jump('loc_E89')

    def _loc_E79(): pass

    label('loc_E79')

    SetChrChipByIndex(0x00F9, 20)

    Jump('loc_E89')

    def _loc_E81(): pass

    label('loc_E81')

    SetChrChipByIndex(0x00F9, 21)

    Jump('loc_E89')

    def _loc_E89(): pass

    label('loc_E89')

    @scena.Lambda('lambda_0E8F')
    def lambda_0E8F():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0E8F)

    @scena.Lambda('lambda_0E9D')
    def lambda_0E9D():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0E9D)

    Sleep(100)

    @scena.Lambda('lambda_0EB0')
    def lambda_0EB0():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0EB0)

    OP_8C(0x0102, 315, 400)
    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_0ECB')
    def lambda_0ECB():
        OP_6D(470, 400, 33920, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0ECB)

    @scena.Lambda('lambda_0EE3')
    def lambda_0EE3():
        OP_6B(1750, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0EE3)

    SetChrChipByIndex(0x000A, 9)
    SetChrChipByIndex(0x000B, 9)

    @scena.Lambda('lambda_0EFD')
    def lambda_0EFD():
        OP_8F(0x00FE, 1400, 400, 35740, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0EFD)

    @scena.Lambda('lambda_0F18')
    def lambda_0F18():
        OP_8F(0x00FE, -2009, 400, 35920, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0F18)

    Sleep(50)

    SetChrChipByIndex(0x0009, 11)

    @scena.Lambda('lambda_0F3D')
    def lambda_0F3D():
        OP_8F(0x00FE, -290, 400, 32600, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0F3D)

    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    Battle(0x0000040B, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_F84'),
        (0x00000002, 'loc_1057'),
        (0x00000001, 'loc_111B'),
        (-1, 'loc_1120'),
    )

    def _loc_F84(): pass

    label('loc_F84')

    EventBegin(0x00)
    TerminateThread(0x0009, 0x02)
    SetChrFlags(0x0009, 0x0080)
    TerminateThread(0x000A, 0x02)
    SetChrFlags(0x000A, 0x0080)
    TerminateThread(0x000B, 0x02)
    SetChrFlags(0x000B, 0x0080)
    OP_6D(320, 400, 33530, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 320, 400, 33530, 0)
    SetChrPos(0x0001, 320, 400, 33530, 0)
    SetChrPos(0x0002, 320, 400, 33530, 0)
    SetChrPos(0x0003, 320, 400, 33530, 0)
    OP_69(0x0000, 0x00000000)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0103, 65535)
    SetChrChipByIndex(0x00F9, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x0103, 0)
    SetChrSubChip(0x00F9, 0)
    OP_A2(0x1E19)

    Jump('loc_1120')

    def _loc_1057(): pass

    label('loc_1057')

    EventBegin(0x00)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    OP_6D(340, 400, 25660, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 340, 400, 25660, 0)
    SetChrPos(0x0001, 340, 400, 25660, 0)
    SetChrPos(0x0002, 340, 400, 25660, 0)
    SetChrPos(0x0003, 340, 400, 25660, 0)
    OP_69(0x0000, 0x00000000)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0103, 65535)
    SetChrChipByIndex(0x00F9, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x0103, 0)
    SetChrSubChip(0x00F9, 0)

    Jump('loc_1120')

    def _loc_111B(): pass

    label('loc_111B')

    OP_B4(0x00)

    Jump('loc_1120')

    def _loc_1120(): pass

    label('loc_1120')

    Jump('loc_15B6')

    def _loc_1123(): pass

    label('loc_1123')

    OP_22(0x0118, 0x00, 0x64)
    Sleep(1000)

    SetChrFlags(0x0009, 0x0004)
    SetChrPos(0x0009, -240, 2500, 27760, 180)
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x0009, 0x0080)
    SetChrChipByIndex(0x0009, 10)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)
    SetChrFlags(0x000A, 0x0004)
    SetChrPos(0x000A, 3930, 2500, 38750, 225)
    OP_9F(0x000A, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x000A, 8)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    SetChrFlags(0x000B, 0x0004)
    SetChrPos(0x000B, -4940, 2500, 38780, 135)
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

    @scena.Lambda('lambda_11D7')
    def lambda_11D7():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_11D7)

    @scena.Lambda('lambda_11E9')
    def lambda_11E9():
        OP_8F(0x00FE, -240, 500, 27760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_11E9)

    @scena.Lambda('lambda_1204')
    def lambda_1204():
        OP_6D(160, 400, 34890, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1204)

    @scena.Lambda('lambda_121C')
    def lambda_121C():
        OP_6B(2390, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_121C)

    Sleep(100)

    OP_22(0x0099, 0x00, 0x64)

    @scena.Lambda('lambda_1236')
    def lambda_1236():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1236)

    @scena.Lambda('lambda_1248')
    def lambda_1248():
        OP_8F(0x00FE, 3930, 500, 38750, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1248)

    Sleep(100)

    OP_22(0x0099, 0x00, 0x64)

    @scena.Lambda('lambda_126D')
    def lambda_126D():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_126D)

    @scena.Lambda('lambda_127F')
    def lambda_127F():
        OP_8F(0x00FE, -4940, 500, 38780, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_127F)

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
        (0x00000005, 'loc_12F7'),
        (0x00000004, 'loc_12FF'),
        (0x00000006, 'loc_1307'),
        (0x00000007, 'loc_130F'),
        (0x00000008, 'loc_1317'),
        (-1, 'loc_131F'),
    )

    def _loc_12F7(): pass

    label('loc_12F7')

    SetChrChipByIndex(0x00F9, 17)

    Jump('loc_131F')

    def _loc_12FF(): pass

    label('loc_12FF')

    SetChrChipByIndex(0x00F9, 18)

    Jump('loc_131F')

    def _loc_1307(): pass

    label('loc_1307')

    SetChrChipByIndex(0x00F9, 19)

    Jump('loc_131F')

    def _loc_130F(): pass

    label('loc_130F')

    SetChrChipByIndex(0x00F9, 20)

    Jump('loc_131F')

    def _loc_1317(): pass

    label('loc_1317')

    SetChrChipByIndex(0x00F9, 21)

    Jump('loc_131F')

    def _loc_131F(): pass

    label('loc_131F')

    @scena.Lambda('lambda_1325')
    def lambda_1325():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_1325)

    @scena.Lambda('lambda_1333')
    def lambda_1333():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1333)

    Sleep(100)

    @scena.Lambda('lambda_1346')
    def lambda_1346():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1346)

    OP_8C(0x0102, 315, 400)
    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_1361')
    def lambda_1361():
        OP_6D(470, 400, 33920, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1361)

    @scena.Lambda('lambda_1379')
    def lambda_1379():
        OP_6B(1750, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1379)

    SetChrChipByIndex(0x000A, 9)
    SetChrChipByIndex(0x000B, 9)

    @scena.Lambda('lambda_1393')
    def lambda_1393():
        OP_8F(0x00FE, 1400, 400, 35740, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1393)

    @scena.Lambda('lambda_13AE')
    def lambda_13AE():
        OP_8F(0x00FE, -2009, 400, 35920, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_13AE)

    Sleep(50)

    SetChrChipByIndex(0x0009, 11)

    @scena.Lambda('lambda_13D3')
    def lambda_13D3():
        OP_8F(0x00FE, -290, 400, 32600, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_13D3)

    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    Battle(0x0000040B, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_141A'),
        (0x00000002, 'loc_14ED'),
        (0x00000001, 'loc_15B1'),
        (-1, 'loc_15B6'),
    )

    def _loc_141A(): pass

    label('loc_141A')

    EventBegin(0x00)
    TerminateThread(0x0009, 0x02)
    SetChrFlags(0x0009, 0x0080)
    TerminateThread(0x000A, 0x02)
    SetChrFlags(0x000A, 0x0080)
    TerminateThread(0x000B, 0x02)
    SetChrFlags(0x000B, 0x0080)
    OP_6D(320, 400, 33530, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 320, 400, 33530, 0)
    SetChrPos(0x0001, 320, 400, 33530, 0)
    SetChrPos(0x0002, 320, 400, 33530, 0)
    SetChrPos(0x0003, 320, 400, 33530, 0)
    OP_69(0x0000, 0x00000000)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0103, 65535)
    SetChrChipByIndex(0x00F9, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x0103, 0)
    SetChrSubChip(0x00F9, 0)
    OP_A2(0x1E19)

    Jump('loc_15B6')

    def _loc_14ED(): pass

    label('loc_14ED')

    EventBegin(0x00)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    OP_6D(340, 400, 25660, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 340, 400, 25660, 0)
    SetChrPos(0x0001, 340, 400, 25660, 0)
    SetChrPos(0x0002, 340, 400, 25660, 0)
    SetChrPos(0x0003, 340, 400, 25660, 0)
    OP_69(0x0000, 0x00000000)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0103, 65535)
    SetChrChipByIndex(0x00F9, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x0103, 0)
    SetChrSubChip(0x00F9, 0)

    Jump('loc_15B6')

    def _loc_15B1(): pass

    label('loc_15B1')

    OP_B4(0x00)

    Jump('loc_15B6')

    def _loc_15B6(): pass

    label('loc_15B6')

    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x15BA
@scena.Code('func_08_15BA')
def func_08_15BA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C4, 1, 0x1E21)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_197C',
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
    OP_B0(0x0008, 0x64)
    OP_70(0x0004, 0x000000F0)
    Sleep(100)

    OP_70(0x0005, 0x000000F0)
    Sleep(100)

    OP_70(0x0006, 0x000000F0)
    Sleep(100)

    OP_70(0x0007, 0x000000F0)
    Sleep(100)

    OP_70(0x0008, 0x000000F0)
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
            '#1S『关于‘环’的封印（３／４）』\n',
            '　\n',
            '在■■洛伊梅拉■■的攻■中，\n',
            '设■终于■■完成，\n',
            '然而确保从■■脉■■■计划中■■■能■\n',
            '还需■■些■间。\n',
            '　\n',
            '但是，■■■因为■■建造■成■\n',
            '我们大意■■■\n',
            '我们不小心让一台■■特洛■■\n',
            '■入了■■的内部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■旦让■进入■■\n',
            '想要抑制住■■攻■就不■■■■■。\n',
            '■洛伊梅拉■■一转眼\n',
            '■■■■■■处\n',
            '　\n',
            '■─真是■■一■啊。\n',
            '#1S来到最深■■■■■■■\n',
            '正要展■■坏■■时，\n',
            '必要■能■■■■■了，\n',
            '于是我们■上启■■■第■结■■。',
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
            (TxtCtl.Item, ItemTable['数据水晶１０']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['数据水晶１０'], 1)
    OP_A2(0x1E21)
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
    OP_6F(0x0008, 0)
    OP_6D(350, 200, 36760, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 350, 200, 36760, 0)
    SetChrPos(0x0001, 350, 200, 36760, 0)
    SetChrPos(0x0002, 350, 200, 36760, 0)
    SetChrPos(0x0003, 350, 200, 36760, 0)
    OP_69(0x0000, 0x00000000)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Jump('loc_1B8B')

    def _loc_197C(): pass

    label('loc_197C')

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
            '#1S『关于‘环’的封印（３／４）』\n',
            '　\n',
            '在■■洛伊梅拉■■的攻■中，\n',
            '设■终于■■完成，\n',
            '然而确保从■■脉■■■计划中■■■能■\n',
            '还需■■些■间。\n',
            '　\n',
            '但是，■■■因为■■建造■成■\n',
            '我们大意■■■\n',
            '我们不小心让一台■■特洛■■\n',
            '■入了■■的内部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■旦让■进入■■\n',
            '想要抑制住■■攻■就不■■■■■。\n',
            '■洛伊梅拉■■一转眼\n',
            '■■■■■■处\n',
            '　\n',
            '■─真是■■一■啊。\n',
            '#1S来到最深■■■■■■■\n',
            '正要展■■坏■■时，\n',
            '必要■能■■■■■了，\n',
            '于是我们■上启■■■第■结■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_0D()

    def _loc_1B8B(): pass

    label('loc_1B8B')

    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0x1B8F
@scena.Code('func_09_1B8F')
def func_09_1B8F():
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
        (0x00000000, 'loc_1C09'),
        (0x00000001, 'loc_1C0F'),
        (-1, 'loc_1C15'),
    )

    def _loc_1C09(): pass

    label('loc_1C09')

    OP_A2(0x1200)

    Jump('loc_1C15')

    def _loc_1C0F(): pass

    label('loc_1C0F')

    OP_A2(0x1201)

    Jump('loc_1C15')

    def _loc_1C15(): pass

    label('loc_1C15')

    Return()

# id: 0x000A offset: 0x1C16
@scena.Code('func_0A_1C16')
def func_0A_1C16():
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

# id: 0x000B offset: 0x1CA3
@scena.Code('func_0B_1CA3')
def func_0B_1CA3():
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
    Call(0, 0x000F)
    Call(0, 0x0011)
    Fade(500)
    OP_6D(-70, 200, -64510, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0000, -70, 200, -64510, 0)
    SetChrPos(0x0001, -70, 200, -64510, 0)
    SetChrPos(0x0002, -70, 200, -64510, 0)
    SetChrPos(0x0003, -70, 200, -64510, 0)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x1DB0
@scena.Code('func_0C_1DB0')
def func_0C_1DB0():
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
    SetChrPos(0x0101, 500, 200, -67000, 180)
    SetChrPos(0x0102, -500, 200, -67000, 180)
    SetChrPos(0x00F8, 500, 200, -66000, 180)
    SetChrPos(0x00F9, -500, 200, -66000, 180)
    OP_0D()
    Call(0, 0x000F)
    Call(0, 0x0012)
    NewScene('ED6_DT21/C2302._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x1E31
@scena.Code('func_0D_1E31')
def func_0D_1E31():
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
    Call(0, 0x0010)
    Call(0, 0x0011)
    Fade(500)
    OP_6D(90, 200, 64590, 0)
    SetChrPos(0x0000, 90, 200, 64590, 180)
    SetChrPos(0x0001, 90, 200, 64590, 180)
    SetChrPos(0x0002, 90, 200, 64590, 180)
    SetChrPos(0x0003, 90, 200, 64590, 180)
    EventEnd(0x00)

    Return()

# id: 0x000E offset: 0x1F2C
@scena.Code('func_0E_1F2C')
def func_0E_1F2C():
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
    Call(0, 0x0010)
    Call(0, 0x0012)
    NewScene('ED6_DT21/C2304._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x1FA4
@scena.Code('func_0F_1FA4')
def func_0F_1FA4():
    PlayEffect(0x00, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x0010 offset: 0x2083
@scena.Code('func_10_2083')
def func_10_2083():
    PlayEffect(0x01, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x0011 offset: 0x2162
@scena.Code('func_11_2162')
def func_11_2162():
    @scena.Lambda('lambda_2168')
    def lambda_2168():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2168)

    @scena.Lambda('lambda_217A')
    def lambda_217A():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_217A)

    @scena.Lambda('lambda_218C')
    def lambda_218C():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_218C)

    @scena.Lambda('lambda_219E')
    def lambda_219E():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_219E)

    Sleep(2500)

    Return()

# id: 0x0012 offset: 0x21B0
@scena.Code('func_12_21B0')
def func_12_21B0():
    @scena.Lambda('lambda_21B6')
    def lambda_21B6():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_21B6)

    @scena.Lambda('lambda_21C8')
    def lambda_21C8():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_21C8)

    @scena.Lambda('lambda_21DA')
    def lambda_21DA():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_21DA)

    @scena.Lambda('lambda_21EC')
    def lambda_21EC():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_21EC)

    Sleep(2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
