import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3602_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3602   ._SN')

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
    TXT(0x0A, ''),
    TXT(0x0B, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3602.x'
    header.mapIndex       = 1
    header.bgm            = 60
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2E82
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
        ('ED6_DT29/CH12660._CH', 'ED6_DT29/CH12660P._CP'),
        ('ED6_DT29/CH12661._CH', 'ED6_DT29/CH12661P._CP'),
        ('ED6_DT29/CH12670._CH', 'ED6_DT29/CH12670P._CP'),
        ('ED6_DT29/CH12671._CH', 'ED6_DT29/CH12671P._CP'),
        ('ED6_DT29/CH12680._CH', 'ED6_DT29/CH12680P._CP'),
        ('ED6_DT29/CH12681._CH', 'ED6_DT29/CH12681P._CP'),
        ('ED6_DT29/CH12690._CH', 'ED6_DT29/CH12690P._CP'),
        ('ED6_DT29/CH12691._CH', 'ED6_DT29/CH12691P._CP'),
        ('ED6_DT29/CH12700._CH', 'ED6_DT29/CH12700P._CP'),
        ('ED6_DT29/CH12701._CH', 'ED6_DT29/CH12701P._CP'),
        ('ED6_DT29/CH12710._CH', 'ED6_DT29/CH12710P._CP'),
        ('ED6_DT29/CH12711._CH', 'ED6_DT29/CH12711P._CP'),
        ('ED6_DT29/CH12720._CH', 'ED6_DT29/CH12720P._CP'),
        ('ED6_DT29/CH12721._CH', 'ED6_DT29/CH12721P._CP'),
    ]

# id: 0x10002 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 16890,
            z           = -3600,
            y           = -90,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0414,
            word_18     = 0x1EB8,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -30,
            z           = -3600,
            y           = 17250,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0414,
            word_18     = 0x1EB9,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -20800,
            z           = -3600,
            y           = 20800,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0414,
            word_18     = 0x1EBA,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 13110,
            z           = -3600,
            y           = -13270,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0414,
            word_18     = 0x1EBB,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 60,
            z           = -450,
            y           = 61800,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0415,
            word_18     = 0x1EBC,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -24710,
            z           = -7600,
            y           = -24730,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0410,
            word_18     = 0x1EBD,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -24890,
            z           = -7600,
            y           = 24770,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0411,
            word_18     = 0x1EBE,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 24900,
            z           = -7600,
            y           = 24950,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0410,
            word_18     = 0x1EBF,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -24090,
            z           = -3600,
            y           = -300,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0411,
            word_18     = 0x1EC0,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 300,
            z           = -3600,
            y           = -23660,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0410,
            word_18     = 0x1EC1,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x232
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x232
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 50,
            triggerZ            = 0,
            triggerY            = 72970,
            triggerRange        = 1000,
            actorX              = -40,
            actorZ              = 0,
            actorY              = 73590,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -6880,
            triggerZ            = 0,
            triggerY            = 66010,
            triggerRange        = 1000,
            actorX              = -7540,
            actorZ              = 0,
            actorY              = 66010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 6880,
            triggerZ            = 0,
            triggerY            = 66010,
            triggerRange        = 1000,
            actorX              = 7580,
            actorZ              = 0,
            actorY              = 66010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -22970,
            triggerZ            = -3600,
            triggerY            = 7630,
            triggerRange        = 1000,
            actorX              = -22840,
            actorZ              = -3600,
            actorY              = 8250,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -16670,
            triggerZ            = -3600,
            triggerY            = -50,
            triggerRange        = 1000,
            actorX              = -15970,
            actorZ              = -3600,
            actorY              = 20,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = -3600,
            triggerY            = -16640,
            triggerRange        = 1000,
            actorX              = 10,
            actorZ              = -3600,
            actorY              = -15930,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 7680,
            triggerZ            = -3600,
            triggerY            = -22920,
            triggerRange        = 1000,
            actorX              = 8300,
            actorZ              = -3600,
            actorY              = -22720,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 45890,
            triggerZ            = -8000,
            triggerY            = -47410,
            triggerRange        = 1000,
            actorX              = 45890,
            actorZ              = -8000,
            actorY              = -47410,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 45890,
            triggerZ            = -8000,
            triggerY            = 46040,
            triggerRange        = 1000,
            actorX              = 45890,
            actorZ              = -8000,
            actorY              = 46040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -47420,
            triggerZ            = -8000,
            triggerY            = -47410,
            triggerRange        = 1000,
            actorX              = -47420,
            actorZ              = -8000,
            actorY              = -47410,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -47200,
            triggerZ            = -7850,
            triggerY            = 46160,
            triggerRange        = 1000,
            actorX              = -47200,
            actorZ              = -7850,
            actorY              = 46160,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3BE
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_3D6'),
        (0x00000065, 'loc_3DD'),
        (0x00000066, 'loc_3E4'),
        (0x00000067, 'loc_3EB'),
        (-1, 'loc_3F2'),
    )

    def _loc_3D6(): pass

    label('loc_3D6')

    Event(0, 0x000E)

    Jump('loc_3F2')

    def _loc_3DD(): pass

    label('loc_3DD')

    Event(0, 0x0010)

    Jump('loc_3F2')

    def _loc_3E4(): pass

    label('loc_3E4')

    Event(0, 0x0012)

    Jump('loc_3F2')

    def _loc_3EB(): pass

    label('loc_3EB')

    Event(0, 0x0014)

    Jump('loc_3F2')

    def _loc_3F2(): pass

    label('loc_3F2')

    Return()

# id: 0x0001 offset: 0x3F3
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E8, 0, 0x1F40)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_405',
    )

    OP_6F(0x0024, 0)

    Jump('loc_40C')

    def _loc_405(): pass

    label('loc_405')

    OP_6F(0x0024, 60)

    def _loc_40C(): pass

    label('loc_40C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E8, 2, 0x1F42)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_41E',
    )

    OP_6F(0x0025, 0)

    Jump('loc_425')

    def _loc_41E(): pass

    label('loc_41E')

    OP_6F(0x0025, 60)

    def _loc_425(): pass

    label('loc_425')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E8, 4, 0x1F44)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_437',
    )

    OP_6F(0x0026, 0)

    Jump('loc_43E')

    def _loc_437(): pass

    label('loc_437')

    OP_6F(0x0026, 60)

    def _loc_43E(): pass

    label('loc_43E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E8, 6, 0x1F46)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_450',
    )

    OP_6F(0x0027, 0)

    Jump('loc_457')

    def _loc_450(): pass

    label('loc_450')

    OP_6F(0x0027, 60)

    def _loc_457(): pass

    label('loc_457')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E8, 7, 0x1F47)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_469',
    )

    OP_6F(0x0028, 0)

    Jump('loc_470')

    def _loc_469(): pass

    label('loc_469')

    OP_6F(0x0028, 60)

    def _loc_470(): pass

    label('loc_470')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E9, 0, 0x1F48)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_482',
    )

    OP_6F(0x0029, 0)

    Jump('loc_489')

    def _loc_482(): pass

    label('loc_482')

    OP_6F(0x0029, 60)

    def _loc_489(): pass

    label('loc_489')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E9, 1, 0x1F49)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_49B',
    )

    OP_6F(0x002A, 0)

    Jump('loc_4A2')

    def _loc_49B(): pass

    label('loc_49B')

    OP_6F(0x002A, 60)

    def _loc_4A2(): pass

    label('loc_4A2')

    LoadEffect(0x00, 'map\\\\mp049_21.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D7, 0, 0x1EB8)),
            Expr.Return,
        ),
        'loc_4D6',
    )

    SetChrFlags(0x0008, 0x0080)

    def _loc_4D6(): pass

    label('loc_4D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D7, 1, 0x1EB9)),
            Expr.Return,
        ),
        'loc_4E2',
    )

    SetChrFlags(0x0009, 0x0080)

    def _loc_4E2(): pass

    label('loc_4E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D7, 2, 0x1EBA)),
            Expr.Return,
        ),
        'loc_4EE',
    )

    SetChrFlags(0x000A, 0x0080)

    def _loc_4EE(): pass

    label('loc_4EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D7, 3, 0x1EBB)),
            Expr.Return,
        ),
        'loc_4FA',
    )

    SetChrFlags(0x000B, 0x0080)

    def _loc_4FA(): pass

    label('loc_4FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D7, 4, 0x1EBC)),
            Expr.Return,
        ),
        'loc_506',
    )

    SetChrFlags(0x000C, 0x0080)

    def _loc_506(): pass

    label('loc_506')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D7, 5, 0x1EBD)),
            Expr.Return,
        ),
        'loc_512',
    )

    SetChrFlags(0x000D, 0x0080)

    def _loc_512(): pass

    label('loc_512')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D7, 6, 0x1EBE)),
            Expr.Return,
        ),
        'loc_51E',
    )

    SetChrFlags(0x000E, 0x0080)

    def _loc_51E(): pass

    label('loc_51E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D7, 7, 0x1EBF)),
            Expr.Return,
        ),
        'loc_52A',
    )

    SetChrFlags(0x000F, 0x0080)

    def _loc_52A(): pass

    label('loc_52A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D8, 0, 0x1EC0)),
            Expr.Return,
        ),
        'loc_536',
    )

    SetChrFlags(0x0010, 0x0080)

    def _loc_536(): pass

    label('loc_536')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D8, 1, 0x1EC1)),
            Expr.Return,
        ),
        'loc_542',
    )

    SetChrFlags(0x0011, 0x0080)

    def _loc_542(): pass

    label('loc_542')

    Call(0, 0x0009)
    OP_1B(0x00, 0x00, 0x000F)
    OP_1B(0x01, 0x00, 0x0011)
    OP_1B(0x02, 0x00, 0x0013)
    OP_1B(0x03, 0x00, 0x0015)

    Return()

# id: 0x0002 offset: 0x55B
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0xE2, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E8, 0, 0x1F40)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_638',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0024, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_5CF',
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
    OP_A2(0x1F40)

    Jump('loc_635')

    def _loc_5CF(): pass

    label('loc_5CF')

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
    OP_6F(0x0024, 60)
    OP_70(0x0024, 0x00000000)

    def _loc_635(): pass

    label('loc_635')

    Jump('loc_669')

    def _loc_638(): pass

    label('loc_638')

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
    def _loc_669(): pass

    label('loc_669')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x677
@scena.Code('func_03_677')
def func_03_677():
    UnlockAchievement(0x02, 0xE3, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E8, 2, 0x1F42)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_754',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0025, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['玄武甲'], 1)"),
            Expr.Return,
        ),
        'loc_6EB',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['玄武甲']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F42)

    Jump('loc_751')

    def _loc_6EB(): pass

    label('loc_6EB')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['玄武甲']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['玄武甲']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0025, 60)
    OP_70(0x0025, 0x00000000)

    def _loc_751(): pass

    label('loc_751')

    Jump('loc_785')

    def _loc_754(): pass

    label('loc_754')

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
    def _loc_785(): pass

    label('loc_785')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x793
@scena.Code('func_04_793')
def func_04_793():
    UnlockAchievement(0x02, 0xE4, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E8, 4, 0x1F44)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_870',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0026, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['朱雀之弓'], 1)"),
            Expr.Return,
        ),
        'loc_807',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['朱雀之弓']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F44)

    Jump('loc_86D')

    def _loc_807(): pass

    label('loc_807')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['朱雀之弓']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['朱雀之弓']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0026, 60)
    OP_70(0x0026, 0x00000000)

    def _loc_86D(): pass

    label('loc_86D')

    Jump('loc_8A1')

    def _loc_870(): pass

    label('loc_870')

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
    def _loc_8A1(): pass

    label('loc_8A1')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x8AF
@scena.Code('func_05_8AF')
def func_05_8AF():
    UnlockAchievement(0x02, 0xE5, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E8, 6, 0x1F46)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_98C',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0027, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['痊愈之药'], 1)"),
            Expr.Return,
        ),
        'loc_923',
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
    OP_A2(0x1F46)

    Jump('loc_989')

    def _loc_923(): pass

    label('loc_923')

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
    OP_6F(0x0027, 60)
    OP_70(0x0027, 0x00000000)

    def _loc_989(): pass

    label('loc_989')

    Jump('loc_9BD')

    def _loc_98C(): pass

    label('loc_98C')

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
    def _loc_9BD(): pass

    label('loc_9BD')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x9CB
@scena.Code('func_06_9CB')
def func_06_9CB():
    UnlockAchievement(0x02, 0xE6, 0x00, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E8, 7, 0x1F47)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AA0',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0028, 0x0000001E)
    OP_73(0x0028)
    OP_6F(0x0028, 30)
    AddSepith(0x02, 0x012C)
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
            '#58I火之耀晶片×３００\n',
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
    OP_A2(0x1F47)

    Jump('loc_ABA')

    def _loc_AA0(): pass

    label('loc_AA0')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_ABA(): pass

    label('loc_ABA')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xACC
@scena.Code('func_07_ACC')
def func_07_ACC():
    UnlockAchievement(0x02, 0xE7, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E9, 0, 0x1F48)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BA9',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0029, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_B40',
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
    OP_A2(0x1F48)

    Jump('loc_BA6')

    def _loc_B40(): pass

    label('loc_B40')

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
    OP_6F(0x0029, 60)
    OP_70(0x0029, 0x00000000)

    def _loc_BA6(): pass

    label('loc_BA6')

    Jump('loc_BDA')

    def _loc_BA9(): pass

    label('loc_BA9')

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
    def _loc_BDA(): pass

    label('loc_BDA')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xBE8
@scena.Code('func_08_BE8')
def func_08_BE8():
    UnlockAchievement(0x02, 0xE8, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E9, 1, 0x1F49)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CC5',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x002A, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_C5C',
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
    OP_A2(0x1F49)

    Jump('loc_CC2')

    def _loc_C5C(): pass

    label('loc_C5C')

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
    OP_6F(0x002A, 60)
    OP_70(0x002A, 0x00000000)

    def _loc_CC2(): pass

    label('loc_CC2')

    Jump('loc_CF6')

    def _loc_CC5(): pass

    label('loc_CC5')

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
    def _loc_CF6(): pass

    label('loc_CF6')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xD04
@scena.Code('func_09_D04')
def func_09_D04():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 6, 0x1E0E)),
            Expr.Return,
        ),
        'loc_D96',
    )

    OP_72(0x000A, 0x0020)
    OP_72(0x000B, 0x0020)
    OP_72(0x000C, 0x0020)
    OP_72(0x000D, 0x0020)
    OP_72(0x000E, 0x0020)
    OP_72(0x000F, 0x0020)
    OP_72(0x0010, 0x0020)
    OP_72(0x0011, 0x0020)
    OP_72(0x000A, 0x0008)
    OP_72(0x000B, 0x0008)
    OP_72(0x000C, 0x0008)
    OP_72(0x000D, 0x0008)
    OP_72(0x000E, 0x0008)
    OP_72(0x000F, 0x0008)
    OP_72(0x0010, 0x0008)
    OP_72(0x0011, 0x0008)
    OP_6F(0x000A, 360)
    OP_6F(0x000B, 0)
    OP_6F(0x000C, 0)
    OP_6F(0x000D, 0)
    OP_6F(0x000E, 0)
    OP_6F(0x000F, 0)
    OP_6F(0x0010, 0)
    OP_6F(0x0011, 0)

    Jump('loc_E1E')

    def _loc_D96(): pass

    label('loc_D96')

    OP_72(0x000A, 0x0020)
    OP_72(0x000B, 0x0020)
    OP_72(0x000C, 0x0020)
    OP_72(0x000D, 0x0020)
    OP_72(0x000E, 0x0020)
    OP_72(0x000F, 0x0020)
    OP_72(0x0010, 0x0020)
    OP_72(0x0011, 0x0020)
    OP_72(0x000A, 0x0008)
    OP_72(0x000B, 0x0008)
    OP_72(0x000C, 0x0008)
    OP_72(0x000D, 0x0008)
    OP_72(0x000E, 0x0008)
    OP_72(0x000F, 0x0008)
    OP_72(0x0010, 0x0008)
    OP_72(0x0011, 0x0008)
    OP_6F(0x000A, 0)
    OP_6F(0x000B, 0)
    OP_6F(0x000C, 0)
    OP_6F(0x000D, 0)
    OP_6F(0x000E, 0)
    OP_6F(0x000F, 0)
    OP_6F(0x0010, 0)
    OP_6F(0x0011, 0)

    def _loc_E1E(): pass

    label('loc_E1E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 7, 0x1E0F)),
            Expr.Return,
        ),
        'loc_ED2',
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
    OP_72(0x0009, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0008)
    OP_72(0x0005, 0x0008)
    OP_72(0x0006, 0x0008)
    OP_72(0x0007, 0x0008)
    OP_72(0x0008, 0x0008)
    OP_72(0x0009, 0x0008)
    OP_6F(0x0000, 360)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0007, 0)
    OP_6F(0x0008, 0)
    OP_6F(0x0009, 0)

    Jump('loc_F7C')

    def _loc_ED2(): pass

    label('loc_ED2')

    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_72(0x0004, 0x0020)
    OP_72(0x0005, 0x0020)
    OP_72(0x0006, 0x0020)
    OP_72(0x0007, 0x0020)
    OP_72(0x0008, 0x0020)
    OP_72(0x0009, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0008)
    OP_72(0x0005, 0x0008)
    OP_72(0x0006, 0x0008)
    OP_72(0x0007, 0x0008)
    OP_72(0x0008, 0x0008)
    OP_72(0x0009, 0x0008)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0007, 0)
    OP_6F(0x0008, 0)
    OP_6F(0x0009, 0)

    def _loc_F7C(): pass

    label('loc_F7C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 0, 0x1E10)),
            Expr.Return,
        ),
        'loc_100E',
    )

    OP_72(0x0012, 0x0020)
    OP_72(0x0013, 0x0020)
    OP_72(0x0014, 0x0020)
    OP_72(0x0015, 0x0020)
    OP_72(0x0016, 0x0020)
    OP_72(0x0017, 0x0020)
    OP_72(0x0018, 0x0020)
    OP_72(0x0019, 0x0020)
    OP_72(0x0012, 0x0008)
    OP_72(0x0013, 0x0008)
    OP_72(0x0014, 0x0008)
    OP_72(0x0015, 0x0008)
    OP_72(0x0016, 0x0008)
    OP_72(0x0017, 0x0008)
    OP_72(0x0018, 0x0008)
    OP_72(0x0019, 0x0008)
    OP_6F(0x0012, 360)
    OP_6F(0x0013, 0)
    OP_6F(0x0014, 0)
    OP_6F(0x0015, 0)
    OP_6F(0x0016, 0)
    OP_6F(0x0017, 0)
    OP_6F(0x0018, 0)
    OP_6F(0x0019, 0)

    Jump('loc_1096')

    def _loc_100E(): pass

    label('loc_100E')

    OP_72(0x0012, 0x0020)
    OP_72(0x0013, 0x0020)
    OP_72(0x0014, 0x0020)
    OP_72(0x0015, 0x0020)
    OP_72(0x0016, 0x0020)
    OP_72(0x0017, 0x0020)
    OP_72(0x0018, 0x0020)
    OP_72(0x0019, 0x0020)
    OP_72(0x0012, 0x0008)
    OP_72(0x0013, 0x0008)
    OP_72(0x0014, 0x0008)
    OP_72(0x0015, 0x0008)
    OP_72(0x0016, 0x0008)
    OP_72(0x0017, 0x0008)
    OP_72(0x0018, 0x0008)
    OP_72(0x0019, 0x0008)
    OP_6F(0x0012, 0)
    OP_6F(0x0013, 0)
    OP_6F(0x0014, 0)
    OP_6F(0x0015, 0)
    OP_6F(0x0016, 0)
    OP_6F(0x0017, 0)
    OP_6F(0x0018, 0)
    OP_6F(0x0019, 0)

    def _loc_1096(): pass

    label('loc_1096')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 2, 0x1E1A)),
            Expr.Return,
        ),
        'loc_114A',
    )

    OP_72(0x001A, 0x0020)
    OP_72(0x001B, 0x0020)
    OP_72(0x001C, 0x0020)
    OP_72(0x001D, 0x0020)
    OP_72(0x001E, 0x0020)
    OP_72(0x001F, 0x0020)
    OP_72(0x0020, 0x0020)
    OP_72(0x0021, 0x0020)
    OP_72(0x0022, 0x0020)
    OP_72(0x0023, 0x0020)
    OP_72(0x001A, 0x0008)
    OP_72(0x001B, 0x0008)
    OP_72(0x001C, 0x0008)
    OP_72(0x001D, 0x0008)
    OP_72(0x001E, 0x0008)
    OP_72(0x001F, 0x0008)
    OP_72(0x0020, 0x0008)
    OP_72(0x0021, 0x0008)
    OP_72(0x0022, 0x0008)
    OP_72(0x0023, 0x0008)
    OP_6F(0x001A, 360)
    OP_6F(0x001B, 0)
    OP_6F(0x001C, 0)
    OP_6F(0x001D, 0)
    OP_6F(0x001E, 0)
    OP_6F(0x001F, 0)
    OP_6F(0x0020, 0)
    OP_6F(0x0021, 0)
    OP_6F(0x0022, 0)
    OP_6F(0x0023, 0)

    Jump('loc_11F4')

    def _loc_114A(): pass

    label('loc_114A')

    OP_72(0x001A, 0x0020)
    OP_72(0x001B, 0x0020)
    OP_72(0x001C, 0x0020)
    OP_72(0x001D, 0x0020)
    OP_72(0x001E, 0x0020)
    OP_72(0x001F, 0x0020)
    OP_72(0x0020, 0x0020)
    OP_72(0x0021, 0x0020)
    OP_72(0x0022, 0x0020)
    OP_72(0x0023, 0x0020)
    OP_72(0x001A, 0x0008)
    OP_72(0x001B, 0x0008)
    OP_72(0x001C, 0x0008)
    OP_72(0x001D, 0x0008)
    OP_72(0x001E, 0x0008)
    OP_72(0x001F, 0x0008)
    OP_72(0x0020, 0x0008)
    OP_72(0x0021, 0x0008)
    OP_72(0x0022, 0x0008)
    OP_72(0x0023, 0x0008)
    OP_6F(0x001A, 0)
    OP_6F(0x001B, 0)
    OP_6F(0x001C, 0)
    OP_6F(0x001D, 0)
    OP_6F(0x001E, 0)
    OP_6F(0x001F, 0)
    OP_6F(0x0020, 0)
    OP_6F(0x0021, 0)
    OP_6F(0x0022, 0)
    OP_6F(0x0023, 0)

    def _loc_11F4(): pass

    label('loc_11F4')

    Return()

# id: 0x000A offset: 0x11F5
@scena.Code('func_0A_11F5')
def func_0A_11F5():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 6, 0x1E0E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1562',
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
    OP_B0(0x000A, 0x78)
    OP_70(0x000A, 0x00000168)
    Sleep(2500)

    OP_22(0x009D, 0x00, 0x64)
    OP_B0(0x000E, 0x64)
    OP_B0(0x000F, 0x64)
    OP_B0(0x0010, 0x64)
    OP_B0(0x0011, 0x64)
    OP_70(0x000E, 0x000000F0)
    Sleep(100)

    OP_70(0x000F, 0x000000F0)
    Sleep(100)

    OP_70(0x0010, 0x000000F0)
    Sleep(100)

    OP_70(0x0011, 0x000000F0)
    Sleep(100)

    OP_22(0x00B9, 0x00, 0x64)
    OP_B0(0x000B, 0x64)
    OP_B0(0x000C, 0x64)
    OP_B0(0x000D, 0x64)
    OP_70(0x000B, 0x00000168)
    OP_70(0x000C, 0x00000168)
    OP_70(0x000D, 0x00000168)
    OP_73(0x000B)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于湖岸的地下设施（１／４）』\n',
            '　\n',
            '要使■■■■构』■形\n',
            '巨■■■■■■\n',
            '■■模■■施■是不可■■的\n',
            '■先，作■■量■■，\n',
            '我们研究■■■■『■■的利用\n',
            '　\n',
            '　\n',
            '　\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■』对人的愿望■■■■\n',
            '■予恩■\n',
            '也就是■，可以■此想到\n',
            '是否只要是■实现人的愿望，就可以从『环』中■■■应的能量',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S……■■■种■■没能■得■。\n',
            '■■』在拥有了■主性■■■久，\n',
            '那种■■■人们的■■\n',
            '■为了■方■的■予',
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
            (TxtCtl.Item, ItemTable['数据水晶４']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['数据水晶４'], 1)
    OP_A2(0x1E0E)
    Sleep(100)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6F(0x000A, 360)
    OP_6F(0x000B, 0)
    OP_6F(0x000C, 0)
    OP_6F(0x000D, 0)
    OP_6F(0x000E, 0)
    OP_6F(0x000F, 0)
    OP_6F(0x0010, 0)
    OP_6F(0x0011, 0)
    OP_6D(44390, -7800, -49020, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 44390, -7800, -49020, 45)
    SetChrPos(0x0001, 44390, -7800, -49020, 45)
    SetChrPos(0x0002, 44390, -7800, -49020, 45)
    SetChrPos(0x0003, 44390, -7800, -49020, 45)
    OP_69(0x0000, 0x00000000)
    Sleep(500)

    FadeIn(1000, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Jump('loc_172E')

    def _loc_1562(): pass

    label('loc_1562')

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
            '#1S『关于湖岸的地下设施（１／４）』\n',
            '　\n',
            '要使■■■■构』■形\n',
            '巨■■■■■■\n',
            '■■模■■施■是不可■■的\n',
            '■先，作■■量■■，\n',
            '我们研究■■■■『■■的利用\n',
            '　\n',
            '　\n',
            '　\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■』对人的愿望■■■■\n',
            '■予恩■\n',
            '也就是■，可以■此想到\n',
            '是否只要是■实现人的愿望，就可以从『环』中■■■应的能量',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S……■■■种■■没能■得■。\n',
            '■■』在拥有了■主性■■■久，\n',
            '那种■■■人们的■■\n',
            '■为了■方■的■予',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_0D()

    def _loc_172E(): pass

    label('loc_172E')

    TalkEnd(0x00FF)

    Return()

# id: 0x000B offset: 0x1732
@scena.Code('func_0B_1732')
def func_0B_1732():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 7, 0x1E0F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AB4',
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
    OP_B0(0x0009, 0x64)
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

    OP_70(0x0009, 0x000000F0)
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
            '#1S『关于湖岸的地下设施（２／４）』\n',
            '　\n',
            '■■■环■的力量■■■■法实现。\n',
            '#1S于是我们■■意力■向了城■外部\n',
            '■■找■■深■■埋■在大地■的七耀脉■■，\n',
            '并■■图在那■■■■施。\n',
            '　\n',
            '■是，我们■经\n',
            '被置于『■』■监■之下',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■环』的■■■■\n',
            '似乎是■■■的存续放■第■位\n',
            '而排■■■■能对此■成■胁的■■\n',
            '　\n',
            '■■■了■■『■』，\n',
            '我们在观■七■■的名义下■■■设■■建造。',
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
            (TxtCtl.Item, ItemTable['数据水晶５']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['数据水晶５'], 1)
    OP_A2(0x1E0F)
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
    OP_6F(0x0009, 0)
    OP_6D(44260, -7800, 44300, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 44260, -7800, 44300, 45)
    SetChrPos(0x0001, 44260, -7800, 44300, 45)
    SetChrPos(0x0002, 44260, -7800, 44300, 45)
    SetChrPos(0x0003, 44260, -7800, 44300, 45)
    OP_69(0x0000, 0x00000000)
    Sleep(500)

    FadeIn(1000, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Jump('loc_1C67')

    def _loc_1AB4(): pass

    label('loc_1AB4')

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
            '#1S『关于湖岸的地下设施（２／４）』\n',
            '　\n',
            '■■■环■的力量■■■■法实现。\n',
            '#1S于是我们■■意力■向了城■外部\n',
            '■■找■■深■■埋■在大地■的七耀脉■■，\n',
            '并■■图在那■■■■施。\n',
            '　\n',
            '■是，我们■经\n',
            '被置于『■』■监■之下',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■环』的■■■■\n',
            '似乎是■■■的存续放■第■位\n',
            '而排■■■■能对此■成■胁的■■\n',
            '　\n',
            '■■■了■■『■』，\n',
            '我们在观■七■■的名义下■■■设■■建造。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_0D()

    def _loc_1C67(): pass

    label('loc_1C67')

    TalkEnd(0x00FF)

    Return()

# id: 0x000C offset: 0x1C6B
@scena.Code('func_0C_1C6B')
def func_0C_1C6B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 0, 0x1E10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F7B',
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
    OP_B0(0x0012, 0x78)
    OP_70(0x0012, 0x00000168)
    Sleep(2500)

    OP_22(0x009D, 0x00, 0x64)
    OP_B0(0x0016, 0x64)
    OP_B0(0x0017, 0x64)
    OP_B0(0x0018, 0x64)
    OP_B0(0x0019, 0x64)
    OP_70(0x0016, 0x000000F0)
    Sleep(100)

    OP_70(0x0017, 0x000000F0)
    Sleep(100)

    OP_70(0x0018, 0x000000F0)
    Sleep(100)

    OP_70(0x0019, 0x000000F0)
    Sleep(100)

    OP_22(0x00B9, 0x00, 0x64)
    OP_B0(0x0013, 0x64)
    OP_B0(0x0014, 0x64)
    OP_B0(0x0015, 0x64)
    OP_70(0x0013, 0x00000168)
    OP_70(0x0014, 0x00000168)
    OP_70(0x0015, 0x00000168)
    OP_73(0x0013)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于湖岸的地下设施（３／４）』\n',
            '　\n',
            '设施■■■■雷利亚■东■\n',
            '地下5■0■■的■方。\n',
            '#1S■■调■，\n',
            '那里是七■脉■■■中■地方。\n',
            '　\n',
            '延展至城■之下■■地\n',
            '被郁郁■葱■原生■包围。\n',
            '#1S■■■足，\n',
            '没有任■事物对工程■■■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■■一边逃避『■』■监视，\n',
            '一边■结■■■■力量\n',
            '抓紧■行地下■■的■■。',
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
            (TxtCtl.Item, ItemTable['数据水晶６']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['数据水晶６'], 1)
    OP_A2(0x1E10)
    Sleep(100)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6F(0x0012, 360)
    OP_6F(0x0013, 0)
    OP_6F(0x0014, 0)
    OP_6F(0x0015, 0)
    OP_6F(0x0016, 0)
    OP_6F(0x0017, 0)
    OP_6F(0x0018, 0)
    OP_6F(0x0019, 0)
    OP_6D(-49000, -7800, -49110, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, -49000, -7800, -49110, 45)
    SetChrPos(0x0001, -49000, -7800, -49110, 45)
    SetChrPos(0x0002, -49000, -7800, -49110, 45)
    SetChrPos(0x0003, -49000, -7800, -49110, 45)
    OP_69(0x0000, 0x00000000)
    Sleep(500)

    FadeIn(1000, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Jump('loc_20EA')

    def _loc_1F7B(): pass

    label('loc_1F7B')

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
            '#1S『关于湖岸的地下设施（３／４）』\n',
            '　\n',
            '设施■■■■雷利亚■东■\n',
            '地下5■0■■的■方。\n',
            '#1S■■调■，\n',
            '那里是七■脉■■■中■地方。\n',
            '　\n',
            '延展至城■之下■■地\n',
            '被郁郁■葱■原生■包围。\n',
            '#1S■■■足，\n',
            '没有任■事物对工程■■■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■■一边逃避『■』■监视，\n',
            '一边■结■■■■力量\n',
            '抓紧■行地下■■的■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_0D()

    def _loc_20EA(): pass

    label('loc_20EA')

    TalkEnd(0x00FF)

    Return()

# id: 0x000D offset: 0x20EE
@scena.Code('func_0D_20EE')
def func_0D_20EE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 2, 0x1E1A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_244F',
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
    OP_B0(0x001A, 0x78)
    OP_70(0x001A, 0x00000168)
    Sleep(2500)

    OP_22(0x009D, 0x00, 0x64)
    OP_B0(0x001E, 0x64)
    OP_B0(0x001F, 0x64)
    OP_B0(0x0020, 0x64)
    OP_B0(0x0021, 0x64)
    OP_B0(0x0022, 0x64)
    OP_B0(0x0023, 0x64)
    OP_70(0x001E, 0x000000F0)
    Sleep(100)

    OP_70(0x001F, 0x000000F0)
    Sleep(100)

    OP_70(0x0020, 0x000000F0)
    Sleep(100)

    OP_70(0x0021, 0x000000F0)
    Sleep(100)

    OP_70(0x0022, 0x000000F0)
    Sleep(100)

    OP_70(0x0023, 0x000000F0)
    Sleep(100)

    OP_22(0x00B9, 0x00, 0x64)
    OP_B0(0x001B, 0x64)
    OP_B0(0x001C, 0x64)
    OP_B0(0x001D, 0x64)
    OP_70(0x001B, 0x00000168)
    OP_70(0x001C, 0x00000168)
    OP_70(0x001D, 0x00000168)
    OP_73(0x001B)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于湖岸的地下设施（４／４）』\n',
            '　\n',
            '推进地下■■■建■■期间，\n',
            '■们在『环■■■■的情况■，\n',
            '■■面■边\n',
            '建成■■巨大■■■物。\n',
            '　\n',
            '■■■■■相同\n',
            '朝向■■』■■向的■■■■宁堡』\n',
            '另■种是为■■■■■\n',
            '而■■的4个■■■塔■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S这两■建■■在计■■\n',
            '分■有着■■■要■任务，\n',
            '它们■■下■■同■，\n',
            '是■封印机构■■■■或缺■。',
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
            (TxtCtl.Item, ItemTable['数据水晶７']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['数据水晶７'], 1)
    OP_A2(0x1E1A)
    Sleep(100)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6F(0x001A, 360)
    OP_6F(0x001B, 0)
    OP_6F(0x001B, 0)
    OP_6F(0x001C, 0)
    OP_6F(0x001D, 0)
    OP_6F(0x001E, 0)
    OP_6F(0x001F, 0)
    OP_6F(0x0020, 0)
    OP_6F(0x0021, 0)
    OP_6F(0x0022, 0)
    OP_6F(0x0023, 0)
    OP_6D(-49080, -7800, 44450, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, -49080, -7800, 44450, 45)
    SetChrPos(0x0001, -49080, -7800, 44450, 45)
    SetChrPos(0x0002, -49080, -7800, 44450, 45)
    SetChrPos(0x0003, -49080, -7800, 44450, 45)
    OP_69(0x0000, 0x00000000)
    Sleep(500)

    FadeIn(1000, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Jump('loc_25DA')

    def _loc_244F(): pass

    label('loc_244F')

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
            '#1S『关于湖岸的地下设施（４／４）』\n',
            '　\n',
            '推进地下■■■建■■期间，\n',
            '■们在『环■■■■的情况■，\n',
            '■■面■边\n',
            '建成■■巨大■■■物。\n',
            '　\n',
            '■■■■■相同\n',
            '朝向■■』■■向的■■■■宁堡』\n',
            '另■种是为■■■■■\n',
            '而■■的4个■■■塔■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S这两■建■■在计■■\n',
            '分■有着■■■要■任务，\n',
            '它们■■下■■同■，\n',
            '是■封印机构■■■■或缺■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_0D()

    def _loc_25DA(): pass

    label('loc_25DA')

    TalkEnd(0x00FF)

    Return()

# id: 0x000E offset: 0x25DE
@scena.Code('func_0E_25DE')
def func_0E_25DE():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(66500, -210, 0, 0)
    SetChrPos(0x0101, 66000, -210, -500, 270)
    SetChrPos(0x0102, 66000, -210, 500, 270)
    SetChrPos(0x00F8, 67000, -210, -500, 270)
    SetChrPos(0x00F9, 67000, -210, 500, 270)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0016)
    Call(0, 0x0018)
    Fade(500)
    OP_6D(64530, -210, -40, 0)
    SetChrPos(0x0000, 64530, -210, -40, 270)
    SetChrPos(0x0001, 64530, -210, -40, 270)
    SetChrPos(0x0002, 64530, -210, -40, 270)
    SetChrPos(0x0003, 64530, -210, -40, 270)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x000F offset: 0x26DE
@scena.Code('func_0F_26DE')
def func_0F_26DE():
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
    OP_6D(66500, -210, 0, 0)
    SetChrPos(0x0101, 67000, -210, 500, 90)
    SetChrPos(0x0102, 67000, -210, -500, 90)
    SetChrPos(0x00F8, 66000, -210, 500, 90)
    SetChrPos(0x00F9, 66000, -210, -500, 90)
    OP_0D()
    Call(0, 0x0016)
    Call(0, 0x0019)
    NewScene('ED6_DT21/C3601._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x2756
@scena.Code('func_10_2756')
def func_10_2756():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(0, -7360, 500, 0)
    SetChrPos(0x0101, 500, -7360, 0, 180)
    SetChrPos(0x0102, -500, -7360, 0, 180)
    SetChrPos(0x00F8, 500, -7360, 1000, 180)
    SetChrPos(0x00F9, -500, -7360, 1000, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0016)
    Call(0, 0x0018)
    Fade(500)
    OP_6D(30, -7360, -1280, 0)
    SetChrPos(0x0000, 30, -7360, -1280, 180)
    SetChrPos(0x0001, 30, -7360, -1280, 180)
    SetChrPos(0x0002, 30, -7360, -1280, 180)
    SetChrPos(0x0003, 30, -7360, -1280, 180)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0011 offset: 0x2856
@scena.Code('func_11_2856')
def func_11_2856():
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
    OP_6D(0, -7360, 500, 0)
    SetChrPos(0x0101, -500, -7360, 1000, 0)
    SetChrPos(0x0102, 500, -7360, 1000, 0)
    SetChrPos(0x00F8, -500, -7360, 0, 0)
    SetChrPos(0x00F9, 500, -7360, 0, 0)
    OP_0D()
    Call(0, 0x0016)
    Call(0, 0x0019)
    NewScene('ED6_DT21/C3601._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x28CE
@scena.Code('func_12_28CE')
def func_12_28CE():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(-66500, -210, 0, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0101, -66000, -210, 500, 90)
    SetChrPos(0x0102, -66000, -210, -500, 90)
    SetChrPos(0x00F8, -67000, -210, 500, 90)
    SetChrPos(0x00F9, -67000, -210, -500, 90)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0016)
    Call(0, 0x0018)
    Fade(500)
    OP_6D(-64580, -210, 80, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0000, -64580, -210, 80, 90)
    SetChrPos(0x0001, -64580, -210, 80, 90)
    SetChrPos(0x0002, -64580, -210, 80, 90)
    SetChrPos(0x0003, -64580, -210, 80, 90)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0013 offset: 0x29E0
@scena.Code('func_13_29E0')
def func_13_29E0():
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
    OP_6D(-66500, -210, 0, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0101, -67000, -210, -500, 270)
    SetChrPos(0x0102, -67000, -210, 500, 270)
    SetChrPos(0x00F8, -66000, -210, -500, 270)
    SetChrPos(0x00F9, -66000, -210, 500, 270)
    OP_0D()
    Call(0, 0x0016)
    Call(0, 0x0019)
    NewScene('ED6_DT21/C3601._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0014 offset: 0x2A61
@scena.Code('func_14_2A61')
def func_14_2A61():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(0, -210, -66500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x0101, -500, -210, -66000, 0)
    SetChrPos(0x0102, 500, -210, -66000, 0)
    SetChrPos(0x00F8, -500, -210, -67000, 0)
    SetChrPos(0x00F9, 500, -210, -67000, 0)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0017)
    Call(0, 0x0018)
    Fade(500)
    OP_6D(60, -210, -64319, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0000, 60, -210, -64319, 0)
    SetChrPos(0x0001, 60, -210, -64319, 0)
    SetChrPos(0x0002, 60, -210, -64319, 0)
    SetChrPos(0x0003, 60, -210, -64319, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0015 offset: 0x2B73
@scena.Code('func_15_2B73')
def func_15_2B73():
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
    OP_6D(0, -210, -66500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x0101, 500, -210, -67000, 180)
    SetChrPos(0x0102, -500, -210, -67000, 180)
    SetChrPos(0x00F8, 500, -210, -66000, 180)
    SetChrPos(0x00F9, -500, -210, -66000, 180)
    OP_0D()
    Call(0, 0x0017)
    Call(0, 0x0019)
    NewScene('ED6_DT21/C3603._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0016 offset: 0x2BF4
@scena.Code('func_16_2BF4')
def func_16_2BF4():
    PlayEffect(0x00, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x0017 offset: 0x2CD3
@scena.Code('func_17_2CD3')
def func_17_2CD3():
    PlayEffect(0x01, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x0018 offset: 0x2DB2
@scena.Code('func_18_2DB2')
def func_18_2DB2():
    @scena.Lambda('lambda_2DB8')
    def lambda_2DB8():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2DB8)

    @scena.Lambda('lambda_2DCA')
    def lambda_2DCA():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_2DCA)

    @scena.Lambda('lambda_2DDC')
    def lambda_2DDC():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_2DDC)

    @scena.Lambda('lambda_2DEE')
    def lambda_2DEE():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_2DEE)

    Sleep(2500)

    Return()

# id: 0x0019 offset: 0x2E00
@scena.Code('func_19_2E00')
def func_19_2E00():
    @scena.Lambda('lambda_2E06')
    def lambda_2E06():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2E06)

    @scena.Lambda('lambda_2E18')
    def lambda_2E18():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_2E18)

    @scena.Lambda('lambda_2E2A')
    def lambda_2E2A():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_2E2A)

    @scena.Lambda('lambda_2E3C')
    def lambda_2E3C():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_2E3C)

    Sleep(2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
