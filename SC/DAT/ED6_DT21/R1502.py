import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R1502_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1502   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '命运编造者'),
    TXT(0x02, '拉文努村方向'),
    TXT(0x03, '拉文努废坑方向'),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
    TXT(0x09, ''),
    TXT(0x0A, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'R1502.x'
    header.mapIndex       = 59
    header.bgm            = 22
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x7CE
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
        ('ED6_DT09/CH10030._CH', 'ED6_DT09/CH10030P._CP'),
        ('ED6_DT09/CH10031._CH', 'ED6_DT09/CH10031P._CP'),
        ('ED6_DT09/CH10860._CH', 'ED6_DT09/CH10860P._CP'),
        ('ED6_DT09/CH10861._CH', 'ED6_DT09/CH10861P._CP'),
        ('ED6_DT09/CH10310._CH', 'ED6_DT09/CH10310P._CP'),
        ('ED6_DT09/CH10311._CH', 'ED6_DT09/CH10311P._CP'),
        ('ED6_DT09/CH10330._CH', 'ED6_DT09/CH10330P._CP'),
        ('ED6_DT09/CH10331._CH', 'ED6_DT09/CH10331P._CP'),
    ]

# id: 0x10002 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -8730,
            z                   = -140,
            y                   = 1940,
            direction           = 270,
            word_0E             = 2,
            dword_10            = 131072,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -4760,
            z                   = 10,
            y                   = -38310,
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
            x                   = -62970,
            z                   = -30,
            y                   = 86680,
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

# id: 0x10003 offset: 0x14A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -31260,
            z           = -20,
            y           = -41320,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x012F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -40880,
            z           = 20,
            y           = -10170,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0130,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -35910,
            z           = -40,
            y           = 12760,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x012D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -88970,
            z           = -90,
            y           = -16370,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x012F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -70020,
            z           = -20,
            y           = 24980,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0130,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -81390,
            z           = -70,
            y           = 41540,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x012D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1F2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -8730,
            y           = -140,
            z           = 1940,
            range       = 2000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0x212
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -98600,
            triggerZ            = -90,
            triggerY            = 21830,
            triggerRange        = 1000,
            actorX              = -98170,
            actorZ              = 1490,
            actorY              = 22340,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -95400,
            triggerZ            = -120,
            triggerY            = 32479,
            triggerRange        = 1000,
            actorX              = -95800,
            actorZ              = -120,
            actorY              = 32080,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1440,
            triggerZ            = -20,
            triggerY            = 7890,
            triggerRange        = 1000,
            actorX              = -790,
            actorZ              = -20,
            actorY              = 8100,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -96250,
            triggerZ            = -90,
            triggerY            = -17480,
            triggerRange        = 1000,
            actorX              = -96950,
            actorZ              = -90,
            actorY              = -17530,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2A2
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x2A3
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFD40E0, 0xFFFE4698, 0x00230021)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2CD',
    )

    OP_B1('R1502_y')

    Jump('loc_2D6')

    def _loc_2CD(): pass

    label('loc_2CD')

    OP_B1('R1502_n')

    def _loc_2D6(): pass

    label('loc_2D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0365, 1, 0x1B29)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E8',
    )

    OP_6F(0x0001, 0)

    Jump('loc_2EF')

    def _loc_2E8(): pass

    label('loc_2E8')

    OP_6F(0x0001, 60)

    def _loc_2EF(): pass

    label('loc_2EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0365, 2, 0x1B2A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_301',
    )

    OP_6F(0x0002, 0)

    Jump('loc_308')

    def _loc_301(): pass

    label('loc_301')

    OP_6F(0x0002, 60)

    def _loc_308(): pass

    label('loc_308')

    OP_64(0x00, 0x0001)
    OP_71(0x0000, 0x0000)
    OP_71(0x0000, 0x0004)
    OP_64(0x03, 0x0001)
    OP_71(0x0003, 0x0000)
    OP_71(0x0003, 0x0004)
    OP_E0(0x01, 0xA2, 0x87, 0xFE, 0xFF, 0x60, 0xFF, 0xFF, 0xFF, 0x24, 0x7C, 0x00, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_350',
    )

    SetChrFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)

    Jump('loc_362')

    def _loc_350(): pass

    label('loc_350')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x035F, 5, 0x1AFD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_362',
    )

    ClearChrFlags(0x0008, 0x0080)
    OP_B2(0x01, 0x00, 0x0080)

    def _loc_362(): pass

    label('loc_362')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_372',
    )

    OP_10(0x01, 0x01)
    OP_10(0x02, 0x00)

    Jump('loc_388')

    def _loc_372(): pass

    label('loc_372')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 5, 0x1A15)),
            Expr.Return,
        ),
        'loc_382',
    )

    OP_10(0x01, 0x00)
    OP_10(0x02, 0x01)

    Jump('loc_388')

    def _loc_382(): pass

    label('loc_382')

    OP_10(0x01, 0x00)
    OP_10(0x02, 0x01)

    def _loc_388(): pass

    label('loc_388')

    If(
        (
            (Expr.Eval, "OP_29(0x007D, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x007D, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3A0',
    )

    OP_10(0x01, 0x00)
    OP_10(0x02, 0x01)

    def _loc_3A0(): pass

    label('loc_3A0')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B2',
    )

    OP_10(0x01, 0x00)
    OP_10(0x02, 0x01)

    def _loc_3B2(): pass

    label('loc_3B2')

    Return()

# id: 0x0002 offset: 0x3B3
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3C8',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_3C8(): pass

    label('loc_3C8')

    Return()

# id: 0x0003 offset: 0x3C9
@scena.Code('func_03_3C9')
def func_03_3C9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x035F, 5, 0x1AFD)),
            Expr.Return,
        ),
        'loc_3D1',
    )

    Return()

    def _loc_3D1(): pass

    label('loc_3D1')

    EventBegin(0x01)

    ExecExpressionWithValue(
        0x0000,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0004,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0005,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0006,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0007,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    SetChrSubChip(0x0004, 0)
    SetChrSubChip(0x0005, 0)
    SetChrSubChip(0x0006, 0)
    SetChrSubChip(0x0007, 0)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '大型魔兽正在四处游荡中。',
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
        0,
        (
            TXT(0x00, '【消灭它】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000001, 'loc_4B6'),
        (-1, 'loc_4D9'),
    )

    def _loc_4B6(): pass

    label('loc_4B6')

    Fade(500)
    OP_89(0x0000, -15290, -10, 5520, 135)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_4D9(): pass

    label('loc_4D9')

    Battle(0x00000EFB, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, -15290, -10, 5520, 135)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_512'),
        (0x00000001, 'loc_515'),
        (-1, 'loc_518'),
    )

    def _loc_512(): pass

    label('loc_512')

    EventEnd(0x00)

    Return()

    def _loc_515(): pass

    label('loc_515')

    OP_B4(0x00)

    Return()

    def _loc_518(): pass

    label('loc_518')

    EventBegin(0x01)
    SetChrFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)
    OP_0D()
    Sleep(400)

    OP_22(0x0017, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '消灭了通缉魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A2(0x1AFD)
    OP_28(0x00B4, 0x04, 0x10)
    OP_28(0x00B4, 0x04, 0x02)
    OP_28(0x00B4, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x584
@scena.Code('func_04_584')
def func_04_584():
    Return()

# id: 0x0005 offset: 0x585
@scena.Code('func_05_585')
def func_05_585():
    UnlockAchievement(0x02, 0xDD, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0365, 1, 0x1B29)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_662',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['清醒之药'], 1)"),
            Expr.Return,
        ),
        'loc_5F9',
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
    OP_A2(0x1B29)

    Jump('loc_65F')

    def _loc_5F9(): pass

    label('loc_5F9')

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
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_65F(): pass

    label('loc_65F')

    Jump('loc_693')

    def _loc_662(): pass

    label('loc_662')

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
    def _loc_693(): pass

    label('loc_693')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x6A1
@scena.Code('func_06_6A1')
def func_06_6A1():
    UnlockAchievement(0x02, 0xDE, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0365, 2, 0x1B2A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_77E',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_715',
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
    OP_A2(0x1B2A)

    Jump('loc_77B')

    def _loc_715(): pass

    label('loc_715')

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
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)

    def _loc_77B(): pass

    label('loc_77B')

    Jump('loc_7AF')

    def _loc_77E(): pass

    label('loc_77E')

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
    def _loc_7AF(): pass

    label('loc_7AF')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x7BD
@scena.Code('func_07_7BD')
def func_07_7BD():
    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
