import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5502_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5502   ._SN')

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
    header.mapName        = 'Other'
    header.mapModel       = 'C5502.x'
    header.mapIndex       = 1
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1580
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
        ('ED6_DT29/CH12190._CH', 'ED6_DT29/CH12190P._CP'),
        ('ED6_DT29/CH12191._CH', 'ED6_DT29/CH12191P._CP'),
        ('ED6_DT29/CH12200._CH', 'ED6_DT29/CH12200P._CP'),
        ('ED6_DT29/CH12201._CH', 'ED6_DT29/CH12201P._CP'),
        ('ED6_DT29/CH12210._CH', 'ED6_DT29/CH12210P._CP'),
        ('ED6_DT29/CH12211._CH', 'ED6_DT29/CH12211P._CP'),
        ('ED6_DT29/CH12220._CH', 'ED6_DT29/CH12220P._CP'),
        ('ED6_DT29/CH12221._CH', 'ED6_DT29/CH12221P._CP'),
    ]

# id: 0x10002 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -47360,
            z                   = -1000,
            y                   = 191570,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x10A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 12820,
            z           = 0,
            y           = 136490,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0387,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -27240,
            z           = 0,
            y           = 139530,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0388,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -42600,
            z           = 0,
            y           = 150280,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0387,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -39260,
            z           = 0,
            y           = 169730,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0388,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -28360,
            z           = 0,
            y           = 190270,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0387,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 14670,
            z           = 0,
            y           = 176940,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0388,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -32659,
            z           = -2000,
            y           = 160510,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0387,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -18800,
            z           = -2000,
            y           = 167080,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0387,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -43100,
            z           = -2000,
            y           = 155530,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0387,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x206
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x206
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -1160,
            triggerZ            = 0,
            triggerY            = 144370,
            triggerRange        = 1700,
            actorX              = -1160,
            actorZ              = 2500,
            actorY              = 144370,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -13210,
            triggerZ            = 0,
            triggerY            = 169110,
            triggerRange        = 1700,
            actorX              = -13210,
            actorZ              = 2500,
            actorY              = 169110,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4340,
            triggerZ            = 0,
            triggerY            = 181980,
            triggerRange        = 1700,
            actorX              = 4340,
            actorZ              = 2500,
            actorY              = 181980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -30880,
            triggerZ            = 0,
            triggerY            = 150510,
            triggerRange        = 1700,
            actorX              = -30880,
            actorZ              = 2500,
            actorY              = 150510,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -38950,
            triggerZ            = 0,
            triggerY            = 173800,
            triggerRange        = 1000,
            actorX              = -38990,
            actorZ              = 0,
            actorY              = 174460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -42500,
            triggerZ            = 0,
            triggerY            = 173790,
            triggerRange        = 1000,
            actorX              = -42500,
            actorZ              = 0,
            actorY              = 174410,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -35450,
            triggerZ            = 0,
            triggerY            = 173790,
            triggerRange        = 1000,
            actorX              = -35450,
            actorZ              = 0,
            actorY              = 174450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -36970,
            triggerZ            = 0,
            triggerY            = 187560,
            triggerRange        = 1000,
            actorX              = -36880,
            actorZ              = 0,
            actorY              = 186860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 11070,
            triggerZ            = 0,
            triggerY            = 155530,
            triggerRange        = 1000,
            actorX              = 11070,
            actorZ              = 0,
            actorY              = 154910,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -7710,
            triggerZ            = 0,
            triggerY            = 158960,
            triggerRange        = 1000,
            actorX              = -7050,
            actorZ              = 0,
            actorY              = 158960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -47400,
            triggerZ            = -2000,
            triggerY            = 190910,
            triggerRange        = 1000,
            actorX              = -47360,
            actorZ              = -2000,
            actorY              = 191570,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x392
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x393
@scena.Code('Init')
def Init():
    OP_22(0x01C7, 0x00, 0x64)
    OP_72(0x0000, 0x0028)
    OP_72(0x0001, 0x0028)
    OP_72(0x0002, 0x0028)
    OP_72(0x0003, 0x0028)
    OP_72(0x0004, 0x0028)
    OP_72(0x0005, 0x0028)
    OP_72(0x0006, 0x0028)
    OP_72(0x0007, 0x0028)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 0, 0x10A8)),
            Expr.Return,
        ),
        'loc_3D5',
    )

    OP_6F(0x0001, 120)
    OP_6F(0x0006, 60)

    def _loc_3D5(): pass

    label('loc_3D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 7, 0x10A7)),
            Expr.Return,
        ),
        'loc_3EA',
    )

    OP_6F(0x0001, 120)
    OP_6F(0x0006, 160)

    def _loc_3EA(): pass

    label('loc_3EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 2, 0x10AA)),
            Expr.Return,
        ),
        'loc_3FF',
    )

    OP_6F(0x0003, 120)
    OP_6F(0x0002, 60)

    def _loc_3FF(): pass

    label('loc_3FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 1, 0x10A9)),
            Expr.Return,
        ),
        'loc_414',
    )

    OP_6F(0x0003, 120)
    OP_6F(0x0002, 160)

    def _loc_414(): pass

    label('loc_414')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 4, 0x10AC)),
            Expr.Return,
        ),
        'loc_429',
    )

    OP_6F(0x0004, 120)
    OP_6F(0x0005, 60)

    def _loc_429(): pass

    label('loc_429')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 3, 0x10AB)),
            Expr.Return,
        ),
        'loc_43E',
    )

    OP_6F(0x0004, 120)
    OP_6F(0x0005, 160)

    def _loc_43E(): pass

    label('loc_43E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 5, 0x10AD)),
            Expr.Return,
        ),
        'loc_453',
    )

    OP_6F(0x0007, 60)
    OP_6F(0x0000, 260)

    def _loc_453(): pass

    label('loc_453')

    ExecExpressionWithVar(
        0x2A,
        (
            (Expr.PushLong, 0x6D6),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0222, 0, 0x1110)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_46F',
    )

    OP_6F(0x0008, 0)

    Jump('loc_476')

    def _loc_46F(): pass

    label('loc_46F')

    OP_6F(0x0008, 60)

    def _loc_476(): pass

    label('loc_476')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0222, 1, 0x1111)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_488',
    )

    OP_6F(0x0009, 0)

    Jump('loc_48F')

    def _loc_488(): pass

    label('loc_488')

    OP_6F(0x0009, 60)

    def _loc_48F(): pass

    label('loc_48F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0222, 2, 0x1112)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4A1',
    )

    OP_6F(0x000A, 0)

    Jump('loc_4A8')

    def _loc_4A1(): pass

    label('loc_4A1')

    OP_6F(0x000A, 60)

    def _loc_4A8(): pass

    label('loc_4A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0222, 3, 0x1113)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4BA',
    )

    OP_6F(0x000B, 0)

    Jump('loc_4C1')

    def _loc_4BA(): pass

    label('loc_4BA')

    OP_6F(0x000B, 60)

    def _loc_4C1(): pass

    label('loc_4C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0222, 4, 0x1114)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4D3',
    )

    OP_6F(0x000C, 0)

    Jump('loc_4DA')

    def _loc_4D3(): pass

    label('loc_4D3')

    OP_6F(0x000C, 60)

    def _loc_4DA(): pass

    label('loc_4DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0222, 5, 0x1115)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4EC',
    )

    OP_6F(0x000D, 0)

    Jump('loc_4F3')

    def _loc_4EC(): pass

    label('loc_4EC')

    OP_6F(0x000D, 60)

    def _loc_4F3(): pass

    label('loc_4F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0222, 6, 0x1116)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_505',
    )

    OP_6F(0x000E, 0)

    Jump('loc_50C')

    def _loc_505(): pass

    label('loc_505')

    OP_6F(0x000E, 60)

    def _loc_50C(): pass

    label('loc_50C')

    OP_E0(0x08, 0xDA, 0x67, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0xD2, 0xA8, 0x02, 0x00)
    OP_E0(0x09, 0x64, 0x5B, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0xD2, 0xA8, 0x02, 0x00)
    OP_E0(0x0A, 0xF6, 0x73, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0xD2, 0xA8, 0x02, 0x00)

    Return()

# id: 0x0002 offset: 0x537
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_54C',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_54C(): pass

    label('loc_54C')

    Return()

# id: 0x0003 offset: 0x54D
@scena.Code('func_03_54D')
def func_03_54D():
    UnlockAchievement(0x02, 0x87, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0222, 0, 0x1110)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_62A',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0008, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大吃一惊曲奇饼'], 1)"),
            Expr.Return,
        ),
        'loc_5C1',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['大吃一惊曲奇饼']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1110)

    Jump('loc_627')

    def _loc_5C1(): pass

    label('loc_5C1')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['大吃一惊曲奇饼']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['大吃一惊曲奇饼']),
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

    def _loc_627(): pass

    label('loc_627')

    Jump('loc_65B')

    def _loc_62A(): pass

    label('loc_62A')

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
    def _loc_65B(): pass

    label('loc_65B')

    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6B5',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0014)"),
            Expr.Return,
        ),
        'loc_67A',
    )

    Jump('loc_6B5')

    def _loc_67A(): pass

    label('loc_67A')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['大吃一惊曲奇饼']),
            (TxtCtl.SetColor, 0x0),
            '的食谱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#480i的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6B5(): pass

    label('loc_6B5')

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x6BE
@scena.Code('func_04_6BE')
def func_04_6BE():
    UnlockAchievement(0x02, 0x88, 0x01, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0222, 1, 0x1111)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7DC',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0009, 0x0000001E)
    OP_73(0x0009)
    OP_6F(0x0009, 30)
    AddSepith(0x00, 0x000A)
    AddSepith(0x01, 0x000A)
    AddSepith(0x02, 0x000A)
    AddSepith(0x03, 0x000A)
    AddSepith(0x04, 0x000A)
    AddSepith(0x05, 0x000A)
    AddSepith(0x06, 0x000A)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1111)

    Jump('loc_7F6')

    def _loc_7DC(): pass

    label('loc_7DC')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_7F6(): pass

    label('loc_7F6')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x808
@scena.Code('func_05_808')
def func_05_808():
    UnlockAchievement(0x02, 0x89, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0222, 2, 0x1112)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8E5',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000A, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_87C',
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
    OP_A2(0x1112)

    Jump('loc_8E2')

    def _loc_87C(): pass

    label('loc_87C')

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

    def _loc_8E2(): pass

    label('loc_8E2')

    Jump('loc_916')

    def _loc_8E5(): pass

    label('loc_8E5')

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
    def _loc_916(): pass

    label('loc_916')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x924
@scena.Code('func_06_924')
def func_06_924():
    UnlockAchievement(0x02, 0x8A, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0222, 3, 0x1113)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A01',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000B, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_998',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1113)

    Jump('loc_9FE')

    def _loc_998(): pass

    label('loc_998')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x000B, 60)
    OP_70(0x000B, 0x00000000)

    def _loc_9FE(): pass

    label('loc_9FE')

    Jump('loc_A32')

    def _loc_A01(): pass

    label('loc_A01')

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
    def _loc_A32(): pass

    label('loc_A32')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xA40
@scena.Code('func_07_A40')
def func_07_A40():
    UnlockAchievement(0x02, 0x8B, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0222, 4, 0x1114)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B1D',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000C, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['攻击１'], 1)"),
            Expr.Return,
        ),
        'loc_AB4',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['攻击１']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1114)

    Jump('loc_B1A')

    def _loc_AB4(): pass

    label('loc_AB4')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['攻击１']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['攻击１']),
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

    def _loc_B1A(): pass

    label('loc_B1A')

    Jump('loc_B4E')

    def _loc_B1D(): pass

    label('loc_B1D')

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
    def _loc_B4E(): pass

    label('loc_B4E')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xB5C
@scena.Code('func_08_B5C')
def func_08_B5C():
    UnlockAchievement(0x02, 0x8C, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0222, 5, 0x1115)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C39',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000D, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['银耳环'], 1)"),
            Expr.Return,
        ),
        'loc_BD0',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['银耳环']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1115)

    Jump('loc_C36')

    def _loc_BD0(): pass

    label('loc_BD0')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['银耳环']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['银耳环']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x000D, 60)
    OP_70(0x000D, 0x00000000)

    def _loc_C36(): pass

    label('loc_C36')

    Jump('loc_C6A')

    def _loc_C39(): pass

    label('loc_C39')

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
    def _loc_C6A(): pass

    label('loc_C6A')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xC78
@scena.Code('func_09_C78')
def func_09_C78():
    UnlockAchievement(0x02, 0x8D, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0222, 6, 0x1116)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E10',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000E, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0222, 7, 0x1117)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D5C',
    )

    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ChrTurnDirection(0x0008, 0x0000, 0)
    OP_91(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_0CCF')
    def lambda_0CCF():
        OP_91(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0CCF)

    @scena.Lambda('lambda_0CEA')
    def lambda_0CEA():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000258)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0CEA)

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
    Battle(0x00000391, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_D37'),
        (0x00000002, 'loc_D49'),
        (0x00000001, 'loc_D59'),
        (-1, 'loc_D5C'),
    )

    def _loc_D37(): pass

    label('loc_D37')

    OP_A2(0x1117)
    OP_6F(0x000E, 60)
    Sleep(500)

    Jump('loc_D5C')

    def _loc_D49(): pass

    label('loc_D49')

    OP_6F(0x000E, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_D59(): pass

    label('loc_D59')

    OP_B4(0x00)

    Return()

    def _loc_D5C(): pass

    label('loc_D5C')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['驱动１'], 1)"),
            Expr.Return,
        ),
        'loc_DAB',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['驱动１']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1116)

    Jump('loc_E0D')

    def _loc_DAB(): pass

    label('loc_DAB')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['驱动１']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['驱动１']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x000E, 60)
    OP_70(0x000E, 0x00000000)

    def _loc_E0D(): pass

    label('loc_E0D')

    Jump('loc_E3F')

    def _loc_E10(): pass

    label('loc_E10')

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
    def _loc_E3F(): pass

    label('loc_E3F')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000A offset: 0xE4D
@scena.Code('func_0A_E4D')
def func_0A_E4D():
    TalkBegin(0x00FF)
    ClearMapFlags(0x00000001)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有拉杆。是否扳动？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 0, 0x10A8)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 7, 0x10A7)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F8B',
    )

    Menu(
        0,
        260,
        200,
        1,
        (
            TXT(0x00, '拉到右边\n'),
            TXT(0x01, '拉到左边\n'),
            TXT(0x02, '不动\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F1E',
    )

    OP_6F(0x0006, 0)
    OP_70(0x0006, 0x0000003C)
    OP_22(0x00FA, 0x00, 0x64)
    OP_73(0x0006)
    OP_A2(0x10A8)
    Sleep(500)

    OP_6D(3880, 0, 135860, 1400)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 0x00000078)
    OP_22(0x00FB, 0x00, 0x64)
    OP_73(0x0001)
    Sleep(1000)

    Fade(500)
    OP_69(0x0000, 0x00000000)

    Jump('loc_F81')

    def _loc_F1E(): pass

    label('loc_F1E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F81',
    )

    OP_6F(0x0006, 100)
    OP_70(0x0006, 0x000000A0)
    OP_22(0x00FA, 0x00, 0x64)
    OP_73(0x0006)
    OP_A2(0x10A7)
    Sleep(500)

    OP_6D(3880, 0, 135860, 1400)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 0x00000078)
    OP_22(0x00FB, 0x00, 0x64)
    OP_73(0x0001)
    Sleep(1000)

    Fade(500)
    OP_69(0x0000, 0x00000000)

    def _loc_F81(): pass

    label('loc_F81')

    OP_69(0x0000, 0x00000258)

    Jump('loc_103E')

    def _loc_F8B(): pass

    label('loc_F8B')

    Menu(
        0,
        260,
        200,
        1,
        (
            TXT(0x00, '恢复原状\n'),
            TXT(0x01, '不动\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1037',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 0, 0x10A8)),
            Expr.Return,
        ),
        'loc_FDA',
    )

    OP_6F(0x0006, 60)
    OP_70(0x0006, 0x00000000)
    OP_22(0x00FA, 0x00, 0x64)
    OP_73(0x0006)
    OP_A3(0x10A8)

    Jump('loc_FFA')

    def _loc_FDA(): pass

    label('loc_FDA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 7, 0x10A7)),
            Expr.Return,
        ),
        'loc_FFA',
    )

    OP_6F(0x0006, 160)
    OP_70(0x0006, 0x00000064)
    OP_22(0x00FA, 0x00, 0x64)
    OP_73(0x0006)
    OP_A3(0x10A7)

    def _loc_FFA(): pass

    label('loc_FFA')

    Sleep(500)

    OP_6D(3880, 0, 135860, 1200)
    OP_6F(0x0001, 120)
    OP_70(0x0001, 0x00000000)
    OP_22(0x00FB, 0x00, 0x64)
    OP_73(0x0001)
    Sleep(1000)

    Fade(500)
    OP_69(0x0000, 0x00000000)

    def _loc_1037(): pass

    label('loc_1037')

    OP_69(0x0000, 0x00000258)
    def _loc_103E(): pass

    label('loc_103E')

    SetMapFlags(0x00000001)
    TalkEnd(0x00FF)

    Return()

# id: 0x000B offset: 0x1047
@scena.Code('func_0B_1047')
def func_0B_1047():
    TalkBegin(0x00FF)
    ClearMapFlags(0x00000001)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有拉杆。是否扳动？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 2, 0x10AA)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 1, 0x10A9)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1185',
    )

    Menu(
        0,
        260,
        200,
        1,
        (
            TXT(0x00, '拉到右边\n'),
            TXT(0x01, '拉到左边\n'),
            TXT(0x02, '不动\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1118',
    )

    OP_6F(0x0002, 0)
    OP_70(0x0002, 0x0000003C)
    OP_22(0x00FA, 0x00, 0x64)
    OP_73(0x0002)
    OP_A2(0x10AA)
    Sleep(500)

    OP_6D(-12270, 0, 174500, 1200)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 0x00000078)
    OP_22(0x00FB, 0x00, 0x64)
    OP_73(0x0003)
    Sleep(1000)

    Fade(500)
    OP_69(0x0000, 0x00000000)

    Jump('loc_117B')

    def _loc_1118(): pass

    label('loc_1118')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_117B',
    )

    OP_6F(0x0002, 100)
    OP_70(0x0002, 0x000000A0)
    OP_22(0x00FA, 0x00, 0x64)
    OP_73(0x0002)
    OP_A2(0x10A9)
    Sleep(500)

    OP_6D(-12270, 0, 174500, 1200)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 0x00000078)
    OP_22(0x00FB, 0x00, 0x64)
    OP_73(0x0003)
    Sleep(1000)

    Fade(500)
    OP_69(0x0000, 0x00000000)

    def _loc_117B(): pass

    label('loc_117B')

    OP_69(0x0000, 0x00000258)

    Jump('loc_1238')

    def _loc_1185(): pass

    label('loc_1185')

    Menu(
        0,
        260,
        200,
        1,
        (
            TXT(0x00, '恢复原状\n'),
            TXT(0x01, '不动\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1231',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 2, 0x10AA)),
            Expr.Return,
        ),
        'loc_11D4',
    )

    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)
    OP_22(0x00FA, 0x00, 0x64)
    OP_73(0x0002)
    OP_A3(0x10AA)

    Jump('loc_11F4')

    def _loc_11D4(): pass

    label('loc_11D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 1, 0x10A9)),
            Expr.Return,
        ),
        'loc_11F4',
    )

    OP_6F(0x0002, 160)
    OP_70(0x0002, 0x00000064)
    OP_22(0x00FA, 0x00, 0x64)
    OP_73(0x0002)
    OP_A3(0x10A9)

    def _loc_11F4(): pass

    label('loc_11F4')

    Sleep(500)

    OP_6D(-12270, 0, 174500, 1200)
    OP_6F(0x0003, 120)
    OP_70(0x0003, 0x00000000)
    OP_22(0x00FB, 0x00, 0x64)
    OP_73(0x0003)
    Sleep(1000)

    Fade(500)
    OP_69(0x0000, 0x00000000)

    def _loc_1231(): pass

    label('loc_1231')

    OP_69(0x0000, 0x00000258)
    def _loc_1238(): pass

    label('loc_1238')

    SetMapFlags(0x00000001)
    TalkEnd(0x00FF)

    Return()

# id: 0x000C offset: 0x1241
@scena.Code('func_0C_1241')
def func_0C_1241():
    TalkBegin(0x00FF)
    ClearMapFlags(0x00000001)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有拉杆。是否扳动？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 4, 0x10AC)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 3, 0x10AB)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1389',
    )

    Menu(
        0,
        260,
        200,
        1,
        (
            TXT(0x00, '拉到右边\n'),
            TXT(0x01, '拉到左边\n'),
            TXT(0x02, '不动\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1317',
    )

    OP_6F(0x0005, 0)
    OP_70(0x0005, 0x0000003C)
    OP_22(0x00FA, 0x00, 0x64)
    OP_73(0x0005)
    OP_A2(0x10AC)
    Sleep(500)

    OP_6D(-8090, -60, 183030, 1200)
    Sleep(300)

    OP_6F(0x0004, 0)
    OP_70(0x0004, 0x00000078)
    OP_22(0x00FB, 0x00, 0x64)
    OP_73(0x0004)
    Sleep(1000)

    Fade(500)
    OP_69(0x0000, 0x00000000)

    Jump('loc_137F')

    def _loc_1317(): pass

    label('loc_1317')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_137F',
    )

    OP_6F(0x0005, 100)
    OP_22(0x00FA, 0x00, 0x64)
    OP_70(0x0005, 0x000000A0)
    OP_73(0x0005)
    OP_A2(0x10AB)
    Sleep(500)

    OP_6D(-8090, -60, 183030, 1200)
    Sleep(300)

    OP_6F(0x0004, 0)
    OP_70(0x0004, 0x00000078)
    OP_22(0x00FB, 0x00, 0x64)
    OP_73(0x0004)
    Sleep(1000)

    Fade(500)
    OP_69(0x0000, 0x00000000)

    def _loc_137F(): pass

    label('loc_137F')

    OP_69(0x0000, 0x00000258)

    Jump('loc_1441')

    def _loc_1389(): pass

    label('loc_1389')

    Menu(
        0,
        260,
        200,
        1,
        (
            TXT(0x00, '恢复原状\n'),
            TXT(0x01, '不动\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_143A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 4, 0x10AC)),
            Expr.Return,
        ),
        'loc_13D8',
    )

    OP_6F(0x0005, 60)
    OP_70(0x0005, 0x00000000)
    OP_22(0x00FA, 0x00, 0x64)
    OP_73(0x0005)
    OP_A3(0x10AC)

    Jump('loc_13F8')

    def _loc_13D8(): pass

    label('loc_13D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 3, 0x10AB)),
            Expr.Return,
        ),
        'loc_13F8',
    )

    OP_6F(0x0005, 160)
    OP_70(0x0005, 0x00000064)
    OP_22(0x00FA, 0x00, 0x64)
    OP_73(0x0005)
    OP_A3(0x10AB)

    def _loc_13F8(): pass

    label('loc_13F8')

    Sleep(500)

    OP_6D(-8090, -60, 183030, 1200)
    Sleep(300)

    OP_6F(0x0004, 120)
    OP_70(0x0004, 0x00000000)
    OP_22(0x00FB, 0x00, 0x64)
    OP_73(0x0004)
    Sleep(1000)

    Fade(500)
    OP_69(0x0000, 0x00000000)

    def _loc_143A(): pass

    label('loc_143A')

    OP_69(0x0000, 0x00000258)
    def _loc_1441(): pass

    label('loc_1441')

    SetMapFlags(0x00000001)
    TalkEnd(0x00FF)

    Return()

# id: 0x000D offset: 0x144A
@scena.Code('func_0D_144A')
def func_0D_144A():
    SetMapFlags(0x00000080)
    ClearMapFlags(0x00000001)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有扳手。是否扳动？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 5, 0x10AD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14EE',
    )

    Menu(
        0,
        260,
        200,
        1,
        (
            TXT(0x00, '降下\n'),
            TXT(0x01, '不动\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14EB',
    )

    EventBegin(0x00)
    OP_6F(0x0007, 0)
    OP_70(0x0007, 0x0000003C)
    OP_22(0x00FA, 0x00, 0x64)
    OP_73(0x0007)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 0x000000FA)
    OP_22(0x00FC, 0x00, 0x64)
    OP_73(0x0000)
    OP_A2(0x10AD)
    SetMapFlags(0x00000001)
    EventEnd(0x03)

    Return()

    def _loc_14EB(): pass

    label('loc_14EB')

    Jump('loc_154F')

    def _loc_14EE(): pass

    label('loc_14EE')

    Menu(
        0,
        260,
        200,
        1,
        (
            TXT(0x00, '拉起\n'),
            TXT(0x01, '不动\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_154F',
    )

    EventBegin(0x00)
    OP_6F(0x0007, 60)
    OP_70(0x0007, 0x00000000)
    OP_22(0x00FA, 0x00, 0x64)
    OP_73(0x0007)
    OP_6F(0x0000, 250)
    OP_70(0x0000, 0x00000000)
    OP_22(0x00FC, 0x00, 0x64)
    OP_73(0x0000)
    OP_A3(0x10AD)
    SetMapFlags(0x00000001)
    EventEnd(0x03)

    Return()

    def _loc_154F(): pass

    label('loc_154F')

    OP_69(0x0000, 0x00000258)
    ClearMapFlags(0x00000080)
    SetMapFlags(0x00000001)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
